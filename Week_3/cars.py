class car:
    def __init__(self,model,make,year_of_production,fuel_capacity,horsepower):
        self.model=model
        self.make=make
        self.year_of_production=year_of_production
        self.fuel_capacity=fuel_capacity
        self.horsepower=horsepower

def print_make(model,make):
    print("The car is of {1} make".format(model,make))

my_car=car("Nissan","GTR-R35","2005","6 Litre","1200")
