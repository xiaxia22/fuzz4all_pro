# Interface StringMonitorMBean

**Source:** `java.management\javax\management\monitor\StringMonitorMBean.html`

### Class Description

```java
public interface
StringMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the string monitor MBean.

**All Superinterfaces:** MonitorMBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

String
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

#### String
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

#### String
getStringToCompare()

Gets the string to compare with the observed attribute.

**Returns:**
- The string value.

**See Also:**
- setStringToCompare(java.lang.String)

---

#### void setStringToCompare​(
String
value)
throws
IllegalArgumentException

Sets the string to compare with the observed attribute.

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

#### boolean getNotifyMatch()

Gets the matching notification's on/off switch value.

**Returns:**
- true

if the string monitor notifies when
matching,

false

otherwise.

**See Also:**
- setNotifyMatch(boolean)

---

#### void setNotifyMatch​(boolean value)

Sets the matching notification's on/off switch value.

**Parameters:**
- value

- The matching notification's on/off switch value.

**See Also:**
- getNotifyMatch()

---

#### boolean getNotifyDiffer()

Gets the differing notification's on/off switch value.

**Returns:**
- true

if the string monitor notifies when
differing,

false

otherwise.

**See Also:**
- setNotifyDiffer(boolean)

---

#### void setNotifyDiffer​(boolean value)

Sets the differing notification's on/off switch value.

**Parameters:**
- value

- The differing notification's on/off switch value.

**See Also:**
- getNotifyDiffer()

---

### Additional Sections

#### Interface StringMonitorMBean

**All Superinterfaces:** MonitorMBean

**All Known Implementing Classes:** StringMonitor

```java
public interface
StringMonitorMBean

extends
MonitorMBean
```

Exposes the remote management interface of the string monitor MBean.

**Since:** 1.5

public interface

StringMonitorMBean

extends

MonitorMBean

Exposes the remote management interface of the string monitor MBean.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

getNotifyDiffer

()

Gets the differing notification's on/off switch value.

boolean

getNotifyMatch

()

Gets the matching notification's on/off switch value.

String

getStringToCompare

()

Gets the string to compare with the observed attribute.

void

setNotifyDiffer

​(boolean value)

Sets the differing notification's on/off switch value.

void

setNotifyMatch

​(boolean value)

Sets the matching notification's on/off switch value.

void

setStringToCompare

​(

String

value)

Sets the string to compare with the observed attribute.

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

getNotifyDiffer

()

Gets the differing notification's on/off switch value.

boolean

getNotifyMatch

()

Gets the matching notification's on/off switch value.

String

getStringToCompare

()

Gets the string to compare with the observed attribute.

void

setNotifyDiffer

​(boolean value)

Sets the differing notification's on/off switch value.

void

setNotifyMatch

​(boolean value)

Sets the matching notification's on/off switch value.

void

setStringToCompare

​(

String

value)

Sets the string to compare with the observed attribute.

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

Gets the differing notification's on/off switch value.

Gets the matching notification's on/off switch value.

Gets the string to compare with the observed attribute.

Sets the differing notification's on/off switch value.

Sets the matching notification's on/off switch value.

Sets the string to compare with the observed attribute.

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

String
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
String
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

- getStringToCompare

```java
String
getStringToCompare()
```

Gets the string to compare with the observed attribute.

**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

- setStringToCompare

```java
void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute.

**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

- getNotifyMatch

```java
boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
matching,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

- setNotifyMatch

```java
void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value.

**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

- getNotifyDiffer

```java
boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
differing,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

- setNotifyDiffer

```java
void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value.

**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

Method Detail

- getDerivedGauge

```java
@Deprecated

String
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
String
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

- getStringToCompare

```java
String
getStringToCompare()
```

Gets the string to compare with the observed attribute.

**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

- setStringToCompare

```java
void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute.

**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

- getNotifyMatch

```java
boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
matching,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

- setNotifyMatch

```java
void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value.

**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

- getNotifyDiffer

```java
boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
differing,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

- setNotifyDiffer

```java
void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value.

**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

---

#### Method Detail

getDerivedGauge

```java
@Deprecated

String
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

String

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
String
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

String

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

getStringToCompare

```java
String
getStringToCompare()
```

Gets the string to compare with the observed attribute.

**Returns:** The string value.
**See Also:** setStringToCompare(java.lang.String)

---

#### getStringToCompare

String

getStringToCompare()

Gets the string to compare with the observed attribute.

setStringToCompare

```java
void setStringToCompare​(
String
value)
throws
IllegalArgumentException
```

Sets the string to compare with the observed attribute.

**Parameters:** value

- The string value.
**Throws:** IllegalArgumentException

- The specified
string to compare is null.
**See Also:** getStringToCompare()

---

#### setStringToCompare

void setStringToCompare​(

String

value)
throws

IllegalArgumentException

Sets the string to compare with the observed attribute.

getNotifyMatch

```java
boolean getNotifyMatch()
```

Gets the matching notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
matching,

false

otherwise.
**See Also:** setNotifyMatch(boolean)

---

#### getNotifyMatch

boolean getNotifyMatch()

Gets the matching notification's on/off switch value.

setNotifyMatch

```java
void setNotifyMatch​(boolean value)
```

Sets the matching notification's on/off switch value.

**Parameters:** value

- The matching notification's on/off switch value.
**See Also:** getNotifyMatch()

---

#### setNotifyMatch

void setNotifyMatch​(boolean value)

Sets the matching notification's on/off switch value.

getNotifyDiffer

```java
boolean getNotifyDiffer()
```

Gets the differing notification's on/off switch value.

**Returns:** true

if the string monitor notifies when
differing,

false

otherwise.
**See Also:** setNotifyDiffer(boolean)

---

#### getNotifyDiffer

boolean getNotifyDiffer()

Gets the differing notification's on/off switch value.

setNotifyDiffer

```java
void setNotifyDiffer​(boolean value)
```

Sets the differing notification's on/off switch value.

**Parameters:** value

- The differing notification's on/off switch value.
**See Also:** getNotifyDiffer()

---

#### setNotifyDiffer

void setNotifyDiffer​(boolean value)

Sets the differing notification's on/off switch value.

---

