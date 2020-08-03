import json
import unittest
from ddt import ddt, data

from Until.opera_cookies import OperaCookie
from Until.opera_ini import OperaIni
from Until.opera_excel import OperaExcel
from Base.base_request import BaseRequest
from Until.verification import verification_result


@ddt
class TestRunCaseDdt(unittest.TestCase):

    cases_data = OperaExcel().get_excel_value()

    def setUp(self) -> None:
        self.opera_excel = OperaExcel()
        self.opera_ini = OperaIni()
        self.opera_cookies = OperaCookie()
        self.request = BaseRequest()
        self.base_url = self.opera_ini.get_ini_data('test', 'host')

    @data(*cases_data)
    def test_cases(self, cases_data):
        case_id = cases_data[0]
        is_run = cases_data[2]
        is_depend = cases_data[3]
        depend_key = cases_data[4]
        url = self.base_url + cases_data[5]
        method = cases_data[6]
        try:
            data = json.loads(cases_data[7])
        except Exception:
            data = None
        is_cookie = cases_data[8]
        headers = cases_data[9]
        expect_result = cases_data[10]
        row = self.opera_excel.get_data_row(case_id)
        if headers == '':
            headers = None
        if is_run == 'yes':
            if is_cookie == 'write':
                res = self.request.run_method(method, url, headers, data=data)
                # 将cookies写入cookies文件
                self.opera_cookies.write_cookies(res)
            elif is_cookie == 'read':
                if is_depend:
                    # 1、读取前置条件的值
                    # 2、获取到它是依赖哪个case
                    # 3、找到那个case的行数，并且读取它的响应结果
                    # 4、使用Jmespath方法，传入depend_key，和依赖用例的响应结果
                    # 5、获取到值后，将修改data的值
                    pass
                # 读取cookies文件的cookies
                cookies = self.opera_cookies.read_cookies()
                res = self.request.run_method(method, url, headers, cookies=cookies, data=data)
            if verification_result(expect_result, res):
                self.opera_excel.write_actual_res_result(row, '测试成功', res.text)
            else:
                self.opera_excel.write_actual_res_result(row, '测试失败', res.text)

if __name__ == '__main__':
    unittest.main()