class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered: bool = False

    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered is True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += quantity * price_per_ingredient

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_ingredient: float):
        if self.ordered is True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if not quantity <= self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_ingredient

    def make_order(self):
        self.ordered = True
        ingredients_list = []
        for key, val in self.ingredients.items():
            ingredients_list.append(f"{key}: {val}")
        ingredients_string = ", ".join(ingredients_list)
        return f"You've ordered pizza {self.name} prepared with " \
               f"{ingredients_string} and the price will be {self.price}lv."  # {self.price:2.f}???

#
# margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# margarita.add_extra('mozzarella', 1, 0.5)
# margarita.add_extra('cheese', 1, 1)
# margarita.remove_ingredient('cheese', 1, 1)
# print(margarita.remove_ingredient('bacon', 1, 2.5))
# print(margarita.remove_ingredient('tomatoes', 2, 0.5))
# margarita.remove_ingredient('cheese', 2, 1)
# print(margarita.make_order())
# print(margarita.add_extra('cheese', 1, 1))

# AssertionError: "You'[31 chars]ared with cheese: 2, tomatoes: 1,  and the price will be 12lv." != "You'[31 chars]ared with cheese: 2, tomatoes: 1 and the price will be 12lv."
# - You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1,  and the price will be 12lv.
# ?                                                                    --
# + You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 1 and the price will be 12lv.
