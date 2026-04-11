# Class TimerNotification

**Source:** `java.management\javax\management\timer\TimerNotification.html`

### Class Description

```java
public class
TimerNotification

extends
Notification
```

This class provides definitions of the notifications sent by timer MBeans.

It defines a timer notification identifier which allows to retrieve a timer notification
from the list of notifications of a timer MBean.

The timer notifications are created and handled by the timer MBean.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TimerNotification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

Integer
id)

Creates a timer notification object.

**Parameters:**
- type

- The notification type.
- source

- The notification producer.
- sequenceNumber

- The notification sequence number within the source object.
- timeStamp

- The notification emission date.
- msg

- The notification message.
- id

- The notification identifier.

---

### Method Details

#### public
Integer
getNotificationID()

Gets the identifier of this timer notification.

**Returns:**
- The identifier.

---

### Additional Sections

#### Class TimerNotification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification
- - javax.management.timer.TimerNotification

java.util.EventObject

- javax.management.Notification
- - javax.management.timer.TimerNotification

javax.management.Notification

- javax.management.timer.TimerNotification

javax.management.timer.TimerNotification

**All Implemented Interfaces:** Serializable

```java
public class
TimerNotification

extends
Notification
```

This class provides definitions of the notifications sent by timer MBeans.

It defines a timer notification identifier which allows to retrieve a timer notification
from the list of notifications of a timer MBean.

The timer notifications are created and handled by the timer MBean.

**Since:** 1.5
**See Also:** Serialized Form

public class

TimerNotification

extends

Notification

This class provides definitions of the notifications sent by timer MBeans.

It defines a timer notification identifier which allows to retrieve a timer notification
from the list of notifications of a timer MBean.

The timer notifications are created and handled by the timer MBean.

The timer notifications are created and handled by the timer MBean.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.

Notification

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TimerNotification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

Integer

id)

Creates a timer notification object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

getNotificationID

()

Gets the identifier of this timer notification.

- Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

- Fields declared in class javax.management.

Notification

source

---

#### Field Summary

Fields declared in class javax.management.

Notification

source

---

#### Fields declared in class javax.management. Notification

Constructor Summary

Constructors

Constructor

Description

TimerNotification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

Integer

id)

Creates a timer notification object.

---

#### Constructor Summary

Creates a timer notification object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

getNotificationID

()

Gets the identifier of this timer notification.

- Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

- Methods declared in class java.util.

EventObject

getSource

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

Gets the identifier of this timer notification.

Methods declared in class javax.management.

Notification

getMessage

,

getSequenceNumber

,

getTimeStamp

,

getType

,

getUserData

,

setSequenceNumber

,

setSource

,

setTimeStamp

,

setUserData

,

toString

---

#### Methods declared in class javax.management. Notification

Methods declared in class java.util.

EventObject

getSource

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

- TimerNotification

```java
public TimerNotification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

Integer
id)
```

Creates a timer notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification producer.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** msg

- The notification message.
**Parameters:** id

- The notification identifier.

============ METHOD DETAIL ==========

- Method Detail

- getNotificationID

```java
public
Integer
getNotificationID()
```

Gets the identifier of this timer notification.

**Returns:** The identifier.

Constructor Detail

- TimerNotification

```java
public TimerNotification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

Integer
id)
```

Creates a timer notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification producer.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** msg

- The notification message.
**Parameters:** id

- The notification identifier.

---

#### Constructor Detail

TimerNotification

```java
public TimerNotification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

Integer
id)
```

Creates a timer notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification producer.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** msg

- The notification message.
**Parameters:** id

- The notification identifier.

---

#### TimerNotification

public TimerNotification​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

Integer

id)

Creates a timer notification object.

Method Detail

- getNotificationID

```java
public
Integer
getNotificationID()
```

Gets the identifier of this timer notification.

**Returns:** The identifier.

---

#### Method Detail

getNotificationID

```java
public
Integer
getNotificationID()
```

Gets the identifier of this timer notification.

**Returns:** The identifier.

---

#### getNotificationID

public

Integer

getNotificationID()

Gets the identifier of this timer notification.

---

