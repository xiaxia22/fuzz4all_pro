# Class GaugeMonitor

**Source:** `java.management\javax\management\monitor\GaugeMonitor.html`

### Class Description

```java
public class
GaugeMonitor

extends
Monitor

implements
GaugeMonitorMBean
```

Defines a monitor MBean designed to observe the values of a gauge attribute.

A gauge monitor observes an attribute that is continuously
variable with time. A gauge monitor sends notifications as
follows:

- if the attribute value is increasing and becomes equal to or
greater than the high threshold value, a

threshold high
notification

is sent. The notify high flag must be set to

true

.

Subsequent crossings of the high threshold value do not cause
further notifications unless the attribute value becomes equal to
or less than the low threshold value.
- if the attribute value is decreasing and becomes equal to or
less than the low threshold value, a

threshold low
notification

is sent. The notify low flag must be set to

true

.

Subsequent crossings of the low threshold value do not cause
further notifications unless the attribute value becomes equal to
or greater than the high threshold value.

This provides a hysteresis mechanism to avoid repeated triggering
of notifications when the attribute value makes small oscillations
around the high or low threshold value.

If the gauge difference mode is used, the value of the derived
gauge is calculated as the difference between the observed gauge
values for two successive observations.

The derived gauge value (V[t]) is calculated using the following method:

- V[t] = gauge[t] - gauge[t-GP]

This implementation of the gauge monitor requires the observed
attribute to be of the type integer or floating-point
(

Byte

,

Integer

,

Short

,

Long

,

Float

,

Double

).

**All Implemented Interfaces:** MBeanRegistration

,

GaugeMonitorMBean

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

#### public GaugeMonitor()

Default constructor.

---

### Method Details

#### public void start()

Starts the gauge monitor.

**Specified by:**
- start

in interface

MonitorMBean
- start

in class

Monitor

---

#### public void stop()

Stops the gauge monitor.

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

GaugeMonitorMBean

**Parameters:**
- object

- the name of the MBean.

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

GaugeMonitorMBean

**Parameters:**
- object

- the name of the object whose derived gauge
timestamp is to be returned.

**Returns:**
- The derived gauge timestamp of the specified object.

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

GaugeMonitorMBean

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

GaugeMonitorMBean

**Returns:**
- The derived gauge timestamp.

---

#### public
Number
getHighThreshold()

Gets the high threshold value common to all observed MBeans.

**Specified by:**
- getHighThreshold

in interface

GaugeMonitorMBean

**Returns:**
- The high threshold value.

**See Also:**
- setThresholds(java.lang.Number, java.lang.Number)

---

#### public
Number
getLowThreshold()

Gets the low threshold value common to all observed MBeans.

**Specified by:**
- getLowThreshold

in interface

GaugeMonitorMBean

**Returns:**
- The low threshold value.

**See Also:**
- setThresholds(java.lang.Number, java.lang.Number)

---

#### public void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException

Sets the high and the low threshold values common to all
observed MBeans.

**Specified by:**
- setThresholds

in interface

GaugeMonitorMBean

**Parameters:**
- highValue

- The high threshold value.
- lowValue

- The low threshold value.

**Throws:**
- IllegalArgumentException

- The specified high/low
threshold is null or the low threshold is greater than the high
threshold or the high threshold and the low threshold are not
of the same type.

**See Also:**
- getHighThreshold()

,

getLowThreshold()

---

#### public boolean getNotifyHigh()

Gets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- getNotifyHigh

in interface

GaugeMonitorMBean

**Returns:**
- true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.

**See Also:**
- setNotifyHigh(boolean)

---

#### public void setNotifyHigh​(boolean value)

Sets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- setNotifyHigh

in interface

GaugeMonitorMBean

**Parameters:**
- value

- The high notification's on/off switch value.

**See Also:**
- getNotifyHigh()

---

#### public boolean getNotifyLow()

Gets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- getNotifyLow

in interface

GaugeMonitorMBean

**Returns:**
- true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.

**See Also:**
- setNotifyLow(boolean)

---

#### public void setNotifyLow​(boolean value)

Sets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:**
- setNotifyLow

in interface

GaugeMonitorMBean

**Parameters:**
- value

- The low notification's on/off switch value.

**See Also:**
- getNotifyLow()

---

#### public boolean getDifferenceMode()

Gets the difference mode flag value common to all observed MBeans.

**Specified by:**
- getDifferenceMode

in interface

GaugeMonitorMBean

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

GaugeMonitorMBean

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
types sent by the gauge monitor.

**Specified by:**
- getNotificationInfo

in interface

NotificationBroadcaster

**Returns:**
- the array of possible notifications.

---

### Additional Sections

#### Class GaugeMonitor

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.monitor.Monitor
- - javax.management.monitor.GaugeMonitor

javax.management.NotificationBroadcasterSupport

- javax.management.monitor.Monitor
- - javax.management.monitor.GaugeMonitor

javax.management.monitor.Monitor

- javax.management.monitor.GaugeMonitor

javax.management.monitor.GaugeMonitor

**All Implemented Interfaces:** MBeanRegistration

,

GaugeMonitorMBean

,

MonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

```java
public class
GaugeMonitor

extends
Monitor

implements
GaugeMonitorMBean
```

Defines a monitor MBean designed to observe the values of a gauge attribute.

A gauge monitor observes an attribute that is continuously
variable with time. A gauge monitor sends notifications as
follows:

- if the attribute value is increasing and becomes equal to or
greater than the high threshold value, a

threshold high
notification

is sent. The notify high flag must be set to

true

.

Subsequent crossings of the high threshold value do not cause
further notifications unless the attribute value becomes equal to
or less than the low threshold value.
- if the attribute value is decreasing and becomes equal to or
less than the low threshold value, a

threshold low
notification

is sent. The notify low flag must be set to

true

.

Subsequent crossings of the low threshold value do not cause
further notifications unless the attribute value becomes equal to
or greater than the high threshold value.

This provides a hysteresis mechanism to avoid repeated triggering
of notifications when the attribute value makes small oscillations
around the high or low threshold value.

If the gauge difference mode is used, the value of the derived
gauge is calculated as the difference between the observed gauge
values for two successive observations.

The derived gauge value (V[t]) is calculated using the following method:

- V[t] = gauge[t] - gauge[t-GP]

This implementation of the gauge monitor requires the observed
attribute to be of the type integer or floating-point
(

Byte

,

Integer

,

Short

,

Long

,

Float

,

Double

).

**Since:** 1.5

public class

GaugeMonitor

extends

Monitor

implements

GaugeMonitorMBean

Defines a monitor MBean designed to observe the values of a gauge attribute.

A gauge monitor observes an attribute that is continuously
variable with time. A gauge monitor sends notifications as
follows:

- if the attribute value is increasing and becomes equal to or
greater than the high threshold value, a

threshold high
notification

is sent. The notify high flag must be set to

true

.

Subsequent crossings of the high threshold value do not cause
further notifications unless the attribute value becomes equal to
or less than the low threshold value.
- if the attribute value is decreasing and becomes equal to or
less than the low threshold value, a

threshold low
notification

is sent. The notify low flag must be set to

true

.

Subsequent crossings of the low threshold value do not cause
further notifications unless the attribute value becomes equal to
or greater than the high threshold value.

This provides a hysteresis mechanism to avoid repeated triggering
of notifications when the attribute value makes small oscillations
around the high or low threshold value.

If the gauge difference mode is used, the value of the derived
gauge is calculated as the difference between the observed gauge
values for two successive observations.

The derived gauge value (V[t]) is calculated using the following method:

- V[t] = gauge[t] - gauge[t-GP]

This implementation of the gauge monitor requires the observed
attribute to be of the type integer or floating-point
(

Byte

,

Integer

,

Short

,

Long

,

Float

,

Double

).

A gauge monitor observes an attribute that is continuously
variable with time. A gauge monitor sends notifications as
follows:

- if the attribute value is increasing and becomes equal to or
greater than the high threshold value, a

threshold high
notification

is sent. The notify high flag must be set to

true

.

Subsequent crossings of the high threshold value do not cause
further notifications unless the attribute value becomes equal to
or less than the low threshold value.
- if the attribute value is decreasing and becomes equal to or
less than the low threshold value, a

threshold low
notification

is sent. The notify low flag must be set to

true

.

Subsequent crossings of the low threshold value do not cause
further notifications unless the attribute value becomes equal to
or greater than the high threshold value.

This provides a hysteresis mechanism to avoid repeated triggering
of notifications when the attribute value makes small oscillations
around the high or low threshold value.

If the gauge difference mode is used, the value of the derived
gauge is calculated as the difference between the observed gauge
values for two successive observations.

The derived gauge value (V[t]) is calculated using the following method:

- V[t] = gauge[t] - gauge[t-GP]

This implementation of the gauge monitor requires the observed
attribute to be of the type integer or floating-point
(

Byte

,

Integer

,

Short

,

Long

,

Float

,

Double

).

if the attribute value is increasing and becomes equal to or
greater than the high threshold value, a

threshold high
notification

is sent. The notify high flag must be set to

true

.

Subsequent crossings of the high threshold value do not cause
further notifications unless the attribute value becomes equal to
or less than the low threshold value.

if the attribute value is decreasing and becomes equal to or
less than the low threshold value, a

threshold low
notification

is sent. The notify low flag must be set to

true

.

Subsequent crossings of the low threshold value do not cause
further notifications unless the attribute value becomes equal to
or greater than the high threshold value.

If the gauge difference mode is used, the value of the derived
gauge is calculated as the difference between the observed gauge
values for two successive observations.

The derived gauge value (V[t]) is calculated using the following method:

- V[t] = gauge[t] - gauge[t-GP]

This implementation of the gauge monitor requires the observed
attribute to be of the type integer or floating-point
(

Byte

,

Integer

,

Short

,

Long

,

Float

,

Double

).

V[t] = gauge[t] - gauge[t-GP]

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

GaugeMonitor

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

getHighThreshold

()

Gets the high threshold value common to all observed MBeans.

Number

getLowThreshold

()

Gets the low threshold value common to all observed MBeans.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the gauge monitor.

boolean

getNotifyHigh

()

Gets the high notification's on/off switch value common to all
observed MBeans.

boolean

getNotifyLow

()

Gets the low notification's on/off switch value common to all
observed MBeans.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

void

setNotifyHigh

​(boolean value)

Sets the high notification's on/off switch value common to all
observed MBeans.

void

setNotifyLow

​(boolean value)

Sets the low notification's on/off switch value common to all
observed MBeans.

void

setThresholds

​(

Number

highValue,

Number

lowValue)

Sets the high and the low threshold values common to all
observed MBeans.

void

start

()

Starts the gauge monitor.

void

stop

()

Stops the gauge monitor.

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

GaugeMonitor

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

getHighThreshold

()

Gets the high threshold value common to all observed MBeans.

Number

getLowThreshold

()

Gets the low threshold value common to all observed MBeans.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the gauge monitor.

boolean

getNotifyHigh

()

Gets the high notification's on/off switch value common to all
observed MBeans.

boolean

getNotifyLow

()

Gets the low notification's on/off switch value common to all
observed MBeans.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value common to all observed MBeans.

void

setNotifyHigh

​(boolean value)

Sets the high notification's on/off switch value common to all
observed MBeans.

void

setNotifyLow

​(boolean value)

Sets the low notification's on/off switch value common to all
observed MBeans.

void

setThresholds

​(

Number

highValue,

Number

lowValue)

Sets the high and the low threshold values common to all
observed MBeans.

void

start

()

Starts the gauge monitor.

void

stop

()

Stops the gauge monitor.

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

Gets the high threshold value common to all observed MBeans.

Gets the low threshold value common to all observed MBeans.

Returns a

NotificationInfo

object containing the
name of the Java class of the notification and the notification
types sent by the gauge monitor.

Gets the high notification's on/off switch value common to all
observed MBeans.

Gets the low notification's on/off switch value common to all
observed MBeans.

Sets the difference mode flag value common to all observed MBeans.

Sets the high notification's on/off switch value common to all
observed MBeans.

Sets the low notification's on/off switch value common to all
observed MBeans.

Sets the high and the low threshold values common to all
observed MBeans.

Starts the gauge monitor.

Stops the gauge monitor.

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

- GaugeMonitor

```java
public GaugeMonitor()
```

Default constructor.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
public void start()
```

Starts the gauge monitor.

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

Stops the gauge monitor.

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

GaugeMonitorMBean
**Parameters:** object

- the name of the MBean.
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

GaugeMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

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

GaugeMonitorMBean
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

GaugeMonitorMBean
**Returns:** The derived gauge timestamp.

- getHighThreshold

```java
public
Number
getHighThreshold()
```

Gets the high threshold value common to all observed MBeans.

**Specified by:** getHighThreshold

in interface

GaugeMonitorMBean
**Returns:** The high threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

- getLowThreshold

```java
public
Number
getLowThreshold()
```

Gets the low threshold value common to all observed MBeans.

**Specified by:** getLowThreshold

in interface

GaugeMonitorMBean
**Returns:** The low threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

- setThresholds

```java
public void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values common to all
observed MBeans.

**Specified by:** setThresholds

in interface

GaugeMonitorMBean
**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low
threshold is null or the low threshold is greater than the high
threshold or the high threshold and the low threshold are not
of the same type.
**See Also:** getHighThreshold()

,

getLowThreshold()

- getNotifyHigh

```java
public boolean getNotifyHigh()
```

Gets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyHigh

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

- setNotifyHigh

```java
public void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyHigh

in interface

GaugeMonitorMBean
**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

- getNotifyLow

```java
public boolean getNotifyLow()
```

Gets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyLow

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

- setNotifyLow

```java
public void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyLow

in interface

GaugeMonitorMBean
**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

- getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

GaugeMonitorMBean
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

GaugeMonitorMBean
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
types sent by the gauge monitor.

**Specified by:** getNotificationInfo

in interface

NotificationBroadcaster
**Returns:** the array of possible notifications.

Constructor Detail

- GaugeMonitor

```java
public GaugeMonitor()
```

Default constructor.

---

#### Constructor Detail

GaugeMonitor

```java
public GaugeMonitor()
```

Default constructor.

---

#### GaugeMonitor

public GaugeMonitor()

Default constructor.

Method Detail

- start

```java
public void start()
```

Starts the gauge monitor.

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

Stops the gauge monitor.

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

GaugeMonitorMBean
**Parameters:** object

- the name of the MBean.
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

GaugeMonitorMBean
**Parameters:** object

- the name of the object whose derived gauge
timestamp is to be returned.
**Returns:** The derived gauge timestamp of the specified object.

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

GaugeMonitorMBean
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

GaugeMonitorMBean
**Returns:** The derived gauge timestamp.

- getHighThreshold

```java
public
Number
getHighThreshold()
```

Gets the high threshold value common to all observed MBeans.

**Specified by:** getHighThreshold

in interface

GaugeMonitorMBean
**Returns:** The high threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

- getLowThreshold

```java
public
Number
getLowThreshold()
```

Gets the low threshold value common to all observed MBeans.

**Specified by:** getLowThreshold

in interface

GaugeMonitorMBean
**Returns:** The low threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

- setThresholds

```java
public void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values common to all
observed MBeans.

**Specified by:** setThresholds

in interface

GaugeMonitorMBean
**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low
threshold is null or the low threshold is greater than the high
threshold or the high threshold and the low threshold are not
of the same type.
**See Also:** getHighThreshold()

,

getLowThreshold()

- getNotifyHigh

```java
public boolean getNotifyHigh()
```

Gets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyHigh

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

- setNotifyHigh

```java
public void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyHigh

in interface

GaugeMonitorMBean
**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

- getNotifyLow

```java
public boolean getNotifyLow()
```

Gets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyLow

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

- setNotifyLow

```java
public void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyLow

in interface

GaugeMonitorMBean
**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

- getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

GaugeMonitorMBean
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

GaugeMonitorMBean
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
types sent by the gauge monitor.

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

Starts the gauge monitor.

**Specified by:** start

in interface

MonitorMBean
**Specified by:** start

in class

Monitor

---

#### start

public void start()

Starts the gauge monitor.

stop

```java
public void stop()
```

Stops the gauge monitor.

**Specified by:** stop

in interface

MonitorMBean
**Specified by:** stop

in class

Monitor

---

#### stop

public void stop()

Stops the gauge monitor.

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

GaugeMonitorMBean
**Parameters:** object

- the name of the MBean.
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

GaugeMonitorMBean
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

GaugeMonitorMBean
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

GaugeMonitorMBean
**Returns:** The derived gauge timestamp.

---

#### getDerivedGaugeTimeStamp

@Deprecated

public long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp of the first object in the set
of observed MBeans.

getHighThreshold

```java
public
Number
getHighThreshold()
```

Gets the high threshold value common to all observed MBeans.

**Specified by:** getHighThreshold

in interface

GaugeMonitorMBean
**Returns:** The high threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

---

#### getHighThreshold

public

Number

getHighThreshold()

Gets the high threshold value common to all observed MBeans.

getLowThreshold

```java
public
Number
getLowThreshold()
```

Gets the low threshold value common to all observed MBeans.

**Specified by:** getLowThreshold

in interface

GaugeMonitorMBean
**Returns:** The low threshold value.
**See Also:** setThresholds(java.lang.Number, java.lang.Number)

---

#### getLowThreshold

public

Number

getLowThreshold()

Gets the low threshold value common to all observed MBeans.

setThresholds

```java
public void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values common to all
observed MBeans.

**Specified by:** setThresholds

in interface

GaugeMonitorMBean
**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low
threshold is null or the low threshold is greater than the high
threshold or the high threshold and the low threshold are not
of the same type.
**See Also:** getHighThreshold()

,

getLowThreshold()

---

#### setThresholds

public void setThresholds​(

Number

highValue,

Number

lowValue)
throws

IllegalArgumentException

Sets the high and the low threshold values common to all
observed MBeans.

getNotifyHigh

```java
public boolean getNotifyHigh()
```

Gets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyHigh

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

---

#### getNotifyHigh

public boolean getNotifyHigh()

Gets the high notification's on/off switch value common to all
observed MBeans.

setNotifyHigh

```java
public void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyHigh

in interface

GaugeMonitorMBean
**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

---

#### setNotifyHigh

public void setNotifyHigh​(boolean value)

Sets the high notification's on/off switch value common to all
observed MBeans.

getNotifyLow

```java
public boolean getNotifyLow()
```

Gets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** getNotifyLow

in interface

GaugeMonitorMBean
**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

---

#### getNotifyLow

public boolean getNotifyLow()

Gets the low notification's on/off switch value common to all
observed MBeans.

setNotifyLow

```java
public void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value common to all
observed MBeans.

**Specified by:** setNotifyLow

in interface

GaugeMonitorMBean
**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

---

#### setNotifyLow

public void setNotifyLow​(boolean value)

Sets the low notification's on/off switch value common to all
observed MBeans.

getDifferenceMode

```java
public boolean getDifferenceMode()
```

Gets the difference mode flag value common to all observed MBeans.

**Specified by:** getDifferenceMode

in interface

GaugeMonitorMBean
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

GaugeMonitorMBean
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
types sent by the gauge monitor.

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
types sent by the gauge monitor.

---

