import nmap
import socket
from scapy.all import *
from src.display import *
from tqdm import tqdm
import threading
import os
import time
import sys
import json



class Scanner:
	def __init__(self):
		self.gateway = conf.route.route("0.0.0.0")[2]
		self.gateway = self.gateway+'/24'
		self.up_host = []
		self.important_ports = [20, 21, 22, 53, 80, 123, 179, 443, 500, 587, 3389]

	def scan(self):
		self.nm = nmap.PortScanner()
		self.nm.scan(hosts=self.gateway, arguments='-sn')
		host_list = [(x, self.nm[x]['status']['state']) for x in self.nm.all_hosts()]
		for host, status in host_list:
			self.up_host.append({'host':host, 'mac':getmacbyip(host), 'ports':self.port_scan(host)})
		Output().scan_result(result=self.up_host)
		self.save_log(data=self.up_host)

	def port_scan(self, host):
		self.open_port = []
		print(Fore.YELLOW+Style.BRIGHT+"Scanning For Open Ports in host ["+host+"] among default ports of ",self.important_ports,Style.RESET_ALL)
		for i in tqdm(self.important_ports):
			result = self.nm.scan(host, str(i))
			result = result['scan'][host]['tcp'][i]['state']
			if result == "closed":
				pass
			else:
				self.open_port.append(i)
		return self.open_port
		self.open_port = []

	def save_log(self, data):
		cur_path = os.getcwd()
		t = time.localtime()
		cur_path = cur_path+f'/host_{time.strftime("%H:%M:%S", t)}.log'
		jstr = json.dumps(data)
		with open(cur_path, "w") as jfile:
			jfile.write(jstr)
			jfile.close()



