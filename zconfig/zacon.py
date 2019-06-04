import configparser
import os
import ast
from zacon.constant import *


class ServiceConfig():
    def __init__(self, config_dir='./conf'):
        self._config_dir = config_dir
        self._getConfigDirectory()
        try:
            env = os.environ['SERVICE_ENV_SETTING']
            assert env in ["DEVELOPMENT", "PRODUCTION", "STAGING"]
        except:
            raise ValueError(
                "The environment param `SERVICE_ENV_SETTING` need to be assigned as: DEVELOPMENT | PRODUCTION | STAGING")

        if env == 'DEVELOPMENT':
            self.conf = self._development()
        elif env == 'STAGING':
            self.conf = self._staging()
        elif env == 'PRODUCTION':
            self.conf = self._production()

    def _development(self):
        configParser = configparser.ConfigParser()
        configParser.read(self._dev_config_paths)
        return configParser

    def _staging(self):
        configParser = configparser.ConfigParser()
        configParser.read(self._stag_config_paths)
        return configParser

    def _production(self):
        configParser = configparser.ConfigParser()
        configParser.read(self._prod_config_paths)
        return configParser

    def _getConfigDirectory(self):
        self._dev_config_paths = os.path.join(self._config_dir, DEV_FILENAME)
        self._prod_config_paths = os.path.join(self._config_dir, PROD_FILENAME)
        self._stag_config_paths = os.path.join(self._config_dir, STAG_FILENAME)
        for f in [self._dev_config_paths, self._prod_config_paths, self._stag_config_paths]:
            if not os.path.exists(f):
                raise FileNotFoundError("File not found: {}".format(f))

    def getString(self, block, key, default=None):
        return str(self.conf[block][key])

    def getInt(self, block, key, default=0):
        if self.conf[block][key] is None:
            return default
        return int(self.conf[block][key])

    def getFloat(self, block, key, default=0.0):
        if self.conf[block][key] is None:
            return default
        return float(self.conf[block][key])

    def getBool(self, block, key, default=0.0):
        if self.conf[block][key] is None:
            return default
        return bool(self.conf[block][key])

    def getList(self, block, key, default=[]):
        if self.conf[block][key] is None:
            return default
        return ast.literal_eval(self.conf[block][key])