class Car(object): 
    def __init__(self,name,color,seat_count,speed_limit,company):
        self.name = name
        self.color = color
        self.seat_count = seat_count
        self.speed_limit = speed_limit
        self.company = company

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")

    def accelerate(self):
        print("Accelerating...")

    def change_gear(self,gear_type):
        gear_type = input("Whoch gear do you want to switch to? ")
        print("Gear changed to "+gear_type)

 
audi = Car("A5","Black","6","160","Volkswagen")
print(audi.color)

    