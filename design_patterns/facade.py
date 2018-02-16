# it is also called interface
__doc__ = '''Provide a unified interface to a set of interfaces (adapters) in a subsystem. 
Facade defines a higher-level interface that makes the subsystem easier to use.'''

import logging
from design_patterns.travel import Car, Ship, Bike, Plane, TransportationCompany
from design_patterns.adapter import GeneralAdapterClass

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


class VehicleFacade:
    vehicle_adapters = None

    @classmethod
    def create_vehicle(cls):
        logger.info("Creating Vehicle!")
        cls.vehicle_adapters = [GeneralAdapterClass(Car(), travel='drive'),
                                GeneralAdapterClass(Car(), travel='drive'),
                                GeneralAdapterClass(Plane(), travel='fly'),
                                GeneralAdapterClass(Bike(), travel='ride'),
                                GeneralAdapterClass(Ship(), travel='sail'),
                                GeneralAdapterClass(Car(), travel='drive'),
                                GeneralAdapterClass(Plane(), travel='fly')]

    @classmethod
    def move_vehicles(cls):
        logger.info("Moving Vehicle ..")

        for vehicle in cls.vehicle_adapters:
            vehicle.travel()

    @classmethod
    def monitor_cars(cls, observer):
        cls.vehicle_adapters[0].add_observer(observer)
        logger.info("Added the observer to the Cars")

    @classmethod
    def change_cars_name(cls, new_name):
        logger.info("Changing the Cars name")
        # logger.info("current car name is {}".format(cls.vehicle_adapters[0].name))
        cls.vehicle_adapters[0].name = new_name
        logger.info("Cars name changed")




if __name__ == '__main__':
    monitor = TransportationCompany()

    VehicleFacade.create_vehicle()
    VehicleFacade.move_vehicles()

    VehicleFacade.monitor_cars(monitor)
    VehicleFacade.change_cars_name("disooqi")




