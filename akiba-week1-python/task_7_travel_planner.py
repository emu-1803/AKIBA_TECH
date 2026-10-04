destination = input("Destination: ")
distance = float(input("Distance in kilometers: "))
speed = float(input("Average speed in km/h: "))

time = distance / speed

hours=int(time)
minutes=int((time-hours)*60)

print()
print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Average Speed: {speed} km/h")
print(f"Estimated Travel Time: {hours} hours and {minutes} minutes")