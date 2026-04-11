# Class SQLIntegrityConstraintViolationException

**Source:** `java.sql\java\sql\SQLIntegrityConstraintViolationException.html`

### Class Description

```java
public class
SQLIntegrityConstraintViolationException

extends
SQLNonTransientException
```

The subclass of

SQLException

thrown when the SQLState class value
is '

23

', or under vendor-specified conditions.
This indicates that an integrity
constraint (foreign key, primary key or unique key) has been violated.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public SQLIntegrityConstraintViolationException()

Constructs a

SQLIntegrityConstraintViolationException

object.
The

reason

,

SQLState

are initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason)

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized
to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:**
- reason

- a description of the exception

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState)

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

**Parameters:**
- reason

- a description of the exception
- SQLState

- an XOPEN or SQL:2003 code identifying the exception

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:**
- reason

- a description of the exception
- SQLState

- an XOPEN or SQL:2003 code identifying the exception
- vendorCode

- a database vendor specific exception code

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
Throwable
cause)

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.
The

reason

is initialized to

null

if

cause==null

or to

cause.toString()

if

cause!=null

.

**Parameters:**
- cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason,

Throwable
cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

**Parameters:**
- reason

- a description of the exception.
- cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:**
- reason

- a description of the exception.
- SQLState

- an XOPEN or SQL:2003 code identifying the exception
- cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

**Parameters:**
- reason

- a description of the exception
- SQLState

- an XOPEN or SQL:2003 code identifying the exception
- vendorCode

- a database vendor-specific exception code
- cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SQLIntegrityConstraintViolationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLIntegrityConstraintViolationException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLIntegrityConstraintViolationException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLIntegrityConstraintViolationException

java.sql.SQLException

- java.sql.SQLNonTransientException
- - java.sql.SQLIntegrityConstraintViolationException

java.sql.SQLNonTransientException

- java.sql.SQLIntegrityConstraintViolationException

java.sql.SQLIntegrityConstraintViolationException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLIntegrityConstraintViolationException

extends
SQLNonTransientException
```

The subclass of

SQLException

thrown when the SQLState class value
is '

23

', or under vendor-specified conditions.
This indicates that an integrity
constraint (foreign key, primary key or unique key) has been violated.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLIntegrityConstraintViolationException

extends

SQLNonTransientException

The subclass of

SQLException

thrown when the SQLState class value
is '

23

', or under vendor-specified conditions.
This indicates that an integrity
constraint (foreign key, primary key or unique key) has been violated.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLIntegrityConstraintViolationException

()

Constructs a

SQLIntegrityConstraintViolationException

object.

SQLIntegrityConstraintViolationException

​(

String

reason)

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState)

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.

SQLIntegrityConstraintViolationException

​(

String

reason,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.

SQLIntegrityConstraintViolationException

​(

Throwable

cause)

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

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

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

Constructor Summary

Constructors

Constructor

Description

SQLIntegrityConstraintViolationException

()

Constructs a

SQLIntegrityConstraintViolationException

object.

SQLIntegrityConstraintViolationException

​(

String

reason)

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState)

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

SQLIntegrityConstraintViolationException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.

SQLIntegrityConstraintViolationException

​(

String

reason,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.

SQLIntegrityConstraintViolationException

​(

Throwable

cause)

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.

---

#### Constructor Summary

Constructs a

SQLIntegrityConstraintViolationException

object.

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

.

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.

Method Summary

- Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

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

- Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Method Summary

Methods declared in class java.sql.

SQLException

getErrorCode

,

getNextException

,

getSQLState

,

iterator

,

setNextException

---

#### Methods declared in class java.sql. SQLException

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

Methods declared in interface java.lang.

Iterable

forEach

,

spliterator

---

#### Methods declared in interface java.lang. Iterable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException()
```

Constructs a

SQLIntegrityConstraintViolationException

object.
The

reason

,

SQLState

are initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason)
```

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized
to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState)
```

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor specific exception code
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
Throwable
cause)
```

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.
The

reason

is initialized to

null

if

cause==null

or to

cause.toString()

if

cause!=null

.

**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

Constructor Detail

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException()
```

Constructs a

SQLIntegrityConstraintViolationException

object.
The

reason

,

SQLState

are initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason)
```

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized
to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState)
```

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor specific exception code
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
Throwable
cause)
```

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.
The

reason

is initialized to

null

if

cause==null

or to

cause.toString()

if

cause!=null

.

**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### Constructor Detail

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException()
```

Constructs a

SQLIntegrityConstraintViolationException

object.
The

reason

,

SQLState

are initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException()

Constructs a

SQLIntegrityConstraintViolationException

object.
The

reason

,

SQLState

are initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason)
```

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized
to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason)

Constructs a

SQLIntegrityConstraintViolationException

with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized
to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState)
```

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason,

String

SQLState)

Constructs a

SQLIntegrityConstraintViolationException

object with a given

reason

and

SQLState

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor specific exception code
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

vendorCode

.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
Throwable
cause)
```

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.
The

reason

is initialized to

null

if

cause==null

or to

cause.toString()

if

cause!=null

.

**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

Throwable

cause)

Constructs an

SQLIntegrityConstraintViolationException

object with
a given

cause

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.
The

reason

is initialized to

null

if

cause==null

or to

cause.toString()

if

cause!=null

.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLIntegrityConstraintViolationException

```java
public SQLIntegrityConstraintViolationException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLIntegrityConstraintViolationException

public SQLIntegrityConstraintViolationException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLIntegrityConstraintViolationException

object
with a given

reason

,

SQLState

,

vendorCode

and

cause

.

---

