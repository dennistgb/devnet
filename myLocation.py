class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country


    def myLocation(self):
        print(f"Hi, my name is {self.name} and I live in {self.country}.")

#first instantation of the class Location 
locl = Location("Tomas", "Portugal")
locl.myLocation()

#3 more instantations of the class Location
loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")

loc2.myLocation()
loc3.myLocation()

your_loc = Location("Your_name", "Your_country")
your_loc.myLocation()
