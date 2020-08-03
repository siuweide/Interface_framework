import jmespath

class OperaDepend(object):

    def split_data(self, data):
        case_id = data.split('>')[0]
        depend_key = data.split('>')[1]
        return case_id, depend_key

    def get_data(self, data, res):
        case_id, depend_key = self.split_data(data)
        data = jmespath.search(depend_key, res)
        return data

if __name__ == '__main__':
    test = OperaDepend()
    print(test.split_data('case>data[0].message'))

