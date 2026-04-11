# Class UnsolicitedNotificationEvent

**Source:** `java.naming\javax\naming\ldap\UnsolicitedNotificationEvent.html`

### Class Description

```java
public class
UnsolicitedNotificationEvent

extends
EventObject
```

This class represents an event fired in response to an unsolicited
notification sent by the LDAP server.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnsolicitedNotificationEvent​(
Object
src,

UnsolicitedNotification
notice)

Constructs a new instance of

UnsolicitedNotificationEvent

.

**Parameters:**
- src

- The non-null source that fired the event.
- notice

- The non-null unsolicited notification.

---

### Method Details

#### public
UnsolicitedNotification
getNotification()

Returns the unsolicited notification.

**Returns:**
- The non-null unsolicited notification that caused this
event to be fired.

---

#### public void dispatch​(
UnsolicitedNotificationListener
listener)

Invokes the

notificationReceived()

method on
a listener using this event.

**Parameters:**
- listener

- The non-null listener on which to invoke

notificationReceived

.

---

### Additional Sections

#### Class UnsolicitedNotificationEvent

java.lang.Object

- java.util.EventObject
- - javax.naming.ldap.UnsolicitedNotificationEvent

java.util.EventObject

- javax.naming.ldap.UnsolicitedNotificationEvent

javax.naming.ldap.UnsolicitedNotificationEvent

**All Implemented Interfaces:** Serializable

```java
public class
UnsolicitedNotificationEvent

extends
EventObject
```

This class represents an event fired in response to an unsolicited
notification sent by the LDAP server.

**Since:** 1.3
**See Also:** UnsolicitedNotification

,

UnsolicitedNotificationListener

,

EventContext.addNamingListener(javax.naming.Name, int, javax.naming.event.NamingListener)

,

EventDirContext.addNamingListener(javax.naming.Name, java.lang.String, javax.naming.directory.SearchControls, javax.naming.event.NamingListener)

,

EventContext.removeNamingListener(javax.naming.event.NamingListener)

,

Serialized Form

public class

UnsolicitedNotificationEvent

extends

EventObject

This class represents an event fired in response to an unsolicited
notification sent by the LDAP server.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnsolicitedNotificationEvent

​(

Object

src,

UnsolicitedNotification

notice)

Constructs a new instance of

UnsolicitedNotificationEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

UnsolicitedNotificationListener

listener)

Invokes the

notificationReceived()

method on
a listener using this event.

UnsolicitedNotification

getNotification

()

Returns the unsolicited notification.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

UnsolicitedNotificationEvent

​(

Object

src,

UnsolicitedNotification

notice)

Constructs a new instance of

UnsolicitedNotificationEvent

.

---

#### Constructor Summary

Constructs a new instance of

UnsolicitedNotificationEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

dispatch

​(

UnsolicitedNotificationListener

listener)

Invokes the

notificationReceived()

method on
a listener using this event.

UnsolicitedNotification

getNotification

()

Returns the unsolicited notification.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Invokes the

notificationReceived()

method on
a listener using this event.

Returns the unsolicited notification.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

- UnsolicitedNotificationEvent

```java
public UnsolicitedNotificationEvent​(
Object
src,

UnsolicitedNotification
notice)
```

Constructs a new instance of

UnsolicitedNotificationEvent

.

**Parameters:** src

- The non-null source that fired the event.
**Parameters:** notice

- The non-null unsolicited notification.

============ METHOD DETAIL ==========

- Method Detail

- getNotification

```java
public
UnsolicitedNotification
getNotification()
```

Returns the unsolicited notification.

**Returns:** The non-null unsolicited notification that caused this
event to be fired.

- dispatch

```java
public void dispatch​(
UnsolicitedNotificationListener
listener)
```

Invokes the

notificationReceived()

method on
a listener using this event.

**Parameters:** listener

- The non-null listener on which to invoke

notificationReceived

.

Constructor Detail

- UnsolicitedNotificationEvent

```java
public UnsolicitedNotificationEvent​(
Object
src,

UnsolicitedNotification
notice)
```

Constructs a new instance of

UnsolicitedNotificationEvent

.

**Parameters:** src

- The non-null source that fired the event.
**Parameters:** notice

- The non-null unsolicited notification.

---

#### Constructor Detail

UnsolicitedNotificationEvent

```java
public UnsolicitedNotificationEvent​(
Object
src,

UnsolicitedNotification
notice)
```

Constructs a new instance of

UnsolicitedNotificationEvent

.

**Parameters:** src

- The non-null source that fired the event.
**Parameters:** notice

- The non-null unsolicited notification.

---

#### UnsolicitedNotificationEvent

public UnsolicitedNotificationEvent​(

Object

src,

UnsolicitedNotification

notice)

Constructs a new instance of

UnsolicitedNotificationEvent

.

Method Detail

- getNotification

```java
public
UnsolicitedNotification
getNotification()
```

Returns the unsolicited notification.

**Returns:** The non-null unsolicited notification that caused this
event to be fired.

- dispatch

```java
public void dispatch​(
UnsolicitedNotificationListener
listener)
```

Invokes the

notificationReceived()

method on
a listener using this event.

**Parameters:** listener

- The non-null listener on which to invoke

notificationReceived

.

---

#### Method Detail

getNotification

```java
public
UnsolicitedNotification
getNotification()
```

Returns the unsolicited notification.

**Returns:** The non-null unsolicited notification that caused this
event to be fired.

---

#### getNotification

public

UnsolicitedNotification

getNotification()

Returns the unsolicited notification.

dispatch

```java
public void dispatch​(
UnsolicitedNotificationListener
listener)
```

Invokes the

notificationReceived()

method on
a listener using this event.

**Parameters:** listener

- The non-null listener on which to invoke

notificationReceived

.

---

#### dispatch

public void dispatch​(

UnsolicitedNotificationListener

listener)

Invokes the

notificationReceived()

method on
a listener using this event.

---

