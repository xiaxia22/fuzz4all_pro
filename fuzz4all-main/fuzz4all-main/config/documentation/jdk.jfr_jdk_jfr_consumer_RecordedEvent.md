# Class RecordedEvent

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedEvent.html`

### Class Description

```java
public final class
RecordedEvent

extends
RecordedObject
```

A recorded event.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
RecordedStackTrace
getStackTrace()

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

**Returns:**
- stack trace, or

null

if doesn't exist for the event

---

#### public
RecordedThread
getThread()

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

**Returns:**
- thread, or

null

if doesn't exist for the event

---

#### public
EventType
getEventType()

Returns the event type that describes the event.

**Returns:**
- the event type, not

null

---

#### public
Instant
getStartTime()

Returns the start time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:**
- the start time, not

null

---

#### public
Instant
getEndTime()

Returns the end time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:**
- the end time, not

null

---

#### public
Duration
getDuration()

Returns the duration of the event, measured in nanoseconds.

**Returns:**
- the duration in nanoseconds, not

null

---

#### public
List
<
ValueDescriptor
> getFields()

Returns the list of descriptors that describes the fields of the event.

**Overrides:**
- getFields

in class

RecordedObject

**Returns:**
- descriptors, not

null

---

### Additional Sections

#### Class RecordedEvent

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedEvent

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedEvent

jdk.jfr.consumer.RecordedEvent

```java
public final class
RecordedEvent

extends
RecordedObject
```

A recorded event.

**Since:** 9

public final class

RecordedEvent

extends

RecordedObject

A recorded event.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Duration

getDuration

()

Returns the duration of the event, measured in nanoseconds.

Instant

getEndTime

()

Returns the end time of the event.

EventType

getEventType

()

Returns the event type that describes the event.

List

<

ValueDescriptor

>

getFields

()

Returns the list of descriptors that describes the fields of the event.

RecordedStackTrace

getStackTrace

()

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

Instant

getStartTime

()

Returns the start time of the event.

RecordedThread

getThread

()

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

,

toString

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Duration

getDuration

()

Returns the duration of the event, measured in nanoseconds.

Instant

getEndTime

()

Returns the end time of the event.

EventType

getEventType

()

Returns the event type that describes the event.

List

<

ValueDescriptor

>

getFields

()

Returns the list of descriptors that describes the fields of the event.

RecordedStackTrace

getStackTrace

()

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

Instant

getStartTime

()

Returns the start time of the event.

RecordedThread

getThread

()

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

- Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

,

toString

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

Returns the duration of the event, measured in nanoseconds.

Returns the end time of the event.

Returns the event type that describes the event.

Returns the list of descriptors that describes the fields of the event.

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

Returns the start time of the event.

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

Methods declared in class jdk.jfr.consumer.

RecordedObject

getBoolean

,

getByte

,

getChar

,

getClass

,

getDouble

,

getDuration

,

getFloat

,

getInstant

,

getInt

,

getLong

,

getShort

,

getString

,

getThread

,

getValue

,

hasField

,

toString

---

#### Methods declared in class jdk.jfr.consumer. RecordedObject

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

============ METHOD DETAIL ==========

- Method Detail

- getStackTrace

```java
public
RecordedStackTrace
getStackTrace()
```

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

**Returns:** stack trace, or

null

if doesn't exist for the event

- getThread

```java
public
RecordedThread
getThread()
```

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

**Returns:** thread, or

null

if doesn't exist for the event

- getEventType

```java
public
EventType
getEventType()
```

Returns the event type that describes the event.

**Returns:** the event type, not

null

- getStartTime

```java
public
Instant
getStartTime()
```

Returns the start time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the start time, not

null

- getEndTime

```java
public
Instant
getEndTime()
```

Returns the end time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the end time, not

null

- getDuration

```java
public
Duration
getDuration()
```

Returns the duration of the event, measured in nanoseconds.

**Returns:** the duration in nanoseconds, not

null

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns the list of descriptors that describes the fields of the event.

**Overrides:** getFields

in class

RecordedObject
**Returns:** descriptors, not

null

Method Detail

- getStackTrace

```java
public
RecordedStackTrace
getStackTrace()
```

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

**Returns:** stack trace, or

null

if doesn't exist for the event

- getThread

```java
public
RecordedThread
getThread()
```

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

**Returns:** thread, or

null

if doesn't exist for the event

- getEventType

```java
public
EventType
getEventType()
```

Returns the event type that describes the event.

**Returns:** the event type, not

null

- getStartTime

```java
public
Instant
getStartTime()
```

Returns the start time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the start time, not

null

- getEndTime

```java
public
Instant
getEndTime()
```

Returns the end time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the end time, not

null

- getDuration

```java
public
Duration
getDuration()
```

Returns the duration of the event, measured in nanoseconds.

**Returns:** the duration in nanoseconds, not

null

- getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns the list of descriptors that describes the fields of the event.

**Overrides:** getFields

in class

RecordedObject
**Returns:** descriptors, not

null

---

#### Method Detail

getStackTrace

```java
public
RecordedStackTrace
getStackTrace()
```

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

**Returns:** stack trace, or

null

if doesn't exist for the event

---

#### getStackTrace

public

RecordedStackTrace

getStackTrace()

Returns the stack trace that was created when the event was committed, or

null

if the event lacks a stack trace.

getThread

```java
public
RecordedThread
getThread()
```

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

**Returns:** thread, or

null

if doesn't exist for the event

---

#### getThread

public

RecordedThread

getThread()

Returns the thread from which the event was committed, or

null

if
the thread was not recorded.

getEventType

```java
public
EventType
getEventType()
```

Returns the event type that describes the event.

**Returns:** the event type, not

null

---

#### getEventType

public

EventType

getEventType()

Returns the event type that describes the event.

getStartTime

```java
public
Instant
getStartTime()
```

Returns the start time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the start time, not

null

---

#### getStartTime

public

Instant

getStartTime()

Returns the start time of the event.

If the event is an instant event, then the start time and end time are the same.

If the event is an instant event, then the start time and end time are the same.

getEndTime

```java
public
Instant
getEndTime()
```

Returns the end time of the event.

If the event is an instant event, then the start time and end time are the same.

**Returns:** the end time, not

null

---

#### getEndTime

public

Instant

getEndTime()

Returns the end time of the event.

If the event is an instant event, then the start time and end time are the same.

If the event is an instant event, then the start time and end time are the same.

getDuration

```java
public
Duration
getDuration()
```

Returns the duration of the event, measured in nanoseconds.

**Returns:** the duration in nanoseconds, not

null

---

#### getDuration

public

Duration

getDuration()

Returns the duration of the event, measured in nanoseconds.

getFields

```java
public
List
<
ValueDescriptor
> getFields()
```

Returns the list of descriptors that describes the fields of the event.

**Overrides:** getFields

in class

RecordedObject
**Returns:** descriptors, not

null

---

#### getFields

public

List

<

ValueDescriptor

> getFields()

Returns the list of descriptors that describes the fields of the event.

---

