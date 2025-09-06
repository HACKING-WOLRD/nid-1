
import os, sys, time, random

# Colors
R = '\033[1;31m'; G = '\033[1;32m'; Y = '\033[1;33m'
C = '\033[1;36m'; M = '\033[1;35m'; W = '\033[1;37m'; RESET = '\033[0m'

def clear(): os.system("clear")

def banner():
    print(f"""{M}
 ███╗   ██╗███╗   ██╗███████╗██████╗ ██╗ ██████╗ 
 ████╗  ██║████╗  ██║██╔════╝██╔══██╗██║██╔═══██╗
 ██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝██║██║   ██║
 ██║╚██╗██║██║╚██╗██║██╔══╝  ██╔═══╝ ██║██║   ██║
 ██║ ╚████║██║ ╚████║███████╗██║     ██║╚██████╔╝
 ╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝ ╚═════╝ 
          {C}VIP Number Info Finder — work
""" + RESET)

def loading(txt, t=2):
    for i in range(t*4):
        sys.stdout.write(Y + f"\r{txt}" + "."*(i%4) + RESET)
        sys.stdout.flush()
        time.sleep(0.3)
    print()

def fake_info(number):
    names = ["Rakib Hasan","Tamanna Akter","Sajib Rahman","Nusrat Jahan","Atik Khan","Mehedi Hasan","Mahiya Akter"]
    fathers = ["Abdul Karim","Jalal Uddin","Kamrul Hasan","Shafiqul Islam"]
    mothers = ["Rokeya Begum","Salma Akter","Shirin Sultana","Hasina Khatun"]
    areas = ["Dhaka, Bangladesh","Chattogram, Bangladesh","Barishal, Bangladesh","Sylhet, Bangladesh","Khulna, Bangladesh","Rajshahi, Bangladesh"]
    
    nid = str(random.randint(1000000000,9999999999))
    print(f"{G}[✓] Phone Number: {W}{number}")
    print(f"{G}[✓] NID Number  : {W}{nid}")
    print(f"{G}[✓] Name        : {W}{random.choice(names)}")
    print(f"{G}[✓] Father Name : {W}{random.choice(fathers)}")
    print(f"{G}[✓] Mother Name : {W}{random.choice(mothers)}")
    print(f"{G}[✓] Location    : {W}{random.choice(areas)}")
    print(f"{Y}[i] SIM Registered Date: {W}{random.randint(2015,2023)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}")
    print(f"{M}─────────────────────────────────────────────{RESET}")

def main():
    clear()
    banner()
    number = input(C + "[+] Enter Phone Number: " + W)
    print()
    loading("Connecting to Govt Database", 3)
    loading("Fetching SIM Registration Details", 2)
    loading("Bypassing Security Layer", 2)
    print()
    fake_info(number)
    input(Y + "\nPress Enter to exit..." + RESET)

if __name__ == "__main__":
    main()