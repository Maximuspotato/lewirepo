class Event(object):
    
    def __init__(self,name,category,location):
        self.name=name
        self.category=category
        self.location=location

    def addEvent(self,name,category,location):
        self.name=name
        self.category=category
        self.location=location
        return self.name, self.category, self.location


    def modifyEvent(self,name,category,location):
        self.name=name
        self.category=category
        self.location=location
        return self.name, self.category, self.location

    def deleteEvent(self,name):
        if name==self.name:
            self.name=""
            self.category=""
            self.location=""
            return self.name, self.category, self.location
        else:
            raise ValueError

    def searchEvent(self,name):
        if name==self.name:
            return self.name, self.category, self.location
        else:
            raise ValueError


