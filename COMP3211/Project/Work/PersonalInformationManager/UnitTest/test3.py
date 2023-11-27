import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
parent_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_path)
path = os.path.join(parent_path,"model")
sys.path.append(path)
from model.PIRCollection import PIRCollection

class PIMTest(unittest.TestCase):
    def setUp(self) :
        self.text = "hi"
        self.time = "2023/12/01 23:59"
        
    def test_matches_text(self):
        collection = PIRCollection()
        search_type = 1
        collection.updateSearchType(search_type)
        collection.matches_type()
        expected_result = ["hi"]
        result = collection.matches_text(self.text)
        self.assertEqual(expected_result, result)
    def test_matches_time(self):
        collection = PIRCollection()
        search_type = 2
        collection.updateSearchType(search_type)
        collection.matches_type()



if __name__ == '__main__':
    unittest.main()