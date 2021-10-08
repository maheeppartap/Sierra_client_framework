import string
import paramiko

from AP_Handler import APHandler, security_options
from abc import ABC


class Lexus(APHandler, ABC):
    def _change_security(self, sec: security_options):
        pass

    def _change_ssid(self, SSID: string):
        pass

    @staticmethod
    def _verify_config(config: dict):
        pass

    def _create_config(self, raw_data: dict):
        super()._create_config(raw_data)

    def _unpack_data(self, raw_data: dict):
        pass

    def __init__(self):
        super().__init__()
