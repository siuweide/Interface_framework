import json
import unittest
from ddt import ddt, data
from Until.opera_ini import OperaIni
from Until.opera_excel import OperaExcel
from Base.base_request import BaseRequest
from Until.verification import verification_result


@ddt
class TestRunCaseDdt(unittest.TestCase):

    cases_data = OperaExcel().get_excel_value()

    def setUp(self) -> None:
        self.opera_ini = OperaIni()
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
        data = json.loads(cases_data[7])
        is_cookie = cases_data[8]
        headers = cases_data[9]
        expect_result = cases_data[10]
        if headers == '':
            headers = None
        if is_run == 'yes':
            res = self.request.run_method(method, url, headers, data=data)
            if verification_result(expect_result, res):
                print('测试成功')

if __name__ == '__main__':
    unittest.main()