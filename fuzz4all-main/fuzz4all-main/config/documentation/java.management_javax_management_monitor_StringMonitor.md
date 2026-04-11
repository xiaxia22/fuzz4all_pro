# Class StringMonitor

**Source:** `java.management\javax\management\monitor\StringMonitor.html`

### Class Description

```java
public class
StringMonitor

extends
Monitor

implements
StringMonitorMBean
```

Defines a monitor MBean designed to observe the values of a string
attribute.

A string monitor sends notifications as follows:

- if the attribute value matches the string to compare value,
a

match notification

is sent.
The notify match flag must be set to

true

.

Subsequent matchings of the string to compare values do not
cause further notifications unless
the attribute value differs from the string to compare value.

if the attribute value differs from the string to compare value,
a

differ notification

is sent.
The notify differ flag must be set to

true

.

Subsequent differences from the string to compare value do
not cause further notifications unless
the attribute value matches the string to compare value.

**All Implemented Interfaces:** MBeanRegistration

,

MonitorMBean

,

StringMonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

*No entries found.*

### Constructor Details

#### public StringMonitor()

Default constructor.

---

### Method Details

#### public void start()

Starts the string monitor.

**Specified by:**
- start

in interface

MonitorMBean
- start

in class

Monitor

---

#### public void stop()

Stops the string monitor.

**Specified by:**
- stop

in interface

MonitorMBean
- stop

in class

Monitor

---

#### public
String
getDerivedGauge​(
ObjectName
object)

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

**Specified by:**
- getDerivedGauge

in interface

StringMonitorMBean

**Parameters:**
- object

- the name of the MBean whose derived gauge is required.

**Returns:**
- The derived gauge of the specified object.

---

#### public long getDerivedGaugeTimeStamp​(
ObjectName
object)

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

**Specified by:**
- getDerivedGaugeTimeStamp

in interface

StringMonitorMBean

**Parameters:**
- object

- the name of the object whose derived gauge
timestamp is to be returned.

**Returns:**
- The derived gauge timestamp of the specified object.

---

#### @Deprecated

public
String
getDerivedGauge()

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:**
- getDerivedGauge

in interface

StringMonitorMBean

**Returns:**
- The derived gauge.

---

#### @Deprecated

public long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

**Specified by:**
- getDerivedGaugeTimeStamp

in interface

StringMonitorMBean

**Returns:**
- The derived gauge timestamp.

---

#### public
String
getStringToCompare()

Gets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:**
- getStringToCompare

in interface

StringMonitorMBean

**Returns:**
- The string value.

**See Also:**
- setStringToCompare(java.lang.String)

---

#### public void setStringToCompare​(
String
value)
throws
IllegalArgumentException

Sets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:**
- setStringToCompare

in interface

StringMonitorMBean

**Parameters:**
- value

- The string value.

**Throws:**
- IllegalArgumentException

- The specified
string to compare is null.

**See Also:**
- getStringToCompare()

---

#### public boolean getNotifyMatch()

Gets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:**
- getNotifyMatch

in interface

StringMonitorMBean

**Returns:**
- true

if the string monitor notifies when
matching the string to compare,

false

otherwise.

**See Also:**
- setNotifyMatch(boolean)

---

#### public void setNotifyMatch​(boolean value)

Sets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:**
- setNotifyMatch

in interface

StringMonitorMBean

**Parameters:**
- value

- The matching notification's on/off switch value.

**See Also:**
- getNotifyMatch()

---

#### public boolean getNotifyDiffer()

Gets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:**
- getNotifyDiffer

in interface

StringMonitorMBean

**Returns:**
- true

if the string monitor notifies when
differing from the string to compare,

false

otherwise.

**See Also:**
- setNotifyDiffer(boolean)

---

#### public void setNotifyDiffer​(boolean value)

Sets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:**
- setNotifyDiffer

in interface

StringMonitorMBean

**Parameters:**
- value

- The differing notification's on/off switch value.

**See Also:**
- getNotifyDiffer()

---

#### public
MBeanNotificationInfo
[] getNotificationInfo()

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- the array of possible notifications.

---

### Additional Sections

#### Class StringMonitor

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.monitor.Monitor
- - javax.management.monitor.StringMonitor

javax.management.NotificationBroadcasterSupport

- javax.management.monitor.Monitor
- - javax.management.monitor.StringMonitor

javax.management.monitor.Monitor

- javax.management.monitor.StringMonitor

javax.management.monitor.StringMonitor

**All Implemented Interfaces:** MBeanRegistration

,

MonitorMBean

,

StringMonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

```java
public class
StringMonitor

extends
Monitor

implements
StringMonitorMBean
```

Defines a monitor MBean designed to observe the values of a string
attribute.

A string monitor sends notifications as follows:

- if the attribute value matches the string to compare value,
a

match notification

is sent.
The notify match flag must be set to

true

.

Subsequent matchings of the string to compare values do not
cause further notifications unless
the attribute value differs from the string to compare value.

if the attribute value differs from the string to compare value,
a

differ notification

is sent.
The notify differ flag must be set to

true

.

Subsequent differences from the string to compare value do
not cause further notifications unless
the attribute value matches the string to compare value.

**Since:** 1.5

public class

StringMonitor

extends

Monitor

implements

StringMonitorMBean

Defines a monitor MBean designed to observe the values of a string
attribute.

A string monitor sends notifications as follows:

- if the attribute value matches the string to compare value,
a

match notification

is sent.
The notify match flag must be set to

true

.

Subsequent matchings of the string to compare values do not
cause further notifications unless
the attribute value differs from the string to compare value.

if the attribute value differs from the string to compare value,
a

differ notification

is sent.
The notify differ flag must be set to

true

.

Subsequent differences from the string to compare value do
not cause further notifications unless
the attribute value matches the string to compare value.

A string monitor sends notifications as follows:

- if the attribute value matches the string to compare value,
a

match notification

is sent.
The notify match flag must be set to

true

.

Subsequent matchings of the string to compare values do not
cause further notifications unless
the attribute value differs from the string to compare value.

if the attribute value differs from the string to compare value,
a

differ notification

is sent.
The notify differ flag must be set to

true

.

Subsequent differences from the string to compare value do
not cause further notifications unless
the attribute value matches the string to compare value.

if the attribute value matches the string to compare value,
a

match notification

is sent.
The notify match flag must be set to

true

.

Subsequent matchings of the string to compare values do not
cause further notifications unless
the attribute value differs from the string to compare value.

if the attribute value differs from the string to compare value,
a

differ notification

is sent.
The notify differ flag must be set to

true

.

Subsequent differences from the string to compare value do
not cause further notifications unless
the attribute value matches the string to compare value.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.management.monitor.

Monitor

alreadyNotified

,

alreadyNotifieds

,

capacityIncrement

,

dbgTag

,

elementCount

,

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

,

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

,

OBSERVED_OBJECT_ERROR_NOTIFIED

,

RESET_FLAGS_ALREADY_NOTIFIED

,

RUNTIME_ERROR_NOTIFIED

,

server

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StringMonitor

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getDerivedGauge

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

String

getDerivedGauge

​(

ObjectName

object)

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

long

getDerivedGaugeTimeStamp

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

long

getDerivedGaugeTimeStamp

​(

ObjectName

object)

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

boolean

getNotifyDiffer

()

Gets the differing notification's on/off switch value common to
all observed MBeans.

boolean

getNotifyMatch

()

Gets the matching notification's on/off switch value common to
all observed MBeans.

String

getStringToCompare

()

Gets the string to compare with the observed attribute common
to all observed MBeans.

void

setNotifyDiffer

​(boolean value)

Sets the differing notification's on/off switch value common to
all observed MBeans.

void

setNotifyMatch

​(boolean value)

Sets the matching notification's on/off switch value common to
all observed MBeans.

void

setStringToCompare

​(

String

value)

Sets the string to compare with the observed attribute common
to all observed MBeans.

void

start

()

Starts the string monitor.

void

stop

()

Stops the string monitor.

- Methods declared in class javax.management.monitor.

Monitor

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.monitor.

MonitorMBean

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Field Summary

- Fields declared in class javax.management.monitor.

Monitor

alreadyNotified

,

alreadyNotifieds

,

capacityIncrement

,

dbgTag

,

elementCount

,

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

,

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

,

OBSERVED_OBJECT_ERROR_NOTIFIED

,

RESET_FLAGS_ALREADY_NOTIFIED

,

RUNTIME_ERROR_NOTIFIED

,

server

---

#### Field Summary

Fields declared in class javax.management.monitor.

Monitor

alreadyNotified

,

alreadyNotifieds

,

capacityIncrement

,

dbgTag

,

elementCount

,

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

,

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

,

OBSERVED_OBJECT_ERROR_NOTIFIED

,

RESET_FLAGS_ALREADY_NOTIFIED

,

RUNTIME_ERROR_NOTIFIED

,

server

---

#### Fields declared in class javax.management.monitor. Monitor

Constructor Summary

Constructors

Constructor

Description

StringMonitor

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getDerivedGauge

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

String

getDerivedGauge

​(

ObjectName

object)

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

long

getDerivedGaugeTimeStamp

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

long

getDerivedGaugeTimeStamp

​(

ObjectName

object)

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

boolean

getNotifyDiffer

()

Gets the differing notification's on/off switch value common to
all observed MBeans.

boolean

getNotifyMatch

()

Gets the matching notification's on/off switch value common to
all observed MBeans.

String

getStringToCompare

()

Gets the string to compare with the observed attribute common
to all observed MBeans.

void

setNotifyDiffer

​(boolean value)

Sets the differing notification's on/off switch value common to
all observed MBeans.

void

setNotifyMatch

​(boolean value)

Sets the matching notification's on/off switch value common to
all observed MBeans.

void

setStringToCompare

​(

String

value)

Sets the string to compare with the observed attribute common
to all observed MBeans.

void

start

()

Starts the string monitor.

void

stop

()

Stops the string monitor.

- Methods declared in class javax.management.monitor.

Monitor

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

- Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

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

- Methods declared in interface javax.management.monitor.

MonitorMBean

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

- Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

Gets the differing notification's on/off switch value common to
all observed MBeans.

Gets the matching notification's on/off switch value common to
all observed MBeans.

Gets the string to compare with the observed attribute common
to all observed MBeans.

Sets the differing notification's on/off switch value common to
all observed MBeans.

Sets the matching notification's on/off switch value common to
all observed MBeans.

Sets the string to compare with the observed attribute common
to all observed MBeans.

Starts the string monitor.

Stops the string monitor.

Methods declared in class javax.management.monitor.

Monitor

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

---

#### Methods declared in class javax.management.monitor. Monitor

Methods declared in class javax.management.

NotificationBroadcasterSupport

addNotificationListener

,

handleNotification

,

sendNotification

---

#### Methods declared in class javax.management. NotificationBroadcasterSupport

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

Methods declared in interface javax.management.monitor.

MonitorMBean

addObservedObject

,

containsObservedObject

,

getGranularityPeriod

,

getObservedAttribute

,

getObservedObject

,

getObservedObjects

,

isActive

,

removeObservedObject

,

setGranularityPeriod

,

setObservedAttribute

,

setObservedObject

---

#### Methods declared in interface javax.management.monitor. MonitorMBean

Methods declared in interface javax.management.

NotificationBroadcaster

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationBroadcaster

Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StringMonitor

```java
public StringMonitor()
```

Default constructor.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
public void start()
```

Starts the string monitor.

**Specified by:** start

in interface

MonitorMBean
**Specified by:** start

in class

Monitor

- stop

```java
public void stop()
```

Stops the string monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

- getDerivedGauge

```java
public
String
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Parameters:** object

- the name of the MBean whose derived gauge is required.
**Returns:** The derived gauge of the specified object.

- getDerivedGaugeTimeStamp

```java
public long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

- getDerivedGauge

```java
@Deprecated

public
String
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Returns:** The derived gauge.

- getDerivedGaugeTimeStamp

```java
@Deprecated

public long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Returns:** The derived gauge timestamp.

- getStringToCompare

```java
public
String
getStringToCompare()
```

Gets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** getStringToCompare

in interface

StringMonitorMBean
**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

- setStringToCompare

```java
public void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** setStringToCompare

in interface

StringMonitorMBean
**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

- getNotifyMatch

```java
public boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyMatch

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
matching the string to compare,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

- setNotifyMatch

```java
public void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyMatch

in interface

StringMonitorMBean
**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

- getNotifyDiffer

```java
public boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyDiffer

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
differing from the string to compare,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

- setNotifyDiffer

```java
public void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyDiffer

in interface

StringMonitorMBean
**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

Constructor Detail

- StringMonitor

```java
public StringMonitor()
```

Default constructor.

---

#### Constructor Detail

StringMonitor

```java
public StringMonitor()
```

Default constructor.

---

#### StringMonitor

public StringMonitor()

Default constructor.

Method Detail

- start

```java
public void start()
```

Starts the string monitor.

**Specified by:** start

in interface

MonitorMBean
**Specified by:** start

in class

Monitor

- stop

```java
public void stop()
```

Stops the string monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

- getDerivedGauge

```java
public
String
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Parameters:** object

- the name of the MBean whose derived gauge is required.
**Returns:** The derived gauge of the specified object.

- getDerivedGaugeTimeStamp

```java
public long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

- getDerivedGauge

```java
@Deprecated

public
String
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Returns:** The derived gauge.

- getDerivedGaugeTimeStamp

```java
@Deprecated

public long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Returns:** The derived gauge timestamp.

- getStringToCompare

```java
public
String
getStringToCompare()
```

Gets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** getStringToCompare

in interface

StringMonitorMBean
**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

- setStringToCompare

```java
public void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** setStringToCompare

in interface

StringMonitorMBean
**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

- getNotifyMatch

```java
public boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyMatch

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
matching the string to compare,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

- setNotifyMatch

```java
public void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyMatch

in interface

StringMonitorMBean
**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

- getNotifyDiffer

```java
public boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyDiffer

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
differing from the string to compare,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

- setNotifyDiffer

```java
public void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyDiffer

in interface

StringMonitorMBean
**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

---

#### Method Detail

start

```java
public void start()
```

Starts the string monitor.

**Specified by:** start

in interface

MonitorMBean
**Specified by:** start

in class

Monitor

---

#### start

public void start()

Starts the string monitor.

stop

```java
public void stop()
```

Stops the string monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

---

#### stop

public void stop()

Stops the string monitor.

getDerivedGauge

```java
public
String
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Parameters:** object

- the name of the MBean whose derived gauge is required.
**Returns:** The derived gauge of the specified object.

---

#### getDerivedGauge

public

String

getDerivedGauge​(

ObjectName

object)

Gets the derived gauge of the specified object, if this object is
contained in the set of observed MBeans, or

null

otherwise.

getDerivedGaugeTimeStamp

```java
public long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

---

#### getDerivedGaugeTimeStamp

public long getDerivedGaugeTimeStamp​(

ObjectName

object)

Gets the derived gauge timestamp of the specified object, if
this object is contained in the set of observed MBeans, or

0

otherwise.

getDerivedGauge

```java
@Deprecated

public
String
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

StringMonitorMBean
**Returns:** The derived gauge.

---

#### getDerivedGauge

@Deprecated

public

String

getDerivedGauge()

Returns the derived gauge of the first object in the set of
observed MBeans.

getDerivedGaugeTimeStamp

```java
@Deprecated

public long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

**Specified by:** getDerivedGaugeTimeStamp

in interface

StringMonitorMBean
**Returns:** The derived gauge timestamp.

---

#### getDerivedGaugeTimeStamp

@Deprecated

public long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

getStringToCompare

```java
public
String
getStringToCompare()
```

Gets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** getStringToCompare

in interface

StringMonitorMBean
**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

---

#### getStringToCompare

public

String

getStringToCompare()

Gets the string to compare with the observed attribute common
to all observed MBeans.

setStringToCompare

```java
public void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute common
to all observed MBeans.

**Specified by:** setStringToCompare

in interface

StringMonitorMBean
**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

---

#### setStringToCompare

public void setStringToCompare​(

String

value)
throws

IllegalArgumentException

Sets the string to compare with the observed attribute common
to all observed MBeans.

getNotifyMatch

```java
public boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyMatch

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
matching the string to compare,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

---

#### getNotifyMatch

public boolean getNotifyMatch()

Gets the matching notification's on/off switch value common to
all observed MBeans.

setNotifyMatch

```java
public void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyMatch

in interface

StringMonitorMBean
**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

---

#### setNotifyMatch

public void setNotifyMatch​(boolean value)

Sets the matching notification's on/off switch value common to
all observed MBeans.

getNotifyDiffer

```java
public boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** getNotifyDiffer

in interface

StringMonitorMBean
**Returns:** true

if the string monitor notifies when
differing from the string to compare,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

---

#### getNotifyDiffer

public boolean getNotifyDiffer()

Gets the differing notification's on/off switch value common to
all observed MBeans.

setNotifyDiffer

```java
public void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value common to
all observed MBeans.

**Specified by:** setNotifyDiffer

in interface

StringMonitorMBean
**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

---

#### setNotifyDiffer

public void setNotifyDiffer​(boolean value)

Sets the differing notification's on/off switch value common to
all observed MBeans.

getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

---

#### getNotificationInfo

public

MBeanNotificationInfo

[] getNotificationInfo()

Returns a

NotificationInfo

object containing the name of
the Java class of the notification and the notification types sent by
the string monitor.

---

