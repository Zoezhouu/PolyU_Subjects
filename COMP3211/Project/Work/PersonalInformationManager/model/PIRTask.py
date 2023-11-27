class Task:
    def __init__(self, description, deadline):
        self.PIRType = 'Task'
        self.description = description
        self.deadline = deadline

    # create(return info)  
    def setTask(self, newDesc, newDeadline):
        self.description = newDesc
        self.deadline = newDeadline
        return self.PIRType, self.description, self.deadline
    
    # read(return info)
    def getPIMTask(self):
        return  self.PIRType, self.description, self.deadline

    # tostring(return string to printed PIR record on interface)
    def TaskToString(self):
        string = self.PIRType + ":\nDescription: " + self.description + "\nDeadline: " + self.deadline
        return string
    
    # task to PIR record form(return in PIR form)
    def TaskToPIR(self):
        return self.description + "," + self.deadline
    
    # update(return updated info)
    def updateTask(self, newDesc, newDeadline):
        if newDesc != self.description:
            self.description = newDesc
        if newDeadline != self.deadline:
            self.deadline = newDeadline
            return self.PIRType, self.description, self.deadline
    
    # delete(in PIRCollection)