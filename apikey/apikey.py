import pathlib
import configparser


def save_apikey(service: str, apikey: str, filename: str = None):
    if filename is None:
        filename = f"{pathlib.Path.home()}/.apikey-store"
    config = configparser.ConfigParser()
    config[service] = {}
    config[service]['api-key'] = apikey
    with open(filename, 'w') as fileptr:
        config.write(fileptr)
    return None


def read_apikey(service: str, filename: str = None) -> str:
    if filename is None:
        filename = f"{pathlib.Path.home()}/.apikey-store"
    config = configparser.ConfigParser()
    config.read(filename)
    return config[service]['api-key']
