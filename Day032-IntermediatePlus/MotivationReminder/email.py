import this


class Email:
    def __init__(self,sender,receiver,subject,body,password):
        this.sender=sender
        this.receiver=receiver
        this.subject=subject
        this.body=body
        this.password=password

# define getters and setters

    def setPassword(self,password):
        self.password=password

    def getPassword(self):
        return self.password
