from scapy.all import sniff
import csv

buttonDict = {}

def readCSV():
	for key, val in csv.reader(open("buttons.csv", 'r')):
		buttonDict[key] = val
	
def button_detect(pkt):
	pktKey = "ARP"
	if pkt[pktKey].op == 1:
		for i in buttonDict:
			if pkt[pktKey].hwsrc == buttonDict[i]:
				return buttonDict[i]

#readCSV()

#print(sniff(prn=button_detect, filter="arp", store=0))

def main():
	readCSV()
	for key in buttonDict:
		print(key + " " + buttonDict[key])
	print(sniff(prn=button_detect, filter="arp", store=0))

if __name__ == "__main__":
	main()