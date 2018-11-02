import sys
import ldap


Server = "ldap://<ldap server>"

username = ""
fullUsername = "DIR\\"
password = ""

Base = "dc=DIR,dc=co,dc=com"
Scope = ldap.SCOPE_SUBTREE
Filter = "(&(objectClass=user)(sAMAccountName="+username+"))"
Attrs = ["displayName"]

l = ldap.initialize(Server)
l.protocol_version = 3
l.set_option(ldap.OPT_REFERRALS, 0)
print l.simple_bind_s(fullUsername, password)

r = l.search(Base, Scope, Filter, Attrs)
Type, user = l.result(r, 60)
Name, Attrs = user[0]
if hasattr(Attrs, 'has_key') and Attrs.has_key('displayName'):
  displayName = Attrs['displayName'][0]
  print displayName

sys.exit()