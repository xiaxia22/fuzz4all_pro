# Class MonitorNotification

**Source:** `java.management\javax\management\monitor\MonitorNotification.html`

### Class Description

```java
public class
MonitorNotification

extends
Notification
```

Provides definitions of the notifications sent by monitor MBeans.

The notification source and a set of parameters concerning the monitor MBean's state
need to be specified when creating a new object of this class.

The list of notifications fired by the monitor MBeans is the following:

- Common to all kind of monitors:

- The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

Common to the counter and the gauge monitors:

- The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

Counter monitors only:

- The observed attribute has reached the threshold value.

Gauge monitors only:

- The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

String monitors only:

- The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final
String
OBSERVED_OBJECT_ERROR

Notification type denoting that the observed object is not registered in the MBean server.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.mbean

.

**See Also:**
- Constant Field Values

---

#### public static final
String
OBSERVED_ATTRIBUTE_ERROR

Notification type denoting that the observed attribute is not contained in the observed object.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.attribute

.

**See Also:**
- Constant Field Values

---

#### public static final
String
OBSERVED_ATTRIBUTE_TYPE_ERROR

Notification type denoting that the type of the observed attribute is not correct.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.type

.

**See Also:**
- Constant Field Values

---

#### public static final
String
THRESHOLD_ERROR

Notification type denoting that the type of the thresholds, offset or modulus is not correct.
This notification is fired by counter and gauge monitors.

The value of this notification type is

jmx.monitor.error.threshold

.

**See Also:**
- Constant Field Values

---

#### public static final
String
RUNTIME_ERROR

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.runtime

.

**See Also:**
- Constant Field Values

---

#### public static final
String
THRESHOLD_VALUE_EXCEEDED

Notification type denoting that the observed attribute has reached the threshold value.
This notification is only fired by counter monitors.

The value of this notification type is

jmx.monitor.counter.threshold

.

**See Also:**
- Constant Field Values

---

#### public static final
String
THRESHOLD_HIGH_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold high value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.high

.

**See Also:**
- Constant Field Values

---

#### public static final
String
THRESHOLD_LOW_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold low value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.low

.

**See Also:**
- Constant Field Values

---

#### public static final
String
STRING_TO_COMPARE_VALUE_MATCHED

Notification type denoting that the observed attribute has matched the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.matches

.

**See Also:**
- Constant Field Values

---

#### public static final
String
STRING_TO_COMPARE_VALUE_DIFFERED

Notification type denoting that the observed attribute has differed from the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.differs

.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public
ObjectName
getObservedObject()

Gets the observed object of this monitor notification.

**Returns:**
- The observed object.

---

#### public
String
getObservedAttribute()

Gets the observed attribute of this monitor notification.

**Returns:**
- The observed attribute.

---

#### public
Object
getDerivedGauge()

Gets the derived gauge of this monitor notification.

**Returns:**
- The derived gauge.

---

#### public
Object
getTrigger()

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

**Returns:**
- The trigger.

---

### Additional Sections

#### Class MonitorNotification

java.lang.Object

- java.util.EventObject
- - javax.management.Notification
- - javax.management.monitor.MonitorNotification

java.util.EventObject

- javax.management.Notification
- - javax.management.monitor.MonitorNotification

javax.management.Notification

- javax.management.monitor.MonitorNotification

javax.management.monitor.MonitorNotification

**All Implemented Interfaces:** Serializable

```java
public class
MonitorNotification

extends
Notification
```

Provides definitions of the notifications sent by monitor MBeans.

The notification source and a set of parameters concerning the monitor MBean's state
need to be specified when creating a new object of this class.

The list of notifications fired by the monitor MBeans is the following:

- Common to all kind of monitors:

- The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

Common to the counter and the gauge monitors:

- The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

Counter monitors only:

- The observed attribute has reached the threshold value.

Gauge monitors only:

- The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

String monitors only:

- The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

**Since:** 1.5
**See Also:** Serialized Form

public class

MonitorNotification

extends

Notification

Provides definitions of the notifications sent by monitor MBeans.

The notification source and a set of parameters concerning the monitor MBean's state
need to be specified when creating a new object of this class.

The list of notifications fired by the monitor MBeans is the following:

- Common to all kind of monitors:

- The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

Common to the counter and the gauge monitors:

- The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

Counter monitors only:

- The observed attribute has reached the threshold value.

Gauge monitors only:

- The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

String monitors only:

- The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

The notification source and a set of parameters concerning the monitor MBean's state
need to be specified when creating a new object of this class.

The list of notifications fired by the monitor MBeans is the following:

- Common to all kind of monitors:

- The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

Common to the counter and the gauge monitors:

- The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

Counter monitors only:

- The observed attribute has reached the threshold value.

Gauge monitors only:

- The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

String monitors only:

- The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

Common to all kind of monitors:

- The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

Common to the counter and the gauge monitors:

- The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

Counter monitors only:

- The observed attribute has reached the threshold value.

Gauge monitors only:

- The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

String monitors only:

- The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

The observed object is not registered in the MBean server.

The observed attribute is not contained in the observed object.

The type of the observed attribute is not correct.

Any exception (except the cases described above) occurs when trying to get the value of the observed attribute.

The threshold high or threshold low are not of the same type as the gauge (gauge monitors).

The threshold or the offset or the modulus are not of the same type as the counter (counter monitors).

The observed attribute has reached the threshold value.

The observed attribute has exceeded the threshold high value.

The observed attribute has exceeded the threshold low value.

The observed attribute has matched the "string to compare" value.

The observed attribute has differed from the "string to compare" value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

OBSERVED_ATTRIBUTE_ERROR

Notification type denoting that the observed attribute is not contained in the observed object.

static

String

OBSERVED_ATTRIBUTE_TYPE_ERROR

Notification type denoting that the type of the observed attribute is not correct.

static

String

OBSERVED_OBJECT_ERROR

Notification type denoting that the observed object is not registered in the MBean server.

static

String

RUNTIME_ERROR

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.

static

String

STRING_TO_COMPARE_VALUE_DIFFERED

Notification type denoting that the observed attribute has differed from the "string to compare" value.

static

String

STRING_TO_COMPARE_VALUE_MATCHED

Notification type denoting that the observed attribute has matched the "string to compare" value.

static

String

THRESHOLD_ERROR

Notification type denoting that the type of the thresholds, offset or modulus is not correct.

static

String

THRESHOLD_HIGH_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold high value.

static

String

THRESHOLD_LOW_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold low value.

static

String

THRESHOLD_VALUE_EXCEEDED

Notification type denoting that the observed attribute has reached the threshold value.

- Fields declared in class javax.management.

Notification

source

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getDerivedGauge

()

Gets the derived gauge of this monitor notification.

String

getObservedAttribute

()

Gets the observed attribute of this monitor notification.

ObjectName

getObservedObject

()

Gets the observed object of this monitor notification.

Object

getTrigger

()

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

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

OBSERVED_ATTRIBUTE_ERROR

Notification type denoting that the observed attribute is not contained in the observed object.

static

String

OBSERVED_ATTRIBUTE_TYPE_ERROR

Notification type denoting that the type of the observed attribute is not correct.

static

String

OBSERVED_OBJECT_ERROR

Notification type denoting that the observed object is not registered in the MBean server.

static

String

RUNTIME_ERROR

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.

static

String

STRING_TO_COMPARE_VALUE_DIFFERED

Notification type denoting that the observed attribute has differed from the "string to compare" value.

static

String

STRING_TO_COMPARE_VALUE_MATCHED

Notification type denoting that the observed attribute has matched the "string to compare" value.

static

String

THRESHOLD_ERROR

Notification type denoting that the type of the thresholds, offset or modulus is not correct.

static

String

THRESHOLD_HIGH_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold high value.

static

String

THRESHOLD_LOW_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold low value.

static

String

THRESHOLD_VALUE_EXCEEDED

Notification type denoting that the observed attribute has reached the threshold value.

- Fields declared in class javax.management.

Notification

source

---

#### Field Summary

Notification type denoting that the observed attribute is not contained in the observed object.

Notification type denoting that the type of the observed attribute is not correct.

Notification type denoting that the observed object is not registered in the MBean server.

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.

Notification type denoting that the observed attribute has differed from the "string to compare" value.

Notification type denoting that the observed attribute has matched the "string to compare" value.

Notification type denoting that the type of the thresholds, offset or modulus is not correct.

Notification type denoting that the observed attribute has exceeded the threshold high value.

Notification type denoting that the observed attribute has exceeded the threshold low value.

Notification type denoting that the observed attribute has reached the threshold value.

Fields declared in class javax.management.

Notification

source

---

#### Fields declared in class javax.management. Notification

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

getDerivedGauge

()

Gets the derived gauge of this monitor notification.

String

getObservedAttribute

()

Gets the observed attribute of this monitor notification.

ObjectName

getObservedObject

()

Gets the observed object of this monitor notification.

Object

getTrigger

()

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

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

Gets the derived gauge of this monitor notification.

Gets the observed attribute of this monitor notification.

Gets the observed object of this monitor notification.

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

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

- OBSERVED_OBJECT_ERROR

```java
public static final
String
OBSERVED_OBJECT_ERROR
```

Notification type denoting that the observed object is not registered in the MBean server.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.mbean

.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_ERROR
```

Notification type denoting that the observed attribute is not contained in the observed object.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.attribute

.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_TYPE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_TYPE_ERROR
```

Notification type denoting that the type of the observed attribute is not correct.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.type

.

**See Also:** Constant Field Values

- THRESHOLD_ERROR

```java
public static final
String
THRESHOLD_ERROR
```

Notification type denoting that the type of the thresholds, offset or modulus is not correct.
This notification is fired by counter and gauge monitors.

The value of this notification type is

jmx.monitor.error.threshold

.

**See Also:** Constant Field Values

- RUNTIME_ERROR

```java
public static final
String
RUNTIME_ERROR
```

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.runtime

.

**See Also:** Constant Field Values

- THRESHOLD_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has reached the threshold value.
This notification is only fired by counter monitors.

The value of this notification type is

jmx.monitor.counter.threshold

.

**See Also:** Constant Field Values

- THRESHOLD_HIGH_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_HIGH_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold high value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.high

.

**See Also:** Constant Field Values

- THRESHOLD_LOW_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_LOW_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold low value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.low

.

**See Also:** Constant Field Values

- STRING_TO_COMPARE_VALUE_MATCHED

```java
public static final
String
STRING_TO_COMPARE_VALUE_MATCHED
```

Notification type denoting that the observed attribute has matched the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.matches

.

**See Also:** Constant Field Values

- STRING_TO_COMPARE_VALUE_DIFFERED

```java
public static final
String
STRING_TO_COMPARE_VALUE_DIFFERED
```

Notification type denoting that the observed attribute has differed from the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.differs

.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getObservedObject

```java
public
ObjectName
getObservedObject()
```

Gets the observed object of this monitor notification.

**Returns:** The observed object.

- getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the observed attribute of this monitor notification.

**Returns:** The observed attribute.

- getDerivedGauge

```java
public
Object
getDerivedGauge()
```

Gets the derived gauge of this monitor notification.

**Returns:** The derived gauge.

- getTrigger

```java
public
Object
getTrigger()
```

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

**Returns:** The trigger.

Field Detail

- OBSERVED_OBJECT_ERROR

```java
public static final
String
OBSERVED_OBJECT_ERROR
```

Notification type denoting that the observed object is not registered in the MBean server.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.mbean

.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_ERROR
```

Notification type denoting that the observed attribute is not contained in the observed object.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.attribute

.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_TYPE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_TYPE_ERROR
```

Notification type denoting that the type of the observed attribute is not correct.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.type

.

**See Also:** Constant Field Values

- THRESHOLD_ERROR

```java
public static final
String
THRESHOLD_ERROR
```

Notification type denoting that the type of the thresholds, offset or modulus is not correct.
This notification is fired by counter and gauge monitors.

The value of this notification type is

jmx.monitor.error.threshold

.

**See Also:** Constant Field Values

- RUNTIME_ERROR

```java
public static final
String
RUNTIME_ERROR
```

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.runtime

.

**See Also:** Constant Field Values

- THRESHOLD_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has reached the threshold value.
This notification is only fired by counter monitors.

The value of this notification type is

jmx.monitor.counter.threshold

.

**See Also:** Constant Field Values

- THRESHOLD_HIGH_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_HIGH_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold high value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.high

.

**See Also:** Constant Field Values

- THRESHOLD_LOW_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_LOW_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold low value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.low

.

**See Also:** Constant Field Values

- STRING_TO_COMPARE_VALUE_MATCHED

```java
public static final
String
STRING_TO_COMPARE_VALUE_MATCHED
```

Notification type denoting that the observed attribute has matched the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.matches

.

**See Also:** Constant Field Values

- STRING_TO_COMPARE_VALUE_DIFFERED

```java
public static final
String
STRING_TO_COMPARE_VALUE_DIFFERED
```

Notification type denoting that the observed attribute has differed from the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.differs

.

**See Also:** Constant Field Values

---

#### Field Detail

OBSERVED_OBJECT_ERROR

```java
public static final
String
OBSERVED_OBJECT_ERROR
```

Notification type denoting that the observed object is not registered in the MBean server.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.mbean

.

**See Also:** Constant Field Values

---

#### OBSERVED_OBJECT_ERROR

public static final

String

OBSERVED_OBJECT_ERROR

Notification type denoting that the observed object is not registered in the MBean server.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.mbean

.

OBSERVED_ATTRIBUTE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_ERROR
```

Notification type denoting that the observed attribute is not contained in the observed object.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.attribute

.

**See Also:** Constant Field Values

---

#### OBSERVED_ATTRIBUTE_ERROR

public static final

String

OBSERVED_ATTRIBUTE_ERROR

Notification type denoting that the observed attribute is not contained in the observed object.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.attribute

.

OBSERVED_ATTRIBUTE_TYPE_ERROR

```java
public static final
String
OBSERVED_ATTRIBUTE_TYPE_ERROR
```

Notification type denoting that the type of the observed attribute is not correct.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.type

.

**See Also:** Constant Field Values

---

#### OBSERVED_ATTRIBUTE_TYPE_ERROR

public static final

String

OBSERVED_ATTRIBUTE_TYPE_ERROR

Notification type denoting that the type of the observed attribute is not correct.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.type

.

THRESHOLD_ERROR

```java
public static final
String
THRESHOLD_ERROR
```

Notification type denoting that the type of the thresholds, offset or modulus is not correct.
This notification is fired by counter and gauge monitors.

The value of this notification type is

jmx.monitor.error.threshold

.

**See Also:** Constant Field Values

---

#### THRESHOLD_ERROR

public static final

String

THRESHOLD_ERROR

Notification type denoting that the type of the thresholds, offset or modulus is not correct.
This notification is fired by counter and gauge monitors.

The value of this notification type is

jmx.monitor.error.threshold

.

RUNTIME_ERROR

```java
public static final
String
RUNTIME_ERROR
```

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.runtime

.

**See Also:** Constant Field Values

---

#### RUNTIME_ERROR

public static final

String

RUNTIME_ERROR

Notification type denoting that a non-predefined error type has occurred when trying to get the value of the observed attribute.
This notification is fired by all kinds of monitors.

The value of this notification type is

jmx.monitor.error.runtime

.

THRESHOLD_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has reached the threshold value.
This notification is only fired by counter monitors.

The value of this notification type is

jmx.monitor.counter.threshold

.

**See Also:** Constant Field Values

---

#### THRESHOLD_VALUE_EXCEEDED

public static final

String

THRESHOLD_VALUE_EXCEEDED

Notification type denoting that the observed attribute has reached the threshold value.
This notification is only fired by counter monitors.

The value of this notification type is

jmx.monitor.counter.threshold

.

THRESHOLD_HIGH_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_HIGH_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold high value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.high

.

**See Also:** Constant Field Values

---

#### THRESHOLD_HIGH_VALUE_EXCEEDED

public static final

String

THRESHOLD_HIGH_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold high value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.high

.

THRESHOLD_LOW_VALUE_EXCEEDED

```java
public static final
String
THRESHOLD_LOW_VALUE_EXCEEDED
```

Notification type denoting that the observed attribute has exceeded the threshold low value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.low

.

**See Also:** Constant Field Values

---

#### THRESHOLD_LOW_VALUE_EXCEEDED

public static final

String

THRESHOLD_LOW_VALUE_EXCEEDED

Notification type denoting that the observed attribute has exceeded the threshold low value.
This notification is only fired by gauge monitors.

The value of this notification type is

jmx.monitor.gauge.low

.

STRING_TO_COMPARE_VALUE_MATCHED

```java
public static final
String
STRING_TO_COMPARE_VALUE_MATCHED
```

Notification type denoting that the observed attribute has matched the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.matches

.

**See Also:** Constant Field Values

---

#### STRING_TO_COMPARE_VALUE_MATCHED

public static final

String

STRING_TO_COMPARE_VALUE_MATCHED

Notification type denoting that the observed attribute has matched the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.matches

.

STRING_TO_COMPARE_VALUE_DIFFERED

```java
public static final
String
STRING_TO_COMPARE_VALUE_DIFFERED
```

Notification type denoting that the observed attribute has differed from the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.differs

.

**See Also:** Constant Field Values

---

#### STRING_TO_COMPARE_VALUE_DIFFERED

public static final

String

STRING_TO_COMPARE_VALUE_DIFFERED

Notification type denoting that the observed attribute has differed from the "string to compare" value.
This notification is only fired by string monitors.

The value of this notification type is

jmx.monitor.string.differs

.

Method Detail

- getObservedObject

```java
public
ObjectName
getObservedObject()
```

Gets the observed object of this monitor notification.

**Returns:** The observed object.

- getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the observed attribute of this monitor notification.

**Returns:** The observed attribute.

- getDerivedGauge

```java
public
Object
getDerivedGauge()
```

Gets the derived gauge of this monitor notification.

**Returns:** The derived gauge.

- getTrigger

```java
public
Object
getTrigger()
```

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

**Returns:** The trigger.

---

#### Method Detail

getObservedObject

```java
public
ObjectName
getObservedObject()
```

Gets the observed object of this monitor notification.

**Returns:** The observed object.

---

#### getObservedObject

public

ObjectName

getObservedObject()

Gets the observed object of this monitor notification.

getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the observed attribute of this monitor notification.

**Returns:** The observed attribute.

---

#### getObservedAttribute

public

String

getObservedAttribute()

Gets the observed attribute of this monitor notification.

getDerivedGauge

```java
public
Object
getDerivedGauge()
```

Gets the derived gauge of this monitor notification.

**Returns:** The derived gauge.

---

#### getDerivedGauge

public

Object

getDerivedGauge()

Gets the derived gauge of this monitor notification.

getTrigger

```java
public
Object
getTrigger()
```

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

**Returns:** The trigger.

---

#### getTrigger

public

Object

getTrigger()

Gets the threshold/string (depending on the monitor type) that triggered off this monitor notification.

---

