"""
    This is the entrypoint
"""
from Parser import Parser
import Helpers


def begin_test(data):
    # print(f'{data}')

    # This will be a list containing tuples of device name and reference to their classes
    device_classes = []
    for key in data.keys():
        try:
            obj = Helpers.__AP__(key)()
            obj._create_config(data[key])
            device_classes.append((key, Helpers.__AP__(key)))
        except AttributeError or TypeError:
            print(f'begin_test: {key} is not implemented')
        print(f'class {key}: {Helpers.__AP__(key)}')


def main():
    # Step 1: call the parser to read the configuration and verify
    x = Parser()

    # Read the raw data into the dictionary. read() will contact the AP classes and verify if the data is  valid
    raw_data = x.read(path="framework_tests/sample_yaml/t2_correct.yaml")

    begin_test(raw_data)


if __name__ == "__main__":
    main()
