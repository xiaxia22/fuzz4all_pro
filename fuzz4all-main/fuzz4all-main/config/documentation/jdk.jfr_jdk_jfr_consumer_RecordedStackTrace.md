# Class RecordedStackTrace

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedStackTrace.html`

### Class Description

```java
public final class
RecordedStackTrace

extends
RecordedObject
```

A recorded stack trace.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
List
<
RecordedFrame
> getFrames()

Returns the frames in the stack trace.

**Returns:**
- a list of Java stack frames, not

null

---

#### public boolean isTruncated()

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

**Returns:**
- true

if the stack trace is truncated,

false

otherwise

---

### Additional Sections

#### Class RecordedStackTrace

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedStackTrace

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedStackTrace

jdk.jfr.consumer.RecordedStackTrace

```java
public final class
RecordedStackTrace

extends
RecordedObject
```

A recorded stack trace.

**Since:** 9

public final class

RecordedStackTrace

extends

RecordedObject

A recorded stack trace.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

List

<

RecordedFrame

>

getFrames

()

Returns the frames in the stack trace.

boolean

isTruncated

()

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

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

getFields

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

List

<

RecordedFrame

>

getFrames

()

Returns the frames in the stack trace.

boolean

isTruncated

()

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

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

getFields

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

Returns the frames in the stack trace.

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

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

getFields

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

- getFrames

```java
public
List
<
RecordedFrame
> getFrames()
```

Returns the frames in the stack trace.

**Returns:** a list of Java stack frames, not

null

- isTruncated

```java
public boolean isTruncated()
```

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

**Returns:** true

if the stack trace is truncated,

false

otherwise

Method Detail

- getFrames

```java
public
List
<
RecordedFrame
> getFrames()
```

Returns the frames in the stack trace.

**Returns:** a list of Java stack frames, not

null

- isTruncated

```java
public boolean isTruncated()
```

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

**Returns:** true

if the stack trace is truncated,

false

otherwise

---

#### Method Detail

getFrames

```java
public
List
<
RecordedFrame
> getFrames()
```

Returns the frames in the stack trace.

**Returns:** a list of Java stack frames, not

null

---

#### getFrames

public

List

<

RecordedFrame

> getFrames()

Returns the frames in the stack trace.

isTruncated

```java
public boolean isTruncated()
```

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

**Returns:** true

if the stack trace is truncated,

false

otherwise

---

#### isTruncated

public boolean isTruncated()

Returns

true

if the stack trace is truncated due to its size,

false

otherwise.

---

