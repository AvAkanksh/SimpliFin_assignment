class User:
    def __init__(self,id,userDetails):
        self.id = id
        self.name,self.gender,self.age = userDetails["name"],userDetails["gender"],userDetails["age"]
        self.rides_offered = [] # list of ride ids offered by the user
        self.rides_taken = [] # list of ride ids taken by the user
        
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, gender={self.gender}, age={self.age}, rides_offered={len(self.rides_offered)}, rides_taken={len(self.rides_taken)})"