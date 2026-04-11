# Class ClosedChannelException

**Source:** `java.base\java\nio\channels\ClosedChannelException.html`

### Class Description

```java
public class
ClosedChannelException

extends
IOException
```

Checked exception thrown when an attempt is made to invoke or complete an
I/O operation upon channel that is closed, or at least closed to that
operation. That this exception is thrown does not necessarily imply that
the channel is completely closed. A socket channel whose write half has
been shut down, for example, may still be open for reading.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClosedChannelException()

Constructs an instance of this class.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ClosedChannelException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.nio.channels.ClosedChannelException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.nio.channels.ClosedChannelException

java.lang.Exception

- java.io.IOException
- - java.nio.channels.ClosedChannelException

java.io.IOException

- java.nio.channels.ClosedChannelException

java.nio.channels.ClosedChannelException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AsynchronousCloseException

```java
public class
ClosedChannelException

extends
IOException
```

Checked exception thrown when an attempt is made to invoke or complete an
I/O operation upon channel that is closed, or at least closed to that
operation. That this exception is thrown does not necessarily imply that
the channel is completely closed. A socket channel whose write half has
been shut down, for example, may still be open for reading.

**Since:** 1.4
**See Also:** Serialized Form

public class

ClosedChannelException

extends

IOException

Checked exception thrown when an attempt is made to invoke or complete an
I/O operation upon channel that is closed, or at least closed to that
operation. That this exception is thrown does not necessarily imply that
the channel is completely closed. A socket channel whose write half has
been shut down, for example, may still be open for reading.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClosedChannelException

()

Constructs an instance of this class.

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

Constructor Summary

Constructors

Constructor

Description

ClosedChannelException

()

Constructs an instance of this class.

---

#### Constructor Summary

Constructs an instance of this class.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ClosedChannelException

```java
public ClosedChannelException()
```

Constructs an instance of this class.

Constructor Detail

- ClosedChannelException

```java
public ClosedChannelException()
```

Constructs an instance of this class.

---

#### Constructor Detail

ClosedChannelException

```java
public ClosedChannelException()
```

Constructs an instance of this class.

---

#### ClosedChannelException

public ClosedChannelException()

Constructs an instance of this class.

---

