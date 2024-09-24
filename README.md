# CheckProx

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
python3 CheckProxies.py
Enter the path to your proxies file when prompted.

The valid proxies will be saved in a file named Valid_Proxies.txt.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
@ALHARAMM
