import configparser
from datetime import datetime


def load_properties(file_path):
    config = configparser.ConfigParser()
    with open(file_path, 'r', encoding='utf-8') as f:
        file_content = '[DEFAULT]\n' + f.read()
    config.read_string(file_content)
    
    return dict(config['DEFAULT'])

def load_config():
    config = load_properties('config.properties')   
    config["begin"] = datetime.strptime(config["begin"], "%Y-%m-%d")
    config["end"] = datetime.strptime(config["end"], "%Y-%m-%d")
    config["gardes_max"] = int(config["gardes_max"])
    config["depth"] = int(config["depth"])
    config["debug"] = eval(config["debug"])
    return config
