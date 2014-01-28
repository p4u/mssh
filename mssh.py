import IMssh
import sys
import string
import os

def run (uhost, port, passw,cmds):		
	SSH = IMssh.ssh()
	
	uhp = uhost.split('@')
	if len(uhp) > 1:
		user = uhp[0]
		host = uhp[1]
	else:
		host = uhp[0]
		user = "root"

#	print "user:%s host:%s port:%s passw:%s" %(user,host,port,passw)

	try:
		ret = SSH.login(user,host,port,passw)
	except:
		print "ERROR: Cannot log in"
		return

	if not ret:
		print "ERROR: Cannot connect to host"
		return

	if SSH.get_error() != "NoError":
		print SSH.get_error()
		return

	for com in cmds:
		try:
			List_exec = SSH.execute(com)
		except:
			print "ERROR: command cannot be executed, connection failed?"
			return
	
	i=1
	while i < len(List_exec):
		print List_exec[i]
		i=i+1
	
	SSH.logout()


def help():
	print "Use: %s <host_file> <cmd_file> [global_passwrd]" %sys.argv[0]
	print ""
	print "    -host_file syntax:"
	print "                      <[user1@]IP1[:port1]> [password1]"
	print "                      <[user2@]IP2[:port2]> [password2]"
	print "    -cmd_file syntax:" 
	print "                      <cmd1>"
	print "                      <cmd2>" 
	sys.exit(1)

def main ():
	if len(sys.argv) < 3: help()
	host_file = sys.argv[1]
	cmd_file = sys.argv[2]

	if len(sys.argv) > 3:
		gl_password = sys.argv[3]
	else:
		gl_password = ""

	cf = open(cmd_file,'r')
	cmdlst = []
	cmdlst.append('export PS1=""')
	for c in cf.readlines():
		cmdlst.append(c)
	cf.close()

	hf = open(host_file,'r')
	for h in hf.readlines():
		hs = h.split()
		if len(hs) > 1:
			password = hs[1]
			host = hs[0]
		elif len(hs) > 0:
			password = gl_password 
			host = hs[0]

		hss = host.split(":")
		if len(hss) > 1:
			host = hss[0]
			port = hss[1]
		else:
			host = hss[0]
			port = 22
			
		print "--------------------------------------"
		print "   Connecting %s %s" %(host,port)
		print "--------------------------------------"
		run(host,port,password,cmdlst)


if __name__ == '__main__':
        main()

