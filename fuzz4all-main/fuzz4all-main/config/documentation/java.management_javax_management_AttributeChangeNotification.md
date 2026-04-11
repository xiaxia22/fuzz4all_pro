# Class AttributeChangeNotification

**Source:** `java.management\javax\management\AttributeChangeNotification.html`

### Class Description

```java
public class
AttributeChangeNotification

extends
Notification
```

Provides definitions of the attribute change notifications sent by MBeans.

It's up to the MBean owning the attribute of interest to create and send
attribute change notifications when the attribute change occurs.
So the

NotificationBroadcaster

interface has to be implemented
by any MBean for which an attribute change is of interest.

Example:
If an MBean called

myMbean

needs to notify registered listeners
when its attribute:

String myString

is modified,

myMbean

creates and emits the following notification:

new AttributeChangeNotification(myMbean, sequenceNumber, timeStamp, msg,
"myString", "String", oldValue, newValue);

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
String
ATTRIBUTE_CHANGE

Notification type which indicates that the observed MBean attribute value has changed.

The value of this type string is

jmx.attribute.change

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public AttributeChangeNotification​(
Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

String
attributeName,

String
attributeType,

Object
oldValue,

Object
newValue)

Constructs an attribute change notification object.
In addition to the information common to all notification, the caller must supply the name and type
of the attribute, as well as its old and new values.

**Parameters:**
- source

- The notification producer, that is, the MBean the attribute belongs to.
- sequenceNumber

- The notification sequence number within the source object.
- timeStamp

- The date at which the notification is being sent.
- msg

- A String containing the message of the notification.
- attributeName

- A String giving the name of the attribute.
- attributeType

- A String containing the type of the attribute.
- oldValue

- An object representing value of the attribute before the change.
- newValue

- An object representing value of the attribute after the change.

---

### Method Details

#### public
String
getAttributeName()

Gets the name of the attribute which has changed.

**Returns:**
- A String containing the name of the attribute.

---

#### public
String
getAttributeType()

Gets the type of the attribute which has changed.

**Returns:**
- A String containing the type of the attribute.

---

#### public
Object
getOldValue()

Gets the old value of the attribute which has changed.

**Returns:**
- An Object containing the old value of the attribute.

---

#### public
Object
getNewValue()

Gets the new value of the attribute which has changed.

**Returns:**
- An Object containing the new value of the attribute.

---

### Additional Sections

#### Class AttributeChangeNotification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification
- - javax.management.AttributeChangeNotification

java.util.EventObject

- javax.management.Notification
- - javax.management.AttributeChangeNotification

javax.management.Notification

- javax.management.AttributeChangeNotification

javax.management.AttributeChangeNotification

**All Implemented Interfaces:** Serializable

```java
public class
AttributeChangeNotification

extends
Notification
```

Provides definitions of the attribute change notifications sent by MBeans.

It's up to the MBean owning the attribute of interest to create and send
attribute change notifications when the attribute change occurs.
So the

NotificationBroadcaster

interface has to be implemented
by any MBean for which an attribute change is of interest.

Example:
If an MBean called

myMbean

needs to notify registered listeners
when its attribute:

String myString

is modified,

myMbean

creates and emits the following notification:

new AttributeChangeNotification(myMbean, sequenceNumber, timeStamp, msg,
"myString", "String", oldValue, newValue);

**Since:** 1.5
**See Also:** Serialized Form

public class

AttributeChangeNotification

extends

Notification

Provides definitions of the attribute change notifications sent by MBeans.

It's up to the MBean owning the attribute of interest to create and send
attribute change notifications when the attribute change occurs.
So the

NotificationBroadcaster

interface has to be implemented
by any MBean for which an attribute change is of interest.

Example:
If an MBean called

myMbean

needs to notify registered listeners
when its attribute:

String myString

is modified,

myMbean

creates and emits the following notification:

new AttributeChangeNotification(myMbean, sequenceNumber, timeStamp, msg,
"myString", "String", oldValue, newValue);

It's up to the MBean owning the attribute of interest to create and send
attribute change notifications when the attribute change occurs.
So the

NotificationBroadcaster

interface has to be implemented
by any MBean for which an attribute change is of interest.

Example:
If an MBean called

myMbean

needs to notify registered listeners
when its attribute:

String myString

is modified,

myMbean

creates and emits the following notification:

new AttributeChangeNotification(myMbean, sequenceNumber, timeStamp, msg,
"myString", "String", oldValue, newValue);

Example:
If an MBean called

myMbean

needs to notify registered listeners
when its attribute:

String myString

is modified,

myMbean

creates and emits the following notification:

new AttributeChangeNotification(myMbean, sequenceNumber, timeStamp, msg,
"myString", "String", oldValue, newValue);

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ATTRIBUTE_CHANGE

Notification type which indicates that the observed MBean attribute value has changed.

- Fields declared in class javax.management.

Notification

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AttributeChangeNotification

​(

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

String

attributeName,

String

attributeType,

Object

oldValue,

Object

newValue)

Constructs an attribute change notification object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeName

()

Gets the name of the attribute which has changed.

String

getAttributeType

()

Gets the type of the attribute which has changed.

Object

getNewValue

()

Gets the new value of the attribute which has changed.

Object

getOldValue

()

Gets the old value of the attribute which has changed.

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

Fields

Modifier and Type

Field

Description

static

String

ATTRIBUTE_CHANGE

Notification type which indicates that the observed MBean attribute value has changed.

- Fields declared in class javax.management.

Notification

source

---

#### Field Summary

Notification type which indicates that the observed MBean attribute value has changed.

Fields declared in class javax.management.

Notification

source

---

#### Fields declared in class javax.management. Notification

Constructor Summary

Constructors

Constructor

Description

AttributeChangeNotification

​(

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

String

attributeName,

String

attributeType,

Object

oldValue,

Object

newValue)

Constructs an attribute change notification object.

---

#### Constructor Summary

Constructs an attribute change notification object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAttributeName

()

Gets the name of the attribute which has changed.

String

getAttributeType

()

Gets the type of the attribute which has changed.

Object

getNewValue

()

Gets the new value of the attribute which has changed.

Object

getOldValue

()

Gets the old value of the attribute which has changed.

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

Gets the name of the attribute which has changed.

Gets the type of the attribute which has changed.

Gets the new value of the attribute which has changed.

Gets the old value of the attribute which has changed.

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

============ FIELD DETAIL ===========

- Field Detail

- ATTRIBUTE_CHANGE

```java
public static final
String
ATTRIBUTE_CHANGE
```

Notification type which indicates that the observed MBean attribute value has changed.

The value of this type string is

jmx.attribute.change

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AttributeChangeNotification

```java
public AttributeChangeNotification​(
Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

String
attributeName,

String
attributeType,

Object
oldValue,

Object
newValue)
```

Constructs an attribute change notification object.
In addition to the information common to all notification, the caller must supply the name and type
of the attribute, as well as its old and new values.

**Parameters:** source

- The notification producer, that is, the MBean the attribute belongs to.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The date at which the notification is being sent.
**Parameters:** msg

- A String containing the message of the notification.
**Parameters:** attributeName

- A String giving the name of the attribute.
**Parameters:** attributeType

- A String containing the type of the attribute.
**Parameters:** oldValue

- An object representing value of the attribute before the change.
**Parameters:** newValue

- An object representing value of the attribute after the change.

============ METHOD DETAIL ==========

- Method Detail

- getAttributeName

```java
public
String
getAttributeName()
```

Gets the name of the attribute which has changed.

**Returns:** A String containing the name of the attribute.

- getAttributeType

```java
public
String
getAttributeType()
```

Gets the type of the attribute which has changed.

**Returns:** A String containing the type of the attribute.

- getOldValue

```java
public
Object
getOldValue()
```

Gets the old value of the attribute which has changed.

**Returns:** An Object containing the old value of the attribute.

- getNewValue

```java
public
Object
getNewValue()
```

Gets the new value of the attribute which has changed.

**Returns:** An Object containing the new value of the attribute.

Field Detail

- ATTRIBUTE_CHANGE

```java
public static final
String
ATTRIBUTE_CHANGE
```

Notification type which indicates that the observed MBean attribute value has changed.

The value of this type string is

jmx.attribute.change

.

**See Also:** Constant Field Values

---

#### Field Detail

ATTRIBUTE_CHANGE

```java
public static final
String
ATTRIBUTE_CHANGE
```

Notification type which indicates that the observed MBean attribute value has changed.

The value of this type string is

jmx.attribute.change

.

**See Also:** Constant Field Values

---

#### ATTRIBUTE_CHANGE

public static final

String

ATTRIBUTE_CHANGE

Notification type which indicates that the observed MBean attribute value has changed.

The value of this type string is

jmx.attribute.change

.

Constructor Detail

- AttributeChangeNotification

```java
public AttributeChangeNotification​(
Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

String
attributeName,

String
attributeType,

Object
oldValue,

Object
newValue)
```

Constructs an attribute change notification object.
In addition to the information common to all notification, the caller must supply the name and type
of the attribute, as well as its old and new values.

**Parameters:** source

- The notification producer, that is, the MBean the attribute belongs to.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The date at which the notification is being sent.
**Parameters:** msg

- A String containing the message of the notification.
**Parameters:** attributeName

- A String giving the name of the attribute.
**Parameters:** attributeType

- A String containing the type of the attribute.
**Parameters:** oldValue

- An object representing value of the attribute before the change.
**Parameters:** newValue

- An object representing value of the attribute after the change.

---

#### Constructor Detail

AttributeChangeNotification

```java
public AttributeChangeNotification​(
Object
source,
long sequenceNumber,
long timeStamp,

String
msg,

String
attributeName,

String
attributeType,

Object
oldValue,

Object
newValue)
```

Constructs an attribute change notification object.
In addition to the information common to all notification, the caller must supply the name and type
of the attribute, as well as its old and new values.

**Parameters:** source

- The notification producer, that is, the MBean the attribute belongs to.
**Parameters:** sequenceNumber

- The notification sequence number within the source object.
**Parameters:** timeStamp

- The date at which the notification is being sent.
**Parameters:** msg

- A String containing the message of the notification.
**Parameters:** attributeName

- A String giving the name of the attribute.
**Parameters:** attributeType

- A String containing the type of the attribute.
**Parameters:** oldValue

- An object representing value of the attribute before the change.
**Parameters:** newValue

- An object representing value of the attribute after the change.

---

#### AttributeChangeNotification

public AttributeChangeNotification​(

Object

source,
long sequenceNumber,
long timeStamp,

String

msg,

String

attributeName,

String

attributeType,

Object

oldValue,

Object

newValue)

Constructs an attribute change notification object.
In addition to the information common to all notification, the caller must supply the name and type
of the attribute, as well as its old and new values.

Method Detail

- getAttributeName

```java
public
String
getAttributeName()
```

Gets the name of the attribute which has changed.

**Returns:** A String containing the name of the attribute.

- getAttributeType

```java
public
String
getAttributeType()
```

Gets the type of the attribute which has changed.

**Returns:** A String containing the type of the attribute.

- getOldValue

```java
public
Object
getOldValue()
```

Gets the old value of the attribute which has changed.

**Returns:** An Object containing the old value of the attribute.

- getNewValue

```java
public
Object
getNewValue()
```

Gets the new value of the attribute which has changed.

**Returns:** An Object containing the new value of the attribute.

---

#### Method Detail

getAttributeName

```java
public
String
getAttributeName()
```

Gets the name of the attribute which has changed.

**Returns:** A String containing the name of the attribute.

---

#### getAttributeName

public

String

getAttributeName()

Gets the name of the attribute which has changed.

getAttributeType

```java
public
String
getAttributeType()
```

Gets the type of the attribute which has changed.

**Returns:** A String containing the type of the attribute.

---

#### getAttributeType

public

String

getAttributeType()

Gets the type of the attribute which has changed.

getOldValue

```java
public
Object
getOldValue()
```

Gets the old value of the attribute which has changed.

**Returns:** An Object containing the old value of the attribute.

---

#### getOldValue

public

Object

getOldValue()

Gets the old value of the attribute which has changed.

getNewValue

```java
public
Object
getNewValue()
```

Gets the new value of the attribute which has changed.

**Returns:** An Object containing the new value of the attribute.

---

#### getNewValue

public

Object

getNewValue()

Gets the new value of the attribute which has changed.

---

