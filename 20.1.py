#20.1 task /1
# class BikeListing:
#     def __init__(self, reserve_price):
#         self.set_reserve_price(reserve_price)

#     def get_reserve_price(self):
#         return self.__reserve_price

#     def set_reserve_price(self, value):
#         if value <= 0:
#             raise ValueError("Price must be greater than 0")
#         self.__reserve_price = value

# b1 = BikeListing(35000)
# print("Reserve Price:", b1.get_reserve_price())

# # print(b1.__reserve_price)
# Reserve Price: 35000
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

#20.2 task/2
# class BikeListing:
#     def __init__(self, reserve_price):
#         self.reserve_price = reserve_price

#     @property
#     def reserve_price(self):
#         return self.__reserve_price

#     @reserve_price.setter
#     def reserve_price(self, value):
#         if value < 5000 or value > 200000:
#             raise ValueError("Price must be between 5000 and 200000")
#         self.__reserve_price = value

# listing = BikeListing(30000)

# for price in (2000, 15000, 120000, 250000):
#     try:
#         listing.reserve_price = price
#         print(price, "-> ACCEPTED")
#     except ValueError as err:
#         print(price, "->", err)
# 2000 -> Price must be between 5000 and 200000
# 15000 -> ACCEPTED
# 120000 -> ACCEPTED
# 250000 -> Price must be between 5000 and 200000
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft

#20.3 task/3
# from abc import ABC, abstractmethod

# class Listing(ABC):
#     @abstractmethod
#     def final_price(self):
#         pass

# temp = Listing()  # TypeError: Can't instantiate abstract class Listing

# class BikeListing(Listing):
#     def __init__(self, reserve_price):
#         self.reserve_price = reserve_price

#     @property
#     def reserve_price(self):
#         return self.__reserve_price

#     @reserve_price.setter
#     def reserve_price(self, value):
#         if value < 5000 or value > 200000:
#             raise ValueError("Price must be between 5000 and 200000")
#         self.__reserve_price = value

#     def final_price(self):
#         return round(self.reserve_price + (self.reserve_price * 0.02))

# bike = BikeListing(50000)
# print("Reserve Price:", bike.reserve_price)
# print("Final Price (with 2% fee):", bike.final_price())
# Reserve Price: 50000
# Final Price (with 2% fee): 51000
# PS C:\Users\ANSARI ANAM\AppData\Local\Programs\Microsoft VS Code> 

#20.4 task /4
# from abc import ABC, abstractmethod

# class Listing(ABC):
#     @abstractmethod
#     def final_price(self):
#         pass

# class BikeListing(Listing):
#     def __init__(self, reserve_price):
#         self.reserve_price = reserve_price

#     @property
#     def reserve_price(self):
#         return self.__reserve_price

#     @reserve_price.setter
#     def reserve_price(self, value):
#         if value < 5000 or value > 200000:
#             raise ValueError("Price must be between 5000 and 200000")
#         self.__reserve_price = value

#     def final_price(self):
#         return round(self.reserve_price + (self.reserve_price * 0.02))

# test_prices = (0, -100, 500, 5000, 30000, 250000)

# for price in test_prices:
#     try:
#         bike = BikeListing(price)
#         print(f"{price} -> ACCEPTED | Final Price: {bike.final_price()}")
#     except ValueError as err:
#         print(f"{price} -> REJECTED ({err})")
# 0 -> REJECTED (Price must be between 5000 and 200000)
# -100 -> REJECTED (Price must be between 5000 and 200000)
# 500 -> REJECTED (Price must be between 5000 and 200000)
# 5000 -> ACCEPTED | Final Price: 5100
# 30000 -> ACCEPTED | Final Price: 30600
# 250000 -> REJECTED (Price must be between 5000 and 200000)