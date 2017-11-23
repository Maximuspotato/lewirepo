from validate_email import validate_email
class User(object):
    #initialize the class
    def __init__(self,email,password):
        self.email=email
        self.password=password

    #register users
    def regUser(self,regEmail, regPassword, regConPassowrd):
        if validate_email(regEmail)==True:
            self.email=regEmail
        else:
            pass

        if len(regPassword)>=8:
            self.password=regPassword
        else:
            pass

        if regConPassowrd==self.password:
            regConPassowrd=self.password
        else:
            pass

        return self.email, self.password, regConPassowrd
    
    #login user
    def logUser(self,logEmail, logPassword):
        if logEmail == self.email and logPassword == self.password:
            return logEmail, logPassword
        else:
            pass

    def delUser(self,uEmail):
        if uEmail==self.email:
            self.email=""
            self.password=""
            return self.email, self.password
        