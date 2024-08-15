```markdown
# MacSpoofer

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

## 🌐 Overview

**MacSpoofer** is a powerful and intuitive Python script tailored for cybersecurity enthusiasts and professionals. It provides seamless automation to spoof the MAC address of a network interface and effortlessly manage WiFi connections. Whether you are testing network security or simply exploring, this tool simplifies the process with just a few commands.

## ✨ Features

- **MAC Address Spoofing**: Instantly change your network interface's MAC address to any desired address.
- **WiFi Network Management**: Automatically add and connect to WiFi networks. If a network already exists, it intelligently skips re-adding and directly connects.
- **Root Privileges Verification**: Ensures the script is executed with the necessary root privileges for all operations.
- **Cross-Interface Compatibility**: Supports a wide range of network interfaces on Linux systems.
- **Comprehensive Logging**: All actions are logged into `mac_spoof.log` for easy troubleshooting and audit purposes.

## 🛠️ Prerequisites

- **Linux Operating System**
- **Python 3.x**
- `nmcli` (NetworkManager Command Line Interface)
- `macchanger`
- `colorama`

## 📦 Installation

1. **Clone the Repository**  
   Start by cloning the repository to your local machine:
   ```bash
   git clone https://github.com/kaleemullahkhan786/MacSpoofer.git
   cd MacSpoofer.py
   ```

2. **Install Dependencies**  
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Run the Script**  
   Execute the script with root privileges:
   ```bash
   sudo python3 MacSpoofer.py
   ```

2. **Follow Prompts**  
   - **Network Interface**: Enter the name of your network interface (e.g., `wlan0`).
   - **Target MAC Address**: Enter the MAC address you wish to spoof (e.g., `00:11:22:33:44:55`).
   - **WiFi SSID**: Enter the SSID of the WiFi network.
   - **WiFi Password**: Enter the password for the WiFi network.

### 📖 Example

```bash
$ sudo python3 MacSpoofer.py

888b     d888                   .d8888b.                              .d888                 
8888b   d8888                  d88P  Y88b                            d88P                  
88888b.d88888                  Y88b.                                 888                    
888Y88888P888  8888b.   .d8888b "Y888b.   88888b.   .d88b.   .d88b.  888888 .d88b.  888d888 
888 Y888P 888     "88b d88P"       "Y88b. 888 "88b d88""88b d88""88b 888   d8P  Y8b 888P"   
888  Y8P  888 .d888888 888           "888 888  888 888  888 888  888 888   88888888 888     
888   "   888 888  888 Y88b.   Y88b  d88P 888 d88P Y88..88P Y88..88P 888   Y8b.     888     
888       888 "Y888888  "Y8888P "Y8888P"  88888P"   "Y88P"   "Y88P"  888    "Y8888  888     
                                          888                                               
                                          888                                               
                                          888                                              
                                                                 

Coder: Kaleemullah Khan
MacSpoofer Version: 1.1

Program Started .....
Enter the network interface: wlan0
Enter the target MAC address: 18:ce:94:c3:6a:f8
Enter the WiFi SSID (network name): TP-LINK_5B1866
Enter the WiFi password: 11221122
[Console] ===> Disabling WPA service
[Console] ===> Killing the Network and Libs for WPA service
[Console] ===> Starting the Network and Libs for WPA service
[Console] ===> Bringing the Interface Down
[Console] ===> Changing the MAC Address on Interface wlan0 to 18:ce:94:c3:6a:f8
[Console] ===> Enabling the interface: wlan0 up
[Console] ===> Starting a Network Manager Service
[Console] ===> Done
[Console] ===> Configuring WiFi network TP-LINK_5B1866
Connection 'TP-LINK_5B1866' (924b7a5a-7bf7-4a14-b19e-965b3ea21498) successfully added.
[Console] ===> WiFi network TP-LINK_5B1866 configured successfully.
[Console] ===> Successfully connected to TP-LINK_5B1866
[Console] ===> All operations completed successfully.
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## ⚠️ Disclaimer

This script is intended for ethical hacking and educational purposes only. **Do not** use it on networks or systems without proper authorization. Misuse of this tool could result in legal consequences.

---

**WiFi-MAC-Spoofer** © 2024 by [Your Name]. Proudly developed for the cybersecurity community.
```
 
