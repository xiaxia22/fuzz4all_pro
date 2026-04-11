# Class MembershipKey

**Source:** `java.base\java\nio\channels\MembershipKey.html`

### Class Description

```java
public abstract class
MembershipKey

extends
Object
```

A token representing the membership of an Internet Protocol (IP) multicast
group.

A membership key may represent a membership to receive all datagrams sent
to the group, or it may be

source-specific

, meaning that it
represents a membership that receives only datagrams from a specific source
address. Whether or not a membership key is source-specific may be determined
by invoking its

sourceAddress

method.

A membership key is valid upon creation and remains valid until the
membership is dropped by invoking the

drop

method, or
the channel is closed. The validity of the membership key may be tested
by invoking its

isValid

method.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

**Since:** 1.7
**See Also:** MulticastChannel

---

### Field Details

*No entries found.*

### Constructor Details

#### protected MembershipKey()

Initializes a new instance of this class.

---

### Method Details

#### public abstract boolean isValid()

Tells whether or not this membership is valid.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

**Returns:**
- true

if this membership key is valid,

false

otherwise

---

#### public abstract void drop()

Drop membership.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

---

#### public abstract
MembershipKey
block​(
InetAddress
source)
throws
IOException

Block multicast datagrams from the given source address.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

**Parameters:**
- source

- The source address to block

**Returns:**
- This membership key

**Throws:**
- IllegalArgumentException

- If the

source

parameter is not a unicast address or
is not the same address type as the multicast group
- IllegalStateException

- If this membership key is source-specific or is no longer valid
- UnsupportedOperationException

- If the underlying operating system does not support source
filtering
- IOException

- If an I/O error occurs

---

#### public abstract
MembershipKey
unblock​(
InetAddress
source)

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

**Parameters:**
- source

- The source address to unblock

**Returns:**
- This membership key

**Throws:**
- IllegalStateException

- If the given source address is not currently blocked or the
membership key is no longer valid

---

#### public abstract
MulticastChannel
channel()

Returns the channel for which this membership key was created. This
method will continue to return the channel even after the membership
becomes

invalid

.

**Returns:**
- the channel

---

#### public abstract
InetAddress
group()

Returns the multicast group for which this membership key was created.
This method will continue to return the group even after the membership
becomes

invalid

.

**Returns:**
- the multicast group

---

#### public abstract
NetworkInterface
networkInterface()

Returns the network interface for which this membership key was created.
This method will continue to return the network interface even after the
membership becomes

invalid

.

**Returns:**
- the network interface

---

#### public abstract
InetAddress
sourceAddress()

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

**Returns:**
- The source address if this membership key is source-specific,
otherwise

null

---

### Additional Sections

#### Class MembershipKey

java.lang.Object

- java.nio.channels.MembershipKey

java.nio.channels.MembershipKey

```java
public abstract class
MembershipKey

extends
Object
```

A token representing the membership of an Internet Protocol (IP) multicast
group.

A membership key may represent a membership to receive all datagrams sent
to the group, or it may be

source-specific

, meaning that it
represents a membership that receives only datagrams from a specific source
address. Whether or not a membership key is source-specific may be determined
by invoking its

sourceAddress

method.

A membership key is valid upon creation and remains valid until the
membership is dropped by invoking the

drop

method, or
the channel is closed. The validity of the membership key may be tested
by invoking its

isValid

method.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

**Since:** 1.7
**See Also:** MulticastChannel

public abstract class

MembershipKey

extends

Object

A token representing the membership of an Internet Protocol (IP) multicast
group.

A membership key may represent a membership to receive all datagrams sent
to the group, or it may be

source-specific

, meaning that it
represents a membership that receives only datagrams from a specific source
address. Whether or not a membership key is source-specific may be determined
by invoking its

sourceAddress

method.

A membership key is valid upon creation and remains valid until the
membership is dropped by invoking the

drop

method, or
the channel is closed. The validity of the membership key may be tested
by invoking its

isValid

method.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

A membership key may represent a membership to receive all datagrams sent
to the group, or it may be

source-specific

, meaning that it
represents a membership that receives only datagrams from a specific source
address. Whether or not a membership key is source-specific may be determined
by invoking its

sourceAddress

method.

A membership key is valid upon creation and remains valid until the
membership is dropped by invoking the

drop

method, or
the channel is closed. The validity of the membership key may be tested
by invoking its

isValid

method.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

A membership key is valid upon creation and remains valid until the
membership is dropped by invoking the

drop

method, or
the channel is closed. The validity of the membership key may be tested
by invoking its

isValid

method.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

Where a membership key is not source-specific and the underlying operation
system supports source filtering, then the

block

and

unblock

methods can be used to block or unblock multicast datagrams
from particular source addresses.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MembershipKey

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

MembershipKey

block

​(

InetAddress

source)

Block multicast datagrams from the given source address.

abstract

MulticastChannel

channel

()

Returns the channel for which this membership key was created.

abstract void

drop

()

Drop membership.

abstract

InetAddress

group

()

Returns the multicast group for which this membership key was created.

abstract boolean

isValid

()

Tells whether or not this membership is valid.

abstract

NetworkInterface

networkInterface

()

Returns the network interface for which this membership key was created.

abstract

InetAddress

sourceAddress

()

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

abstract

MembershipKey

unblock

​(

InetAddress

source)

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MembershipKey

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

MembershipKey

block

​(

InetAddress

source)

Block multicast datagrams from the given source address.

abstract

MulticastChannel

channel

()

Returns the channel for which this membership key was created.

abstract void

drop

()

Drop membership.

abstract

InetAddress

group

()

Returns the multicast group for which this membership key was created.

abstract boolean

isValid

()

Tells whether or not this membership is valid.

abstract

NetworkInterface

networkInterface

()

Returns the network interface for which this membership key was created.

abstract

InetAddress

sourceAddress

()

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

abstract

MembershipKey

unblock

​(

InetAddress

source)

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

- Methods declared in class java.lang.

Object

clone

,

equals

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

Block multicast datagrams from the given source address.

Returns the channel for which this membership key was created.

Drop membership.

Returns the multicast group for which this membership key was created.

Tells whether or not this membership is valid.

Returns the network interface for which this membership key was created.

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

Methods declared in class java.lang.

Object

clone

,

equals

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MembershipKey

```java
protected MembershipKey()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- isValid

```java
public abstract boolean isValid()
```

Tells whether or not this membership is valid.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

**Returns:** true

if this membership key is valid,

false

otherwise

- drop

```java
public abstract void drop()
```

Drop membership.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

- block

```java
public abstract
MembershipKey
block​(
InetAddress
source)
throws
IOException
```

Block multicast datagrams from the given source address.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

**Parameters:** source

- The source address to block
**Returns:** This membership key
**Throws:** IllegalArgumentException

- If the

source

parameter is not a unicast address or
is not the same address type as the multicast group
**Throws:** IllegalStateException

- If this membership key is source-specific or is no longer valid
**Throws:** UnsupportedOperationException

- If the underlying operating system does not support source
filtering
**Throws:** IOException

- If an I/O error occurs

- unblock

```java
public abstract
MembershipKey
unblock​(
InetAddress
source)
```

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

**Parameters:** source

- The source address to unblock
**Returns:** This membership key
**Throws:** IllegalStateException

- If the given source address is not currently blocked or the
membership key is no longer valid

- channel

```java
public abstract
MulticastChannel
channel()
```

Returns the channel for which this membership key was created. This
method will continue to return the channel even after the membership
becomes

invalid

.

**Returns:** the channel

- group

```java
public abstract
InetAddress
group()
```

Returns the multicast group for which this membership key was created.
This method will continue to return the group even after the membership
becomes

invalid

.

**Returns:** the multicast group

- networkInterface

```java
public abstract
NetworkInterface
networkInterface()
```

Returns the network interface for which this membership key was created.
This method will continue to return the network interface even after the
membership becomes

invalid

.

**Returns:** the network interface

- sourceAddress

```java
public abstract
InetAddress
sourceAddress()
```

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

**Returns:** The source address if this membership key is source-specific,
otherwise

null

Constructor Detail

- MembershipKey

```java
protected MembershipKey()
```

Initializes a new instance of this class.

---

#### Constructor Detail

MembershipKey

```java
protected MembershipKey()
```

Initializes a new instance of this class.

---

#### MembershipKey

protected MembershipKey()

Initializes a new instance of this class.

Method Detail

- isValid

```java
public abstract boolean isValid()
```

Tells whether or not this membership is valid.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

**Returns:** true

if this membership key is valid,

false

otherwise

- drop

```java
public abstract void drop()
```

Drop membership.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

- block

```java
public abstract
MembershipKey
block​(
InetAddress
source)
throws
IOException
```

Block multicast datagrams from the given source address.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

**Parameters:** source

- The source address to block
**Returns:** This membership key
**Throws:** IllegalArgumentException

- If the

source

parameter is not a unicast address or
is not the same address type as the multicast group
**Throws:** IllegalStateException

- If this membership key is source-specific or is no longer valid
**Throws:** UnsupportedOperationException

- If the underlying operating system does not support source
filtering
**Throws:** IOException

- If an I/O error occurs

- unblock

```java
public abstract
MembershipKey
unblock​(
InetAddress
source)
```

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

**Parameters:** source

- The source address to unblock
**Returns:** This membership key
**Throws:** IllegalStateException

- If the given source address is not currently blocked or the
membership key is no longer valid

- channel

```java
public abstract
MulticastChannel
channel()
```

Returns the channel for which this membership key was created. This
method will continue to return the channel even after the membership
becomes

invalid

.

**Returns:** the channel

- group

```java
public abstract
InetAddress
group()
```

Returns the multicast group for which this membership key was created.
This method will continue to return the group even after the membership
becomes

invalid

.

**Returns:** the multicast group

- networkInterface

```java
public abstract
NetworkInterface
networkInterface()
```

Returns the network interface for which this membership key was created.
This method will continue to return the network interface even after the
membership becomes

invalid

.

**Returns:** the network interface

- sourceAddress

```java
public abstract
InetAddress
sourceAddress()
```

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

**Returns:** The source address if this membership key is source-specific,
otherwise

null

---

#### Method Detail

isValid

```java
public abstract boolean isValid()
```

Tells whether or not this membership is valid.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

**Returns:** true

if this membership key is valid,

false

otherwise

---

#### isValid

public abstract boolean isValid()

Tells whether or not this membership is valid.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

A multicast group membership is valid upon creation and remains
valid until the membership is dropped by invoking the

drop

method, or the channel is closed.

drop

```java
public abstract void drop()
```

Drop membership.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

---

#### drop

public abstract void drop()

Drop membership.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

If the membership key represents a membership to receive all datagrams
then the membership is dropped and the channel will no longer receive any
datagrams sent to the group. If the membership key is source-specific
then the channel will no longer receive datagrams sent to the group from
that source address.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

After membership is dropped it may still be possible to receive
datagrams sent to the group. This can arise when datagrams are waiting to
be received in the socket's receive buffer. After membership is dropped
then the channel may

join

the group again
in which case a new membership key is returned.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

Upon return, this membership object will be

invalid

.
If the multicast group membership is already invalid then invoking this
method has no effect. Once a multicast group membership is invalid,
it remains invalid forever.

block

```java
public abstract
MembershipKey
block​(
InetAddress
source)
throws
IOException
```

Block multicast datagrams from the given source address.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

**Parameters:** source

- The source address to block
**Returns:** This membership key
**Throws:** IllegalArgumentException

- If the

source

parameter is not a unicast address or
is not the same address type as the multicast group
**Throws:** IllegalStateException

- If this membership key is source-specific or is no longer valid
**Throws:** UnsupportedOperationException

- If the underlying operating system does not support source
filtering
**Throws:** IOException

- If an I/O error occurs

---

#### block

public abstract

MembershipKey

block​(

InetAddress

source)
throws

IOException

Block multicast datagrams from the given source address.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

If this membership key is not source-specific, and the underlying
operating system supports source filtering, then this method blocks
multicast datagrams from the given source address. If the given source
address is already blocked then this method has no effect.
After a source address is blocked it may still be possible to receive
datagrams from that source. This can arise when datagrams are waiting to
be received in the socket's receive buffer.

unblock

```java
public abstract
MembershipKey
unblock​(
InetAddress
source)
```

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

**Parameters:** source

- The source address to unblock
**Returns:** This membership key
**Throws:** IllegalStateException

- If the given source address is not currently blocked or the
membership key is no longer valid

---

#### unblock

public abstract

MembershipKey

unblock​(

InetAddress

source)

Unblock multicast datagrams from the given source address that was
previously blocked using the

block

method.

channel

```java
public abstract
MulticastChannel
channel()
```

Returns the channel for which this membership key was created. This
method will continue to return the channel even after the membership
becomes

invalid

.

**Returns:** the channel

---

#### channel

public abstract

MulticastChannel

channel()

Returns the channel for which this membership key was created. This
method will continue to return the channel even after the membership
becomes

invalid

.

group

```java
public abstract
InetAddress
group()
```

Returns the multicast group for which this membership key was created.
This method will continue to return the group even after the membership
becomes

invalid

.

**Returns:** the multicast group

---

#### group

public abstract

InetAddress

group()

Returns the multicast group for which this membership key was created.
This method will continue to return the group even after the membership
becomes

invalid

.

networkInterface

```java
public abstract
NetworkInterface
networkInterface()
```

Returns the network interface for which this membership key was created.
This method will continue to return the network interface even after the
membership becomes

invalid

.

**Returns:** the network interface

---

#### networkInterface

public abstract

NetworkInterface

networkInterface()

Returns the network interface for which this membership key was created.
This method will continue to return the network interface even after the
membership becomes

invalid

.

sourceAddress

```java
public abstract
InetAddress
sourceAddress()
```

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

**Returns:** The source address if this membership key is source-specific,
otherwise

null

---

#### sourceAddress

public abstract

InetAddress

sourceAddress()

Returns the source address if this membership key is source-specific,
or

null

if this membership is not source-specific.

---

