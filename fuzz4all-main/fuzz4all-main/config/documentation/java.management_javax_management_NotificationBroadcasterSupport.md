# Class NotificationBroadcasterSupport

**Source:** `java.management\javax\management\NotificationBroadcasterSupport.html`

### Class Description

```java
public class
NotificationBroadcasterSupport

extends
Object

implements
NotificationEmitter
```

Provides an implementation of

NotificationEmitter

interface. This can be used as the super class of an MBean that
sends notifications.

By default, the notification dispatch model is synchronous.
That is, when a thread calls sendNotification, the

NotificationListener.handleNotification

method of each listener
is called within that thread. You can override this default
by overriding

handleNotification

in a subclass, or by passing an
Executor to the constructor.

If the method call of a filter or listener throws an

Exception

,
then that exception does not prevent other listeners from being invoked. However,
if the method call of a filter or of

Executor.execute

or of

handleNotification

(when no

Excecutor

is specified) throws an

Error

, then that

Error

is propagated to the caller of

sendNotification

.

Remote listeners added using the JMX Remote API (see JMXConnector) are not
usually called synchronously. That is, when sendNotification returns, it is
not guaranteed that any remote listeners have yet received the notification.

**All Implemented Interfaces:** NotificationBroadcaster

,

NotificationEmitter

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotificationBroadcasterSupport()

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification. This constructor is equivalent to

NotificationBroadcasterSupport(null, null)

.

---

#### public NotificationBroadcasterSupport​(
Executor
executor)

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

. When

sendNotification

is called, a listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes place in the thread
that called

sendNotification

. Then, for each selected listener,

executor.execute

is called with a command
that calls the

handleNotification

method.
This constructor is equivalent to

NotificationBroadcasterSupport(executor, null)

.

**Parameters:**
- executor

- an executor used by the method

sendNotification

to
send each notification. If it is null, the thread calling

sendNotification

will invoke the

handleNotification

method itself.

**Since:**
- 1.6

---

#### public NotificationBroadcasterSupport​(
MBeanNotificationInfo
... info)

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:**
- info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.

**Since:**
- 1.6

---

#### public NotificationBroadcasterSupport​(
Executor
executor,

MBeanNotificationInfo
... info)

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:**
- executor

- an executor used by the method

sendNotification

to send each notification. If it
is null, the thread calling

sendNotification

will
invoke the

handleNotification

method itself.
- info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.

**Since:**
- 1.6

---

### Method Details

#### public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)

Adds a listener.

**Specified by:**
- addNotificationListener

in interface

NotificationBroadcaster

**Parameters:**
- listener

- The listener to receive notifications.
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

- thrown if the listener is null.

**See Also:**
- NotificationBroadcaster.removeNotificationListener(javax.management.NotificationListener)

---

#### public void sendNotification​(
Notification
notification)

Sends a notification.

If an

Executor

was specified in the constructor, it will be given one
task per selected listener to deliver the notification to that listener.

**Parameters:**
- notification

- The notification to send.

---

#### protected void handleNotification​(
NotificationListener
listener,

Notification
notif,

Object
handback)

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

**Parameters:**
- listener

- the listener to which the notification is being
delivered.
- notif

- the notification being delivered to the listener.
- handback

- the handback object that was supplied when the
listener was added.

---

### Additional Sections

#### Class NotificationBroadcasterSupport

java.lang.Object

- javax.management.NotificationBroadcasterSupport

javax.management.NotificationBroadcasterSupport

**All Implemented Interfaces:** NotificationBroadcaster

,

NotificationEmitter

**Direct Known Subclasses:** JMXConnectorServer

,

Monitor

,

RelationService

,

Timer

```java
public class
NotificationBroadcasterSupport

extends
Object

implements
NotificationEmitter
```

Provides an implementation of

NotificationEmitter

interface. This can be used as the super class of an MBean that
sends notifications.

By default, the notification dispatch model is synchronous.
That is, when a thread calls sendNotification, the

NotificationListener.handleNotification

method of each listener
is called within that thread. You can override this default
by overriding

handleNotification

in a subclass, or by passing an
Executor to the constructor.

If the method call of a filter or listener throws an

Exception

,
then that exception does not prevent other listeners from being invoked. However,
if the method call of a filter or of

Executor.execute

or of

handleNotification

(when no

Excecutor

is specified) throws an

Error

, then that

Error

is propagated to the caller of

sendNotification

.

Remote listeners added using the JMX Remote API (see JMXConnector) are not
usually called synchronously. That is, when sendNotification returns, it is
not guaranteed that any remote listeners have yet received the notification.

**Since:** 1.5

public class

NotificationBroadcasterSupport

extends

Object

implements

NotificationEmitter

Provides an implementation of

NotificationEmitter

interface. This can be used as the super class of an MBean that
sends notifications.

By default, the notification dispatch model is synchronous.
That is, when a thread calls sendNotification, the

NotificationListener.handleNotification

method of each listener
is called within that thread. You can override this default
by overriding

handleNotification

in a subclass, or by passing an
Executor to the constructor.

If the method call of a filter or listener throws an

Exception

,
then that exception does not prevent other listeners from being invoked. However,
if the method call of a filter or of

Executor.execute

or of

handleNotification

(when no

Excecutor

is specified) throws an

Error

, then that

Error

is propagated to the caller of

sendNotification

.

Remote listeners added using the JMX Remote API (see JMXConnector) are not
usually called synchronously. That is, when sendNotification returns, it is
not guaranteed that any remote listeners have yet received the notification.

Provides an implementation of

NotificationEmitter

interface. This can be used as the super class of an MBean that
sends notifications.

By default, the notification dispatch model is synchronous.
That is, when a thread calls sendNotification, the

NotificationListener.handleNotification

method of each listener
is called within that thread. You can override this default
by overriding

handleNotification

in a subclass, or by passing an
Executor to the constructor.

If the method call of a filter or listener throws an

Exception

,
then that exception does not prevent other listeners from being invoked. However,
if the method call of a filter or of

Executor.execute

or of

handleNotification

(when no

Excecutor

is specified) throws an

Error

, then that

Error

is propagated to the caller of

sendNotification

.

Remote listeners added using the JMX Remote API (see JMXConnector) are not
usually called synchronously. That is, when sendNotification returns, it is
not guaranteed that any remote listeners have yet received the notification.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NotificationBroadcasterSupport

()

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification.

NotificationBroadcasterSupport

​(

Executor

executor)

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

.

NotificationBroadcasterSupport

​(

Executor

executor,

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

NotificationBroadcasterSupport

​(

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

Adds a listener.

protected void

handleNotification

​(

NotificationListener

listener,

Notification

notif,

Object

handback)

This method is called by

sendNotification

for each listener in order to send the
notification to that listener.

void

sendNotification

​(

Notification

notification)

Sends a notification.

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

Constructor Summary

Constructors

Constructor

Description

NotificationBroadcasterSupport

()

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification.

NotificationBroadcasterSupport

​(

Executor

executor)

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

.

NotificationBroadcasterSupport

​(

Executor

executor,

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

NotificationBroadcasterSupport

​(

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent.

---

#### Constructor Summary

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification.

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

.

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent.

Method Summary

All Methods

Instance Methods

Concrete Methods

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

Adds a listener.

protected void

handleNotification

​(

NotificationListener

listener,

Notification

notif,

Object

handback)

This method is called by

sendNotification

for each listener in order to send the
notification to that listener.

void

sendNotification

​(

Notification

notification)

Sends a notification.

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

Adds a listener.

This method is called by

sendNotification

for each listener in order to send the
notification to that listener.

Sends a notification.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport()
```

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification. This constructor is equivalent to

NotificationBroadcasterSupport(null, null)

.

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor)
```

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

. When

sendNotification

is called, a listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes place in the thread
that called

sendNotification

. Then, for each selected listener,

executor.execute

is called with a command
that calls the

handleNotification

method.
This constructor is equivalent to

NotificationBroadcasterSupport(executor, null)

.

**Parameters:** executor

- an executor used by the method

sendNotification

to
send each notification. If it is null, the thread calling

sendNotification

will invoke the

handleNotification

method itself.
**Since:** 1.6

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor,

MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** executor

- an executor used by the method

sendNotification

to send each notification. If it
is null, the thread calling

sendNotification

will
invoke the

handleNotification

method itself.
**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener to receive notifications.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- thrown if the listener is null.
**See Also:** NotificationBroadcaster.removeNotificationListener(javax.management.NotificationListener)

- sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Sends a notification.

If an

Executor

was specified in the constructor, it will be given one
task per selected listener to deliver the notification to that listener.

**Parameters:** notification

- The notification to send.

- handleNotification

```java
protected void handleNotification​(
NotificationListener
listener,

Notification
notif,

Object
handback)
```

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

**Parameters:** listener

- the listener to which the notification is being
delivered.
**Parameters:** notif

- the notification being delivered to the listener.
**Parameters:** handback

- the handback object that was supplied when the
listener was added.

Constructor Detail

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport()
```

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification. This constructor is equivalent to

NotificationBroadcasterSupport(null, null)

.

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor)
```

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

. When

sendNotification

is called, a listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes place in the thread
that called

sendNotification

. Then, for each selected listener,

executor.execute

is called with a command
that calls the

handleNotification

method.
This constructor is equivalent to

NotificationBroadcasterSupport(executor, null)

.

**Parameters:** executor

- an executor used by the method

sendNotification

to
send each notification. If it is null, the thread calling

sendNotification

will invoke the

handleNotification

method itself.
**Since:** 1.6

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

- NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor,

MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** executor

- an executor used by the method

sendNotification

to send each notification. If it
is null, the thread calling

sendNotification

will
invoke the

handleNotification

method itself.
**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

---

#### Constructor Detail

NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport()
```

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification. This constructor is equivalent to

NotificationBroadcasterSupport(null, null)

.

---

#### NotificationBroadcasterSupport

public NotificationBroadcasterSupport()

Constructs a NotificationBroadcasterSupport where each listener is invoked by the
thread sending the notification. This constructor is equivalent to

NotificationBroadcasterSupport(null, null)

.

NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor)
```

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

. When

sendNotification

is called, a listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes place in the thread
that called

sendNotification

. Then, for each selected listener,

executor.execute

is called with a command
that calls the

handleNotification

method.
This constructor is equivalent to

NotificationBroadcasterSupport(executor, null)

.

**Parameters:** executor

- an executor used by the method

sendNotification

to
send each notification. If it is null, the thread calling

sendNotification

will invoke the

handleNotification

method itself.
**Since:** 1.6

---

#### NotificationBroadcasterSupport

public NotificationBroadcasterSupport​(

Executor

executor)

Constructs a NotificationBroadcasterSupport where each listener is invoked using
the given

Executor

. When

sendNotification

is called, a listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes place in the thread
that called

sendNotification

. Then, for each selected listener,

executor.execute

is called with a command
that calls the

handleNotification

method.
This constructor is equivalent to

NotificationBroadcasterSupport(executor, null)

.

NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

---

#### NotificationBroadcasterSupport

public NotificationBroadcasterSupport​(

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

Constructs a NotificationBroadcasterSupport with information
about the notifications that may be sent. Each listener is
invoked by the thread sending the notification. This
constructor is equivalent to

NotificationBroadcasterSupport(null, info)

.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

NotificationBroadcasterSupport

```java
public NotificationBroadcasterSupport​(
Executor
executor,

MBeanNotificationInfo
... info)
```

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

**Parameters:** executor

- an executor used by the method

sendNotification

to send each notification. If it
is null, the thread calling

sendNotification

will
invoke the

handleNotification

method itself.
**Parameters:** info

- an array indicating, for each notification this
MBean may send, the name of the Java class of the notification
and the notification type. Can be null, which is equivalent to
an empty array.
**Since:** 1.6

---

#### NotificationBroadcasterSupport

public NotificationBroadcasterSupport​(

Executor

executor,

MBeanNotificationInfo

... info)

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

Constructs a NotificationBroadcasterSupport with information about the notifications that may be sent,
and where each listener is invoked using the given

Executor

.

When

sendNotification

is called, a
listener is selected if it was added with a null

NotificationFilter

, or if

isNotificationEnabled

returns true for the notification being sent. The call to

NotificationFilter.isNotificationEnabled

takes
place in the thread that called

sendNotification

. Then, for each selected
listener,

executor.execute

is called
with a command that calls the

handleNotification

method.

If the

info

array is not empty, then it is
cloned by the constructor as if by

info.clone()

, and
each call to

NotificationBroadcaster.getNotificationInfo()

returns a new
clone.

Method Detail

- addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener to receive notifications.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- thrown if the listener is null.
**See Also:** NotificationBroadcaster.removeNotificationListener(javax.management.NotificationListener)

- sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Sends a notification.

If an

Executor

was specified in the constructor, it will be given one
task per selected listener to deliver the notification to that listener.

**Parameters:** notification

- The notification to send.

- handleNotification

```java
protected void handleNotification​(
NotificationListener
listener,

Notification
notif,

Object
handback)
```

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

**Parameters:** listener

- the listener to which the notification is being
delivered.
**Parameters:** notif

- the notification being delivered to the listener.
**Parameters:** handback

- the handback object that was supplied when the
listener was added.

---

#### Method Detail

addNotificationListener

```java
public void addNotificationListener​(
NotificationListener
listener,

NotificationFilter
filter,

Object
handback)
```

Adds a listener.

**Specified by:** addNotificationListener

in interface

NotificationBroadcaster
**Parameters:** listener

- The listener to receive notifications.
**Parameters:** filter

- The filter object. If filter is null, no
filtering will be performed before handling notifications.
**Parameters:** handback

- An opaque object to be sent back to the
listener when a notification is emitted. This object cannot be
used by the Notification broadcaster object. It should be
resent unchanged with the notification to the listener.
**Throws:** IllegalArgumentException

- thrown if the listener is null.
**See Also:** NotificationBroadcaster.removeNotificationListener(javax.management.NotificationListener)

---

#### addNotificationListener

public void addNotificationListener​(

NotificationListener

listener,

NotificationFilter

filter,

Object

handback)

Adds a listener.

sendNotification

```java
public void sendNotification​(
Notification
notification)
```

Sends a notification.

If an

Executor

was specified in the constructor, it will be given one
task per selected listener to deliver the notification to that listener.

**Parameters:** notification

- The notification to send.

---

#### sendNotification

public void sendNotification​(

Notification

notification)

Sends a notification.

If an

Executor

was specified in the constructor, it will be given one
task per selected listener to deliver the notification to that listener.

handleNotification

```java
protected void handleNotification​(
NotificationListener
listener,

Notification
notif,

Object
handback)
```

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

**Parameters:** listener

- the listener to which the notification is being
delivered.
**Parameters:** notif

- the notification being delivered to the listener.
**Parameters:** handback

- the handback object that was supplied when the
listener was added.

---

#### handleNotification

protected void handleNotification​(

NotificationListener

listener,

Notification

notif,

Object

handback)

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

This method is called by

sendNotification

for each listener in order to send the
notification to that listener. It can be overridden in
subclasses to change the behavior of notification delivery,
for instance to deliver the notification in a separate
thread.

The default implementation of this method is equivalent to

```java
listener.handleNotification(notif, handback);
```

listener.handleNotification(notif, handback);

---

