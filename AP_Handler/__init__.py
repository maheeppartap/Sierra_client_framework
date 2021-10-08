import string
from . import security_options

"""
    Naming scheme: 
    - all virtual functions will be have a leading underscore before their name, like _change_security. This denotes a function
    to be implemented in a child class
    
"""


class APHandler:
    """
    This is designed to be the parent class of all APs. This class will be inherited by all third party APs, including
    Lexus. I will be treating Lexus same as all APs because this framework can be used for future non lexus APs as well.
    """

    def __init__(self, ssid="", security="", curr_pmf="", curr_broadcasting=False):
        self.curr_ssid = ssid
        self.curr_security = security
        self.curr_pmf = curr_pmf
        self.curr_broadcasting = curr_broadcasting

    def _change_security(self, sec: security_options):
        raise NotImplementedError()

    def _change_ssid(self, SSID: string):
        raise NotImplementedError()

    @staticmethod
    def _verify_config(config: dict):
        raise NotImplementedError()

    def _create_config(self, raw_data: dict):
        pass

    def _unpack_data(self, raw_data: dict):
        raise NotImplementedError()

    # todo: Add more functions as we go, for now let's keep it simple and confined to 2 things
