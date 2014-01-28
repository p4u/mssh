==== MultiSSH ====

Licence: GPLv3

Status: Quick and dirty but works :)

Execute SSH commands to multiple nodes specifying a global password for all nodes 
or a specific password for each one. Port and username are also customizable.
All information is read from the text files "hosts" and "cmds".
PublicKey authentication is also supported, password is only used if it is requested.

    Use: python2 mssh.py <host_file> <cmd_file> [global_passwrd]

      -host_file syntax:
                      <[user1@]IP1[|port1]> [password1]
                      <[user2@]IP2[|port2]> [password2]
      -cmd_file syntax:
                      <cmd1>
                      <cmd2>

Example: 

    python2 main.py hosts cmds

    Connecting 172.30.22.1 22
      uname -a
       Linux qMp2b64 3.3.8 #55 Tue Jan 21 10:45:04 EST 2014 i586 GNU/Linux date
       Tue Jan 28 15:29:08 UTC 2014

    Connecting root@10.1.9.1 22
      uname -a
       Linux GSalcolea46-578a 3.3.8 #251 Wed Nov 27 03:34:39 EST 2013 mips GNU/Linux date
       Tue Jan 28 15:29:16 UTC 2014

