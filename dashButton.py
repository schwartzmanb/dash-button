from scapy.all import *
import csv

buttonDict = {}

def readCSV():
	for key, val in csv.reader(open("buttons.csv", 'r')):
		buttonDict[key] = val
	
def button_detect(pkt):
	if pkt[ARP].op == 1:
		for i in buttons:
			if pkt[ARP].hwsrc == buttons[i]:
				return buttons[i]
readCSV()
for key in buttonDict:
	print(key + buttonDict[key])

print(sniff(prn=button_detect, filter="arp", store=0))
