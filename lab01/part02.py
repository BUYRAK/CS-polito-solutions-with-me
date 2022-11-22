def compute_operating_cost(annual_km_driven, years, fuel_cost, km_per_liter):

    annual_fuel_consumed = annual_km_driven / km_per_liter
    annual_fuel_cost = fuel_cost * annual_fuel_consumed
    operating_cost = annual_fuel_cost * years

    return operating_cost

car_1_price = float(input("What is the price of car 1?"))
car_2_price = float(input("What is the price of car 2?"))

car_1_km_per_liter = float(input("How many km does car 1 do with a liter of fuel?"))
car_2_km_per_liter = float(input("How many km does car 2 do with a liter of fuel?"))

years = int(input("How many years will you drive this car? "))
km_per_year = int(input("On average, how many km will you drive each year? "))
fuel_cost = float(input("On average, how much dollars does it coast a liter of fuel? "))

annual_km_driven = years * km_per_year

car_1_operating_cost = compute_operating_cost(annual_km_driven, years,
                                              fuel_cost, car_1_km_per_liter)

car_2_operating_cost = compute_operating_cost(annual_km_driven, years,
                                              fuel_cost, car_2_km_per_liter)

car_1_total_cost = car_1_price + car_1_operating_cost
car_2_total_cost = car_2_price + car_2_operating_cost

if car_1_total_cost < car_2_total_cost:
    print("Car 1 is less expenisve overall")
else:
    print("Car 2 is less expensive overall")