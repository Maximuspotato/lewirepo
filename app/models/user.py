from validate_email import validate_email

class User(object):
    users=[{
        'email':None,
        'password':None
    }]
    #initialize the class
    def __init__(self,email,password):
        self.email=email
        self.password=password

    #register users
    def regUser(self,regEmail, regPassword, regConPassowrd):
        if validate_email(regEmail)==True:
            self.email=regEmail
            User.users[0]['email']=self.email
        else:
            raise ValueError

        if len(regPassword)>=8:
            self.password=regPassword
            User.users[0]['password']=self.password
        else:
            raise ValueError

        if regConPassowrd==self.password:
            regConPassowrd=self.password
        else:
            raise ValueError

        return self.email, self.password, regConPassowrd, User.users
    
    #login user
    def logUser(self,logEmail, logPassword):
        if logEmail == self.email and logPassword == self.password:
            return logEmail, logPassword
        else:
            raise ValueError

    def delUser(self,uEmail):
        if uEmail==self.email:
            self.email=""
            self.password=""
            return self.email, self.password
        