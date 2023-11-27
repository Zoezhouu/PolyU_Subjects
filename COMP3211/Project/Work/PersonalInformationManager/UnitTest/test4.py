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
    def setUp(self):
        self.searchType = 1
        self.text_criteria = "hello"
        self.time_criteria = "2023/12/01 23:59"
        self.condition = "="

    def matches_type(self):
        pirCollection = PIRCollection()   
        pirCollection.updateSearchType(self.searchType)
        result = pirCollection.matches_type()
        expected_result = ["ly","hi","hihihi","11111","hello world"]
        self.assertEqual(expected_result,result) 

    def test_matches_text(self):
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.matches_text(self.text_criteria)
        expected_result = ["hello world"]
        self.assertEqual(expected_result, result)

    def test_matches_time(self):
        self.searchType = 2
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.matches_time(self.time_criteria,self.condition)
        expected_result = ["Group Report,2023/12/01 23:59","Group Presentation,2023/12/01 23:59","Group Meeting,2023/12/01 23:59"]
        self.assertEqual(expected_result,result)
    
    def test_updateSearchType(self):
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        expected_result = self.searchType
        self.assertEqual(expected_result,pirCollection.searchType)





if __name__ == '__main__':
    unittest.main()        