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

# try:
#     t1 = GetYamlConfig.get_yaml_config()  # 静态方法无需实例化,直接用类名.方法名调用
#     print(t1)
#     print(t1['EMAIL'])
#     print(t1['EMAIL'][0]['EMAIL_HOST'])
#     print(t1['EMAIL'][1]['EMAIL_USER'])
#     print(t1['EMAIL'][2]['EMAIL_PASSWORD'])
# except IndexError:
#     print('超出边界')
