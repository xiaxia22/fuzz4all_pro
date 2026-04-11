# Class RecordedThread

**Source:** `jdk.jfr\jdk\jfr\consumer\RecordedThread.html`

### Class Description

```java
public final class
RecordedThread

extends
RecordedObject
```

A recorded thread.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
String
getOSName()

Returns the thread name used by the operating system.

**Returns:**
- the OS thread name, or

null

if doesn't exist

---

#### public long getOSThreadId()

Returns the thread ID used by the operating system.

**Returns:**
- The Java thread ID, or

-1

if doesn't exist

---

#### public
RecordedThreadGroup
getThreadGroup()

Returns the Java thread group, if available.

**Returns:**
- the thread group, or

null

if doesn't exist

---

#### public
String
getJavaName()

Returns the Java thread name, or

null

if if doesn't exist.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

**Returns:**
- the Java thread name, or

null

if doesn't exist

---

#### public long getJavaThreadId()

Returns the Java thread ID, or

-1

if it's not a Java thread.

**Returns:**
- the Java thread ID, or

-1

if it's not a Java thread

---

#### public long getId()

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

**Returns:**
- a unique ID for the thread

---

### Additional Sections

#### Class RecordedThread

java.lang.Object

- jdk.jfr.consumer.RecordedObject
- - jdk.jfr.consumer.RecordedThread

jdk.jfr.consumer.RecordedObject

- jdk.jfr.consumer.RecordedThread

jdk.jfr.consumer.RecordedThread

```java
public final class
RecordedThread

extends
RecordedObject
```

A recorded thread.

**Since:** 9

public final class

RecordedThread

extends

RecordedObject

A recorded thread.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getId

()

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

String

getJavaName

()

Returns the Java thread name, or

null

if if doesn't exist.

long

getJavaThreadId

()

Returns the Java thread ID, or

-1

if it's not a Java thread.

String

getOSName

()

Returns the thread name used by the operating system.

long

getOSThreadId

()

Returns the thread ID used by the operating system.

RecordedThreadGroup

getThreadGroup

()

Returns the Java thread group, if available.

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

long

getId

()

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

String

getJavaName

()

Returns the Java thread name, or

null

if if doesn't exist.

long

getJavaThreadId

()

Returns the Java thread ID, or

-1

if it's not a Java thread.

String

getOSName

()

Returns the thread name used by the operating system.

long

getOSThreadId

()

Returns the thread ID used by the operating system.

RecordedThreadGroup

getThreadGroup

()

Returns the Java thread group, if available.

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

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

Returns the Java thread name, or

null

if if doesn't exist.

Returns the Java thread ID, or

-1

if it's not a Java thread.

Returns the thread name used by the operating system.

Returns the thread ID used by the operating system.

Returns the Java thread group, if available.

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

- getOSName

```java
public
String
getOSName()
```

Returns the thread name used by the operating system.

**Returns:** the OS thread name, or

null

if doesn't exist

- getOSThreadId

```java
public long getOSThreadId()
```

Returns the thread ID used by the operating system.

**Returns:** The Java thread ID, or

-1

if doesn't exist

- getThreadGroup

```java
public
RecordedThreadGroup
getThreadGroup()
```

Returns the Java thread group, if available.

**Returns:** the thread group, or

null

if doesn't exist

- getJavaName

```java
public
String
getJavaName()
```

Returns the Java thread name, or

null

if if doesn't exist.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

**Returns:** the Java thread name, or

null

if doesn't exist

- getJavaThreadId

```java
public long getJavaThreadId()
```

Returns the Java thread ID, or

-1

if it's not a Java thread.

**Returns:** the Java thread ID, or

-1

if it's not a Java thread

- getId

```java
public long getId()
```

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

**Returns:** a unique ID for the thread

Method Detail

- getOSName

```java
public
String
getOSName()
```

Returns the thread name used by the operating system.

**Returns:** the OS thread name, or

null

if doesn't exist

- getOSThreadId

```java
public long getOSThreadId()
```

Returns the thread ID used by the operating system.

**Returns:** The Java thread ID, or

-1

if doesn't exist

- getThreadGroup

```java
public
RecordedThreadGroup
getThreadGroup()
```

Returns the Java thread group, if available.

**Returns:** the thread group, or

null

if doesn't exist

- getJavaName

```java
public
String
getJavaName()
```

Returns the Java thread name, or

null

if if doesn't exist.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

**Returns:** the Java thread name, or

null

if doesn't exist

- getJavaThreadId

```java
public long getJavaThreadId()
```

Returns the Java thread ID, or

-1

if it's not a Java thread.

**Returns:** the Java thread ID, or

-1

if it's not a Java thread

- getId

```java
public long getId()
```

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

**Returns:** a unique ID for the thread

---

#### Method Detail

getOSName

```java
public
String
getOSName()
```

Returns the thread name used by the operating system.

**Returns:** the OS thread name, or

null

if doesn't exist

---

#### getOSName

public

String

getOSName()

Returns the thread name used by the operating system.

getOSThreadId

```java
public long getOSThreadId()
```

Returns the thread ID used by the operating system.

**Returns:** The Java thread ID, or

-1

if doesn't exist

---

#### getOSThreadId

public long getOSThreadId()

Returns the thread ID used by the operating system.

getThreadGroup

```java
public
RecordedThreadGroup
getThreadGroup()
```

Returns the Java thread group, if available.

**Returns:** the thread group, or

null

if doesn't exist

---

#### getThreadGroup

public

RecordedThreadGroup

getThreadGroup()

Returns the Java thread group, if available.

getJavaName

```java
public
String
getJavaName()
```

Returns the Java thread name, or

null

if if doesn't exist.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

**Returns:** the Java thread name, or

null

if doesn't exist

---

#### getJavaName

public

String

getJavaName()

Returns the Java thread name, or

null

if if doesn't exist.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

Returns

java.lang.Thread.getName()

if the thread has a Java
representation.

null

otherwise.

getJavaThreadId

```java
public long getJavaThreadId()
```

Returns the Java thread ID, or

-1

if it's not a Java thread.

**Returns:** the Java thread ID, or

-1

if it's not a Java thread

---

#### getJavaThreadId

public long getJavaThreadId()

Returns the Java thread ID, or

-1

if it's not a Java thread.

getId

```java
public long getId()
```

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

**Returns:** a unique ID for the thread

---

#### getId

public long getId()

Returns a unique ID for both native threads and Java threads that can't be
reused within the lifespan of the JVM.

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

See

getJavaThreadId()

for the ID that is returned by

java.lang.Thread.getId()

---

