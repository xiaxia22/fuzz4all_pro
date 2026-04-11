# Class StandardEmitterMBean

**Source:** `java.management\javax\management\StandardEmitterMBean.html`

### Class Description

```java
public class
StandardEmitterMBean

extends
StandardMBean

implements
NotificationEmitter
```

An MBean whose management interface is determined by reflection
on a Java interface, and that emits notifications.

The following example shows how to use the public constructor

StandardEmitterMBean(implementation, mbeanInterface, emitter)

to
create an MBean emitting notifications with any
implementation class name

Impl

, with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, and with any implementation of the interface

NotificationEmitter

. The example uses the class

NotificationBroadcasterSupport

as an implementation
of the interface

NotificationEmitter

.

```java
MBeanServer mbs;
...
final String[] types = new String[] {"sun.disc.space","sun.disc.alarm"};
final MBeanNotificationInfo info = new MBeanNotificationInfo(
types,
Notification.class.getName(),
"Notification about disc info.");
final NotificationEmitter emitter =
new NotificationBroadcasterSupport(info);

final Intf impl = new Impl(...);
final Object mbean = new StandardEmitterMBean(
impl, Intf.class, emitter);
mbs.registerMBean(mbean, objectName);
```

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

*No entries found.*

### Constructor Details

#### public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,

NotificationEmitter
emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Parameters:**
- implementation

- the implementation of the MBean interface.
- mbeanInterface

- a Standard MBean interface.
- emitter

- the object that will handle notifications.

**Throws:**
- IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

**Type Parameters:**
- T

- the implementation type of the MBean

---

#### public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Parameters:**
- implementation

- the implementation of the MBean interface.
- mbeanInterface

- a Standard MBean interface.
- isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
- emitter

- the object that will handle notifications.

**Throws:**
- IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

**Type Parameters:**
- T

- the implementation type of the MBean

---

#### protected StandardEmitterMBean​(
Class
<?> mbeanInterface,

NotificationEmitter
emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:**
- mbeanInterface

- a StandardMBean interface.
- emitter

- the object that will handle notifications.

**Throws:**
- IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

---

#### protected StandardEmitterMBean​(
Class
<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:**
- mbeanInterface

- a StandardMBean interface.
- isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
- emitter

- the object that will handle notifications.

**Throws:**
- IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

---

### Method Details

#### public void sendNotification​(
Notification
n)

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

**Parameters:**
- n

- the notification to send.

**Throws:**
- ClassCastException

- if the

emitter

parameter to the
constructor was not a

NotificationBroadcasterSupport

.

---

### Additional Sections

#### Class StandardEmitterMBean

java.lang.Object

- javax.management.StandardMBean
- - javax.management.StandardEmitterMBean

javax.management.StandardMBean

- javax.management.StandardEmitterMBean

javax.management.StandardEmitterMBean

**All Implemented Interfaces:** DynamicMBean

,

MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

```java
public class
StandardEmitterMBean

extends
StandardMBean

implements
NotificationEmitter
```

An MBean whose management interface is determined by reflection
on a Java interface, and that emits notifications.

The following example shows how to use the public constructor

StandardEmitterMBean(implementation, mbeanInterface, emitter)

to
create an MBean emitting notifications with any
implementation class name

Impl

, with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, and with any implementation of the interface

NotificationEmitter

. The example uses the class

NotificationBroadcasterSupport

as an implementation
of the interface

NotificationEmitter

.

```java
MBeanServer mbs;
...
final String[] types = new String[] {"sun.disc.space","sun.disc.alarm"};
final MBeanNotificationInfo info = new MBeanNotificationInfo(
types,
Notification.class.getName(),
"Notification about disc info.");
final NotificationEmitter emitter =
new NotificationBroadcasterSupport(info);

final Intf impl = new Impl(...);
final Object mbean = new StandardEmitterMBean(
impl, Intf.class, emitter);
mbs.registerMBean(mbean, objectName);
```

**Since:** 1.6
**See Also:** StandardMBean

public class

StandardEmitterMBean

extends

StandardMBean

implements

NotificationEmitter

An MBean whose management interface is determined by reflection
on a Java interface, and that emits notifications.

The following example shows how to use the public constructor

StandardEmitterMBean(implementation, mbeanInterface, emitter)

to
create an MBean emitting notifications with any
implementation class name

Impl

, with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, and with any implementation of the interface

NotificationEmitter

. The example uses the class

NotificationBroadcasterSupport

as an implementation
of the interface

NotificationEmitter

.

```java
MBeanServer mbs;
...
final String[] types = new String[] {"sun.disc.space","sun.disc.alarm"};
final MBeanNotificationInfo info = new MBeanNotificationInfo(
types,
Notification.class.getName(),
"Notification about disc info.");
final NotificationEmitter emitter =
new NotificationBroadcasterSupport(info);

final Intf impl = new Impl(...);
final Object mbean = new StandardEmitterMBean(
impl, Intf.class, emitter);
mbs.registerMBean(mbean, objectName);
```

An MBean whose management interface is determined by reflection
on a Java interface, and that emits notifications.

The following example shows how to use the public constructor

StandardEmitterMBean(implementation, mbeanInterface, emitter)

to
create an MBean emitting notifications with any
implementation class name

Impl

, with a management
interface defined (as for current Standard MBeans) by any interface

Intf

, and with any implementation of the interface

NotificationEmitter

. The example uses the class

NotificationBroadcasterSupport

as an implementation
of the interface

NotificationEmitter

.

MBeanServer mbs;
...
final String[] types = new String[] {"sun.disc.space","sun.disc.alarm"};
final MBeanNotificationInfo info = new MBeanNotificationInfo(
types,
Notification.class.getName(),
"Notification about disc info.");
final NotificationEmitter emitter =
new NotificationBroadcasterSupport(info);

final Intf impl = new Impl(...);
final Object mbean = new StandardEmitterMBean(
impl, Intf.class, emitter);
mbs.registerMBean(mbean, objectName);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StandardEmitterMBean

​(

Class

<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

.

protected

StandardEmitterMBean

​(

Class

<?> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.

StandardEmitterMBean

​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

.

StandardEmitterMBean

​(T implementation,

Class

<T> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

sendNotification

​(

Notification

n)

Sends a notification.

- Methods declared in class javax.management.

StandardMBean

cacheMBeanInfo

,

getCachedMBeanInfo

,

getClassName

,

getConstructors

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getImpact

,

getImplementation

,

getImplementationClass

,

getMBeanInfo

,

getMBeanInterface

,

getParameterName

,

getParameterName

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

setImplementation

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

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StandardEmitterMBean

​(

Class

<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

.

protected

StandardEmitterMBean

​(

Class

<?> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.

StandardEmitterMBean

​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

.

StandardEmitterMBean

​(T implementation,

Class

<T> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.

---

#### Constructor Summary

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

.

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

.

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

sendNotification

​(

Notification

n)

Sends a notification.

- Methods declared in class javax.management.

StandardMBean

cacheMBeanInfo

,

getCachedMBeanInfo

,

getClassName

,

getConstructors

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getImpact

,

getImplementation

,

getImplementationClass

,

getMBeanInfo

,

getMBeanInterface

,

getParameterName

,

getParameterName

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

setImplementation

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

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

- Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

getNotificationInfo

,

removeNotificationListener

- Methods declared in interface javax.management.

NotificationEmitter

removeNotificationListener

---

#### Method Summary

Sends a notification.

Methods declared in class javax.management.

StandardMBean

cacheMBeanInfo

,

getCachedMBeanInfo

,

getClassName

,

getConstructors

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getDescription

,

getImpact

,

getImplementation

,

getImplementationClass

,

getMBeanInfo

,

getMBeanInterface

,

getParameterName

,

getParameterName

,

postDeregister

,

postRegister

,

preDeregister

,

preRegister

,

setImplementation

---

#### Methods declared in class javax.management. StandardMBean

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

DynamicMBean

getAttribute

,

getAttributes

,

invoke

,

setAttribute

,

setAttributes

---

#### Methods declared in interface javax.management. DynamicMBean

Methods declared in interface javax.management.

NotificationBroadcaster

addNotificationListener

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

- StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

- StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

- StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

============ METHOD DETAIL ==========

- Method Detail

- sendNotification

```java
public void sendNotification​(
Notification
n)
```

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

**Parameters:** n

- the notification to send.
**Throws:** ClassCastException

- if the

emitter

parameter to the
constructor was not a

NotificationBroadcasterSupport

.

Constructor Detail

- StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

- StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

- StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

- StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

---

#### Constructor Detail

StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

---

#### StandardEmitterMBean

public StandardEmitterMBean​(T implementation,

Class

<T> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

. It is legal and useful
for

implementation

and

emitter

to be the same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

StandardEmitterMBean

```java
public StandardEmitterMBean​(T implementation,

Class
<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

**Type Parameters:** T

- the implementation type of the MBean
**Parameters:** implementation

- the implementation of the MBean interface.
**Parameters:** mbeanInterface

- a Standard MBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if the given

implementation

does not implement the
specified interface, or if

emitter

is null.

---

#### StandardEmitterMBean

public StandardEmitterMBean​(T implementation,

Class

<T> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

Make an MBean whose management interface is specified by

mbeanInterface

, with the given implementation and where
notifications are handled by the given

NotificationEmitter

. This constructor can be used to make
either Standard MBeans or MXBeans. The resultant MBean
implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

. It is legal and
useful for

implementation

and

emitter

to be the
same object.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

---

#### StandardEmitterMBean

protected StandardEmitterMBean​(

Class

<?> mbeanInterface,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

Make an MBean whose management interface is specified by

mbeanInterface

, and
where notifications are handled by the given

NotificationEmitter

.
The resultant MBean implements the

NotificationEmitter

interface
by forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

StandardEmitterMBean

```java
protected StandardEmitterMBean​(
Class
<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter
emitter)
```

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

**Parameters:** mbeanInterface

- a StandardMBean interface.
**Parameters:** isMXBean

- If true, the

mbeanInterface

parameter
names an MXBean interface and the resultant MBean is an MXBean.
**Parameters:** emitter

- the object that will handle notifications.
**Throws:** IllegalArgumentException

- if the

mbeanInterface

does not follow JMX design patterns for Management Interfaces, or
if

this

does not implement the specified interface, or
if

emitter

is null.

---

#### StandardEmitterMBean

protected StandardEmitterMBean​(

Class

<?> mbeanInterface,
boolean isMXBean,

NotificationEmitter

emitter)

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

Make an MBean whose management interface is specified by

mbeanInterface

, and where notifications are handled by
the given

NotificationEmitter

. This constructor can be
used to make either Standard MBeans or MXBeans. The resultant
MBean implements the

NotificationEmitter

interface by
forwarding its methods to

emitter

.

If

emitter

is an instance of

NotificationBroadcasterSupport

then the MBean's

sendNotification

method will call

emitter.

sendNotification

.

The array returned by

NotificationBroadcaster.getNotificationInfo()

on the
new MBean is a copy of the array returned by

emitter.

getNotificationInfo()

at the time of construction. If the array
returned by

emitter.getNotificationInfo()

later changes,
that will have no effect on this object's

getNotificationInfo()

.

This constructor must be called from a subclass that implements
the given

mbeanInterface

.

Method Detail

- sendNotification

```java
public void sendNotification​(
Notification
n)
```

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

**Parameters:** n

- the notification to send.
**Throws:** ClassCastException

- if the

emitter

parameter to the
constructor was not a

NotificationBroadcasterSupport

.

---

#### Method Detail

sendNotification

```java
public void sendNotification​(
Notification
n)
```

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

**Parameters:** n

- the notification to send.
**Throws:** ClassCastException

- if the

emitter

parameter to the
constructor was not a

NotificationBroadcasterSupport

.

---

#### sendNotification

public void sendNotification​(

Notification

n)

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

Sends a notification.

If the

emitter

parameter to the constructor was an
instance of

NotificationBroadcasterSupport

then this
method will call

emitter.

sendNotification

.

---

