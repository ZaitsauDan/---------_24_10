import unittest

# Abstract classes for products
class AbstractProductA:
    def operation(self):
        pass

class AbstractProductB:
    def operation(self):
        pass

# Concrete products A1 and A2
class ConcreteProductA1(AbstractProductA):
    def operation(self):
        return "Operation result A1"

class ConcreteProductA2(AbstractProductA):
    def operation(self):
        return "Operation result A2"

# Concrete products B1 and B2
class ConcreteProductB1(AbstractProductB):
    def operation(self):
        return "Operation result B1"

class ConcreteProductB2(AbstractProductB):
    def operation(self):
        return "Operation result B2"

# Abstract factory
class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass

# Concrete factories 1 and 2
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

class TestAbstractFactory(unittest.TestCase):
    def test_factory1(self):
        factory = ConcreteFactory1()
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()

        self.assertEqual(product_a.operation(), "Operation result A1")
        self.assertEqual(product_b.operation(), "Operation result B1")

    def test_factory2(self):
        factory = ConcreteFactory2()
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()

        self.assertEqual(product_a.operation(), "Operation result A2")
        self.assertEqual(product_b.operation(), "Operation result B2")

if __name__ == "__main__":
    unittest.main()