# receive if any update happens
# it is not thread save
# make sure it is thread save


class Observer:
    def update(self, obj, *args, **kwargs):
        raise NotImplementedError


class Observable:
    def __init__(self):
        self._observers = list()

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)
