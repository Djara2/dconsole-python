import os
os.system("sudo apt install python3-pip")
os.system("sudo apt install w3m")
os.system("pip install pyperclip")
os.system("pip install rich")
systemType = input("Are you on mobile? ")
if systemType != "y":
    os.system("sudo apt-get install python3-tk python3-dev")



