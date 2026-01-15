# class Car:
#     pass

# my_first_car = Car()
# my_first_car.brand = "Ford"
# my_first_car.model = "Cuga"
# print(type(my_first_car))
# print(my_first_car.brand, my_first_car.model)

# my_second_car = Car()
# print(type(my_first_car))
# print(my_second_car.brand, my_second_car.model)

# class Car:
#     def __init__(self):
#         self.brand = ""
#         self.model = ""

# my_first_car = Car()
# my_first_car.brand = "Ford"
# my_first_car.model = "Cuga"
# print(type(my_first_car))
# print(my_first_car.brand, my_first_car.model)

# my_second_car = Car()
# print(type(my_second_car))
# my_second_car.brand = "BMW"
# my_second_car.model = "M100"
# print(my_second_car.brand, my_second_car.model)


class Car:
    def __init__(self, brand, model = "ABC"):
        self.brand = brand
        self.model = model
        self.wheels = 4
        self.is_engine_on = False
    
    def __repr__(self):
        return f"Car {self.brand} {self.model} has {self.wheels} wheel"
    
    def change_engine(self, passkey=""):
        if passkey == "112233":
            self.is_engine_on = not(self.is_engine_on)
            print(f"Engine is {"on" if self.is_engine_on else "off"} ")
        else:
            print("Wrong passkey")


my_first_car = Car("Ford", "Cuga")
print(type(my_first_car))
print(my_first_car.brand, my_first_car.model)

my_second_car = Car("BMW","100")
print(type(my_second_car))
print(my_second_car.brand, my_second_car.model)


my_third_car = Car("Audi")
print(my_third_car.brand, my_third_car.model)
my_third_car.wheels = 5
print(my_third_car.wheels)
print("engine status:", my_third_car.is_engine_on)
my_third_car.change_engine()
my_third_car.is_engine_on = True
print("engine status:", my_third_car.is_engine_on)
my_third_car.change_engine("112233")
print("engine status:", my_third_car.is_engine_on)

class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    
    def __repr__(self):
        return f"Awalible: {self.__balance} USD"
    
    def get_balance(self):
        return self.__balance

    def get_balance_print(self):
        print(self.__balance)

    def set_balance(self, value):
        if isinstance(value, (int, float)):
            self.__balance = value

account = BankAccount(1000) #  account._BankAccount__balance = 1000
# account.__balance = 100000
# print(account.__balance)
# print(account.__dict__)
account.set_balance(100)
print(account.get_balance())

print(my_third_car)
print(account)
print(my_first_car)
print(my_second_car)

alex = BankAccount(10)
nata = BankAccount(25)
print(alex.get_balance() > nata.get_balance())
#print(alex.get_balance_print() > nata.get_balance_print())

class Animal:

    def birth(self):
        print("this animal has births")

    def speak(self):
        pass  # Загальний метод для всіх тварин
        return "Kwa-kwa"


class Dog(Animal):

    def speak(self):
        return "Wof!"


class Cat(Animal):

    def speak(self):
        return "Meeo!"

class Koza(Animal):
    
    def speak(self):
        return

patron = Dog()
murzik = Cat()

print(patron.speak())
print(murzik.speak())
patron.birth()
murzik.birth()
zhaba = Animal()
print(zhaba.speak())

belka = Koza()
print(belka.speak())


# Без ООП
name = "John"
age = 25
print(f"{name} is {age} years old.")

# З ООП
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

person1 = Person("Jon", 15)
person2 = Person("Daeneris", 15)
person3 = Person("Tyrion", 30)
person4 = Person("Sansa", 15)
person5 = Person("Arya", 10)
person6 = Person("Jaime", 35)
person7 = Person("Cersei", 35)

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
print(person4.get_info())
print(person5.get_info())
print(person6.get_info())
print(person7.get_info())


class Vehicle:
    def __init__(self, color):
        self.color = color


class NewCar(Vehicle):
    def __init__(self, color, brand):
        super().__init__(color)
        self.brand = brand

my_new_car = NewCar("white", "Dodje")
print(my_new_car.color, my_new_car.brand)