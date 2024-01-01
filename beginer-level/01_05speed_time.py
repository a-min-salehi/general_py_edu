distance = float(input("enter the distance(Km)"))
speed = float(input("enter the speed (km/h)"))

time = distance / speed

h = int(time)
s = int(time % 1 * 60)

print("time = ", h , ":" , s)
