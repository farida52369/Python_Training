# ################### Self Control -- To work without distructions
# ################### Creator: Fareeda Ragab

# The modules we need
import time
from datetime import datetime as dt

# Your PC Local Host
local_host = "127.0.0.1"
# The Websites U wanna Stop them
website_wanna_block = ["www.facebook.com", "facebook.com"]
# The file You wanna Access From your system -- This line of code works for Ubuntu and Mac -- Not windows
host_file = "/etc/hosts"


# The Main Function
def self_control():
    # Making timing to restrict the time u could unblock and block the webs
    # I made the blocking (9am, 14pm) --  make your own timing
    if dt(dt.now().year,
          dt.now().month,
          dt.now().day, 9) < dt.now() < dt(dt.now().year,
                                           dt.now().month,
                                           dt.now().day, 14):
        # Openning the file to add the webs u wanna block
        with open(host_file, "r+") as f:
            content = f.read()
            for website in website_wanna_block:
                if website in content:
                    pass
                else:
                    f.write(local_host + " " + website + "\n")
        print("Websites have blocked successfully!!")

    else:
        # Openning the file to remove the webs if found in
        with open(host_file, "r+") as f:
            content = f.readlines()
            f.seek(0)
            # Like Making the cursor of the editing in the very beginning of the file
            for line in content:
                if not any(website in line for website in website_wanna_block):
                    f.write(line)
            f.truncate()
        print("Websites Successfully Unblocked!")


# The Base
if __name__ == "__main__":
    self_control()

# The End :)
