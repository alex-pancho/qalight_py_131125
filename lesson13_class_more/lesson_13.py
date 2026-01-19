

class Car:
    pass # тут є ініціалізація, але прихована


class CarNew:

    def __init__(self):
        pass # клас ініціалізуємо без параметрів


class CarParams:

    def __init__(self, make, model): # клас ініціалізуємо з параметрами
        self.make = make
        self.__model = model
    
    @property  # гетер
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if value == "":
            raise ValueError("Cant use empty value")
        elif value != self.__model:
            self.__model = value
        else:
            print("not set")
    
    def __repr__(self):
         return f"The {self.make} {self.model} object"

    def __del__(self):
        print(f"The {self.make} {self.model} object has been destroyed.")
    
    def __len__(self):
        return 100


my_car = CarParams("Toyota", "Camry") # створення обєкту класу

# Використання об'єкта та доступ до його атрибутів
print(my_car.make)  # Виведе: Toyota
print(my_car.model) # Виведе: Camry
try:
    my_car.model = "" # Raise ValErr
except ValueError:
    print("Go to val error")
    my_car.model = "Corolla"
print(my_car)

print(len("aaa"))

print(len(my_car))

class Person():
    def __init__(self, age:int = 0) -> None:
        self.__age = age
        self.__name = ""

    @property  # it is getter
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, years:int):
        #self.__age = years
        if not isinstance(years, int):
            raise ValueError("add_year must be int")
        if years >= self.__age:
            self.__age = years
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name, str):
            raise ValueError("new_name must be str")
        if len(new_name) >= len(self.__name):
            self.__name = new_name
