"""
This code will parse the yaml files. Will include a lexical analyzer and parser to check for wrong input. That's it.
"""
import inspect
import string

import yaml


class Parser:
    def __init__(self):
        pass

    def read(self, path: string):
        print("opening file: ", path, "\n")
        with open(path) as file:
            r = yaml.load(file, Loader=yaml.FullLoader)
        # print(r)
        self.verify(data=r)

        return r

    def verify(self, data: dict):
        """
        Will return true if data is well formed. To support different APs, this function will call some derived function
        inside the APs implementation to check if the requested configuration is compatible or not.
        The AP's verify function is expected to
        :param data: dict read from config yaml
        :return:
        """
        import Helpers as hp
        for i in data.keys():
            if i == "steps":
                continue
            try:
                print(f'{hp.__AP__(i)._verify_config(data.get(i))}')
            except AttributeError:
                print(f'{self.__class__.__name__}, line {inspect.currentframe().f_lineno}: {i} is not implemented')
