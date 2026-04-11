# Class InterfaceAddress

**Source:** `java.base\java\net\InterfaceAddress.html`

### Class Description

```java
public class
InterfaceAddress

extends
Object
```

This class represents a Network Interface address. In short it's an
IP address, a subnet mask and a broadcast address when the address is
an IPv4 one. An IP address and a network prefix length in the case
of IPv6 address.

**Since:** 1.6
**See Also:** NetworkInterface

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
InetAddress
getAddress()

Returns an

InetAddress

for this address.

**Returns:**
- the

InetAddress

for this address.

---

#### public
InetAddress
getBroadcast()

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

**Returns:**
- the

InetAddress

representing the broadcast
address or

null

if there is no broadcast address.

---

#### public short getNetworkPrefixLength()

Returns the network prefix length for this address. This is also known
as the subnet mask in the context of IPv4 addresses.
Typical IPv4 values would be 8 (255.0.0.0), 16 (255.255.0.0)
or 24 (255.255.255.0).

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

**Returns:**
- a

short

representing the prefix length for the
subnet of that address.

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

and it represents the same interface address as
this object.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

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
- hashCode()

---

#### public int hashCode()

Returns a hashcode for this Interface address.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this Interface address.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Converts this Interface address to a

String

. The
string returned is of the form: InetAddress / prefix length [ broadcast address ].

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this Interface address.

---

### Additional Sections

#### Class InterfaceAddress

java.lang.Object

- java.net.InterfaceAddress

java.net.InterfaceAddress

```java
public class
InterfaceAddress

extends
Object
```

This class represents a Network Interface address. In short it's an
IP address, a subnet mask and a broadcast address when the address is
an IPv4 one. An IP address and a network prefix length in the case
of IPv6 address.

**Since:** 1.6
**See Also:** NetworkInterface

public class

InterfaceAddress

extends

Object

This class represents a Network Interface address. In short it's an
IP address, a subnet mask and a broadcast address when the address is
an IPv4 one. An IP address and a network prefix length in the case
of IPv6 address.

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

Compares this object against the specified object.

InetAddress

getAddress

()

Returns an

InetAddress

for this address.

InetAddress

getBroadcast

()

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

short

getNetworkPrefixLength

()

Returns the network prefix length for this address.

int

hashCode

()

Returns a hashcode for this Interface address.

String

toString

()

Converts this Interface address to a

String

.

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

Compares this object against the specified object.

InetAddress

getAddress

()

Returns an

InetAddress

for this address.

InetAddress

getBroadcast

()

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

short

getNetworkPrefixLength

()

Returns the network prefix length for this address.

int

hashCode

()

Returns a hashcode for this Interface address.

String

toString

()

Converts this Interface address to a

String

.

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

Compares this object against the specified object.

Returns an

InetAddress

for this address.

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Returns the network prefix length for this address.

Returns a hashcode for this Interface address.

Converts this Interface address to a

String

.

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

============ METHOD DETAIL ==========

- Method Detail

- getAddress

```java
public
InetAddress
getAddress()
```

Returns an

InetAddress

for this address.

**Returns:** the

InetAddress

for this address.

- getBroadcast

```java
public
InetAddress
getBroadcast()
```

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

**Returns:** the

InetAddress

representing the broadcast
address or

null

if there is no broadcast address.

- getNetworkPrefixLength

```java
public short getNetworkPrefixLength()
```

Returns the network prefix length for this address. This is also known
as the subnet mask in the context of IPv4 addresses.
Typical IPv4 values would be 8 (255.0.0.0), 16 (255.255.0.0)
or 24 (255.255.255.0).

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

**Returns:** a

short

representing the prefix length for the
subnet of that address.

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

and it represents the same interface address as
this object.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this Interface address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Interface address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Converts this Interface address to a

String

. The
string returned is of the form: InetAddress / prefix length [ broadcast address ].

**Overrides:** toString

in class

Object
**Returns:** a string representation of this Interface address.

Method Detail

- getAddress

```java
public
InetAddress
getAddress()
```

Returns an

InetAddress

for this address.

**Returns:** the

InetAddress

for this address.

- getBroadcast

```java
public
InetAddress
getBroadcast()
```

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

**Returns:** the

InetAddress

representing the broadcast
address or

null

if there is no broadcast address.

- getNetworkPrefixLength

```java
public short getNetworkPrefixLength()
```

Returns the network prefix length for this address. This is also known
as the subnet mask in the context of IPv4 addresses.
Typical IPv4 values would be 8 (255.0.0.0), 16 (255.255.0.0)
or 24 (255.255.255.0).

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

**Returns:** a

short

representing the prefix length for the
subnet of that address.

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

and it represents the same interface address as
this object.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** hashCode()

- hashCode

```java
public int hashCode()
```

Returns a hashcode for this Interface address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Interface address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Converts this Interface address to a

String

. The
string returned is of the form: InetAddress / prefix length [ broadcast address ].

**Overrides:** toString

in class

Object
**Returns:** a string representation of this Interface address.

---

#### Method Detail

getAddress

```java
public
InetAddress
getAddress()
```

Returns an

InetAddress

for this address.

**Returns:** the

InetAddress

for this address.

---

#### getAddress

public

InetAddress

getAddress()

Returns an

InetAddress

for this address.

getBroadcast

```java
public
InetAddress
getBroadcast()
```

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

**Returns:** the

InetAddress

representing the broadcast
address or

null

if there is no broadcast address.

---

#### getBroadcast

public

InetAddress

getBroadcast()

Returns an

InetAddress

for the broadcast address
for this InterfaceAddress.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

Only IPv4 networks have broadcast address therefore, in the case
of an IPv6 network,

null

will be returned.

getNetworkPrefixLength

```java
public short getNetworkPrefixLength()
```

Returns the network prefix length for this address. This is also known
as the subnet mask in the context of IPv4 addresses.
Typical IPv4 values would be 8 (255.0.0.0), 16 (255.255.0.0)
or 24 (255.255.255.0).

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

**Returns:** a

short

representing the prefix length for the
subnet of that address.

---

#### getNetworkPrefixLength

public short getNetworkPrefixLength()

Returns the network prefix length for this address. This is also known
as the subnet mask in the context of IPv4 addresses.
Typical IPv4 values would be 8 (255.0.0.0), 16 (255.255.0.0)
or 24 (255.255.255.0).

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

Typical IPv6 values would be 128 (::1/128) or 10 (fe80::203:baff:fe27:1243/10)

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

and it represents the same interface address as
this object.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** hashCode()

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

and it represents the same interface address as
this object.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

Two instances of

InterfaceAddress

represent the same
address if the InetAddress, the prefix length and the broadcast are
the same for both.

hashCode

```java
public int hashCode()
```

Returns a hashcode for this Interface address.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this Interface address.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hashcode for this Interface address.

toString

```java
public
String
toString()
```

Converts this Interface address to a

String

. The
string returned is of the form: InetAddress / prefix length [ broadcast address ].

**Overrides:** toString

in class

Object
**Returns:** a string representation of this Interface address.

---

#### toString

public

String

toString()

Converts this Interface address to a

String

. The
string returned is of the form: InetAddress / prefix length [ broadcast address ].

---

