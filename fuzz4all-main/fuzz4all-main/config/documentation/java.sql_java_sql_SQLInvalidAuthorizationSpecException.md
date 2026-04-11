# Class SQLInvalidAuthorizationSpecException

**Source:** `java.sql\java\sql\SQLInvalidAuthorizationSpecException.html`

### Class Description

```java
public class
SQLInvalidAuthorizationSpecException

extends
SQLNonTransientException
```

The subclass of

SQLException

thrown when the SQLState class value
is '

28

', or under vendor-specified conditions. This indicates that
the authorization credentials presented during connection establishment
are not valid.

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

#### public SQLInvalidAuthorizationSpecException()

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
Throwable
cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason,

Throwable
cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

#### Class SQLInvalidAuthorizationSpecException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLInvalidAuthorizationSpecException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLInvalidAuthorizationSpecException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLNonTransientException
- - java.sql.SQLInvalidAuthorizationSpecException

java.sql.SQLException

- java.sql.SQLNonTransientException
- - java.sql.SQLInvalidAuthorizationSpecException

java.sql.SQLNonTransientException

- java.sql.SQLInvalidAuthorizationSpecException

java.sql.SQLInvalidAuthorizationSpecException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLInvalidAuthorizationSpecException

extends
SQLNonTransientException
```

The subclass of

SQLException

thrown when the SQLState class value
is '

28

', or under vendor-specified conditions. This indicates that
the authorization credentials presented during connection establishment
are not valid.

Please consult your driver vendor documentation for the vendor-specified
conditions for which this

Exception

may be thrown.

**Since:** 1.6
**See Also:** Serialized Form

public class

SQLInvalidAuthorizationSpecException

extends

SQLNonTransientException

The subclass of

SQLException

thrown when the SQLState class value
is '

28

', or under vendor-specified conditions. This indicates that
the authorization credentials presented during connection establishment
are not valid.

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

SQLInvalidAuthorizationSpecException

()

Constructs a

SQLInvalidAuthorizationSpecException

object.

SQLInvalidAuthorizationSpecException

​(

String

reason)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

SQLState

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

cause

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

cause

.

SQLInvalidAuthorizationSpecException

​(

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

()

Constructs a

SQLInvalidAuthorizationSpecException

object.

SQLInvalidAuthorizationSpecException

​(

String

reason)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

SQLState

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

cause

.

SQLInvalidAuthorizationSpecException

​(

String

reason,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

cause

.

SQLInvalidAuthorizationSpecException

​(

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLInvalidAuthorizationSpecException

object.

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

.

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

SQLState

.

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

and

cause

.

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException()
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException()
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

- SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException()
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException()

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason,

String

SQLState)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLInvalidAuthorizationSpecException

```java
public SQLInvalidAuthorizationSpecException​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLInvalidAuthorizationSpecException

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

#### SQLInvalidAuthorizationSpecException

public SQLInvalidAuthorizationSpecException​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLInvalidAuthorizationSpecException

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

