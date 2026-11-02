class Category:
    def __init__(self, category, category_type):
        self.category = category
        self.category_type = category_type

    @property
    def category_type(self):
        return self.__category_type
    
    @category_type.setter
    def category_type(self, category_type):
        if category_type not in ("income", "expense"):
            raise ValueError("Transaction type must be either income or expense")
        self.__category_type = category_type