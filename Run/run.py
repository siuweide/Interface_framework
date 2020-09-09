import os
import unittest
from time import strftime
from Run.run_case import TestRunCaseDdt
from BeautifulReport import BeautifulReport

def go_on_run():
    base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    report_path = base_path + '/Reports/'
    now = strftime("%Y_%m_%d_%H_%M_%S")
    file_name = now + '.html'
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRunCaseDdt)
    runner = BeautifulReport(suite)
    runner.report(description='发布会接口自动化测试报告', filename=file_name, log_path=report_path)

if __name__ == '__main__':
    go_on_run()