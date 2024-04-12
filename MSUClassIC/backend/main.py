"""import csv
import sqlite3

# connection todatabse
 connection = sqlite3.connect("tutorial.db")""""


# Clas Definitions 
""" User class"""
class User:
    def __init__(self, name:str, user_name:str ):
        self.name = name
        self.user_name = user_name 

    def login(self):
        # firebase implementation 
        pass

    def logout(self):
        # firebase implementation 
        pass





""" Chair class, derived from user"""
class Chair(User):
    def __init__(self,  name:str, user_name:str, department:str):
        super().__init__(name, user_name)
        self.department = department 

    #void    
    def View_class_schedule(self):
        # what is the exact implementation ## need to reevaluate logic here 
        ## some iteration needs to happen here 
        pass 

    #void
    def Request_class_change(self, course_code:int):
        # do we still need this?
        pass 






""" View class"""
class View:
    def __init__(self, user_role:str, display_mode:str):
        self.user_role = user_role
        self.display_mode = display_mode
    
    #void
    def Display_schedule(self):
        pass 

    #void
    def Switch_display_mode(self, mode:str):
        pass 
    
    #void
    def Highlight_conflict(self):
        pass    
     

""" Course class"""
class Course: 
    def __init__(self, subject:str, code:str, title:str, section:str, Expected_enrollment:int):
        self.subject = subject
        self.code = code
        self.title = title
        self.section = section
        self.Expected_enrollment = Expected_enrollment

    def set_subject(self,setter:str):
         pass 
    def get_subject(self)->str:
         pass 
    def set_code(,self, setter:str):
         pass 
    def get_code(self)->str:
         pass 
    def set_title(self,setter:str):
        pass
    def get_title(self)->str:
        pass
    def set_section(self,setter:str):
        pass
    def get_section(self)->str:
        pass
    def set_Expected_enrollment(self,setter:str):
        pass
    def get_Expected_enrollment(self)->str:
        pass






""" Time class"""
class Time:
    def __init__(self,class_time:str, days_of_class:list """might need to be string"""):
        self.class_time = class_time
        self.days_of_class = days_of_class
    
    def set_class_time(time_of_class:str):
        pass
    def get_class_time()->str:
        pass
    def set_days_of_class(days_of_class:list):
        pass
    def get_days_of_class()->list:
        pass

    
""" Professor class"""
class Professor:
    def __init__(self, name: str, department:str, courses_taught:list):
        self.name = name
        self.department = department
        self.courses_taught = courses_taught
    
    def set_name(self, name:str):
        pass

    def get_name(self)->str:
        pass

    def set_department(self, department:str):
        pass

    def get_department(self)->str:
        pass

    def set_courses_taught(self, courses:list):
        pass

    def get_courses_taught(self)->list:
        pass




""" Location class"""
class Location:
    def __init__(self, building:str, room_no:str, max_capacity:int):
        self.building = building
        self.room_no = room_no
        self.max_capacity = max_capacity

    def set_building(self, building:str):
        pass

    def get_building(self)->str:
        pass

    def set_room_no(self, room_no:str):
        pass

    def get_room_no(self)->str:
        pass

    def set_max_capacity(self, max_capacity:int):
        pass

    def get_max_capacity(self)->int:
        pass



        
""" Entry class"""
class Entry:
    def __init__(self, course:Course, time:Time,professor:Professor,location:Location):
        pass

    def view_change_entry(self):
        pass
    def check_conflicts(self):
        pass









""" Database  class""" #very much related to entry
class Database:
    pass
""" User class"""