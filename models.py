import json

class Habits:
    def __init__(self, name, count):
        self._name = name
        self._count = count

   
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

   
   
    def get_count(self):
        return self._count
   
    def set_count(self, count):
        self._count = count 

    def check_in(self):
        self._count += 1


class HabitTracker:
    def __init__(self):
        self._habits=[]
        self._filename= 'habits'
        self.load()

        
    

    
