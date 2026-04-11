# Class InterruptedIOException

**Source:** `java.base\java\io\InterruptedIOException.html`

### Class Description

```java
public class
InterruptedIOException

extends
IOException
```

Signals that an I/O operation has been interrupted. An

InterruptedIOException

is thrown to indicate that an
input or output transfer has been terminated because the thread
performing it was interrupted. The field

bytesTransferred

indicates how many bytes were successfully transferred before
the interruption occurred.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public int bytesTransferred

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

---

### Constructor Details

#### public InterruptedIOException()

Constructs an

InterruptedIOException

with

null

as its error detail message.

---

#### public InterruptedIOException​(
String
s)

Constructs an

InterruptedIOException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:**
- s

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InterruptedIOException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.InterruptedIOException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.InterruptedIOException

java.lang.Exception

- java.io.IOException
- - java.io.InterruptedIOException

java.io.IOException

- java.io.InterruptedIOException

java.io.InterruptedIOException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SocketTimeoutException

```java
public class
InterruptedIOException

extends
IOException
```

Signals that an I/O operation has been interrupted. An

InterruptedIOException

is thrown to indicate that an
input or output transfer has been terminated because the thread
performing it was interrupted. The field

bytesTransferred

indicates how many bytes were successfully transferred before
the interruption occurred.

**Since:** 1.0
**See Also:** InputStream

,

OutputStream

,

Thread.interrupt()

,

Serialized Form

public class

InterruptedIOException

extends

IOException

Signals that an I/O operation has been interrupted. An

InterruptedIOException

is thrown to indicate that an
input or output transfer has been terminated because the thread
performing it was interrupted. The field

bytesTransferred

indicates how many bytes were successfully transferred before
the interruption occurred.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

int

bytesTransferred

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InterruptedIOException

()

Constructs an

InterruptedIOException

with

null

as its error detail message.

InterruptedIOException

​(

String

s)

Constructs an

InterruptedIOException

with the
specified detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Field Summary

Fields

Modifier and Type

Field

Description

int

bytesTransferred

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

---

#### Field Summary

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

Constructor Summary

Constructors

Constructor

Description

InterruptedIOException

()

Constructs an

InterruptedIOException

with

null

as its error detail message.

InterruptedIOException

​(

String

s)

Constructs an

InterruptedIOException

with the
specified detail message.

---

#### Constructor Summary

Constructs an

InterruptedIOException

with

null

as its error detail message.

Constructs an

InterruptedIOException

with the
specified detail message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

============ FIELD DETAIL ===========

- Field Detail

- bytesTransferred

```java
public int bytesTransferred
```

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InterruptedIOException

```java
public InterruptedIOException()
```

Constructs an

InterruptedIOException

with

null

as its error detail message.

- InterruptedIOException

```java
public InterruptedIOException​(
String
s)
```

Constructs an

InterruptedIOException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

Field Detail

- bytesTransferred

```java
public int bytesTransferred
```

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

---

#### Field Detail

bytesTransferred

```java
public int bytesTransferred
```

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

---

#### bytesTransferred

public int bytesTransferred

Reports how many bytes had been transferred as part of the I/O
operation before it was interrupted.

Constructor Detail

- InterruptedIOException

```java
public InterruptedIOException()
```

Constructs an

InterruptedIOException

with

null

as its error detail message.

- InterruptedIOException

```java
public InterruptedIOException​(
String
s)
```

Constructs an

InterruptedIOException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

---

#### Constructor Detail

InterruptedIOException

```java
public InterruptedIOException()
```

Constructs an

InterruptedIOException

with

null

as its error detail message.

---

#### InterruptedIOException

public InterruptedIOException()

Constructs an

InterruptedIOException

with

null

as its error detail message.

InterruptedIOException

```java
public InterruptedIOException​(
String
s)
```

Constructs an

InterruptedIOException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

**Parameters:** s

- the detail message.

---

#### InterruptedIOException

public InterruptedIOException​(

String

s)

Constructs an

InterruptedIOException

with the
specified detail message. The string

s

can be
retrieved later by the

Throwable.getMessage()

method of class

java.lang.Throwable

.

---

