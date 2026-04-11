# Class NetworkInterface

**Source:** `java.base\java\net\NetworkInterface.html`

### Class Description

```java
public final class
NetworkInterface

extends
Object
```

This class represents a Network Interface made up of a name,
and a list of IP addresses assigned to this interface.
It is used to identify the local interface on which a multicast group
is joined.

Interfaces are normally known by names such as "le0".

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getName()

Get the name of this network interface.

**Returns:**
- the name of this network interface

---

#### public
Enumeration
<
InetAddress
> getInetAddresses()

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:**
- an Enumeration object with all or a subset of the InetAddresses
bound to this network interface

**See Also:**
- inetAddresses()

---

#### public
Stream
<
InetAddress
> inetAddresses()

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:**
- a Stream object with all or a subset of the InetAddresses
bound to this network interface

**Since:**
- 9

---

#### public
List
<
InterfaceAddress
> getInterfaceAddresses()

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

**Returns:**
- a

List

object with all or a subset of the
InterfaceAddresss of this network interface

**Since:**
- 1.6

---

#### public
Enumeration
<
NetworkInterface
> getSubInterfaces()

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

For instance eth0:1 will be a subinterface to eth0.

**Returns:**
- an Enumeration object with all of the subinterfaces
of this network interface

**See Also:**
- subInterfaces()

**Since:**
- 1.6

---

#### public
Stream
<
NetworkInterface
> subInterfaces()

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

**Returns:**
- a Stream object with all of the subinterfaces
of this network interface

**Since:**
- 9

---

#### public
NetworkInterface
getParent()

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

**Returns:**
- The

NetworkInterface

this interface is attached to.

**Since:**
- 1.6

---

#### public int getIndex()

Returns the index of this network interface. The index is an integer greater
or equal to zero, or

-1

for unknown. This is a system specific value
and interfaces with the same name can have different indexes on different
machines.

**Returns:**
- the index of this network interface or

-1

if the index is
unknown

**See Also:**
- getByIndex(int)

**Since:**
- 1.7

---

#### public
String
getDisplayName()

Get the display name of this network interface.
A display name is a human readable String describing the network
device.

**Returns:**
- a non-empty string representing the display name of this network
interface, or null if no display name is available.

---

#### public static
NetworkInterface
getByName​(
String
name)
throws
SocketException

Searches for the network interface with the specified name.

**Parameters:**
- name

- The name of the network interface.

**Returns:**
- A

NetworkInterface

with the specified name,
or

null

if there is no network interface
with the specified name.

**Throws:**
- SocketException

- If an I/O error occurs.
- NullPointerException

- If the specified name is

null

.

---

#### public static
NetworkInterface
getByIndex​(int index)
throws
SocketException

Get a network interface given its index.

**Parameters:**
- index

- an integer, the index of the interface

**Returns:**
- the NetworkInterface obtained from its index, or

null

if
there is no interface with such an index on the system

**Throws:**
- SocketException

- if an I/O error occurs.
- IllegalArgumentException

- if index has a negative value

**See Also:**
- getIndex()

**Since:**
- 1.7

---

#### public static
NetworkInterface
getByInetAddress​(
InetAddress
addr)
throws
SocketException

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

**Parameters:**
- addr

- The

InetAddress

to search with.

**Returns:**
- A

NetworkInterface

or

null

if there is no network interface
with the specified IP address.

**Throws:**
- SocketException

- If an I/O error occurs.
- NullPointerException

- If the specified address is

null

.

---

#### public static
Enumeration
<
NetworkInterface
> getNetworkInterfaces()
throws
SocketException

Returns an

Enumeration

of all the interfaces on this machine. The

Enumeration

contains at least one element, possibly representing
a loopback interface that only supports communication between entities on
this machine.

**Returns:**
- an Enumeration of NetworkInterfaces found on this machine

**Throws:**
- SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.

**See Also:**
- networkInterfaces()

**API Note:**
- this method can be used in combination with

getInetAddresses()

to obtain all IP addresses for this node

---

#### public static
Stream
<
NetworkInterface
> networkInterfaces()
throws
SocketException

Returns a

Stream

of all the interfaces on this machine. The

Stream

contains at least one interface, possibly representing a
loopback interface that only supports communication between entities on
this machine.

**Returns:**
- a Stream of NetworkInterfaces found on this machine

**Throws:**
- SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.

**Since:**
- 9

**API Note:**
- this method can be used in combination with

inetAddresses()

} to obtain a stream of all IP addresses for
this node, for example:

```java
Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
.flatMap(NetworkInterface::inetAddresses);
```

---

#### public boolean isUp()
throws
SocketException

Returns whether a network interface is up and running.

**Returns:**
- true

if the interface is up and running.

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public boolean isLoopback()
throws
SocketException

Returns whether a network interface is a loopback interface.

**Returns:**
- true

if the interface is a loopback interface.

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public boolean isPointToPoint()
throws
SocketException

Returns whether a network interface is a point to point interface.
A typical point to point interface would be a PPP connection through
a modem.

**Returns:**
- true

if the interface is a point to point
interface.

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public boolean supportsMulticast()
throws
SocketException

Returns whether a network interface supports multicasting or not.

**Returns:**
- true

if the interface supports Multicasting.

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public byte[] getHardwareAddress()
throws
SocketException

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.
If a security manager is set, then the caller must have
the permission

NetPermission

("getNetworkInformation").

**Returns:**
- a byte array containing the address, or

null

if
the address doesn't exist, is not accessible or a security
manager is set and the caller does not have the permission
NetPermission("getNetworkInformation")

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public int getMTU()
throws
SocketException

Returns the Maximum Transmission Unit (MTU) of this interface.

**Returns:**
- the value of the MTU for that interface.

**Throws:**
- SocketException

- if an I/O error occurs.

**Since:**
- 1.6

---

#### public boolean isVirtual()

Returns whether this interface is a virtual interface (also called
subinterface).
Virtual interfaces are, on some systems, interfaces created as a child
of a physical interface and given different settings (like address or
MTU). Usually the name of the interface will the name of the parent
followed by a colon (:) and a number identifying the child since there
can be several virtual interfaces attached to a single physical
interface.

**Returns:**
- true

if this interface is a virtual interface.

**Since:**
- 1.6

---

#### public boolean equals​(
Object
obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same NetworkInterface
as this object.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

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
- InetAddress.getAddress()

---

### Additional Sections

#### Class NetworkInterface

java.lang.Object

- java.net.NetworkInterface

java.net.NetworkInterface

```java
public final class
NetworkInterface

extends
Object
```

This class represents a Network Interface made up of a name,
and a list of IP addresses assigned to this interface.
It is used to identify the local interface on which a multicast group
is joined.

Interfaces are normally known by names such as "le0".

**Since:** 1.4

public final class

NetworkInterface

extends

Object

This class represents a Network Interface made up of a name,
and a list of IP addresses assigned to this interface.
It is used to identify the local interface on which a multicast group
is joined.

Interfaces are normally known by names such as "le0".

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

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

Compares this object against the specified object.

static

NetworkInterface

getByIndex

​(int index)

Get a network interface given its index.

static

NetworkInterface

getByInetAddress

​(

InetAddress

addr)

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

static

NetworkInterface

getByName

​(

String

name)

Searches for the network interface with the specified name.

String

getDisplayName

()

Get the display name of this network interface.

byte[]

getHardwareAddress

()

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.

int

getIndex

()

Returns the index of this network interface.

Enumeration

<

InetAddress

>

getInetAddresses

()

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

List

<

InterfaceAddress

>

getInterfaceAddresses

()

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

int

getMTU

()

Returns the Maximum Transmission Unit (MTU) of this interface.

String

getName

()

Get the name of this network interface.

static

Enumeration

<

NetworkInterface

>

getNetworkInterfaces

()

Returns an

Enumeration

of all the interfaces on this machine.

NetworkInterface

getParent

()

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

Enumeration

<

NetworkInterface

>

getSubInterfaces

()

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

Stream

<

InetAddress

>

inetAddresses

()

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

boolean

isLoopback

()

Returns whether a network interface is a loopback interface.

boolean

isPointToPoint

()

Returns whether a network interface is a point to point interface.

boolean

isUp

()

Returns whether a network interface is up and running.

boolean

isVirtual

()

Returns whether this interface is a virtual interface (also called
subinterface).

static

Stream

<

NetworkInterface

>

networkInterfaces

()

Returns a

Stream

of all the interfaces on this machine.

Stream

<

NetworkInterface

>

subInterfaces

()

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

boolean

supportsMulticast

()

Returns whether a network interface supports multicasting or not.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Method Summary

All Methods

Static Methods

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

Compares this object against the specified object.

static

NetworkInterface

getByIndex

​(int index)

Get a network interface given its index.

static

NetworkInterface

getByInetAddress

​(

InetAddress

addr)

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

static

NetworkInterface

getByName

​(

String

name)

Searches for the network interface with the specified name.

String

getDisplayName

()

Get the display name of this network interface.

byte[]

getHardwareAddress

()

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.

int

getIndex

()

Returns the index of this network interface.

Enumeration

<

InetAddress

>

getInetAddresses

()

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

List

<

InterfaceAddress

>

getInterfaceAddresses

()

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

int

getMTU

()

Returns the Maximum Transmission Unit (MTU) of this interface.

String

getName

()

Get the name of this network interface.

static

Enumeration

<

NetworkInterface

>

getNetworkInterfaces

()

Returns an

Enumeration

of all the interfaces on this machine.

NetworkInterface

getParent

()

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

Enumeration

<

NetworkInterface

>

getSubInterfaces

()

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

Stream

<

InetAddress

>

inetAddresses

()

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

boolean

isLoopback

()

Returns whether a network interface is a loopback interface.

boolean

isPointToPoint

()

Returns whether a network interface is a point to point interface.

boolean

isUp

()

Returns whether a network interface is up and running.

boolean

isVirtual

()

Returns whether this interface is a virtual interface (also called
subinterface).

static

Stream

<

NetworkInterface

>

networkInterfaces

()

Returns a

Stream

of all the interfaces on this machine.

Stream

<

NetworkInterface

>

subInterfaces

()

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

boolean

supportsMulticast

()

Returns whether a network interface supports multicasting or not.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Compares this object against the specified object.

Get a network interface given its index.

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

Searches for the network interface with the specified name.

Get the display name of this network interface.

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.

Returns the index of this network interface.

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

Returns the Maximum Transmission Unit (MTU) of this interface.

Get the name of this network interface.

Returns an

Enumeration

of all the interfaces on this machine.

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

Returns whether a network interface is a loopback interface.

Returns whether a network interface is a point to point interface.

Returns whether a network interface is up and running.

Returns whether this interface is a virtual interface (also called
subinterface).

Returns a

Stream

of all the interfaces on this machine.

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

Returns whether a network interface supports multicasting or not.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public
String
getName()
```

Get the name of this network interface.

**Returns:** the name of this network interface

- getInetAddresses

```java
public
Enumeration
<
InetAddress
> getInetAddresses()
```

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** an Enumeration object with all or a subset of the InetAddresses
bound to this network interface
**See Also:** inetAddresses()

- inetAddresses

```java
public
Stream
<
InetAddress
> inetAddresses()
```

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** a Stream object with all or a subset of the InetAddresses
bound to this network interface
**Since:** 9

- getInterfaceAddresses

```java
public
List
<
InterfaceAddress
> getInterfaceAddresses()
```

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

**Returns:** a

List

object with all or a subset of the
InterfaceAddresss of this network interface
**Since:** 1.6

- getSubInterfaces

```java
public
Enumeration
<
NetworkInterface
> getSubInterfaces()
```

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

For instance eth0:1 will be a subinterface to eth0.

**Returns:** an Enumeration object with all of the subinterfaces
of this network interface
**Since:** 1.6
**See Also:** subInterfaces()

- subInterfaces

```java
public
Stream
<
NetworkInterface
> subInterfaces()
```

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

**Returns:** a Stream object with all of the subinterfaces
of this network interface
**Since:** 9

- getParent

```java
public
NetworkInterface
getParent()
```

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

**Returns:** The

NetworkInterface

this interface is attached to.
**Since:** 1.6

- getIndex

```java
public int getIndex()
```

Returns the index of this network interface. The index is an integer greater
or equal to zero, or

-1

for unknown. This is a system specific value
and interfaces with the same name can have different indexes on different
machines.

**Returns:** the index of this network interface or

-1

if the index is
unknown
**Since:** 1.7
**See Also:** getByIndex(int)

- getDisplayName

```java
public
String
getDisplayName()
```

Get the display name of this network interface.
A display name is a human readable String describing the network
device.

**Returns:** a non-empty string representing the display name of this network
interface, or null if no display name is available.

- getByName

```java
public static
NetworkInterface
getByName​(
String
name)
throws
SocketException
```

Searches for the network interface with the specified name.

**Parameters:** name

- The name of the network interface.
**Returns:** A

NetworkInterface

with the specified name,
or

null

if there is no network interface
with the specified name.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified name is

null

.

- getByIndex

```java
public static
NetworkInterface
getByIndex​(int index)
throws
SocketException
```

Get a network interface given its index.

**Parameters:** index

- an integer, the index of the interface
**Returns:** the NetworkInterface obtained from its index, or

null

if
there is no interface with such an index on the system
**Throws:** SocketException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if index has a negative value
**Since:** 1.7
**See Also:** getIndex()

- getByInetAddress

```java
public static
NetworkInterface
getByInetAddress​(
InetAddress
addr)
throws
SocketException
```

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

**Parameters:** addr

- The

InetAddress

to search with.
**Returns:** A

NetworkInterface

or

null

if there is no network interface
with the specified IP address.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified address is

null

.

- getNetworkInterfaces

```java
public static
Enumeration
<
NetworkInterface
> getNetworkInterfaces()
throws
SocketException
```

Returns an

Enumeration

of all the interfaces on this machine. The

Enumeration

contains at least one element, possibly representing
a loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

getInetAddresses()

to obtain all IP addresses for this node
**Returns:** an Enumeration of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**See Also:** networkInterfaces()

- networkInterfaces

```java
public static
Stream
<
NetworkInterface
> networkInterfaces()
throws
SocketException
```

Returns a

Stream

of all the interfaces on this machine. The

Stream

contains at least one interface, possibly representing a
loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

inetAddresses()

} to obtain a stream of all IP addresses for
this node, for example:

```java
Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
.flatMap(NetworkInterface::inetAddresses);
```
**Returns:** a Stream of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**Since:** 9

- isUp

```java
public boolean isUp()
throws
SocketException
```

Returns whether a network interface is up and running.

**Returns:** true

if the interface is up and running.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isLoopback

```java
public boolean isLoopback()
throws
SocketException
```

Returns whether a network interface is a loopback interface.

**Returns:** true

if the interface is a loopback interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isPointToPoint

```java
public boolean isPointToPoint()
throws
SocketException
```

Returns whether a network interface is a point to point interface.
A typical point to point interface would be a PPP connection through
a modem.

**Returns:** true

if the interface is a point to point
interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- supportsMulticast

```java
public boolean supportsMulticast()
throws
SocketException
```

Returns whether a network interface supports multicasting or not.

**Returns:** true

if the interface supports Multicasting.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- getHardwareAddress

```java
public byte[] getHardwareAddress()
throws
SocketException
```

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.
If a security manager is set, then the caller must have
the permission

NetPermission

("getNetworkInformation").

**Returns:** a byte array containing the address, or

null

if
the address doesn't exist, is not accessible or a security
manager is set and the caller does not have the permission
NetPermission("getNetworkInformation")
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- getMTU

```java
public int getMTU()
throws
SocketException
```

Returns the Maximum Transmission Unit (MTU) of this interface.

**Returns:** the value of the MTU for that interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isVirtual

```java
public boolean isVirtual()
```

Returns whether this interface is a virtual interface (also called
subinterface).
Virtual interfaces are, on some systems, interfaces created as a child
of a physical interface and given different settings (like address or
MTU). Usually the name of the interface will the name of the parent
followed by a colon (:) and a number identifying the child since there
can be several virtual interfaces attached to a single physical
interface.

**Returns:** true

if this interface is a virtual interface.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same NetworkInterface
as this object.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.getAddress()

Method Detail

- getName

```java
public
String
getName()
```

Get the name of this network interface.

**Returns:** the name of this network interface

- getInetAddresses

```java
public
Enumeration
<
InetAddress
> getInetAddresses()
```

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** an Enumeration object with all or a subset of the InetAddresses
bound to this network interface
**See Also:** inetAddresses()

- inetAddresses

```java
public
Stream
<
InetAddress
> inetAddresses()
```

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** a Stream object with all or a subset of the InetAddresses
bound to this network interface
**Since:** 9

- getInterfaceAddresses

```java
public
List
<
InterfaceAddress
> getInterfaceAddresses()
```

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

**Returns:** a

List

object with all or a subset of the
InterfaceAddresss of this network interface
**Since:** 1.6

- getSubInterfaces

```java
public
Enumeration
<
NetworkInterface
> getSubInterfaces()
```

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

For instance eth0:1 will be a subinterface to eth0.

**Returns:** an Enumeration object with all of the subinterfaces
of this network interface
**Since:** 1.6
**See Also:** subInterfaces()

- subInterfaces

```java
public
Stream
<
NetworkInterface
> subInterfaces()
```

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

**Returns:** a Stream object with all of the subinterfaces
of this network interface
**Since:** 9

- getParent

```java
public
NetworkInterface
getParent()
```

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

**Returns:** The

NetworkInterface

this interface is attached to.
**Since:** 1.6

- getIndex

```java
public int getIndex()
```

Returns the index of this network interface. The index is an integer greater
or equal to zero, or

-1

for unknown. This is a system specific value
and interfaces with the same name can have different indexes on different
machines.

**Returns:** the index of this network interface or

-1

if the index is
unknown
**Since:** 1.7
**See Also:** getByIndex(int)

- getDisplayName

```java
public
String
getDisplayName()
```

Get the display name of this network interface.
A display name is a human readable String describing the network
device.

**Returns:** a non-empty string representing the display name of this network
interface, or null if no display name is available.

- getByName

```java
public static
NetworkInterface
getByName​(
String
name)
throws
SocketException
```

Searches for the network interface with the specified name.

**Parameters:** name

- The name of the network interface.
**Returns:** A

NetworkInterface

with the specified name,
or

null

if there is no network interface
with the specified name.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified name is

null

.

- getByIndex

```java
public static
NetworkInterface
getByIndex​(int index)
throws
SocketException
```

Get a network interface given its index.

**Parameters:** index

- an integer, the index of the interface
**Returns:** the NetworkInterface obtained from its index, or

null

if
there is no interface with such an index on the system
**Throws:** SocketException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if index has a negative value
**Since:** 1.7
**See Also:** getIndex()

- getByInetAddress

```java
public static
NetworkInterface
getByInetAddress​(
InetAddress
addr)
throws
SocketException
```

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

**Parameters:** addr

- The

InetAddress

to search with.
**Returns:** A

NetworkInterface

or

null

if there is no network interface
with the specified IP address.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified address is

null

.

- getNetworkInterfaces

```java
public static
Enumeration
<
NetworkInterface
> getNetworkInterfaces()
throws
SocketException
```

Returns an

Enumeration

of all the interfaces on this machine. The

Enumeration

contains at least one element, possibly representing
a loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

getInetAddresses()

to obtain all IP addresses for this node
**Returns:** an Enumeration of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**See Also:** networkInterfaces()

- networkInterfaces

```java
public static
Stream
<
NetworkInterface
> networkInterfaces()
throws
SocketException
```

Returns a

Stream

of all the interfaces on this machine. The

Stream

contains at least one interface, possibly representing a
loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

inetAddresses()

} to obtain a stream of all IP addresses for
this node, for example:

```java
Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
.flatMap(NetworkInterface::inetAddresses);
```
**Returns:** a Stream of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**Since:** 9

- isUp

```java
public boolean isUp()
throws
SocketException
```

Returns whether a network interface is up and running.

**Returns:** true

if the interface is up and running.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isLoopback

```java
public boolean isLoopback()
throws
SocketException
```

Returns whether a network interface is a loopback interface.

**Returns:** true

if the interface is a loopback interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isPointToPoint

```java
public boolean isPointToPoint()
throws
SocketException
```

Returns whether a network interface is a point to point interface.
A typical point to point interface would be a PPP connection through
a modem.

**Returns:** true

if the interface is a point to point
interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- supportsMulticast

```java
public boolean supportsMulticast()
throws
SocketException
```

Returns whether a network interface supports multicasting or not.

**Returns:** true

if the interface supports Multicasting.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- getHardwareAddress

```java
public byte[] getHardwareAddress()
throws
SocketException
```

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.
If a security manager is set, then the caller must have
the permission

NetPermission

("getNetworkInformation").

**Returns:** a byte array containing the address, or

null

if
the address doesn't exist, is not accessible or a security
manager is set and the caller does not have the permission
NetPermission("getNetworkInformation")
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- getMTU

```java
public int getMTU()
throws
SocketException
```

Returns the Maximum Transmission Unit (MTU) of this interface.

**Returns:** the value of the MTU for that interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

- isVirtual

```java
public boolean isVirtual()
```

Returns whether this interface is a virtual interface (also called
subinterface).
Virtual interfaces are, on some systems, interfaces created as a child
of a physical interface and given different settings (like address or
MTU). Usually the name of the interface will the name of the parent
followed by a colon (:) and a number identifying the child since there
can be several virtual interfaces attached to a single physical
interface.

**Returns:** true

if this interface is a virtual interface.
**Since:** 1.6

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same NetworkInterface
as this object.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.getAddress()

---

#### Method Detail

getName

```java
public
String
getName()
```

Get the name of this network interface.

**Returns:** the name of this network interface

---

#### getName

public

String

getName()

Get the name of this network interface.

getInetAddresses

```java
public
Enumeration
<
InetAddress
> getInetAddresses()
```

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** an Enumeration object with all or a subset of the InetAddresses
bound to this network interface
**See Also:** inetAddresses()

---

#### getInetAddresses

public

Enumeration

<

InetAddress

> getInetAddresses()

Get an Enumeration with all or a subset of the InetAddresses bound to
this network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException
will be returned in the Enumeration. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

inetAddresses

```java
public
Stream
<
InetAddress
> inetAddresses()
```

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

**Returns:** a Stream object with all or a subset of the InetAddresses
bound to this network interface
**Since:** 9

---

#### inetAddresses

public

Stream

<

InetAddress

> inetAddresses()

Get a Stream of all or a subset of the InetAddresses bound to this
network interface.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

If there is a security manager, its

checkConnect

method is called for each InetAddress. Only InetAddresses where
the

checkConnect

doesn't throw a SecurityException will be
returned in the Stream. However, if the caller has the

NetPermission

("getNetworkInformation") permission, then all
InetAddresses are returned.

getInterfaceAddresses

```java
public
List
<
InterfaceAddress
> getInterfaceAddresses()
```

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

**Returns:** a

List

object with all or a subset of the
InterfaceAddresss of this network interface
**Since:** 1.6

---

#### getInterfaceAddresses

public

List

<

InterfaceAddress

> getInterfaceAddresses()

Get a List of all or a subset of the

InterfaceAddresses

of this network interface.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

If there is a security manager, its

checkConnect

method is called with the InetAddress for each InterfaceAddress.
Only InterfaceAddresses where the

checkConnect

doesn't throw
a SecurityException will be returned in the List.

getSubInterfaces

```java
public
Enumeration
<
NetworkInterface
> getSubInterfaces()
```

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

For instance eth0:1 will be a subinterface to eth0.

**Returns:** an Enumeration object with all of the subinterfaces
of this network interface
**Since:** 1.6
**See Also:** subInterfaces()

---

#### getSubInterfaces

public

Enumeration

<

NetworkInterface

> getSubInterfaces()

Get an Enumeration with all the subinterfaces (also known as virtual
interfaces) attached to this network interface.

For instance eth0:1 will be a subinterface to eth0.

For instance eth0:1 will be a subinterface to eth0.

subInterfaces

```java
public
Stream
<
NetworkInterface
> subInterfaces()
```

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

**Returns:** a Stream object with all of the subinterfaces
of this network interface
**Since:** 9

---

#### subInterfaces

public

Stream

<

NetworkInterface

> subInterfaces()

Get a Stream of all subinterfaces (also known as virtual
interfaces) attached to this network interface.

getParent

```java
public
NetworkInterface
getParent()
```

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

**Returns:** The

NetworkInterface

this interface is attached to.
**Since:** 1.6

---

#### getParent

public

NetworkInterface

getParent()

Returns the parent NetworkInterface of this interface if this is
a subinterface, or

null

if it is a physical
(non virtual) interface or has no parent.

getIndex

```java
public int getIndex()
```

Returns the index of this network interface. The index is an integer greater
or equal to zero, or

-1

for unknown. This is a system specific value
and interfaces with the same name can have different indexes on different
machines.

**Returns:** the index of this network interface or

-1

if the index is
unknown
**Since:** 1.7
**See Also:** getByIndex(int)

---

#### getIndex

public int getIndex()

Returns the index of this network interface. The index is an integer greater
or equal to zero, or

-1

for unknown. This is a system specific value
and interfaces with the same name can have different indexes on different
machines.

getDisplayName

```java
public
String
getDisplayName()
```

Get the display name of this network interface.
A display name is a human readable String describing the network
device.

**Returns:** a non-empty string representing the display name of this network
interface, or null if no display name is available.

---

#### getDisplayName

public

String

getDisplayName()

Get the display name of this network interface.
A display name is a human readable String describing the network
device.

getByName

```java
public static
NetworkInterface
getByName​(
String
name)
throws
SocketException
```

Searches for the network interface with the specified name.

**Parameters:** name

- The name of the network interface.
**Returns:** A

NetworkInterface

with the specified name,
or

null

if there is no network interface
with the specified name.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified name is

null

.

---

#### getByName

public static

NetworkInterface

getByName​(

String

name)
throws

SocketException

Searches for the network interface with the specified name.

getByIndex

```java
public static
NetworkInterface
getByIndex​(int index)
throws
SocketException
```

Get a network interface given its index.

**Parameters:** index

- an integer, the index of the interface
**Returns:** the NetworkInterface obtained from its index, or

null

if
there is no interface with such an index on the system
**Throws:** SocketException

- if an I/O error occurs.
**Throws:** IllegalArgumentException

- if index has a negative value
**Since:** 1.7
**See Also:** getIndex()

---

#### getByIndex

public static

NetworkInterface

getByIndex​(int index)
throws

SocketException

Get a network interface given its index.

getByInetAddress

```java
public static
NetworkInterface
getByInetAddress​(
InetAddress
addr)
throws
SocketException
```

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

**Parameters:** addr

- The

InetAddress

to search with.
**Returns:** A

NetworkInterface

or

null

if there is no network interface
with the specified IP address.
**Throws:** SocketException

- If an I/O error occurs.
**Throws:** NullPointerException

- If the specified address is

null

.

---

#### getByInetAddress

public static

NetworkInterface

getByInetAddress​(

InetAddress

addr)
throws

SocketException

Convenience method to search for a network interface that
has the specified Internet Protocol (IP) address bound to
it.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

If the specified IP address is bound to multiple network
interfaces it is not defined which network interface is
returned.

getNetworkInterfaces

```java
public static
Enumeration
<
NetworkInterface
> getNetworkInterfaces()
throws
SocketException
```

Returns an

Enumeration

of all the interfaces on this machine. The

Enumeration

contains at least one element, possibly representing
a loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

getInetAddresses()

to obtain all IP addresses for this node
**Returns:** an Enumeration of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**See Also:** networkInterfaces()

---

#### getNetworkInterfaces

public static

Enumeration

<

NetworkInterface

> getNetworkInterfaces()
throws

SocketException

Returns an

Enumeration

of all the interfaces on this machine. The

Enumeration

contains at least one element, possibly representing
a loopback interface that only supports communication between entities on
this machine.

networkInterfaces

```java
public static
Stream
<
NetworkInterface
> networkInterfaces()
throws
SocketException
```

Returns a

Stream

of all the interfaces on this machine. The

Stream

contains at least one interface, possibly representing a
loopback interface that only supports communication between entities on
this machine.

**API Note:** this method can be used in combination with

inetAddresses()

} to obtain a stream of all IP addresses for
this node, for example:

```java
Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
.flatMap(NetworkInterface::inetAddresses);
```
**Returns:** a Stream of NetworkInterfaces found on this machine
**Throws:** SocketException

- if an I/O error occurs,
or if the platform does not have at least one configured
network interface.
**Since:** 9

---

#### networkInterfaces

public static

Stream

<

NetworkInterface

> networkInterfaces()
throws

SocketException

Returns a

Stream

of all the interfaces on this machine. The

Stream

contains at least one interface, possibly representing a
loopback interface that only supports communication between entities on
this machine.

Stream<InetAddress> addrs = NetworkInterface.networkInterfaces()
.flatMap(NetworkInterface::inetAddresses);

isUp

```java
public boolean isUp()
throws
SocketException
```

Returns whether a network interface is up and running.

**Returns:** true

if the interface is up and running.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### isUp

public boolean isUp()
throws

SocketException

Returns whether a network interface is up and running.

isLoopback

```java
public boolean isLoopback()
throws
SocketException
```

Returns whether a network interface is a loopback interface.

**Returns:** true

if the interface is a loopback interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### isLoopback

public boolean isLoopback()
throws

SocketException

Returns whether a network interface is a loopback interface.

isPointToPoint

```java
public boolean isPointToPoint()
throws
SocketException
```

Returns whether a network interface is a point to point interface.
A typical point to point interface would be a PPP connection through
a modem.

**Returns:** true

if the interface is a point to point
interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### isPointToPoint

public boolean isPointToPoint()
throws

SocketException

Returns whether a network interface is a point to point interface.
A typical point to point interface would be a PPP connection through
a modem.

supportsMulticast

```java
public boolean supportsMulticast()
throws
SocketException
```

Returns whether a network interface supports multicasting or not.

**Returns:** true

if the interface supports Multicasting.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### supportsMulticast

public boolean supportsMulticast()
throws

SocketException

Returns whether a network interface supports multicasting or not.

getHardwareAddress

```java
public byte[] getHardwareAddress()
throws
SocketException
```

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.
If a security manager is set, then the caller must have
the permission

NetPermission

("getNetworkInformation").

**Returns:** a byte array containing the address, or

null

if
the address doesn't exist, is not accessible or a security
manager is set and the caller does not have the permission
NetPermission("getNetworkInformation")
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### getHardwareAddress

public byte[] getHardwareAddress()
throws

SocketException

Returns the hardware address (usually MAC) of the interface if it
has one and if it can be accessed given the current privileges.
If a security manager is set, then the caller must have
the permission

NetPermission

("getNetworkInformation").

getMTU

```java
public int getMTU()
throws
SocketException
```

Returns the Maximum Transmission Unit (MTU) of this interface.

**Returns:** the value of the MTU for that interface.
**Throws:** SocketException

- if an I/O error occurs.
**Since:** 1.6

---

#### getMTU

public int getMTU()
throws

SocketException

Returns the Maximum Transmission Unit (MTU) of this interface.

isVirtual

```java
public boolean isVirtual()
```

Returns whether this interface is a virtual interface (also called
subinterface).
Virtual interfaces are, on some systems, interfaces created as a child
of a physical interface and given different settings (like address or
MTU). Usually the name of the interface will the name of the parent
followed by a colon (:) and a number identifying the child since there
can be several virtual interfaces attached to a single physical
interface.

**Returns:** true

if this interface is a virtual interface.
**Since:** 1.6

---

#### isVirtual

public boolean isVirtual()

Returns whether this interface is a virtual interface (also called
subinterface).
Virtual interfaces are, on some systems, interfaces created as a child
of a physical interface and given different settings (like address or
MTU). Usually the name of the interface will the name of the parent
followed by a colon (:) and a number identifying the child since there
can be several virtual interfaces attached to a single physical
interface.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same NetworkInterface
as this object.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** InetAddress.getAddress()

---

#### equals

public boolean equals​(

Object

obj)

Compares this object against the specified object.
The result is

true

if and only if the argument is
not

null

and it represents the same NetworkInterface
as this object.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

Two instances of

NetworkInterface

represent the same
NetworkInterface if both name and addrs are the same for both.

---

