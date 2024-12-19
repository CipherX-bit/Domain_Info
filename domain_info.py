import subprocess
import time
import socket
import whois
from datetime import datetime

def logo():
    # Logo that gets printed before the update starts
    print('''
 ______   _______  _______  _______ _________ _            _________ _        _______  _______ 
(  __  \ (  ___  )(       )(  ___  )\__   __/( (    /|     \__   __/( (    /|(  ____ \(  ___  )
| (  \  )| (   ) || () () || (   ) |   ) (   |  \  ( |        ) (   |  \  ( || (    \/| (   ) |
| |   ) || |   | || || || || (___) |   | |   |   \ | |        | |   |   \ | || (__    | |   | |
| |   | || |   | || |(_)| ||  ___  |   | |   | (\ \) |        | |   | (\ \) ||  __)   | |   | |
| |   ) || |   | || |   | || (   ) |   | |   | | \   |        | |   | | \   || (      | |   | |
| (__/  )| (___) || )   ( || )   ( |___) (___| )  \  |     ___) (___| )  \  || )      | (___) |
(______/ (_______)|/     \||/     \|\_______/|/    )_)_____\_______/|/    )_)|/       (_______)
By CipherX (https://github.com/YassineDouadi)        (_____)                                   
''')

def format_date(date):
    if isinstance(date, list):
        return date[0].strftime("%Y-%m-%d %H:%M:%S") if date else "N/A"
    elif isinstance(date, datetime):
        return date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return "N/A"

def get_domain_info(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"\nIP Address: {ip_address}")
    except socket.gaierror:
        print("Error: Unable to resolve domain name.")
        return

    try:
        domain_info = whois.whois(domain_name)
        print("\n--- Domain Information ---")
        print(f"Domain Name     : {domain_info.domain_name if domain_info.domain_name else 'N/A'}")
        print(f"Registrar       : {domain_info.registrar if domain_info.registrar else 'N/A'}")
        print(f"Creation Date   : {format_date(domain_info.creation_date)}")
        print(f"Expiration Date : {format_date(domain_info.expiration_date)}")
        print(f"Nameservers     : {', '.join(domain_info.name_servers) if domain_info.name_servers else 'N/A'}")
        
        if hasattr(domain_info, 'registrant_name') and domain_info.registrant_name:
            print(f"Registrant Name : {domain_info.registrant_name}")
        else:
            print("Registrant Name : Not available or redacted for privacy.")
    except Exception as e:
        print(f"Error retrieving WHOIS information: {e}")

def about_us():
    print('''
About Us:
This script, created by CipherX, is a tool for retrieving domain information (IP address, WHOIS details, etc.).
You can learn more about this project or contribute at: https://github.com/YassineDouadi
''')

def help_menu():
    print('''
Help:
1. Domain Info: Enter a domain name to retrieve its IP address and WHOIS information.
2. About Us: Learn about this script and its creator.
3. Help: View this help menu.
4. Update Domain_Info: Future feature (under development).
x. Exit: Quit the script.
''')

def update_domain_info():
    """Simulates updating the tool."""
    logo()
    print("Updating Domain_Info.........")
    time.sleep(1)

    try:
        # Simulate Git clone and installation commands
        subprocess.run(["git", "clone", "https://github.com/YassineDouadi/Domain_Info.git", "~/Domain_Info"], check=True)
        subprocess.run(["sh", "install"], cwd="~/Domain_Info", check=True)
        print("IP-Domain_Info updated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during update: {e}")
    except FileNotFoundError:
        print("Git or installation command not found. Please ensure you have Git and shell installed.")

    time.sleep(1)

if __name__ == "__main__":
    while True:
        print('''
 ______   _______  _______  _______ _________ _            _________ _        _______  _______ 
(  __  \ (  ___  )(       )(  ___  )\__   __/( (    /|     \__   __/( (    /|(  ____ \(  ___  )
| (  \  )| (   ) || () () || (   ) |   ) (   |  \  ( |        ) (   |  \  ( || (    \/| (   ) |
| |   ) || |   | || || || || (___) |   | |   |   \ | |        | |   |   \ | || (__    | |   | |
| |   | || |   | || |(_)| ||  ___  |   | |   | (\ \) |        | |   | (\ \) ||  __)   | |   | |
| |   ) || |   | || |   | || (   ) |   | |   | | \   |        | |   | | \   || (      | |   | |
| (__/  )| (___) || )   ( || )   ( |___) (___| )  \  |     ___) (___| )  \  || )      | (___) |
(______/ (_______)|/     \||/     \|\_______/|/    )_)_____\_______/|/    )_)|/       (_______)
By CipherX (https://github.com/YassineDouadi)        (_____)                                   
''')

        print('''
[1] Get Domain Info
[2] About Us
[3] Help
[4] Update Domain_Info
[x] Exit
''')
        choice = input("Enter your choice: ").strip().lower()
        
        if choice == "1":
            domain = input("Enter the domain name (e.g., example.com): ").strip()
            if domain:
                get_domain_info(domain)
            else:
                print("Please enter a valid domain name.")
        elif choice == "2":
            about_us()
        elif choice == "3":
            help_menu()
        elif choice == "4":
            update_domain_info()
        elif choice == "x":
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
