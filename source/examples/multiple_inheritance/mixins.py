import time


class Base():
    def log(self):
        pass


class LoggingMixin(Base):
    def log(self):
        print("time is: %s" % time.time())
        # print("this is:", self)
        super().log()


class Vehicle(Base):
    def log(self):
        print("this is:", self.__repr__())
        super().log()


class TwoWheeledVehicle(Vehicle):
    pass


class LightVehicle(Vehicle):
    pass


class HeavyVehicle(Vehicle):
    pass


class Bike(LoggingMixin, TwoWheeledVehicle, LightVehicle):
    pass


class MotorCycle(TwoWheeledVehicle, HeavyVehicle):
    pass


class Tank(HeavyVehicle):
    pass


bike = Bike()
tank = Tank()

bike.log()
tank.log()
