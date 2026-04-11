# Class GarbageCollectionNotificationInfo

**Source:** `jdk.management\com\sun\management\GarbageCollectionNotificationInfo.html`

### Class Description

```java
public class
GarbageCollectionNotificationInfo

extends
Object

implements
CompositeDataView
```

The information about a garbage collection

A garbage collection notification is emitted by

GarbageCollectorMXBean

when the Java virtual machine completes a garbage collection action
The notification emitted will contain the garbage collection notification
information about the status of the memory:

- The name of the garbage collector used to perform the collection.
- The action performed by the garbage collector.
- The cause of the garbage collection action.
- A

GcInfo

object containing some statistics about the GC cycle
(start time, end time) and the memory usage before and after
the GC cycle.

A

CompositeData

representing
the

GarbageCollectionNotificationInfo

object
is stored in the

userdata

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

GarbageCollectionNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}
```

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

**All Implemented Interfaces:** CompositeDataView

---

### Field Details

#### public static final
String
GARBAGE_COLLECTION_NOTIFICATION

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.
This notification is emitted by a

GarbageCollectorMXBean

.
The value of this notification type is

com.sun.management.gc.notification

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public GarbageCollectionNotificationInfo​(
String
gcName,

String
gcAction,

String
gcCause,

GcInfo
gcInfo)

Constructs a

GarbageCollectionNotificationInfo

object.

**Parameters:**
- gcName

- The name of the garbage collector used to perform the collection
- gcAction

- The name of the action performed by the garbage collector
- gcCause

- The cause of the garbage collection action
- gcInfo

- a GcInfo object providing statistics about the GC cycle

---

### Method Details

#### public
String
getGcName()

Returns the name of the garbage collector used to perform the collection

**Returns:**
- the name of the garbage collector used to perform the collection

---

#### public
String
getGcAction()

Returns the action performed by the garbage collector

**Returns:**
- the action performed by the garbage collector

---

#### public
String
getGcCause()

Returns the cause of the garbage collection

**Returns:**
- the cause of the garbage collection

---

#### public
GcInfo
getGcInfo()

Returns the GC information related to the last garbage collection

**Returns:**
- the GC information related to the
last garbage collection

---

#### public static
GarbageCollectionNotificationInfo
from​(
CompositeData
cd)

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

description

Attribute Name

Type

gcName

java.lang.String

gcAction

java.lang.String

gcCause

java.lang.String

gcInfo

javax.management.openmbean.CompositeData

**Parameters:**
- cd

-

CompositeData

representing a

GarbageCollectionNotificationInfo

**Returns:**
- a

GarbageCollectionNotificationInfo

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

GarbaageCollectionNotificationInfo

object.

---

### Additional Sections

#### Class GarbageCollectionNotificationInfo

java.lang.Object

- com.sun.management.GarbageCollectionNotificationInfo

com.sun.management.GarbageCollectionNotificationInfo

**All Implemented Interfaces:** CompositeDataView

```java
public class
GarbageCollectionNotificationInfo

extends
Object

implements
CompositeDataView
```

The information about a garbage collection

A garbage collection notification is emitted by

GarbageCollectorMXBean

when the Java virtual machine completes a garbage collection action
The notification emitted will contain the garbage collection notification
information about the status of the memory:

- The name of the garbage collector used to perform the collection.
- The action performed by the garbage collector.
- The cause of the garbage collection action.
- A

GcInfo

object containing some statistics about the GC cycle
(start time, end time) and the memory usage before and after
the GC cycle.

A

CompositeData

representing
the

GarbageCollectionNotificationInfo

object
is stored in the

userdata

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

GarbageCollectionNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}
```

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

public class

GarbageCollectionNotificationInfo

extends

Object

implements

CompositeDataView

The information about a garbage collection

A garbage collection notification is emitted by

GarbageCollectorMXBean

when the Java virtual machine completes a garbage collection action
The notification emitted will contain the garbage collection notification
information about the status of the memory:

- The name of the garbage collector used to perform the collection.
- The action performed by the garbage collector.
- The cause of the garbage collection action.
- A

GcInfo

object containing some statistics about the GC cycle
(start time, end time) and the memory usage before and after
the GC cycle.

A

CompositeData

representing
the

GarbageCollectionNotificationInfo

object
is stored in the

userdata

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

GarbageCollectionNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}
```

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

A garbage collection notification is emitted by

GarbageCollectorMXBean

when the Java virtual machine completes a garbage collection action
The notification emitted will contain the garbage collection notification
information about the status of the memory:

- The name of the garbage collector used to perform the collection.
- The action performed by the garbage collector.
- The cause of the garbage collection action.
- A

GcInfo

object containing some statistics about the GC cycle
(start time, end time) and the memory usage before and after
the GC cycle.

A

CompositeData

representing
the

GarbageCollectionNotificationInfo

object
is stored in the

userdata

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

GarbageCollectionNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}
```

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

The name of the garbage collector used to perform the collection.

The action performed by the garbage collector.

The cause of the garbage collection action.

A

GcInfo

object containing some statistics about the GC cycle
(start time, end time) and the memory usage before and after
the GC cycle.

A

CompositeData

representing
the

GarbageCollectionNotificationInfo

object
is stored in the

userdata

of a

notification

.
The

from

method is provided to convert from
a

CompositeData

to a

GarbageCollectionNotificationInfo

object. For example:

```java
Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}
```

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

Notification notif;

// receive the notification emitted by a GarbageCollectorMXBean and set to notif
...

String notifType = notif.getType();
if (notifType.equals(GarbageCollectionNotificationInfo.GARBAGE_COLLECTION_NOTIFICATION)) {
// retrieve the garbage collection notification information
CompositeData cd = (CompositeData) notif.getUserData();
GarbageCollectionNotificationInfo info = GarbageCollectionNotificationInfo.from(cd);
....
}

The type of the notification emitted by a

GarbageCollectorMXBean

is:

- A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

A

garbage collection notification

.

Used by every notification emitted by the garbage collector, the details about
the notification are provided in the

action

String

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

GARBAGE_COLLECTION_NOTIFICATION

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

GarbageCollectionNotificationInfo

​(

String

gcName,

String

gcAction,

String

gcCause,

GcInfo

gcInfo)

Constructs a

GarbageCollectionNotificationInfo

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

GarbageCollectionNotificationInfo

from

​(

CompositeData

cd)

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.

String

getGcAction

()

Returns the action performed by the garbage collector

String

getGcCause

()

Returns the cause of the garbage collection

GcInfo

getGcInfo

()

Returns the GC information related to the last garbage collection

String

getGcName

()

Returns the name of the garbage collector used to perform the collection

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

- Methods declared in interface javax.management.openmbean.

CompositeDataView

toCompositeData

Field Summary

Fields

Modifier and Type

Field

Description

static

String

GARBAGE_COLLECTION_NOTIFICATION

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.

---

#### Field Summary

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.

Constructor Summary

Constructors

Constructor

Description

GarbageCollectionNotificationInfo

​(

String

gcName,

String

gcAction,

String

gcCause,

GcInfo

gcInfo)

Constructs a

GarbageCollectionNotificationInfo

object.

---

#### Constructor Summary

Constructs a

GarbageCollectionNotificationInfo

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

GarbageCollectionNotificationInfo

from

​(

CompositeData

cd)

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.

String

getGcAction

()

Returns the action performed by the garbage collector

String

getGcCause

()

Returns the cause of the garbage collection

GcInfo

getGcInfo

()

Returns the GC information related to the last garbage collection

String

getGcName

()

Returns the name of the garbage collector used to perform the collection

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

- Methods declared in interface javax.management.openmbean.

CompositeDataView

toCompositeData

---

#### Method Summary

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.

Returns the action performed by the garbage collector

Returns the cause of the garbage collection

Returns the GC information related to the last garbage collection

Returns the name of the garbage collector used to perform the collection

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

Methods declared in interface javax.management.openmbean.

CompositeDataView

toCompositeData

---

#### Methods declared in interface javax.management.openmbean. CompositeDataView

============ FIELD DETAIL ===========

- Field Detail

- GARBAGE_COLLECTION_NOTIFICATION

```java
public static final
String
GARBAGE_COLLECTION_NOTIFICATION
```

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.
This notification is emitted by a

GarbageCollectorMXBean

.
The value of this notification type is

com.sun.management.gc.notification

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- GarbageCollectionNotificationInfo

```java
public GarbageCollectionNotificationInfo​(
String
gcName,

String
gcAction,

String
gcCause,

GcInfo
gcInfo)
```

Constructs a

GarbageCollectionNotificationInfo

object.

**Parameters:** gcName

- The name of the garbage collector used to perform the collection
**Parameters:** gcAction

- The name of the action performed by the garbage collector
**Parameters:** gcCause

- The cause of the garbage collection action
**Parameters:** gcInfo

- a GcInfo object providing statistics about the GC cycle

============ METHOD DETAIL ==========

- Method Detail

- getGcName

```java
public
String
getGcName()
```

Returns the name of the garbage collector used to perform the collection

**Returns:** the name of the garbage collector used to perform the collection

- getGcAction

```java
public
String
getGcAction()
```

Returns the action performed by the garbage collector

**Returns:** the action performed by the garbage collector

- getGcCause

```java
public
String
getGcCause()
```

Returns the cause of the garbage collection

**Returns:** the cause of the garbage collection

- getGcInfo

```java
public
GcInfo
getGcInfo()
```

Returns the GC information related to the last garbage collection

**Returns:** the GC information related to the
last garbage collection

- from

```java
public static
GarbageCollectionNotificationInfo
from​(
CompositeData
cd)
```

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

description

Attribute Name

Type

gcName

java.lang.String

gcAction

java.lang.String

gcCause

java.lang.String

gcInfo

javax.management.openmbean.CompositeData

**Parameters:** cd

-

CompositeData

representing a

GarbageCollectionNotificationInfo
**Returns:** a

GarbageCollectionNotificationInfo

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

GarbaageCollectionNotificationInfo

object.

Field Detail

- GARBAGE_COLLECTION_NOTIFICATION

```java
public static final
String
GARBAGE_COLLECTION_NOTIFICATION
```

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.
This notification is emitted by a

GarbageCollectorMXBean

.
The value of this notification type is

com.sun.management.gc.notification

.

**See Also:** Constant Field Values

---

#### Field Detail

GARBAGE_COLLECTION_NOTIFICATION

```java
public static final
String
GARBAGE_COLLECTION_NOTIFICATION
```

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.
This notification is emitted by a

GarbageCollectorMXBean

.
The value of this notification type is

com.sun.management.gc.notification

.

**See Also:** Constant Field Values

---

#### GARBAGE_COLLECTION_NOTIFICATION

public static final

String

GARBAGE_COLLECTION_NOTIFICATION

Notification type denoting that
the Java virtual machine has completed a garbage collection cycle.
This notification is emitted by a

GarbageCollectorMXBean

.
The value of this notification type is

com.sun.management.gc.notification

.

Constructor Detail

- GarbageCollectionNotificationInfo

```java
public GarbageCollectionNotificationInfo​(
String
gcName,

String
gcAction,

String
gcCause,

GcInfo
gcInfo)
```

Constructs a

GarbageCollectionNotificationInfo

object.

**Parameters:** gcName

- The name of the garbage collector used to perform the collection
**Parameters:** gcAction

- The name of the action performed by the garbage collector
**Parameters:** gcCause

- The cause of the garbage collection action
**Parameters:** gcInfo

- a GcInfo object providing statistics about the GC cycle

---

#### Constructor Detail

GarbageCollectionNotificationInfo

```java
public GarbageCollectionNotificationInfo​(
String
gcName,

String
gcAction,

String
gcCause,

GcInfo
gcInfo)
```

Constructs a

GarbageCollectionNotificationInfo

object.

**Parameters:** gcName

- The name of the garbage collector used to perform the collection
**Parameters:** gcAction

- The name of the action performed by the garbage collector
**Parameters:** gcCause

- The cause of the garbage collection action
**Parameters:** gcInfo

- a GcInfo object providing statistics about the GC cycle

---

#### GarbageCollectionNotificationInfo

public GarbageCollectionNotificationInfo​(

String

gcName,

String

gcAction,

String

gcCause,

GcInfo

gcInfo)

Constructs a

GarbageCollectionNotificationInfo

object.

Method Detail

- getGcName

```java
public
String
getGcName()
```

Returns the name of the garbage collector used to perform the collection

**Returns:** the name of the garbage collector used to perform the collection

- getGcAction

```java
public
String
getGcAction()
```

Returns the action performed by the garbage collector

**Returns:** the action performed by the garbage collector

- getGcCause

```java
public
String
getGcCause()
```

Returns the cause of the garbage collection

**Returns:** the cause of the garbage collection

- getGcInfo

```java
public
GcInfo
getGcInfo()
```

Returns the GC information related to the last garbage collection

**Returns:** the GC information related to the
last garbage collection

- from

```java
public static
GarbageCollectionNotificationInfo
from​(
CompositeData
cd)
```

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

description

Attribute Name

Type

gcName

java.lang.String

gcAction

java.lang.String

gcCause

java.lang.String

gcInfo

javax.management.openmbean.CompositeData

**Parameters:** cd

-

CompositeData

representing a

GarbageCollectionNotificationInfo
**Returns:** a

GarbageCollectionNotificationInfo

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

GarbaageCollectionNotificationInfo

object.

---

#### Method Detail

getGcName

```java
public
String
getGcName()
```

Returns the name of the garbage collector used to perform the collection

**Returns:** the name of the garbage collector used to perform the collection

---

#### getGcName

public

String

getGcName()

Returns the name of the garbage collector used to perform the collection

getGcAction

```java
public
String
getGcAction()
```

Returns the action performed by the garbage collector

**Returns:** the action performed by the garbage collector

---

#### getGcAction

public

String

getGcAction()

Returns the action performed by the garbage collector

getGcCause

```java
public
String
getGcCause()
```

Returns the cause of the garbage collection

**Returns:** the cause of the garbage collection

---

#### getGcCause

public

String

getGcCause()

Returns the cause of the garbage collection

getGcInfo

```java
public
GcInfo
getGcInfo()
```

Returns the GC information related to the last garbage collection

**Returns:** the GC information related to the
last garbage collection

---

#### getGcInfo

public

GcInfo

getGcInfo()

Returns the GC information related to the last garbage collection

from

```java
public static
GarbageCollectionNotificationInfo
from​(
CompositeData
cd)
```

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

description

Attribute Name

Type

gcName

java.lang.String

gcAction

java.lang.String

gcCause

java.lang.String

gcInfo

javax.management.openmbean.CompositeData

**Parameters:** cd

-

CompositeData

representing a

GarbageCollectionNotificationInfo
**Returns:** a

GarbageCollectionNotificationInfo

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

GarbaageCollectionNotificationInfo

object.

---

#### from

public static

GarbageCollectionNotificationInfo

from​(

CompositeData

cd)

Returns a

GarbageCollectionNotificationInfo

object represented by the
given

CompositeData

.
The given

CompositeData

must contain
the following attributes:

description

Attribute Name

Type

gcName

java.lang.String

gcAction

java.lang.String

gcCause

java.lang.String

gcInfo

javax.management.openmbean.CompositeData

---

