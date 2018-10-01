from scapy.all import sniff
import csv
import sys

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


def arp_detect(pkt):
    pktKey = "ARP"
    if pkt[pktKey].op == 1:
        return pkt[pktKey].hwsrc


def main():
    if "--listen" in sys.argv:
        print(sniff(prn=arp_detect, filter="arp", store=0))
    elif "-l" in sys.argv:
        print(sniff(prn=arp_detect, filter="arp", store=0))
    else:
    	for key in buttonDict:
        	print(key + " " + buttonDict[key])
    	print(sniff(prn=button_detect, filter="arp", store=0))


if __name__ == "__main__":
    if "--read" in sys.argv:
        readCSV(sys.argv[sys.argv.index("--read") + 1])
    elif "-r" in sys.argv:
        readCSV(sys.argv[sys.argv.index("-r") + 1])

    main()
