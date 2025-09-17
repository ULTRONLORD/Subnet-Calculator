# 🔥 Subnet Calculator – Python Project  

Welcome to my **Subnet Calculator** project 🚀.  
This tool was built from a tasked assigned to a friend, but I designed it to be practical, interactive, and fun to use.  

If you’ve ever struggled with subnetting or just wanted a quick way to calculate everything about an IP block — this project is for you.  

---

## ✨ What it Does
- 🏷️ Detects **IP Class (A–E)** automatically  
- 🧮 Calculates:
  - Network Address  
  - Broadcast Address  
  - Number of Valid Hosts  
  - Wildcard Mask  
  - CIDR Notation  
- 🎲 Can **generate random host IPs** from the subnet  
- 💾 Option to **save everything neatly into a report file (`subnet_ips.txt`)**  
- 🔁 Keeps running until you’re done (no need to restart for each subnet)  
- ❌ Smart error handling: if you type something wrong or leave it blank, it just asks you again  

---

## 🖥️ Demo

**Example Run:**

```

📡 Subnet Calculator Project

# 👉 Enter an IP/mask (e.g., 192.168.10.0/26 or just 192.168.10.0): 192.168.1.0/28

# Input: 192.168.1.0/28

IP Class          : Class C
Network Address   : 192.168.1.0
Broadcast Address : 192.168.1.15
Valid Hosts       : 14
Wildcard Mask     : 0.0.0.15
CIDR Notation     : /28
=======================

👉 Do you want to generate random host IPs from this subnet? (y/n): y
How many IPs do you want? (Max 14): 5

🔹 Random Host IPs:

1. 192.168.1.2
2. 192.168.1.6
3. 192.168.1.9
4. 192.168.1.12
5. 192.168.1.14

💾 Do you want to save these IPs to a file? (y/n): y
✅ Saved subnet report to subnet\_ips.txt

```

---

## 📂 Sample Report (`subnet_ips.txt`)

```

# Subnet Report

Input Subnet   : 192.168.1.0/28
IP Class       : Class C
Network Address: 192.168.1.0
Broadcast Addr : 192.168.1.15
Valid Hosts    : 14
Wildcard Mask  : 0.0.0.15
CIDR Notation  : /28

## Generated Random Host IPs

1. 192.168.1.2
2. 192.168.1.6
3. 192.168.1.9
4. 192.168.1.12
5. 192.168.1.14

````


---

## ⚙️ Tech Used
- **Language:** Python 3  
- **Libraries:**  
  - [`ipaddress`](https://docs.python.org/3/library/ipaddress.html) – handles subnetting logic  
  - [`random`](https://docs.python.org/3/library/random.html) – for random host IP generation  

No external dependencies → just run it with plain Python 🐍.  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/subnet-calculator.git
   cd subnet-calculator

2. Run the script:

   python subnet_calculator.py

3. Follow the on-screen prompts


## 💡 Why I Built This

Subnetting is one of those things that can feel intimidating at first. I wanted a project that would:

* Reinforce my networking fundamentals
* Give me hands-on experience with Python’s `ipaddress` module
* Be practical enough to use in labs or troubleshooting scenarios

---

## 🔮 Future Improvements

* Add support for IPv6 🌍
* Export results to `.csv` or `.json` for automation use cases
* Build a simple web UI using Flask or Django

---

## 🙌 Let’s Connect

If you found this useful, feel free to ⭐ the repo!
I’m always open to feedback, collaborations, or just geeking out about networking + Python.

📧 Email: *ezimakoelvis@gmail.com*
💼 LinkedIn: *https://www.linkedin.com/in/elvis-ezimako-cybersecurity*

```
