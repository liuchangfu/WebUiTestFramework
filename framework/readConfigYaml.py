import os
import yaml


def get_yaml():
    path = os.pardir + '\\testConfig\\config.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        cfg = f.read()
        text = yaml.load(cfg)
        return text


try:
    t1 = get_yaml()
    print(t1)
    print(t1['EMAIL'])
    print(t1['EMAIL'][0]['EMAIL_HOST'])
    print(t1['EMAIL'][1]['EMAIL_USER'])
    print(t1['EMAIL'][2]['EMAIL_PASSWORD'])
    print(t1['EMAIL'][3]['EMAIL_PASSWORD'])
except IndexError:
    print('超出边界')
