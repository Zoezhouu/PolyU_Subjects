class Contact:
    def __init__(self, name, address, mobile_num):
        self.PIRType = 'Contact'
        self.name = name
        self.address = address
        self.mobile_num = mobile_num
    
    # create (return info)
    def setContact(self, newName, newAddr, newMobileNum):
        self.name = newName
        self.address = newAddr
        self.mobile_num = newMobileNum
        return self.PIRType, self.name, self.address, self.mobile_num
        
    # read(return info)
    def getContact(self):
        return self.PIRType, self.name, self.address, self.mobile_num

    # tostring(return string to printed PIR record on interface)
    def ContactToString(self):
        string = self.PIRType + ":\nName: " + self.name + "\nAddress:" + self.address + "\nMobile Number: " + self.mobile_num
        return string
    
    # contact to PIR record form(return in PIR form)
    def ContactToPIR(self):
        return self.name + "," + self.address + "," + self.mobile_num
    
    
    # update(return updated info)
    def updateContact(self, newName, newAddress, newMobileNum):
        if newName != self.name:
            self.name = newName
        if newAddress != self.address:
            self.address = newAddress
        if newMobileNum != self.mobile_num:
            self.mobile_num = newMobileNum
        return self.PIRType, self.name, self.address, self.mobile_num


    # delete(in PIRCollection)

