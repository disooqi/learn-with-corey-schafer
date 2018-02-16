import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('oop.err.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)

# logging.basicConfig(level=logging.INFO, filename='oop.log', format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

class Employee:
    # class variables
    raise_amount = 1.04
    # class method
    def __init__(self, first, last, pay):
        self.first = first # class attribute (instance variable)
        self.last = last
        self.pay = pay
        self._email = first+'.'+last+'@qf.org.qa'
        logger.info('Employee "{}" has been created!'.format(self.__repr__()))

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_mail):
        try:
            self._email = new_mail
            raise Exception
        except Exception:
            logger.exception("Error setting email!")


    @email.deleter
    def email(self):
        logger.info('Email deleted!')
        self._email = None


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def class_method(cls):
        pass

    @classmethod
    def from_string(cls, emp_str):
        f, l, p = emp_str.split('_')
        return cls(f, l, p)

    @staticmethod
    def static_method():
        pass

    def __repr__(self):
        # mostly for debugging and logging
        return 'Employee("{0.first}", "{0.last}", {0.pay})'.format(self)

    def __str__(self):
        return '{0.first} {0.last} - {0.email}'.format(self)

class Dev(Employee):
    raise_amount = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

def main():
    emp_1 = Dev('Mohamed', 'Eldesouki', 2000000, 'Python')
    emp_2_str = "Mariam_Eldesouki_30000000"
    emp_2 = Manager.from_string(emp_2_str)
    emp_3_str = "Fatema_Eldesouki_30000000"

    # print('{0.first} {0.last} takes {0.pay}'.format(emp_1))
    emp_1.apply_raise()
    emp_1.email = 'disooqi@gmail.com'
    # print('{0.first} {0.last} takes {0.pay}'.format(emp_1))
    del emp_1.email
    # print('{0.first} {0.last} takes {0.pay}'.format(emp_1))
    # print(repr(emp_1))
    # print(str(emp_1))

if __name__ == '__main__':
    main()