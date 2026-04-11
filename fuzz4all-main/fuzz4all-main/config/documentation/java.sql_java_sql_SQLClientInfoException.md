# Class SQLClientInfoException

**Source:** `java.sql\java\sql\SQLClientInfoException.html`

### Class Description

```java
public class
SQLClientInfoException

extends
SQLException
```

The subclass of

SQLException

is thrown when one or more client info properties
could not be set on a

Connection

. In addition to the information provided
by

SQLException

, a

SQLClientInfoException

provides a list of client info
properties that were not set.

Some databases do not allow multiple client info properties to be set
atomically. For those databases, it is possible that some of the client
info properties had been set even though the

Connection.setClientInfo

method threw an exception. An application can use the

getFailedProperties

method to retrieve a list of client info properties that were not set. The
properties are identified by passing a

Map<String,ClientInfoStatus>

to
the appropriate

SQLClientInfoException

constructor.

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

#### public SQLClientInfoException()

Constructs a

SQLClientInfoException

Object.
The

reason

,

SQLState

, and failedProperties list are initialized to

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

#### public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.
The

reason

and

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

**Parameters:**
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus

**Since:**
- 1.6

---

#### public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

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

and the vendor code is initialized to 0.

**Parameters:**
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
- cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.

**Since:**
- 1.6

---

#### public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.
The

SQLState

is initialized
to

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
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus

**Since:**
- 1.6

---

#### public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

**Parameters:**
- reason

- a description of the exception
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
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

#### public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

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
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus

**Since:**
- 1.6

---

#### public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

. The vendor code is initialized to 0.

**Parameters:**
- reason

- a description of the exception
- SQLState

- an XOPEN or SQL:2003 code identifying the exception
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
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

#### public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

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
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus

**Since:**
- 1.6

---

#### public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

**Parameters:**
- reason

- a description of the exception
- SQLState

- an XOPEN or SQL:2003 code identifying the exception
- vendorCode

- a database vendor-specific exception code
- failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
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

#### public
Map
<
String
,​
ClientInfoStatus
> getFailedProperties()

Returns the list of client info properties that could not be set. The
keys in the Map contain the names of the client info
properties that could not be set and the values contain one of the
reason codes defined in

ClientInfoStatus

**Returns:**
- Map list containing the client info properties that could
not be set

**Since:**
- 1.6

---

### Additional Sections

#### Class SQLClientInfoException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLClientInfoException

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLClientInfoException

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLClientInfoException

java.sql.SQLException

- java.sql.SQLClientInfoException

java.sql.SQLClientInfoException

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
SQLClientInfoException

extends
SQLException
```

The subclass of

SQLException

is thrown when one or more client info properties
could not be set on a

Connection

. In addition to the information provided
by

SQLException

, a

SQLClientInfoException

provides a list of client info
properties that were not set.

Some databases do not allow multiple client info properties to be set
atomically. For those databases, it is possible that some of the client
info properties had been set even though the

Connection.setClientInfo

method threw an exception. An application can use the

getFailedProperties

method to retrieve a list of client info properties that were not set. The
properties are identified by passing a

Map<String,ClientInfoStatus>

to
the appropriate

SQLClientInfoException

constructor.

**Since:** 1.6
**See Also:** ClientInfoStatus

,

Connection.setClientInfo(java.lang.String, java.lang.String)

,

Serialized Form

public class

SQLClientInfoException

extends

SQLException

The subclass of

SQLException

is thrown when one or more client info properties
could not be set on a

Connection

. In addition to the information provided
by

SQLException

, a

SQLClientInfoException

provides a list of client info
properties that were not set.

Some databases do not allow multiple client info properties to be set
atomically. For those databases, it is possible that some of the client
info properties had been set even though the

Connection.setClientInfo

method threw an exception. An application can use the

getFailedProperties

method to retrieve a list of client info properties that were not set. The
properties are identified by passing a

Map<String,ClientInfoStatus>

to
the appropriate

SQLClientInfoException

constructor.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLClientInfoException

()

Constructs a

SQLClientInfoException

Object.

SQLClientInfoException

​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.

SQLClientInfoException

​(

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.

SQLClientInfoException

​(

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

ClientInfoStatus

>

getFailedProperties

()

Returns the list of client info properties that could not be set.

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

SQLClientInfoException

()

Constructs a

SQLClientInfoException

Object.

SQLClientInfoException

​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.

SQLClientInfoException

​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.

SQLClientInfoException

​(

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.

SQLClientInfoException

​(

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

---

#### Constructor Summary

Constructs a

SQLClientInfoException

Object.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Map

<

String

,​

ClientInfoStatus

>

getFailedProperties

()

Returns the list of client info properties that could not be set.

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

Returns the list of client info properties that could not be set.

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

- SQLClientInfoException

```java
public SQLClientInfoException()
```

Constructs a

SQLClientInfoException

Object.
The

reason

,

SQLState

, and failedProperties list are initialized to

null

and the vendor code is initialized to 0.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.
The

reason

and

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

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

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

and the vendor code is initialized to 0.

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.
The

SQLState

is initialized
to

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

. The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getFailedProperties

```java
public
Map
<
String
,​
ClientInfoStatus
> getFailedProperties()
```

Returns the list of client info properties that could not be set. The
keys in the Map contain the names of the client info
properties that could not be set and the values contain one of the
reason codes defined in

ClientInfoStatus

**Returns:** Map list containing the client info properties that could
not be set
**Since:** 1.6

Constructor Detail

- SQLClientInfoException

```java
public SQLClientInfoException()
```

Constructs a

SQLClientInfoException

Object.
The

reason

,

SQLState

, and failedProperties list are initialized to

null

and the vendor code is initialized to 0.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.
The

reason

and

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

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

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

and the vendor code is initialized to 0.

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.
The

SQLState

is initialized
to

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

. The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

- SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
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

SQLClientInfoException

```java
public SQLClientInfoException()
```

Constructs a

SQLClientInfoException

Object.
The

reason

,

SQLState

, and failedProperties list are initialized to

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

#### SQLClientInfoException

public SQLClientInfoException()

Constructs a

SQLClientInfoException

Object.
The

reason

,

SQLState

, and failedProperties list are initialized to

null

and the vendor code is initialized to 0.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.
The

reason

and

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

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

failedProperties

.
The

reason

and

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

SQLClientInfoException

```java
public SQLClientInfoException​(
Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

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

and the vendor code is initialized to 0.

**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the (which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with
a given

cause

and

failedProperties

.

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

and the vendor code is initialized to 0.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.
The

SQLState

is initialized
to

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

cause

and

failedProperties

.
The

SQLState

is initialized
to

null

and the vendor code is initialized to 0.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

and

failedProperties

.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method. The vendor code
is initialized to 0.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

. The vendor code is initialized to 0.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

String

SQLState,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

and

failedProperties

. The vendor code is initialized to 0.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

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
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

vendorCode

and

failedProperties

.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

SQLClientInfoException

```java
public SQLClientInfoException​(
String
reason,

String
SQLState,
int vendorCode,

Map
<
String
,​
ClientInfoStatus
> failedProperties,

Throwable
cause)
```

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

**Parameters:** reason

- a description of the exception
**Parameters:** SQLState

- an XOPEN or SQL:2003 code identifying the exception
**Parameters:** vendorCode

- a database vendor-specific exception code
**Parameters:** failedProperties

- A Map containing the property values that could not
be set. The keys in the Map
contain the names of the client info
properties that could not be set and
the values contain one of the reason codes
defined in

ClientInfoStatus
**Parameters:** cause

- the underlying reason for this

SQLException

(which is saved for later retrieval by the

getCause()

method); may be null indicating
the cause is non-existent or unknown.
**Since:** 1.6

---

#### SQLClientInfoException

public SQLClientInfoException​(

String

reason,

String

SQLState,
int vendorCode,

Map

<

String

,​

ClientInfoStatus

> failedProperties,

Throwable

cause)

Constructs a

SQLClientInfoException

object initialized with a
given

reason

,

SQLState

,

cause

,

vendorCode

and

failedProperties

.

Method Detail

- getFailedProperties

```java
public
Map
<
String
,​
ClientInfoStatus
> getFailedProperties()
```

Returns the list of client info properties that could not be set. The
keys in the Map contain the names of the client info
properties that could not be set and the values contain one of the
reason codes defined in

ClientInfoStatus

**Returns:** Map list containing the client info properties that could
not be set
**Since:** 1.6

---

#### Method Detail

getFailedProperties

```java
public
Map
<
String
,​
ClientInfoStatus
> getFailedProperties()
```

Returns the list of client info properties that could not be set. The
keys in the Map contain the names of the client info
properties that could not be set and the values contain one of the
reason codes defined in

ClientInfoStatus

**Returns:** Map list containing the client info properties that could
not be set
**Since:** 1.6

---

#### getFailedProperties

public

Map

<

String

,​

ClientInfoStatus

> getFailedProperties()

Returns the list of client info properties that could not be set. The
keys in the Map contain the names of the client info
properties that could not be set and the values contain one of the
reason codes defined in

ClientInfoStatus

---

