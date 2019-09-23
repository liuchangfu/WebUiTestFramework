# _*_ coding:utf-8 _*_
import os
import yaml


class GetTestCaseYamlConfig(object):
    """
    静态方法由类调用，无默认参数。将实例方法参数中的self去掉，然后在方法定义上方加上@staticmethod，就成为静态方法。
    它属于类，和实例无关。建议只使用类名.静态方法的调用方式。
    """

    @staticmethod
    def get_testcase_yaml_config():
        path = os.pardir + '\\testConfig\\testcase.yaml'
        with open(path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            text = yaml.load(cfg)
        return text

    def __getitem__(self, item):
        return self.get_testcase_yaml_config()[item]


# t1 = GetTestCaseYamlConfig.get_testcase_yaml_config()  # 静态方法无需实例化,直接用类名.方法名调用
# print(t1)
# print(t1[0])
# print(t1[0]['username'])
# print(t1[0]['password'])
# print(t1[1])
print(t1[2])
