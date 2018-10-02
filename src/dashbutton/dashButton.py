from scapy.all import sniff
import csv
import sys
from vendorDiscovery import returnManufacturor

buttonDict = {}

# Open csv file from path specified
def readCSV(filename):
    try:
        csvFile = open(filename, 'r')
    except IOError:
        print("File does not exist.")
        return 1
    for key, val in csv.reader(csvFile):
        buttonDict[key] = val

# Return key of button (name) upon detection of MAC address
def button_detect(pkt):
    pktKey = "ARP"
    if pkt[pktKey].op == 1:
        for i in buttonDict:
            if pkt[pktKey].hwsrc == buttonDict[i]:
                return buttonDict[i]

# Continously detect all ARP packets and output their MAC address
def arp_detect(pkt):
    pktKey = "ARP"
    if pkt[pktKey].op == 1:
        mac = pkt[pktKey].hwsrc
        vendor = returnManufacturor(mac)
        return "MAC: " + mac + " Vendor: " + vendor


def main():
    if "--listen" in sys.argv or "-l" in sys.argv:
        print(sniff(count=100, prn=arp_detect, filter="arp", store=0))
    else:
        for key in buttonDict:
            print(key + " " + buttonDict[key])
        print(sniff(prn=button_detect, filter="arp", store=0))


if __name__ == "__main__":
    if "--read" in sys.argv or "-r" in sys.argv:
        if "--read" in sys.argv:
            argIndex = sys.argv.index("--read")
        else:
            argIndex = sys.argv.index("-r")
        readCSV(sys.argv[argIndex + 1])
    main()
