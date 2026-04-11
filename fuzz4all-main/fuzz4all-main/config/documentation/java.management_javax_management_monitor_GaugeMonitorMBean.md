# Interface GaugeMonitorMBean

**Source:** `java.management\javax\management\monitor\GaugeMonitorMBean.html`

### Class Description

```java
public interface
GaugeMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the gauge monitor MBean.

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
getHighThreshold()

Gets the high threshold value.

**Returns:**
- The high threshold value.

---

#### Number
getLowThreshold()

Gets the low threshold value.

**Returns:**
- The low threshold value.

---

#### void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException

Sets the high and the low threshold values.

**Parameters:**
- highValue

- The high threshold value.
- lowValue

- The low threshold value.

**Throws:**
- IllegalArgumentException

- The specified high/low threshold is null
or the low threshold is greater than the high threshold
or the high threshold and the low threshold are not of the same type.

---

#### boolean getNotifyHigh()

Gets the high notification's on/off switch value.

**Returns:**
- true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.

**See Also:**
- setNotifyHigh(boolean)

---

#### void setNotifyHigh​(boolean value)

Sets the high notification's on/off switch value.

**Parameters:**
- value

- The high notification's on/off switch value.

**See Also:**
- getNotifyHigh()

---

#### boolean getNotifyLow()

Gets the low notification's on/off switch value.

**Returns:**
- true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.

**See Also:**
- setNotifyLow(boolean)

---

#### void setNotifyLow​(boolean value)

Sets the low notification's on/off switch value.

**Parameters:**
- value

- The low notification's on/off switch value.

**See Also:**
- getNotifyLow()

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

#### Interface GaugeMonitorMBean

**All Superinterfaces:** MonitorMBean

**All Known Implementing Classes:** GaugeMonitor

```java
public interface
GaugeMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the gauge monitor MBean.

**Since:** 1.5

public interface

GaugeMonitorMBean

extends

MonitorMBean

Exposes the remote management interface of the gauge monitor MBean.

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

getHighThreshold

()

Gets the high threshold value.

Number

getLowThreshold

()

Gets the low threshold value.

boolean

getNotifyHigh

()

Gets the high notification's on/off switch value.

boolean

getNotifyLow

()

Gets the low notification's on/off switch value.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value.

void

setNotifyHigh

​(boolean value)

Sets the high notification's on/off switch value.

void

setNotifyLow

​(boolean value)

Sets the low notification's on/off switch value.

void

setThresholds

​(

Number

highValue,

Number

lowValue)

Sets the high and the low threshold values.

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

getHighThreshold

()

Gets the high threshold value.

Number

getLowThreshold

()

Gets the low threshold value.

boolean

getNotifyHigh

()

Gets the high notification's on/off switch value.

boolean

getNotifyLow

()

Gets the low notification's on/off switch value.

void

setDifferenceMode

​(boolean value)

Sets the difference mode flag value.

void

setNotifyHigh

​(boolean value)

Sets the high notification's on/off switch value.

void

setNotifyLow

​(boolean value)

Sets the low notification's on/off switch value.

void

setThresholds

​(

Number

highValue,

Number

lowValue)

Sets the high and the low threshold values.

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

Gets the high threshold value.

Gets the low threshold value.

Gets the high notification's on/off switch value.

Gets the low notification's on/off switch value.

Sets the difference mode flag value.

Sets the high notification's on/off switch value.

Sets the low notification's on/off switch value.

Sets the high and the low threshold values.

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

- getHighThreshold

```java
Number
getHighThreshold()
```

Gets the high threshold value.

**Returns:** The high threshold value.

- getLowThreshold

```java
Number
getLowThreshold()
```

Gets the low threshold value.

**Returns:** The low threshold value.

- setThresholds

```java
void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values.

**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low threshold is null
or the low threshold is greater than the high threshold
or the high threshold and the low threshold are not of the same type.

- getNotifyHigh

```java
boolean getNotifyHigh()
```

Gets the high notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

- setNotifyHigh

```java
void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value.

**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

- getNotifyLow

```java
boolean getNotifyLow()
```

Gets the low notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

- setNotifyLow

```java
void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value.

**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

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

- getHighThreshold

```java
Number
getHighThreshold()
```

Gets the high threshold value.

**Returns:** The high threshold value.

- getLowThreshold

```java
Number
getLowThreshold()
```

Gets the low threshold value.

**Returns:** The low threshold value.

- setThresholds

```java
void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values.

**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low threshold is null
or the low threshold is greater than the high threshold
or the high threshold and the low threshold are not of the same type.

- getNotifyHigh

```java
boolean getNotifyHigh()
```

Gets the high notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

- setNotifyHigh

```java
void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value.

**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

- getNotifyLow

```java
boolean getNotifyLow()
```

Gets the low notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

- setNotifyLow

```java
void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value.

**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

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

getHighThreshold

```java
Number
getHighThreshold()
```

Gets the high threshold value.

**Returns:** The high threshold value.

---

#### getHighThreshold

Number

getHighThreshold()

Gets the high threshold value.

getLowThreshold

```java
Number
getLowThreshold()
```

Gets the low threshold value.

**Returns:** The low threshold value.

---

#### getLowThreshold

Number

getLowThreshold()

Gets the low threshold value.

setThresholds

```java
void setThresholds​(
Number
highValue,

Number
lowValue)
throws
IllegalArgumentException
```

Sets the high and the low threshold values.

**Parameters:** highValue

- The high threshold value.
**Parameters:** lowValue

- The low threshold value.
**Throws:** IllegalArgumentException

- The specified high/low threshold is null
or the low threshold is greater than the high threshold
or the high threshold and the low threshold are not of the same type.

---

#### setThresholds

void setThresholds​(

Number

highValue,

Number

lowValue)
throws

IllegalArgumentException

Sets the high and the low threshold values.

getNotifyHigh

```java
boolean getNotifyHigh()
```

Gets the high notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the high threshold,

false

otherwise.
**See Also:** setNotifyHigh(boolean)

---

#### getNotifyHigh

boolean getNotifyHigh()

Gets the high notification's on/off switch value.

setNotifyHigh

```java
void setNotifyHigh​(boolean value)
```

Sets the high notification's on/off switch value.

**Parameters:** value

- The high notification's on/off switch value.
**See Also:** getNotifyHigh()

---

#### setNotifyHigh

void setNotifyHigh​(boolean value)

Sets the high notification's on/off switch value.

getNotifyLow

```java
boolean getNotifyLow()
```

Gets the low notification's on/off switch value.

**Returns:** true

if the gauge monitor notifies when
exceeding the low threshold,

false

otherwise.
**See Also:** setNotifyLow(boolean)

---

#### getNotifyLow

boolean getNotifyLow()

Gets the low notification's on/off switch value.

setNotifyLow

```java
void setNotifyLow​(boolean value)
```

Sets the low notification's on/off switch value.

**Parameters:** value

- The low notification's on/off switch value.
**See Also:** getNotifyLow()

---

#### setNotifyLow

void setNotifyLow​(boolean value)

Sets the low notification's on/off switch value.

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

