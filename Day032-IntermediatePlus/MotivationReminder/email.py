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

    def setSender(self,sender):
        self.sender=sender

    def getSender(self):
        return self.sender

    def setReceiver(self,receiver):
        self.receiver=receiver

    def getReceiver(self):
        return self.receiver

    def setSubject(self,subject):
        self.subject=subject

    def getSubject(self):
        return self.subject

    def setBody(self,body):
        self.body=body

    def getBody(self):
        return self.body

