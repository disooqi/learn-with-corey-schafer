import getpass
import telnetlib
from telnetlib import Telnet

with Telnet('localhost', 9600) as tn:
    tn.write('disooqi'.encode('ascii'))
# tn.interact()
