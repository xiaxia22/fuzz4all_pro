# Class RowSetWarning

**Source:** `java.sql.rowset\javax\sql\rowset\RowSetWarning.html`

### Class Description

```java
public class
RowSetWarning

extends
SQLException
```

An extension of

SQLException

that provides information
about database warnings set on

RowSet

objects.
Warnings are silently chained to the object whose method call
caused it to be reported.
This class complements the

SQLWarning

class.

Rowset warnings may be retrieved from

JdbcRowSet

,

CachedRowSet

™,

WebRowSet

,

FilteredRowSet

, or

JoinRowSet

implementations. To retrieve the first warning reported on any

RowSet

implementation, use the method

getRowSetWarnings

defined
in the

JdbcRowSet

interface or the

CachedRowSet

interface. To retrieve a warning chained to the first warning, use the

RowSetWarning

method

getNextWarning

. To retrieve subsequent warnings, call

getNextWarning

on each

RowSetWarning

object that is
returned.

The inherited methods

getMessage

,

getSQLState

,
and

getErrorCode

retrieve information contained in a

RowSetWarning

object.

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

#### public RowSetWarning​(
String
reason)

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

**Parameters:**
- reason

- a

String

object giving a description
of the warning; if the

String

is

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor

---

#### public RowSetWarning()

Constructs a default

RowSetWarning

object. The reason
defaults to

null

, SQLState defaults to null and vendorCode
defaults to 0.

---

#### public RowSetWarning​(
String
reason,

String
SQLState)

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState. The vendor code defaults to 0.

If the

reason

or

SQLState

parameters are

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor.

**Parameters:**
- reason

- a

String

giving a description of the
warning;
- SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.

---

#### public RowSetWarning​(
String
reason,

String
SQLState,
int vendorCode)

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

If the

reason

, or the

SQLState

parameters are

null

, this constructor behaves like the default
(zero parameter)

RowSetWarning

constructor.

**Parameters:**
- reason

- a

String

giving a description of the
warning;
- SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.
- vendorCode

- a database vendor-specific warning code

---

### Method Details

#### public
RowSetWarning
getNextWarning()

Retrieves the warning chained to this

RowSetWarning

object.

**Returns:**
- the

RowSetWarning

object chained to this one; if no

RowSetWarning

object is chained to this one,

null

is returned (default value)

**See Also:**
- setNextWarning(javax.sql.rowset.RowSetWarning)

---

#### public void setNextWarning​(
RowSetWarning
warning)

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

**Parameters:**
- warning

- the

RowSetWarning

object to be set as the
next warning; if the

RowSetWarning

is null, this
represents the finish point in the warning chain

**See Also:**
- getNextWarning()

---

### Additional Sections

#### Class RowSetWarning

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - javax.sql.rowset.RowSetWarning

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - javax.sql.rowset.RowSetWarning

java.lang.Exception

- java.sql.SQLException
- - javax.sql.rowset.RowSetWarning

java.sql.SQLException

- javax.sql.rowset.RowSetWarning

javax.sql.rowset.RowSetWarning

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
RowSetWarning

extends
SQLException
```

An extension of

SQLException

that provides information
about database warnings set on

RowSet

objects.
Warnings are silently chained to the object whose method call
caused it to be reported.
This class complements the

SQLWarning

class.

Rowset warnings may be retrieved from

JdbcRowSet

,

CachedRowSet

™,

WebRowSet

,

FilteredRowSet

, or

JoinRowSet

implementations. To retrieve the first warning reported on any

RowSet

implementation, use the method

getRowSetWarnings

defined
in the

JdbcRowSet

interface or the

CachedRowSet

interface. To retrieve a warning chained to the first warning, use the

RowSetWarning

method

getNextWarning

. To retrieve subsequent warnings, call

getNextWarning

on each

RowSetWarning

object that is
returned.

The inherited methods

getMessage

,

getSQLState

,
and

getErrorCode

retrieve information contained in a

RowSetWarning

object.

**Since:** 1.5
**See Also:** Serialized Form

public class

RowSetWarning

extends

SQLException

An extension of

SQLException

that provides information
about database warnings set on

RowSet

objects.
Warnings are silently chained to the object whose method call
caused it to be reported.
This class complements the

SQLWarning

class.

Rowset warnings may be retrieved from

JdbcRowSet

,

CachedRowSet

™,

WebRowSet

,

FilteredRowSet

, or

JoinRowSet

implementations. To retrieve the first warning reported on any

RowSet

implementation, use the method

getRowSetWarnings

defined
in the

JdbcRowSet

interface or the

CachedRowSet

interface. To retrieve a warning chained to the first warning, use the

RowSetWarning

method

getNextWarning

. To retrieve subsequent warnings, call

getNextWarning

on each

RowSetWarning

object that is
returned.

The inherited methods

getMessage

,

getSQLState

,
and

getErrorCode

retrieve information contained in a

RowSetWarning

object.

Rowset warnings may be retrieved from

JdbcRowSet

,

CachedRowSet

™,

WebRowSet

,

FilteredRowSet

, or

JoinRowSet

implementations. To retrieve the first warning reported on any

RowSet

implementation, use the method

getRowSetWarnings

defined
in the

JdbcRowSet

interface or the

CachedRowSet

interface. To retrieve a warning chained to the first warning, use the

RowSetWarning

method

getNextWarning

. To retrieve subsequent warnings, call

getNextWarning

on each

RowSetWarning

object that is
returned.

The inherited methods

getMessage

,

getSQLState

,
and

getErrorCode

retrieve information contained in a

RowSetWarning

object.

The inherited methods

getMessage

,

getSQLState

,
and

getErrorCode

retrieve information contained in a

RowSetWarning

object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RowSetWarning

()

Constructs a default

RowSetWarning

object.

RowSetWarning

​(

String

reason)

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

RowSetWarning

​(

String

reason,

String

SQLState)

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState.

RowSetWarning

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

RowSetWarning

getNextWarning

()

Retrieves the warning chained to this

RowSetWarning

object.

void

setNextWarning

​(

RowSetWarning

warning)

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

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

RowSetWarning

()

Constructs a default

RowSetWarning

object.

RowSetWarning

​(

String

reason)

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

RowSetWarning

​(

String

reason,

String

SQLState)

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState.

RowSetWarning

​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

---

#### Constructor Summary

Constructs a default

RowSetWarning

object.

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState.

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

RowSetWarning

getNextWarning

()

Retrieves the warning chained to this

RowSetWarning

object.

void

setNextWarning

​(

RowSetWarning

warning)

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

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

RowSetWarning

object.

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

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

- RowSetWarning

```java
public RowSetWarning​(
String
reason)
```

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

**Parameters:** reason

- a

String

object giving a description
of the warning; if the

String

is

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor

- RowSetWarning

```java
public RowSetWarning()
```

Constructs a default

RowSetWarning

object. The reason
defaults to

null

, SQLState defaults to null and vendorCode
defaults to 0.

- RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState)
```

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState. The vendor code defaults to 0.

If the

reason

or

SQLState

parameters are

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.

- RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

If the

reason

, or the

SQLState

parameters are

null

, this constructor behaves like the default
(zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.
**Parameters:** vendorCode

- a database vendor-specific warning code

============ METHOD DETAIL ==========

- Method Detail

- getNextWarning

```java
public
RowSetWarning
getNextWarning()
```

Retrieves the warning chained to this

RowSetWarning

object.

**Returns:** the

RowSetWarning

object chained to this one; if no

RowSetWarning

object is chained to this one,

null

is returned (default value)
**See Also:** setNextWarning(javax.sql.rowset.RowSetWarning)

- setNextWarning

```java
public void setNextWarning​(
RowSetWarning
warning)
```

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

**Parameters:** warning

- the

RowSetWarning

object to be set as the
next warning; if the

RowSetWarning

is null, this
represents the finish point in the warning chain
**See Also:** getNextWarning()

Constructor Detail

- RowSetWarning

```java
public RowSetWarning​(
String
reason)
```

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

**Parameters:** reason

- a

String

object giving a description
of the warning; if the

String

is

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor

- RowSetWarning

```java
public RowSetWarning()
```

Constructs a default

RowSetWarning

object. The reason
defaults to

null

, SQLState defaults to null and vendorCode
defaults to 0.

- RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState)
```

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState. The vendor code defaults to 0.

If the

reason

or

SQLState

parameters are

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.

- RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

If the

reason

, or the

SQLState

parameters are

null

, this constructor behaves like the default
(zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.
**Parameters:** vendorCode

- a database vendor-specific warning code

---

#### Constructor Detail

RowSetWarning

```java
public RowSetWarning​(
String
reason)
```

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

**Parameters:** reason

- a

String

object giving a description
of the warning; if the

String

is

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor

---

#### RowSetWarning

public RowSetWarning​(

String

reason)

Constructs a

RowSetWarning

object
with the given value for the reason; SQLState defaults to null,
and vendorCode defaults to 0.

RowSetWarning

```java
public RowSetWarning()
```

Constructs a default

RowSetWarning

object. The reason
defaults to

null

, SQLState defaults to null and vendorCode
defaults to 0.

---

#### RowSetWarning

public RowSetWarning()

Constructs a default

RowSetWarning

object. The reason
defaults to

null

, SQLState defaults to null and vendorCode
defaults to 0.

RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState)
```

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState. The vendor code defaults to 0.

If the

reason

or

SQLState

parameters are

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.

---

#### RowSetWarning

public RowSetWarning​(

String

reason,

String

SQLState)

Constructs a

RowSetWarning

object initialized with the
given values for the reason and SQLState. The vendor code defaults to 0.

If the

reason

or

SQLState

parameters are

null

,
this constructor behaves like the default (zero parameter)

RowSetWarning

constructor.

RowSetWarning

```java
public RowSetWarning​(
String
reason,

String
SQLState,
int vendorCode)
```

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

If the

reason

, or the

SQLState

parameters are

null

, this constructor behaves like the default
(zero parameter)

RowSetWarning

constructor.

**Parameters:** reason

- a

String

giving a description of the
warning;
**Parameters:** SQLState

- an XOPEN code identifying the warning; if a non standard
XOPEN

SQLState

is supplied, no exception is thrown.
**Parameters:** vendorCode

- a database vendor-specific warning code

---

#### RowSetWarning

public RowSetWarning​(

String

reason,

String

SQLState,
int vendorCode)

Constructs a fully specified

RowSetWarning

object initialized
with the given values for the reason, SQLState and vendorCode.

If the

reason

, or the

SQLState

parameters are

null

, this constructor behaves like the default
(zero parameter)

RowSetWarning

constructor.

Method Detail

- getNextWarning

```java
public
RowSetWarning
getNextWarning()
```

Retrieves the warning chained to this

RowSetWarning

object.

**Returns:** the

RowSetWarning

object chained to this one; if no

RowSetWarning

object is chained to this one,

null

is returned (default value)
**See Also:** setNextWarning(javax.sql.rowset.RowSetWarning)

- setNextWarning

```java
public void setNextWarning​(
RowSetWarning
warning)
```

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

**Parameters:** warning

- the

RowSetWarning

object to be set as the
next warning; if the

RowSetWarning

is null, this
represents the finish point in the warning chain
**See Also:** getNextWarning()

---

#### Method Detail

getNextWarning

```java
public
RowSetWarning
getNextWarning()
```

Retrieves the warning chained to this

RowSetWarning

object.

**Returns:** the

RowSetWarning

object chained to this one; if no

RowSetWarning

object is chained to this one,

null

is returned (default value)
**See Also:** setNextWarning(javax.sql.rowset.RowSetWarning)

---

#### getNextWarning

public

RowSetWarning

getNextWarning()

Retrieves the warning chained to this

RowSetWarning

object.

setNextWarning

```java
public void setNextWarning​(
RowSetWarning
warning)
```

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

**Parameters:** warning

- the

RowSetWarning

object to be set as the
next warning; if the

RowSetWarning

is null, this
represents the finish point in the warning chain
**See Also:** getNextWarning()

---

#### setNextWarning

public void setNextWarning​(

RowSetWarning

warning)

Sets

warning

as the next warning, that is, the warning chained
to this

RowSetWarning

object.

---

