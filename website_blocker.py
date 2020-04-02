import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list = []

# Take website list from file
with open("website_list.txt") as file:
    for line in file:
        split = line.split()[0]
        website_list.append(split)

while True:
    # range from 8am - 4pm
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours...")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                # checks all websotes in website list for the if statement
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")

    time.sleep(5)
