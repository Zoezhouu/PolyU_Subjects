import unittest
from model.PIRContact import Contact
from model.PIREvent import Event
from model.PIRNote import Note

class PIMTest(unittest.TestCase):
    def setUp(self) :
        self.TypeC = "Contact"
        self.Name = "Max"
        self.Addr = "PQ666"
        self.MobileNum = "66666666"
        self.TypeE = "Event"
        self.Description = "Group Meeting"
        self.Start_time = "2023/11/11 13:00"
        self.Alarm = "2023/11/11 12:50"
    #test for contact
    def test_setContact(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = 'Contact', self.Name, self.Addr, self.MobileNum
        result = contact.setContact(self.Name, self.Addr, self.MobileNum)
        self.assertEqual(expected_result, result)

    def test_getContact(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = 'Contact', self.Name, self.Addr, self.MobileNum
        result = contact.getContact()
        self.assertEqual(expected_result, result)

    def test_ContactToString(self):
        contact = Contact("Max","PQ666","66666666")
        # Type = "Contact"
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = self.TypeC + ":\nName: " + self.Name + "\nAddress:" + self.Addr + "\nMobile Number: " + self.MobileNum
        result = contact.ContactToString()
        self.assertEqual(expected_result, result)

    def test_ContactToPIR(self):
        contact = Contact("Max","PQ666","66666666")
        # Name = "Max"
        # Addr = "PQ666"
        # MobileNum = "66666666"
        expected_result = self.Name + "," + self.Addr + "," + self.MobileNum
        result = contact.ContactToPIR()
        self.assertEqual(expected_result, result)
    
    def test_updateContact(self):
        contact = Contact("Max","PQ666","66666666")
        contact.Name = self.Name
        contact.Addr = self.Addr
        contact.MobileNum = self.MobileNum
        # expected_result = 'Contact', contact.name, contact.address, contact.mobile_num
        result = contact.updateContact("Amy", "PQ999", "88888888")
        # self.assertEqual(expected_result, result)
        self.assertEqual(contact.name, "Amy")
        self.assertEqual(contact.address, "PQ999")
        self.assertEqual(contact.mobile_num, "88888888")

    #test for event
    def test_setEvent(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = 'Event', self.Description, self.Start_time, self.Alarm
        result = event.setEvent(self.Description, self.Start_time, self.Alarm)
        self.assertEqual(expected_result, result)

    def test_getPIMEvent(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = 'Event', self.Description, self.Start_time, self.Alarm
        result = event.setEvent(self.Description, self.Start_time, self.Alarm)
        self.assertEqual(expected_result, result)

    def test_EventToString(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Type = "Event"
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = self.TypeE + ":\nDescription: " + self.Description + "\nStart Time:" + self.Start_time + "\nAlarm Time: " + self.Alarm
        result = event.EventToString()
        self.assertEqual(expected_result, result)

    def test_EventToPIR(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        # Description = "Group Meeting"
        # Start_time = "2023/11/11 13:00"
        # Alarm = "2023/11/11 12:50"
        expected_result = self.Description + "," + self.Start_time + "," + self.Alarm
        result = event.EventToPIR()
        self.assertEqual(expected_result, result)

    def test_updateEvent(self):
        event = Event("Group Meeting","2023/11/11 13:00", "2023/11/11 12:50")
        event.Description = self.Description
        event.Start_time = self.Start_time
        event.Alarm = self.Alarm
        result = event.updateEvent("interview", "2023/12/12 18:00", "2023/12/12 17:50")
        self.assertEqual(event.description , "interview")
        self.assertEqual(event.start_time, "2023/12/12 18:00")
        self.assertEqual(event.alarm, "2023/12/12 17:50")

if __name__ == '__main__':
    unittest.main()
    
    # #test for note
    # def test_setNote(self):
    #     note = Note("hi")
    #     content = "hi"
    #     expected_result = 'Note', content
    #     result = note.setNote(content)
    #     self.assertEqual(expected_result, result)

    # def test_getNote(self):
    #     note = Note("hi")
    #     content = "hi"
    #     expected_result = 'Note', content
    #     result = note.getPIMNote()
    #     self.assertEqual(expected_result, result)

    # def test_NoteToString(self):
    #     note = Note("hi")
    #     Type = "Note"
    #     content = "hi"
    #     expected_result = Type + ":\nContent: " + content
    #     result = note.NoteToString()
    #     self.assertEqual(expected_result, result)

    # def test_NoteToPIR(self):
    #     note = Note("hi")
    #     content = "hi"
    #     expected_result = content
    #     result = note.NoteToPIR()
    #     self.assertEqual(expected_result, result)

    # def test_NoteToString(self):
    #     note = Note("hi")
    #     Type = "Note"
    #     content = "hi"
    #     expected_result = Type + ":\nContent: " + content
    #     result = note.NoteToString()
    #     self.assertEqual(expected_result, result)

    # def test_NoteToPIR(self):
    #     note = Note("hi")
    #     content = "hi"
    #     expected_result = content
    #     result = note.NoteToPIR()
    #     self.assertEqual(expected_result, result)














    

    


    # def test_setPIMContact(self):
    #     newName = 'Max'
    #     newAddr = 'PQ666'
    #     newMobileNum = '66666666'
    #     contact = Contact()
    #     expected_result = 'Contact', newName, newAddr, newMobileNum
    #     self.assertEqual(expected_result, contact.setContact(newName, newAddr, newMobileNum))


if __name__ == '__main__':
    unittest.main()


        # def setup(self):
    #     self.filename = 'record.pim'
    #     content = """------Text------
    #              Notes
    #              hi

    #              ------Task------
    #              Description,Deadline
    #              Assignment 2,2023/11/01 23:59
    #              ------Contact------
    #              Name,Address,Mobile_num
    #              Max,PQ666,66666666

    #              ------Event------
    #              Description,Start_time,Alarm
    #              Group Meeting,2023/11/11 13:00, 2023/11/11 12:50

    #              ------End------"""
    #     with open (self.filename, 'w') as file:
    #         file.write(content)

    # #create testing
    # def test_createTask(self):
    #     pass
    #     # expected_result = 'hi'
    #     # self.assertEqual(expected_result)
    #     #a= ''
    #     #b= ''
    #     #self.assertEqual(a, b)    
    # def test_createNote(self):
    #     pass
    #     # expected_test = 'Note'
    #     # filename = 'record.pim'
    #     # with open(filename, 'w') as file:
    #     #     file.write(expected_test)
    #     # with open(filename, 'r') as file:
    #     #     expected_result = file.read()
    #     # self.assertEqual(expected_result, expected_test)
    # def test_createEvent(self):
    #     pass
    #     # expected_test = 'Event'
    #     # filename = 'record.pim'
    #     # with open(filename, 'w') as file:
    #     #     file.write(expected_test)
    #     # with open(filename, 'r') as file:
    #     #     expected_result = file.read()
    #     # self.assertEqual(expected_result, expected_test)
    # def test_createContact(self):
    #     pass
    # #search testing
    # def test_searchTask(self):
    #     pass
    # def test_seachNote(self):
    #     pass
    # def test_searchEvent(self):
    #     pass
    # def test_searchContact(self):
    #     pass
    # #modify testing
    # def test_modifyTask(self):
    #     pass
    # def test_modifyNote(self):
    #     pass
    # def test_modifyEvent(self):
    #     pass
    # def test_modifyContact(self):
    #     pass
    # #delect testing
    # def test_delectTask(self):
    #     pass
    # def test_delectNote(self):
    #     pass
    # def test_delectEvent(self):
    #     pass
    # def test_delectContact(self):
    #     pass
    # #display testing
    # def test_displayTask(self):
    #     pass
    #     # expected_result = """
    #     # Task:
    #     # Description: Assignment 2
    #     # Deadline: 2023/11/01 23:59
    #     # """
    # def test_displayNote(self):
    #     pass
    #     # expected_result = """
    #     # Note:
    #     # Content: hi"""
    # def test_displayEvent(self):
    #     pass
    #     # expected_result = """
    #     # Event:
    #     # Description: Group Meeting
    #     # Start time: 2023/11/11 13:00
    #     # Alarm: 2023/11/11 12:50
    #     # """
    # def test_displayContact(self):
    #     pass
    #     # expected_result = """
    #     # Contact: 
    #     # Name: Max
    #     # Address: PQ666
    #     # Mobile Number: 66666666"""
    # def test_displayAll(self):
    #     # expected_result = """"""
    #     # with open(self.filename, 'r') as file:
    #     #     expected_output = print(file.read())
    #     # self.assertEqual(expected_result, expected_output)