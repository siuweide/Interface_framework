import json
import pytest
import allure

from Until.opera_ini import OperaIni
from Until.opera_excel import OperaExcel
from Base.base_request import BaseRequest
from Until.opera_cookies import OperaCookie
from Until.opera_depend import OperaDepend
from Until.verification import verification_result



class TestRunCaseDdt():

    cases_data = OperaExcel().get_excel_value()

    opera_excel = OperaExcel()
    opera_ini = OperaIni()
    opera_cookies = OperaCookie()
    request = BaseRequest()
    opera_depend = OperaDepend()
    base_url = opera_ini.get_ini_data('test', 'host')


    @pytest.mark.parametrize('case_id, case_name, is_run, is_depend, depend_key, url, method, '
                             'data, is_cookie, headers, expect_result, actual_result, response', cases_data)
    def test_cases(self, case_id, case_name, is_run, is_depend, depend_key, url, method,
                   data, is_cookie, headers, expect_result, actual_result, response):

        allure.dynamic.title(case_name)
        try:
            case_data = json.loads(data)
        except Exception:
            case_data = None
        row = self.opera_excel.get_case_row(case_id)
        if headers == '':
            headers = None
        if is_run == 'yes':
            if is_cookie == 'write':
                res = self.request.run_method(method, self.base_url+url, headers, data=case_data)
                # 将cookies写入cookies文件
                self.opera_cookies.write_cookies(res)
            elif is_cookie == 'read' or is_cookie == '':
                if is_depend:
                    # 获取依赖接口的数据
                    depend_data = self.opera_depend.get_depend_data(is_depend)
                    try:
                        case_data[depend_key] = depend_data
                    except Exception:
                        case_data = None
                # 读取cookies文件的cookies
                cookies = self.opera_cookies.read_cookies()
                res = self.request.run_method(method, self.base_url+url, headers, cookies=cookies, data=case_data)
            if verification_result(expect_result, res):
                self.opera_excel.write_actual_res_result(row, '测试成功', res.text)
            else:
                self.opera_excel.write_actual_res_result(row, '测试失败', res.text)

if __name__ == '__main__':
    pytest.main()