names = [] # Separate names and birthdates
birth_days = [] # Separate names and birthdates

f = open("DOB.txt", "r") # Open the file and read its lines
data = f.readlines()

for line in data:           
    parts = line.split()          # To split each line 
    names.append(parts[:2])       # To store the name
    birth_days.append(parts[2:])  # To store the bday

f.close()

print("Names")                                        # To Print names Heading
for i, name in enumerate(names, start=1):
    print("{}. {}".format(i, " ".join(name)))         # To Print names 

print("\nBirth Dates")                                # To Print Birth Dates Heading
for i, birth_day in enumerate(birth_days, start=1):
    print("{}. {}".format(i, " ".join(birth_day)))    # To Print Birthdays