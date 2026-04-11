# Class SocketPermission

**Source:** `java.base\java\net\SocketPermission.html`

### Class Description

```java
public final class
SocketPermission

extends
Permission

implements
Serializable
```

This class represents access to a network via sockets.
A SocketPermission consists of a
host specification and a set of "actions" specifying ways to
connect to that host. The host is specified as

```java
host = (hostname | IPv4address | iPv6reference) [:portrange]
portrange = portnumber | -portnumber | portnumber-[portnumber]
```

The host is expressed as a DNS name, as a numerical IP address,
or as "localhost" (for the local machine).
The wildcard "*" may be included once in a DNS name host
specification. If it is included, it must be in the leftmost
position, as in "*.sun.com".

The format of the IPv6reference should follow that specified in

RFC 2732: Format
for Literal IPv6 Addresses in URLs

:

```java
ipv6reference = "[" IPv6address "]"
```

For example, you can construct a SocketPermission instance
as the following:

```java
String hostAddress = inetaddress.getHostAddress();
if (inetaddress instanceof Inet6Address) {
sp = new SocketPermission("[" + hostAddress + "]:" + port, action);
} else {
sp = new SocketPermission(hostAddress + ":" + port, action);
}
```

or

```java
String host = url.getHost();
sp = new SocketPermission(host + ":" + port, action);
```

The

full uncompressed form

of
an IPv6 literal address is also valid.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public SocketPermission​(
String
host,

String
action)

Creates a new SocketPermission object with the specified actions.
The host is expressed as a DNS name, or as a numerical IP address.
Optionally, a port or a portrange may be supplied (separated
from the DNS name or IP address by a colon).

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

**Parameters:**
- host

- the hostname or IPaddress of the computer, optionally
including a colon followed by a port or port range.
- action

- the action string.

---

### Method Details

#### public boolean implies​(
Permission
p)

Checks if this socket permission object "implies" the
specified permission.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

**Specified by:**
- implies

in class

Permission

**Parameters:**
- p

- the permission to check against.

**Returns:**
- true if the specified permission is implied by this object,
false if not.

---

#### public boolean equals​(
Object
obj)

Checks two SocketPermission objects for equality.

**Specified by:**
- equals

in class

Permission

**Parameters:**
- obj

- the object to test for equality with this object.

**Returns:**
- true if

obj

is a SocketPermission, and has the
same hostname, port range, and actions as this
SocketPermission object. However, port range will be ignored
in the comparison if

obj

only contains the action, 'resolve'.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code value for this object.

**Specified by:**
- hashCode

in class

Permission

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
getActions()

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
connect, listen, accept, resolve.

**Specified by:**
- getActions

in class

Permission

**Returns:**
- the canonical string representation of the actions.

---

#### public
PermissionCollection
newPermissionCollection()

Returns a new PermissionCollection object for storing SocketPermission
objects.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

**Overrides:**
- newPermissionCollection

in class

Permission

**Returns:**
- a new PermissionCollection object suitable for storing SocketPermissions.

---

### Additional Sections

#### Class SocketPermission

java.lang.Object

- java.security.Permission
- - java.net.SocketPermission

java.security.Permission

- java.net.SocketPermission

java.net.SocketPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
SocketPermission

extends
Permission

implements
Serializable
```

This class represents access to a network via sockets.
A SocketPermission consists of a
host specification and a set of "actions" specifying ways to
connect to that host. The host is specified as

```java
host = (hostname | IPv4address | iPv6reference) [:portrange]
portrange = portnumber | -portnumber | portnumber-[portnumber]
```

The host is expressed as a DNS name, as a numerical IP address,
or as "localhost" (for the local machine).
The wildcard "*" may be included once in a DNS name host
specification. If it is included, it must be in the leftmost
position, as in "*.sun.com".

The format of the IPv6reference should follow that specified in

RFC 2732: Format
for Literal IPv6 Addresses in URLs

:

```java
ipv6reference = "[" IPv6address "]"
```

For example, you can construct a SocketPermission instance
as the following:

```java
String hostAddress = inetaddress.getHostAddress();
if (inetaddress instanceof Inet6Address) {
sp = new SocketPermission("[" + hostAddress + "]:" + port, action);
} else {
sp = new SocketPermission(hostAddress + ":" + port, action);
}
```

or

```java
String host = url.getHost();
sp = new SocketPermission(host + ":" + port, action);
```

The

full uncompressed form

of
an IPv6 literal address is also valid.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

**Since:** 1.2
**See Also:** Permissions

,

SocketPermission

public final class

SocketPermission

extends

Permission

implements

Serializable

This class represents access to a network via sockets.
A SocketPermission consists of a
host specification and a set of "actions" specifying ways to
connect to that host. The host is specified as

```java
host = (hostname | IPv4address | iPv6reference) [:portrange]
portrange = portnumber | -portnumber | portnumber-[portnumber]
```

The host is expressed as a DNS name, as a numerical IP address,
or as "localhost" (for the local machine).
The wildcard "*" may be included once in a DNS name host
specification. If it is included, it must be in the leftmost
position, as in "*.sun.com".

The format of the IPv6reference should follow that specified in

RFC 2732: Format
for Literal IPv6 Addresses in URLs

:

```java
ipv6reference = "[" IPv6address "]"
```

For example, you can construct a SocketPermission instance
as the following:

```java
String hostAddress = inetaddress.getHostAddress();
if (inetaddress instanceof Inet6Address) {
sp = new SocketPermission("[" + hostAddress + "]:" + port, action);
} else {
sp = new SocketPermission(hostAddress + ":" + port, action);
}
```

or

```java
String host = url.getHost();
sp = new SocketPermission(host + ":" + port, action);
```

The

full uncompressed form

of
an IPv6 literal address is also valid.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

host = (hostname | IPv4address | iPv6reference) [:portrange]
portrange = portnumber | -portnumber | portnumber-[portnumber]

The format of the IPv6reference should follow that specified in

RFC 2732: Format
for Literal IPv6 Addresses in URLs

:

```java
ipv6reference = "[" IPv6address "]"
```

For example, you can construct a SocketPermission instance
as the following:

```java
String hostAddress = inetaddress.getHostAddress();
if (inetaddress instanceof Inet6Address) {
sp = new SocketPermission("[" + hostAddress + "]:" + port, action);
} else {
sp = new SocketPermission(hostAddress + ":" + port, action);
}
```

or

```java
String host = url.getHost();
sp = new SocketPermission(host + ":" + port, action);
```

The

full uncompressed form

of
an IPv6 literal address is also valid.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

ipv6reference = "[" IPv6address "]"

String hostAddress = inetaddress.getHostAddress();
if (inetaddress instanceof Inet6Address) {
sp = new SocketPermission("[" + hostAddress + "]:" + port, action);
} else {
sp = new SocketPermission(hostAddress + ":" + port, action);
}

String host = url.getHost();
sp = new SocketPermission(host + ":" + port, action);

The

full uncompressed form

of
an IPv6 literal address is also valid.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

The port or portrange is optional. A port specification of the
form "N-", where

N

is a port number, signifies all ports
numbered

N

and above, while a specification of the
form "-N" indicates all ports numbered

N

and below.
The special port value

0

refers to the entire

ephemeral

port range. This is a fixed range of ports a system may use to
allocate dynamic ports from. The actual range may be system dependent.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

The possible ways to connect to the host are

```java
accept
connect
listen
resolve
```

The "listen" action is only meaningful when used with "localhost" and
means the ability to bind to a specified port.
The "resolve" action is implied when any of the other actions are present.
The action "resolve" refers to host/ip name service lookups.

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

accept
connect
listen
resolve

The actions string is converted to lowercase before processing.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

As an example of the creation and meaning of SocketPermissions,
note that if the following permission:

```java
p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");
```

is granted to some code, it allows that code to connect to port 7777 on

puffin.eng.sun.com

, and to accept connections on that port.

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

p1 = new SocketPermission("puffin.eng.sun.com:7777", "connect,accept");

Similarly, if the following permission:

```java
p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");
```

is granted to some code, it allows that code to
accept connections on, connect to, or listen on any port between
1024 and 65535 on the local host.

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

p2 = new SocketPermission("localhost:1024-", "accept,connect,listen");

Note: Granting code permission to accept or make connections to remote
hosts may be dangerous because malevolent code can then more easily
transfer and share confidential data among parties who may not
otherwise have access to the data.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SocketPermission

​(

String

host,

String

action)

Creates a new SocketPermission object with the specified actions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two SocketPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this socket permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing SocketPermission
objects.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

SocketPermission

​(

String

host,

String

action)

Creates a new SocketPermission object with the specified actions.

---

#### Constructor Summary

Creates a new SocketPermission object with the specified actions.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Checks two SocketPermission objects for equality.

String

getActions

()

Returns the canonical string representation of the actions.

int

hashCode

()

Returns the hash code value for this object.

boolean

implies

​(

Permission

p)

Checks if this socket permission object "implies" the
specified permission.

PermissionCollection

newPermissionCollection

()

Returns a new PermissionCollection object for storing SocketPermission
objects.

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Checks two SocketPermission objects for equality.

Returns the canonical string representation of the actions.

Returns the hash code value for this object.

Checks if this socket permission object "implies" the
specified permission.

Returns a new PermissionCollection object for storing SocketPermission
objects.

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SocketPermission

```java
public SocketPermission​(
String
host,

String
action)
```

Creates a new SocketPermission object with the specified actions.
The host is expressed as a DNS name, or as a numerical IP address.
Optionally, a port or a portrange may be supplied (separated
from the DNS name or IP address by a colon).

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

**Parameters:** host

- the hostname or IPaddress of the computer, optionally
including a colon followed by a port or port range.
**Parameters:** action

- the action string.

============ METHOD DETAIL ==========

- Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this socket permission object "implies" the
specified permission.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two SocketPermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a SocketPermission, and has the
same hostname, port range, and actions as this
SocketPermission object. However, port range will be ignored
in the comparison if

obj

only contains the action, 'resolve'.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
connect, listen, accept, resolve.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing SocketPermission
objects.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing SocketPermissions.

Constructor Detail

- SocketPermission

```java
public SocketPermission​(
String
host,

String
action)
```

Creates a new SocketPermission object with the specified actions.
The host is expressed as a DNS name, or as a numerical IP address.
Optionally, a port or a portrange may be supplied (separated
from the DNS name or IP address by a colon).

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

**Parameters:** host

- the hostname or IPaddress of the computer, optionally
including a colon followed by a port or port range.
**Parameters:** action

- the action string.

---

#### Constructor Detail

SocketPermission

```java
public SocketPermission​(
String
host,

String
action)
```

Creates a new SocketPermission object with the specified actions.
The host is expressed as a DNS name, or as a numerical IP address.
Optionally, a port or a portrange may be supplied (separated
from the DNS name or IP address by a colon).

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

**Parameters:** host

- the hostname or IPaddress of the computer, optionally
including a colon followed by a port or port range.
**Parameters:** action

- the action string.

---

#### SocketPermission

public SocketPermission​(

String

host,

String

action)

Creates a new SocketPermission object with the specified actions.
The host is expressed as a DNS name, or as a numerical IP address.
Optionally, a port or a portrange may be supplied (separated
from the DNS name or IP address by a colon).

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

To specify the local machine, use "localhost" as the

host

.
Also note: An empty

host

String ("") is equivalent to "localhost".

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

The

actions

parameter contains a comma-separated list of the
actions granted for the specified host (and port(s)). Possible actions are
"connect", "listen", "accept", "resolve", or
any combination of those. "resolve" is automatically added
when any of the other three are specified.

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

Examples of SocketPermission instantiation are the following:

```java
nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");
```

nr = new SocketPermission("www.catalog.com", "connect");
nr = new SocketPermission("www.sun.com:80", "connect");
nr = new SocketPermission("*.sun.com", "connect");
nr = new SocketPermission("*.edu", "resolve");
nr = new SocketPermission("204.160.241.0", "connect");
nr = new SocketPermission("localhost:1024-65535", "listen");
nr = new SocketPermission("204.160.241.0:1024-65535", "connect");

Method Detail

- implies

```java
public boolean implies​(
Permission
p)
```

Checks if this socket permission object "implies" the
specified permission.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

- equals

```java
public boolean equals​(
Object
obj)
```

Checks two SocketPermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a SocketPermission, and has the
same hostname, port range, and actions as this
SocketPermission object. However, port range will be ignored
in the comparison if

obj

only contains the action, 'resolve'.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
connect, listen, accept, resolve.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

- newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing SocketPermission
objects.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing SocketPermissions.

---

#### Method Detail

implies

```java
public boolean implies​(
Permission
p)
```

Checks if this socket permission object "implies" the
specified permission.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

**Specified by:** implies

in class

Permission
**Parameters:** p

- the permission to check against.
**Returns:** true if the specified permission is implied by this object,
false if not.

---

#### implies

public boolean implies​(

Permission

p)

Checks if this socket permission object "implies" the
specified permission.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

More specifically, this method first ensures that all of the following
are true (and returns false if any of them are not):

- p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

Then

implies

checks each of the following, in order,
and for each returns true if the stated condition is true:

- If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

If none of the above are true,

implies

returns false.

p

is an instanceof SocketPermission,

p

's actions are a proper subset of this
object's actions, and

p

's port range is included in this port range. Note:
port range is ignored when p only contains the action, 'resolve'.

If this object was initialized with a single IP address and one of

p

's
IP addresses is equal to this object's IP address.

If this object is a wildcard domain (such as *.sun.com), and

p

's canonical name (the name without any preceding *)
ends with this object's canonical host name. For example, *.sun.com
implies *.eng.sun.com.

If this object was not initialized with a single IP address, and one of this
object's IP addresses equals one of

p

's IP addresses.

If this canonical name equals

p

's canonical name.

equals

```java
public boolean equals​(
Object
obj)
```

Checks two SocketPermission objects for equality.

**Specified by:** equals

in class

Permission
**Parameters:** obj

- the object to test for equality with this object.
**Returns:** true if

obj

is a SocketPermission, and has the
same hostname, port range, and actions as this
SocketPermission object. However, port range will be ignored
in the comparison if

obj

only contains the action, 'resolve'.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Checks two SocketPermission objects for equality.

hashCode

```java
public int hashCode()
```

Returns the hash code value for this object.

**Specified by:** hashCode

in class

Permission
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code value for this object.

getActions

```java
public
String
getActions()
```

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
connect, listen, accept, resolve.

**Specified by:** getActions

in class

Permission
**Returns:** the canonical string representation of the actions.

---

#### getActions

public

String

getActions()

Returns the canonical string representation of the actions.
Always returns present actions in the following order:
connect, listen, accept, resolve.

newPermissionCollection

```java
public
PermissionCollection
newPermissionCollection()
```

Returns a new PermissionCollection object for storing SocketPermission
objects.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

**Overrides:** newPermissionCollection

in class

Permission
**Returns:** a new PermissionCollection object suitable for storing SocketPermissions.

---

#### newPermissionCollection

public

PermissionCollection

newPermissionCollection()

Returns a new PermissionCollection object for storing SocketPermission
objects.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

SocketPermission objects must be stored in a manner that allows them
to be inserted into the collection in any order, but that also enables the
PermissionCollection

implies

method to be implemented in an efficient (and consistent) manner.

---

