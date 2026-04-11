# Class SQLRecoverableException

**Source:** `java.sql\java\sql\SQLRecoverableException.html`

### Class Description

```java
public class
SQLRecoverableException

extends
SQLException
```

The subclass of

SQLException

thrown in situations where a
previously failed operation might be able to succeed if the application performs
some recovery steps and retries the entire transaction or in the case of a
distributed transaction, the transaction branch. At a minimum,
the recovery operation must include closing the current connection and getting
a new connection.

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

#### public SQLRecoverableException()

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason,

String
SQLState)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
Throwable
cause)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason,

Throwable
cause)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLRecoverableException

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

#### public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLRecoverableException

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

#### Class SQLRecoverableException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLRecoverableException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLRecoverableException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLRecoverableException

java.sql.SQLException

- java.sql.SQLRecoverableException

java.sql.SQLRecoverableException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLRecoverableException

extends
SQLException
```

The subclass of

SQLException

thrown in situations where a
previously failed operation might be able to succeed if the application performs
some recovery steps and retries the entire transaction or in the case of a
distributed transaction, the transaction branch. At a minimum,
the recovery operation must include closing the current connection and getting
a new connection.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLRecoverableException

extends

SQLException

The subclass of

SQLException

thrown in situations where a
previously failed operation might be able to succeed if the application performs
some recovery steps and retries the entire transaction or in the case of a
distributed transaction, the transaction branch. At a minimum,
the recovery operation must include closing the current connection and getting
a new connection.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLRecoverableException

()

Constructs a

SQLRecoverableException

object.

SQLRecoverableException

​(

String

reason)

Constructs a

SQLRecoverableException

object
with a given

reason

.

SQLRecoverableException

​(

String

reason,

String

SQLState)

Constructs a

SQLRecoverableException

object
with a given

reason

and

SQLState

.

SQLRecoverableException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLRecoverableException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

cause

.

SQLRecoverableException

​(

String

reason,

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

reason

and

cause

.

SQLRecoverableException

​(

Throwable

cause)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

()

Constructs a

SQLRecoverableException

object.

SQLRecoverableException

​(

String

reason)

Constructs a

SQLRecoverableException

object
with a given

reason

.

SQLRecoverableException

​(

String

reason,

String

SQLState)

Constructs a

SQLRecoverableException

object
with a given

reason

and

SQLState

.

SQLRecoverableException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLRecoverableException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

cause

.

SQLRecoverableException

​(

String

reason,

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

reason

and

cause

.

SQLRecoverableException

​(

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLRecoverableException

object.

Constructs a

SQLRecoverableException

object
with a given

reason

.

Constructs a

SQLRecoverableException

object
with a given

reason

and

SQLState

.

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLRecoverableException

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

SQLRecoverableException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLRecoverableException

object
with a given

reason

and

cause

.

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException()
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException()
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

- SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException()
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException()

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason,

String

SQLState)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
Throwable
cause)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

Throwable

cause)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason,

Throwable

cause)

Constructs a

SQLRecoverableException

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

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLRecoverableException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLRecoverableException

```java
public SQLRecoverableException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLRecoverableException

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

#### SQLRecoverableException

public SQLRecoverableException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLRecoverableException

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

