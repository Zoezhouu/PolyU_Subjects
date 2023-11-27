class Event:
    def __init__(self, description, start_time, alarm):
        self.PIRType = 'Event'
        self.description = description
        self.start_time = start_time
        self.alarm = alarm

    # create event (return info)
    def setEvent(self, newDesc, newStartTime, newAlarm):
        self.description = newDesc
        self.start_time = newStartTime
        self.alarm = newAlarm
        return self.PIRType, self.description, self.start_time, self.alarm

    # read (return info)
    def getPIMEvent(self):
        return self.PIRType, self.description, self.start_time, self.alarm
    
    # tostring(return string to printed PIR record on interface)
    def EventToString(self):
        string = self.PIRType + ":\nDescription: " + self.description + "\nStart Time:" + self.start_time + "\nAlarm Time: " + self.alarm
        return string
    
    # event to PIR record form(return in PIR form)
    def EventToPIR(self):
        return self.description + "," + self.start_time + "," + self.alarm
    
    # update(return updated info)
    def updateEvent(self, newDesc, newStartTime, newAlarm):
        if newDesc != self.description:
            self.description = newDesc
        if newStartTime != self.start_time:
            self.start_time = newStartTime
        if newAlarm != self.alarm:
            self.alarm = newAlarm
        return self.PIRType, self.description, self.start_time, self.alarm

    # delete(in PIRCollection)
