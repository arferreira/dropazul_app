import json
import os
__BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def get_settings_development():
    """
    Pegando o arquivo de configuração e devolvendo como um objeto Json
    :return:
    """
    with open("{0}/{1}".format(__BASE_DIR, "settings_development.json")) as data_file:
        data = json.load(data_file)
    return data


def get_settings_production():
    """
    Pegando o arquivo de configuração e devolvendo como um objeto Json
    :return:
    """
    with open("{0}/{1}".format(__BASE_DIR, "settings_production.json")) as data_file:
        data = json.load(data_file)
    return data
