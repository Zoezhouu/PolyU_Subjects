class Note:
    def __init__(self, content):
        self.PIRType = 'Note'
        self.content = content

    # create (return info) 
    def setNote(self, newContent):
        self.content = newContent
        return self.PIRType, self.content

    
    # read(return info)
    def getPIMNote(self):
        return self.PIRType, self.content
    
    # tostring(return string to printed PIR record on interface)
    def NoteToString(self):
        string = self.PIRType + ":\nContent: " + self.content
        return string
    
    # note to PIR record form(return in PIR form)
    def NoteToPIR(self):
        return self.content

    # update(return updated info)
    def updateNote(self, newContent):
        if newContent != self.content:
            self.content = newContent
        return self.PIRType, self.content
    
    # delete(in PIRCollection)
