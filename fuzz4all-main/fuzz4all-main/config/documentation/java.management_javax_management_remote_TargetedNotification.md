# Class TargetedNotification

**Source:** `java.management\javax\management\remote\TargetedNotification.html`

### Class Description

```java
public class
TargetedNotification

extends
Object

implements
Serializable
```

A (Notification, Listener ID) pair.

This class is used to associate an emitted notification
with the listener ID to which it is targeted.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TargetedNotification​(
Notification
notification,

Integer
listenerID)

Constructs a

TargetedNotification

object. The
object contains a pair (Notification, Listener ID).
The Listener ID identifies the client listener to which that
notification is targeted. The client listener ID is one
previously returned by the connector server in response to an

addNotificationListener

request.

**Parameters:**
- notification

- Notification emitted from the MBean server.
- listenerID

- The ID of the listener to which this
notification is targeted.

**Throws:**
- IllegalArgumentException

- if the

listenerID

or

notification

is null.

---

### Method Details

#### public
Notification
getNotification()

The emitted notification.

**Returns:**
- The notification.

---

#### public
Integer
getListenerID()

The ID of the listener to which the notification is
targeted.

**Returns:**
- The listener ID.

---

#### public
String
toString()

Returns a textual representation of this Targeted Notification.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this Targeted Notification.

---

### Additional Sections

#### Class TargetedNotification

java.lang.Object

- javax.management.remote.TargetedNotification

javax.management.remote.TargetedNotification

**All Implemented Interfaces:** Serializable

```java
public class
TargetedNotification

extends
Object

implements
Serializable
```

A (Notification, Listener ID) pair.

This class is used to associate an emitted notification
with the listener ID to which it is targeted.

**Since:** 1.5
**See Also:** Serialized Form

public class

TargetedNotification

extends

Object

implements

Serializable

A (Notification, Listener ID) pair.

This class is used to associate an emitted notification
with the listener ID to which it is targeted.

A (Notification, Listener ID) pair.

This class is used to associate an emitted notification
with the listener ID to which it is targeted.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TargetedNotification

​(

Notification

notification,

Integer

listenerID)

Constructs a

TargetedNotification

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

getListenerID

()

The ID of the listener to which the notification is
targeted.

Notification

getNotification

()

The emitted notification.

String

toString

()

Returns a textual representation of this Targeted Notification.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

TargetedNotification

​(

Notification

notification,

Integer

listenerID)

Constructs a

TargetedNotification

object.

---

#### Constructor Summary

Constructs a

TargetedNotification

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

getListenerID

()

The ID of the listener to which the notification is
targeted.

Notification

getNotification

()

The emitted notification.

String

toString

()

Returns a textual representation of this Targeted Notification.

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

wait

,

wait

,

wait

---

#### Method Summary

The ID of the listener to which the notification is
targeted.

The emitted notification.

Returns a textual representation of this Targeted Notification.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TargetedNotification

```java
public TargetedNotification​(
Notification
notification,

Integer
listenerID)
```

Constructs a

TargetedNotification

object. The
object contains a pair (Notification, Listener ID).
The Listener ID identifies the client listener to which that
notification is targeted. The client listener ID is one
previously returned by the connector server in response to an

addNotificationListener

request.

**Parameters:** notification

- Notification emitted from the MBean server.
**Parameters:** listenerID

- The ID of the listener to which this
notification is targeted.
**Throws:** IllegalArgumentException

- if the

listenerID

or

notification

is null.

============ METHOD DETAIL ==========

- Method Detail

- getNotification

```java
public
Notification
getNotification()
```

The emitted notification.

**Returns:** The notification.

- getListenerID

```java
public
Integer
getListenerID()
```

The ID of the listener to which the notification is
targeted.

**Returns:** The listener ID.

- toString

```java
public
String
toString()
```

Returns a textual representation of this Targeted Notification.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this Targeted Notification.

Constructor Detail

- TargetedNotification

```java
public TargetedNotification​(
Notification
notification,

Integer
listenerID)
```

Constructs a

TargetedNotification

object. The
object contains a pair (Notification, Listener ID).
The Listener ID identifies the client listener to which that
notification is targeted. The client listener ID is one
previously returned by the connector server in response to an

addNotificationListener

request.

**Parameters:** notification

- Notification emitted from the MBean server.
**Parameters:** listenerID

- The ID of the listener to which this
notification is targeted.
**Throws:** IllegalArgumentException

- if the

listenerID

or

notification

is null.

---

#### Constructor Detail

TargetedNotification

```java
public TargetedNotification​(
Notification
notification,

Integer
listenerID)
```

Constructs a

TargetedNotification

object. The
object contains a pair (Notification, Listener ID).
The Listener ID identifies the client listener to which that
notification is targeted. The client listener ID is one
previously returned by the connector server in response to an

addNotificationListener

request.

**Parameters:** notification

- Notification emitted from the MBean server.
**Parameters:** listenerID

- The ID of the listener to which this
notification is targeted.
**Throws:** IllegalArgumentException

- if the

listenerID

or

notification

is null.

---

#### TargetedNotification

public TargetedNotification​(

Notification

notification,

Integer

listenerID)

Constructs a

TargetedNotification

object. The
object contains a pair (Notification, Listener ID).
The Listener ID identifies the client listener to which that
notification is targeted. The client listener ID is one
previously returned by the connector server in response to an

addNotificationListener

request.

Method Detail

- getNotification

```java
public
Notification
getNotification()
```

The emitted notification.

**Returns:** The notification.

- getListenerID

```java
public
Integer
getListenerID()
```

The ID of the listener to which the notification is
targeted.

**Returns:** The listener ID.

- toString

```java
public
String
toString()
```

Returns a textual representation of this Targeted Notification.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this Targeted Notification.

---

#### Method Detail

getNotification

```java
public
Notification
getNotification()
```

The emitted notification.

**Returns:** The notification.

---

#### getNotification

public

Notification

getNotification()

The emitted notification.

getListenerID

```java
public
Integer
getListenerID()
```

The ID of the listener to which the notification is
targeted.

**Returns:** The listener ID.

---

#### getListenerID

public

Integer

getListenerID()

The ID of the listener to which the notification is
targeted.

toString

```java
public
String
toString()
```

Returns a textual representation of this Targeted Notification.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this Targeted Notification.

---

#### toString

public

String

toString()

Returns a textual representation of this Targeted Notification.

---

