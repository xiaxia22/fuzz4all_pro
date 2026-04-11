# Class MemoryNotificationInfo

**Source:** `java.management\java\lang\management\MemoryNotificationInfo.html`

### Class Description

```java
public class
MemoryNotificationInfo

extends
Object
```

The information about a memory notification.

A memory notification is emitted by

MemoryMXBean

when the Java virtual machine detects that the memory usage
of a memory pool is exceeding a threshold value.
The notification emitted will contain the memory notification
information about the detected condition:

- The name of the memory pool.
- The memory usage of the memory pool when the notification
was constructed.
- The number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

usage threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

A

CompositeData

representing
the

MemoryNotificationInfo

object
is stored in the

user data

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

MemoryNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}
```

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

**Since:** 1.5

---

### Field Details

#### public static final
String
MEMORY_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.
This notification is emitted by

MemoryMXBean

.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
The value of this notification type is

java.management.memory.threshold.exceeded

.

**See Also:**
- Constant Field Values

---

#### public static final
String
MEMORY_COLLECTION_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.
This notification is emitted by

MemoryMXBean

.
The value of this notification type is

java.management.memory.collection.threshold.exceeded

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MemoryNotificationInfo​(
String
poolName,

MemoryUsage
usage,
long count)

Constructs a

MemoryNotificationInfo

object.

**Parameters:**
- poolName

- The name of the memory pool which triggers this notification.
- usage

- Memory usage of the memory pool.
- count

- The threshold crossing count.

---

### Method Details

#### public
String
getPoolName()

Returns the name of the memory pool that triggers this notification.
The memory pool usage has crossed a threshold.

**Returns:**
- the name of the memory pool that triggers this notification.

---

#### public
MemoryUsage
getUsage()

Returns the memory usage of the memory pool
when this notification was constructed.

**Returns:**
- the memory usage of the memory pool
when this notification was constructed.

---

#### public long getCount()

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

**Returns:**
- the number of times that the memory usage has crossed
a threshold when the notification was constructed.

---

#### public static
MemoryNotificationInfo
from​(
CompositeData
cd)

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

poolName

java.lang.String

usage

javax.management.openmbean.CompositeData

count

java.lang.Long

**Parameters:**
- cd

-

CompositeData

representing a

MemoryNotificationInfo

**Returns:**
- a

MemoryNotificationInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.

**Throws:**
- IllegalArgumentException

- if

cd

does not
represent a

MemoryNotificationInfo

object.

---

### Additional Sections

#### Class MemoryNotificationInfo

java.lang.Object

- java.lang.management.MemoryNotificationInfo

java.lang.management.MemoryNotificationInfo

```java
public class
MemoryNotificationInfo

extends
Object
```

The information about a memory notification.

A memory notification is emitted by

MemoryMXBean

when the Java virtual machine detects that the memory usage
of a memory pool is exceeding a threshold value.
The notification emitted will contain the memory notification
information about the detected condition:

- The name of the memory pool.
- The memory usage of the memory pool when the notification
was constructed.
- The number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

usage threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

A

CompositeData

representing
the

MemoryNotificationInfo

object
is stored in the

user data

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

MemoryNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}
```

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

**Since:** 1.5

public class

MemoryNotificationInfo

extends

Object

The information about a memory notification.

A memory notification is emitted by

MemoryMXBean

when the Java virtual machine detects that the memory usage
of a memory pool is exceeding a threshold value.
The notification emitted will contain the memory notification
information about the detected condition:

- The name of the memory pool.
- The memory usage of the memory pool when the notification
was constructed.
- The number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

usage threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

A

CompositeData

representing
the

MemoryNotificationInfo

object
is stored in the

user data

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

MemoryNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}
```

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

A memory notification is emitted by

MemoryMXBean

when the Java virtual machine detects that the memory usage
of a memory pool is exceeding a threshold value.
The notification emitted will contain the memory notification
information about the detected condition:

- The name of the memory pool.
- The memory usage of the memory pool when the notification
was constructed.
- The number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

usage threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

A

CompositeData

representing
the

MemoryNotificationInfo

object
is stored in the

user data

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

MemoryNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}
```

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

The name of the memory pool.

The memory usage of the memory pool when the notification
was constructed.

The number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

usage threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

A

CompositeData

representing
the

MemoryNotificationInfo

object
is stored in the

user data

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

MemoryNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}
```

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

Notification notif;

// receive the notification emitted by MemoryMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(MemoryNotificationInfo.MEMORY_THRESHOLD_EXCEEDED) ||
notifType.equals(MemoryNotificationInfo.MEMORY_COLLECTION_THRESHOLD_EXCEEDED)) {
// retrieve the memory notification information
CompositeData cd = (CompositeData) notif.getUserData();
MemoryNotificationInfo info = MemoryNotificationInfo.from(cd);
....
}

The types of notifications emitted by

MemoryMXBean

are:

- A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
- A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

A

usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is increased and has reached
or exceeded its

usage threshold

value.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.

A

collection usage threshold exceeded notification

.

This notification will be emitted when
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

MEMORY_COLLECTION_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

static

String

MEMORY_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MemoryNotificationInfo

​(

String

poolName,

MemoryUsage

usage,
long count)

Constructs a

MemoryNotificationInfo

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemoryNotificationInfo

from

​(

CompositeData

cd)

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.

long

getCount

()

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.

String

getPoolName

()

Returns the name of the memory pool that triggers this notification.

MemoryUsage

getUsage

()

Returns the memory usage of the memory pool
when this notification was constructed.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

MEMORY_COLLECTION_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

static

String

MEMORY_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.

---

#### Field Summary

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.

Constructor Summary

Constructors

Constructor

Description

MemoryNotificationInfo

​(

String

poolName,

MemoryUsage

usage,
long count)

Constructs a

MemoryNotificationInfo

object.

---

#### Constructor Summary

Constructs a

MemoryNotificationInfo

object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

MemoryNotificationInfo

from

​(

CompositeData

cd)

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.

long

getCount

()

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.

String

getPoolName

()

Returns the name of the memory pool that triggers this notification.

MemoryUsage

getUsage

()

Returns the memory usage of the memory pool
when this notification was constructed.

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

---

#### Method Summary

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.

Returns the name of the memory pool that triggers this notification.

Returns the memory usage of the memory pool
when this notification was constructed.

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

============ FIELD DETAIL ===========

- Field Detail

- MEMORY_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.
This notification is emitted by

MemoryMXBean

.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
The value of this notification type is

java.management.memory.threshold.exceeded

.

**See Also:** Constant Field Values

- MEMORY_COLLECTION_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_COLLECTION_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.
This notification is emitted by

MemoryMXBean

.
The value of this notification type is

java.management.memory.collection.threshold.exceeded

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MemoryNotificationInfo

```java
public MemoryNotificationInfo​(
String
poolName,

MemoryUsage
usage,
long count)
```

Constructs a

MemoryNotificationInfo

object.

**Parameters:** poolName

- The name of the memory pool which triggers this notification.
**Parameters:** usage

- Memory usage of the memory pool.
**Parameters:** count

- The threshold crossing count.

============ METHOD DETAIL ==========

- Method Detail

- getPoolName

```java
public
String
getPoolName()
```

Returns the name of the memory pool that triggers this notification.
The memory pool usage has crossed a threshold.

**Returns:** the name of the memory pool that triggers this notification.

- getUsage

```java
public
MemoryUsage
getUsage()
```

Returns the memory usage of the memory pool
when this notification was constructed.

**Returns:** the memory usage of the memory pool
when this notification was constructed.

- getCount

```java
public long getCount()
```

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

**Returns:** the number of times that the memory usage has crossed
a threshold when the notification was constructed.

- from

```java
public static
MemoryNotificationInfo
from​(
CompositeData
cd)
```

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

poolName

java.lang.String

usage

javax.management.openmbean.CompositeData

count

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryNotificationInfo
**Returns:** a

MemoryNotificationInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryNotificationInfo

object.

Field Detail

- MEMORY_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.
This notification is emitted by

MemoryMXBean

.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
The value of this notification type is

java.management.memory.threshold.exceeded

.

**See Also:** Constant Field Values

- MEMORY_COLLECTION_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_COLLECTION_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.
This notification is emitted by

MemoryMXBean

.
The value of this notification type is

java.management.memory.collection.threshold.exceeded

.

**See Also:** Constant Field Values

---

#### Field Detail

MEMORY_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.
This notification is emitted by

MemoryMXBean

.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
The value of this notification type is

java.management.memory.threshold.exceeded

.

**See Also:** Constant Field Values

---

#### MEMORY_THRESHOLD_EXCEEDED

public static final

String

MEMORY_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool has
reached or exceeded its

usage threshold

value.
This notification is emitted by

MemoryMXBean

.
Subsequent crossing of the usage threshold value does not cause
further notification until the memory usage has returned
to become less than the usage threshold value.
The value of this notification type is

java.management.memory.threshold.exceeded

.

MEMORY_COLLECTION_THRESHOLD_EXCEEDED

```java
public static final
String
MEMORY_COLLECTION_THRESHOLD_EXCEEDED
```

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.
This notification is emitted by

MemoryMXBean

.
The value of this notification type is

java.management.memory.collection.threshold.exceeded

.

**See Also:** Constant Field Values

---

#### MEMORY_COLLECTION_THRESHOLD_EXCEEDED

public static final

String

MEMORY_COLLECTION_THRESHOLD_EXCEEDED

Notification type denoting that
the memory usage of a memory pool is greater than or equal to its

collection usage threshold

after the Java virtual machine
has expended effort in recycling unused objects in that
memory pool.
This notification is emitted by

MemoryMXBean

.
The value of this notification type is

java.management.memory.collection.threshold.exceeded

.

Constructor Detail

- MemoryNotificationInfo

```java
public MemoryNotificationInfo​(
String
poolName,

MemoryUsage
usage,
long count)
```

Constructs a

MemoryNotificationInfo

object.

**Parameters:** poolName

- The name of the memory pool which triggers this notification.
**Parameters:** usage

- Memory usage of the memory pool.
**Parameters:** count

- The threshold crossing count.

---

#### Constructor Detail

MemoryNotificationInfo

```java
public MemoryNotificationInfo​(
String
poolName,

MemoryUsage
usage,
long count)
```

Constructs a

MemoryNotificationInfo

object.

**Parameters:** poolName

- The name of the memory pool which triggers this notification.
**Parameters:** usage

- Memory usage of the memory pool.
**Parameters:** count

- The threshold crossing count.

---

#### MemoryNotificationInfo

public MemoryNotificationInfo​(

String

poolName,

MemoryUsage

usage,
long count)

Constructs a

MemoryNotificationInfo

object.

Method Detail

- getPoolName

```java
public
String
getPoolName()
```

Returns the name of the memory pool that triggers this notification.
The memory pool usage has crossed a threshold.

**Returns:** the name of the memory pool that triggers this notification.

- getUsage

```java
public
MemoryUsage
getUsage()
```

Returns the memory usage of the memory pool
when this notification was constructed.

**Returns:** the memory usage of the memory pool
when this notification was constructed.

- getCount

```java
public long getCount()
```

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

**Returns:** the number of times that the memory usage has crossed
a threshold when the notification was constructed.

- from

```java
public static
MemoryNotificationInfo
from​(
CompositeData
cd)
```

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

poolName

java.lang.String

usage

javax.management.openmbean.CompositeData

count

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryNotificationInfo
**Returns:** a

MemoryNotificationInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryNotificationInfo

object.

---

#### Method Detail

getPoolName

```java
public
String
getPoolName()
```

Returns the name of the memory pool that triggers this notification.
The memory pool usage has crossed a threshold.

**Returns:** the name of the memory pool that triggers this notification.

---

#### getPoolName

public

String

getPoolName()

Returns the name of the memory pool that triggers this notification.
The memory pool usage has crossed a threshold.

getUsage

```java
public
MemoryUsage
getUsage()
```

Returns the memory usage of the memory pool
when this notification was constructed.

**Returns:** the memory usage of the memory pool
when this notification was constructed.

---

#### getUsage

public

MemoryUsage

getUsage()

Returns the memory usage of the memory pool
when this notification was constructed.

getCount

```java
public long getCount()
```

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

**Returns:** the number of times that the memory usage has crossed
a threshold when the notification was constructed.

---

#### getCount

public long getCount()

Returns the number of times that the memory usage has crossed
a threshold when the notification was constructed.
For usage threshold notifications, this count will be the

threshold
count

. For collection threshold notifications,
this count will be the

collection usage threshold count

.

from

```java
public static
MemoryNotificationInfo
from​(
CompositeData
cd)
```

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

poolName

java.lang.String

usage

javax.management.openmbean.CompositeData

count

java.lang.Long

**Parameters:** cd

-

CompositeData

representing a

MemoryNotificationInfo
**Returns:** a

MemoryNotificationInfo

object represented
by

cd

if

cd

is not

null

;

null

otherwise.
**Throws:** IllegalArgumentException

- if

cd

does not
represent a

MemoryNotificationInfo

object.

---

#### from

public static

MemoryNotificationInfo

from​(

CompositeData

cd)

Returns a

MemoryNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

The attributes and the types the given CompositeData contains

Attribute Name

Type

poolName

java.lang.String

usage

javax.management.openmbean.CompositeData

count

java.lang.Long

---

