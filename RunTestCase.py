# _*_ coding:utf-8 _*_
# author:Administrator
# datetime:2020/4/28 18:19
import sys
import pytest
from config.conf import ROOT_DIR, HTML_NAME, REPORT_DIR, CURRENT_DATE


def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--reruns', '1', '--html=' + './testReports/' + HTML_NAME]
    pytest.main(args)


if __name__ == '__main__':
    main()
