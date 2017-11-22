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
        #if name==self.name and category==self.category and location==self.location:
        self.name=name
        self.category=category
        self.location=location
        return self.name, self.category, self.location
        #else:
            #pass

