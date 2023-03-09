from colorama import Fore, Back, Style
from prettytable import PrettyTable
from scapy.all import *
import pandas
from IPython.display import display

class Output:
	def __init__(self):
		self.f = Fore
		self.b = Back
		self.s = Style

	def out_root(self):
		table = PrettyTable(['Commands', 'Description'])
		table.align = 'c'
		table.add_row(["modules", "To Show the Modules."])
		table.add_row(["clear", "To Clear Screen."])
		table.add_row(["scan", "To scan the Entire network."])
		table.add_row(["exit", "To Quit the program."])
		table.add_row(["about", "About the author."])
		print(Style.BRIGHT,table)


	def Modules(self):
		table = PrettyTable(['Modules', 'Description'])
		table.align = "c"
		table.add_row(["mitm", "To perform man in the middle attack."])
		print(Style.BRIGHT,table)


	def scan_result(self,result):
		table = PrettyTable(['IP ADDRESS', 'MAC ADDRESS', 'STATUS', 'OPEN PORTS [DEFAULT]'])
		table.align = "c"
		for x in result:
			table.add_row([self.f.YELLOW+Style.BRIGHT+x['host']+self.s.RESET_ALL, self.f.YELLOW+Style.BRIGHT+x['mac']+self.s.RESET_ALL, self.f.YELLOW+Style.BRIGHT+"up"+self.s.RESET_ALL, self.f.YELLOW+Style.BRIGHT+str(x['ports'])+self.s.RESET_ALL])
		print(table)


	def about_author(self):
		table = PrettyTable(['About Author'])
		table.align = "c"
		table.add_row([Fore.GREEN+Style.BRIGHT+"Welcome to Netsploit\nhttps://www.github.com/programmingrakesh/netsploit\nAuthor: Subbu Rakesh"])
		print(Style.BRIGHT,table)

	def option_mitm(self, targetip="-"):
		print(Style.BRIGHT,"Mitm Options:")
		table = PrettyTable(['Variables', 'Values'])
		table.align = "c"
		table.add_row([Fore.MAGENTA+Style.BRIGHT+"Target IP"+Style.RESET_ALL, Fore.MAGENTA+Style.BRIGHT+targetip+Style.RESET_ALL])
		print(Style.BRIGHT,table)

	def help_mitm(self):
		table = PrettyTable(['Commands', 'Description'])
		table.align = "c"
		table.add_row(['option', 'View the options about about the Module.'])
		table.add_row(['set <Target IP>', 'Set the Target IP Address.'])
		table.add_row(['run', 'To run the script.'])
		table.add_row(['back', 'Back to main menu.'])
		print(Style.BRIGHT,table)