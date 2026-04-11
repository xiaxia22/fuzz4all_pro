# Class SQLWarning

**Source:** `java.sql\java\sql\SQLWarning.html`

### Class Description

```java
public class
SQLWarning

extends
SQLException
```

An exception that provides information on database access
warnings. Warnings are silently chained to the object whose method
caused it to be reported.

Warnings may be retrieved from

Connection

,

Statement

,
and

ResultSet

objects. Trying to retrieve a warning on a
connection after it has been closed will cause an exception to be thrown.
Similarly, trying to retrieve a warning on a statement after it has been
closed or on a result set after it has been closed will cause
an exception to be thrown. Note that closing a statement also
closes a result set that it might have produced.

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

#### public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLWarning

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

- a description of the warning
- SQLState

- an XOPEN or SQL:2003 code identifying the warning
- vendorCode

- a database vendor-specific warning code

---

#### public SQLWarning​(
String
reason,

String
SQLState)

Constructs a

SQLWarning

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

- a description of the warning
- SQLState

- an XOPEN or SQL:2003 code identifying the warning

---

#### public SQLWarning​(
String
reason)

Constructs a

SQLWarning

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

- a description of the warning

---

#### public SQLWarning()

Constructs a

SQLWarning

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

---

#### public SQLWarning​(
Throwable
cause)

Constructs a

SQLWarning

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

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### public SQLWarning​(
String
reason,

Throwable
cause)

Constructs a

SQLWarning

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

- a description of the warning
- cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

---

#### public SQLWarning​(
String
reason,

String
SQLState,

Throwable
cause)

Constructs a

SQLWarning

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

- a description of the warning
- SQLState

- an XOPEN or SQL:2003 code identifying the warning
- cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)

Constructs a

SQLWarning

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

- a description of the warning
- SQLState

- an XOPEN or SQL:2003 code identifying the warning
- vendorCode

- a database vendor-specific warning code
- cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

### Method Details

#### public
SQLWarning
getNextWarning()

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

**Returns:**
- the next

SQLException

in the chain;

null

if none

**See Also:**
- setNextWarning(java.sql.SQLWarning)

---

#### public void setNextWarning​(
SQLWarning
w)

Adds a

SQLWarning

object to the end of the chain.

**Parameters:**
- w

- the new end of the

SQLException

chain

**See Also:**
- getNextWarning()

---

### Additional Sections

#### Class SQLWarning

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLWarning

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLWarning

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLWarning

java.sql.SQLException

- java.sql.SQLWarning

java.sql.SQLWarning

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

**Direct Known Subclasses:** DataTruncation

```java
public class
SQLWarning

extends
SQLException
```

An exception that provides information on database access
warnings. Warnings are silently chained to the object whose method
caused it to be reported.

Warnings may be retrieved from

Connection

,

Statement

,
and

ResultSet

objects. Trying to retrieve a warning on a
connection after it has been closed will cause an exception to be thrown.
Similarly, trying to retrieve a warning on a statement after it has been
closed or on a result set after it has been closed will cause
an exception to be thrown. Note that closing a statement also
closes a result set that it might have produced.

**Since:** 1.1
**See Also:** Connection.getWarnings()

,

Statement.getWarnings()

,

ResultSet.getWarnings()

,

Serialized Form

public class

SQLWarning

extends

SQLException

An exception that provides information on database access
warnings. Warnings are silently chained to the object whose method
caused it to be reported.

Warnings may be retrieved from

Connection

,

Statement

,
and

ResultSet

objects. Trying to retrieve a warning on a
connection after it has been closed will cause an exception to be thrown.
Similarly, trying to retrieve a warning on a statement after it has been
closed or on a result set after it has been closed will cause
an exception to be thrown. Note that closing a statement also
closes a result set that it might have produced.

Warnings may be retrieved from

Connection

,

Statement

,
and

ResultSet

objects. Trying to retrieve a warning on a
connection after it has been closed will cause an exception to be thrown.
Similarly, trying to retrieve a warning on a statement after it has been
closed or on a result set after it has been closed will cause
an exception to be thrown. Note that closing a statement also
closes a result set that it might have produced.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLWarning

()

Constructs a

SQLWarning

object.

SQLWarning

​(

String

reason)

Constructs a

SQLWarning

object
with a given

reason

.

SQLWarning

​(

String

reason,

String

SQLState)

Constructs a

SQLWarning

object
with a given

reason

and

SQLState

.

SQLWarning

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLWarning

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLWarning

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

SQLWarning

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

cause

.

SQLWarning

​(

String

reason,

Throwable

cause)

Constructs a

SQLWarning

object
with a given

reason

and

cause

.

SQLWarning

​(

Throwable

cause)

Constructs a

SQLWarning

object
with a given

cause

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SQLWarning

getNextWarning

()

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

void

setNextWarning

​(

SQLWarning

w)

Adds a

SQLWarning

object to the end of the chain.

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

SQLWarning

()

Constructs a

SQLWarning

object.

SQLWarning

​(

String

reason)

Constructs a

SQLWarning

object
with a given

reason

.

SQLWarning

​(

String

reason,

String

SQLState)

Constructs a

SQLWarning

object
with a given

reason

and

SQLState

.

SQLWarning

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

vendorCode

.

SQLWarning

​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLWarning

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

SQLWarning

​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

cause

.

SQLWarning

​(

String

reason,

Throwable

cause)

Constructs a

SQLWarning

object
with a given

reason

and

cause

.

SQLWarning

​(

Throwable

cause)

Constructs a

SQLWarning

object
with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLWarning

object.

Constructs a

SQLWarning

object
with a given

reason

.

Constructs a

SQLWarning

object
with a given

reason

and

SQLState

.

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLWarning

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

SQLWarning

object
with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLWarning

object
with a given

reason

and

cause

.

Constructs a

SQLWarning

object
with a given

cause

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

SQLWarning

getNextWarning

()

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

void

setNextWarning

​(

SQLWarning

w)

Adds a

SQLWarning

object to the end of the chain.

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

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

Adds a

SQLWarning

object to the end of the chain.

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

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning

- SQLWarning

```java
public SQLWarning​(
String
reason)
```

Constructs a

SQLWarning

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

- a description of the warning

- SQLWarning

```java
public SQLWarning()
```

Constructs a

SQLWarning

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

- SQLWarning

```java
public SQLWarning​(
Throwable
cause)
```

Constructs a

SQLWarning

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

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

============ METHOD DETAIL ==========

- Method Detail

- getNextWarning

```java
public
SQLWarning
getNextWarning()
```

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

**Returns:** the next

SQLException

in the chain;

null

if none
**See Also:** setNextWarning(java.sql.SQLWarning)

- setNextWarning

```java
public void setNextWarning​(
SQLWarning
w)
```

Adds a

SQLWarning

object to the end of the chain.

**Parameters:** w

- the new end of the

SQLException

chain
**See Also:** getNextWarning()

Constructor Detail

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning

- SQLWarning

```java
public SQLWarning​(
String
reason)
```

Constructs a

SQLWarning

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

- a description of the warning

- SQLWarning

```java
public SQLWarning()
```

Constructs a

SQLWarning

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

- SQLWarning

```java
public SQLWarning​(
Throwable
cause)
```

Constructs a

SQLWarning

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

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

- SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### Constructor Detail

SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code

---

#### SQLWarning

public SQLWarning​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning

---

#### SQLWarning

public SQLWarning​(

String

reason,

String

SQLState)

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning​(
String
reason)
```

Constructs a

SQLWarning

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

- a description of the warning

---

#### SQLWarning

public SQLWarning​(

String

reason)

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning()
```

Constructs a

SQLWarning

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

---

#### SQLWarning

public SQLWarning()

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning​(
Throwable
cause)
```

Constructs a

SQLWarning

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

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### SQLWarning

public SQLWarning​(

Throwable

cause)

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning​(
String
reason,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

---

#### SQLWarning

public SQLWarning​(

String

reason,

Throwable

cause)

Constructs a

SQLWarning

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

SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### SQLWarning

public SQLWarning​(

String

reason,

String

SQLState,

Throwable

cause)

Constructs a

SQLWarning

object
with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLWarning

```java
public SQLWarning​(
String
reason,

String
SQLState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLWarning

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

- a description of the warning
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the warning
**Parameters:** vendorCode

- a database vendor-specific warning code
**Parameters:** cause

- the underlying reason for this

SQLWarning

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

---

#### SQLWarning

public SQLWarning​(

String

reason,

String

SQLState,
int vendorCode,

Throwable

cause)

Constructs a

SQLWarning

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

Method Detail

- getNextWarning

```java
public
SQLWarning
getNextWarning()
```

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

**Returns:** the next

SQLException

in the chain;

null

if none
**See Also:** setNextWarning(java.sql.SQLWarning)

- setNextWarning

```java
public void setNextWarning​(
SQLWarning
w)
```

Adds a

SQLWarning

object to the end of the chain.

**Parameters:** w

- the new end of the

SQLException

chain
**See Also:** getNextWarning()

---

#### Method Detail

getNextWarning

```java
public
SQLWarning
getNextWarning()
```

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

**Returns:** the next

SQLException

in the chain;

null

if none
**See Also:** setNextWarning(java.sql.SQLWarning)

---

#### getNextWarning

public

SQLWarning

getNextWarning()

Retrieves the warning chained to this

SQLWarning

object by

setNextWarning

.

setNextWarning

```java
public void setNextWarning​(
SQLWarning
w)
```

Adds a

SQLWarning

object to the end of the chain.

**Parameters:** w

- the new end of the

SQLException

chain
**See Also:** getNextWarning()

---

#### setNextWarning

public void setNextWarning​(

SQLWarning

w)

Adds a

SQLWarning

object to the end of the chain.

---

