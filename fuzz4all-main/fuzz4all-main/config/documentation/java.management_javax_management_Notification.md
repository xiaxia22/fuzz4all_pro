# Class Notification

**Source:** `java.management\javax\management\Notification.html`

### Class Description

```java
public class
Notification

extends
EventObject
```

The Notification class represents a notification emitted by an
MBean. It contains a reference to the source MBean: if the
notification has been forwarded through the MBean server, and the
original source of the notification was a reference to the emitting
MBean object, then the MBean server replaces it by the MBean's
ObjectName. If the listener has registered directly with the
MBean, this is either the object name or a direct reference to the
MBean.

It is strongly recommended that notification senders use the
object name rather than a reference to the MBean object as the
source.

The

serialVersionUID

of this class is

-7516092053498031989L

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
Object
source

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

---

### Constructor Details

#### public Notification​(
String
type,

Object
source,
long sequenceNumber)

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:**
- type

- The notification type.
- source

- The notification source.
- sequenceNumber

- The notification sequence number within the source object.

---

#### public Notification​(
String
type,

Object
source,
long sequenceNumber,

String
message)

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:**
- type

- The notification type.
- source

- The notification source.
- sequenceNumber

- The notification sequence number within the source object.
- message

- The detailed message.

---

#### public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp)

Creates a Notification object.

**Parameters:**
- type

- The notification type.
- source

- The notification source.
- sequenceNumber

- The notification sequence number within the source object.
- timeStamp

- The notification emission date.

---

#### public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
message)

Creates a Notification object.

**Parameters:**
- type

- The notification type.
- source

- The notification source.
- sequenceNumber

- The notification sequence number within the source object.
- timeStamp

- The notification emission date.
- message

- The detailed message.

---

### Method Details

#### public void setSource​(
Object
source)

Sets the source.

**Parameters:**
- source

- the new source for this object.

**See Also:**
- EventObject.getSource()

---

#### public long getSequenceNumber()

Get the notification sequence number.

**Returns:**
- The notification sequence number within the source object. It's a serial number
identifying a particular instance of notification in the context of the notification source.
The notification model does not assume that notifications will be received in the same order
that they are sent. The sequence number helps listeners to sort received notifications.

**See Also:**
- setSequenceNumber(long)

---

#### public void setSequenceNumber​(long sequenceNumber)

Set the notification sequence number.

**Parameters:**
- sequenceNumber

- The notification sequence number within the source object. It is
a serial number identifying a particular instance of notification in the
context of the notification source.

**See Also:**
- getSequenceNumber()

---

#### public
String
getType()

Get the notification type.

**Returns:**
- The notification type. It's a string expressed in a dot notation
similar to Java properties. It is recommended that the notification type
should follow the reverse-domain-name convention used by Java package
names. An example of a notification type is com.example.alarm.router.

---

#### public long getTimeStamp()

Get the notification timestamp.

**Returns:**
- The notification timestamp.

**See Also:**
- setTimeStamp(long)

---

#### public void setTimeStamp​(long timeStamp)

Set the notification timestamp.

**Parameters:**
- timeStamp

- The notification timestamp. It indicates when the notification was generated.

**See Also:**
- getTimeStamp()

---

#### public
String
getMessage()

Get the notification message.

**Returns:**
- The message string of this notification object.

---

#### public
Object
getUserData()

Get the user data.

**Returns:**
- The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.

**See Also:**
- setUserData(java.lang.Object)

---

#### public void setUserData​(
Object
userData)

Set the user data.

**Parameters:**
- userData

- The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.

**See Also:**
- getUserData()

---

#### public
String
toString()

Returns a String representation of this notification.

**Overrides:**
- toString

in class

EventObject

**Returns:**
- A String representation of this notification.

---

### Additional Sections

#### Class Notification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification

java.util.EventObject

- javax.management.Notification

javax.management.Notification

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AttributeChangeNotification

,

JMXConnectionNotification

,

MBeanServerNotification

,

MonitorNotification

,

RelationNotification

,

TimerNotification

```java
public class
Notification

extends
EventObject
```

The Notification class represents a notification emitted by an
MBean. It contains a reference to the source MBean: if the
notification has been forwarded through the MBean server, and the
original source of the notification was a reference to the emitting
MBean object, then the MBean server replaces it by the MBean's
ObjectName. If the listener has registered directly with the
MBean, this is either the object name or a direct reference to the
MBean.

It is strongly recommended that notification senders use the
object name rather than a reference to the MBean object as the
source.

The

serialVersionUID

of this class is

-7516092053498031989L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

Notification

extends

EventObject

The Notification class represents a notification emitted by an
MBean. It contains a reference to the source MBean: if the
notification has been forwarded through the MBean server, and the
original source of the notification was a reference to the emitting
MBean object, then the MBean server replaces it by the MBean's
ObjectName. If the listener has registered directly with the
MBean, this is either the object name or a direct reference to the
MBean.

It is strongly recommended that notification senders use the
object name rather than a reference to the MBean object as the
source.

The

serialVersionUID

of this class is

-7516092053498031989L

.

The Notification class represents a notification emitted by an
MBean. It contains a reference to the source MBean: if the
notification has been forwarded through the MBean server, and the
original source of the notification was a reference to the emitting
MBean object, then the MBean server replaces it by the MBean's
ObjectName. If the listener has registered directly with the
MBean, this is either the object name or a direct reference to the
MBean.

It is strongly recommended that notification senders use the
object name rather than a reference to the MBean object as the
source.

The

serialVersionUID

of this class is

-7516092053498031989L

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

source

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Notification

​(

String

type,

Object

source,
long sequenceNumber)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

message)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,

String

message)

Creates a Notification object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Get the notification message.

long

getSequenceNumber

()

Get the notification sequence number.

long

getTimeStamp

()

Get the notification timestamp.

String

getType

()

Get the notification type.

Object

getUserData

()

Get the user data.

void

setSequenceNumber

​(long sequenceNumber)

Set the notification sequence number.

void

setSource

​(

Object

source)

Sets the source.

void

setTimeStamp

​(long timeStamp)

Set the notification timestamp.

void

setUserData

​(

Object

userData)

Set the user data.

String

toString

()

Returns a String representation of this notification.

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

Fields

Modifier and Type

Field

Description

protected

Object

source

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

---

#### Field Summary

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

Constructor Summary

Constructors

Constructor

Description

Notification

​(

String

type,

Object

source,
long sequenceNumber)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

message)

Creates a Notification object.

Notification

​(

String

type,

Object

source,
long sequenceNumber,

String

message)

Creates a Notification object.

---

#### Constructor Summary

Creates a Notification object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getMessage

()

Get the notification message.

long

getSequenceNumber

()

Get the notification sequence number.

long

getTimeStamp

()

Get the notification timestamp.

String

getType

()

Get the notification type.

Object

getUserData

()

Get the user data.

void

setSequenceNumber

​(long sequenceNumber)

Set the notification sequence number.

void

setSource

​(

Object

source)

Sets the source.

void

setTimeStamp

​(long timeStamp)

Set the notification timestamp.

void

setUserData

​(

Object

userData)

Set the user data.

String

toString

()

Returns a String representation of this notification.

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

Get the notification message.

Get the notification sequence number.

Get the notification timestamp.

Get the notification type.

Get the user data.

Set the notification sequence number.

Sets the source.

Set the notification timestamp.

Set the user data.

Returns a String representation of this notification.

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

============ FIELD DETAIL ===========

- Field Detail

- source

```java
protected
Object
source
```

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,

String
message)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** message

- The detailed message.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
message)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** message

- The detailed message.

============ METHOD DETAIL ==========

- Method Detail

- setSource

```java
public void setSource​(
Object
source)
```

Sets the source.

**Parameters:** source

- the new source for this object.
**See Also:** EventObject.getSource()

- getSequenceNumber

```java
public long getSequenceNumber()
```

Get the notification sequence number.

**Returns:** The notification sequence number within the source object. It's a serial number
identifying a particular instance of notification in the context of the notification source.
The notification model does not assume that notifications will be received in the same order
that they are sent. The sequence number helps listeners to sort received notifications.
**See Also:** setSequenceNumber(long)

- setSequenceNumber

```java
public void setSequenceNumber​(long sequenceNumber)
```

Set the notification sequence number.

**Parameters:** sequenceNumber

- The notification sequence number within the source object. It is
a serial number identifying a particular instance of notification in the
context of the notification source.
**See Also:** getSequenceNumber()

- getType

```java
public
String
getType()
```

Get the notification type.

**Returns:** The notification type. It's a string expressed in a dot notation
similar to Java properties. It is recommended that the notification type
should follow the reverse-domain-name convention used by Java package
names. An example of a notification type is com.example.alarm.router.

- getTimeStamp

```java
public long getTimeStamp()
```

Get the notification timestamp.

**Returns:** The notification timestamp.
**See Also:** setTimeStamp(long)

- setTimeStamp

```java
public void setTimeStamp​(long timeStamp)
```

Set the notification timestamp.

**Parameters:** timeStamp

- The notification timestamp. It indicates when the notification was generated.
**See Also:** getTimeStamp()

- getMessage

```java
public
String
getMessage()
```

Get the notification message.

**Returns:** The message string of this notification object.

- getUserData

```java
public
Object
getUserData()
```

Get the user data.

**Returns:** The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** setUserData(java.lang.Object)

- setUserData

```java
public void setUserData​(
Object
userData)
```

Set the user data.

**Parameters:** userData

- The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** getUserData()

- toString

```java
public
String
toString()
```

Returns a String representation of this notification.

**Overrides:** toString

in class

EventObject
**Returns:** A String representation of this notification.

Field Detail

- source

```java
protected
Object
source
```

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

---

#### Field Detail

source

```java
protected
Object
source
```

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

---

#### source

protected

Object

source

This field hides the

EventObject.source

field in the
parent class to make it non-transient and therefore part of the
serialized form.

Constructor Detail

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,

String
message)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** message

- The detailed message.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.

- Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
message)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** message

- The detailed message.

---

#### Constructor Detail

Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.

---

#### Notification

public Notification​(

String

type,

Object

source,
long sequenceNumber)

Creates a Notification object.
The notification timeStamp is set to the current date.

Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,

String
message)
```

Creates a Notification object.
The notification timeStamp is set to the current date.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** message

- The detailed message.

---

#### Notification

public Notification​(

String

type,

Object

source,
long sequenceNumber,

String

message)

Creates a Notification object.
The notification timeStamp is set to the current date.

Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.

---

#### Notification

public Notification​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp)

Creates a Notification object.

Notification

```java
public Notification​(
String
type,

Object
source,
long sequenceNumber,
long timeStamp,

String
message)
```

Creates a Notification object.

**Parameters:** type

- The notification type.
**Parameters:** source

- The notification source.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The notification emission date.
**Parameters:** message

- The detailed message.

---

#### Notification

public Notification​(

String

type,

Object

source,
long sequenceNumber,
long timeStamp,

String

message)

Creates a Notification object.

Method Detail

- setSource

```java
public void setSource​(
Object
source)
```

Sets the source.

**Parameters:** source

- the new source for this object.
**See Also:** EventObject.getSource()

- getSequenceNumber

```java
public long getSequenceNumber()
```

Get the notification sequence number.

**Returns:** The notification sequence number within the source object. It's a serial number
identifying a particular instance of notification in the context of the notification source.
The notification model does not assume that notifications will be received in the same order
that they are sent. The sequence number helps listeners to sort received notifications.
**See Also:** setSequenceNumber(long)

- setSequenceNumber

```java
public void setSequenceNumber​(long sequenceNumber)
```

Set the notification sequence number.

**Parameters:** sequenceNumber

- The notification sequence number within the source object. It is
a serial number identifying a particular instance of notification in the
context of the notification source.
**See Also:** getSequenceNumber()

- getType

```java
public
String
getType()
```

Get the notification type.

**Returns:** The notification type. It's a string expressed in a dot notation
similar to Java properties. It is recommended that the notification type
should follow the reverse-domain-name convention used by Java package
names. An example of a notification type is com.example.alarm.router.

- getTimeStamp

```java
public long getTimeStamp()
```

Get the notification timestamp.

**Returns:** The notification timestamp.
**See Also:** setTimeStamp(long)

- setTimeStamp

```java
public void setTimeStamp​(long timeStamp)
```

Set the notification timestamp.

**Parameters:** timeStamp

- The notification timestamp. It indicates when the notification was generated.
**See Also:** getTimeStamp()

- getMessage

```java
public
String
getMessage()
```

Get the notification message.

**Returns:** The message string of this notification object.

- getUserData

```java
public
Object
getUserData()
```

Get the user data.

**Returns:** The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** setUserData(java.lang.Object)

- setUserData

```java
public void setUserData​(
Object
userData)
```

Set the user data.

**Parameters:** userData

- The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** getUserData()

- toString

```java
public
String
toString()
```

Returns a String representation of this notification.

**Overrides:** toString

in class

EventObject
**Returns:** A String representation of this notification.

---

#### Method Detail

setSource

```java
public void setSource​(
Object
source)
```

Sets the source.

**Parameters:** source

- the new source for this object.
**See Also:** EventObject.getSource()

---

#### setSource

public void setSource​(

Object

source)

Sets the source.

getSequenceNumber

```java
public long getSequenceNumber()
```

Get the notification sequence number.

**Returns:** The notification sequence number within the source object. It's a serial number
identifying a particular instance of notification in the context of the notification source.
The notification model does not assume that notifications will be received in the same order
that they are sent. The sequence number helps listeners to sort received notifications.
**See Also:** setSequenceNumber(long)

---

#### getSequenceNumber

public long getSequenceNumber()

Get the notification sequence number.

setSequenceNumber

```java
public void setSequenceNumber​(long sequenceNumber)
```

Set the notification sequence number.

**Parameters:** sequenceNumber

- The notification sequence number within the source object. It is
a serial number identifying a particular instance of notification in the
context of the notification source.
**See Also:** getSequenceNumber()

---

#### setSequenceNumber

public void setSequenceNumber​(long sequenceNumber)

Set the notification sequence number.

getType

```java
public
String
getType()
```

Get the notification type.

**Returns:** The notification type. It's a string expressed in a dot notation
similar to Java properties. It is recommended that the notification type
should follow the reverse-domain-name convention used by Java package
names. An example of a notification type is com.example.alarm.router.

---

#### getType

public

String

getType()

Get the notification type.

getTimeStamp

```java
public long getTimeStamp()
```

Get the notification timestamp.

**Returns:** The notification timestamp.
**See Also:** setTimeStamp(long)

---

#### getTimeStamp

public long getTimeStamp()

Get the notification timestamp.

setTimeStamp

```java
public void setTimeStamp​(long timeStamp)
```

Set the notification timestamp.

**Parameters:** timeStamp

- The notification timestamp. It indicates when the notification was generated.
**See Also:** getTimeStamp()

---

#### setTimeStamp

public void setTimeStamp​(long timeStamp)

Set the notification timestamp.

getMessage

```java
public
String
getMessage()
```

Get the notification message.

**Returns:** The message string of this notification object.

---

#### getMessage

public

String

getMessage()

Get the notification message.

getUserData

```java
public
Object
getUserData()
```

Get the user data.

**Returns:** The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** setUserData(java.lang.Object)

---

#### getUserData

public

Object

getUserData()

Get the user data.

setUserData

```java
public void setUserData​(
Object
userData)
```

Set the user data.

**Parameters:** userData

- The user data object. It is used for whatever data
the notification source wishes to communicate to its consumers.
**See Also:** getUserData()

---

#### setUserData

public void setUserData​(

Object

userData)

Set the user data.

toString

```java
public
String
toString()
```

Returns a String representation of this notification.

**Overrides:** toString

in class

EventObject
**Returns:** A String representation of this notification.

---

#### toString

public

String

toString()

Returns a String representation of this notification.

---

