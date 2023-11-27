# from model.PIRContact import Contact
# from model.PIREvent import Event
# from model.PIRNote import Note
# from model.PIRTask import Task
# from controller.findIndex import findIndex

class PIRView:
    

    @staticmethod
    def NoteDetail(content):
        # note = Note()
        print("Note: ")
        print("Content: "+ content)
        print("----------------------------------------------------")
    
    @staticmethod
    def TaskDetail(description, deadline):
        print("Task: ")
        print("Description: " + description)
        print("Deadline: " + deadline)
        print("----------------------------------------------------")
    
    @staticmethod
    def ContactDetail(name, address, mobileNum):
        print("Contact: ")
        print("Name: " + name)
        print("Address: " + address)
        print("Mobile Number" + mobileNum)
        print("----------------------------------------------------")

    @staticmethod
    def EventDetail(description, start_time, alarm):
        print("Event:")
        print("Description: " + description)
        print("Start time: " + start_time)
        print("Alarm: " + alarm)
        print("----------------------------------------------------")

    