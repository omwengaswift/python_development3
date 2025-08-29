# ================================
# Assignment: OOP Concepts in Python
# ================================

# --------------------------------
# Part 1: Design Your Own Class
# --------------------------------

# Base Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device: {self.brand} {self.model}"


# Derived Class: Smartphone (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)  # Inherit from Device
        self.os = os
        self.storage = storage
        self.battery = 100  # Default battery level

    def make_call(self, contact):
        print(f"📞 Calling {contact} using {self.brand} {self.model}...")

    def install_app(self, app_name):
        print(f"📲 Installing {app_name} on {self.brand} {self.model}...")

    def charge(self):
        self.battery = 100
        print(f"🔋 {self.brand} {self.model} is now fully charged.")

    # Overriding method (Polymorphism)
    def device_info(self):
        return f"Smartphone: {self.brand} {self.model}, OS: {self.os}, Storage: {self.storage}GB"


# Creating Smartphone objects
phone1 = Smartphone("Samsung", "Galaxy S23", "Android", 256)
phone2 = Smartphone("Apple", "iPhone 15", "iOS", 512)

# Using Smartphone methods
print(phone1.device_info())
phone1.make_call("Alice")
phone1.install_app("WhatsApp")
phone1.charge()

print(phone2.device_info())

# --------------------------------
# Part 2: Polymorphism Challenge
# --------------------------------

# Base Class: Vehicle
class Vehicle:
    def move(self):
        pass  # Abstract-like method


# Child Classes implementing move() differently
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Testing polymorphism with vehicles
print("\n--- Vehicle Movements ---")
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each class has its own version of move()
