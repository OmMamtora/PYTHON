def f_to_c(farenheit):
    
    c = 5*(f - 32) / 9
    return c

f = int(input("Enter temperature in farenhhrit:->"))

result = f_to_c(f)

print(f"Farenheit : {f} \ncelcius : {round(result,2)}°C")