# Class IIOException

**Source:** `java.desktop\javax\imageio\IIOException.html`

### Class Description

```java
public class
IIOException

extends
IOException
```

An exception class used for signaling run-time failure of reading
and writing operations.

In addition to a message string, a reference to another

Throwable

(

Error

or

Exception

) is maintained. This reference, if
non-

null

, refers to the event that caused this
exception to occur. For example, an

IOException

while
reading from a

File

would be stored there.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public IIOException​(
String
message)

Constructs an

IIOException

with a given message

String

. No underlying cause is set;

getCause

will return

null

.

**Parameters:**
- message

- the error message.

**See Also:**
- Throwable.getMessage()

---

#### public IIOException​(
String
message,

Throwable
cause)

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

**Parameters:**
- message

- the error message.
- cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur.

**See Also:**
- Throwable.getCause()

,

Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class IIOException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.imageio.IIOException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.imageio.IIOException

java.lang.Exception

- java.io.IOException
- - javax.imageio.IIOException

java.io.IOException

- javax.imageio.IIOException

javax.imageio.IIOException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** IIOInvalidTreeException

```java
public class
IIOException

extends
IOException
```

An exception class used for signaling run-time failure of reading
and writing operations.

In addition to a message string, a reference to another

Throwable

(

Error

or

Exception

) is maintained. This reference, if
non-

null

, refers to the event that caused this
exception to occur. For example, an

IOException

while
reading from a

File

would be stored there.

**See Also:** Serialized Form

public class

IIOException

extends

IOException

An exception class used for signaling run-time failure of reading
and writing operations.

In addition to a message string, a reference to another

Throwable

(

Error

or

Exception

) is maintained. This reference, if
non-

null

, refers to the event that caused this
exception to occur. For example, an

IOException

while
reading from a

File

would be stored there.

In addition to a message string, a reference to another

Throwable

(

Error

or

Exception

) is maintained. This reference, if
non-

null

, refers to the event that caused this
exception to occur. For example, an

IOException

while
reading from a

File

would be stored there.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

IIOException

​(

String

message)

Constructs an

IIOException

with a given message

String

.

IIOException

​(

String

message,

Throwable

cause)

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

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

IIOException

​(

String

message)

Constructs an

IIOException

with a given message

String

.

IIOException

​(

String

message,

Throwable

cause)

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

---

#### Constructor Summary

Constructs an

IIOException

with a given message

String

.

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

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

- IIOException

```java
public IIOException​(
String
message)
```

Constructs an

IIOException

with a given message

String

. No underlying cause is set;

getCause

will return

null

.

**Parameters:** message

- the error message.
**See Also:** Throwable.getMessage()

- IIOException

```java
public IIOException​(
String
message,

Throwable
cause)
```

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

**Parameters:** message

- the error message.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur.
**See Also:** Throwable.getCause()

,

Throwable.getMessage()

Constructor Detail

- IIOException

```java
public IIOException​(
String
message)
```

Constructs an

IIOException

with a given message

String

. No underlying cause is set;

getCause

will return

null

.

**Parameters:** message

- the error message.
**See Also:** Throwable.getMessage()

- IIOException

```java
public IIOException​(
String
message,

Throwable
cause)
```

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

**Parameters:** message

- the error message.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur.
**See Also:** Throwable.getCause()

,

Throwable.getMessage()

---

#### Constructor Detail

IIOException

```java
public IIOException​(
String
message)
```

Constructs an

IIOException

with a given message

String

. No underlying cause is set;

getCause

will return

null

.

**Parameters:** message

- the error message.
**See Also:** Throwable.getMessage()

---

#### IIOException

public IIOException​(

String

message)

Constructs an

IIOException

with a given message

String

. No underlying cause is set;

getCause

will return

null

.

IIOException

```java
public IIOException​(
String
message,

Throwable
cause)
```

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

**Parameters:** message

- the error message.
**Parameters:** cause

- the

Throwable

(

Error

or

Exception

) that caused this exception to occur.
**See Also:** Throwable.getCause()

,

Throwable.getMessage()

---

#### IIOException

public IIOException​(

String

message,

Throwable

cause)

Constructs an

IIOException

with a given message

String

and a

Throwable

that was its
underlying cause.

---

