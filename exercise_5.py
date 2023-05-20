name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
my_teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print('Actually that\'s not too heavy.')
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")


print('------------')
print('Study Drills')

# convert inches to centimeters
height_in_centimeters = height * 2.54
print(f"His height in centimeters is {round(height_in_centimeters, 2)}.")

# convert pounds to kilograms
weight_in_kilograms = weight * 0.45359237
print(f"His weight in kilograms is {round(weight_in_kilograms, 2)}.")