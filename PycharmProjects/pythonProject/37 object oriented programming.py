from car import Car

car_1 = Car("Chevy","Malibu",2004,"Tan")
car_2 = Car("Honda","Accord",2016,"Black")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()