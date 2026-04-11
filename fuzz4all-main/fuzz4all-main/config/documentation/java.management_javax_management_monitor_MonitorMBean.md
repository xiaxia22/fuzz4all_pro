# Interface MonitorMBean

**Source:** `java.management\javax\management\monitor\MonitorMBean.html`

### Class Description

```java
public interface
MonitorMBean
```

Exposes the remote management interface of monitor MBeans.

**All Known Subinterfaces:** CounterMonitorMBean

,

GaugeMonitorMBean

,

StringMonitorMBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void start()

Starts the monitor.

---

#### void stop()

Stops the monitor.

---

#### void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException

Adds the specified object in the set of observed MBeans.

**Parameters:**
- object

- The object to observe.

**Throws:**
- IllegalArgumentException

- the specified object is null.

---

#### void removeObservedObject​(
ObjectName
object)

Removes the specified object from the set of observed MBeans.

**Parameters:**
- object

- The object to remove.

---

#### boolean containsObservedObject​(
ObjectName
object)

Tests whether the specified object is in the set of observed MBeans.

**Parameters:**
- object

- The object to check.

**Returns:**
- true

if the specified object is in the set,

false

otherwise.

---

#### ObjectName
[] getObservedObjects()

Returns an array containing the objects being observed.

**Returns:**
- The objects being observed.

---

#### @Deprecated

ObjectName
getObservedObject()

Gets the object name of the object being observed.

**Returns:**
- The object being observed.

**See Also:**
- setObservedObject(javax.management.ObjectName)

---

#### @Deprecated

void setObservedObject​(
ObjectName
object)

Sets the object to observe identified by its object name.

**Parameters:**
- object

- The object to observe.

**See Also:**
- getObservedObject()

---

#### String
getObservedAttribute()

Gets the attribute being observed.

**Returns:**
- The attribute being observed.

**See Also:**
- setObservedAttribute(java.lang.String)

---

#### void setObservedAttribute​(
String
attribute)

Sets the attribute to observe.

**Parameters:**
- attribute

- The attribute to observe.

**See Also:**
- getObservedAttribute()

---

#### long getGranularityPeriod()

Gets the granularity period (in milliseconds).

**Returns:**
- The granularity period.

**See Also:**
- setGranularityPeriod(long)

---

#### void setGranularityPeriod​(long period)
throws
IllegalArgumentException

Sets the granularity period (in milliseconds).

**Parameters:**
- period

- The granularity period.

**Throws:**
- IllegalArgumentException

- The granularity
period is less than or equal to zero.

**See Also:**
- getGranularityPeriod()

---

#### boolean isActive()

Tests if the monitor MBean is active.
A monitor MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

**Returns:**
- true

if the monitor MBean is active,

false

otherwise.

---

### Additional Sections

#### Interface MonitorMBean

**All Known Subinterfaces:** CounterMonitorMBean

,

GaugeMonitorMBean

,

StringMonitorMBean

**All Known Implementing Classes:** CounterMonitor

,

GaugeMonitor

,

Monitor

,

StringMonitor

```java
public interface
MonitorMBean
```

Exposes the remote management interface of monitor MBeans.

**Since:** 1.5

public interface

MonitorMBean

Exposes the remote management interface of monitor MBeans.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObservedObject

​(

ObjectName

object)

Adds the specified object in the set of observed MBeans.

boolean

containsObservedObject

​(

ObjectName

object)

Tests whether the specified object is in the set of observed MBeans.

long

getGranularityPeriod

()

Gets the granularity period (in milliseconds).

String

getObservedAttribute

()

Gets the attribute being observed.

ObjectName

getObservedObject

()

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

ObjectName

[]

getObservedObjects

()

Returns an array containing the objects being observed.

boolean

isActive

()

Tests if the monitor MBean is active.

void

removeObservedObject

​(

ObjectName

object)

Removes the specified object from the set of observed MBeans.

void

setGranularityPeriod

​(long period)

Sets the granularity period (in milliseconds).

void

setObservedAttribute

​(

String

attribute)

Sets the attribute to observe.

void

setObservedObject

​(

ObjectName

object)

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

void

start

()

Starts the monitor.

void

stop

()

Stops the monitor.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObservedObject

​(

ObjectName

object)

Adds the specified object in the set of observed MBeans.

boolean

containsObservedObject

​(

ObjectName

object)

Tests whether the specified object is in the set of observed MBeans.

long

getGranularityPeriod

()

Gets the granularity period (in milliseconds).

String

getObservedAttribute

()

Gets the attribute being observed.

ObjectName

getObservedObject

()

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

ObjectName

[]

getObservedObjects

()

Returns an array containing the objects being observed.

boolean

isActive

()

Tests if the monitor MBean is active.

void

removeObservedObject

​(

ObjectName

object)

Removes the specified object from the set of observed MBeans.

void

setGranularityPeriod

​(long period)

Sets the granularity period (in milliseconds).

void

setObservedAttribute

​(

String

attribute)

Sets the attribute to observe.

void

setObservedObject

​(

ObjectName

object)

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

void

start

()

Starts the monitor.

void

stop

()

Stops the monitor.

---

#### Method Summary

Adds the specified object in the set of observed MBeans.

Tests whether the specified object is in the set of observed MBeans.

Gets the granularity period (in milliseconds).

Gets the attribute being observed.

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Returns an array containing the objects being observed.

Tests if the monitor MBean is active.

Removes the specified object from the set of observed MBeans.

Sets the granularity period (in milliseconds).

Sets the attribute to observe.

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Starts the monitor.

Stops the monitor.

============ METHOD DETAIL ==========

- Method Detail

- start

```java
void start()
```

Starts the monitor.

- stop

```java
void stop()
```

Stops the monitor.

- addObservedObject

```java
void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans.

**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- the specified object is null.

- removeObservedObject

```java
void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Parameters:** object

- The object to remove.

- containsObservedObject

```java
boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is in the set,

false

otherwise.

- getObservedObjects

```java
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Returns:** The objects being observed.

- getObservedObject

```java
@Deprecated

ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Gets the object name of the object being observed.

**Returns:** The object being observed.
**See Also:** setObservedObject(javax.management.ObjectName)

- setObservedObject

```java
@Deprecated

void setObservedObject​(
ObjectName
object)
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Sets the object to observe identified by its object name.

**Parameters:** object

- The object to observe.
**See Also:** getObservedObject()

- getObservedAttribute

```java
String
getObservedAttribute()
```

Gets the attribute being observed.

**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

- setObservedAttribute

```java
void setObservedAttribute​(
String
attribute)
```

Sets the attribute to observe.

**Parameters:** attribute

- The attribute to observe.
**See Also:** getObservedAttribute()

- getGranularityPeriod

```java
long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

**Returns:** The granularity period.
**See Also:** setGranularityPeriod(long)

- setGranularityPeriod

```java
void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

**Parameters:** period

- The granularity period.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

- isActive

```java
boolean isActive()
```

Tests if the monitor MBean is active.
A monitor MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

**Returns:** true

if the monitor MBean is active,

false

otherwise.

Method Detail

- start

```java
void start()
```

Starts the monitor.

- stop

```java
void stop()
```

Stops the monitor.

- addObservedObject

```java
void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans.

**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- the specified object is null.

- removeObservedObject

```java
void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Parameters:** object

- The object to remove.

- containsObservedObject

```java
boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is in the set,

false

otherwise.

- getObservedObjects

```java
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Returns:** The objects being observed.

- getObservedObject

```java
@Deprecated

ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Gets the object name of the object being observed.

**Returns:** The object being observed.
**See Also:** setObservedObject(javax.management.ObjectName)

- setObservedObject

```java
@Deprecated

void setObservedObject​(
ObjectName
object)
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Sets the object to observe identified by its object name.

**Parameters:** object

- The object to observe.
**See Also:** getObservedObject()

- getObservedAttribute

```java
String
getObservedAttribute()
```

Gets the attribute being observed.

**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

- setObservedAttribute

```java
void setObservedAttribute​(
String
attribute)
```

Sets the attribute to observe.

**Parameters:** attribute

- The attribute to observe.
**See Also:** getObservedAttribute()

- getGranularityPeriod

```java
long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

**Returns:** The granularity period.
**See Also:** setGranularityPeriod(long)

- setGranularityPeriod

```java
void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

**Parameters:** period

- The granularity period.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

- isActive

```java
boolean isActive()
```

Tests if the monitor MBean is active.
A monitor MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

**Returns:** true

if the monitor MBean is active,

false

otherwise.

---

#### Method Detail

start

```java
void start()
```

Starts the monitor.

---

#### start

void start()

Starts the monitor.

stop

```java
void stop()
```

Stops the monitor.

---

#### stop

void stop()

Stops the monitor.

addObservedObject

```java
void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans.

**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- the specified object is null.

---

#### addObservedObject

void addObservedObject​(

ObjectName

object)
throws

IllegalArgumentException

Adds the specified object in the set of observed MBeans.

removeObservedObject

```java
void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Parameters:** object

- The object to remove.

---

#### removeObservedObject

void removeObservedObject​(

ObjectName

object)

Removes the specified object from the set of observed MBeans.

containsObservedObject

```java
boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is in the set,

false

otherwise.

---

#### containsObservedObject

boolean containsObservedObject​(

ObjectName

object)

Tests whether the specified object is in the set of observed MBeans.

getObservedObjects

```java
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Returns:** The objects being observed.

---

#### getObservedObjects

ObjectName

[] getObservedObjects()

Returns an array containing the objects being observed.

getObservedObject

```java
@Deprecated

ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Gets the object name of the object being observed.

**Returns:** The object being observed.
**See Also:** setObservedObject(javax.management.ObjectName)

---

#### getObservedObject

@Deprecated

ObjectName

getObservedObject()

Gets the object name of the object being observed.

setObservedObject

```java
@Deprecated

void setObservedObject​(
ObjectName
object)
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Sets the object to observe identified by its object name.

**Parameters:** object

- The object to observe.
**See Also:** getObservedObject()

---

#### setObservedObject

@Deprecated

void setObservedObject​(

ObjectName

object)

Sets the object to observe identified by its object name.

getObservedAttribute

```java
String
getObservedAttribute()
```

Gets the attribute being observed.

**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

---

#### getObservedAttribute

String

getObservedAttribute()

Gets the attribute being observed.

setObservedAttribute

```java
void setObservedAttribute​(
String
attribute)
```

Sets the attribute to observe.

**Parameters:** attribute

- The attribute to observe.
**See Also:** getObservedAttribute()

---

#### setObservedAttribute

void setObservedAttribute​(

String

attribute)

Sets the attribute to observe.

getGranularityPeriod

```java
long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

**Returns:** The granularity period.
**See Also:** setGranularityPeriod(long)

---

#### getGranularityPeriod

long getGranularityPeriod()

Gets the granularity period (in milliseconds).

setGranularityPeriod

```java
void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

**Parameters:** period

- The granularity period.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

---

#### setGranularityPeriod

void setGranularityPeriod​(long period)
throws

IllegalArgumentException

Sets the granularity period (in milliseconds).

isActive

```java
boolean isActive()
```

Tests if the monitor MBean is active.
A monitor MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

**Returns:** true

if the monitor MBean is active,

false

otherwise.

---

#### isActive

boolean isActive()

Tests if the monitor MBean is active.
A monitor MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

---

