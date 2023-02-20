import random
print("Do you want to roll a dice?")
response = "y"
while response == "y":
    no = random.radiant(1,6)
if no == 1:
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[     ]")
    print("[-----]")

if no == 2:
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[   0 ]")
    print("[-----]")

if no == 3:
    print("[-----]")
    print("[ 0   ]")
    print("[     ]")
    print("[     ]")
    print("[-----]")

if no == 4:
    print("[-----]")
    print("[ 0 0 ]")
    print("[   0 ]")
    print("[ 0   ]")
    print("[-----]")

if no == 5:
    print("[-----]")
    print("[ 0  0]")
    print("[  0  ]")
    print("[ 0 0 ]")
    print("[-----]")

if no == 6:
    print("[-----]")
    print("[ 0 0 ]")
    print("[  0 0]")
    print("[0  0 ]")
    print("[-----]")

response = input("press Y to roll again and N to exit")
print("/n")

