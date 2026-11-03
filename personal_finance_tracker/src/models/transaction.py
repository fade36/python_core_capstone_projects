from decimal import Decimal
from datetime import date
from models.category import Category
from uuid import uuid4

class Transaction:
    def __init__(self, value, category, transaction_date, description):
        self.id = uuid4()
        self.value = value
        self.category = category
        self.transaction_date = transaction_date
        self.description = description
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if not isinstance(value,(int, Decimal)):
            raise TypeError("Value must be integer or decimal")
        
        value = Decimal(value)

        if value <= 0:
            raise ValueError("Value must be greater than 0")
        
        self.__value = value

    @property
    def transaction_date(self):
        return self.__transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        if type(transaction_date) is not date:
            raise TypeError("Date must be a date object")

        self.__transaction_date = transaction_date

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category):
        if not isinstance(category, Category):
            raise TypeError("Category must be a Category object")

        self.__category = category
