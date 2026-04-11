# Class SQLException

**Source:** `java.sql\java\sql\SQLException.html`

### Class Description

```java
public class
SQLException

extends
Exception

implements
Iterable
<
Throwable
>
```

An exception that provides information on a database access
error or other errors.

Each

SQLException

provides several kinds of information:

- a string describing the error. This is used as the Java Exception
message, available via the method

getMessage

.

a "SQLstate" string, which follows either the XOPEN SQLstate conventions
or the SQL:2003 conventions.
The values of the SQLState string are described in the appropriate spec.
The

DatabaseMetaData

method

getSQLStateType

can be used to discover whether the driver returns the XOPEN type or
the SQL:2003 type.

an integer error code that is specific to each vendor. Normally this will
be the actual error code returned by the underlying database.

a chain to a next Exception. This can be used to provide additional
error information.

the causal relationship, if any for this

SQLException

.

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

#### public SQLException​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a

SQLException

object with a given

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

- a database vendor-specific exception code

---

#### public SQLException​(
String
reason,

String
SQLState)

Constructs a

SQLException

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

---

#### public SQLException​(
String
reason)

Constructs a

SQLException

object with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:**
- reason

- a description of the exception

---

#### public SQLException()

Constructs a

SQLException

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

#### public SQLException​(
Throwable
cause)

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLException​(
String
reason,

Throwable
cause)

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLException​(
String
reason,

String
sqlState,

Throwable
cause)

Constructs a

SQLException

object with a given

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
- sqlState

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

#### public SQLException​(
String
reason,

String
sqlState,
int vendorCode,

Throwable
cause)

Constructs a

SQLException

object with a given

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
- sqlState

- an XOPEN or SQL:2003 code identifying the exception
- vendorCode

- a database vendor-specific exception code
- cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

**Since:**
- 1.6

---

### Method Details

#### public
String
getSQLState()

Retrieves the SQLState for this

SQLException

object.

**Returns:**
- the SQLState value

---

#### public int getErrorCode()

Retrieves the vendor-specific exception code
for this

SQLException

object.

**Returns:**
- the vendor's error code

---

#### public
SQLException
getNextException()

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

**Returns:**
- the next

SQLException

object in the chain;

null

if there are none

**See Also:**
- setNextException(java.sql.SQLException)

---

#### public void setNextException​(
SQLException
ex)

Adds an

SQLException

object to the end of the chain.

**Parameters:**
- ex

- the new exception that will be added to the end of
the

SQLException

chain

**See Also:**
- getNextException()

---

#### public
Iterator
<
Throwable
> iterator()

Returns an iterator over the chained SQLExceptions. The iterator will
be used to iterate over each SQLException and its underlying cause
(if any).

**Specified by:**
- iterator

in interface

Iterable

<

Throwable

>

**Returns:**
- an iterator over the chained SQLExceptions and causes in the proper
order

**Since:**
- 1.6

---

### Additional Sections

#### Class SQLException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException

java.lang.Exception

- java.sql.SQLException

java.sql.SQLException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

**Direct Known Subclasses:** BatchUpdateException

,

RowSetWarning

,

SerialException

,

SQLClientInfoException

,

SQLNonTransientException

,

SQLRecoverableException

,

SQLTransientException

,

SQLWarning

,

SyncFactoryException

,

SyncProviderException

```java
public class
SQLException

extends
Exception

implements
Iterable
<
Throwable
>
```

An exception that provides information on a database access
error or other errors.

Each

SQLException

provides several kinds of information:

- a string describing the error. This is used as the Java Exception
message, available via the method

getMessage

.

a "SQLstate" string, which follows either the XOPEN SQLstate conventions
or the SQL:2003 conventions.
The values of the SQLState string are described in the appropriate spec.
The

DatabaseMetaData

method

getSQLStateType

can be used to discover whether the driver returns the XOPEN type or
the SQL:2003 type.

an integer error code that is specific to each vendor. Normally this will
be the actual error code returned by the underlying database.

a chain to a next Exception. This can be used to provide additional
error information.

the causal relationship, if any for this

SQLException

.

**Since:** 1.1
**See Also:** Serialized Form

public class

SQLException

extends

Exception

implements

Iterable

<

Throwable

>

An exception that provides information on a database access
error or other errors.

Each

SQLException

provides several kinds of information:

- a string describing the error. This is used as the Java Exception
message, available via the method

getMessage

.

a "SQLstate" string, which follows either the XOPEN SQLstate conventions
or the SQL:2003 conventions.
The values of the SQLState string are described in the appropriate spec.
The

DatabaseMetaData

method

getSQLStateType

can be used to discover whether the driver returns the XOPEN type or
the SQL:2003 type.

an integer error code that is specific to each vendor. Normally this will
be the actual error code returned by the underlying database.

a chain to a next Exception. This can be used to provide additional
error information.

the causal relationship, if any for this

SQLException

.

Each

SQLException

provides several kinds of information:

- a string describing the error. This is used as the Java Exception
message, available via the method

getMessage

.

a "SQLstate" string, which follows either the XOPEN SQLstate conventions
or the SQL:2003 conventions.
The values of the SQLState string are described in the appropriate spec.
The

DatabaseMetaData

method

getSQLStateType

can be used to discover whether the driver returns the XOPEN type or
the SQL:2003 type.

an integer error code that is specific to each vendor. Normally this will
be the actual error code returned by the underlying database.

a chain to a next Exception. This can be used to provide additional
error information.

the causal relationship, if any for this

SQLException

.

a string describing the error. This is used as the Java Exception
message, available via the method

getMessage

.

a "SQLstate" string, which follows either the XOPEN SQLstate conventions
or the SQL:2003 conventions.
The values of the SQLState string are described in the appropriate spec.
The

DatabaseMetaData

method

getSQLStateType

can be used to discover whether the driver returns the XOPEN type or
the SQL:2003 type.

an integer error code that is specific to each vendor. Normally this will
be the actual error code returned by the underlying database.

a chain to a next Exception. This can be used to provide additional
error information.

the causal relationship, if any for this

SQLException

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLException

()

Constructs a

SQLException

object.

SQLException

​(

String

reason)

Constructs a

SQLException

object with a given

reason

.

SQLException

​(

String

reason,

String

SQLState)

Constructs a

SQLException

object with a given

reason

and

SQLState

.

SQLException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLException

object with a given

reason

,

SQLState

and

vendorCode

.

SQLException

​(

String

reason,

String

sqlState,
int vendorCode,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

,

vendorCode

and

cause

.

SQLException

​(

String

reason,

String

sqlState,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.

SQLException

​(

String

reason,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

and

cause

.

SQLException

​(

Throwable

cause)

Constructs a

SQLException

object with a given

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

int

getErrorCode

()

Retrieves the vendor-specific exception code
for this

SQLException

object.

SQLException

getNextException

()

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

String

getSQLState

()

Retrieves the SQLState for this

SQLException

object.

Iterator

<

Throwable

>

iterator

()

Returns an iterator over the chained SQLExceptions.

void

setNextException

​(

SQLException

ex)

Adds an

SQLException

object to the end of the chain.

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

SQLException

()

Constructs a

SQLException

object.

SQLException

​(

String

reason)

Constructs a

SQLException

object with a given

reason

.

SQLException

​(

String

reason,

String

SQLState)

Constructs a

SQLException

object with a given

reason

and

SQLState

.

SQLException

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLException

object with a given

reason

,

SQLState

and

vendorCode

.

SQLException

​(

String

reason,

String

sqlState,
int vendorCode,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

,

vendorCode

and

cause

.

SQLException

​(

String

reason,

String

sqlState,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.

SQLException

​(

String

reason,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

and

cause

.

SQLException

​(

Throwable

cause)

Constructs a

SQLException

object with a given

cause

.

---

#### Constructor Summary

Constructs a

SQLException

object.

Constructs a

SQLException

object with a given

reason

.

Constructs a

SQLException

object with a given

reason

and

SQLState

.

Constructs a

SQLException

object with a given

reason

,

SQLState

and

vendorCode

.

Constructs a

SQLException

object with a given

reason

,

SQLState

,

vendorCode

and

cause

.

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.

Constructs a

SQLException

object with a given

reason

and

cause

.

Constructs a

SQLException

object with a given

cause

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getErrorCode

()

Retrieves the vendor-specific exception code
for this

SQLException

object.

SQLException

getNextException

()

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

String

getSQLState

()

Retrieves the SQLState for this

SQLException

object.

Iterator

<

Throwable

>

iterator

()

Returns an iterator over the chained SQLExceptions.

void

setNextException

​(

SQLException

ex)

Adds an

SQLException

object to the end of the chain.

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

Retrieves the vendor-specific exception code
for this

SQLException

object.

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

Retrieves the SQLState for this

SQLException

object.

Returns an iterator over the chained SQLExceptions.

Adds an

SQLException

object to the end of the chain.

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

- SQLException

```java
public SQLException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLException

object with a given

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

- a database vendor-specific exception code

- SQLException

```java
public SQLException​(
String
reason,

String
SQLState)
```

Constructs a

SQLException

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

- SQLException

```java
public SQLException​(
String
reason)
```

Constructs a

SQLException

object with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception

- SQLException

```java
public SQLException()
```

Constructs a

SQLException

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

- SQLException

```java
public SQLException​(
Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

String
sqlState,

Throwable
cause)
```

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** sqlState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

String
sqlState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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
**Parameters:** sqlState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getSQLState

```java
public
String
getSQLState()
```

Retrieves the SQLState for this

SQLException

object.

**Returns:** the SQLState value

- getErrorCode

```java
public int getErrorCode()
```

Retrieves the vendor-specific exception code
for this

SQLException

object.

**Returns:** the vendor's error code

- getNextException

```java
public
SQLException
getNextException()
```

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

**Returns:** the next

SQLException

object in the chain;

null

if there are none
**See Also:** setNextException(java.sql.SQLException)

- setNextException

```java
public void setNextException​(
SQLException
ex)
```

Adds an

SQLException

object to the end of the chain.

**Parameters:** ex

- the new exception that will be added to the end of
the

SQLException

chain
**See Also:** getNextException()

- iterator

```java
public
Iterator
<
Throwable
> iterator()
```

Returns an iterator over the chained SQLExceptions. The iterator will
be used to iterate over each SQLException and its underlying cause
(if any).

**Specified by:** iterator

in interface

Iterable

<

Throwable

>
**Returns:** an iterator over the chained SQLExceptions and causes in the proper
order
**Since:** 1.6

Constructor Detail

- SQLException

```java
public SQLException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLException

object with a given

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

- a database vendor-specific exception code

- SQLException

```java
public SQLException​(
String
reason,

String
SQLState)
```

Constructs a

SQLException

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

- SQLException

```java
public SQLException​(
String
reason)
```

Constructs a

SQLException

object with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception

- SQLException

```java
public SQLException()
```

Constructs a

SQLException

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

- SQLException

```java
public SQLException​(
Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

String
sqlState,

Throwable
cause)
```

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** sqlState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLException

```java
public SQLException​(
String
reason,

String
sqlState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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
**Parameters:** sqlState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### Constructor Detail

SQLException

```java
public SQLException​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a

SQLException

object with a given

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

- a database vendor-specific exception code

---

#### SQLException

public SQLException​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a

SQLException

object with a given

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

SQLException

```java
public SQLException​(
String
reason,

String
SQLState)
```

Constructs a

SQLException

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

---

#### SQLException

public SQLException​(

String

reason,

String

SQLState)

Constructs a

SQLException

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

SQLException

```java
public SQLException​(
String
reason)
```

Constructs a

SQLException

object with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** reason

- a description of the exception

---

#### SQLException

public SQLException​(

String

reason)

Constructs a

SQLException

object with a given

reason

. The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLException

```java
public SQLException()
```

Constructs a

SQLException

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

#### SQLException

public SQLException()

Constructs a

SQLException

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

SQLException

```java
public SQLException​(
Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLException

public SQLException​(

Throwable

cause)

Constructs a

SQLException

object with a given

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

SQLException

```java
public SQLException​(
String
reason,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLException

public SQLException​(

String

reason,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

and

cause

.
The

SQLState

is initialized to

null

and the vendor code is initialized to 0.

SQLException

```java
public SQLException​(
String
reason,

String
sqlState,

Throwable
cause)
```

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception.
**Parameters:** sqlState

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

#### SQLException

public SQLException​(

String

reason,

String

sqlState,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

and

cause

.
The vendor code is initialized to 0.

SQLException

```java
public SQLException​(
String
reason,

String
sqlState,
int vendorCode,

Throwable
cause)
```

Constructs a

SQLException

object with a given

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
**Parameters:** sqlState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLException

public SQLException​(

String

reason,

String

sqlState,
int vendorCode,

Throwable

cause)

Constructs a

SQLException

object with a given

reason

,

SQLState

,

vendorCode

and

cause

.

Method Detail

- getSQLState

```java
public
String
getSQLState()
```

Retrieves the SQLState for this

SQLException

object.

**Returns:** the SQLState value

- getErrorCode

```java
public int getErrorCode()
```

Retrieves the vendor-specific exception code
for this

SQLException

object.

**Returns:** the vendor's error code

- getNextException

```java
public
SQLException
getNextException()
```

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

**Returns:** the next

SQLException

object in the chain;

null

if there are none
**See Also:** setNextException(java.sql.SQLException)

- setNextException

```java
public void setNextException​(
SQLException
ex)
```

Adds an

SQLException

object to the end of the chain.

**Parameters:** ex

- the new exception that will be added to the end of
the

SQLException

chain
**See Also:** getNextException()

- iterator

```java
public
Iterator
<
Throwable
> iterator()
```

Returns an iterator over the chained SQLExceptions. The iterator will
be used to iterate over each SQLException and its underlying cause
(if any).

**Specified by:** iterator

in interface

Iterable

<

Throwable

>
**Returns:** an iterator over the chained SQLExceptions and causes in the proper
order
**Since:** 1.6

---

#### Method Detail

getSQLState

```java
public
String
getSQLState()
```

Retrieves the SQLState for this

SQLException

object.

**Returns:** the SQLState value

---

#### getSQLState

public

String

getSQLState()

Retrieves the SQLState for this

SQLException

object.

getErrorCode

```java
public int getErrorCode()
```

Retrieves the vendor-specific exception code
for this

SQLException

object.

**Returns:** the vendor's error code

---

#### getErrorCode

public int getErrorCode()

Retrieves the vendor-specific exception code
for this

SQLException

object.

getNextException

```java
public
SQLException
getNextException()
```

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

**Returns:** the next

SQLException

object in the chain;

null

if there are none
**See Also:** setNextException(java.sql.SQLException)

---

#### getNextException

public

SQLException

getNextException()

Retrieves the exception chained to this

SQLException

object by setNextException(SQLException ex).

setNextException

```java
public void setNextException​(
SQLException
ex)
```

Adds an

SQLException

object to the end of the chain.

**Parameters:** ex

- the new exception that will be added to the end of
the

SQLException

chain
**See Also:** getNextException()

---

#### setNextException

public void setNextException​(

SQLException

ex)

Adds an

SQLException

object to the end of the chain.

iterator

```java
public
Iterator
<
Throwable
> iterator()
```

Returns an iterator over the chained SQLExceptions. The iterator will
be used to iterate over each SQLException and its underlying cause
(if any).

**Specified by:** iterator

in interface

Iterable

<

Throwable

>
**Returns:** an iterator over the chained SQLExceptions and causes in the proper
order
**Since:** 1.6

---

#### iterator

public

Iterator

<

Throwable

> iterator()

Returns an iterator over the chained SQLExceptions. The iterator will
be used to iterate over each SQLException and its underlying cause
(if any).

---

