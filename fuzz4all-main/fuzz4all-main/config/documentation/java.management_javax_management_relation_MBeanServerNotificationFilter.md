# Class MBeanServerNotificationFilter

**Source:** `java.management\javax\management\relation\MBeanServerNotificationFilter.html`

### Class Description

```java
public class
MBeanServerNotificationFilter

extends
NotificationFilterSupport
```

Filter for

MBeanServerNotification

.
This filter filters MBeanServerNotification notifications by
selecting the ObjectNames of interest and the operations (registration,
unregistration, both) of interest (corresponding to notification
types).

The

serialVersionUID

of this class is

2605900539589789736L

.

**All Implemented Interfaces:** Serializable

,

NotificationFilter

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanServerNotificationFilter()

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

---

### Method Details

#### public void disableAllObjectNames()

Disables any MBeanServerNotification (all ObjectNames are
deselected).

---

#### public void disableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException

Disables MBeanServerNotifications concerning given ObjectName.

**Parameters:**
- objectName

- ObjectName no longer of interest

**Throws:**
- IllegalArgumentException

- if the given ObjectName is null

---

#### public void enableAllObjectNames()

Enables all MBeanServerNotifications (all ObjectNames are selected).

---

#### public void enableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException

Enables MBeanServerNotifications concerning given ObjectName.

**Parameters:**
- objectName

- ObjectName of interest

**Throws:**
- IllegalArgumentException

- if the given ObjectName is null

---

#### public
Vector
<
ObjectName
> getEnabledObjectNames()

Gets all the ObjectNames enabled.

**Returns:**
- Vector of ObjectNames:

- null means all ObjectNames are implicitly selected, except the
ObjectNames explicitly deselected

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

---

#### public
Vector
<
ObjectName
> getDisabledObjectNames()

Gets all the ObjectNames disabled.

**Returns:**
- Vector of ObjectNames:

- null means all ObjectNames are implicitly deselected, except the
ObjectNames explicitly selected

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

---

#### public boolean isNotificationEnabled​(
Notification
notif)
throws
IllegalArgumentException

Invoked before sending the specified notification to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

**Specified by:**
- isNotificationEnabled

in interface

NotificationFilter

**Overrides:**
- isNotificationEnabled

in class

NotificationFilterSupport

**Parameters:**
- notif

- The notification to be sent.

**Returns:**
- true if the notification has to be sent to the listener, false
otherwise.

**Throws:**
- IllegalArgumentException

- if null parameter

---

### Additional Sections

#### Class MBeanServerNotificationFilter

java.lang.Object

- javax.management.NotificationFilterSupport
- - javax.management.relation.MBeanServerNotificationFilter

javax.management.NotificationFilterSupport

- javax.management.relation.MBeanServerNotificationFilter

javax.management.relation.MBeanServerNotificationFilter

**All Implemented Interfaces:** Serializable

,

NotificationFilter

```java
public class
MBeanServerNotificationFilter

extends
NotificationFilterSupport
```

Filter for

MBeanServerNotification

.
This filter filters MBeanServerNotification notifications by
selecting the ObjectNames of interest and the operations (registration,
unregistration, both) of interest (corresponding to notification
types).

The

serialVersionUID

of this class is

2605900539589789736L

.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanServerNotificationFilter

extends

NotificationFilterSupport

Filter for

MBeanServerNotification

.
This filter filters MBeanServerNotification notifications by
selecting the ObjectNames of interest and the operations (registration,
unregistration, both) of interest (corresponding to notification
types).

The

serialVersionUID

of this class is

2605900539589789736L

.

The

serialVersionUID

of this class is

2605900539589789736L

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanServerNotificationFilter

()

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

disableAllObjectNames

()

Disables any MBeanServerNotification (all ObjectNames are
deselected).

void

disableObjectName

​(

ObjectName

objectName)

Disables MBeanServerNotifications concerning given ObjectName.

void

enableAllObjectNames

()

Enables all MBeanServerNotifications (all ObjectNames are selected).

void

enableObjectName

​(

ObjectName

objectName)

Enables MBeanServerNotifications concerning given ObjectName.

Vector

<

ObjectName

>

getDisabledObjectNames

()

Gets all the ObjectNames disabled.

Vector

<

ObjectName

>

getEnabledObjectNames

()

Gets all the ObjectNames enabled.

boolean

isNotificationEnabled

​(

Notification

notif)

Invoked before sending the specified notification to the listener.

- Methods declared in class javax.management.

NotificationFilterSupport

disableAllTypes

,

disableType

,

enableType

,

getEnabledTypes

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

Constructor

Description

MBeanServerNotificationFilter

()

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

---

#### Constructor Summary

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

disableAllObjectNames

()

Disables any MBeanServerNotification (all ObjectNames are
deselected).

void

disableObjectName

​(

ObjectName

objectName)

Disables MBeanServerNotifications concerning given ObjectName.

void

enableAllObjectNames

()

Enables all MBeanServerNotifications (all ObjectNames are selected).

void

enableObjectName

​(

ObjectName

objectName)

Enables MBeanServerNotifications concerning given ObjectName.

Vector

<

ObjectName

>

getDisabledObjectNames

()

Gets all the ObjectNames disabled.

Vector

<

ObjectName

>

getEnabledObjectNames

()

Gets all the ObjectNames enabled.

boolean

isNotificationEnabled

​(

Notification

notif)

Invoked before sending the specified notification to the listener.

- Methods declared in class javax.management.

NotificationFilterSupport

disableAllTypes

,

disableType

,

enableType

,

getEnabledTypes

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

Disables any MBeanServerNotification (all ObjectNames are
deselected).

Disables MBeanServerNotifications concerning given ObjectName.

Enables all MBeanServerNotifications (all ObjectNames are selected).

Enables MBeanServerNotifications concerning given ObjectName.

Gets all the ObjectNames disabled.

Gets all the ObjectNames enabled.

Invoked before sending the specified notification to the listener.

Methods declared in class javax.management.

NotificationFilterSupport

disableAllTypes

,

disableType

,

enableType

,

getEnabledTypes

---

#### Methods declared in class javax.management. NotificationFilterSupport

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

- MBeanServerNotificationFilter

```java
public MBeanServerNotificationFilter()
```

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

============ METHOD DETAIL ==========

- Method Detail

- disableAllObjectNames

```java
public void disableAllObjectNames()
```

Disables any MBeanServerNotification (all ObjectNames are
deselected).

- disableObjectName

```java
public void disableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Disables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName no longer of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

- enableAllObjectNames

```java
public void enableAllObjectNames()
```

Enables all MBeanServerNotifications (all ObjectNames are selected).

- enableObjectName

```java
public void enableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Enables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

- getEnabledObjectNames

```java
public
Vector
<
ObjectName
> getEnabledObjectNames()
```

Gets all the ObjectNames enabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly selected, except the
ObjectNames explicitly deselected

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

- getDisabledObjectNames

```java
public
Vector
<
ObjectName
> getDisabledObjectNames()
```

Gets all the ObjectNames disabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly deselected, except the
ObjectNames explicitly selected

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

- isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notif)
throws
IllegalArgumentException
```

Invoked before sending the specified notification to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Overrides:** isNotificationEnabled

in class

NotificationFilterSupport
**Parameters:** notif

- The notification to be sent.
**Returns:** true if the notification has to be sent to the listener, false
otherwise.
**Throws:** IllegalArgumentException

- if null parameter

Constructor Detail

- MBeanServerNotificationFilter

```java
public MBeanServerNotificationFilter()
```

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

---

#### Constructor Detail

MBeanServerNotificationFilter

```java
public MBeanServerNotificationFilter()
```

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

---

#### MBeanServerNotificationFilter

public MBeanServerNotificationFilter()

Creates a filter selecting all MBeanServerNotification notifications for
all ObjectNames.

Method Detail

- disableAllObjectNames

```java
public void disableAllObjectNames()
```

Disables any MBeanServerNotification (all ObjectNames are
deselected).

- disableObjectName

```java
public void disableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Disables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName no longer of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

- enableAllObjectNames

```java
public void enableAllObjectNames()
```

Enables all MBeanServerNotifications (all ObjectNames are selected).

- enableObjectName

```java
public void enableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Enables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

- getEnabledObjectNames

```java
public
Vector
<
ObjectName
> getEnabledObjectNames()
```

Gets all the ObjectNames enabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly selected, except the
ObjectNames explicitly deselected

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

- getDisabledObjectNames

```java
public
Vector
<
ObjectName
> getDisabledObjectNames()
```

Gets all the ObjectNames disabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly deselected, except the
ObjectNames explicitly selected

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

- isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notif)
throws
IllegalArgumentException
```

Invoked before sending the specified notification to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Overrides:** isNotificationEnabled

in class

NotificationFilterSupport
**Parameters:** notif

- The notification to be sent.
**Returns:** true if the notification has to be sent to the listener, false
otherwise.
**Throws:** IllegalArgumentException

- if null parameter

---

#### Method Detail

disableAllObjectNames

```java
public void disableAllObjectNames()
```

Disables any MBeanServerNotification (all ObjectNames are
deselected).

---

#### disableAllObjectNames

public void disableAllObjectNames()

Disables any MBeanServerNotification (all ObjectNames are
deselected).

disableObjectName

```java
public void disableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Disables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName no longer of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

---

#### disableObjectName

public void disableObjectName​(

ObjectName

objectName)
throws

IllegalArgumentException

Disables MBeanServerNotifications concerning given ObjectName.

enableAllObjectNames

```java
public void enableAllObjectNames()
```

Enables all MBeanServerNotifications (all ObjectNames are selected).

---

#### enableAllObjectNames

public void enableAllObjectNames()

Enables all MBeanServerNotifications (all ObjectNames are selected).

enableObjectName

```java
public void enableObjectName​(
ObjectName
objectName)
throws
IllegalArgumentException
```

Enables MBeanServerNotifications concerning given ObjectName.

**Parameters:** objectName

- ObjectName of interest
**Throws:** IllegalArgumentException

- if the given ObjectName is null

---

#### enableObjectName

public void enableObjectName​(

ObjectName

objectName)
throws

IllegalArgumentException

Enables MBeanServerNotifications concerning given ObjectName.

getEnabledObjectNames

```java
public
Vector
<
ObjectName
> getEnabledObjectNames()
```

Gets all the ObjectNames enabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly selected, except the
ObjectNames explicitly deselected

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

---

#### getEnabledObjectNames

public

Vector

<

ObjectName

> getEnabledObjectNames()

Gets all the ObjectNames enabled.

- null means all ObjectNames are implicitly selected, except the
ObjectNames explicitly deselected

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

- empty means all ObjectNames are deselected, i.e. no ObjectName
selected.

getDisabledObjectNames

```java
public
Vector
<
ObjectName
> getDisabledObjectNames()
```

Gets all the ObjectNames disabled.

**Returns:** Vector of ObjectNames:

- null means all ObjectNames are implicitly deselected, except the
ObjectNames explicitly selected

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

---

#### getDisabledObjectNames

public

Vector

<

ObjectName

> getDisabledObjectNames()

Gets all the ObjectNames disabled.

- null means all ObjectNames are implicitly deselected, except the
ObjectNames explicitly selected

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

- empty means all ObjectNames are selected, i.e. no ObjectName
deselected.

isNotificationEnabled

```java
public boolean isNotificationEnabled​(
Notification
notif)
throws
IllegalArgumentException
```

Invoked before sending the specified notification to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

**Specified by:** isNotificationEnabled

in interface

NotificationFilter
**Overrides:** isNotificationEnabled

in class

NotificationFilterSupport
**Parameters:** notif

- The notification to be sent.
**Returns:** true if the notification has to be sent to the listener, false
otherwise.
**Throws:** IllegalArgumentException

- if null parameter

---

#### isNotificationEnabled

public boolean isNotificationEnabled​(

Notification

notif)
throws

IllegalArgumentException

Invoked before sending the specified notification to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

If:

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

- the ObjectName of the concerned MBean is selected (explicitly OR
(implicitly and not explicitly deselected))

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

AND

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

- the type of the operation (registration or unregistration) is
selected

then the notification is sent to the listener.

then the notification is sent to the listener.

---

