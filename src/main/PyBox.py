
class PyBox:

    def __init__(self):
        self.boxObj = []

    def __str__(self):
        return "Box" + f"{self.boxObj}"

    def isPresent(self):
        return len(self.boxObj) == 1 and self.boxObj[0] != None

    def put(self, obj):
        if obj != None:
            self.boxObj.clear()
            self.boxObj.append(obj)

    def get(self):
        if len(self.boxObj) == 1:
            return self.boxObj[0]
        return None
    
    def getOrElseReturn(self, retObj):
        if len(self.boxObj) == 1:
            return self.boxObj[0]
        return retObj

    def clear(self):
        self.boxObj.clear()

    def getOrElseThrow(self, Exception, msg):
        if len(self.boxObj) == 1:
            return self.boxObj[0]
        
        raise Exception(msg)