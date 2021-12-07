from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = 'This code works!'
        return result


class ConcreteCreator1(Creator):

    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):

    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteProduct1(Product):

    def operation(self):
        return 'Result of operation of Product1'


class ConcreteProduct2(Product):

    def operation(self):
        return 'Result of operation of Product2'


def client_code(creator: Creator):
    print('Client: I\'m not aware of the creator\'s class, but it still works. \n', f'{creator.some_operation()}', end='')


if __name__ == '__main__':
    print('App: launched with ConcreteCreator1.')
    client_code(ConcreteCreator1())
    print('\n')

    print('App: launched with ConcreteCreator2.')
    client_code(ConcreteCreator2())

