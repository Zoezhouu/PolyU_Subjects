class Command:
    def __init__(self):
        pass

    def mainCommand(self):
        return input("Please choose what you want to do. 1, 2, 3, 4, 5, 6: ")
    
    # choice for creating PIR
    def createCommand(self):
        return input("Please enter 1, 2, 3, 4, 5 to choose what you want to do: ")

    # create note command
    def createNoteCommand(self):
        content = input("Enter your note:")
        return content
    
    # create task (text) command
    def createTaskTextCommand(self):
        return input("Enter task text:")
    
    # create date command
    def getDateTaskCommand(self):
        return input("Enter date and time for task ( in format YYYY/MM/DD hh:mm): ")
    
    # create contact command
    def createContactNameCommand(self):
        return input("Enter a name for contact item:")
    
    def createContactAddrCommand(self):
        return input("Enter an contact address: ")
    
    def createContactMobileNumCommand(self):
        return input("Enter a contact number: ")
    
    # create event command
    def createEventDescCommand(self):
        return input("Enter a description for this event: ")
    
    # create event start-time date
    def getDateStartCommand(self):
        return input("Enter date and time for event start time( in format YYYY/MM/DD hh:mm): ")
    
    def getDateAlarmCommand(self):
        return input("Enter date and alarm time for this event( in format YYYY/MM/DD hh:mm): ")
    
    def searchTypeCommand(self):
        return input("Please enter 1, 2, 3, 4, 5, 6 to choose what you want to do. ")

    def get_logical_condition_withtime(self):
        conditon = input("Enter condition (time, value, condition) or (text, value): , or PRESS \"enter\" to finish. ")
        conditon = conditon.split(",")
        return conditon
    
    def get_logical_condition_text(self):
        conditon = input("Enter text filter: ")
        conditon = conditon.split(",")
        return conditon

    def get_include_or_not(self):
        not_operator = input("Enter \"!\" to search excluding this condition, or PRESS \"enter\" button to search including this condition: ")
        return not_operator
    
    def get_operator(self):
        operator = input("Enter operator: \"||\", \"&&\" : , or PRESS \"enter\" to finish. ")
        return operator
    
    def get_search_filterNoteContact(self):
        searchFilter = input("Please enter 1, 2 to choose what you want to do: ")
        return searchFilter        

    def get_search_filterTaskEvent(self):
        searchFilter = input("Please enter 1, 2, 3 to choose what you want to do.: ")
        return searchFilter

    def get_logical_condition_time(Self):
        conditon = input("Enter time in form of: value(YYYY/MM/DD HH:MM), condition(<, = , >): ")
        conditon = conditon.split(",")
        return conditon
    
    def get_modify_option(self):
        return input("Please enter 1, 2, 3 to choose modify option: ")
    
    def get_modify_text(self):
        search_text = input("Enter original text you want to modify: ")
        replace_text = input("Enter replaced text: ")
        return search_text,replace_text
    
    def get_display_option(self):
        return input("Please enter 1, 2, 3, 4, 5 to choose what you want to display, or back to home page: ")
    