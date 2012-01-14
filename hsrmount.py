#!/usr/bin/python
#
# Simple script to mount shares at HSR
# v1.0 (20.09.2010)
#
# Author: Danilo Bargen <gezuru@gmail.com>
# Some code stolen from http://sel.pastebin.com/9kCpmA4y
#
# License:
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
# Version 2, December 2004
# 
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#  
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#  
# 0. You just DO WHAT THE FUCK YOU WANT TO.
 

from config import auth
import os, sys, subprocess
import getpass

############################
# Set the following options
############################

localuser = getpass.getuser()
username, password = auth.userinfo()

server = "152.96.90.26" # Server providing the following shares
shares = ["skripte"] # The shares on the server to mount
 
 
##############
# Main script
##############

# Check for root permissions
if os.getuid():
    print "You need root permissions to mount smb shares."
    sys.exit(-1)
 
try:    
    retval = ""
    print ""
    for entry in shares:
        retval = subprocess.check_call(["mkdir", "-p", "/mnt/%s" % entry])
        retval = retval + subprocess.check_call(["mount", "-t", "cifs", "//%s/%s" % (server, entry), "-o", "user=%s,pass=%s" % (username, password), "-o", "uid=%s" % localuser, "/mnt/%s" % entry])
        print "Mounted /mnt/%s" % (entry)

    print "\nDone mounting."
except:
    print "\nAn error occured. Blame the monkeys."
