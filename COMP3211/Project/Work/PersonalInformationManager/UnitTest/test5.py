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
        self.strings_to_remove = ["ly"]
        self.not_ornot = "-"

    def test_findIndex(self):
        pirCollection = PIRCollection()
        result = pirCollection.findIndex(self.searchType)
        expected_result = 0
        self.assertEqual(expected_result,result) 

    def test_not_included_file(self):
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.not_included_file(self.strings_to_remove)
        expected_result = ["hi","hihihi","11111","no","hello world"]   
        self.assertEqual(expected_result,result)    

    def test_not_ornot_filter_text(self):
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.not_ornot_filter_text(self.not_ornot,"ly")
        expected_result = ["hi","hihihi","11111","no","hello world"]   
        self.assertEqual(expected_result,result)  
        self.not_ornot = "+"
        result = pirCollection.not_ornot_filter_text(self.not_ornot,"hi")
        expected_result = ["hi"]
        self.assertEqual(expected_result,result) 

    def test_not_ornot_filter_time(self):
        pirCollection = PIRCollection()
        self.searchType = 2
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.not_ornot_filter_time(self.not_ornot,"2023/11/01 23:59","<")    
        expected_result = ["Assignment 2,2023/11/01 23:59","Assignment 3,2023/11/29 23:59",
                           "Group Report,2023/12/01 23:59", "Group Presentation,2023/12/01 23:59", 
                           "Group Meeting,2023/12/01 23:59"]   
        self.assertEqual(expected_result,result) 
        self.not_ornot = "+"
        result = pirCollection.not_ornot_filter_time(self.not_ornot,"2023/11/01 23:59","<")
        expected_result = ["Assignment 1,2023/10/01 23:59"]
        self.assertEqual(expected_result,result) 

    def test_get_index(self):
        pirCollection = PIRCollection()
        pirCollection.updateSearchType(self.searchType)
        pirCollection.matches_type()
        result = pirCollection.get_index(["hi"])
        expected_result = [3]
        self.assertEqual(expected_result,result)

    def test_checkDateFormat(self):
        pirCollection = PIRCollection()
        date = "2023/11/01 23:59"
        result = pirCollection.checkDateFormat(date)
        expected_result = True
        self.assertEqual(expected_result,result)







if __name__ == '__main__':
    unittest.main()          
