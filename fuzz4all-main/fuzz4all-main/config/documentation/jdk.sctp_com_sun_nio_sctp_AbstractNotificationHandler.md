# Class AbstractNotificationHandler<T>

**Source:** `jdk.sctp\com\sun\nio\sctp\AbstractNotificationHandler.html`

### Class Description

```java
public class
AbstractNotificationHandler<T>

extends
Object

implements
NotificationHandler
<T>
```

A skeletal handler that consumes notifications and continues.

This class trivially implements the

handleNotification

methods to
return

CONTINUE

so that all notifications are
consumed and the channel continues to try and receive a message.

It also provides overloaded versions of the

handleNotification

methods, one for each of the required supported notification types,

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

, and

ShutdownNotification

. The
appropriate method will be invoked when the notification is received.

**All Implemented Interfaces:** NotificationHandler

<T>

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractNotificationHandler()

Initializes a new instance of this class.

---

### Method Details

#### public
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)

Invoked when an implementation specific notification is received from the
SCTP stack.

**Specified by:**
- handleNotification

in interface

NotificationHandler

<

T

>

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the

receive

operation when it was
initiated.

**Returns:**
- The handler result

---

#### public
HandlerResult
handleNotification​(
AssociationChangeNotification
notification,

T
attachment)

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the

receive

operation when it was
initiated.

**Returns:**
- The handler result

---

#### public
HandlerResult
handleNotification​(
PeerAddressChangeNotification
notification,

T
attachment)

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the

receive

operation when it was
initiated.

**Returns:**
- The handler result

---

#### public
HandlerResult
handleNotification​(
SendFailedNotification
notification,

T
attachment)

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the

receive

operation when it was
initiated.

**Returns:**
- The handler result

---

#### public
HandlerResult
handleNotification​(
ShutdownNotification
notification,

T
attachment)

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

**Parameters:**
- notification

- The notification
- attachment

- The object attached to the

receive

operation when it was
initiated.

**Returns:**
- The handler result

---

### Additional Sections

#### Class AbstractNotificationHandler<T>

java.lang.Object

- com.sun.nio.sctp.AbstractNotificationHandler<T>

com.sun.nio.sctp.AbstractNotificationHandler<T>

**All Implemented Interfaces:** NotificationHandler

<T>

```java
public class
AbstractNotificationHandler<T>

extends
Object

implements
NotificationHandler
<T>
```

A skeletal handler that consumes notifications and continues.

This class trivially implements the

handleNotification

methods to
return

CONTINUE

so that all notifications are
consumed and the channel continues to try and receive a message.

It also provides overloaded versions of the

handleNotification

methods, one for each of the required supported notification types,

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

, and

ShutdownNotification

. The
appropriate method will be invoked when the notification is received.

**Since:** 1.7

public class

AbstractNotificationHandler<T>

extends

Object

implements

NotificationHandler

<T>

A skeletal handler that consumes notifications and continues.

This class trivially implements the

handleNotification

methods to
return

CONTINUE

so that all notifications are
consumed and the channel continues to try and receive a message.

It also provides overloaded versions of the

handleNotification

methods, one for each of the required supported notification types,

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

, and

ShutdownNotification

. The
appropriate method will be invoked when the notification is received.

This class trivially implements the

handleNotification

methods to
return

CONTINUE

so that all notifications are
consumed and the channel continues to try and receive a message.

It also provides overloaded versions of the

handleNotification

methods, one for each of the required supported notification types,

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

, and

ShutdownNotification

. The
appropriate method will be invoked when the notification is received.

It also provides overloaded versions of the

handleNotification

methods, one for each of the required supported notification types,

AssociationChangeNotification

,

PeerAddressChangeNotification

,

SendFailedNotification

, and

ShutdownNotification

. The
appropriate method will be invoked when the notification is received.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractNotificationHandler

()

Initializes a new instance of this class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HandlerResult

handleNotification

​(

AssociationChangeNotification

notification,

T

attachment)

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

Notification

notification,

T

attachment)

Invoked when an implementation specific notification is received from the
SCTP stack.

HandlerResult

handleNotification

​(

PeerAddressChangeNotification

notification,

T

attachment)

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

SendFailedNotification

notification,

T

attachment)

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

ShutdownNotification

notification,

T

attachment)

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

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

AbstractNotificationHandler

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

HandlerResult

handleNotification

​(

AssociationChangeNotification

notification,

T

attachment)

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

Notification

notification,

T

attachment)

Invoked when an implementation specific notification is received from the
SCTP stack.

HandlerResult

handleNotification

​(

PeerAddressChangeNotification

notification,

T

attachment)

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

SendFailedNotification

notification,

T

attachment)

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

HandlerResult

handleNotification

​(

ShutdownNotification

notification,

T

attachment)

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

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

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

Invoked when an implementation specific notification is received from the
SCTP stack.

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

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

- AbstractNotificationHandler

```java
protected AbstractNotificationHandler()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- handleNotification

```java
public
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when an implementation specific notification is received from the
SCTP stack.

**Specified by:** handleNotification

in interface

NotificationHandler

<

T

>
**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
AssociationChangeNotification
notification,

T
attachment)
```

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
PeerAddressChangeNotification
notification,

T
attachment)
```

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
SendFailedNotification
notification,

T
attachment)
```

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
ShutdownNotification
notification,

T
attachment)
```

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

Constructor Detail

- AbstractNotificationHandler

```java
protected AbstractNotificationHandler()
```

Initializes a new instance of this class.

---

#### Constructor Detail

AbstractNotificationHandler

```java
protected AbstractNotificationHandler()
```

Initializes a new instance of this class.

---

#### AbstractNotificationHandler

protected AbstractNotificationHandler()

Initializes a new instance of this class.

Method Detail

- handleNotification

```java
public
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when an implementation specific notification is received from the
SCTP stack.

**Specified by:** handleNotification

in interface

NotificationHandler

<

T

>
**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
AssociationChangeNotification
notification,

T
attachment)
```

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
PeerAddressChangeNotification
notification,

T
attachment)
```

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
SendFailedNotification
notification,

T
attachment)
```

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

- handleNotification

```java
public
HandlerResult
handleNotification​(
ShutdownNotification
notification,

T
attachment)
```

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### Method Detail

handleNotification

```java
public
HandlerResult
handleNotification​(
Notification
notification,

T
attachment)
```

Invoked when an implementation specific notification is received from the
SCTP stack.

**Specified by:** handleNotification

in interface

NotificationHandler

<

T

>
**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### handleNotification

public

HandlerResult

handleNotification​(

Notification

notification,

T

attachment)

Invoked when an implementation specific notification is received from the
SCTP stack.

handleNotification

```java
public
HandlerResult
handleNotification​(
AssociationChangeNotification
notification,

T
attachment)
```

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### handleNotification

public

HandlerResult

handleNotification​(

AssociationChangeNotification

notification,

T

attachment)

Invoked when an

AssociationChangeNotification

is received from
the SCTP stack.

handleNotification

```java
public
HandlerResult
handleNotification​(
PeerAddressChangeNotification
notification,

T
attachment)
```

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### handleNotification

public

HandlerResult

handleNotification​(

PeerAddressChangeNotification

notification,

T

attachment)

Invoked when an

PeerAddressChangeNotification

is received from
the SCTP stack.

handleNotification

```java
public
HandlerResult
handleNotification​(
SendFailedNotification
notification,

T
attachment)
```

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### handleNotification

public

HandlerResult

handleNotification​(

SendFailedNotification

notification,

T

attachment)

Invoked when an

SendFailedNotification

is received from
the SCTP stack.

handleNotification

```java
public
HandlerResult
handleNotification​(
ShutdownNotification
notification,

T
attachment)
```

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

**Parameters:** notification

- The notification
**Parameters:** attachment

- The object attached to the

receive

operation when it was
initiated.
**Returns:** The handler result

---

#### handleNotification

public

HandlerResult

handleNotification​(

ShutdownNotification

notification,

T

attachment)

Invoked when an

ShutdownNotification

is received from
the SCTP stack.

---

