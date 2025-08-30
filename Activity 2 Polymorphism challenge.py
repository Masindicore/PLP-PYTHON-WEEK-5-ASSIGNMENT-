
     # Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism


class Car(Vehicle):
    def move(self):
        print("The car is driving on the road.")


class Plane(Vehicle):
    def move(self):
        print("The plane is flying in the sky.")


class Boat(Vehicle):
    def move(self):
        print("The boat is sailing on the water.")


class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling down the path.")


# Demonstrate polymorphism
def demonstrate_movement(vehicles):
    print("=== Vehicle Movement Demo ===")
    for vehicle in vehicles:
        vehicle.move()


# Create objects
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Run the demonstration
demonstrate_movement(vehicles)
   
