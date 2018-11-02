import getpass
import os
import pwd

print getpass.getuser()

print pwd.getpwuid( os.getuid() )[ 0 ]
