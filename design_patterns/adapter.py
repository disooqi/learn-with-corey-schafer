# https://en.wikipedia.org/wiki/Software_design_pattern
import logging
from design_patterns.observer import Observable


logger = logging.getLogger(__name__)
f = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
fh = logging.FileHandler('logs/adapter.log')
fh.setFormatter(f)

logger.addHandler(fh)
logger.setLevel(logging.INFO)


class GeneralAdapterClass(Observable):
    __doc__ = '''
    Convert the interface of a class into another interface clients expect. An adapter lets classes 
    work together that could not otherwise because of incompatible interfaces. The enterprise 
    integration pattern equivalent is the translator.
    '''
    _initialized = False

    def __init__(self, vehicle, **adapted_methods):
        super().__init__()
        self.vehicle = vehicle

        for key, value in adapted_methods.items():
            func = getattr(self.vehicle, value)
            self.__setattr__(key, func)

        self._initialized = True

    def __getattr__(self, attr):
        return getattr(self.vehicle, attr)

    def __setattr__(self, key, value):
        if not self._initialized:
            super().__setattr__(key, value)

        else:
            setattr(self.vehicle, key, value)
            self.notify_observer(key=key, value=value)





#
# class ShipAdapter:
#     def __init__(self, ship):
#         self.ship = ship
#
#     def travel(self):
#         self.ship.sail()
#
#
# class PlaneAdapter:
#     def __init__(self, plane):
#         self.plane = plane
#
#     def travel(self):
#         self.plane.fly()
#
#
# class CarAdapter:
#     def __init__(self, car):
#         self.car = car
#
#     def travel(self):
#         self.car.drive()
#
# class BikeAdapter:
#     def __init__(self, bike):
#         self.bike = bike
#
#     def travel(self):
#         self.bike.ride()