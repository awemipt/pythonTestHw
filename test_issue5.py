import unittest
from unittest.mock import patch
from issue5 import what_is_year_now

class TestWhatIsYearNow(unittest.TestCase):

    @patch('issue5.urllib.request.urlopen')
    @patch('json.read')
    def test_year_now(self, mockload):
        mockload.return_value = {'currentDateTime': '2023-11-23'}
        result= what_is_year_now()
        self.assertEqual(result, 2023)


if __name__ == "__main__":
    unittest.main()