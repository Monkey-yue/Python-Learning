class Restaurant():
    '''学习：方法初始化，参数的不同定义法与调用，父类继承与覆写'''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 这里设置默认值，如果在形参声明将必须传递实参
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Restaurant is opening")

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='IceCream'):
        # 默认Icecream，传参给父类
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def increment_flavors(self):
        flavors = input("What kind of flavors do you want?")
        self.flavors.append(flavors)
        print("you have " + str(self.flavors) + " now!")


restaurant = Restaurant('kkkk', 'BBQ')
print(restaurant.restaurant_name + '\n' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
ice_cream = IceCreamStand('ice')
ice_cream.increment_flavors()
