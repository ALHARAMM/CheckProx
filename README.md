# CheckProx
![Screenshot from 2024-09-23 22-18-39](https://github.com/user-attachments/assets/d7cb8a0c-6934-442f-a0f2-d8d86c5d2e51)

## Overview
This is a simple Python script that checks the validity of a list of proxies. It tests each proxy against a specified URL and outputs valid proxies to a file.

## Features
- Read proxy lists from a file.
- Test proxies concurrently for faster execution.
- Save valid proxies to a separate file.
- Simple command-line interface.

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ALHARAMM/CheckProx.git
   cd CheckProx
2. Install the required library: 
   pip install requests
## Usage
Create a text file (e.g., Proxies.txt) with proxies listed one per line in the format http://user:pass@host:port or just http://host:port.

## Run the script:
3. ```bash
   python3 CheckProx.py
The valid proxies will be saved in a file named Valid_Proxies.txt.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **ALHARAMM** - [GitHub Profile](https://github.com/ALHARAMM)

