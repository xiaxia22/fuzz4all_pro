# Interface CounterMonitorMBean

**Source:** `java.management\javax\management\monitor\CounterMonitorMBean.html`

### Class Description

```java
public interface
CounterMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the counter monitor MBean.

**All Superinterfaces:** MonitorMBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

Number
getDerivedGauge()

Gets the derived gauge.

**Returns:**
- The derived gauge.

---

#### @Deprecated

long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp.

**Returns:**
- The derived gauge timestamp.

---

#### @Deprecated

Number
getThreshold()

Gets the threshold value.

**Returns:**
- The threshold value.

**See Also:**
- setThreshold(Number)

---

#### @Deprecated

void setThreshold​(
Number
value)
throws
IllegalArgumentException

Sets the threshold value.

**Parameters:**
- value

- The threshold value.

**Throws:**
- IllegalArgumentException

- The specified threshold is null or the threshold value is less than zero.

**See Also:**
- getThreshold()

---

#### Number
getDerivedGauge​(
ObjectName
object)

Gets the derived gauge for the specified MBean.

**Parameters:**
- object

- the MBean for which the derived gauge is to be returned

**Returns:**
- The derived gauge for the specified MBean if this MBean is in the
set of observed MBeans, or

null

otherwise.

---

#### long getDerivedGaugeTimeStamp​(
ObjectName
object)

Gets the derived gauge timestamp for the specified MBean.

**Parameters:**
- object

- the MBean for which the derived gauge timestamp is to be returned

**Returns:**
- The derived gauge timestamp for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.

---

#### Number
getThreshold​(
ObjectName
object)

Gets the threshold value for the specified MBean.

**Parameters:**
- object

- the MBean for which the threshold value is to be returned

**Returns:**
- The threshold value for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.

**See Also:**
- setThreshold(java.lang.Number)

---

#### Number
getInitThreshold()

Gets the initial threshold value common to all observed objects.

**Returns:**
- The initial threshold value.

**See Also:**
- setInitThreshold(java.lang.Number)

---

#### void setInitThreshold​(
Number
value)
throws
IllegalArgumentException

Sets the initial threshold value common to all observed MBeans.

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

#### Number
getOffset()

Gets the offset value.

**Returns:**
- The offset value.

**See Also:**
- setOffset(Number)

---

#### void setOffset​(
Number
value)
throws
IllegalArgumentException

Sets the offset value.

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

#### Number
getModulus()

Gets the modulus value.

**Returns:**
- The modulus value.

**See Also:**
- setModulus(java.lang.Number)

---

#### void setModulus​(
Number
value)
throws
IllegalArgumentException

Sets the modulus value.

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

#### boolean getNotify()

Gets the notification's on/off switch value.

**Returns:**
- true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.

**See Also:**
- setNotify(boolean)

---

#### void setNotify​(boolean value)

Sets the notification's on/off switch value.

**Parameters:**
- value

- The notification's on/off switch value.

**See Also:**
- getNotify()

---

#### boolean getDifferenceMode()

Gets the difference mode flag value.

**Returns:**
- true

if the difference mode is used,

false

otherwise.

**See Also:**
- setDifferenceMode(boolean)

---

#### void setDifferenceMode​(boolean value)

Sets the difference mode flag value.

**Parameters:**
- value

- The difference mode flag value.

**See Also:**
- getDifferenceMode()

---

### Additional Sections

#### Interface CounterMonitorMBean

**All Superinterfaces:** MonitorMBean

**All Known Implementing Classes:** CounterMonitor

```java
public interface
CounterMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the counter monitor MBean.

**Since:** 1.5

public interface

CounterMonitorMBean

extends

MonitorMBean

Exposes the remote management interface of the counter monitor MBean.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

Gets the derived gauge for the specified MBean.

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

Gets the derived gauge timestamp for the specified MBean.

boolean

getDifferenceMode

()

Gets the difference mode flag value.

Number

getInitThreshold

()

Gets the initial threshold value common to all observed objects.

Number

getModulus

()

Gets the modulus value.

boolean

getNotify

()

Gets the notification's on/off switch value.

Number

getOffset

()

Gets the offset value.

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

Gets the threshold value for the specified MBean.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value.

void

setInitThreshold

​(

Number

value)

Sets the initial threshold value common to all observed MBeans.

void

setModulus

​(

Number

value)

Sets the modulus value.

void

setNotify

​(boolean value)

Sets the notification's on/off switch value.

void

setOffset

​(

Number

value)

Sets the offset value.

void

setThreshold

​(

Number

value)

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

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

,

start

,

stop

Method Summary

All Methods

Instance Methods

Abstract Methods

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

Gets the derived gauge for the specified MBean.

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

Gets the derived gauge timestamp for the specified MBean.

boolean

getDifferenceMode

()

Gets the difference mode flag value.

Number

getInitThreshold

()

Gets the initial threshold value common to all observed objects.

Number

getModulus

()

Gets the modulus value.

boolean

getNotify

()

Gets the notification's on/off switch value.

Number

getOffset

()

Gets the offset value.

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

Gets the threshold value for the specified MBean.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value.

void

setInitThreshold

​(

Number

value)

Sets the initial threshold value common to all observed MBeans.

void

setModulus

​(

Number

value)

Sets the modulus value.

void

setNotify

​(boolean value)

Sets the notification's on/off switch value.

void

setOffset

​(

Number

value)

Sets the offset value.

void

setThreshold

​(

Number

value)

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

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

,

start

,

stop

---

#### Method Summary

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Gets the derived gauge for the specified MBean.

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp for the specified MBean.

Gets the difference mode flag value.

Gets the initial threshold value common to all observed objects.

Gets the modulus value.

Gets the notification's on/off switch value.

Gets the offset value.

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value for the specified MBean.

Sets the difference mode flag value.

Sets the initial threshold value common to all observed MBeans.

Sets the modulus value.

Sets the notification's on/off switch value.

Sets the offset value.

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

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

,

start

,

stop

---

#### Methods declared in interface javax.management.monitor. MonitorMBean

============ METHOD DETAIL ==========

- Method Detail

- getDerivedGauge

```java
@Deprecated

Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Gets the derived gauge.

**Returns:** The derived gauge.

- getDerivedGaugeTimeStamp

```java
@Deprecated

long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp.

**Returns:** The derived gauge timestamp.

- getThreshold

```java
@Deprecated

Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value.

**Returns:** The threshold value.
**See Also:** setThreshold(Number)

- setThreshold

```java
@Deprecated

void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the threshold value.

**Parameters:** value

- The threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is null or the threshold value is less than zero.
**See Also:** getThreshold()

- getDerivedGauge

```java
Number
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge is to be returned
**Returns:** The derived gauge for the specified MBean if this MBean is in the
set of observed MBeans, or

null

otherwise.

- getDerivedGaugeTimeStamp

```java
long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge timestamp is to be returned
**Returns:** The derived gauge timestamp for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.

- getThreshold

```java
Number
getThreshold​(
ObjectName
object)
```

Gets the threshold value for the specified MBean.

**Parameters:** object

- the MBean for which the threshold value is to be returned
**Returns:** The threshold value for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.
**See Also:** setThreshold(java.lang.Number)

- getInitThreshold

```java
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Returns:** The initial threshold value.
**See Also:** setInitThreshold(java.lang.Number)

- setInitThreshold

```java
void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed MBeans.

**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

- getOffset

```java
Number
getOffset()
```

Gets the offset value.

**Returns:** The offset value.
**See Also:** setOffset(Number)

- setOffset

```java
void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value.

**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

- getModulus

```java
Number
getModulus()
```

Gets the modulus value.

**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

- setModulus

```java
void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value.

**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

- getNotify

```java
boolean getNotify()
```

Gets the notification's on/off switch value.

**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

- setNotify

```java
void setNotify​(boolean value)
```

Sets the notification's on/off switch value.

**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

- getDifferenceMode

```java
boolean getDifferenceMode()
```

Gets the difference mode flag value.

**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

- setDifferenceMode

```java
void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value.

**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

Method Detail

- getDerivedGauge

```java
@Deprecated

Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Gets the derived gauge.

**Returns:** The derived gauge.

- getDerivedGaugeTimeStamp

```java
@Deprecated

long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp.

**Returns:** The derived gauge timestamp.

- getThreshold

```java
@Deprecated

Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value.

**Returns:** The threshold value.
**See Also:** setThreshold(Number)

- setThreshold

```java
@Deprecated

void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the threshold value.

**Parameters:** value

- The threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is null or the threshold value is less than zero.
**See Also:** getThreshold()

- getDerivedGauge

```java
Number
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge is to be returned
**Returns:** The derived gauge for the specified MBean if this MBean is in the
set of observed MBeans, or

null

otherwise.

- getDerivedGaugeTimeStamp

```java
long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge timestamp is to be returned
**Returns:** The derived gauge timestamp for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.

- getThreshold

```java
Number
getThreshold​(
ObjectName
object)
```

Gets the threshold value for the specified MBean.

**Parameters:** object

- the MBean for which the threshold value is to be returned
**Returns:** The threshold value for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.
**See Also:** setThreshold(java.lang.Number)

- getInitThreshold

```java
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Returns:** The initial threshold value.
**See Also:** setInitThreshold(java.lang.Number)

- setInitThreshold

```java
void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed MBeans.

**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

- getOffset

```java
Number
getOffset()
```

Gets the offset value.

**Returns:** The offset value.
**See Also:** setOffset(Number)

- setOffset

```java
void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value.

**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

- getModulus

```java
Number
getModulus()
```

Gets the modulus value.

**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

- setModulus

```java
void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value.

**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

- getNotify

```java
boolean getNotify()
```

Gets the notification's on/off switch value.

**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

- setNotify

```java
void setNotify​(boolean value)
```

Sets the notification's on/off switch value.

**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

- getDifferenceMode

```java
boolean getDifferenceMode()
```

Gets the difference mode flag value.

**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

- setDifferenceMode

```java
void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value.

**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

---

#### Method Detail

getDerivedGauge

```java
@Deprecated

Number
getDerivedGauge()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGauge(ObjectName)

Gets the derived gauge.

**Returns:** The derived gauge.

---

#### getDerivedGauge

@Deprecated

Number

getDerivedGauge()

Gets the derived gauge.

getDerivedGaugeTimeStamp

```java
@Deprecated

long getDerivedGaugeTimeStamp()
```

Deprecated.

As of JMX 1.2, replaced by

getDerivedGaugeTimeStamp(ObjectName)

Gets the derived gauge timestamp.

**Returns:** The derived gauge timestamp.

---

#### getDerivedGaugeTimeStamp

@Deprecated

long getDerivedGaugeTimeStamp()

Gets the derived gauge timestamp.

getThreshold

```java
@Deprecated

Number
getThreshold()
```

Deprecated.

As of JMX 1.2, replaced by

getThreshold(ObjectName)

Gets the threshold value.

**Returns:** The threshold value.
**See Also:** setThreshold(Number)

---

#### getThreshold

@Deprecated

Number

getThreshold()

Gets the threshold value.

setThreshold

```java
@Deprecated

void setThreshold​(
Number
value)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

setInitThreshold(java.lang.Number)

Sets the threshold value.

**Parameters:** value

- The threshold value.
**Throws:** IllegalArgumentException

- The specified threshold is null or the threshold value is less than zero.
**See Also:** getThreshold()

---

#### setThreshold

@Deprecated

void setThreshold​(

Number

value)
throws

IllegalArgumentException

Sets the threshold value.

getDerivedGauge

```java
Number
getDerivedGauge​(
ObjectName
object)
```

Gets the derived gauge for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge is to be returned
**Returns:** The derived gauge for the specified MBean if this MBean is in the
set of observed MBeans, or

null

otherwise.

---

#### getDerivedGauge

Number

getDerivedGauge​(

ObjectName

object)

Gets the derived gauge for the specified MBean.

getDerivedGaugeTimeStamp

```java
long getDerivedGaugeTimeStamp​(
ObjectName
object)
```

Gets the derived gauge timestamp for the specified MBean.

**Parameters:** object

- the MBean for which the derived gauge timestamp is to be returned
**Returns:** The derived gauge timestamp for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.

---

#### getDerivedGaugeTimeStamp

long getDerivedGaugeTimeStamp​(

ObjectName

object)

Gets the derived gauge timestamp for the specified MBean.

getThreshold

```java
Number
getThreshold​(
ObjectName
object)
```

Gets the threshold value for the specified MBean.

**Parameters:** object

- the MBean for which the threshold value is to be returned
**Returns:** The threshold value for the specified MBean if this MBean
is in the set of observed MBeans, or

null

otherwise.
**See Also:** setThreshold(java.lang.Number)

---

#### getThreshold

Number

getThreshold​(

ObjectName

object)

Gets the threshold value for the specified MBean.

getInitThreshold

```java
Number
getInitThreshold()
```

Gets the initial threshold value common to all observed objects.

**Returns:** The initial threshold value.
**See Also:** setInitThreshold(java.lang.Number)

---

#### getInitThreshold

Number

getInitThreshold()

Gets the initial threshold value common to all observed objects.

setInitThreshold

```java
void setInitThreshold​(
Number
value)
throws
IllegalArgumentException
```

Sets the initial threshold value common to all observed MBeans.

**Parameters:** value

- The initial threshold value.
**Throws:** IllegalArgumentException

- The specified
threshold is null or the threshold value is less than zero.
**See Also:** getInitThreshold()

---

#### setInitThreshold

void setInitThreshold​(

Number

value)
throws

IllegalArgumentException

Sets the initial threshold value common to all observed MBeans.

getOffset

```java
Number
getOffset()
```

Gets the offset value.

**Returns:** The offset value.
**See Also:** setOffset(Number)

---

#### getOffset

Number

getOffset()

Gets the offset value.

setOffset

```java
void setOffset​(
Number
value)
throws
IllegalArgumentException
```

Sets the offset value.

**Parameters:** value

- The offset value.
**Throws:** IllegalArgumentException

- The specified
offset is null or the offset value is less than zero.
**See Also:** getOffset()

---

#### setOffset

void setOffset​(

Number

value)
throws

IllegalArgumentException

Sets the offset value.

getModulus

```java
Number
getModulus()
```

Gets the modulus value.

**Returns:** The modulus value.
**See Also:** setModulus(java.lang.Number)

---

#### getModulus

Number

getModulus()

Gets the modulus value.

setModulus

```java
void setModulus​(
Number
value)
throws
IllegalArgumentException
```

Sets the modulus value.

**Parameters:** value

- The modulus value.
**Throws:** IllegalArgumentException

- The specified
modulus is null or the modulus value is less than zero.
**See Also:** getModulus()

---

#### setModulus

void setModulus​(

Number

value)
throws

IllegalArgumentException

Sets the modulus value.

getNotify

```java
boolean getNotify()
```

Gets the notification's on/off switch value.

**Returns:** true

if the counter monitor notifies when
exceeding the threshold,

false

otherwise.
**See Also:** setNotify(boolean)

---

#### getNotify

boolean getNotify()

Gets the notification's on/off switch value.

setNotify

```java
void setNotify​(boolean value)
```

Sets the notification's on/off switch value.

**Parameters:** value

- The notification's on/off switch value.
**See Also:** getNotify()

---

#### setNotify

void setNotify​(boolean value)

Sets the notification's on/off switch value.

getDifferenceMode

```java
boolean getDifferenceMode()
```

Gets the difference mode flag value.

**Returns:** true

if the difference mode is used,

false

otherwise.
**See Also:** setDifferenceMode(boolean)

---

#### getDifferenceMode

boolean getDifferenceMode()

Gets the difference mode flag value.

setDifferenceMode

```java
void setDifferenceMode​(boolean value)
```

Sets the difference mode flag value.

**Parameters:** value

- The difference mode flag value.
**See Also:** getDifferenceMode()

---

#### setDifferenceMode

void setDifferenceMode​(boolean value)

Sets the difference mode flag value.

---

