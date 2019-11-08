import os
import yaml

# 获取配置文件路径
path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testConfig', 'config.yaml')


class GetYamlConfig(object):
    """
    读取指定目录下的yaml配置文件
    """

    # 静态方法无需实例化,直接用类名.方法名调用
    @staticmethod
    def get_yaml_config():
        with open(path, 'r', encoding='utf-8') as f:
            cfg = f.read()
            text = yaml.load(cfg, Loader=yaml.FullLoader)
        return text

    def __getitem__(self, item):
        return self.get_yaml_config()[item]



# t1 = GetYamlConfig().get_yaml_config()
# print(t1['COOKES'])
# print(t1['COOKES'][0])
# print(t1['COOKES'][1])
# print(t1['COOKES'][2])
# print('-------------------------------------------')
# print(t1['COOKES'][0]['NAME1'])
# print(t1['COOKES'][0]['VAULE1'])
# print(t1['COOKES'][1]['NAME2'])
# print(t1['COOKES'][1]['VAULE2'])
# print(t1['COOKES'][2]['DOMAIN'])



