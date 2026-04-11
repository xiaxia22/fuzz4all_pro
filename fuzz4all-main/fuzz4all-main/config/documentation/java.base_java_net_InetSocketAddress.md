# Class InetSocketAddress

**Source:** `java.base\java\net\InetSocketAddress.html`

### Class Description

```java
public class
InetSocketAddress

extends
SocketAddress
```

This class implements an IP Socket Address (IP address + port number)
It can also be a pair (hostname + port number), in which case an attempt
will be made to resolve the hostname. If resolution fails then the address
is said to be

unresolved

but can still be used on some circumstances
like connecting through a proxy.

It provides an immutable object used by sockets for binding, connecting, or
as returned values.

The

wildcard

is a special local IP address. It usually means "any"
and can only be used for

bind

operations.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InetSocketAddress​(int port)

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:**
- port

- The port number

**Throws:**
- IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

---

#### public InetSocketAddress​(
InetAddress
addr,
int port)

Creates a socket address from an IP address and a port number.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

**Parameters:**
- addr

- The IP address
- port

- The port number

**Throws:**
- IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

---

#### public InetSocketAddress​(
String
hostname,
int port)

Creates a socket address from a hostname and a port number.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:**
- hostname

- the Host name
- port

- The port number

**Throws:**
- IllegalArgumentException

- if the port parameter is outside the range
of valid port values, or if the hostname parameter is

null

.
- SecurityException

- if a security manager is present and
permission to resolve the host name is
denied.

**See Also:**
- isUnresolved()

---

### Method Details

#### public static
InetSocketAddress
createUnresolved​(
String
host,
int port)

Creates an unresolved socket address from a hostname and a port number.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:**
- host

- the Host name
- port

- The port number

**Returns:**
- an

InetSocketAddress

representing the unresolved
socket address

**Throws:**
- IllegalArgumentException

- if the port parameter is outside
the range of valid port values, or if the hostname
parameter is

null

.

**See Also:**
- isUnresolved()

**Since:**
- 1.5

---

#### public final int getPort()

Gets the port number.

**Returns:**
- the port number.

---

#### public final
InetAddress
getAddress()

Gets the

InetAddress

.

**Returns:**
- the InetAddress or

null

if it is unresolved.

---

#### public final
String
getHostName()

Gets the

hostname

.
Note: This method may trigger a name service reverse lookup if the
address was created with a literal IP address.

**Returns:**
- the hostname part of the address.

---

#### public final
String
getHostString()

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).
This has the benefit of

not

attempting a reverse lookup.

**Returns:**
- the hostname, or String representation of the address.

**Since:**
- 1.7

---

#### public final boolean isUnresolved()

Checks whether the address has been resolved or not.

**Returns:**
- true

if the hostname couldn't be resolved into
an

InetAddress

.

---

#### public
String
toString()

Constructs a string representation of this InetSocketAddress.
This String is constructed by calling toString() on the InetAddress
and concatenating the port number (with a colon). If the address
is unresolved then the part before the colon will only contain the hostname.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object.

---

#### public final boolean equals​(
Object
obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same address as
this object.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to compare against.

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- InetAddress.equals(java.lang.Object)

---

#### public final int hashCode()

Returns a hashcode for this socket address.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this socket address.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class InetSocketAddress

java.lang.Object

- java.net.SocketAddress
- - java.net.InetSocketAddress

java.net.SocketAddress

- java.net.InetSocketAddress

java.net.InetSocketAddress

**All Implemented Interfaces:** Serializable

```java
public class
InetSocketAddress

extends
SocketAddress
```

This class implements an IP Socket Address (IP address + port number)
It can also be a pair (hostname + port number), in which case an attempt
will be made to resolve the hostname. If resolution fails then the address
is said to be

unresolved

but can still be used on some circumstances
like connecting through a proxy.

It provides an immutable object used by sockets for binding, connecting, or
as returned values.

The

wildcard

is a special local IP address. It usually means "any"
and can only be used for

bind

operations.

**Since:** 1.4
**See Also:** Socket

,

ServerSocket

,

Serialized Form

public class

InetSocketAddress

extends

SocketAddress

This class implements an IP Socket Address (IP address + port number)
It can also be a pair (hostname + port number), in which case an attempt
will be made to resolve the hostname. If resolution fails then the address
is said to be

unresolved

but can still be used on some circumstances
like connecting through a proxy.

It provides an immutable object used by sockets for binding, connecting, or
as returned values.

The

wildcard

is a special local IP address. It usually means "any"
and can only be used for

bind

operations.

It provides an immutable object used by sockets for binding, connecting, or
as returned values.

The

wildcard

is a special local IP address. It usually means "any"
and can only be used for

bind

operations.

The

wildcard

is a special local IP address. It usually means "any"
and can only be used for

bind

operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InetSocketAddress

​(int port)

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

InetSocketAddress

​(

String

hostname,
int port)

Creates a socket address from a hostname and a port number.

InetSocketAddress

​(

InetAddress

addr,
int port)

Creates a socket address from an IP address and a port number.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

InetSocketAddress

createUnresolved

​(

String

host,
int port)

Creates an unresolved socket address from a hostname and a port number.

boolean

equals

​(

Object

obj)

Compares this object against the specified object.

InetAddress

getAddress

()

Gets the

InetAddress

.

String

getHostName

()

Gets the

hostname

.

String

getHostString

()

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).

int

getPort

()

Gets the port number.

int

hashCode

()

Returns a hashcode for this socket address.

boolean

isUnresolved

()

Checks whether the address has been resolved or not.

String

toString

()

Constructs a string representation of this InetSocketAddress.

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

InetSocketAddress

​(int port)

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

InetSocketAddress

​(

String

hostname,
int port)

Creates a socket address from a hostname and a port number.

InetSocketAddress

​(

InetAddress

addr,
int port)

Creates a socket address from an IP address and a port number.

---

#### Constructor Summary

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

Creates a socket address from a hostname and a port number.

Creates a socket address from an IP address and a port number.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

InetSocketAddress

createUnresolved

​(

String

host,
int port)

Creates an unresolved socket address from a hostname and a port number.

boolean

equals

​(

Object

obj)

Compares this object against the specified object.

InetAddress

getAddress

()

Gets the

InetAddress

.

String

getHostName

()

Gets the

hostname

.

String

getHostString

()

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).

int

getPort

()

Gets the port number.

int

hashCode

()

Returns a hashcode for this socket address.

boolean

isUnresolved

()

Checks whether the address has been resolved or not.

String

toString

()

Constructs a string representation of this InetSocketAddress.

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

Creates an unresolved socket address from a hostname and a port number.

Compares this object against the specified object.

Gets the

InetAddress

.

Gets the

hostname

.

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).

Gets the port number.

Returns a hashcode for this socket address.

Checks whether the address has been resolved or not.

Constructs a string representation of this InetSocketAddress.

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

- InetSocketAddress

```java
public InetSocketAddress​(int port)
```

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

- InetSocketAddress

```java
public InetSocketAddress​(
InetAddress
addr,
int port)
```

Creates a socket address from an IP address and a port number.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

**Parameters:** addr

- The IP address
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

- InetSocketAddress

```java
public InetSocketAddress​(
String
hostname,
int port)
```

Creates a socket address from a hostname and a port number.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** hostname

- the Host name
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the range
of valid port values, or if the hostname parameter is

null

.
**Throws:** SecurityException

- if a security manager is present and
permission to resolve the host name is
denied.
**See Also:** isUnresolved()

============ METHOD DETAIL ==========

- Method Detail

- createUnresolved

```java
public static
InetSocketAddress
createUnresolved​(
String
host,
int port)
```

Creates an unresolved socket address from a hostname and a port number.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** host

- the Host name
**Parameters:** port

- The port number
**Returns:** an

InetSocketAddress

representing the unresolved
socket address
**Throws:** IllegalArgumentException

- if the port parameter is outside
the range of valid port values, or if the hostname
parameter is

null

.
**Since:** 1.5
**See Also:** isUnresolved()

- getPort

```java
public final int getPort()
```

Gets the port number.

**Returns:** the port number.

- getAddress

```java
public final
InetAddress
getAddress()
```

Gets the

InetAddress

.

**Returns:** the InetAddress or

null

if it is unresolved.

- getHostName

```java
public final
String
getHostName()
```

Gets the

hostname

.
Note: This method may trigger a name service reverse lookup if the
address was created with a literal IP address.

**Returns:** the hostname part of the address.

- getHostString

```java
public final
String
getHostString()
```

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).
This has the benefit of

not

attempting a reverse lookup.

**Returns:** the hostname, or String representation of the address.
**Since:** 1.7

- isUnresolved

```java
public final boolean isUnresolved()
```

Checks whether the address has been resolved or not.

**Returns:** true

if the hostname couldn't be resolved into
an

InetAddress

.

- toString

```java
public
String
toString()
```

Constructs a string representation of this InetSocketAddress.
This String is constructed by calling toString() on the InetAddress
and concatenating the port number (with a colon). If the address
is unresolved then the part before the colon will only contain the hostname.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same address as
this object.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.equals(java.lang.Object)

- hashCode

```java
public final int hashCode()
```

Returns a hashcode for this socket address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this socket address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Constructor Detail

- InetSocketAddress

```java
public InetSocketAddress​(int port)
```

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

- InetSocketAddress

```java
public InetSocketAddress​(
InetAddress
addr,
int port)
```

Creates a socket address from an IP address and a port number.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

**Parameters:** addr

- The IP address
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

- InetSocketAddress

```java
public InetSocketAddress​(
String
hostname,
int port)
```

Creates a socket address from a hostname and a port number.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** hostname

- the Host name
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the range
of valid port values, or if the hostname parameter is

null

.
**Throws:** SecurityException

- if a security manager is present and
permission to resolve the host name is
denied.
**See Also:** isUnresolved()

---

#### Constructor Detail

InetSocketAddress

```java
public InetSocketAddress​(int port)
```

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

---

#### InetSocketAddress

public InetSocketAddress​(int port)

Creates a socket address where the IP address is the wildcard address
and the port number a specified value.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

InetSocketAddress

```java
public InetSocketAddress​(
InetAddress
addr,
int port)
```

Creates a socket address from an IP address and a port number.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

**Parameters:** addr

- The IP address
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the specified
range of valid port values.

---

#### InetSocketAddress

public InetSocketAddress​(

InetAddress

addr,
int port)

Creates a socket address from an IP address and a port number.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A

null

address will assign the

wildcard

address.

A

null

address will assign the

wildcard

address.

InetSocketAddress

```java
public InetSocketAddress​(
String
hostname,
int port)
```

Creates a socket address from a hostname and a port number.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** hostname

- the Host name
**Parameters:** port

- The port number
**Throws:** IllegalArgumentException

- if the port parameter is outside the range
of valid port values, or if the hostname parameter is

null

.
**Throws:** SecurityException

- if a security manager is present and
permission to resolve the host name is
denied.
**See Also:** isUnresolved()

---

#### InetSocketAddress

public InetSocketAddress​(

String

hostname,
int port)

Creates a socket address from a hostname and a port number.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

An attempt will be made to resolve the hostname into an InetAddress.
If that attempt fails, the address will be flagged as

unresolved

.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

If there is a security manager, its

checkConnect

method
is called with the host name as its argument to check the permission
to resolve it. This could result in a SecurityException.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

Method Detail

- createUnresolved

```java
public static
InetSocketAddress
createUnresolved​(
String
host,
int port)
```

Creates an unresolved socket address from a hostname and a port number.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** host

- the Host name
**Parameters:** port

- The port number
**Returns:** an

InetSocketAddress

representing the unresolved
socket address
**Throws:** IllegalArgumentException

- if the port parameter is outside
the range of valid port values, or if the hostname
parameter is

null

.
**Since:** 1.5
**See Also:** isUnresolved()

- getPort

```java
public final int getPort()
```

Gets the port number.

**Returns:** the port number.

- getAddress

```java
public final
InetAddress
getAddress()
```

Gets the

InetAddress

.

**Returns:** the InetAddress or

null

if it is unresolved.

- getHostName

```java
public final
String
getHostName()
```

Gets the

hostname

.
Note: This method may trigger a name service reverse lookup if the
address was created with a literal IP address.

**Returns:** the hostname part of the address.

- getHostString

```java
public final
String
getHostString()
```

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).
This has the benefit of

not

attempting a reverse lookup.

**Returns:** the hostname, or String representation of the address.
**Since:** 1.7

- isUnresolved

```java
public final boolean isUnresolved()
```

Checks whether the address has been resolved or not.

**Returns:** true

if the hostname couldn't be resolved into
an

InetAddress

.

- toString

```java
public
String
toString()
```

Constructs a string representation of this InetSocketAddress.
This String is constructed by calling toString() on the InetAddress
and concatenating the port number (with a colon). If the address
is unresolved then the part before the colon will only contain the hostname.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

- equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same address as
this object.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.equals(java.lang.Object)

- hashCode

```java
public final int hashCode()
```

Returns a hashcode for this socket address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this socket address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

createUnresolved

```java
public static
InetSocketAddress
createUnresolved​(
String
host,
int port)
```

Creates an unresolved socket address from a hostname and a port number.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

**Parameters:** host

- the Host name
**Parameters:** port

- The port number
**Returns:** an

InetSocketAddress

representing the unresolved
socket address
**Throws:** IllegalArgumentException

- if the port parameter is outside
the range of valid port values, or if the hostname
parameter is

null

.
**Since:** 1.5
**See Also:** isUnresolved()

---

#### createUnresolved

public static

InetSocketAddress

createUnresolved​(

String

host,
int port)

Creates an unresolved socket address from a hostname and a port number.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

No attempt will be made to resolve the hostname into an InetAddress.
The address will be flagged as

unresolved

.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

A valid port value is between 0 and 65535.
A port number of

zero

will let the system pick up an
ephemeral port in a

bind

operation.

getPort

```java
public final int getPort()
```

Gets the port number.

**Returns:** the port number.

---

#### getPort

public final int getPort()

Gets the port number.

getAddress

```java
public final
InetAddress
getAddress()
```

Gets the

InetAddress

.

**Returns:** the InetAddress or

null

if it is unresolved.

---

#### getAddress

public final

InetAddress

getAddress()

Gets the

InetAddress

.

getHostName

```java
public final
String
getHostName()
```

Gets the

hostname

.
Note: This method may trigger a name service reverse lookup if the
address was created with a literal IP address.

**Returns:** the hostname part of the address.

---

#### getHostName

public final

String

getHostName()

Gets the

hostname

.
Note: This method may trigger a name service reverse lookup if the
address was created with a literal IP address.

getHostString

```java
public final
String
getHostString()
```

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).
This has the benefit of

not

attempting a reverse lookup.

**Returns:** the hostname, or String representation of the address.
**Since:** 1.7

---

#### getHostString

public final

String

getHostString()

Returns the hostname, or the String form of the address if it
doesn't have a hostname (it was created using a literal).
This has the benefit of

not

attempting a reverse lookup.

isUnresolved

```java
public final boolean isUnresolved()
```

Checks whether the address has been resolved or not.

**Returns:** true

if the hostname couldn't be resolved into
an

InetAddress

.

---

#### isUnresolved

public final boolean isUnresolved()

Checks whether the address has been resolved or not.

toString

```java
public
String
toString()
```

Constructs a string representation of this InetSocketAddress.
This String is constructed by calling toString() on the InetAddress
and concatenating the port number (with a colon). If the address
is unresolved then the part before the colon will only contain the hostname.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.

---

#### toString

public

String

toString()

Constructs a string representation of this InetSocketAddress.
This String is constructed by calling toString() on the InetAddress
and concatenating the port number (with a colon). If the address
is unresolved then the part before the colon will only contain the hostname.

equals

```java
public final boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same address as
this object.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.equals(java.lang.Object)

---

#### equals

public final boolean equals​(

Object

obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same address as
this object.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

Two instances of

InetSocketAddress

represent the same
address if both the InetAddresses (or hostnames if it is unresolved) and port
numbers are equal.
If both addresses are unresolved, then the hostname and the port number
are compared.

Note: Hostnames are case insensitive. e.g. "FooBar" and "foobar" are
considered equal.

hashCode

```java
public final int hashCode()
```

Returns a hashcode for this socket address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this socket address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public final int hashCode()

Returns a hashcode for this socket address.

---

