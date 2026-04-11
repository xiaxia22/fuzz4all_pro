# Class CounterMonitor

**Source:** `java.management\javax\management\monitor\CounterMonitor.html`

### Class Description

```java
public class
CounterMonitor

extends
Monitor

implements
CounterMonitorMBean
```

Defines a monitor MBean designed to observe the values of a counter
attribute.

A counter monitor sends a

threshold
notification

when the value of the counter reaches or exceeds a
threshold known as the comparison level. The notify flag must be
set to

true

.

In addition, an offset mechanism enables particular counting
intervals to be detected. If the offset value is not zero,
whenever the threshold is triggered by the counter value reaching a
comparison level, that comparison level is incremented by the
offset value. This is regarded as taking place instantaneously,
that is, before the count is incremented. Thus, for each level,
the threshold triggers an event notification every time the count
increases by an interval equal to the offset value.

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

**All Implemented Interfaces:** MBeanRegistration

,

CounterMonitorMBean

,

MonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

*No entries found.*

### Constructor Details

#### public CounterMonitor()

Default constructor.

---

### Method Details

#### public void start()

Starts the counter monitor.

**Specified by:**
- start

in interface

MonitorMBean
- start

in class

Monitor

---

#### public void stop()

Stops the counter monitor.

**Specified by:**
- stop

in interface

MonitorMBean
- stop

in class

Monitor

---

#### public
Number
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

CounterMonitorMBean

**Parameters:**
- object

- the name of the object whose derived gauge is to
be returned.

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

CounterMonitorMBean

**Parameters:**
- object

- the name of the object whose derived gauge
timestamp is to be returned.

**Returns:**
- The derived gauge timestamp of the specified object.

---

#### public
Number
getThreshold​(
ObjectName
object)

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

**Specified by:**
- getThreshold

in interface

CounterMonitorMBean

**Parameters:**
- object

- the name of the object whose threshold is to be
returned.

**Returns:**
- The threshold value of the specified object.

**See Also:**
- CounterMonitorMBean.setThreshold(java.lang.Number)

---

#### public
Number
getInitThreshold()

Gets the initial threshold value common to all observed objects.

**Specified by:**
- getInitThreshold

in interface

CounterMonitorMBean

**Returns:**
- The initial threshold.

**See Also:**
- setInitThreshold(java.lang.Number)

---

#### public void setInitThreshold​(
Number
value)
throws
IllegalArgumentException

Sets the initial threshold value common to all observed objects.

The current threshold of every object in the set of
observed MBeans is updated consequently.

**Specified by:**
- setInitThreshold

in interface

CounterMonitorMBean

**Parameters:**
- value

- The initial threshold value.

**Throws:**
- IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.

**See Also:**
- getInitThreshold()

---

#### @Deprecated

public
Number
getDerivedGauge()

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:**
- getDerivedGauge

in interface

CounterMonitorMBean

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

CounterMonitorMBean

**Returns:**
- The derived gauge timestamp.

---

#### @Deprecated

public
Number
getThreshold()

Gets the threshold value of the first object in the set of
observed MBeans.

**Specified by:**
- getThreshold

in interface

CounterMonitorMBean

**Returns:**
- The threshold value.

**See Also:**
- setThreshold(java.lang.Number)

---

#### @Deprecated

public void setThreshold​(
Number
value)
throws
IllegalArgumentException

Sets the initial threshold value.

**Specified by:**
- setThreshold

in interface

CounterMonitorMBean

**Parameters:**
- value

- The initial threshold value.

**Throws:**
- IllegalArgumentException

- The specified threshold is
null or the threshold value is less than zero.

**See Also:**
- getThreshold()

---

#### public
Number
getOffset()

Gets the offset value common to all observed MBeans.

**Specified by:**
- getOffset

in interface

CounterMonitorMBean

**Returns:**
- The offset value.

**See Also:**
- setOffset(java.lang.Number)

---

#### public void setOffset​(
Number
value)
throws
IllegalArgumentException

Sets the offset value common to all observed MBeans.

**Specified by:**
- setOffset

in interface

CounterMonitorMBean

**Parameters:**
- value

- The offset value.

**Throws:**
- IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.

**See Also:**
- getOffset()

---

#### public
Number
getModulus()

Gets the modulus value common to all observed MBeans.

**Specified by:**
- getModulus

in interface

CounterMonitorMBean

**Returns:**
- The modulus value.

**See Also:**
- setModulus(java.lang.Number)

---

#### public void setModulus​(
Number
value)
throws
IllegalArgumentException

Sets the modulus value common to all observed MBeans.

**Specified by:**
- setModulus

in interface

CounterMonitorMBean

**Parameters:**
- value

- The modulus value.

**Throws:**
- IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.

**See Also:**
- getModulus()

---

#### public boolean getNotify()

Gets the notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- getNotify

in interface

CounterMonitorMBean

**Returns:**
- true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.

**See Also:**
- setNotify(boolean)

---

#### public void setNotify​(boolean value)

Sets the notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- setNotify

in interface

CounterMonitorMBean

**Parameters:**
- value

- The notification's on/off switch value.

**See Also:**
- getNotify()

---

#### public boolean getDifferenceMode()

Gets the difference mode flag value common to all observed MBeans.

**Specified by:**
- getDifferenceMode

in interface

CounterMonitorMBean

**Returns:**
- true

if the difference mode is used,

false

otherwise.

**See Also:**
- setDifferenceMode(boolean)

---

#### public void setDifferenceMode​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

**Specified by:**
- setDifferenceMode

in interface

CounterMonitorMBean

**Parameters:**
- value

- The difference mode flag value.

**See Also:**
- getDifferenceMode()

---

#### public
MBeanNotificationInfo
[] getNotificationInfo()

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- the array of possible notifications.

---

### Additional Sections

#### Class CounterMonitor

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.monitor.Monitor
- - javax.management.monitor.CounterMonitor

javax.management.NotificationBroadcasterSupport

- javax.management.monitor.Monitor
- - javax.management.monitor.CounterMonitor

javax.management.monitor.Monitor

- javax.management.monitor.CounterMonitor

javax.management.monitor.CounterMonitor

**All Implemented Interfaces:** MBeanRegistration

,

CounterMonitorMBean

,

MonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

```java
public class
CounterMonitor

extends
Monitor

implements
CounterMonitorMBean
```

Defines a monitor MBean designed to observe the values of a counter
attribute.

A counter monitor sends a

threshold
notification

when the value of the counter reaches or exceeds a
threshold known as the comparison level. The notify flag must be
set to

true

.

In addition, an offset mechanism enables particular counting
intervals to be detected. If the offset value is not zero,
whenever the threshold is triggered by the counter value reaching a
comparison level, that comparison level is incremented by the
offset value. This is regarded as taking place instantaneously,
that is, before the count is incremented. Thus, for each level,
the threshold triggers an event notification every time the count
increases by an interval equal to the offset value.

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

**Since:** 1.5

public class

CounterMonitor

extends

Monitor

implements

CounterMonitorMBean

Defines a monitor MBean designed to observe the values of a counter
attribute.

A counter monitor sends a

threshold
notification

when the value of the counter reaches or exceeds a
threshold known as the comparison level. The notify flag must be
set to

true

.

In addition, an offset mechanism enables particular counting
intervals to be detected. If the offset value is not zero,
whenever the threshold is triggered by the counter value reaching a
comparison level, that comparison level is incremented by the
offset value. This is regarded as taking place instantaneously,
that is, before the count is incremented. Thus, for each level,
the threshold triggers an event notification every time the count
increases by an interval equal to the offset value.

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

A counter monitor sends a

threshold
notification

when the value of the counter reaches or exceeds a
threshold known as the comparison level. The notify flag must be
set to

true

.

In addition, an offset mechanism enables particular counting
intervals to be detected. If the offset value is not zero,
whenever the threshold is triggered by the counter value reaching a
comparison level, that comparison level is incremented by the
offset value. This is regarded as taking place instantaneously,
that is, before the count is incremented. Thus, for each level,
the threshold triggers an event notification every time the count
increases by an interval equal to the offset value.

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

In addition, an offset mechanism enables particular counting
intervals to be detected. If the offset value is not zero,
whenever the threshold is triggered by the counter value reaching a
comparison level, that comparison level is incremented by the
offset value. This is regarded as taking place instantaneously,
that is, before the count is incremented. Thus, for each level,
the threshold triggers an event notification every time the count
increases by an interval equal to the offset value.

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

If the counter can wrap around its maximum value, the modulus
needs to be specified. The modulus is the value at which the
counter is reset to zero.

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

If the counter difference mode is used, the value of the
derived gauge is calculated as the difference between the observed
counter values for two successive observations. If this difference
is negative, the value of the derived gauge is incremented by the
value of the modulus. The derived gauge value (V[t]) is calculated
using the following method:

- if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

This implementation of the counter monitor requires the observed
attribute to be of the type integer (

Byte

,

Integer

,

Short

,

Long

).

if (counter[t] - counter[t-GP]) is positive then
V[t] = counter[t] - counter[t-GP]

if (counter[t] - counter[t-GP]) is negative then
V[t] = counter[t] - counter[t-GP] + MODULUS

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

CounterMonitor

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

Number

getDerivedGauge

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Number

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

boolean

getDifferenceMode

()

Gets the difference mode flag value common to all observed MBeans.

Number

getInitThreshold

()

Gets the initial threshold value common to all observed objects.

Number

getModulus

()

Gets the modulus value common to all observed MBeans.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

boolean

getNotify

()

Gets the notification's on/off switch value common to all
observed MBeans.

Number

getOffset

()

Gets the offset value common to all observed MBeans.

Number

getThreshold

()

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Number

getThreshold

​(

ObjectName

object)

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

void

setInitThreshold

​(

Number

value)

Sets the initial threshold value common to all observed objects.

void

setModulus

​(

Number

value)

Sets the modulus value common to all observed MBeans.

void

setNotify

​(boolean value)

Sets the notification's on/off switch value common to all
observed MBeans.

void

setOffset

​(

Number

value)

Sets the offset value common to all observed MBeans.

void

setThreshold

​(

Number

value)

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

void

start

()

Starts the counter monitor.

void

stop

()

Stops the counter monitor.

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

CounterMonitor

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

Number

getDerivedGauge

()

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Number

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

boolean

getDifferenceMode

()

Gets the difference mode flag value common to all observed MBeans.

Number

getInitThreshold

()

Gets the initial threshold value common to all observed objects.

Number

getModulus

()

Gets the modulus value common to all observed MBeans.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

boolean

getNotify

()

Gets the notification's on/off switch value common to all
observed MBeans.

Number

getOffset

()

Gets the offset value common to all observed MBeans.

Number

getThreshold

()

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Number

getThreshold

​(

ObjectName

object)

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

void

setInitThreshold

​(

Number

value)

Sets the initial threshold value common to all observed objects.

void

setModulus

​(

Number

value)

Sets the modulus value common to all observed MBeans.

void

setNotify

​(boolean value)

Sets the notification's on/off switch value common to all
observed MBeans.

void

setOffset

​(

Number

value)

Sets the offset value common to all observed MBeans.

void

setThreshold

​(

Number

value)

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

void

start

()

Starts the counter monitor.

void

stop

()

Stops the counter monitor.

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

Gets the difference mode flag value common to all observed MBeans.

Gets the initial threshold value common to all observed objects.

Gets the modulus value common to all observed MBeans.

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

Gets the notification's on/off switch value common to all
observed MBeans.

Gets the offset value common to all observed MBeans.

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

Sets the difference mode flag value common to all observed MBeans.

Sets the initial threshold value common to all observed objects.

Sets the modulus value common to all observed MBeans.

Sets the notification's on/off switch value common to all
observed MBeans.

Sets the offset value common to all observed MBeans.

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Starts the counter monitor.

Stops the counter monitor.

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

- CounterMonitor

```java
public CounterMonitor()
```

Default constructor.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
public void start()
```

Starts the counter monitor.

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

Stops the counter monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

- getDerivedGauge

```java
public
Number
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

CounterMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge is to
be returned.
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

CounterMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

- getThreshold

```java
public
Number
getThreshold​(
ObjectName
object)
```

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Parameters:** object

- the name of the object whose threshold is to be
returned.
**Returns:** The threshold value of the specified object.
**See Also:** CounterMonitorMBean.setThreshold(java.lang.Number)

- getInitThreshold

```java
public
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Specified by:** getInitThreshold

in interface

CounterMonitorMBean
**Returns:** The initial threshold.
**See Also:** setInitThreshold(java.lang.Number)

- setInitThreshold

```java
public void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed objects.

The current threshold of every object in the set of
observed MBeans is updated consequently.

**Specified by:** setInitThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

- getDerivedGauge

```java
@Deprecated

public
Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

CounterMonitorMBean
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

CounterMonitorMBean
**Returns:** The derived gauge timestamp.

- getThreshold

```java
@Deprecated

public
Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value of the first object in the set of
observed MBeans.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Returns:** The threshold value.
**See Also:** setThreshold(java.lang.Number)

- setThreshold

```java
@Deprecated

public void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the initial threshold value.

**Specified by:** setThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is
null or the threshold value is less than zero.
**See Also:** getThreshold()

- getOffset

```java
public
Number
getOffset()
```

Gets the offset value common to all observed MBeans.

**Specified by:** getOffset

in interface

CounterMonitorMBean
**Returns:** The offset value.
**See Also:** setOffset(java.lang.Number)

- setOffset

```java
public void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value common to all observed MBeans.

**Specified by:** setOffset

in interface

CounterMonitorMBean
**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

- getModulus

```java
public
Number
getModulus()
```

Gets the modulus value common to all observed MBeans.

**Specified by:** getModulus

in interface

CounterMonitorMBean
**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

- setModulus

```java
public void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value common to all observed MBeans.

**Specified by:** setModulus

in interface

CounterMonitorMBean
**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

- getNotify

```java
public boolean getNotify()
```

Gets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotify

in interface

CounterMonitorMBean
**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

- setNotify

```java
public void setNotify​(boolean value)
```

Sets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotify

in interface

CounterMonitorMBean
**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

- getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

CounterMonitorMBean
**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

- setDifferenceMode

```java
public void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value common to all observed MBeans.

**Specified by:** setDifferenceMode

in interface

CounterMonitorMBean
**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

Constructor Detail

- CounterMonitor

```java
public CounterMonitor()
```

Default constructor.

---

#### Constructor Detail

CounterMonitor

```java
public CounterMonitor()
```

Default constructor.

---

#### CounterMonitor

public CounterMonitor()

Default constructor.

Method Detail

- start

```java
public void start()
```

Starts the counter monitor.

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

Stops the counter monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

- getDerivedGauge

```java
public
Number
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

CounterMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge is to
be returned.
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

CounterMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

- getThreshold

```java
public
Number
getThreshold​(
ObjectName
object)
```

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Parameters:** object

- the name of the object whose threshold is to be
returned.
**Returns:** The threshold value of the specified object.
**See Also:** CounterMonitorMBean.setThreshold(java.lang.Number)

- getInitThreshold

```java
public
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Specified by:** getInitThreshold

in interface

CounterMonitorMBean
**Returns:** The initial threshold.
**See Also:** setInitThreshold(java.lang.Number)

- setInitThreshold

```java
public void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed objects.

The current threshold of every object in the set of
observed MBeans is updated consequently.

**Specified by:** setInitThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

- getDerivedGauge

```java
@Deprecated

public
Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

CounterMonitorMBean
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

CounterMonitorMBean
**Returns:** The derived gauge timestamp.

- getThreshold

```java
@Deprecated

public
Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value of the first object in the set of
observed MBeans.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Returns:** The threshold value.
**See Also:** setThreshold(java.lang.Number)

- setThreshold

```java
@Deprecated

public void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the initial threshold value.

**Specified by:** setThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is
null or the threshold value is less than zero.
**See Also:** getThreshold()

- getOffset

```java
public
Number
getOffset()
```

Gets the offset value common to all observed MBeans.

**Specified by:** getOffset

in interface

CounterMonitorMBean
**Returns:** The offset value.
**See Also:** setOffset(java.lang.Number)

- setOffset

```java
public void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value common to all observed MBeans.

**Specified by:** setOffset

in interface

CounterMonitorMBean
**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

- getModulus

```java
public
Number
getModulus()
```

Gets the modulus value common to all observed MBeans.

**Specified by:** getModulus

in interface

CounterMonitorMBean
**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

- setModulus

```java
public void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value common to all observed MBeans.

**Specified by:** setModulus

in interface

CounterMonitorMBean
**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

- getNotify

```java
public boolean getNotify()
```

Gets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotify

in interface

CounterMonitorMBean
**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

- setNotify

```java
public void setNotify​(boolean value)
```

Sets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotify

in interface

CounterMonitorMBean
**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

- getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

CounterMonitorMBean
**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

- setDifferenceMode

```java
public void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value common to all observed MBeans.

**Specified by:** setDifferenceMode

in interface

CounterMonitorMBean
**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

- getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

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

Starts the counter monitor.

**Specified by:** start

in interface

MonitorMBean
**Specified by:** start

in class

Monitor

---

#### start

public void start()

Starts the counter monitor.

stop

```java
public void stop()
```

Stops the counter monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

---

#### stop

public void stop()

Stops the counter monitor.

getDerivedGauge

```java
public
Number
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

CounterMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge is to
be returned.
**Returns:** The derived gauge of the specified object.

---

#### getDerivedGauge

public

Number

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

CounterMonitorMBean
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

getThreshold

```java
public
Number
getThreshold​(
ObjectName
object)
```

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Parameters:** object

- the name of the object whose threshold is to be
returned.
**Returns:** The threshold value of the specified object.
**See Also:** CounterMonitorMBean.setThreshold(java.lang.Number)

---

#### getThreshold

public

Number

getThreshold​(

ObjectName

object)

Gets the current threshold value of the specified object, if
this object is contained in the set of observed MBeans, or

null

otherwise.

getInitThreshold

```java
public
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Specified by:** getInitThreshold

in interface

CounterMonitorMBean
**Returns:** The initial threshold.
**See Also:** setInitThreshold(java.lang.Number)

---

#### getInitThreshold

public

Number

getInitThreshold()

Gets the initial threshold value common to all observed objects.

setInitThreshold

```java
public void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed objects.

The current threshold of every object in the set of
observed MBeans is updated consequently.

**Specified by:** setInitThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

---

#### setInitThreshold

public void setInitThreshold​(

Number

value)
throws

IllegalArgumentException

Sets the initial threshold value common to all observed objects.

The current threshold of every object in the set of
observed MBeans is updated consequently.

getDerivedGauge

```java
@Deprecated

public
Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Returns the derived gauge of the first object in the set of
observed MBeans.

**Specified by:** getDerivedGauge

in interface

CounterMonitorMBean
**Returns:** The derived gauge.

---

#### getDerivedGauge

@Deprecated

public

Number

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

CounterMonitorMBean
**Returns:** The derived gauge timestamp.

---

#### getDerivedGaugeTimeStamp

@Deprecated

public long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

getThreshold

```java
@Deprecated

public
Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value of the first object in the set of
observed MBeans.

**Specified by:** getThreshold

in interface

CounterMonitorMBean
**Returns:** The threshold value.
**See Also:** setThreshold(java.lang.Number)

---

#### getThreshold

@Deprecated

public

Number

getThreshold()

Gets the threshold value of the first object in the set of
observed MBeans.

setThreshold

```java
@Deprecated

public void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the initial threshold value.

**Specified by:** setThreshold

in interface

CounterMonitorMBean
**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is
null or the threshold value is less than zero.
**See Also:** getThreshold()

---

#### setThreshold

@Deprecated

public void setThreshold​(

Number

value)
throws

IllegalArgumentException

Sets the initial threshold value.

getOffset

```java
public
Number
getOffset()
```

Gets the offset value common to all observed MBeans.

**Specified by:** getOffset

in interface

CounterMonitorMBean
**Returns:** The offset value.
**See Also:** setOffset(java.lang.Number)

---

#### getOffset

public

Number

getOffset()

Gets the offset value common to all observed MBeans.

setOffset

```java
public void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value common to all observed MBeans.

**Specified by:** setOffset

in interface

CounterMonitorMBean
**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

---

#### setOffset

public void setOffset​(

Number

value)
throws

IllegalArgumentException

Sets the offset value common to all observed MBeans.

getModulus

```java
public
Number
getModulus()
```

Gets the modulus value common to all observed MBeans.

**Specified by:** getModulus

in interface

CounterMonitorMBean
**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

---

#### getModulus

public

Number

getModulus()

Gets the modulus value common to all observed MBeans.

setModulus

```java
public void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value common to all observed MBeans.

**Specified by:** setModulus

in interface

CounterMonitorMBean
**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

---

#### setModulus

public void setModulus​(

Number

value)
throws

IllegalArgumentException

Sets the modulus value common to all observed MBeans.

getNotify

```java
public boolean getNotify()
```

Gets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotify

in interface

CounterMonitorMBean
**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

---

#### getNotify

public boolean getNotify()

Gets the notification's on/off switch value common to all
observed MBeans.

setNotify

```java
public void setNotify​(boolean value)
```

Sets the notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotify

in interface

CounterMonitorMBean
**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

---

#### setNotify

public void setNotify​(boolean value)

Sets the notification's on/off switch value common to all
observed MBeans.

getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

CounterMonitorMBean
**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

---

#### getDifferenceMode

public boolean getDifferenceMode()

Gets the difference mode flag value common to all observed MBeans.

setDifferenceMode

```java
public void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value common to all observed MBeans.

**Specified by:** setDifferenceMode

in interface

CounterMonitorMBean
**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

---

#### setDifferenceMode

public void setDifferenceMode​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

getNotificationInfo

```java
public
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

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

object containing the
name of the Java class of the notification and the notification
types sent by the counter monitor.

---

