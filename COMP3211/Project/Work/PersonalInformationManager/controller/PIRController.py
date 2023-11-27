import sys
import os
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from model.PIRNote import Note
from model.PIRTask import Task
from model.PIREvent import Event
from model.PIRContact import Contact
from model.PIRCollection import PIRCollection
from View.PIRView import PIRView
from View.InputView import Command
from View.OutputView import Board
from View.PIRView import PIRView

class PIRController:
    def main(self):
        while True:
            board = Board()
            enter = Command()
            board.mainBoard()
            activity = enter.mainCommand()
            if self.check_int(activity):
                activity = int(activity)
                if activity == 1:
                    self.create()
                elif activity == 2:
                    self.search()
                elif activity == 3:
                    self.modify()
                elif activity == 4:
                    self.delete()
                elif activity == 5:
                    self.display()
                elif activity == 6:
                    sys.exit(0)
            else:
                board.getValidInput()
     
    def create(self):
        while True:
            enter = Command()
            board = Board()
            board.createBoard() 
            command = enter.createCommand()
            if self.check_int(command):
                pircollection = PIRCollection()
                command = int(command)
                if command in range(1,6):
                    break
                else:
                    board.getValidInput()
            else:
                board.getValidInput()

        if command == 1: # Note
            get_content = enter.createNoteCommand()
            note = Note('')
            note.setNote(get_content)
            pircollection.insert(note.NoteToPIR(),pircollection.findIndex(2))
            board.successCreate()
        elif command == 2: #Task
            get_date = enter.getDateTaskCommand()
            while not pircollection.checkDateFormat(get_date):
                board.getValidInput()
                get_date = enter.getDateTaskCommand()
            date = get_date
            taskItem = enter.createTaskTextCommand()
            task = Task('','')
            task.setTask(taskItem,date)
            pircollection.insert(task.TaskToPIR(), pircollection.findIndex(3))
            board.successCreate()
        elif command == 3: # Contact
            get_name = enter.createContactNameCommand()
            get_addr = enter.createContactAddrCommand()
            while True:
                get_mobileNum = enter.createContactMobileNumCommand()
                if get_mobileNum.isnumeric():
                    break
                else:
                    board.getValidInput()
            contact = Contact("","","")
            contact.setContact(get_name, get_addr,get_mobileNum)
            pircollection.insert(contact.ContactToPIR(), pircollection.findIndex(4))
            board.successCreate()
        elif command == 4: # Event
            get_description = enter.createEventDescCommand()
            get_start_time = enter.getDateStartCommand()
            while not pircollection.checkDateFormat(get_start_time):
                board.getValidInput()
                get_start_time = enter.getDateStartCommand()
            get_alarm = enter.getDateAlarmCommand()
            while not pircollection.checkDateFormat(get_alarm):
                board.getValidInput()
                get_alarm = enter.getDateAlarmCommand()
            event = Event('','','')
            event.setEvent(get_description, get_start_time, get_alarm)
            pircollection.insert(event.EventToPIR(), pircollection.findIndex("End"))
            board.successCreate()
        else:
            self.main()



    def search(self):
        enter = Command()
        board = Board() 
        board.searchTypeBoard()
        pircollection = PIRCollection()
        while True:
            searchType = int(enter.searchTypeCommand())
            if self.check_int(searchType):
                searchType = int(searchType)
                if searchType in range(1,6):
                    pircollection.updateSearchType(searchType)                  
                elif searchType == 6:
                    self.main()
                else:
                   board.getValidInput() 
                break
            else:
                board.getValidInput()
        pircollection.matches_type()

        # Search Note, Contact
        if pircollection.searchType == 1 or pircollection.searchType == 3:
            while True:
                board.searchFilterForNoteContact()
                search_filter = enter.get_search_filterNoteContact()
                if self.check_int(search_filter):
                    search_filter = int(search_filter)
                    if search_filter in range(1,3):
                        break
                    else:
                        board.getValidInput()
                else:
                    board.getValidInput()

            #search with single text
            if search_filter == 1:
                text_condition = enter.get_logical_condition_text()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        text_condition.insert(0,"-")
                        break
                    elif include_or_not == "":
                        text_condition.insert(0,"+")
                        break
                    else:
                        board.getValidInput() 
                found_list =  pircollection.not_ornot_filter_text(text_condition[0],text_condition[1])         
                print(found_list)
                print(pircollection.get_index(found_list))
                return found_list
            else:
            #search with combined logic
                text_conditions = []
                operators = []
                # include_or_not
                while True:
                    text_condition = enter.get_logical_condition_text()
                    while True:
                        include_or_not = enter.get_include_or_not()
                        if include_or_not == "!":
                            text_condition.insert(0,"-")
                            break
                        elif include_or_not == "":
                            text_condition.insert(0,"+")
                            break
                        else: 
                            board.getValidInput()                   
                    text_conditions.append(text_condition)
                    while True:
                        operator = enter.get_operator()
                        if operator == "||" or operator == "&&":
                            operators.append(operator)
                            break
                        if operator == "":
                            break
                        else:
                            board.getValidInput()
                    if operator == "":
                        break
                filtered_list = []
                for text_condition in text_conditions:
                    filtered_list.append(pircollection.not_ornot_filter_text(text_condition[0],text_condition[1]))     
                found_list = self.get_union_or_intersection(filtered_list,operators)       
                print(pircollection.get_index(found_list))
                return found_list

        
        # Search Task, Event
        else:
            while True:
                board.searchFilterForTaskEvent()
                search_filter = enter.get_search_filterTaskEvent()
                if self.check_int(search_filter):
                    search_filter = int(search_filter)
                    if search_filter in range(1,4):
                        break
                    else:
                        board.getValidInput()
                else:
                    board.getValidInput()
            #search with single text
            if search_filter == 1:
                text_condition = enter.get_logical_condition_text()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        text_condition.insert(0,"-")
                        break
                    elif include_or_not == "":
                        text_condition.insert(0,"+")
                        break
                    else:
                        board.getValidInput() 
                found_list =  pircollection.not_ornot_filter_text(text_condition[0],text_condition[1])         
                print(found_list)
                print(pircollection.get_index(found_list))
                return found_list
            #search with single time
            elif search_filter == 2:
                time_condition = enter.get_logical_condition_time()
                while True:
                    include_or_not = enter.get_include_or_not()
                    if include_or_not == "!":
                        not_ornot = "-"
                        break
                    elif include_or_not == "":
                        not_ornot = "+"
                        break
                    else:
                        board.getValidInput()   
                found_list =  pircollection.not_ornot_filter_time(not_ornot,time_condition[0],time_condition[1]) 
                print(found_list)
                print(pircollection.get_index(found_list))  
                return found_list
            #search with combined logic
            else:
                conditions = []
                operators = []
                while True:
                    condition = enter.get_logical_condition_withtime()
                    while True:
                        include_or_not = enter.get_include_or_not()
                        if include_or_not == "!":
                            condition.insert(0,"-")
                            break
                        elif include_or_not == "":
                            condition.insert(0,"+")
                            break
                        else: 
                            board.getValidInput()                   
                    conditions.append(condition)
                    while True:
                        operator = enter.get_operator()
                        if operator == "||" or operator == "&&":
                            operators.append(operator)
                            break
                        if operator == "":
                            break
                        else:
                            board.getValidInput()                    
                    if operator == "":
                        break
                filtered_list = []
                for condition in conditions:
                    if len(condition) == 3:
                        filtered_list.append(pircollection.not_ornot_filter_text(condition[0],condition[2]))
                    else:
                        filtered_list.append(pircollection.not_ornot_filter_time(condition[0],condition[2],condition[3])) 

                found_list = self.get_union_or_intersection(filtered_list,operators)       
                print(pircollection.get_index(found_list))
                return found_list

    def delete(self):
        board = Board()
        while True:
            board.deleteBoard()
            pircollection = PIRCollection()
            found_list = self.search()
            index_list = pircollection.get_index(found_list)
            if len(index_list) == 0:
                board.delete_nothing()
                continue
            else:
                pircollection.delete(index_list)
                board.successDelete()
                break

    def modify(self):
        board = Board()
        enter = Command()
        while True:
            board.modifyBoard()
            modify_option = enter.get_modify_option()
            if self.check_int(modify_option):
                modify_option = int(modify_option)
                pircollection = PIRCollection()
                if modify_option == 1:
                    search_text, replace_text = enter.get_modify_text()
                    pircollection.replace_global(search_text,replace_text)
                    board.successModify()
                    break
                elif modify_option == 2:
                    board.modify_specific()
                    found_list = self.search()
                    index_list = pircollection.get_index(found_list)
                    if len(index_list) == 0:
                        board.modify_nothing()
                        continue
                    search_text, replace_text = enter.get_modify_text()
                    pircollection.replace_specific(search_text,replace_text,index_list)
                    board.successModify()
                    break
                elif modify_option == 3:
                    self.main()
                    break
                else:
                    board.getValidInput()
            else:
                board.getValidInput()

    
    def display(self):
        pircollection = PIRCollection()
        enter = Command()
        board = Board()
        while True:
            board.displayBoard()
            display_option = enter.get_display_option()
            if self.check_int(display_option):
                display_option = int(display_option)
                pirview = PIRView()
                if display_option in range(1,5):
                    pircollection.updateSearchType(display_option)
                    content_to_display = pircollection.matches_type()
                    for line in content_to_display:
                        line = line.split(",")
                        if display_option == 1:
                            pirview.NoteDetail(line[0])
                        elif display_option == 2:
                            pirview.TaskDetail(line[0],line[1])
                        elif display_option == 3:
                            pirview.ContactDetail(line[0],line[1],line[2])
                        else:
                            pirview.EventDetail(line[0],line[1],line[2])
                    break       
                elif display_option == 5:
                    pircollection.updateSearchType(1)
                    content_to_display = pircollection.matches_type()   
                    for line in content_to_display:
                        pirview.NoteDetail(line.split(",")[0])
                    pircollection.updateSearchType(2)
                    content_to_display = pircollection.matches_type()   
                    for line in content_to_display:
                        pirview.TaskDetail(line.split(",")[0],line.split(",")[1])
                    pircollection.updateSearchType(3)
                    content_to_display = pircollection.matches_type()   
                    for line in content_to_display:
                        pirview.ContactDetail(line.split(",")[0],line.split(",")[1],line.split(",")[2])
                    pircollection.updateSearchType(4)
                    content_to_display = pircollection.matches_type()   
                    for line in content_to_display:
                        pirview.EventDetail(line.split(",")[0],line.split(",")[1],line.split(",")[2])
                elif display_option == 6:
                    self.main()
                    break
                else:
                    board.getValidInput()                    
            else:
                board.getValidInput() 

    def check_int(self,string):
        try:
            int(string)
            return True
        except ValueError:
            return False
        
    def get_union_or_intersection(self,filtered_list,operators):      
        list2 = [None] * (len(filtered_list) - 1) 
        if operators[0] == "&&":
            set1 = set(filtered_list[0])
            set2 = set(filtered_list[1])
            list2[0] = set1.intersection(set2)
        if operators[0] == "||":
            set1 = set(filtered_list[0])
            set2 = set(filtered_list[1])
            list2[0] = set1.union(set2)

        for i in range(2,len(filtered_list)):   
                                    #len(filtered_list)>=3
                                    #[1,2,3,4] 保持不變
                                    #[ 2",3",4"]儲存
                                    # 1&&2 -> 2" 2"&&3 -> 3" 3"||4 -> 4"
            if operators[i-1] == "&&":
                set1 = set(filtered_list[i])
                set2 = set(list2[i-2])                        
                list2.append(set1.intersection(set2))
            elif operators[i-1] == "||":
                set1 = set(filtered_list[i])
                set2 = set(list2[i-2])                        
                list2.append(set1.union(set2))  
        
        found_list =  list(list2[-1])        
        print(found_list)
        return found_list
        

if __name__ == '__main__':
    pircontroller = PIRController()
    pircontroller.main()
        
