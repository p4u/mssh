#!/usr/bin/env python
import pexpect
import string

class ssh:

 def __init__(self):
    global PROMPT
    PROMPT='~#'
    
 def login(self,user,host,port,passw):
    global ERR
    global p
    ssh_newkey = 'Are you sure you want to continue connecting'
    not_found = 'Name or service not known'
    ERR=0
 
    # 0->timeout 1->newkey 2->host_not_found 3->EOF 4->password 5->prompt
    EXP_LIST=[pexpect.TIMEOUT,ssh_newkey,not_found, pexpect.EOF,'password: ',PROMPT]       
    cmd = 'ssh -p %s -l %s %s'%(port, user, host) 
    try:
        p = pexpect.spawn(cmd)
        i = p.expect(EXP_LIST,10)
    except:
        return False
   
    if i == 1: # SSH does not have the public key. Just accept it.
        p.sendline ('yes')
        i = p.expect(EXP_LIST,10)
     
    if i == 4: #Password is required
        p.sendline(passw)

	i = p.expect(EXP_LIST,10)
     
    if i == 4: #Password FAIL
        ERR=-4
     
    if i == 2: #Host not found
        ERR=-2
              
    elif i == 3: #EOF, maybe Permision denied
        perm_den = string.find(p.before,'Permission denied')
        if perm_den >= 0:
            ERR=-3
        else:
	    return p.before.split('\n')	
            #ERR=-5

    elif i == 5: #Login OK, we have Prompt
        return p.before.split('\n')

    if i == 0: # Timeout
        ERR=-1

#Devuelve una lista separa por saltos de linea. 
#El elemento 0 es el propio comando ejecutado.
 def execute(self,CMD):
    p.sendline(CMD)
    p.expect(pexpect.TIMEOUT,1)
    return p.before.split('\n')


 def logout(self):
    p.sendline('exit')
    p.close()


 def get_error (self):
	error = {
		 0: 'NoError',
    		-1: 'TimeOut',
    		-2: 'Host not found',
    		-3: 'Permission denied',
    		-4: 'Password failed',
		-5: 'EOF not reconized'}			
	return error.get(ERR,'Not reconized')
