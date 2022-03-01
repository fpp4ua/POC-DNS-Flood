# POC-DNS-Flood

_Note_: This is a POC (Proof Of Concept) attack that floods DNS servers, run at your own risk.

## Running
``` sh
python3 -m pip install -r requirements.txt
sudo python3 main.py
```

Full steps from a bash terminal
``` bash
# install git, python3 and python3-pip
sudo apt update
sudo apt install -y git python3 python3-pip

# clone this repo
git clone https://github.com/fpp4ua/POC-DNS-Flood.git

cd POC-DNS-Flood

# install requirements (scapy)
python3 -m pip install -r requirements.txt

# run - sudo is needed to send raw packets
sudo python3 main.py
```

## Options

`FPP_INTERVAL_MS` - set the sending frequency in milliseconds, defaults to 500ms (half a second)
`DO_PRINT` - set to "f" to turn off printing to standard out, defaults to "t" (prints out)
