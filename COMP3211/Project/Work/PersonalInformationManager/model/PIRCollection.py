import os
from datetime import datetime

class PIRCollection:
    def __init__(self):
        self.searchType = "All"
        self.record_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'records.pim')
        self.include_or_not = False
        self.operator = "&&"
        self.type_content = None
        self.not_ornot = ""
    
    def matches_text(self,text_criteria):
        found_lines = []
        for line in self.type_content:
            line = line.strip()
            parts = line.split(",")
            parts1 = line.split(" ")
            if text_criteria in parts or text_criteria in parts1:
                found_lines.append(line)
        return found_lines
    def matches_time(self,time_criteria,condition):
        found_lines = []
        for line in self.type_content:
            parts = line.split(",")
            for part in parts:
                if not self.checkDateFormat(part.strip()):
                    continue               
                time = datetime.strptime(time_criteria.strip(),"%Y/%m/%d %H:%M")
                value = datetime.strptime(part.strip(),"%Y/%m/%d %H:%M")
                condition = condition
                if condition == "<" and value < time:
                    found_lines.append(line.strip())
                elif condition == ">" and value > time:
                    found_lines.append(line.strip())
                elif condition == "=" and value == time:
                    found_lines.append(line.strip())
                else:
                    pass
        return found_lines
        
    # update search type        
    def updateSearchType(self, searchType):
        self.searchType = searchType
    
    # find line index range of searched PIR type
    def findIndex(self, searchType):
        with open(self.record_path, "r") as file:
            lines = file.readlines()
        if searchType == 1:
            word_to_find = "Note"
        elif searchType == 2:
            word_to_find = "Task"
        elif searchType == 3:
            word_to_find = "Contact"
        elif searchType == 4:
            word_to_find = "Event"
        else:
            word_to_find = "End"
        for i, line in enumerate(lines):
            if word_to_find in line:
                index = i
                return index

    # match type
    def matches_type(self):
        with open(self.record_path, "r") as file:
            lines = file.readlines()
            if self.searchType == 1 or self.searchType == 2 or self.searchType == 3 or self.searchType == 4:
                self.type_content = lines[self.findIndex(self.searchType)+2:self.findIndex(self.searchType+1)]
            else:
                self.type_content = lines
        return self.type_content
    
    # check if included in file
    def not_included_file(self,strings_to_remove):
        found_lines = []
        for line in self.type_content:
            if not any(string in line for string in strings_to_remove):
                found_lines.append(line.rstrip())
        return found_lines
    
    def not_ornot_filter_text(self,not_ornot,text_criteria):
        if not_ornot == "-":
            return self.not_included_file(self.matches_text(text_criteria))
        else:
            return self.matches_text(text_criteria)


    def not_ornot_filter_time(self,not_ornot,time_criteria,condition):
        if not_ornot == "-":
            return self.not_included_file(self.matches_time(time_criteria,condition))
        else:
            return self.matches_time(time_criteria,condition)

    def get_index(self,found_lines):
        with open(self.record_path, 'r') as file:
            lines = file.readlines()
        index_list = []
        for index, line in enumerate(lines):
            line = line.strip()
            for found_line in found_lines:
                if found_line == line:
                    index_list.append(index)
        return index_list
    
    #  delete a line from lines list, then copy left lines into file
    def delete(self,line_number_list):
        with open(self.record_path, 'r') as file:
            lines = file.readlines()
        for line_number in sorted(line_number_list,reverse=True):
            if line_number > 0 and line_number <= len(lines):
                del lines[line_number]
        with open(self.record_path, 'w') as file:
            file.writelines(lines)       

    def checkDateFormat(self,date):
        if date is None:
            return False
        date_format = "%Y/%m/%d %H:%M"
        try:
            datetime.strptime(date.strip(), date_format)
        except ValueError:
            return False
        return True

    def replace_global(self,search_text, replace_text):
        with open(self.record_path,'r') as file:
            data = file.read()
            data = data.replace(search_text, replace_text)
        with open(self.record_path,'w') as file:
            file.write(data)

    def replace_specific(self,search_text, replace_text,line_number_list):
        with open(self.record_path,'r') as file:
            data = file.readlines()
        for line_number in line_number_list:
            data[line_number] = data[line_number].replace(search_text,replace_text)
        with open(self.record_path,'w') as file:
            file.writelines(data)

    def insert(self,line_text, line_index):
        # Read the existing contents of the file
        with open(self.record_path, 'r') as file:
            lines = file.readlines()

        # Insert the new line at the specified position
        lines.insert(line_index , line_text + '\n')

        # Write the modified contents back to the file
        with open(self.record_path, 'w') as file:
            file.writelines(lines)
