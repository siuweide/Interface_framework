import os
import xlrd

class OperaExcel(object):

    def __init__(self, excel_path=None):
        base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        if excel_path == None:
            excel_path = base_path + "/Case/test_case.xlsx"
        self.open_excel = xlrd.open_workbook(excel_path)

    def _get_sheet_data(self, index=None):
        if index == None:
            index = 0
        elif not isinstance(index, int):
            raise ValueError('index must be ini')
        data = self.open_excel.sheet_by_index(index)
        return data

    def get_rows(self):
        # 获取有效总行数
        nrows = self._get_sheet_data().nrows
        return nrows

    def get_cols(self):
        # 获取有效总列数
        ncols = self._get_sheet_data().ncols
        return ncols

    def get_row_value(self, row):
        # 获取每一行的内容
        if not isinstance(row, int):
            raise ValueError('row must be int')
        data = self._get_sheet_data().row_values(row)
        return data

    def get_excel_value(self):
        nrows = self.get_rows()
        values_line = []
        for i in range(1, nrows):
            value = self.get_row_value(i)
            values_line.append(value)
        return values_line

if __name__ == '__main__':
    test = OperaExcel()
    print(test.get_excel_value())