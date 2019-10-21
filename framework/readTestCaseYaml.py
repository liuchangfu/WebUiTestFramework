# _*_ coding:utf-8 _*_
import os
import yaml

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testConfig', 'testcase.yaml')
print(path)


class GetTestCaseYamlConfig(object):
    """
    读取指定的目录的yaml格式的测试用例
    """

    # 静态方法无需实例化,直接用类名.方法名调用
    @staticmethod
    def get_testcase_yaml_config():
        with open(path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            text = yaml.load(cfg, Loader=yaml.FullLoader)
        return text

    def __getitem__(self, item):
        return self.get_testcase_yaml_config()[item]

# t1 = GetTestCaseYamlConfig.get_testcase_yaml_config()  # 静态方法无需实例化,直接用类名.方法名调用
# print(t1)
# print(t1[0])
# print(t1[0]['username'])
# print(t1[0]['password'])
# print(t1[1])
# print(t1[2])
