# Class PeerAddressChangeNotification

**Source:** `jdk.sctp\com\sun\nio\sctp\PeerAddressChangeNotification.html`

### Class Description

```java
public abstract class
PeerAddressChangeNotification

extends
Object

implements
Notification
```

Notification emitted when a destination address on a multi-homed peer
encounters a change.

**All Implemented Interfaces:** Notification

---

### Field Details

*No entries found.*

### Constructor Details

#### protected PeerAddressChangeNotification()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
SocketAddress
address()

Returns the peer address.

**Returns:**
- The peer address

---

#### public abstract
Association
association()

Returns the association that this notification is applicable to.

**Specified by:**
- association

in interface

Notification

**Returns:**
- The association whose peer address changed

---

#### public abstract
PeerAddressChangeNotification.AddressChangeEvent
event()

Returns the type of change event.

**Returns:**
- The event

---

### Additional Sections

#### Class PeerAddressChangeNotification

java.lang.Object

- com.sun.nio.sctp.PeerAddressChangeNotification

com.sun.nio.sctp.PeerAddressChangeNotification

**All Implemented Interfaces:** Notification

```java
public abstract class
PeerAddressChangeNotification

extends
Object

implements
Notification
```

Notification emitted when a destination address on a multi-homed peer
encounters a change.

**Since:** 1.7

public abstract class

PeerAddressChangeNotification

extends

Object

implements

Notification

Notification emitted when a destination address on a multi-homed peer
encounters a change.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PeerAddressChangeNotification.AddressChangeEvent

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PeerAddressChangeNotification

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

SocketAddress

address

()

Returns the peer address.

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

PeerAddressChangeNotification.AddressChangeEvent

event

()

Returns the type of change event.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PeerAddressChangeNotification.AddressChangeEvent

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

---

#### Nested Class Summary

Defines the type of address change event that occurred to the destination
address on a multi-homed peer when it encounters a change of interface
details.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PeerAddressChangeNotification

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

SocketAddress

address

()

Returns the peer address.

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

PeerAddressChangeNotification.AddressChangeEvent

event

()

Returns the type of change event.

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

Returns the peer address.

Returns the association that this notification is applicable to.

Returns the type of change event.

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

- PeerAddressChangeNotification

```java
protected PeerAddressChangeNotification()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- address

```java
public abstract
SocketAddress
address()
```

Returns the peer address.

**Returns:** The peer address

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose peer address changed

- event

```java
public abstract
PeerAddressChangeNotification.AddressChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

Constructor Detail

- PeerAddressChangeNotification

```java
protected PeerAddressChangeNotification()
```

Initializes a new instance of this class.

---

#### Constructor Detail

PeerAddressChangeNotification

```java
protected PeerAddressChangeNotification()
```

Initializes a new instance of this class.

---

#### PeerAddressChangeNotification

protected PeerAddressChangeNotification()

Initializes a new instance of this class.

Method Detail

- address

```java
public abstract
SocketAddress
address()
```

Returns the peer address.

**Returns:** The peer address

- association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose peer address changed

- event

```java
public abstract
PeerAddressChangeNotification.AddressChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

---

#### Method Detail

address

```java
public abstract
SocketAddress
address()
```

Returns the peer address.

**Returns:** The peer address

---

#### address

public abstract

SocketAddress

address()

Returns the peer address.

association

```java
public abstract
Association
association()
```

Returns the association that this notification is applicable to.

**Specified by:** association

in interface

Notification
**Returns:** The association whose peer address changed

---

#### association

public abstract

Association

association()

Returns the association that this notification is applicable to.

event

```java
public abstract
PeerAddressChangeNotification.AddressChangeEvent
event()
```

Returns the type of change event.

**Returns:** The event

---

#### event

public abstract

PeerAddressChangeNotification.AddressChangeEvent

event()

Returns the type of change event.

---

