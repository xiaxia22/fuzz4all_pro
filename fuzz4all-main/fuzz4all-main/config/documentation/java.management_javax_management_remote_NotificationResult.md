# Class NotificationResult

**Source:** `java.management\javax\management\remote\NotificationResult.html`

### Class Description

```java
public class
NotificationResult

extends
Object

implements
Serializable
```

Result of a query for buffered notifications. Notifications in
a notification buffer have positive, monotonically increasing
sequence numbers. The result of a notification query contains the
following elements:

- The sequence number of the earliest notification still in
the buffer.

The sequence number of the next notification available for
querying. This will be the starting sequence number for the next
notification query.

An array of (Notification,listenerID) pairs corresponding to
the returned notifications and the listeners they correspond to.

It is possible for the

nextSequenceNumber

to be less
than the

earliestSequenceNumber

. This signifies that
notifications between the two might have been lost.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotificationResult​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification
[] targetedNotifications)

Constructs a notification query result.

**Parameters:**
- earliestSequenceNumber

- the sequence number of the
earliest notification still in the buffer.
- nextSequenceNumber

- the sequence number of the next
notification available for querying.
- targetedNotifications

- the notifications resulting from
the query, and the listeners they correspond to. This array
can be empty.

**Throws:**
- IllegalArgumentException

- if

targetedNotifications

is null or if

earliestSequenceNumber

or

nextSequenceNumber

is negative.

---

### Method Details

#### public long getEarliestSequenceNumber()

Returns the sequence number of the earliest notification still
in the buffer.

**Returns:**
- the sequence number of the earliest notification still
in the buffer.

---

#### public long getNextSequenceNumber()

Returns the sequence number of the next notification available
for querying.

**Returns:**
- the sequence number of the next notification available
for querying.

---

#### public
TargetedNotification
[] getTargetedNotifications()

Returns the notifications resulting from the query, and the
listeners they correspond to.

**Returns:**
- the notifications resulting from the query, and the
listeners they correspond to. This array can be empty.

---

#### public
String
toString()

Returns a string representation of the object. The result
should be a concise but informative representation that is easy
for a person to read.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class NotificationResult

java.lang.Object

- javax.management.remote.NotificationResult

javax.management.remote.NotificationResult

**All Implemented Interfaces:** Serializable

```java
public class
NotificationResult

extends
Object

implements
Serializable
```

Result of a query for buffered notifications. Notifications in
a notification buffer have positive, monotonically increasing
sequence numbers. The result of a notification query contains the
following elements:

- The sequence number of the earliest notification still in
the buffer.

The sequence number of the next notification available for
querying. This will be the starting sequence number for the next
notification query.

An array of (Notification,listenerID) pairs corresponding to
the returned notifications and the listeners they correspond to.

It is possible for the

nextSequenceNumber

to be less
than the

earliestSequenceNumber

. This signifies that
notifications between the two might have been lost.

**Since:** 1.5
**See Also:** Serialized Form

public class

NotificationResult

extends

Object

implements

Serializable

Result of a query for buffered notifications. Notifications in
a notification buffer have positive, monotonically increasing
sequence numbers. The result of a notification query contains the
following elements:

- The sequence number of the earliest notification still in
the buffer.

The sequence number of the next notification available for
querying. This will be the starting sequence number for the next
notification query.

An array of (Notification,listenerID) pairs corresponding to
the returned notifications and the listeners they correspond to.

It is possible for the

nextSequenceNumber

to be less
than the

earliestSequenceNumber

. This signifies that
notifications between the two might have been lost.

Result of a query for buffered notifications. Notifications in
a notification buffer have positive, monotonically increasing
sequence numbers. The result of a notification query contains the
following elements:

The sequence number of the earliest notification still in
the buffer.

The sequence number of the next notification available for
querying. This will be the starting sequence number for the next
notification query.

An array of (Notification,listenerID) pairs corresponding to
the returned notifications and the listeners they correspond to.

It is possible for the

nextSequenceNumber

to be less
than the

earliestSequenceNumber

. This signifies that
notifications between the two might have been lost.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NotificationResult

​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification

[] targetedNotifications)

Constructs a notification query result.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getEarliestSequenceNumber

()

Returns the sequence number of the earliest notification still
in the buffer.

long

getNextSequenceNumber

()

Returns the sequence number of the next notification available
for querying.

TargetedNotification

[]

getTargetedNotifications

()

Returns the notifications resulting from the query, and the
listeners they correspond to.

String

toString

()

Returns a string representation of the object.

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

NotificationResult

​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification

[] targetedNotifications)

Constructs a notification query result.

---

#### Constructor Summary

Constructs a notification query result.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getEarliestSequenceNumber

()

Returns the sequence number of the earliest notification still
in the buffer.

long

getNextSequenceNumber

()

Returns the sequence number of the next notification available
for querying.

TargetedNotification

[]

getTargetedNotifications

()

Returns the notifications resulting from the query, and the
listeners they correspond to.

String

toString

()

Returns a string representation of the object.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the sequence number of the earliest notification still
in the buffer.

Returns the sequence number of the next notification available
for querying.

Returns the notifications resulting from the query, and the
listeners they correspond to.

Returns a string representation of the object.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NotificationResult

```java
public NotificationResult​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification
[] targetedNotifications)
```

Constructs a notification query result.

**Parameters:** earliestSequenceNumber

- the sequence number of the
earliest notification still in the buffer.
**Parameters:** nextSequenceNumber

- the sequence number of the next
notification available for querying.
**Parameters:** targetedNotifications

- the notifications resulting from
the query, and the listeners they correspond to. This array
can be empty.
**Throws:** IllegalArgumentException

- if

targetedNotifications

is null or if

earliestSequenceNumber

or

nextSequenceNumber

is negative.

============ METHOD DETAIL ==========

- Method Detail

- getEarliestSequenceNumber

```java
public long getEarliestSequenceNumber()
```

Returns the sequence number of the earliest notification still
in the buffer.

**Returns:** the sequence number of the earliest notification still
in the buffer.

- getNextSequenceNumber

```java
public long getNextSequenceNumber()
```

Returns the sequence number of the next notification available
for querying.

**Returns:** the sequence number of the next notification available
for querying.

- getTargetedNotifications

```java
public
TargetedNotification
[] getTargetedNotifications()
```

Returns the notifications resulting from the query, and the
listeners they correspond to.

**Returns:** the notifications resulting from the query, and the
listeners they correspond to. This array can be empty.

- toString

```java
public
String
toString()
```

Returns a string representation of the object. The result
should be a concise but informative representation that is easy
for a person to read.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- NotificationResult

```java
public NotificationResult​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification
[] targetedNotifications)
```

Constructs a notification query result.

**Parameters:** earliestSequenceNumber

- the sequence number of the
earliest notification still in the buffer.
**Parameters:** nextSequenceNumber

- the sequence number of the next
notification available for querying.
**Parameters:** targetedNotifications

- the notifications resulting from
the query, and the listeners they correspond to. This array
can be empty.
**Throws:** IllegalArgumentException

- if

targetedNotifications

is null or if

earliestSequenceNumber

or

nextSequenceNumber

is negative.

---

#### Constructor Detail

NotificationResult

```java
public NotificationResult​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification
[] targetedNotifications)
```

Constructs a notification query result.

**Parameters:** earliestSequenceNumber

- the sequence number of the
earliest notification still in the buffer.
**Parameters:** nextSequenceNumber

- the sequence number of the next
notification available for querying.
**Parameters:** targetedNotifications

- the notifications resulting from
the query, and the listeners they correspond to. This array
can be empty.
**Throws:** IllegalArgumentException

- if

targetedNotifications

is null or if

earliestSequenceNumber

or

nextSequenceNumber

is negative.

---

#### NotificationResult

public NotificationResult​(long earliestSequenceNumber,
long nextSequenceNumber,

TargetedNotification

[] targetedNotifications)

Constructs a notification query result.

Method Detail

- getEarliestSequenceNumber

```java
public long getEarliestSequenceNumber()
```

Returns the sequence number of the earliest notification still
in the buffer.

**Returns:** the sequence number of the earliest notification still
in the buffer.

- getNextSequenceNumber

```java
public long getNextSequenceNumber()
```

Returns the sequence number of the next notification available
for querying.

**Returns:** the sequence number of the next notification available
for querying.

- getTargetedNotifications

```java
public
TargetedNotification
[] getTargetedNotifications()
```

Returns the notifications resulting from the query, and the
listeners they correspond to.

**Returns:** the notifications resulting from the query, and the
listeners they correspond to. This array can be empty.

- toString

```java
public
String
toString()
```

Returns a string representation of the object. The result
should be a concise but informative representation that is easy
for a person to read.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getEarliestSequenceNumber

```java
public long getEarliestSequenceNumber()
```

Returns the sequence number of the earliest notification still
in the buffer.

**Returns:** the sequence number of the earliest notification still
in the buffer.

---

#### getEarliestSequenceNumber

public long getEarliestSequenceNumber()

Returns the sequence number of the earliest notification still
in the buffer.

getNextSequenceNumber

```java
public long getNextSequenceNumber()
```

Returns the sequence number of the next notification available
for querying.

**Returns:** the sequence number of the next notification available
for querying.

---

#### getNextSequenceNumber

public long getNextSequenceNumber()

Returns the sequence number of the next notification available
for querying.

getTargetedNotifications

```java
public
TargetedNotification
[] getTargetedNotifications()
```

Returns the notifications resulting from the query, and the
listeners they correspond to.

**Returns:** the notifications resulting from the query, and the
listeners they correspond to. This array can be empty.

---

#### getTargetedNotifications

public

TargetedNotification

[] getTargetedNotifications()

Returns the notifications resulting from the query, and the
listeners they correspond to.

toString

```java
public
String
toString()
```

Returns a string representation of the object. The result
should be a concise but informative representation that is easy
for a person to read.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string representation of the object. The result
should be a concise but informative representation that is easy
for a person to read.

---

