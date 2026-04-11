# Class DataTruncation

**Source:** `java.sql\java\sql\DataTruncation.html`

### Class Description

```java
public class
DataTruncation

extends
SQLWarning
```

An exception thrown as a

DataTruncation

exception
(on writes) or reported as a

DataTruncation

warning (on reads)
when a data values is unexpectedly truncated for reasons other than its having
exceeded

MaxFieldSize

.

The SQLstate for a

DataTruncation

during read is

01004

.

The SQLstate for a

DataTruncation

during write is

22001

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

#### public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:**
- index

- The index of the parameter or column value
- parameter

- true if a parameter value was truncated
- read

- true if a read was truncated
- dataSize

- the original size of the data
- transferSize

- the size after truncation

---

#### public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable
cause)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

**Parameters:**
- index

- The index of the parameter or column value
- parameter

- true if a parameter value was truncated
- read

- true if a read was truncated
- dataSize

- the original size of the data
- transferSize

- the size after truncation
- cause

- the underlying reason for this

DataTruncation

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.

**Since:**
- 1.6

---

### Method Details

#### public int getIndex()

Retrieves the index of the column or parameter that was truncated.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

**Returns:**
- the index of the truncated parameter or column value

---

#### public boolean getParameter()

Indicates whether the value truncated was a parameter value or
a column value.

**Returns:**
- true

if the value truncated was a parameter;

false

if it was a column value

---

#### public boolean getRead()

Indicates whether or not the value was truncated on a read.

**Returns:**
- true

if the value was truncated when read from
the database;

false

if the data was truncated on a write

---

#### public int getDataSize()

Gets the number of bytes of data that should have been transferred.
This number may be approximate if data conversions were being
performed. The value may be

-1

if the size is unknown.

**Returns:**
- the number of bytes of data that should have been transferred

---

#### public int getTransferSize()

Gets the number of bytes of data actually transferred.
The value may be

-1

if the size is unknown.

**Returns:**
- the number of bytes of data actually transferred

---

### Additional Sections

#### Class DataTruncation

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLWarning
- - java.sql.DataTruncation

java.lang.Throwable

- java.lang.Exception
- - java.sql.SQLException
- - java.sql.SQLWarning
- - java.sql.DataTruncation

java.lang.Exception

- java.sql.SQLException
- - java.sql.SQLWarning
- - java.sql.DataTruncation

java.sql.SQLException

- java.sql.SQLWarning
- - java.sql.DataTruncation

java.sql.SQLWarning

- java.sql.DataTruncation

java.sql.DataTruncation

**All Implemented Interfaces:** Serializable

,

Iterable

<

Throwable

>

```java
public class
DataTruncation

extends
SQLWarning
```

An exception thrown as a

DataTruncation

exception
(on writes) or reported as a

DataTruncation

warning (on reads)
when a data values is unexpectedly truncated for reasons other than its having
exceeded

MaxFieldSize

.

The SQLstate for a

DataTruncation

during read is

01004

.

The SQLstate for a

DataTruncation

during write is

22001

.

**Since:** 1.1
**See Also:** Serialized Form

public class

DataTruncation

extends

SQLWarning

An exception thrown as a

DataTruncation

exception
(on writes) or reported as a

DataTruncation

warning (on reads)
when a data values is unexpectedly truncated for reasons other than its having
exceeded

MaxFieldSize

.

The SQLstate for a

DataTruncation

during read is

01004

.

The SQLstate for a

DataTruncation

during write is

22001

.

The SQLstate for a

DataTruncation

during read is

01004

.

The SQLstate for a

DataTruncation

during write is

22001

.

The SQLstate for a

DataTruncation

during write is

22001

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DataTruncation

​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

DataTruncation

​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable

cause)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDataSize

()

Gets the number of bytes of data that should have been transferred.

int

getIndex

()

Retrieves the index of the column or parameter that was truncated.

boolean

getParameter

()

Indicates whether the value truncated was a parameter value or
a column value.

boolean

getRead

()

Indicates whether or not the value was truncated on a read.

int

getTransferSize

()

Gets the number of bytes of data actually transferred.

- Methods declared in class java.sql.

SQLWarning

getNextWarning

,

setNextWarning

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

DataTruncation

​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

DataTruncation

​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable

cause)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

---

#### Constructor Summary

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDataSize

()

Gets the number of bytes of data that should have been transferred.

int

getIndex

()

Retrieves the index of the column or parameter that was truncated.

boolean

getParameter

()

Indicates whether the value truncated was a parameter value or
a column value.

boolean

getRead

()

Indicates whether or not the value was truncated on a read.

int

getTransferSize

()

Gets the number of bytes of data actually transferred.

- Methods declared in class java.sql.

SQLWarning

getNextWarning

,

setNextWarning

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

Gets the number of bytes of data that should have been transferred.

Retrieves the index of the column or parameter that was truncated.

Indicates whether the value truncated was a parameter value or
a column value.

Indicates whether or not the value was truncated on a read.

Gets the number of bytes of data actually transferred.

Methods declared in class java.sql.

SQLWarning

getNextWarning

,

setNextWarning

---

#### Methods declared in class java.sql. SQLWarning

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

- DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation

- DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable
cause)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation
**Parameters:** cause

- the underlying reason for this

DataTruncation

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

============ METHOD DETAIL ==========

- Method Detail

- getIndex

```java
public int getIndex()
```

Retrieves the index of the column or parameter that was truncated.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

**Returns:** the index of the truncated parameter or column value

- getParameter

```java
public boolean getParameter()
```

Indicates whether the value truncated was a parameter value or
a column value.

**Returns:** true

if the value truncated was a parameter;

false

if it was a column value

- getRead

```java
public boolean getRead()
```

Indicates whether or not the value was truncated on a read.

**Returns:** true

if the value was truncated when read from
the database;

false

if the data was truncated on a write

- getDataSize

```java
public int getDataSize()
```

Gets the number of bytes of data that should have been transferred.
This number may be approximate if data conversions were being
performed. The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data that should have been transferred

- getTransferSize

```java
public int getTransferSize()
```

Gets the number of bytes of data actually transferred.
The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data actually transferred

Constructor Detail

- DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation

- DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable
cause)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation
**Parameters:** cause

- the underlying reason for this

DataTruncation

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### Constructor Detail

DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation

---

#### DataTruncation

public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.
The

cause

is not initialized, and may subsequently be
initialized by a call to the

Throwable.initCause(java.lang.Throwable)

method.

DataTruncation

```java
public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable
cause)
```

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

**Parameters:** index

- The index of the parameter or column value
**Parameters:** parameter

- true if a parameter value was truncated
**Parameters:** read

- true if a read was truncated
**Parameters:** dataSize

- the original size of the data
**Parameters:** transferSize

- the size after truncation
**Parameters:** cause

- the underlying reason for this

DataTruncation

(which is saved for later retrieval by the

getCause()

method);
may be null indicating the cause is non-existent or unknown.
**Since:** 1.6

---

#### DataTruncation

public DataTruncation​(int index,
boolean parameter,
boolean read,
int dataSize,
int transferSize,

Throwable

cause)

Creates a

DataTruncation

object
with the SQLState initialized
to 01004 when

read

is set to

true

and 22001
when

read

is set to

false

,
the reason set to "Data truncation", the
vendor code set to 0, and
the other fields set to the given values.

Method Detail

- getIndex

```java
public int getIndex()
```

Retrieves the index of the column or parameter that was truncated.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

**Returns:** the index of the truncated parameter or column value

- getParameter

```java
public boolean getParameter()
```

Indicates whether the value truncated was a parameter value or
a column value.

**Returns:** true

if the value truncated was a parameter;

false

if it was a column value

- getRead

```java
public boolean getRead()
```

Indicates whether or not the value was truncated on a read.

**Returns:** true

if the value was truncated when read from
the database;

false

if the data was truncated on a write

- getDataSize

```java
public int getDataSize()
```

Gets the number of bytes of data that should have been transferred.
This number may be approximate if data conversions were being
performed. The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data that should have been transferred

- getTransferSize

```java
public int getTransferSize()
```

Gets the number of bytes of data actually transferred.
The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data actually transferred

---

#### Method Detail

getIndex

```java
public int getIndex()
```

Retrieves the index of the column or parameter that was truncated.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

**Returns:** the index of the truncated parameter or column value

---

#### getIndex

public int getIndex()

Retrieves the index of the column or parameter that was truncated.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

This may be -1 if the column or parameter index is unknown, in
which case the

parameter

and

read

fields should be ignored.

getParameter

```java
public boolean getParameter()
```

Indicates whether the value truncated was a parameter value or
a column value.

**Returns:** true

if the value truncated was a parameter;

false

if it was a column value

---

#### getParameter

public boolean getParameter()

Indicates whether the value truncated was a parameter value or
a column value.

getRead

```java
public boolean getRead()
```

Indicates whether or not the value was truncated on a read.

**Returns:** true

if the value was truncated when read from
the database;

false

if the data was truncated on a write

---

#### getRead

public boolean getRead()

Indicates whether or not the value was truncated on a read.

getDataSize

```java
public int getDataSize()
```

Gets the number of bytes of data that should have been transferred.
This number may be approximate if data conversions were being
performed. The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data that should have been transferred

---

#### getDataSize

public int getDataSize()

Gets the number of bytes of data that should have been transferred.
This number may be approximate if data conversions were being
performed. The value may be

-1

if the size is unknown.

getTransferSize

```java
public int getTransferSize()
```

Gets the number of bytes of data actually transferred.
The value may be

-1

if the size is unknown.

**Returns:** the number of bytes of data actually transferred

---

#### getTransferSize

public int getTransferSize()

Gets the number of bytes of data actually transferred.
The value may be

-1

if the size is unknown.

---

