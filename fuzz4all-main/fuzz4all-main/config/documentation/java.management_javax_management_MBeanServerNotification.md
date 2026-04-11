# Class MBeanServerNotification

**Source:** `java.management\javax\management\MBeanServerNotification.html`

### Class Description

```java
public class
MBeanServerNotification

extends
Notification
```

Represents a notification emitted by the MBean Server through the MBeanServerDelegate MBean.
The MBean Server emits the following types of notifications: MBean registration, MBean
unregistration.

To receive MBeanServerNotifications, you need to register a listener with
the

MBeanServerDelegate

MBean
that represents the MBeanServer. The ObjectName of the MBeanServerDelegate is

MBeanServerDelegate.DELEGATE_NAME

, which is

JMImplementation:type=MBeanServerDelegate

.

The following code prints a message every time an MBean is registered
or unregistered in the MBean Server

mbeanServer

:

```java
private static final NotificationListener printListener = new NotificationListener() {
public void handleNotification(Notification n, Object handback) {
if (!(n instanceof MBeanServerNotification)) {
System.out.println("Ignored notification of class " + n.getClass().getName());
return;
}
MBeanServerNotification mbsn = (MBeanServerNotification) n;
String what;
if (n.getType().equals(MBeanServerNotification.REGISTRATION_NOTIFICATION))
what = "MBean registered";
else if (n.getType().equals(MBeanServerNotification.UNREGISTRATION_NOTIFICATION))
what = "MBean unregistered";
else
what = "Unknown type " + n.getType();
System.out.println("Received MBean Server notification: " + what + ": " +
mbsn.getMBeanName());
}
};

...
mbeanServer.addNotificationListener(
MBeanServerDelegate.DELEGATE_NAME, printListener, null, null);
```

An MBean which is not an

MBeanServerDelegate

may also emit
MBeanServerNotifications. In particular, there is a convention for
MBeans to emit an MBeanServerNotification for a group of MBeans.

An MBeanServerNotification emitted to denote the registration or
unregistration of a group of MBeans has the following characteristics:

- Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.
- Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered
- Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
String
REGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been registered.
Value is "JMX.mbean.registered".

**See Also:**
- Constant Field Values

---

#### public static final
String
UNREGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been unregistered.
Value is "JMX.mbean.unregistered".

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MBeanServerNotification​(
String
type,

Object
source,
long sequenceNumber,

ObjectName
objectName)

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

**Parameters:**
- type

- A string denoting the type of the
notification. Set it to one these values:

REGISTRATION_NOTIFICATION

,

UNREGISTRATION_NOTIFICATION

.
- source

- The MBeanServerNotification object responsible
for forwarding MBean server notification.
- sequenceNumber

- A sequence number that can be used to order
received notifications.
- objectName

- The object name of the MBean that caused the
notification.

---

### Method Details

#### public
ObjectName
getMBeanName()

Returns the object name of the MBean that caused the notification.

**Returns:**
- the object name of the MBean that caused the notification.

---

### Additional Sections

#### Class MBeanServerNotification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification
- - javax.management.MBeanServerNotification

java.util.EventObject

- javax.management.Notification
- - javax.management.MBeanServerNotification

javax.management.Notification

- javax.management.MBeanServerNotification

javax.management.MBeanServerNotification

**All Implemented Interfaces:** Serializable

```java
public class
MBeanServerNotification

extends
Notification
```

Represents a notification emitted by the MBean Server through the MBeanServerDelegate MBean.
The MBean Server emits the following types of notifications: MBean registration, MBean
unregistration.

To receive MBeanServerNotifications, you need to register a listener with
the

MBeanServerDelegate

MBean
that represents the MBeanServer. The ObjectName of the MBeanServerDelegate is

MBeanServerDelegate.DELEGATE_NAME

, which is

JMImplementation:type=MBeanServerDelegate

.

The following code prints a message every time an MBean is registered
or unregistered in the MBean Server

mbeanServer

:

```java
private static final NotificationListener printListener = new NotificationListener() {
public void handleNotification(Notification n, Object handback) {
if (!(n instanceof MBeanServerNotification)) {
System.out.println("Ignored notification of class " + n.getClass().getName());
return;
}
MBeanServerNotification mbsn = (MBeanServerNotification) n;
String what;
if (n.getType().equals(MBeanServerNotification.REGISTRATION_NOTIFICATION))
what = "MBean registered";
else if (n.getType().equals(MBeanServerNotification.UNREGISTRATION_NOTIFICATION))
what = "MBean unregistered";
else
what = "Unknown type " + n.getType();
System.out.println("Received MBean Server notification: " + what + ": " +
mbsn.getMBeanName());
}
};

...
mbeanServer.addNotificationListener(
MBeanServerDelegate.DELEGATE_NAME, printListener, null, null);
```

An MBean which is not an

MBeanServerDelegate

may also emit
MBeanServerNotifications. In particular, there is a convention for
MBeans to emit an MBeanServerNotification for a group of MBeans.

An MBeanServerNotification emitted to denote the registration or
unregistration of a group of MBeans has the following characteristics:

- Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.
- Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered
- Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanServerNotification

extends

Notification

Represents a notification emitted by the MBean Server through the MBeanServerDelegate MBean.
The MBean Server emits the following types of notifications: MBean registration, MBean
unregistration.

To receive MBeanServerNotifications, you need to register a listener with
the

MBeanServerDelegate

MBean
that represents the MBeanServer. The ObjectName of the MBeanServerDelegate is

MBeanServerDelegate.DELEGATE_NAME

, which is

JMImplementation:type=MBeanServerDelegate

.

The following code prints a message every time an MBean is registered
or unregistered in the MBean Server

mbeanServer

:

```java
private static final NotificationListener printListener = new NotificationListener() {
public void handleNotification(Notification n, Object handback) {
if (!(n instanceof MBeanServerNotification)) {
System.out.println("Ignored notification of class " + n.getClass().getName());
return;
}
MBeanServerNotification mbsn = (MBeanServerNotification) n;
String what;
if (n.getType().equals(MBeanServerNotification.REGISTRATION_NOTIFICATION))
what = "MBean registered";
else if (n.getType().equals(MBeanServerNotification.UNREGISTRATION_NOTIFICATION))
what = "MBean unregistered";
else
what = "Unknown type " + n.getType();
System.out.println("Received MBean Server notification: " + what + ": " +
mbsn.getMBeanName());
}
};

...
mbeanServer.addNotificationListener(
MBeanServerDelegate.DELEGATE_NAME, printListener, null, null);
```

An MBean which is not an

MBeanServerDelegate

may also emit
MBeanServerNotifications. In particular, there is a convention for
MBeans to emit an MBeanServerNotification for a group of MBeans.

An MBeanServerNotification emitted to denote the registration or
unregistration of a group of MBeans has the following characteristics:

- Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.
- Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered
- Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

To receive MBeanServerNotifications, you need to register a listener with
the

MBeanServerDelegate

MBean
that represents the MBeanServer. The ObjectName of the MBeanServerDelegate is

MBeanServerDelegate.DELEGATE_NAME

, which is

JMImplementation:type=MBeanServerDelegate

.

The following code prints a message every time an MBean is registered
or unregistered in the MBean Server

mbeanServer

:

```java
private static final NotificationListener printListener = new NotificationListener() {
public void handleNotification(Notification n, Object handback) {
if (!(n instanceof MBeanServerNotification)) {
System.out.println("Ignored notification of class " + n.getClass().getName());
return;
}
MBeanServerNotification mbsn = (MBeanServerNotification) n;
String what;
if (n.getType().equals(MBeanServerNotification.REGISTRATION_NOTIFICATION))
what = "MBean registered";
else if (n.getType().equals(MBeanServerNotification.UNREGISTRATION_NOTIFICATION))
what = "MBean unregistered";
else
what = "Unknown type " + n.getType();
System.out.println("Received MBean Server notification: " + what + ": " +
mbsn.getMBeanName());
}
};

...
mbeanServer.addNotificationListener(
MBeanServerDelegate.DELEGATE_NAME, printListener, null, null);
```

An MBean which is not an

MBeanServerDelegate

may also emit
MBeanServerNotifications. In particular, there is a convention for
MBeans to emit an MBeanServerNotification for a group of MBeans.

An MBeanServerNotification emitted to denote the registration or
unregistration of a group of MBeans has the following characteristics:

- Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.
- Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered
- Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

The following code prints a message every time an MBean is registered
or unregistered in the MBean Server

mbeanServer

:

private static final NotificationListener printListener = new NotificationListener() {
public void handleNotification(Notification n, Object handback) {
if (!(n instanceof MBeanServerNotification)) {
System.out.println("Ignored notification of class " + n.getClass().getName());
return;
}
MBeanServerNotification mbsn = (MBeanServerNotification) n;
String what;
if (n.getType().equals(MBeanServerNotification.REGISTRATION_NOTIFICATION))
what = "MBean registered";
else if (n.getType().equals(MBeanServerNotification.UNREGISTRATION_NOTIFICATION))
what = "MBean unregistered";
else
what = "Unknown type " + n.getType();
System.out.println("Received MBean Server notification: " + what + ": " +
mbsn.getMBeanName());
}
};

...
mbeanServer.addNotificationListener(
MBeanServerDelegate.DELEGATE_NAME, printListener, null, null);

An MBean which is not an

MBeanServerDelegate

may also emit
MBeanServerNotifications. In particular, there is a convention for
MBeans to emit an MBeanServerNotification for a group of MBeans.

An MBeanServerNotification emitted to denote the registration or
unregistration of a group of MBeans has the following characteristics:

- Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.
- Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered
- Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

Its

notification type

is

"JMX.mbean.registered.group"

or

"JMX.mbean.unregistered.group"

, which can also be written

REGISTRATION_NOTIFICATION

+ ".group"

or

UNREGISTRATION_NOTIFICATION

+ ".group"

.

Its

MBean name

is an ObjectName pattern
that selects the set (or a superset) of the MBeans being registered
or unregistered

Its

user data

can optionally
be set to an array of ObjectNames containing the names of all MBeans
being registered or unregistered.

MBeans which emit these group registration/unregistration notifications will
declare them in their

MBeanNotificationInfo

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

REGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been registered.

static

String

UNREGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been unregistered.

- Fields declared in class javax.management.

Notification

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerNotification

​(

String

type,

Object

source,
long sequenceNumber,

ObjectName

objectName)

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ObjectName

getMBeanName

()

Returns the object name of the MBean that caused the notification.

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

REGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been registered.

static

String

UNREGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been unregistered.

- Fields declared in class javax.management.

Notification

source

---

#### Field Summary

Notification type denoting that an MBean has been registered.

Notification type denoting that an MBean has been unregistered.

Fields declared in class javax.management.

Notification

source

---

#### Fields declared in class javax.management. Notification

Constructor Summary

Constructors

Constructor

Description

MBeanServerNotification

​(

String

type,

Object

source,
long sequenceNumber,

ObjectName

objectName)

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

---

#### Constructor Summary

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

ObjectName

getMBeanName

()

Returns the object name of the MBean that caused the notification.

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

Returns the object name of the MBean that caused the notification.

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

- REGISTRATION_NOTIFICATION

```java
public static final
String
REGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been registered.
Value is "JMX.mbean.registered".

**See Also:** Constant Field Values

- UNREGISTRATION_NOTIFICATION

```java
public static final
String
UNREGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been unregistered.
Value is "JMX.mbean.unregistered".

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MBeanServerNotification

```java
public MBeanServerNotification​(
String
type,

Object
source,
long sequenceNumber,

ObjectName
objectName)
```

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

**Parameters:** type

- A string denoting the type of the
notification. Set it to one these values:

REGISTRATION_NOTIFICATION

,

UNREGISTRATION_NOTIFICATION

.
**Parameters:** source

- The MBeanServerNotification object responsible
for forwarding MBean server notification.
**Parameters:** sequenceNumber

- A sequence number that can be used to order
received notifications.
**Parameters:** objectName

- The object name of the MBean that caused the
notification.

============ METHOD DETAIL ==========

- Method Detail

- getMBeanName

```java
public
ObjectName
getMBeanName()
```

Returns the object name of the MBean that caused the notification.

**Returns:** the object name of the MBean that caused the notification.

Field Detail

- REGISTRATION_NOTIFICATION

```java
public static final
String
REGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been registered.
Value is "JMX.mbean.registered".

**See Also:** Constant Field Values

- UNREGISTRATION_NOTIFICATION

```java
public static final
String
UNREGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been unregistered.
Value is "JMX.mbean.unregistered".

**See Also:** Constant Field Values

---

#### Field Detail

REGISTRATION_NOTIFICATION

```java
public static final
String
REGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been registered.
Value is "JMX.mbean.registered".

**See Also:** Constant Field Values

---

#### REGISTRATION_NOTIFICATION

public static final

String

REGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been registered.
Value is "JMX.mbean.registered".

UNREGISTRATION_NOTIFICATION

```java
public static final
String
UNREGISTRATION_NOTIFICATION
```

Notification type denoting that an MBean has been unregistered.
Value is "JMX.mbean.unregistered".

**See Also:** Constant Field Values

---

#### UNREGISTRATION_NOTIFICATION

public static final

String

UNREGISTRATION_NOTIFICATION

Notification type denoting that an MBean has been unregistered.
Value is "JMX.mbean.unregistered".

Constructor Detail

- MBeanServerNotification

```java
public MBeanServerNotification​(
String
type,

Object
source,
long sequenceNumber,

ObjectName
objectName)
```

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

**Parameters:** type

- A string denoting the type of the
notification. Set it to one these values:

REGISTRATION_NOTIFICATION

,

UNREGISTRATION_NOTIFICATION

.
**Parameters:** source

- The MBeanServerNotification object responsible
for forwarding MBean server notification.
**Parameters:** sequenceNumber

- A sequence number that can be used to order
received notifications.
**Parameters:** objectName

- The object name of the MBean that caused the
notification.

---

#### Constructor Detail

MBeanServerNotification

```java
public MBeanServerNotification​(
String
type,

Object
source,
long sequenceNumber,

ObjectName
objectName)
```

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

**Parameters:** type

- A string denoting the type of the
notification. Set it to one these values:

REGISTRATION_NOTIFICATION

,

UNREGISTRATION_NOTIFICATION

.
**Parameters:** source

- The MBeanServerNotification object responsible
for forwarding MBean server notification.
**Parameters:** sequenceNumber

- A sequence number that can be used to order
received notifications.
**Parameters:** objectName

- The object name of the MBean that caused the
notification.

---

#### MBeanServerNotification

public MBeanServerNotification​(

String

type,

Object

source,
long sequenceNumber,

ObjectName

objectName)

Creates an MBeanServerNotification object specifying object names of
the MBeans that caused the notification and the specified notification
type.

Method Detail

- getMBeanName

```java
public
ObjectName
getMBeanName()
```

Returns the object name of the MBean that caused the notification.

**Returns:** the object name of the MBean that caused the notification.

---

#### Method Detail

getMBeanName

```java
public
ObjectName
getMBeanName()
```

Returns the object name of the MBean that caused the notification.

**Returns:** the object name of the MBean that caused the notification.

---

#### getMBeanName

public

ObjectName

getMBeanName()

Returns the object name of the MBean that caused the notification.

---

