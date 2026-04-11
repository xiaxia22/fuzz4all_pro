# Class ClosedConnectionException

**Source:** `jdk.jdi\com\sun\jdi\connect\spi\ClosedConnectionException.html`

### Class Description

```java
public class
ClosedConnectionException

extends
IOException
```

This exception may be thrown as a result of an asynchronous
close of a

Connection

while an I/O operation is
in progress.

When a thread is blocked in

readPacket

waiting for packet from a target VM the

Connection

may be closed asynchronous by another
thread invokving the

close

method.
When this arises the thread in readPacket will throw this
exception. Similiarly when a thread is blocked in

Connection.writePacket(byte[])

the Connection may be closed.
When this occurs the thread in writePacket will throw
this exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClosedConnectionException()

Constructs a

ClosedConnectionException

with no detail
message.

---

#### public ClosedConnectionException​(
String
message)

Constructs a

ClosedConnectionException

with the
specified detail message.

**Parameters:**
- message

- the detail message pertaining to this exception.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ClosedConnectionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - com.sun.jdi.connect.spi.ClosedConnectionException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - com.sun.jdi.connect.spi.ClosedConnectionException

java.lang.Exception

- java.io.IOException
- - com.sun.jdi.connect.spi.ClosedConnectionException

java.io.IOException

- com.sun.jdi.connect.spi.ClosedConnectionException

com.sun.jdi.connect.spi.ClosedConnectionException

**All Implemented Interfaces:** Serializable

```java
public class
ClosedConnectionException

extends
IOException
```

This exception may be thrown as a result of an asynchronous
close of a

Connection

while an I/O operation is
in progress.

When a thread is blocked in

readPacket

waiting for packet from a target VM the

Connection

may be closed asynchronous by another
thread invokving the

close

method.
When this arises the thread in readPacket will throw this
exception. Similiarly when a thread is blocked in

Connection.writePacket(byte[])

the Connection may be closed.
When this occurs the thread in writePacket will throw
this exception.

**Since:** 1.5
**See Also:** Connection.readPacket()

,

Connection.writePacket(byte[])

,

Serialized Form

public class

ClosedConnectionException

extends

IOException

This exception may be thrown as a result of an asynchronous
close of a

Connection

while an I/O operation is
in progress.

When a thread is blocked in

readPacket

waiting for packet from a target VM the

Connection

may be closed asynchronous by another
thread invokving the

close

method.
When this arises the thread in readPacket will throw this
exception. Similiarly when a thread is blocked in

Connection.writePacket(byte[])

the Connection may be closed.
When this occurs the thread in writePacket will throw
this exception.

When a thread is blocked in

readPacket

waiting for packet from a target VM the

Connection

may be closed asynchronous by another
thread invokving the

close

method.
When this arises the thread in readPacket will throw this
exception. Similiarly when a thread is blocked in

Connection.writePacket(byte[])

the Connection may be closed.
When this occurs the thread in writePacket will throw
this exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClosedConnectionException

()

Constructs a

ClosedConnectionException

with no detail
message.

ClosedConnectionException

​(

String

message)

Constructs a

ClosedConnectionException

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

Constructor Summary

Constructors

Constructor

Description

ClosedConnectionException

()

Constructs a

ClosedConnectionException

with no detail
message.

ClosedConnectionException

​(

String

message)

Constructs a

ClosedConnectionException

with the
specified detail message.

---

#### Constructor Summary

Constructs a

ClosedConnectionException

with no detail
message.

Constructs a

ClosedConnectionException

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ClosedConnectionException

```java
public ClosedConnectionException()
```

Constructs a

ClosedConnectionException

with no detail
message.

- ClosedConnectionException

```java
public ClosedConnectionException​(
String
message)
```

Constructs a

ClosedConnectionException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

Constructor Detail

- ClosedConnectionException

```java
public ClosedConnectionException()
```

Constructs a

ClosedConnectionException

with no detail
message.

- ClosedConnectionException

```java
public ClosedConnectionException​(
String
message)
```

Constructs a

ClosedConnectionException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

---

#### Constructor Detail

ClosedConnectionException

```java
public ClosedConnectionException()
```

Constructs a

ClosedConnectionException

with no detail
message.

---

#### ClosedConnectionException

public ClosedConnectionException()

Constructs a

ClosedConnectionException

with no detail
message.

ClosedConnectionException

```java
public ClosedConnectionException​(
String
message)
```

Constructs a

ClosedConnectionException

with the
specified detail message.

**Parameters:** message

- the detail message pertaining to this exception.

---

#### ClosedConnectionException

public ClosedConnectionException​(

String

message)

Constructs a

ClosedConnectionException

with the
specified detail message.

---

