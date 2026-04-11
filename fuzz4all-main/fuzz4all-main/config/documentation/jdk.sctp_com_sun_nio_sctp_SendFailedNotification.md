# Class SendFailedNotification

**Source:** `jdk.sctp\com\sun\nio\sctp\SendFailedNotification.html`

### Class Description

```java
public abstract class
SendFailedNotification

extends
Object

implements
Notification
```

Notification emitted when a send failed notification has been received.

A send failed notification indicates that a message cannot be delivered.
Typically this is because the association has been shutdown with unsent data
in the socket output buffer, or in the case of a

SctpMultiChannel

the association failed to setup.

**All Implemented Interfaces:** Notification

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SendFailedNotification()

Initializes a new instance of this class.

---

### Method Details

#### public abstract
Association
association()

Returns the association that this notification is applicable to.

**Specified by:**
- association

in interface

Notification

**Returns:**
- The association that failed to send, or

null

if
there is no association, that is, the notification follows a

AssociationChangeNotification.AssocChangeEvent.CANT_START

---

#### public abstract
SocketAddress
address()

Returns the address.

**Returns:**
- The peer primary address of the association or the address that
the message was sent to

---

#### public abstract
ByteBuffer
buffer()

Returns the data that was to be sent.

**Returns:**
- The user data. The buffers position will be

0

and its
limit will be set to the end of the data.

---

#### public abstract int errorCode()

Returns the error code.

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

**Returns:**
- The error code

---

#### public abstract int streamNumber()

Returns the stream number that the messge was to be sent on.

**Returns:**
- The stream number

---

### Additional Sections

#### Class SendFailedNotification

java.lang.Object

- com.sun.nio.sctp.SendFailedNotification

com.sun.nio.sctp.SendFailedNotification

**All Implemented Interfaces:** Notification

```java
public abstract class
SendFailedNotification

extends
Object

implements
Notification
```

Notification emitted when a send failed notification has been received.

A send failed notification indicates that a message cannot be delivered.
Typically this is because the association has been shutdown with unsent data
in the socket output buffer, or in the case of a

SctpMultiChannel

the association failed to setup.

**Since:** 1.7

public abstract class

SendFailedNotification

extends

Object

implements

Notification

Notification emitted when a send failed notification has been received.

A send failed notification indicates that a message cannot be delivered.
Typically this is because the association has been shutdown with unsent data
in the socket output buffer, or in the case of a

SctpMultiChannel

the association failed to setup.

A send failed notification indicates that a message cannot be delivered.
Typically this is because the association has been shutdown with unsent data
in the socket output buffer, or in the case of a

SctpMultiChannel

the association failed to setup.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SendFailedNotification

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

Returns the address.

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

ByteBuffer

buffer

()

Returns the data that was to be sent.

abstract int

errorCode

()

Returns the error code.

abstract int

streamNumber

()

Returns the stream number that the messge was to be sent on.

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

SendFailedNotification

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

Returns the address.

abstract

Association

association

()

Returns the association that this notification is applicable to.

abstract

ByteBuffer

buffer

()

Returns the data that was to be sent.

abstract int

errorCode

()

Returns the error code.

abstract int

streamNumber

()

Returns the stream number that the messge was to be sent on.

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

Returns the address.

Returns the association that this notification is applicable to.

Returns the data that was to be sent.

Returns the error code.

Returns the stream number that the messge was to be sent on.

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

- SendFailedNotification

```java
protected SendFailedNotification()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

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
**Returns:** The association that failed to send, or

null

if
there is no association, that is, the notification follows a

AssociationChangeNotification.AssocChangeEvent.CANT_START

- address

```java
public abstract
SocketAddress
address()
```

Returns the address.

**Returns:** The peer primary address of the association or the address that
the message was sent to

- buffer

```java
public abstract
ByteBuffer
buffer()
```

Returns the data that was to be sent.

**Returns:** The user data. The buffers position will be

0

and its
limit will be set to the end of the data.

- errorCode

```java
public abstract int errorCode()
```

Returns the error code.

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

**Returns:** The error code

- streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the messge was to be sent on.

**Returns:** The stream number

Constructor Detail

- SendFailedNotification

```java
protected SendFailedNotification()
```

Initializes a new instance of this class.

---

#### Constructor Detail

SendFailedNotification

```java
protected SendFailedNotification()
```

Initializes a new instance of this class.

---

#### SendFailedNotification

protected SendFailedNotification()

Initializes a new instance of this class.

Method Detail

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
**Returns:** The association that failed to send, or

null

if
there is no association, that is, the notification follows a

AssociationChangeNotification.AssocChangeEvent.CANT_START

- address

```java
public abstract
SocketAddress
address()
```

Returns the address.

**Returns:** The peer primary address of the association or the address that
the message was sent to

- buffer

```java
public abstract
ByteBuffer
buffer()
```

Returns the data that was to be sent.

**Returns:** The user data. The buffers position will be

0

and its
limit will be set to the end of the data.

- errorCode

```java
public abstract int errorCode()
```

Returns the error code.

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

**Returns:** The error code

- streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the messge was to be sent on.

**Returns:** The stream number

---

#### Method Detail

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
**Returns:** The association that failed to send, or

null

if
there is no association, that is, the notification follows a

AssociationChangeNotification.AssocChangeEvent.CANT_START

---

#### association

public abstract

Association

association()

Returns the association that this notification is applicable to.

address

```java
public abstract
SocketAddress
address()
```

Returns the address.

**Returns:** The peer primary address of the association or the address that
the message was sent to

---

#### address

public abstract

SocketAddress

address()

Returns the address.

buffer

```java
public abstract
ByteBuffer
buffer()
```

Returns the data that was to be sent.

**Returns:** The user data. The buffers position will be

0

and its
limit will be set to the end of the data.

---

#### buffer

public abstract

ByteBuffer

buffer()

Returns the data that was to be sent.

errorCode

```java
public abstract int errorCode()
```

Returns the error code.

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

**Returns:** The error code

---

#### errorCode

public abstract int errorCode()

Returns the error code.

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

The errorCode gives the reason why the send failed, and if set, will
be a SCTP protocol error code as defined in RFC2960 section 3.3.10

streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the messge was to be sent on.

**Returns:** The stream number

---

#### streamNumber

public abstract int streamNumber()

Returns the stream number that the messge was to be sent on.

---

