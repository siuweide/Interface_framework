import json
import jmespath
from Until.opera_excel import OperaExcel


class OperaDepend(object):

    # 1、读取前置条件的值
    # 2、获取到它是依赖哪个case
    # 3、找到那个case的行数，并且读取它的响应结果
    # 4、使用Jmespath方法，传入depend_key，和依赖用例的响应结果
    # 5、获取到值后，将修改data的值

    def __init__(self):
        self.opera_excel = OperaExcel()

    def split_data(self, data):
        case_id = data.split('>')[0]
        depend_key = data.split('>')[1]
        return case_id, depend_key

    def get_depend_data(self, data):
        case_id, depend_key = self.split_data(data)
        row = self.opera_excel.get_case_row(case_id)
        row_values = self.opera_excel.get_row_value(row)
        # 获取响应结果
        res_result = json.loads(row_values[12])
        depend_data = jmespath.search(depend_key, res_result)
        return depend_data

if __name__ == '__main__':
    test = OperaDepend()
    print(test.get_data('case_03>data[0].id'))

