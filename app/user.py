class User(object):
    registeredUsers={}
    #initialize the class
    def __init__(self,email,password):
        self.email=email
        self.password=password

    #register users
        def regUser(self,regEmail, regPassword, regConPassowrd):
            self.email=regEmail
            self.password=regPassword
            regConPassowrd=self.password
            return self.email
    
        def logUser(self,logEmail, logPassword):
            if(logEmail==self.email and logPassword==self.password):
                return True
            else:
                return False