import logging
from design_patterns.observer import Observer

logger = logging.getLogger(__name__)
f = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
fh = logging.FileHandler('logs/travel.log')
fh.setFormatter(f)

logger.addHandler(fh)
logger.setLevel(logging.INFO)


class Ship:
    def __init__(self):
        pass

    def sail(self):
        logger.info("We r sailing")


class Plane:
    def __init__(self):
        pass

    def fly(self):
        logger.info("We r flying")


class Car:
    def drive(self):
        logger.info("we r driving")

class Bike:
    def __init__(self):
        pass

    def ride(self):
        logger.info("we r riding")


class TransportationCompany(Observer):
    def update(self, obj, *args, **kwargs):
        logger.info(f"I know that {obj} has done {args} and {kwargs}")

# car1 = Car()
# car2 = Car()
# bike = Bike()
# plane = Plane()
# ship = Ship()
#
# ff = [CarAdapter(car1), CarAdapter(car2), BikeAdapter(bike), PlaneAdapter(plane),
# ShipAdapter(ship)]
#
# adapters=[GeneralAdapterClass(car1, travel="drive"),
#         GeneralAdapterClass(car2, travel="drive"),
#         GeneralAdapterClass(bike, travel="ride"),
#         GeneralAdapterClass(plane, travel="fly"),
#         GeneralAdapterClass(ship, travel="sail")]
#
# for adp in adapters:
#     adp.travel()