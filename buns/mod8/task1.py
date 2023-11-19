class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if isinstance(coordinates, tuple) and len(coordinates) == 2:
            self._coordinates = coordinates
        else:
            print("Coordinates must be a tuple of two values.")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if isinstance(speed, (int, float)) and speed >= 0:
            self._speed = speed
        else:
            print("Speed must be a non-negative numeric value.")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            print("Brand must be a string.")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        current_year = 2023
        if isinstance(year, int) and 1900 <= year <= current_year:
            self._year = year
        else:
            print("Year must be an integer between 1900 and the current year.")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if isinstance(number, str):
            self._number = number
        else:
            print("Number must be a string.")

    def __str__(self):
        return f"Transport: {self._brand}, Year: {self._year}, Number: {self._number}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        return pos_x <= self._coordinates[0] <= (pos_x + length) and pos_y <= self._coordinates[1] <= (pos_y + width)


class Passenger:
    def __init__(self):
        self.__passengers_capacity = 0
        self.__number_of_passengers = 0

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if isinstance(passengers_capacity, int) and passengers_capacity >= 0:
            self.__passengers_capacity = passengers_capacity
        else:
            print("Passengers capacity must be a non-negative integer.")

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and number_of_passengers >= 0:
            self.__number_of_passengers = number_of_passengers
        else:
            print("Number of passengers must be a non-negative integer.")


class Cargo:
    def __init__(self):
        self.__carrying = 0

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if isinstance(carrying, (int, float)) and carrying >= 0:
            self.__carrying = carrying
        else:
            print("Carrying capacity must be a non-negative numeric value.")


class Plane(Transport):
    def __init__(self, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, (int, float)) and height >= 0:
            self._height = height
        else:
            print("Height must be a non-negative numeric value.")


class Auto(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Ship(Transport):
    def __init__(self, name, port, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._port = port

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self._port = port
        else:
            print("Port must be a string.")


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Airplane(Plane):
    def __init__(self, coordinates, speed, brand, year, number, height, wingspan):
        super().__init__(coordinates, speed, brand, year, number, height)
        self._wingspan = wingspan

    @property
    def wingspan(self):
        return self._wingspan

    @wingspan.setter
    def wingspan(self, wingspan):
        if isinstance(wingspan, (int, float)) and wingspan >= 0:
            self._wingspan = wingspan
        else:
            print("Wingspan must be a non-negative numeric value.")


class Seaplane(Plane, Ship):
    def __init__(self, coordinates, speed, brand, year, number, height, port, floats):
        Plane.__init__(self, coordinates, speed, brand, year, number, height)
        Ship.__init__(self, coordinates, speed, brand, year, number, port)
        self._floats = floats

    @property
    def floats(self):
        return self._floats

    @floats.setter
    def floats(self, floats):
        if isinstance(floats, bool):
            self._floats = floats
        else:
            print("Floats must be a boolean value.")
            
auto_instance = Auto(
    coordinates=(10, 20),
    speed=60.0,
    brand="Toyota",
    year=2020,
    number="ABC123"
)

auto_instance.coordinates = (15, 25)
print(auto_instance)


ship_instance = Ship(
    name="CargoShip1",
    coordinates=(30, 40),
    speed=20.0,
    brand="Maersk",
    year=2015,
    number="XYZ789",
    port="New York"
)


ship_instance.brand = "Maersk Line"
print(ship_instance)

area_check_result = ship_instance.isInArea(pos_x=25, pos_y=35, length=10, width=10)
print(area_check_result)