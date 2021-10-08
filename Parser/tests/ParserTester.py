import unittest
import parser

import Parser


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        filename = "../../framework_tests/sample_yaml/t1_correct.yaml"
        t = Parser.Parser()
        self.assertEqual(t.read(path=filename), 1)

    def test_read_cisco_config(self):
        filename = "../../framework_tests/sample_yaml/t2_correct.yaml"
        t = Parser.Parser()
        self.assertEqual(t.read(path=filename), True)


if __name__ == '__main__':
    unittest.main()
