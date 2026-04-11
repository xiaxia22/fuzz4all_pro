# Class SQLTransientConnectionException

**Source:** `java.sql\java\sql\SQLTransientConnectionException.html`

### Class Description

```java
public class
SQLTransientConnectionException

extends
SQLTransientException
```

The subclass of

SQLException

for the SQLState class
value '

08

', or under vendor-specified conditions. This indicates
that the connection operation that failed might be able to succeed if
the operation is retried without any application-level changes.

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

#### public SQLTransientConnectionException()

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason,

String
SQLState)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
Throwable
cause)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason,

Throwable
cause)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLTransientConnectionException

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

#### public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLTransientConnectionException

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

#### Class SQLTransientConnectionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTransientConnectionException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTransientConnectionException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLTransientException
- - java.sql.SQLTransientConnectionException

java.sql.SQLException

- java.sql.SQLTransientException
- - java.sql.SQLTransientConnectionException

java.sql.SQLTransientException

- java.sql.SQLTransientConnectionException

java.sql.SQLTransientConnectionException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLTransientConnectionException

extends
SQLTransientException
```

The subclass of

SQLException

for the SQLState class
value '

08

', or under vendor-specified conditions. This indicates
that the connection operation that failed might be able to succeed if
the operation is retried without any application-level changes.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLTransientConnectionException

extends

SQLTransientException

The subclass of

SQLException

for the SQLState class
value '

08

', or under vendor-specified conditions. This indicates
that the connection operation that failed might be able to succeed if
the operation is retried without any application-level changes.

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

SQLTransientConnectionException

()

Constructs a

SQLTransientConnectionException

object.

SQLTransientConnectionException

​(

String

reason)

Constructs a

SQLTransientConnectionException

object
with a given

reason

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState)

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

SQLState

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

cause

.

SQLTransientConnectionException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

cause

.

SQLTransientConnectionException

​(

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

()

Constructs a

SQLTransientConnectionException

object.

SQLTransientConnectionException

​(

String

reason)

Constructs a

SQLTransientConnectionException

object
with a given

reason

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState)

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

SQLState

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLTransientConnectionException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

cause

.

SQLTransientConnectionException

​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

cause

.

SQLTransientConnectionException

​(

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLTransientConnectionException

object.

Constructs a

SQLTransientConnectionException

object
with a given

reason

.

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

SQLState

.

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLTransientConnectionException

object
with a given

reason

and

cause

.

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException()
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException()
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

- SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException()
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException()

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason,

String

SQLState)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason,

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLTransientConnectionException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLTransientConnectionException

```java
public SQLTransientConnectionException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLTransientConnectionException

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

#### SQLTransientConnectionException

public SQLTransientConnectionException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLTransientConnectionException

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

