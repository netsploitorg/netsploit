default:
	pip3 install pyinstaller
	pip3 install -r requirements.txt
	pyinstaller --name netsploit --onefile netsploit.py
	cp dist/netsploit /bin
	rm -rf build/ dist/ netsploit.spec

clean:
	rm /bin/netsploit
	clear
