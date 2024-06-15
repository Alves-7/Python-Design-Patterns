# -*- coding: utf-8 -*-
# @FileName : pizza_factory.py.py
# @Time : 2024/6/11 22:00
# @Author : Alves
"""
 假设开办了一家披萨点，供应印式和美式披萨。为此，先创建一个抽象基类——PizzaFactory(AbstractFactory见UML图)。
 PizzaFactory类有两个抽象基类即createVegPizza()和createNonVegPizza()。他们需要痛过ConcreteFactory类来实现。
"""
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    @abstractmethod
    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class UsaPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


"""
 按照上述代码已实现UML图。接下来。定义ChickenPizza和HamPizza，并实现server()方法。
"""

class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, VegPizza):
        pass


class NovegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class ChickenPizza(NovegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Chicken on", type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare", type(self).__name__)


class HamPizza(NovegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, "is served with Ham on", type(VegPizza).__name__)


"""
 当用户来到披萨店并要一份美式非素食披萨的时候，UsaPizzaFactory负责准备素食，然后在上面加上火腿，马上就变成非素食披萨了！
"""

class PizzaStore:
    def __init__(self):
        pass

    def makePizzas(self):
        for factory in [IndianPizzaFactory(), UsaPizzaFactory()]:
            self.factory = factory
            self.NonVegPizza = self.factory.createNonVegPizza()
            self.VegPizza = self.factory.createVegPizza()
            self.VegPizza.prepare()
            self.NonVegPizza.serve(self.VegPizza)


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.makePizzas()
