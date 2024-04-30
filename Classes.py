class Compound:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.binds = []
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    

        