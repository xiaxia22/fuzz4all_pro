# Class SQLTransientException

**Source:** `java.sql\java\sql\SQLTransientException.html`

### Class Description

```java
public class
SQLTransientException

extends
SQLException
```

The subclass of

SQLException

is thrown in situations where a
previously failed operation might be able to succeed when the operation is
retried without any intervention by application-level functionality.

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

#### public SQLTransientException()

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
String
reason)

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
String
reason,

String
SQLState)

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
Throwable
cause)

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
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

#### public SQLTransientException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLTransientException

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

#### public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLTransientException

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

#### Class SQLTransientException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLTransientException

java.sql.SQLException

- java.sql.SQLTransientException

java.sql.SQLTransientException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

**Direct Known Subclasses:** SQLTimeoutException

,

SQLTransactionRollbackException

,

SQLTransientConnectionException

```java
public class
SQLTransientException

extends
SQLException
```

The subclass of

SQLException

is thrown in situations where a
previously failed operation might be able to succeed when the operation is
retried without any intervention by application-level functionality.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLTransientException

extends

SQLException

The subclass of

SQLException

is thrown in situations where a
previously failed operation might be able to succeed when the operation is
retried without any intervention by application-level functionality.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLTransientException

()

Constructs a

SQLTransientException

object.

SQLTransientException

​(

String

reason)

Constructs a

SQLTransientException

object
with a given

reason

.

SQLTransientException

​(

String

reason,

String

SQLState)

Constructs a

SQLTransientException

object
with a given

reason

and

SQLState

.

SQLTransientException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTransientException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientException

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

SQLTransientException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

cause

.

SQLTransientException

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

SQLTransientException

​(

Throwable

cause)

Constructs a

SQLTransientException

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

SQLTransientException

()

Constructs a

SQLTransientException

object.

SQLTransientException

​(

String

reason)

Constructs a

SQLTransientException

object
with a given

reason

.

SQLTransientException

​(

String

reason,

String

SQLState)

Constructs a

SQLTransientException

object
with a given

reason

and

SQLState

.

SQLTransientException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTransientException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientException

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

SQLTransientException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

cause

.

SQLTransientException

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

SQLTransientException

​(

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLTransientException

object.

Constructs a

SQLTransientException

object
with a given

reason

.

Constructs a

SQLTransientException

object
with a given

reason

and

SQLState

.

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLTransientException

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

SQLTransientException

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

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException()
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
Throwable
cause)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException()
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
Throwable
cause)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientException

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

- SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException()
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException()

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException​(
String
reason)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

String

reason)

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

String

reason,

String

SQLState)

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException​(
Throwable
cause)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

Throwable

cause)

Constructs a

SQLTransientException

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

SQLTransientException

```java
public SQLTransientException​(
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

#### SQLTransientException

public SQLTransientException​(

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

SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLTransientException

```java
public SQLTransientException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientException

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

#### SQLTransientException

public SQLTransientException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientException

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

