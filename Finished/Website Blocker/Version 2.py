import time
from datetime import datetime as dt

sites_to_block = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Window_host
redirect = "127.0.0.1"

#Main Code
def block_websites(start_hour, end_hour):
    while True:
        if (
            dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
            < dt.now()
            < dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
        ):
            print("Do the work ....")
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + " " + site + "\n")
        else:
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print("Good Time")
        time.sleep(3)

#Show Current Sites Being Blocked
def print_list():
    print(sites_to_block)

#Add a site to the list
def add_site(site):
    if not site in sites_to_block:
        sites_to_block.append(site)

#Remove a site from the list
def remove_site(site):
    if site in sites_to_block:
        sites_to_block.remove(site)

def change_time():
    pass

if __name__ == "__main__":
    start_hour = input("Input a time you want to start blocking websites at: ")
    end_hour = input("Input a time you want to unblock websites at: ")
    block_websites(int(start_hour),int(end_hour))