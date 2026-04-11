# Class SQLNonTransientException

**Source:** `java.sql\java\sql\SQLNonTransientException.html`

### Class Description

```java
public class
SQLNonTransientException

extends
SQLException
```

The subclass of

SQLException

thrown when an instance where a retry
of the same operation would fail unless the cause of the

SQLException

is corrected.

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

#### public SQLNonTransientException()

Constructs a

SQLNonTransientException

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

#### public SQLNonTransientException​(
String
reason)

Constructs a

SQLNonTransientException

object
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

#### public SQLNonTransientException​(
String
reason,

String
SQLState)

Constructs a

SQLNonTransientException

object
with a given

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

#### public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLNonTransientException

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

#### public SQLNonTransientException​(
Throwable
cause)

Constructs a

SQLNonTransientException

object
with a given

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

#### public SQLNonTransientException​(
String
reason,

Throwable
cause)

Constructs a

SQLTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLNonTransientException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLNonTransientException

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

#### public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLNonTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SQLNonTransientException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLNonTransientException

java.sql.SQLException

- java.sql.SQLNonTransientException

java.sql.SQLNonTransientException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

**Direct Known Subclasses:** SQLDataException

,

SQLFeatureNotSupportedException

,

SQLIntegrityConstraintViolationException

,

SQLInvalidAuthorizationSpecException

,

SQLNonTransientConnectionException

,

SQLSyntaxErrorException

```java
public class
SQLNonTransientException

extends
SQLException
```

The subclass of

SQLException

thrown when an instance where a retry
of the same operation would fail unless the cause of the

SQLException

is corrected.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLNonTransientException

extends

SQLException

The subclass of

SQLException

thrown when an instance where a retry
of the same operation would fail unless the cause of the

SQLException

is corrected.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLNonTransientException

()

Constructs a

SQLNonTransientException

object.

SQLNonTransientException

​(

String

reason)

Constructs a

SQLNonTransientException

object
with a given

reason

.

SQLNonTransientException

​(

String

reason,

String

SQLState)

Constructs a

SQLNonTransientException

object
with a given

reason

and

SQLState

.

SQLNonTransientException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLNonTransientException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLNonTransientException

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

SQLNonTransientException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

cause

.

SQLNonTransientException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

reason

and

cause

.

SQLNonTransientException

​(

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

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

SQLNonTransientException

()

Constructs a

SQLNonTransientException

object.

SQLNonTransientException

​(

String

reason)

Constructs a

SQLNonTransientException

object
with a given

reason

.

SQLNonTransientException

​(

String

reason,

String

SQLState)

Constructs a

SQLNonTransientException

object
with a given

reason

and

SQLState

.

SQLNonTransientException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLNonTransientException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLNonTransientException

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

SQLNonTransientException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

cause

.

SQLNonTransientException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

reason

and

cause

.

SQLNonTransientException

​(

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLNonTransientException

object.

Constructs a

SQLNonTransientException

object
with a given

reason

.

Constructs a

SQLNonTransientException

object
with a given

reason

and

SQLState

.

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLNonTransientException

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

SQLNonTransientException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLTransientException

object
with a given

reason

and

cause

.

Constructs a

SQLNonTransientException

object
with a given

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

- SQLNonTransientException

```java
public SQLNonTransientException()
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason)
```

Constructs a

SQLNonTransientException

object
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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLNonTransientException

object
with a given

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
Throwable
cause)
```

Constructs a

SQLNonTransientException

object
with a given

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

Constructor Detail

- SQLNonTransientException

```java
public SQLNonTransientException()
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason)
```

Constructs a

SQLNonTransientException

object
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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLNonTransientException

object
with a given

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
Throwable
cause)
```

Constructs a

SQLNonTransientException

object
with a given

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

- SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### Constructor Detail

SQLNonTransientException

```java
public SQLNonTransientException()
```

Constructs a

SQLNonTransientException

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

#### SQLNonTransientException

public SQLNonTransientException()

Constructs a

SQLNonTransientException

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

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason)
```

Constructs a

SQLNonTransientException

object
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

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason)

Constructs a

SQLNonTransientException

object
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

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLNonTransientException

object
with a given

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

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason,

String

SQLState)

Constructs a

SQLNonTransientException

object
with a given

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

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLNonTransientException

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

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLNonTransientException

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

SQLNonTransientException

```java
public SQLNonTransientException​(
Throwable
cause)
```

Constructs a

SQLNonTransientException

object
with a given

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

#### SQLNonTransientException

public SQLNonTransientException​(

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

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

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientException

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

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLNonTransientException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLNonTransientException

```java
public SQLNonTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLNonTransientException

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

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLNonTransientException

public SQLNonTransientException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLNonTransientException

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

