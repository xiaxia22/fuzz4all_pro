# Class Timer

**Source:** `java.management\javax\management\timer\Timer.html`

### Class Description

```java
public class
Timer

extends
NotificationBroadcasterSupport

implements
TimerMBean
,
MBeanRegistration
```

Provides the implementation of the timer MBean.
The timer MBean sends out an alarm at a specified time
that wakes up all the listeners registered to receive timer notifications.

This class manages a list of dated timer notifications.
A method allows users to add/remove as many notifications as required.
When a timer notification is emitted by the timer and becomes obsolete,
it is automatically removed from the list of timer notifications.

Additional timer notifications can be added into regularly repeating notifications.

Note:

- When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

**All Implemented Interfaces:** MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

TimerMBean

---

### Field Details

#### public static final long ONE_SECOND

Number of milliseconds in one second.
Useful constant for the

addNotification

method.

**See Also:**
- Constant Field Values

---

#### public static final long ONE_MINUTE

Number of milliseconds in one minute.
Useful constant for the

addNotification

method.

**See Also:**
- Constant Field Values

---

#### public static final long ONE_HOUR

Number of milliseconds in one hour.
Useful constant for the

addNotification

method.

**See Also:**
- Constant Field Values

---

#### public static final long ONE_DAY

Number of milliseconds in one day.
Useful constant for the

addNotification

method.

**See Also:**
- Constant Field Values

---

#### public static final long ONE_WEEK

Number of milliseconds in one week.
Useful constant for the

addNotification

method.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public Timer()

Default constructor.

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

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Not used in this context.

**Specified by:**
- preRegister

in interface

MBeanRegistration

**Parameters:**
- server

- The MBean server in which the timer MBean will be registered.
- name

- The object name of the timer MBean.

**Returns:**
- The name of the timer MBean registered.

**Throws:**
- Exception

- if something goes wrong

---

#### public void postRegister​(
Boolean
registrationDone)

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

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

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Stops the timer.

**Specified by:**
- preDeregister

in interface

MBeanRegistration

**Throws:**
- Exception

- if something goes wrong

---

#### public void postDeregister()

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Not used in this context.

**Specified by:**
- postDeregister

in interface

MBeanRegistration

---

#### public void start()

Starts the timer.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

**Specified by:**
- start

in interface

TimerMBean

---

#### public void stop()

Stops the timer.

**Specified by:**
- stop

in interface

TimerMBean

---

#### public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences,
boolean fixedRate)
throws
IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

**Specified by:**
- addNotification

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.
- message

- The timer notification detailed message.
- userData

- The timer notification user data object.
- date

- The date when the notification occurs.
- period

- The period of the timer notification (in milliseconds).
- nbOccurences

- The total number the timer notification will be emitted.
- fixedRate

- If

true

and if the notification is periodic, the notification
is scheduled with a

fixed-rate

execution scheme. If

false

and if the notification is periodic, the notification
is scheduled with a

fixed-delay

execution scheme. Ignored if the
notification is not periodic.

**Returns:**
- The identifier of the new created timer notification.

**Throws:**
- IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.

**See Also:**
- addNotification(String, String, Object, Date, long, long)

---

#### public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences)
throws
IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

**Specified by:**
- addNotification

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.
- message

- The timer notification detailed message.
- userData

- The timer notification user data object.
- date

- The date when the notification occurs.
- period

- The period of the timer notification (in milliseconds).
- nbOccurences

- The total number the timer notification will be emitted.

**Returns:**
- The identifier of the new created timer notification.

**Throws:**
- IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.

**See Also:**
- addNotification(String, String, Object, Date, long, long, boolean)

---

#### public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period)
throws
IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

**Specified by:**
- addNotification

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.
- message

- The timer notification detailed message.
- userData

- The timer notification user data object.
- date

- The date when the notification occurs.
- period

- The period of the timer notification (in milliseconds).

**Returns:**
- The identifier of the new created timer notification.

**Throws:**
- IllegalArgumentException

- The date is

null

or
the period is negative.

---

#### public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date)
throws
IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

**Specified by:**
- addNotification

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.
- message

- The timer notification detailed message.
- userData

- The timer notification user data object.
- date

- The date when the notification occurs.

**Returns:**
- The identifier of the new created timer notification.

**Throws:**
- IllegalArgumentException

- The date is

null

.

---

#### public void removeNotification​(
Integer
id)
throws
InstanceNotFoundException

Removes the timer notification corresponding to the specified identifier from the list of notifications.

**Specified by:**
- removeNotification

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Throws:**
- InstanceNotFoundException

- The specified identifier does not correspond to any timer notification
in the list of notifications of this timer MBean.

---

#### public void removeNotifications​(
String
type)
throws
InstanceNotFoundException

Removes all the timer notifications corresponding to the specified type from the list of notifications.

**Specified by:**
- removeNotifications

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.

**Throws:**
- InstanceNotFoundException

- The specified type does not correspond to any timer notification
in the list of notifications of this timer MBean.

---

#### public void removeAllNotifications()

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

**Specified by:**
- removeAllNotifications

in interface

TimerMBean

---

#### public int getNbNotifications()

Gets the number of timer notifications registered into the list of notifications.

**Specified by:**
- getNbNotifications

in interface

TimerMBean

**Returns:**
- The number of timer notifications.

---

#### public
Vector
<
Integer
> getAllNotificationIDs()

Gets all timer notification identifiers registered into the list of notifications.

**Specified by:**
- getAllNotificationIDs

in interface

TimerMBean

**Returns:**
- A vector of

Integer

objects containing all the timer notification identifiers.

The vector is empty if there is no timer notification registered for this timer MBean.

---

#### public
Vector
<
Integer
> getNotificationIDs​(
String
type)

Gets all the identifiers of timer notifications corresponding to the specified type.

**Specified by:**
- getNotificationIDs

in interface

TimerMBean

**Parameters:**
- type

- The timer notification type.

**Returns:**
- A vector of

Integer

objects containing all the identifiers of
timer notifications with the specified

type

.

The vector is empty if there is no timer notifications registered for this timer MBean
with the specified

type

.

---

#### public
String
getNotificationType​(
Integer
id)

Gets the timer notification type corresponding to the specified identifier.

**Specified by:**
- getNotificationType

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- The timer notification type or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
String
getNotificationMessage​(
Integer
id)

Gets the timer notification detailed message corresponding to the specified identifier.

**Specified by:**
- getNotificationMessage

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- The timer notification detailed message or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
Object
getNotificationUserData​(
Integer
id)

Gets the timer notification user data object corresponding to the specified identifier.

**Specified by:**
- getNotificationUserData

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- The timer notification user data object or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
Date
getDate​(
Integer
id)

Gets a copy of the date associated to a timer notification.

**Specified by:**
- getDate

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- A copy of the date or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
Long
getPeriod​(
Integer
id)

Gets a copy of the period (in milliseconds) associated to a timer notification.

**Specified by:**
- getPeriod

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- A copy of the period or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
Long
getNbOccurences​(
Integer
id)

Gets a copy of the remaining number of occurrences associated to a timer notification.

**Specified by:**
- getNbOccurences

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- A copy of the remaining number of occurrences or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### public
Boolean
getFixedRate​(
Integer
id)

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

**Specified by:**
- getFixedRate

in interface

TimerMBean

**Parameters:**
- id

- The timer notification identifier.

**Returns:**
- A copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

---

#### public boolean getSendPastNotifications()

Gets the flag indicating whether or not the timer sends past notifications.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:**
- getSendPastNotifications

in interface

TimerMBean

**Returns:**
- The past notifications sending on/off flag value.

**See Also:**
- setSendPastNotifications(boolean)

---

#### public void setSendPastNotifications​(boolean value)

Sets the flag indicating whether the timer sends past notifications or not.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:**
- setSendPastNotifications

in interface

TimerMBean

**Parameters:**
- value

- The past notifications sending on/off flag value.

**See Also:**
- getSendPastNotifications()

---

#### public boolean isActive()

Tests whether the timer MBean is active.
A timer MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

The default value of the active on/off flag is

false

.

**Specified by:**
- isActive

in interface

TimerMBean

**Returns:**
- true

if the timer MBean is active,

false

otherwise.

---

#### public boolean isEmpty()

Tests whether the list of timer notifications is empty.

**Specified by:**
- isEmpty

in interface

TimerMBean

**Returns:**
- true

if the list of timer notifications is empty,

false

otherwise.

---

### Additional Sections

#### Class Timer

java.lang.Object

- javax.management.NotificationBroadcasterSupport
- - javax.management.timer.Timer

javax.management.NotificationBroadcasterSupport

- javax.management.timer.Timer

javax.management.timer.Timer

**All Implemented Interfaces:** MBeanRegistration

,

NotificationBroadcaster

,

NotificationEmitter

,

TimerMBean

```java
public class
Timer

extends
NotificationBroadcasterSupport

implements
TimerMBean
,
MBeanRegistration
```

Provides the implementation of the timer MBean.
The timer MBean sends out an alarm at a specified time
that wakes up all the listeners registered to receive timer notifications.

This class manages a list of dated timer notifications.
A method allows users to add/remove as many notifications as required.
When a timer notification is emitted by the timer and becomes obsolete,
it is automatically removed from the list of timer notifications.

Additional timer notifications can be added into regularly repeating notifications.

Note:

- When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

**Since:** 1.5

public class

Timer

extends

NotificationBroadcasterSupport

implements

TimerMBean

,

MBeanRegistration

Provides the implementation of the timer MBean.
The timer MBean sends out an alarm at a specified time
that wakes up all the listeners registered to receive timer notifications.

This class manages a list of dated timer notifications.
A method allows users to add/remove as many notifications as required.
When a timer notification is emitted by the timer and becomes obsolete,
it is automatically removed from the list of timer notifications.

Additional timer notifications can be added into regularly repeating notifications.

Note:

- When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

This class manages a list of dated timer notifications.
A method allows users to add/remove as many notifications as required.
When a timer notification is emitted by the timer and becomes obsolete,
it is automatically removed from the list of timer notifications.

Additional timer notifications can be added into regularly repeating notifications.

Note:

- When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

Note:

- When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

When sending timer notifications, the timer updates the notification sequence number
irrespective of the notification type.

The timer service relies on the system date of the host where the

Timer

class is loaded.
Listeners may receive untimely notifications
if their host has a different system date.
To avoid such problems, synchronize the system date of all host machines where timing is needed.

The default behavior for periodic notifications is

fixed-delay execution

, as
specified in

Timer

. In order to use

fixed-rate execution

, use the
overloaded

addNotification(String, String, Object, Date, long, long, boolean)

method.

Notification listeners are potentially all executed in the same
thread. Therefore, they should execute rapidly to avoid holding up
other listeners or perturbing the regularity of fixed-delay
executions. See

NotificationBroadcasterSupport

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

ONE_DAY

Number of milliseconds in one day.

static long

ONE_HOUR

Number of milliseconds in one hour.

static long

ONE_MINUTE

Number of milliseconds in one minute.

static long

ONE_SECOND

Number of milliseconds in one second.

static long

ONE_WEEK

Number of milliseconds in one week.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Timer

()

Default constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences,
boolean fixedRate)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

Vector

<

Integer

>

getAllNotificationIDs

()

Gets all timer notification identifiers registered into the list of notifications.

Date

getDate

​(

Integer

id)

Gets a copy of the date associated to a timer notification.

Boolean

getFixedRate

​(

Integer

id)

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

int

getNbNotifications

()

Gets the number of timer notifications registered into the list of notifications.

Long

getNbOccurences

​(

Integer

id)

Gets a copy of the remaining number of occurrences associated to a timer notification.

Vector

<

Integer

>

getNotificationIDs

​(

String

type)

Gets all the identifiers of timer notifications corresponding to the specified type.

String

getNotificationMessage

​(

Integer

id)

Gets the timer notification detailed message corresponding to the specified identifier.

String

getNotificationType

​(

Integer

id)

Gets the timer notification type corresponding to the specified identifier.

Object

getNotificationUserData

​(

Integer

id)

Gets the timer notification user data object corresponding to the specified identifier.

Long

getPeriod

​(

Integer

id)

Gets a copy of the period (in milliseconds) associated to a timer notification.

boolean

getSendPastNotifications

()

Gets the flag indicating whether or not the timer sends past notifications.

boolean

isActive

()

Tests whether the timer MBean is active.

boolean

isEmpty

()

Tests whether the list of timer notifications is empty.

void

postDeregister

()

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

void

removeAllNotifications

()

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

void

removeNotification

​(

Integer

id)

Removes the timer notification corresponding to the specified identifier from the list of notifications.

void

removeNotifications

​(

String

type)

Removes all the timer notifications corresponding to the specified type from the list of notifications.

void

setSendPastNotifications

​(boolean value)

Sets the flag indicating whether the timer sends past notifications or not.

void

start

()

Starts the timer.

void

stop

()

Stops the timer.

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

static long

ONE_DAY

Number of milliseconds in one day.

static long

ONE_HOUR

Number of milliseconds in one hour.

static long

ONE_MINUTE

Number of milliseconds in one minute.

static long

ONE_SECOND

Number of milliseconds in one second.

static long

ONE_WEEK

Number of milliseconds in one week.

---

#### Field Summary

Number of milliseconds in one day.

Number of milliseconds in one hour.

Number of milliseconds in one minute.

Number of milliseconds in one second.

Number of milliseconds in one week.

Constructor Summary

Constructors

Constructor

Description

Timer

()

Default constructor.

---

#### Constructor Summary

Default constructor.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

Integer

addNotification

​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences,
boolean fixedRate)

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

Vector

<

Integer

>

getAllNotificationIDs

()

Gets all timer notification identifiers registered into the list of notifications.

Date

getDate

​(

Integer

id)

Gets a copy of the date associated to a timer notification.

Boolean

getFixedRate

​(

Integer

id)

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

int

getNbNotifications

()

Gets the number of timer notifications registered into the list of notifications.

Long

getNbOccurences

​(

Integer

id)

Gets a copy of the remaining number of occurrences associated to a timer notification.

Vector

<

Integer

>

getNotificationIDs

​(

String

type)

Gets all the identifiers of timer notifications corresponding to the specified type.

String

getNotificationMessage

​(

Integer

id)

Gets the timer notification detailed message corresponding to the specified identifier.

String

getNotificationType

​(

Integer

id)

Gets the timer notification type corresponding to the specified identifier.

Object

getNotificationUserData

​(

Integer

id)

Gets the timer notification user data object corresponding to the specified identifier.

Long

getPeriod

​(

Integer

id)

Gets a copy of the period (in milliseconds) associated to a timer notification.

boolean

getSendPastNotifications

()

Gets the flag indicating whether or not the timer sends past notifications.

boolean

isActive

()

Tests whether the timer MBean is active.

boolean

isEmpty

()

Tests whether the list of timer notifications is empty.

void

postDeregister

()

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

void

postRegister

​(

Boolean

registrationDone)

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

void

preDeregister

()

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

ObjectName

preRegister

​(

MBeanServer

server,

ObjectName

name)

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

void

removeAllNotifications

()

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

void

removeNotification

​(

Integer

id)

Removes the timer notification corresponding to the specified identifier from the list of notifications.

void

removeNotifications

​(

String

type)

Removes all the timer notifications corresponding to the specified type from the list of notifications.

void

setSendPastNotifications

​(boolean value)

Sets the flag indicating whether the timer sends past notifications or not.

void

start

()

Starts the timer.

void

stop

()

Stops the timer.

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

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

Gets all timer notification identifiers registered into the list of notifications.

Gets a copy of the date associated to a timer notification.

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

Gets the number of timer notifications registered into the list of notifications.

Gets a copy of the remaining number of occurrences associated to a timer notification.

Gets all the identifiers of timer notifications corresponding to the specified type.

Gets the timer notification detailed message corresponding to the specified identifier.

Gets the timer notification type corresponding to the specified identifier.

Gets the timer notification user data object corresponding to the specified identifier.

Gets a copy of the period (in milliseconds) associated to a timer notification.

Gets the flag indicating whether or not the timer sends past notifications.

Tests whether the timer MBean is active.

Tests whether the list of timer notifications is empty.

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

Removes the timer notification corresponding to the specified identifier from the list of notifications.

Removes all the timer notifications corresponding to the specified type from the list of notifications.

Sets the flag indicating whether the timer sends past notifications or not.

Starts the timer.

Stops the timer.

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

- ONE_SECOND

```java
public static final long ONE_SECOND
```

Number of milliseconds in one second.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_MINUTE

```java
public static final long ONE_MINUTE
```

Number of milliseconds in one minute.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_HOUR

```java
public static final long ONE_HOUR
```

Number of milliseconds in one hour.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_DAY

```java
public static final long ONE_DAY
```

Number of milliseconds in one day.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_WEEK

```java
public static final long ONE_WEEK
```

Number of milliseconds in one week.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Timer

```java
public Timer()
```

Default constructor.

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

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Not used in this context.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the timer MBean will be registered.
**Parameters:** name

- The object name of the timer MBean.
**Returns:** The name of the timer MBean registered.
**Throws:** Exception

- if something goes wrong

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

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

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Stops the timer.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- if something goes wrong

- postDeregister

```java
public void postDeregister()
```

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

- start

```java
public void start()
```

Starts the timer.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

**Specified by:** start

in interface

TimerMBean

- stop

```java
public void stop()
```

Stops the timer.

**Specified by:** stop

in interface

TimerMBean

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences,
boolean fixedRate)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Parameters:** fixedRate

- If

true

and if the notification is periodic, the notification
is scheduled with a

fixed-rate

execution scheme. If

false

and if the notification is periodic, the notification
is scheduled with a

fixed-delay

execution scheme. Ignored if the
notification is not periodic.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long)

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long, boolean)

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period is negative.

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

.

- removeNotification

```java
public void removeNotification​(
Integer
id)
throws
InstanceNotFoundException
```

Removes the timer notification corresponding to the specified identifier from the list of notifications.

**Specified by:** removeNotification

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Throws:** InstanceNotFoundException

- The specified identifier does not correspond to any timer notification
in the list of notifications of this timer MBean.

- removeNotifications

```java
public void removeNotifications​(
String
type)
throws
InstanceNotFoundException
```

Removes all the timer notifications corresponding to the specified type from the list of notifications.

**Specified by:** removeNotifications

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Throws:** InstanceNotFoundException

- The specified type does not correspond to any timer notification
in the list of notifications of this timer MBean.

- removeAllNotifications

```java
public void removeAllNotifications()
```

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

**Specified by:** removeAllNotifications

in interface

TimerMBean

- getNbNotifications

```java
public int getNbNotifications()
```

Gets the number of timer notifications registered into the list of notifications.

**Specified by:** getNbNotifications

in interface

TimerMBean
**Returns:** The number of timer notifications.

- getAllNotificationIDs

```java
public
Vector
<
Integer
> getAllNotificationIDs()
```

Gets all timer notification identifiers registered into the list of notifications.

**Specified by:** getAllNotificationIDs

in interface

TimerMBean
**Returns:** A vector of

Integer

objects containing all the timer notification identifiers.

The vector is empty if there is no timer notification registered for this timer MBean.

- getNotificationIDs

```java
public
Vector
<
Integer
> getNotificationIDs​(
String
type)
```

Gets all the identifiers of timer notifications corresponding to the specified type.

**Specified by:** getNotificationIDs

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Returns:** A vector of

Integer

objects containing all the identifiers of
timer notifications with the specified

type

.

The vector is empty if there is no timer notifications registered for this timer MBean
with the specified

type

.

- getNotificationType

```java
public
String
getNotificationType​(
Integer
id)
```

Gets the timer notification type corresponding to the specified identifier.

**Specified by:** getNotificationType

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification type or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNotificationMessage

```java
public
String
getNotificationMessage​(
Integer
id)
```

Gets the timer notification detailed message corresponding to the specified identifier.

**Specified by:** getNotificationMessage

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification detailed message or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNotificationUserData

```java
public
Object
getNotificationUserData​(
Integer
id)
```

Gets the timer notification user data object corresponding to the specified identifier.

**Specified by:** getNotificationUserData

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification user data object or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getDate

```java
public
Date
getDate​(
Integer
id)
```

Gets a copy of the date associated to a timer notification.

**Specified by:** getDate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the date or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getPeriod

```java
public
Long
getPeriod​(
Integer
id)
```

Gets a copy of the period (in milliseconds) associated to a timer notification.

**Specified by:** getPeriod

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the period or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNbOccurences

```java
public
Long
getNbOccurences​(
Integer
id)
```

Gets a copy of the remaining number of occurrences associated to a timer notification.

**Specified by:** getNbOccurences

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the remaining number of occurrences or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getFixedRate

```java
public
Boolean
getFixedRate​(
Integer
id)
```

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

**Specified by:** getFixedRate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

- getSendPastNotifications

```java
public boolean getSendPastNotifications()
```

Gets the flag indicating whether or not the timer sends past notifications.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** getSendPastNotifications

in interface

TimerMBean
**Returns:** The past notifications sending on/off flag value.
**See Also:** setSendPastNotifications(boolean)

- setSendPastNotifications

```java
public void setSendPastNotifications​(boolean value)
```

Sets the flag indicating whether the timer sends past notifications or not.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** setSendPastNotifications

in interface

TimerMBean
**Parameters:** value

- The past notifications sending on/off flag value.
**See Also:** getSendPastNotifications()

- isActive

```java
public boolean isActive()
```

Tests whether the timer MBean is active.
A timer MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

The default value of the active on/off flag is

false

.

**Specified by:** isActive

in interface

TimerMBean
**Returns:** true

if the timer MBean is active,

false

otherwise.

- isEmpty

```java
public boolean isEmpty()
```

Tests whether the list of timer notifications is empty.

**Specified by:** isEmpty

in interface

TimerMBean
**Returns:** true

if the list of timer notifications is empty,

false

otherwise.

Field Detail

- ONE_SECOND

```java
public static final long ONE_SECOND
```

Number of milliseconds in one second.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_MINUTE

```java
public static final long ONE_MINUTE
```

Number of milliseconds in one minute.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_HOUR

```java
public static final long ONE_HOUR
```

Number of milliseconds in one hour.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_DAY

```java
public static final long ONE_DAY
```

Number of milliseconds in one day.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

- ONE_WEEK

```java
public static final long ONE_WEEK
```

Number of milliseconds in one week.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### Field Detail

ONE_SECOND

```java
public static final long ONE_SECOND
```

Number of milliseconds in one second.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### ONE_SECOND

public static final long ONE_SECOND

Number of milliseconds in one second.
Useful constant for the

addNotification

method.

ONE_MINUTE

```java
public static final long ONE_MINUTE
```

Number of milliseconds in one minute.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### ONE_MINUTE

public static final long ONE_MINUTE

Number of milliseconds in one minute.
Useful constant for the

addNotification

method.

ONE_HOUR

```java
public static final long ONE_HOUR
```

Number of milliseconds in one hour.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### ONE_HOUR

public static final long ONE_HOUR

Number of milliseconds in one hour.
Useful constant for the

addNotification

method.

ONE_DAY

```java
public static final long ONE_DAY
```

Number of milliseconds in one day.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### ONE_DAY

public static final long ONE_DAY

Number of milliseconds in one day.
Useful constant for the

addNotification

method.

ONE_WEEK

```java
public static final long ONE_WEEK
```

Number of milliseconds in one week.
Useful constant for the

addNotification

method.

**See Also:** Constant Field Values

---

#### ONE_WEEK

public static final long ONE_WEEK

Number of milliseconds in one week.
Useful constant for the

addNotification

method.

Constructor Detail

- Timer

```java
public Timer()
```

Default constructor.

---

#### Constructor Detail

Timer

```java
public Timer()
```

Default constructor.

---

#### Timer

public Timer()

Default constructor.

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

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Not used in this context.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the timer MBean will be registered.
**Parameters:** name

- The object name of the timer MBean.
**Returns:** The name of the timer MBean registered.
**Throws:** Exception

- if something goes wrong

- postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

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

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Stops the timer.

**Specified by:** preDeregister

in interface

MBeanRegistration
**Throws:** Exception

- if something goes wrong

- postDeregister

```java
public void postDeregister()
```

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

- start

```java
public void start()
```

Starts the timer.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

**Specified by:** start

in interface

TimerMBean

- stop

```java
public void stop()
```

Stops the timer.

**Specified by:** stop

in interface

TimerMBean

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences,
boolean fixedRate)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Parameters:** fixedRate

- If

true

and if the notification is periodic, the notification
is scheduled with a

fixed-rate

execution scheme. If

false

and if the notification is periodic, the notification
is scheduled with a

fixed-delay

execution scheme. Ignored if the
notification is not periodic.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long)

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long, boolean)

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period is negative.

- addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

.

- removeNotification

```java
public void removeNotification​(
Integer
id)
throws
InstanceNotFoundException
```

Removes the timer notification corresponding to the specified identifier from the list of notifications.

**Specified by:** removeNotification

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Throws:** InstanceNotFoundException

- The specified identifier does not correspond to any timer notification
in the list of notifications of this timer MBean.

- removeNotifications

```java
public void removeNotifications​(
String
type)
throws
InstanceNotFoundException
```

Removes all the timer notifications corresponding to the specified type from the list of notifications.

**Specified by:** removeNotifications

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Throws:** InstanceNotFoundException

- The specified type does not correspond to any timer notification
in the list of notifications of this timer MBean.

- removeAllNotifications

```java
public void removeAllNotifications()
```

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

**Specified by:** removeAllNotifications

in interface

TimerMBean

- getNbNotifications

```java
public int getNbNotifications()
```

Gets the number of timer notifications registered into the list of notifications.

**Specified by:** getNbNotifications

in interface

TimerMBean
**Returns:** The number of timer notifications.

- getAllNotificationIDs

```java
public
Vector
<
Integer
> getAllNotificationIDs()
```

Gets all timer notification identifiers registered into the list of notifications.

**Specified by:** getAllNotificationIDs

in interface

TimerMBean
**Returns:** A vector of

Integer

objects containing all the timer notification identifiers.

The vector is empty if there is no timer notification registered for this timer MBean.

- getNotificationIDs

```java
public
Vector
<
Integer
> getNotificationIDs​(
String
type)
```

Gets all the identifiers of timer notifications corresponding to the specified type.

**Specified by:** getNotificationIDs

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Returns:** A vector of

Integer

objects containing all the identifiers of
timer notifications with the specified

type

.

The vector is empty if there is no timer notifications registered for this timer MBean
with the specified

type

.

- getNotificationType

```java
public
String
getNotificationType​(
Integer
id)
```

Gets the timer notification type corresponding to the specified identifier.

**Specified by:** getNotificationType

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification type or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNotificationMessage

```java
public
String
getNotificationMessage​(
Integer
id)
```

Gets the timer notification detailed message corresponding to the specified identifier.

**Specified by:** getNotificationMessage

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification detailed message or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNotificationUserData

```java
public
Object
getNotificationUserData​(
Integer
id)
```

Gets the timer notification user data object corresponding to the specified identifier.

**Specified by:** getNotificationUserData

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification user data object or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getDate

```java
public
Date
getDate​(
Integer
id)
```

Gets a copy of the date associated to a timer notification.

**Specified by:** getDate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the date or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getPeriod

```java
public
Long
getPeriod​(
Integer
id)
```

Gets a copy of the period (in milliseconds) associated to a timer notification.

**Specified by:** getPeriod

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the period or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getNbOccurences

```java
public
Long
getNbOccurences​(
Integer
id)
```

Gets a copy of the remaining number of occurrences associated to a timer notification.

**Specified by:** getNbOccurences

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the remaining number of occurrences or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

- getFixedRate

```java
public
Boolean
getFixedRate​(
Integer
id)
```

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

**Specified by:** getFixedRate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

- getSendPastNotifications

```java
public boolean getSendPastNotifications()
```

Gets the flag indicating whether or not the timer sends past notifications.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** getSendPastNotifications

in interface

TimerMBean
**Returns:** The past notifications sending on/off flag value.
**See Also:** setSendPastNotifications(boolean)

- setSendPastNotifications

```java
public void setSendPastNotifications​(boolean value)
```

Sets the flag indicating whether the timer sends past notifications or not.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** setSendPastNotifications

in interface

TimerMBean
**Parameters:** value

- The past notifications sending on/off flag value.
**See Also:** getSendPastNotifications()

- isActive

```java
public boolean isActive()
```

Tests whether the timer MBean is active.
A timer MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

The default value of the active on/off flag is

false

.

**Specified by:** isActive

in interface

TimerMBean
**Returns:** true

if the timer MBean is active,

false

otherwise.

- isEmpty

```java
public boolean isEmpty()
```

Tests whether the list of timer notifications is empty.

**Specified by:** isEmpty

in interface

TimerMBean
**Returns:** true

if the list of timer notifications is empty,

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

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Not used in this context.

**Specified by:** preRegister

in interface

MBeanRegistration
**Parameters:** server

- The MBean server in which the timer MBean will be registered.
**Parameters:** name

- The object name of the timer MBean.
**Returns:** The name of the timer MBean registered.
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

Allows the timer MBean to perform any operations it needs before being registered
in the MBean server.

Not used in this context.

Not used in this context.

postRegister

```java
public void postRegister​(
Boolean
registrationDone)
```

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

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

Allows the timer MBean to perform any operations needed after having been
registered in the MBean server or after the registration has failed.

Not used in this context.

Not used in this context.

preDeregister

```java
public void preDeregister()
throws
Exception
```

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Stops the timer.

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

Allows the timer MBean to perform any operations it needs before being unregistered
by the MBean server.

Stops the timer.

Stops the timer.

postDeregister

```java
public void postDeregister()
```

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Not used in this context.

**Specified by:** postDeregister

in interface

MBeanRegistration

---

#### postDeregister

public void postDeregister()

Allows the timer MBean to perform any operations needed after having been
unregistered by the MBean server.

Not used in this context.

Not used in this context.

start

```java
public void start()
```

Starts the timer.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

**Specified by:** start

in interface

TimerMBean

---

#### start

public void start()

Starts the timer.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

If there is one or more timer notifications before the time in the list of notifications, the notification
is sent according to the

sendPastNotifications

flag and then, updated
according to its period and remaining number of occurrences.
If the timer notification date remains earlier than the current date, this notification is just removed
from the list of notifications.

stop

```java
public void stop()
```

Stops the timer.

**Specified by:** stop

in interface

TimerMBean

---

#### stop

public void stop()

Stops the timer.

addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences,
boolean fixedRate)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Parameters:** fixedRate

- If

true

and if the notification is periodic, the notification
is scheduled with a

fixed-rate

execution scheme. If

false

and if the notification is periodic, the notification
is scheduled with a

fixed-delay

execution scheme. Ignored if the
notification is not periodic.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long)

---

#### addNotification

public

Integer

addNotification​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences,
boolean fixedRate)
throws

IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

In the case of a periodic notification, the value of parameter

fixedRate

is used to
specify the execution scheme, as specified in

Timer

.

addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period,
long nbOccurences)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Parameters:** nbOccurences

- The total number the timer notification will be emitted.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period or the number of occurrences is negative.
**See Also:** addNotification(String, String, Object, Date, long, long, boolean)

---

#### addNotification

public

Integer

addNotification​(

String

type,

String

message,

Object

userData,

Date

date,
long period,
long nbOccurences)
throws

IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date,
period and number of occurrences.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date.

For once-off notifications, the notification is delivered immediately.

For periodic notifications, the first notification is delivered immediately and the
subsequent ones are spaced as specified by the period parameter.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

Note that once the timer notification has been added into the list of notifications,
its associated date, period and number of occurrences cannot be updated.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

In the case of a periodic notification, uses a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long, boolean)

instead.

addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date,
long period)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Parameters:** period

- The period of the timer notification (in milliseconds).
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

or
the period is negative.

---

#### addNotification

public

Integer

addNotification​(

String

type,

String

message,

Object

userData,

Date

date,
long period)
throws

IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and period and a null number of occurrences.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

The timer notification will repeat continuously using the timer period using a

fixed-delay

execution scheme, as specified in

Timer

. In order to use a

fixed-rate

execution scheme, use

addNotification(String, String, Object, Date, long, long,
boolean)

instead.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date. The
first notification is delivered immediately and the subsequent ones are
spaced as specified by the period parameter.

addNotification

```java
public
Integer
addNotification​(
String
type,

String
message,

Object
userData,

Date
date)
throws
IllegalArgumentException
```

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

**Specified by:** addNotification

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Parameters:** message

- The timer notification detailed message.
**Parameters:** userData

- The timer notification user data object.
**Parameters:** date

- The date when the notification occurs.
**Returns:** The identifier of the new created timer notification.
**Throws:** IllegalArgumentException

- The date is

null

.

---

#### addNotification

public

Integer

addNotification​(

String

type,

String

message,

Object

userData,

Date

date)
throws

IllegalArgumentException

Creates a new timer notification with the specified

type

,

message

and

userData

and inserts it into the list of notifications with a given date
and a null period and number of occurrences.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

The timer notification will be handled once at the specified date.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

If the timer notification to be inserted has a date that is before the current date,
the method behaves as if the specified date were the current date and the
notification is delivered immediately.

removeNotification

```java
public void removeNotification​(
Integer
id)
throws
InstanceNotFoundException
```

Removes the timer notification corresponding to the specified identifier from the list of notifications.

**Specified by:** removeNotification

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Throws:** InstanceNotFoundException

- The specified identifier does not correspond to any timer notification
in the list of notifications of this timer MBean.

---

#### removeNotification

public void removeNotification​(

Integer

id)
throws

InstanceNotFoundException

Removes the timer notification corresponding to the specified identifier from the list of notifications.

removeNotifications

```java
public void removeNotifications​(
String
type)
throws
InstanceNotFoundException
```

Removes all the timer notifications corresponding to the specified type from the list of notifications.

**Specified by:** removeNotifications

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Throws:** InstanceNotFoundException

- The specified type does not correspond to any timer notification
in the list of notifications of this timer MBean.

---

#### removeNotifications

public void removeNotifications​(

String

type)
throws

InstanceNotFoundException

Removes all the timer notifications corresponding to the specified type from the list of notifications.

removeAllNotifications

```java
public void removeAllNotifications()
```

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

**Specified by:** removeAllNotifications

in interface

TimerMBean

---

#### removeAllNotifications

public void removeAllNotifications()

Removes all the timer notifications from the list of notifications
and resets the counter used to update the timer notification identifiers.

getNbNotifications

```java
public int getNbNotifications()
```

Gets the number of timer notifications registered into the list of notifications.

**Specified by:** getNbNotifications

in interface

TimerMBean
**Returns:** The number of timer notifications.

---

#### getNbNotifications

public int getNbNotifications()

Gets the number of timer notifications registered into the list of notifications.

getAllNotificationIDs

```java
public
Vector
<
Integer
> getAllNotificationIDs()
```

Gets all timer notification identifiers registered into the list of notifications.

**Specified by:** getAllNotificationIDs

in interface

TimerMBean
**Returns:** A vector of

Integer

objects containing all the timer notification identifiers.

The vector is empty if there is no timer notification registered for this timer MBean.

---

#### getAllNotificationIDs

public

Vector

<

Integer

> getAllNotificationIDs()

Gets all timer notification identifiers registered into the list of notifications.

getNotificationIDs

```java
public
Vector
<
Integer
> getNotificationIDs​(
String
type)
```

Gets all the identifiers of timer notifications corresponding to the specified type.

**Specified by:** getNotificationIDs

in interface

TimerMBean
**Parameters:** type

- The timer notification type.
**Returns:** A vector of

Integer

objects containing all the identifiers of
timer notifications with the specified

type

.

The vector is empty if there is no timer notifications registered for this timer MBean
with the specified

type

.

---

#### getNotificationIDs

public

Vector

<

Integer

> getNotificationIDs​(

String

type)

Gets all the identifiers of timer notifications corresponding to the specified type.

getNotificationType

```java
public
String
getNotificationType​(
Integer
id)
```

Gets the timer notification type corresponding to the specified identifier.

**Specified by:** getNotificationType

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification type or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getNotificationType

public

String

getNotificationType​(

Integer

id)

Gets the timer notification type corresponding to the specified identifier.

getNotificationMessage

```java
public
String
getNotificationMessage​(
Integer
id)
```

Gets the timer notification detailed message corresponding to the specified identifier.

**Specified by:** getNotificationMessage

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification detailed message or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getNotificationMessage

public

String

getNotificationMessage​(

Integer

id)

Gets the timer notification detailed message corresponding to the specified identifier.

getNotificationUserData

```java
public
Object
getNotificationUserData​(
Integer
id)
```

Gets the timer notification user data object corresponding to the specified identifier.

**Specified by:** getNotificationUserData

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** The timer notification user data object or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getNotificationUserData

public

Object

getNotificationUserData​(

Integer

id)

Gets the timer notification user data object corresponding to the specified identifier.

getDate

```java
public
Date
getDate​(
Integer
id)
```

Gets a copy of the date associated to a timer notification.

**Specified by:** getDate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the date or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getDate

public

Date

getDate​(

Integer

id)

Gets a copy of the date associated to a timer notification.

getPeriod

```java
public
Long
getPeriod​(
Integer
id)
```

Gets a copy of the period (in milliseconds) associated to a timer notification.

**Specified by:** getPeriod

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the period or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getPeriod

public

Long

getPeriod​(

Integer

id)

Gets a copy of the period (in milliseconds) associated to a timer notification.

getNbOccurences

```java
public
Long
getNbOccurences​(
Integer
id)
```

Gets a copy of the remaining number of occurrences associated to a timer notification.

**Specified by:** getNbOccurences

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the remaining number of occurrences or null if the identifier is not mapped to any
timer notification registered for this timer MBean.

---

#### getNbOccurences

public

Long

getNbOccurences​(

Integer

id)

Gets a copy of the remaining number of occurrences associated to a timer notification.

getFixedRate

```java
public
Boolean
getFixedRate​(
Integer
id)
```

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

**Specified by:** getFixedRate

in interface

TimerMBean
**Parameters:** id

- The timer notification identifier.
**Returns:** A copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

---

#### getFixedRate

public

Boolean

getFixedRate​(

Integer

id)

Gets a copy of the flag indicating whether a periodic notification is
executed at

fixed-delay

or at

fixed-rate

.

getSendPastNotifications

```java
public boolean getSendPastNotifications()
```

Gets the flag indicating whether or not the timer sends past notifications.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** getSendPastNotifications

in interface

TimerMBean
**Returns:** The past notifications sending on/off flag value.
**See Also:** setSendPastNotifications(boolean)

---

#### getSendPastNotifications

public boolean getSendPastNotifications()

Gets the flag indicating whether or not the timer sends past notifications.

The default value of the past notifications sending on/off flag is

false

.

setSendPastNotifications

```java
public void setSendPastNotifications​(boolean value)
```

Sets the flag indicating whether the timer sends past notifications or not.

The default value of the past notifications sending on/off flag is

false

.

**Specified by:** setSendPastNotifications

in interface

TimerMBean
**Parameters:** value

- The past notifications sending on/off flag value.
**See Also:** getSendPastNotifications()

---

#### setSendPastNotifications

public void setSendPastNotifications​(boolean value)

Sets the flag indicating whether the timer sends past notifications or not.

The default value of the past notifications sending on/off flag is

false

.

isActive

```java
public boolean isActive()
```

Tests whether the timer MBean is active.
A timer MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

The default value of the active on/off flag is

false

.

**Specified by:** isActive

in interface

TimerMBean
**Returns:** true

if the timer MBean is active,

false

otherwise.

---

#### isActive

public boolean isActive()

Tests whether the timer MBean is active.
A timer MBean is marked active when the

start

method is called.
It becomes inactive when the

stop

method is called.

The default value of the active on/off flag is

false

.

isEmpty

```java
public boolean isEmpty()
```

Tests whether the list of timer notifications is empty.

**Specified by:** isEmpty

in interface

TimerMBean
**Returns:** true

if the list of timer notifications is empty,

false

otherwise.

---

#### isEmpty

public boolean isEmpty()

Tests whether the list of timer notifications is empty.

---

