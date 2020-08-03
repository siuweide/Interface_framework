import os
import configparser

class OperaIni(object):
    def __init__(self, file_path=None):
        if file_path == None:
            file_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.config = configparser.ConfigParser()
        self.config.read(file_path + '/Config/server.ini')

    def get_ini_data(self, title, value):
        data = self.config.get(title, value)
        return data

if __name__ == '__main__':
    test = OperaIni()
    print(test.get_ini_data('test', 'host'))

