# Interface NotificationBroadcaster

**Source:** `java.management\javax\management\NotificationBroadcaster.html`

### Class Description

```java
public interface
NotificationBroadcaster
```

Interface implemented by an MBean that emits Notifications. It
allows a listener to be registered with the MBean as a notification
listener.

Notification dispatch

When an MBean emits a notification, it considers each listener that has been
added with

addNotificationListener

and not
subsequently removed with

removeNotificationListener

.
If a filter was provided with that listener, and if the filter's

isNotificationEnabled

method returns
false, the listener is ignored. Otherwise, the listener's

handleNotification

method is called with
the notification, as well as the handback object that was provided to

addNotificationListener

.

If the same listener is added more than once, it is considered as many times as it was
added. It is often useful to add the same listener with different filters or handback
objects.

Implementations of this interface can differ regarding the thread in which the methods
of filters and listeners are called.

If the method call of a filter or listener throws an

Exception

, then that
exception should not prevent other listeners from being invoked. However, if the method
call throws an

Error

, then it is recommended that processing of the notification
stop at that point, and if it is possible to propagate the

Error

to the sender of
the notification, this should be done.

New code should use the

NotificationEmitter

interface
instead.

Implementations of this interface and of

NotificationEmitter

should be careful about synchronization. In particular, it is not a good
idea for an implementation to hold any locks while it is calling a
listener. To deal with the possibility that the list of listeners might
change while a notification is being dispatched, a good strategy is to
use a

CopyOnWriteArrayList

for this list.

**All Known Subinterfaces:** ModelMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationEmitter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException

Adds a listener to this MBean.

**Parameters:**
- listener

- The listener object which will handle the
notifications emitted by the broadcaster.
- filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
- handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.

**Throws:**
- IllegalArgumentException

- Listener parameter is null.

**See Also:**
- removeNotificationListener(javax.management.NotificationListener)

---

#### void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException

Removes a listener from this MBean. If the listener
has been registered with different handback objects or
notification filters, all entries corresponding to the listener
will be removed.

**Parameters:**
- listener

- A listener that was previously added to this
MBean.

**Throws:**
- ListenerNotFoundException

- The listener is not
registered with the MBean.

**See Also:**
- addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### MBeanNotificationInfo
[] getNotificationInfo()

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

**Returns:**
- the array of possible notifications.

---

### Additional Sections

#### Interface NotificationBroadcaster

**All Known Subinterfaces:** ModelMBean

,

ModelMBeanNotificationBroadcaster

,

NotificationEmitter

**All Known Implementing Classes:** CounterMonitor

,

GaugeMonitor

,

JMXConnectorServer

,

MBeanServerDelegate

,

Monitor

,

NotificationBroadcasterSupport

,

RelationService

,

RequiredModelMBean

,

RMIConnectorServer

,

StandardEmitterMBean

,

StringMonitor

,

Timer

```java
public interface
NotificationBroadcaster
```

Interface implemented by an MBean that emits Notifications. It
allows a listener to be registered with the MBean as a notification
listener.

Notification dispatch

When an MBean emits a notification, it considers each listener that has been
added with

addNotificationListener

and not
subsequently removed with

removeNotificationListener

.
If a filter was provided with that listener, and if the filter's

isNotificationEnabled

method returns
false, the listener is ignored. Otherwise, the listener's

handleNotification

method is called with
the notification, as well as the handback object that was provided to

addNotificationListener

.

If the same listener is added more than once, it is considered as many times as it was
added. It is often useful to add the same listener with different filters or handback
objects.

Implementations of this interface can differ regarding the thread in which the methods
of filters and listeners are called.

If the method call of a filter or listener throws an

Exception

, then that
exception should not prevent other listeners from being invoked. However, if the method
call throws an

Error

, then it is recommended that processing of the notification
stop at that point, and if it is possible to propagate the

Error

to the sender of
the notification, this should be done.

New code should use the

NotificationEmitter

interface
instead.

Implementations of this interface and of

NotificationEmitter

should be careful about synchronization. In particular, it is not a good
idea for an implementation to hold any locks while it is calling a
listener. To deal with the possibility that the list of listeners might
change while a notification is being dispatched, a good strategy is to
use a

CopyOnWriteArrayList

for this list.

**Since:** 1.5

public interface

NotificationBroadcaster

Interface implemented by an MBean that emits Notifications. It
allows a listener to be registered with the MBean as a notification
listener.

Notification dispatch

When an MBean emits a notification, it considers each listener that has been
added with

addNotificationListener

and not
subsequently removed with

removeNotificationListener

.
If a filter was provided with that listener, and if the filter's

isNotificationEnabled

method returns
false, the listener is ignored. Otherwise, the listener's

handleNotification

method is called with
the notification, as well as the handback object that was provided to

addNotificationListener

.

If the same listener is added more than once, it is considered as many times as it was
added. It is often useful to add the same listener with different filters or handback
objects.

Implementations of this interface can differ regarding the thread in which the methods
of filters and listeners are called.

If the method call of a filter or listener throws an

Exception

, then that
exception should not prevent other listeners from being invoked. However, if the method
call throws an

Error

, then it is recommended that processing of the notification
stop at that point, and if it is possible to propagate the

Error

to the sender of
the notification, this should be done.

New code should use the

NotificationEmitter

interface
instead.

Implementations of this interface and of

NotificationEmitter

should be careful about synchronization. In particular, it is not a good
idea for an implementation to hold any locks while it is calling a
listener. To deal with the possibility that the list of listeners might
change while a notification is being dispatched, a good strategy is to
use a

CopyOnWriteArrayList

for this list.

Interface implemented by an MBean that emits Notifications. It
allows a listener to be registered with the MBean as a notification
listener.

---

#### Notification dispatch

When an MBean emits a notification, it considers each listener that has been
added with

addNotificationListener

and not
subsequently removed with

removeNotificationListener

.
If a filter was provided with that listener, and if the filter's

isNotificationEnabled

method returns
false, the listener is ignored. Otherwise, the listener's

handleNotification

method is called with
the notification, as well as the handback object that was provided to

addNotificationListener

.

If the same listener is added more than once, it is considered as many times as it was
added. It is often useful to add the same listener with different filters or handback
objects.

Implementations of this interface can differ regarding the thread in which the methods
of filters and listeners are called.

If the method call of a filter or listener throws an

Exception

, then that
exception should not prevent other listeners from being invoked. However, if the method
call throws an

Error

, then it is recommended that processing of the notification
stop at that point, and if it is possible to propagate the

Error

to the sender of
the notification, this should be done.

New code should use the

NotificationEmitter

interface
instead.

Implementations of this interface and of

NotificationEmitter

should be careful about synchronization. In particular, it is not a good
idea for an implementation to hold any locks while it is calling a
listener. To deal with the possibility that the list of listeners might
change while a notification is being dispatched, a good strategy is to
use a

CopyOnWriteArrayList

for this list.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to this MBean.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

void

removeNotificationListener

​(

NotificationListener

listener)

Removes a listener from this MBean.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addNotificationListener

​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener to this MBean.

MBeanNotificationInfo

[]

getNotificationInfo

()

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

void

removeNotificationListener

​(

NotificationListener

listener)

Removes a listener from this MBean.

---

#### Method Summary

Adds a listener to this MBean.

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

Removes a listener from this MBean.

============ METHOD DETAIL ==========

- Method Detail

- addNotificationListener

```java
void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Adds a listener to this MBean.

**Parameters:** listener

- The listener object which will handle the
notifications emitted by the broadcaster.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- Listener parameter is null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

- removeNotificationListener

```java
void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from this MBean. If the listener
has been registered with different handback objects or
notification filters, all entries corresponding to the listener
will be removed.

**Parameters:** listener

- A listener that was previously added to this
MBean.
**Throws:** ListenerNotFoundException

- The listener is not
registered with the MBean.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getNotificationInfo

```java
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

**Returns:** the array of possible notifications.

Method Detail

- addNotificationListener

```java
void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Adds a listener to this MBean.

**Parameters:** listener

- The listener object which will handle the
notifications emitted by the broadcaster.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- Listener parameter is null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

- removeNotificationListener

```java
void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from this MBean. If the listener
has been registered with different handback objects or
notification filters, all entries corresponding to the listener
will be removed.

**Parameters:** listener

- A listener that was previously added to this
MBean.
**Throws:** ListenerNotFoundException

- The listener is not
registered with the MBean.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

- getNotificationInfo

```java
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

**Returns:** the array of possible notifications.

---

#### Method Detail

addNotificationListener

```java
void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
throws
IllegalArgumentException
```

Adds a listener to this MBean.

**Parameters:** listener

- The listener object which will handle the
notifications emitted by the broadcaster.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- Listener parameter is null.
**See Also:** removeNotificationListener(javax.management.NotificationListener)

---

#### addNotificationListener

void addNotificationListener​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)
throws

IllegalArgumentException

Adds a listener to this MBean.

removeNotificationListener

```java
void removeNotificationListener​(
NotificationListener
listener)
throws
ListenerNotFoundException
```

Removes a listener from this MBean. If the listener
has been registered with different handback objects or
notification filters, all entries corresponding to the listener
will be removed.

**Parameters:** listener

- A listener that was previously added to this
MBean.
**Throws:** ListenerNotFoundException

- The listener is not
registered with the MBean.
**See Also:** addNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

,

NotificationEmitter.removeNotificationListener(javax.management.NotificationListener, javax.management.NotificationFilter, java.lang.Object)

---

#### removeNotificationListener

void removeNotificationListener​(

NotificationListener

listener)
throws

ListenerNotFoundException

Removes a listener from this MBean. If the listener
has been registered with different handback objects or
notification filters, all entries corresponding to the listener
will be removed.

getNotificationInfo

```java
MBeanNotificationInfo
[] getNotificationInfo()
```

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

**Returns:** the array of possible notifications.

---

#### getNotificationInfo

MBeanNotificationInfo

[] getNotificationInfo()

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

Returns an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type.

It is not illegal for the MBean to send notifications not
described in this array. However, some clients of the MBean
server may depend on the array being complete for their correct
functioning.

---

