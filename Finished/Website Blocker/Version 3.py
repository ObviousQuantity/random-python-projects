import time
from datetime import datetime as dt
import thread

sites_to_block = [
    "test",
    "test1"
]

Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Window_host
redirect = "127.0.0.1"

class WebBlocker:
    start_hour = 0
    end_hour = 0

    #Main Code
    @classmethod
    def block_websites(cls):
        print(f"blocking sites from {cls.start_hour} to {cls.end_hour}")
        while True:
            if (
                dt(dt.now().year, dt.now().month, dt.now().day, cls.start_hour)
                < dt.now()
                < dt(dt.now().year, dt.now().month, dt.now().day, cls.end_hour)
            ):
                print("Work Time")
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
                print("Fun Time")
            time.sleep(3)

    #Show Current Sites Being Blocked
    def print_list(self):
        print(sites_to_block)

    #Add a site to the list
    def add_site(self,site):
        if not site in sites_to_block:
            sites_to_block.append(site)
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + " " + site + "\n")
            print(f"{site} is now being blocked")

    #Remove a site from the list
    def remove_site(self,site):
        with open(default_hoster, "r") as hostfile:
            hosts = hostfile.readlines()

        with open(default_hoster, "w") as hostfile:
            for line in hosts:
                if line.strip("\n") != f"{redirect} {site}": #note to self: look up what strip does (my guess is it just removes that line)
                    hostfile.write(line)
                    print(f"{site} is no longer being blocked") 

    #Change the time
    @classmethod
    def change_time(cls):
        start_hour = input("Input a time you want to start blocking websites at: ")
        end_hour = input("Input a time you want to unblock websites at: ")
        cls.start_hour = int(start_hour)
        cls.end_hour = int(end_hour)   
        cls.block_websites()

if __name__ == "__main__":
    wb = WebBlocker()
    wb.change_time()
    wb.change_time()
    #wb.remove_site("test")
    #wb.change_time()
    #wb.add_site("test")