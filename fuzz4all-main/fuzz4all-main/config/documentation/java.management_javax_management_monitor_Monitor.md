# Class Monitor

**Source:** `java.management\javax\management\monitor\Monitor.html`

### Class Description

```java
public abstract class
Monitor

extends
NotificationBroadcasterSupport

implements
MonitorMBean
,
MBeanRegistration
```

Defines the part common to all monitor MBeans.
A monitor MBean monitors values of an attribute common to a set of observed
MBeans. The observed attribute is monitored at intervals specified by the
granularity period. A gauge value (derived gauge) is derived from the values
of the observed attribute.

**All Implemented Interfaces:** MBeanRegistration

,

MonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

#### protected static final int capacityIncrement

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

**See Also:**
- Constant Field Values

---

#### protected int elementCount

The number of valid components in the vector of observed objects.

---

#### @Deprecated

protected int alreadyNotified

Monitor errors that have already been notified.

---

#### protected int[] alreadyNotifieds

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

---

#### protected
MBeanServer
server

Reference to the MBean server. This reference is null when the
monitor MBean is not registered in an MBean server. This
reference is initialized before the monitor MBean is registered
in the MBean server.

**See Also:**
- preRegister(MBeanServer server, ObjectName name)

---

#### protected static final int RESET_FLAGS_ALREADY_NOTIFIED

This flag is used to reset the

alreadyNotifieds

monitor attribute.

**See Also:**
- Constant Field Values

---

#### protected static final int OBSERVED_OBJECT_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object. This flag is used to check that the new
observed object is registered in the MBean server at the time
of the first notification.

**See Also:**
- Constant Field Values

---

#### protected static final int OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed attribute. This flag is used to check that the
new observed attribute belongs to the observed object at the
time of the first notification.

**See Also:**
- Constant Field Values

---

#### protected static final int OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to check that the observed attribute type is correct
(depending on the monitor in use) at the time of the first
notification.

**See Also:**
- Constant Field Values

---

#### protected static final int RUNTIME_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to notify any exception (except the cases described above)
when trying to get the value of the observed attribute at the
time of the first notification.

**See Also:**
- Constant Field Values

---

#### @Deprecated

protected
String
dbgTag

This field is retained for compatibility but should not be referenced.

---

### Constructor Details

#### public Monitor()

*No description found.*

---

### Method Details

#### public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Initializes the reference to the MBean server.

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- server

- The MBean server in which the monitor MBean will
be registered.
- name

- The object name of the monitor MBean.

**Returns:**
- The name of the monitor MBean registered.

**Throws:**
- Exception

- if something goes wrong

---

#### public void postRegister​(
Boolean
registrationDone)

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Not used in this context.

**Specified by:**
- postRegister

in interface

MBeanRegistration

**Parameters:**
- registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

---

#### public void preDeregister()
throws
Exception

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Stops the monitor.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- Exception

- if something goes wrong

---

#### public void postDeregister()

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Not used in this context.

**Specified by:**
- postDeregister

in interface

MBeanRegistration

---

#### public abstract void start()

Starts the monitor.

**Specified by:**
- start

in interface

MonitorMBean

---

#### public abstract void stop()

Stops the monitor.

**Specified by:**
- stop

in interface

MonitorMBean

---

#### @Deprecated

public
ObjectName
getObservedObject()

Returns the object name of the first object in the set of observed
MBeans, or

null

if there is no such object.

**Specified by:**
- getObservedObject

in interface

MonitorMBean

**Returns:**
- The object being observed.

**See Also:**
- setObservedObject(ObjectName)

---

#### @Deprecated

public void setObservedObject​(
ObjectName
object)
throws
IllegalArgumentException

Removes all objects from the set of observed objects, and then adds the
specified object.

**Specified by:**
- setObservedObject

in interface

MonitorMBean

**Parameters:**
- object

- The object to observe.

**Throws:**
- IllegalArgumentException

- The specified
object is null.

**See Also:**
- getObservedObject()

---

#### public void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException

Adds the specified object in the set of observed MBeans, if this object
is not already present.

**Specified by:**
- addObservedObject

in interface

MonitorMBean

**Parameters:**
- object

- The object to observe.

**Throws:**
- IllegalArgumentException

- The specified object is null.

---

#### public void removeObservedObject​(
ObjectName
object)

Removes the specified object from the set of observed MBeans.

**Specified by:**
- removeObservedObject

in interface

MonitorMBean

**Parameters:**
- object

- The object to remove.

---

#### public boolean containsObservedObject​(
ObjectName
object)

Tests whether the specified object is in the set of observed MBeans.

**Specified by:**
- containsObservedObject

in interface

MonitorMBean

**Parameters:**
- object

- The object to check.

**Returns:**
- true

if the specified object is present,

false

otherwise.

---

#### public
ObjectName
[] getObservedObjects()

Returns an array containing the objects being observed.

**Specified by:**
- getObservedObjects

in interface

MonitorMBean

**Returns:**
- The objects being observed.

---

#### public
String
getObservedAttribute()

Gets the attribute being observed.

The observed attribute is not initialized by default (set to null).

**Specified by:**
- getObservedAttribute

in interface

MonitorMBean

**Returns:**
- The attribute being observed.

**See Also:**
- setObservedAttribute(java.lang.String)

---

#### public void setObservedAttribute​(
String
attribute)
throws
IllegalArgumentException

Sets the attribute to observe.

The observed attribute is not initialized by default (set to null).

**Specified by:**
- setObservedAttribute

in interface

MonitorMBean

**Parameters:**
- attribute

- The attribute to observe.

**Throws:**
- IllegalArgumentException

- The specified
attribute is null.

**See Also:**
- getObservedAttribute()

---

#### public long getGranularityPeriod()

Gets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:**
- getGranularityPeriod

in interface

MonitorMBean

**Returns:**
- The granularity period value.

**See Also:**
- setGranularityPeriod(long)

---

#### public void setGranularityPeriod​(long period)
throws
IllegalArgumentException

Sets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:**
- setGranularityPeriod

in interface

MonitorMBean

**Parameters:**
- period

- The granularity period value.

**Throws:**
- IllegalArgumentException

- The granularity
period is less than or equal to zero.

**See Also:**
- getGranularityPeriod()

---

#### public boolean isActive()

Tests whether the monitor MBean is active. A monitor MBean is
marked active when the

start

method is called.
It becomes inactive when the

stop

method is
called.

**Specified by:**
- isActive

in interface

MonitorMBean

**Returns:**
- true

if the monitor MBean is active,

false

otherwise.

---

### Additional Sections

#### Class Monitor

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.monitor.Monitor

javax.management.NotificationBroadcasterSupport

- javax.management.monitor.Monitor

javax.management.monitor.Monitor

**All Implemented Interfaces:** MBeanRegistration

,

MonitorMBean

,

NotificationBroadcaster

,

NotificationEmitter

**Direct Known Subclasses:** CounterMonitor

,

GaugeMonitor

,

StringMonitor

```java
public abstract class
Monitor

extends
NotificationBroadcasterSupport

implements
MonitorMBean
,
MBeanRegistration
```

Defines the part common to all monitor MBeans.
A monitor MBean monitors values of an attribute common to a set of observed
MBeans. The observed attribute is monitored at intervals specified by the
granularity period. A gauge value (derived gauge) is derived from the values
of the observed attribute.

**Since:** 1.5

public abstract class

Monitor

extends

NotificationBroadcasterSupport

implements

MonitorMBean

,

MBeanRegistration

Defines the part common to all monitor MBeans.
A monitor MBean monitors values of an attribute common to a set of observed
MBeans. The observed attribute is monitored at intervals specified by the
granularity period. A gauge value (derived gauge) is derived from the values
of the observed attribute.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

alreadyNotified

Deprecated.

equivalent to

alreadyNotifieds

[0].

protected int[]

alreadyNotifieds

Selected monitor errors that have already been notified.

protected static int

capacityIncrement

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

protected

String

dbgTag

Deprecated.

No replacement.

protected int

elementCount

The number of valid components in the vector of observed objects.

protected static int

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed attribute.

protected static int

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute.

protected static int

OBSERVED_OBJECT_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object.

protected static int

RESET_FLAGS_ALREADY_NOTIFIED

This flag is used to reset the

alreadyNotifieds

monitor attribute.

protected static int

RUNTIME_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute.

protected

MBeanServer

server

Reference to the MBean server.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Monitor

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObservedObject

​(

ObjectName

object)

Adds the specified object in the set of observed MBeans, if this object
is not already present.

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

Tests whether the monitor MBean is active.

void

postDeregister

()

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

void

preDeregister

()

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

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

abstract void

start

()

Starts the monitor.

abstract void

stop

()

Stops the monitor.

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

- Methods declared in interface javax.management.

NotificationBroadcaster

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Field Summary

Fields

Modifier and Type

Field

Description

protected int

alreadyNotified

Deprecated.

equivalent to

alreadyNotifieds

[0].

protected int[]

alreadyNotifieds

Selected monitor errors that have already been notified.

protected static int

capacityIncrement

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

protected

String

dbgTag

Deprecated.

No replacement.

protected int

elementCount

The number of valid components in the vector of observed objects.

protected static int

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed attribute.

protected static int

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute.

protected static int

OBSERVED_OBJECT_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object.

protected static int

RESET_FLAGS_ALREADY_NOTIFIED

This flag is used to reset the

alreadyNotifieds

monitor attribute.

protected static int

RUNTIME_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute.

protected

MBeanServer

server

Reference to the MBean server.

---

#### Field Summary

Deprecated.

equivalent to

alreadyNotifieds

[0].

Selected monitor errors that have already been notified.

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

Deprecated.

No replacement.

The number of valid components in the vector of observed objects.

Flag denoting that a notification has occurred after changing
the observed attribute.

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute.

Flag denoting that a notification has occurred after changing
the observed object.

This flag is used to reset the

alreadyNotifieds

monitor attribute.

Reference to the MBean server.

Constructor Summary

Constructors

Constructor

Description

Monitor

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addObservedObject

​(

ObjectName

object)

Adds the specified object in the set of observed MBeans, if this object
is not already present.

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

Tests whether the monitor MBean is active.

void

postDeregister

()

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

void

preDeregister

()

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

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

abstract void

start

()

Starts the monitor.

abstract void

stop

()

Stops the monitor.

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

- Methods declared in interface javax.management.

NotificationBroadcaster

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Adds the specified object in the set of observed MBeans, if this object
is not already present.

Tests whether the specified object is in the set of observed MBeans.

Gets the granularity period (in milliseconds).

Gets the attribute being observed.

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Returns an array containing the objects being observed.

Tests whether the monitor MBean is active.

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Removes the specified object from the set of observed MBeans.

Sets the granularity period (in milliseconds).

Sets the attribute to observe.

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Starts the monitor.

Stops the monitor.

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

Methods declared in interface javax.management.

NotificationBroadcaster

getNotificationInfo

,

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationBroadcaster

Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Methods declared in interface javax.management. NotificationEmitter

============ FIELD DETAIL ===========

- Field Detail

- capacityIncrement

```java
protected static final int capacityIncrement
```

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

**See Also:** Constant Field Values

- elementCount

```java
protected int elementCount
```

The number of valid components in the vector of observed objects.

- alreadyNotified

```java
@Deprecated

protected int alreadyNotified
```

Deprecated.

equivalent to

alreadyNotifieds

[0].

Monitor errors that have already been notified.

- alreadyNotifieds

```java
protected int[] alreadyNotifieds
```

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

- server

```java
protected
MBeanServer
server
```

Reference to the MBean server. This reference is null when the
monitor MBean is not registered in an MBean server. This
reference is initialized before the monitor MBean is registered
in the MBean server.

**See Also:** preRegister(MBeanServer server, ObjectName name)

- RESET_FLAGS_ALREADY_NOTIFIED

```java
protected static final int RESET_FLAGS_ALREADY_NOTIFIED
```

This flag is used to reset the

alreadyNotifieds

monitor attribute.

**See Also:** Constant Field Values

- OBSERVED_OBJECT_ERROR_NOTIFIED

```java
protected static final int OBSERVED_OBJECT_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object. This flag is used to check that the new
observed object is registered in the MBean server at the time
of the first notification.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed attribute. This flag is used to check that the
new observed attribute belongs to the observed object at the
time of the first notification.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to check that the observed attribute type is correct
(depending on the monitor in use) at the time of the first
notification.

**See Also:** Constant Field Values

- RUNTIME_ERROR_NOTIFIED

```java
protected static final int RUNTIME_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to notify any exception (except the cases described above)
when trying to get the value of the observed attribute at the
time of the first notification.

**See Also:** Constant Field Values

- dbgTag

```java
@Deprecated

protected
String
dbgTag
```

Deprecated.

No replacement.

This field is retained for compatibility but should not be referenced.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Monitor

```java
public Monitor()
```

============ METHOD DETAIL ==========

- Method Detail

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Initializes the reference to the MBean server.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the monitor MBean will
be registered.
**Parameters:** name

- The object name of the monitor MBean.
**Returns:** The name of the monitor MBean registered.
**Throws:** Exception

- if something goes wrong

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Not used in this context.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Stops the monitor.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- if something goes wrong

- postDeregister

```java
public void postDeregister()
```

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

- start

```java
public abstract void start()
```

Starts the monitor.

**Specified by:** start

in interface

MonitorMBean

- stop

```java
public abstract void stop()
```

Stops the monitor.

**Specified by:** stop

in interface

MonitorMBean

- getObservedObject

```java
@Deprecated

public
ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Returns the object name of the first object in the set of observed
MBeans, or

null

if there is no such object.

**Specified by:** getObservedObject

in interface

MonitorMBean
**Returns:** The object being observed.
**See Also:** setObservedObject(ObjectName)

- setObservedObject

```java
@Deprecated

public void setObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Removes all objects from the set of observed objects, and then adds the
specified object.

**Specified by:** setObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified
object is null.
**See Also:** getObservedObject()

- addObservedObject

```java
public void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans, if this object
is not already present.

**Specified by:** addObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified object is null.

- removeObservedObject

```java
public void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Specified by:** removeObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to remove.

- containsObservedObject

```java
public boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Specified by:** containsObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is present,

false

otherwise.

- getObservedObjects

```java
public
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Specified by:** getObservedObjects

in interface

MonitorMBean
**Returns:** The objects being observed.

- getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the attribute being observed.

The observed attribute is not initialized by default (set to null).

**Specified by:** getObservedAttribute

in interface

MonitorMBean
**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

- setObservedAttribute

```java
public void setObservedAttribute​(
String
attribute)
throws
IllegalArgumentException
```

Sets the attribute to observe.

The observed attribute is not initialized by default (set to null).

**Specified by:** setObservedAttribute

in interface

MonitorMBean
**Parameters:** attribute

- The attribute to observe.
**Throws:** IllegalArgumentException

- The specified
attribute is null.
**See Also:** getObservedAttribute()

- getGranularityPeriod

```java
public long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** getGranularityPeriod

in interface

MonitorMBean
**Returns:** The granularity period value.
**See Also:** setGranularityPeriod(long)

- setGranularityPeriod

```java
public void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** setGranularityPeriod

in interface

MonitorMBean
**Parameters:** period

- The granularity period value.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

- isActive

```java
public boolean isActive()
```

Tests whether the monitor MBean is active. A monitor MBean is
marked active when the

start

method is called.
It becomes inactive when the

stop

method is
called.

**Specified by:** isActive

in interface

MonitorMBean
**Returns:** true

if the monitor MBean is active,

false

otherwise.

Field Detail

- capacityIncrement

```java
protected static final int capacityIncrement
```

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

**See Also:** Constant Field Values

- elementCount

```java
protected int elementCount
```

The number of valid components in the vector of observed objects.

- alreadyNotified

```java
@Deprecated

protected int alreadyNotified
```

Deprecated.

equivalent to

alreadyNotifieds

[0].

Monitor errors that have already been notified.

- alreadyNotifieds

```java
protected int[] alreadyNotifieds
```

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

- server

```java
protected
MBeanServer
server
```

Reference to the MBean server. This reference is null when the
monitor MBean is not registered in an MBean server. This
reference is initialized before the monitor MBean is registered
in the MBean server.

**See Also:** preRegister(MBeanServer server, ObjectName name)

- RESET_FLAGS_ALREADY_NOTIFIED

```java
protected static final int RESET_FLAGS_ALREADY_NOTIFIED
```

This flag is used to reset the

alreadyNotifieds

monitor attribute.

**See Also:** Constant Field Values

- OBSERVED_OBJECT_ERROR_NOTIFIED

```java
protected static final int OBSERVED_OBJECT_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object. This flag is used to check that the new
observed object is registered in the MBean server at the time
of the first notification.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed attribute. This flag is used to check that the
new observed attribute belongs to the observed object at the
time of the first notification.

**See Also:** Constant Field Values

- OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to check that the observed attribute type is correct
(depending on the monitor in use) at the time of the first
notification.

**See Also:** Constant Field Values

- RUNTIME_ERROR_NOTIFIED

```java
protected static final int RUNTIME_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to notify any exception (except the cases described above)
when trying to get the value of the observed attribute at the
time of the first notification.

**See Also:** Constant Field Values

- dbgTag

```java
@Deprecated

protected
String
dbgTag
```

Deprecated.

No replacement.

This field is retained for compatibility but should not be referenced.

---

#### Field Detail

capacityIncrement

```java
protected static final int capacityIncrement
```

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

**See Also:** Constant Field Values

---

#### capacityIncrement

protected static final int capacityIncrement

The amount by which the capacity of the monitor arrays are
automatically incremented when their size becomes greater than
their capacity.

elementCount

```java
protected int elementCount
```

The number of valid components in the vector of observed objects.

---

#### elementCount

protected int elementCount

The number of valid components in the vector of observed objects.

alreadyNotified

```java
@Deprecated

protected int alreadyNotified
```

Deprecated.

equivalent to

alreadyNotifieds

[0].

Monitor errors that have already been notified.

---

#### alreadyNotified

@Deprecated

protected int alreadyNotified

Monitor errors that have already been notified.

alreadyNotifieds

```java
protected int[] alreadyNotifieds
```

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

---

#### alreadyNotifieds

protected int[] alreadyNotifieds

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

Selected monitor errors that have already been notified.

Each element in this array corresponds to an observed object
in the vector. It contains a bit mask of the flags

OBSERVED_OBJECT_ERROR_NOTIFIED

etc, indicating whether the
corresponding notification has already been sent for the MBean
being monitored.

server

```java
protected
MBeanServer
server
```

Reference to the MBean server. This reference is null when the
monitor MBean is not registered in an MBean server. This
reference is initialized before the monitor MBean is registered
in the MBean server.

**See Also:** preRegister(MBeanServer server, ObjectName name)

---

#### server

protected

MBeanServer

server

Reference to the MBean server. This reference is null when the
monitor MBean is not registered in an MBean server. This
reference is initialized before the monitor MBean is registered
in the MBean server.

RESET_FLAGS_ALREADY_NOTIFIED

```java
protected static final int RESET_FLAGS_ALREADY_NOTIFIED
```

This flag is used to reset the

alreadyNotifieds

monitor attribute.

**See Also:** Constant Field Values

---

#### RESET_FLAGS_ALREADY_NOTIFIED

protected static final int RESET_FLAGS_ALREADY_NOTIFIED

This flag is used to reset the

alreadyNotifieds

monitor attribute.

OBSERVED_OBJECT_ERROR_NOTIFIED

```java
protected static final int OBSERVED_OBJECT_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object. This flag is used to check that the new
observed object is registered in the MBean server at the time
of the first notification.

**See Also:** Constant Field Values

---

#### OBSERVED_OBJECT_ERROR_NOTIFIED

protected static final int OBSERVED_OBJECT_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object. This flag is used to check that the new
observed object is registered in the MBean server at the time
of the first notification.

OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed attribute. This flag is used to check that the
new observed attribute belongs to the observed object at the
time of the first notification.

**See Also:** Constant Field Values

---

#### OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

protected static final int OBSERVED_ATTRIBUTE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed attribute. This flag is used to check that the
new observed attribute belongs to the observed object at the
time of the first notification.

OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

```java
protected static final int OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to check that the observed attribute type is correct
(depending on the monitor in use) at the time of the first
notification.

**See Also:** Constant Field Values

---

#### OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

protected static final int OBSERVED_ATTRIBUTE_TYPE_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to check that the observed attribute type is correct
(depending on the monitor in use) at the time of the first
notification.

RUNTIME_ERROR_NOTIFIED

```java
protected static final int RUNTIME_ERROR_NOTIFIED
```

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to notify any exception (except the cases described above)
when trying to get the value of the observed attribute at the
time of the first notification.

**See Also:** Constant Field Values

---

#### RUNTIME_ERROR_NOTIFIED

protected static final int RUNTIME_ERROR_NOTIFIED

Flag denoting that a notification has occurred after changing
the observed object or the observed attribute. This flag is
used to notify any exception (except the cases described above)
when trying to get the value of the observed attribute at the
time of the first notification.

dbgTag

```java
@Deprecated

protected
String
dbgTag
```

Deprecated.

No replacement.

This field is retained for compatibility but should not be referenced.

---

#### dbgTag

@Deprecated

protected

String

dbgTag

This field is retained for compatibility but should not be referenced.

Constructor Detail

- Monitor

```java
public Monitor()
```

---

#### Constructor Detail

Monitor

```java
public Monitor()
```

---

#### Monitor

public Monitor()

Method Detail

- preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Initializes the reference to the MBean server.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the monitor MBean will
be registered.
**Parameters:** name

- The object name of the monitor MBean.
**Returns:** The name of the monitor MBean registered.
**Throws:** Exception

- if something goes wrong

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Not used in this context.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

- preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Stops the monitor.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- if something goes wrong

- postDeregister

```java
public void postDeregister()
```

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

- start

```java
public abstract void start()
```

Starts the monitor.

**Specified by:** start

in interface

MonitorMBean

- stop

```java
public abstract void stop()
```

Stops the monitor.

**Specified by:** stop

in interface

MonitorMBean

- getObservedObject

```java
@Deprecated

public
ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Returns the object name of the first object in the set of observed
MBeans, or

null

if there is no such object.

**Specified by:** getObservedObject

in interface

MonitorMBean
**Returns:** The object being observed.
**See Also:** setObservedObject(ObjectName)

- setObservedObject

```java
@Deprecated

public void setObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Removes all objects from the set of observed objects, and then adds the
specified object.

**Specified by:** setObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified
object is null.
**See Also:** getObservedObject()

- addObservedObject

```java
public void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans, if this object
is not already present.

**Specified by:** addObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified object is null.

- removeObservedObject

```java
public void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Specified by:** removeObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to remove.

- containsObservedObject

```java
public boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Specified by:** containsObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is present,

false

otherwise.

- getObservedObjects

```java
public
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Specified by:** getObservedObjects

in interface

MonitorMBean
**Returns:** The objects being observed.

- getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the attribute being observed.

The observed attribute is not initialized by default (set to null).

**Specified by:** getObservedAttribute

in interface

MonitorMBean
**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

- setObservedAttribute

```java
public void setObservedAttribute​(
String
attribute)
throws
IllegalArgumentException
```

Sets the attribute to observe.

The observed attribute is not initialized by default (set to null).

**Specified by:** setObservedAttribute

in interface

MonitorMBean
**Parameters:** attribute

- The attribute to observe.
**Throws:** IllegalArgumentException

- The specified
attribute is null.
**See Also:** getObservedAttribute()

- getGranularityPeriod

```java
public long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** getGranularityPeriod

in interface

MonitorMBean
**Returns:** The granularity period value.
**See Also:** setGranularityPeriod(long)

- setGranularityPeriod

```java
public void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** setGranularityPeriod

in interface

MonitorMBean
**Parameters:** period

- The granularity period value.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

- isActive

```java
public boolean isActive()
```

Tests whether the monitor MBean is active. A monitor MBean is
marked active when the

start

method is called.
It becomes inactive when the

stop

method is
called.

**Specified by:** isActive

in interface

MonitorMBean
**Returns:** true

if the monitor MBean is active,

false

otherwise.

---

#### Method Detail

preRegister

```java
public
ObjectName
preRegister​(
MBeanServer
server,

ObjectName
name)
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Initializes the reference to the MBean server.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the monitor MBean will
be registered.
**Parameters:** name

- The object name of the monitor MBean.
**Returns:** The name of the monitor MBean registered.
**Throws:** Exception

- if something goes wrong

---

#### preRegister

public

ObjectName

preRegister​(

MBeanServer

server,

ObjectName

name)
throws

Exception

Allows the monitor MBean to perform any operations it needs
before being registered in the MBean server.

Initializes the reference to the MBean server.

Initializes the reference to the MBean server.

postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Not used in this context.

**Specified by:** postRegister

in interface

MBeanRegistration
**Parameters:** registrationDone

- Indicates whether or not the MBean has
been successfully registered in the MBean server. The value
false means that the registration phase has failed.

---

#### postRegister

public void postRegister​(

Boolean

registrationDone)

Allows the monitor MBean to perform any operations needed after
having been registered in the MBean server or after the
registration has failed.

Not used in this context.

Not used in this context.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Stops the monitor.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- if something goes wrong

---

#### preDeregister

public void preDeregister()
throws

Exception

Allows the monitor MBean to perform any operations it needs
before being unregistered by the MBean server.

Stops the monitor.

Stops the monitor.

postDeregister

```java
public void postDeregister()
```

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

---

#### postDeregister

public void postDeregister()

Allows the monitor MBean to perform any operations needed after
having been unregistered by the MBean server.

Not used in this context.

Not used in this context.

start

```java
public abstract void start()
```

Starts the monitor.

**Specified by:** start

in interface

MonitorMBean

---

#### start

public abstract void start()

Starts the monitor.

stop

```java
public abstract void stop()
```

Stops the monitor.

**Specified by:** stop

in interface

MonitorMBean

---

#### stop

public abstract void stop()

Stops the monitor.

getObservedObject

```java
@Deprecated

public
ObjectName
getObservedObject()
```

Deprecated.

As of JMX 1.2, replaced by

getObservedObjects()

Returns the object name of the first object in the set of observed
MBeans, or

null

if there is no such object.

**Specified by:** getObservedObject

in interface

MonitorMBean
**Returns:** The object being observed.
**See Also:** setObservedObject(ObjectName)

---

#### getObservedObject

@Deprecated

public

ObjectName

getObservedObject()

Returns the object name of the first object in the set of observed
MBeans, or

null

if there is no such object.

setObservedObject

```java
@Deprecated

public void setObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Deprecated.

As of JMX 1.2, replaced by

addObservedObject(javax.management.ObjectName)

Removes all objects from the set of observed objects, and then adds the
specified object.

**Specified by:** setObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified
object is null.
**See Also:** getObservedObject()

---

#### setObservedObject

@Deprecated

public void setObservedObject​(

ObjectName

object)
throws

IllegalArgumentException

Removes all objects from the set of observed objects, and then adds the
specified object.

addObservedObject

```java
public void addObservedObject​(
ObjectName
object)
throws
IllegalArgumentException
```

Adds the specified object in the set of observed MBeans, if this object
is not already present.

**Specified by:** addObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to observe.
**Throws:** IllegalArgumentException

- The specified object is null.

---

#### addObservedObject

public void addObservedObject​(

ObjectName

object)
throws

IllegalArgumentException

Adds the specified object in the set of observed MBeans, if this object
is not already present.

removeObservedObject

```java
public void removeObservedObject​(
ObjectName
object)
```

Removes the specified object from the set of observed MBeans.

**Specified by:** removeObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to remove.

---

#### removeObservedObject

public void removeObservedObject​(

ObjectName

object)

Removes the specified object from the set of observed MBeans.

containsObservedObject

```java
public boolean containsObservedObject​(
ObjectName
object)
```

Tests whether the specified object is in the set of observed MBeans.

**Specified by:** containsObservedObject

in interface

MonitorMBean
**Parameters:** object

- The object to check.
**Returns:** true

if the specified object is present,

false

otherwise.

---

#### containsObservedObject

public boolean containsObservedObject​(

ObjectName

object)

Tests whether the specified object is in the set of observed MBeans.

getObservedObjects

```java
public
ObjectName
[] getObservedObjects()
```

Returns an array containing the objects being observed.

**Specified by:** getObservedObjects

in interface

MonitorMBean
**Returns:** The objects being observed.

---

#### getObservedObjects

public

ObjectName

[] getObservedObjects()

Returns an array containing the objects being observed.

getObservedAttribute

```java
public
String
getObservedAttribute()
```

Gets the attribute being observed.

The observed attribute is not initialized by default (set to null).

**Specified by:** getObservedAttribute

in interface

MonitorMBean
**Returns:** The attribute being observed.
**See Also:** setObservedAttribute(java.lang.String)

---

#### getObservedAttribute

public

String

getObservedAttribute()

Gets the attribute being observed.

The observed attribute is not initialized by default (set to null).

setObservedAttribute

```java
public void setObservedAttribute​(
String
attribute)
throws
IllegalArgumentException
```

Sets the attribute to observe.

The observed attribute is not initialized by default (set to null).

**Specified by:** setObservedAttribute

in interface

MonitorMBean
**Parameters:** attribute

- The attribute to observe.
**Throws:** IllegalArgumentException

- The specified
attribute is null.
**See Also:** getObservedAttribute()

---

#### setObservedAttribute

public void setObservedAttribute​(

String

attribute)
throws

IllegalArgumentException

Sets the attribute to observe.

The observed attribute is not initialized by default (set to null).

getGranularityPeriod

```java
public long getGranularityPeriod()
```

Gets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** getGranularityPeriod

in interface

MonitorMBean
**Returns:** The granularity period value.
**See Also:** setGranularityPeriod(long)

---

#### getGranularityPeriod

public long getGranularityPeriod()

Gets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

setGranularityPeriod

```java
public void setGranularityPeriod​(long period)
throws
IllegalArgumentException
```

Sets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

**Specified by:** setGranularityPeriod

in interface

MonitorMBean
**Parameters:** period

- The granularity period value.
**Throws:** IllegalArgumentException

- The granularity
period is less than or equal to zero.
**See Also:** getGranularityPeriod()

---

#### setGranularityPeriod

public void setGranularityPeriod​(long period)
throws

IllegalArgumentException

Sets the granularity period (in milliseconds).

The default value of the granularity period is 10 seconds.

isActive

```java
public boolean isActive()
```

Tests whether the monitor MBean is active. A monitor MBean is
marked active when the

start

method is called.
It becomes inactive when the

stop

method is
called.

**Specified by:** isActive

in interface

MonitorMBean
**Returns:** true

if the monitor MBean is active,

false

otherwise.

---

#### isActive

public boolean isActive()

Tests whether the monitor MBean is active. A monitor MBean is
marked active when the

start

method is called.
It becomes inactive when the

stop

method is
called.

---

