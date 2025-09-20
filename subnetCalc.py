import ipaddress
import random

# -------------------------------
# Function to determine IP Class
# -------------------------------
def get_ip_class(ip):
    """Determine the class of an IPv4 address using its first octet."""
    first_octet = int(str(ip).split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 254:
        return "Class E (Experimental)"
    else:
        return "Invalid or Reserved"


# ------------------------------------------------
# Function to return default subnet if /prefix is missing
# ------------------------------------------------
def get_default_prefix(ip):
    """Assign default subnet mask prefix if user does not enter one."""
    ip_class = get_ip_class(ip)

    if ip_class == "Class A":
        return 8
    elif ip_class == "Class B":
        return 16
    elif ip_class == "Class C":
        return 24
    else:
        return 24


# ----------------------------------------
# Main subnet calculator logic
# ----------------------------------------
def subnet_calculator(ip_with_prefix):
    try:
        # If user didn’t add a /prefix → add default prefix based on IP class
        if "/" not in ip_with_prefix:
            ip_only = ip_with_prefix.strip()
            prefix = get_default_prefix(ip_only)
            ip_with_prefix = f"{ip_only}/{prefix}"

        # Convert to IP network object
        network = ipaddress.ip_network(ip_with_prefix, strict=False)

        # Get IP class
        ip_class = get_ip_class(network.network_address)

        # -------- Display subnet details --------
        print("="*65)
        print(f" Input: {ip_with_prefix}")
        print("="*65)
        print(f" IP Class          : {ip_class}")
        print(f" Subnet Mask       : {network.netmask}")
        print(f" CIDR Notation     : /{network.prefixlen}")
        print(f" Network Address   : {network.network_address}")
        print(f" Broadcast Address : {network.broadcast_address}")
        valid_hosts = max(network.num_addresses - 2, 0)
        print(f" Valid Hosts       : {valid_hosts}")
        print(f" Wildcard Mask     : {ipaddress.IPv4Address(int(network.hostmask))}")
        print("="*65 + "\n")

        # -------- Generate random IPs option --------
        if valid_hosts > 0:  
            choice = input("👉 Do you want to generate random host IPs from this subnet? (y/n): ").lower()
            if choice == "y":
                try:
                    num = int(input(f"How many IPs do you want? (Max {valid_hosts}): "))

                    if num > valid_hosts:
                        print(f"⚠ Too many requested! Showing maximum {valid_hosts} IPs instead.\n")
                        num = valid_hosts

                    all_hosts = list(network.hosts())
                    random_ips = random.sample(all_hosts, num)

                    print("\n🔹 Random Host IPs:")
                    for i, ip in enumerate(random_ips, start=1):
                        print(f"   {i}. {ip}")
                    print("\n")

                    # Ask to save to file
                    save_choice = input(" Do you want to save these IPs to a file? (y/n): ").lower()
                    if save_choice == "y":
                        filename = "subnet_ips.txt"
                        with open(filename, "w") as f:
                            f.write("Subnet Report\n")
                            f.write("=============\n")
                            f.write(f"Input Subnet   : {ip_with_prefix}\n")
                            f.write(f"IP Class       : {ip_class}\n")
                            f.write(f"Subnet Mask    : {network.netmask}\n")
                            f.write(f"CIDR Notation  : /{network.prefixlen}\n")
                            f.write(f"Network Address: {network.network_address}\n")
                            f.write(f"Broadcast Addr : {network.broadcast_address}\n")
                            f.write(f"Valid Hosts    : {valid_hosts}\n")
                            f.write(f"Wildcard Mask  : {ipaddress.IPv4Address(int(network.hostmask))}\n\n")

                            f.write("Generated Random Host IPs\n")
                            f.write("-------------------------\n")
                            for i, ip in enumerate(random_ips, start=1):
                                f.write(f"{i}. {ip}\n")

                        print(f"✅ Saved subnet report to {filename}\n")

                except ValueError:
                    print("⚠ Invalid number entered.\n")

        return True  # success  #yipee

    except ValueError as e:
        print(f"❌ Invalid input '{ip_with_prefix}': {e}\n")
        return False  # failed


# ----------------------------------------
# MAIN PROGRAM
# ----------------------------------------
def main():
    print("\n📡 Subnet Calculator\n")

    while True:
        while True:
            user_input = input("👉 Enter an IP/mask (e.g., 192.168.10.0/26 or just 192.168.10.0): ")

            if not user_input.strip():
                print("⚠ No input provided. Please try again.\n")
                continue

            if subnet_calculator(user_input):
                break

        again = input("🔁 Do you want to calculate another subnet? (y/n): ").lower()
        if again != "y":
            print("\n✅ Thanks for using the Subnet Calculator. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
