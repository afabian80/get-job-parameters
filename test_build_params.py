import unittest
from build_params import UrlReader

class TestBuildParams(unittest.TestCase):

    def test_url_read(self):
        url_reader = UrlReader()
        code, data = url_reader.read('http://www.google.com')
        self.assertEqual(code,200)


if __name__ == '__main__':
    unittest.main()
