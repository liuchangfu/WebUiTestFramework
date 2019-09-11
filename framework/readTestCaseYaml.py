# _*_ coding:utf-8 _*_
import os
import yaml


def get_yaml():
    path = os.pardir + '\\testConfig\\testcase.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        text = yaml.load(cfg)
        return text


t1 = get_yaml()
print(t1)
