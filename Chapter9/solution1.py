class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0} has {1}".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("{0} is open".format(self.restaurant_name))

restaurant = Restaurant("Uncreative Name", "Food")
print("Name: {0}".format(restaurant.restaurant_name))
print("Food type: {0}".format(restaurant.cuisine_type))

restaurant.open_restaurant()
restaurant.describe_restaurant()
