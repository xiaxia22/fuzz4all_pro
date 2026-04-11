# Class SQLTimeoutException

**Source:** `java.sql\java\sql\SQLTimeoutException.html`

### Class Description

```java
public class
SQLTimeoutException

extends
SQLTransientException
```

The subclass of

SQLException

thrown when the timeout specified by

Statement.setQueryTimeout

,

DriverManager.setLoginTimeout

,

DataSource.setLoginTimeout

,

XADataSource.setLoginTimeout

has expired.

This exception does not correspond to a standard SQLState.

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

#### public SQLTimeoutException()

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason,

String
SQLState)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
Throwable
cause)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason,

Throwable
cause)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLTimeoutException

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

#### public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLTimeoutException

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

#### Class SQLTimeoutException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTimeoutException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTimeoutException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTimeoutException

java.sql.SQLException

- java.sql.SQLTransientException
- - java.sql.SQLTimeoutException

java.sql.SQLTransientException

- java.sql.SQLTimeoutException

java.sql.SQLTimeoutException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLTimeoutException

extends
SQLTransientException
```

The subclass of

SQLException

thrown when the timeout specified by

Statement.setQueryTimeout

,

DriverManager.setLoginTimeout

,

DataSource.setLoginTimeout

,

XADataSource.setLoginTimeout

has expired.

This exception does not correspond to a standard SQLState.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLTimeoutException

extends

SQLTransientException

The subclass of

SQLException

thrown when the timeout specified by

Statement.setQueryTimeout

,

DriverManager.setLoginTimeout

,

DataSource.setLoginTimeout

,

XADataSource.setLoginTimeout

has expired.

This exception does not correspond to a standard SQLState.

This exception does not correspond to a standard SQLState.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLTimeoutException

()

Constructs a

SQLTimeoutException

object.

SQLTimeoutException

​(

String

reason)

Constructs a

SQLTimeoutException

object
with a given

reason

.

SQLTimeoutException

​(

String

reason,

String

SQLState)

Constructs a

SQLTimeoutException

object
with a given

reason

and

SQLState

.

SQLTimeoutException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTimeoutException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

cause

.

SQLTimeoutException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

reason

and

cause

.

SQLTimeoutException

​(

Throwable

cause)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

()

Constructs a

SQLTimeoutException

object.

SQLTimeoutException

​(

String

reason)

Constructs a

SQLTimeoutException

object
with a given

reason

.

SQLTimeoutException

​(

String

reason,

String

SQLState)

Constructs a

SQLTimeoutException

object
with a given

reason

and

SQLState

.

SQLTimeoutException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTimeoutException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

cause

.

SQLTimeoutException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

reason

and

cause

.

SQLTimeoutException

​(

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLTimeoutException

object.

Constructs a

SQLTimeoutException

object
with a given

reason

.

Constructs a

SQLTimeoutException

object
with a given

reason

and

SQLState

.

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLTimeoutException

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

SQLTimeoutException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLTimeoutException

object
with a given

reason

and

cause

.

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException()
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException()
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

- SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException()
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException()

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason,

String

SQLState)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
Throwable
cause)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

Throwable

cause)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason,

Throwable

cause)

Constructs a

SQLTimeoutException

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

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTimeoutException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLTimeoutException

```java
public SQLTimeoutException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTimeoutException

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

#### SQLTimeoutException

public SQLTimeoutException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTimeoutException

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

