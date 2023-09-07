from datetime import datetime
import time

class Clock():
    def __init__(self):
        self.Alarm_List = {}
        self.now = 0
        self.current_time = 0
    def Current_Time_Update(self):
        self.now = datetime.now()
        self.current_time = self.now.strftime("%H:%M")
        return self.current_time

    def add_alarm(self):
        self.Alarm_Name= input("please enter name for alarm: ")
        self.Alarm_Time = input("Please enter Time for Alarm as HH:MM")
        print("Alarm name is: "+self.Alarm_Name)
        
        if self.Alarm_Name in self.Alarm_List:
            print ("Name Alrady Exits")
            self.add_alarm()
        else:
            self.Alarm_List[self.Alarm_Name] = {self.Alarm_Time}
            
    def Set_Alarm(self):
        time.sleep(30)
        for i in self.Alarm_List:
            if self.Alarm_Time == str(self.Current_Time_Update()):
                print("Alarm " + self.Alarm_Name + " " + self.Alarm_Time)
                self.Menu()
            else :
                print(self.Alarm_List)
                print("Current Time is: " +self.Current_Time_Update())
                self.Set_Alarm()
    def Menu(self):
        print("Please Choose Option:")
        print(" 1.Current Time""\n 2.Add Alarm""\n 3.Remove Alarm""\n 4.Alarm List""\n 5.Set Alarms""\n 6.Quit")
        Choice = input()
        if Choice == "1":
            print(self.Current_Time_Update())
            self.Menu()
        elif Choice == "2":
            self.add_alarm()
            self.Menu()
        elif Choice == "3":
            quit()
        elif Choice == "4":
            print(self.Alarm_List)
            self.Menu()
        elif Choice == "5":
            Yeet.Set_Alarm()
            self.Menu
        elif Choice == "6":
            quit
        else:
            "Not a Valid Selection"
            self.Menu()


Alarm_Clock = Clock()
Alarm_Clock.Menu()
