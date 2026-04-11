# Interface RowSetInternal

**Source:** `java.sql\javax\sql\RowSetInternal.html`

### Class Description

```java
public interface
RowSetInternal
```

The interface that a

RowSet

object implements in order to
present itself to a

RowSetReader

or

RowSetWriter

object. The

RowSetInternal

interface contains
methods that let the reader or writer access and modify the internal
state of the rowset.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
[] getParams()
throws
SQLException

Retrieves the parameters that have been set for this

RowSet

object's command.

**Returns:**
- an array of the current parameter values for this

RowSet

object's command

**Throws:**
- SQLException

- if a database access error occurs

---

#### Connection
getConnection()
throws
SQLException

Retrieves the

Connection

object that was passed to this

RowSet

object.

**Returns:**
- the

Connection

object passed to the rowset
or

null

if none was passed

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setMetaData​(
RowSetMetaData
md)
throws
SQLException

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object. The

RowSetReader

object associated with the rowset
will use

RowSetMetaData

methods to set the values giving
information about the rowset's columns.

**Parameters:**
- md

- the

RowSetMetaData

object that will be set with
information about the rowset's columns

**Throws:**
- SQLException

- if a database access error occurs

---

#### ResultSet
getOriginal()
throws
SQLException

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

**Returns:**
- the original value of the rowset

**Throws:**
- SQLException

- if a database access error occurs

---

#### ResultSet
getOriginalRow()
throws
SQLException

Retrieves a

ResultSet

object containing the original value
of the current row only. If the current row has no original value,
an empty result set is returned. If there is no current row,
an exception is thrown.

**Returns:**
- the original value of the current row as a

ResultSet

object

**Throws:**
- SQLException

- if a database access error occurs or this method
is called while the cursor is on the insert row, before the
first row, or after the last row

---

### Additional Sections

#### Interface RowSetInternal

```java
public interface
RowSetInternal
```

The interface that a

RowSet

object implements in order to
present itself to a

RowSetReader

or

RowSetWriter

object. The

RowSetInternal

interface contains
methods that let the reader or writer access and modify the internal
state of the rowset.

**Since:** 1.4

public interface

RowSetInternal

The interface that a

RowSet

object implements in order to
present itself to a

RowSetReader

or

RowSetWriter

object. The

RowSetInternal

interface contains
methods that let the reader or writer access and modify the internal
state of the rowset.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Connection

getConnection

()

Retrieves the

Connection

object that was passed to this

RowSet

object.

ResultSet

getOriginal

()

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

ResultSet

getOriginalRow

()

Retrieves a

ResultSet

object containing the original value
of the current row only.

Object

[]

getParams

()

Retrieves the parameters that have been set for this

RowSet

object's command.

void

setMetaData

​(

RowSetMetaData

md)

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Connection

getConnection

()

Retrieves the

Connection

object that was passed to this

RowSet

object.

ResultSet

getOriginal

()

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

ResultSet

getOriginalRow

()

Retrieves a

ResultSet

object containing the original value
of the current row only.

Object

[]

getParams

()

Retrieves the parameters that have been set for this

RowSet

object's command.

void

setMetaData

​(

RowSetMetaData

md)

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object.

---

#### Method Summary

Retrieves the

Connection

object that was passed to this

RowSet

object.

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

Retrieves a

ResultSet

object containing the original value
of the current row only.

Retrieves the parameters that have been set for this

RowSet

object's command.

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object.

============ METHOD DETAIL ==========

- Method Detail

- getParams

```java
Object
[] getParams()
throws
SQLException
```

Retrieves the parameters that have been set for this

RowSet

object's command.

**Returns:** an array of the current parameter values for this

RowSet

object's command
**Throws:** SQLException

- if a database access error occurs

- getConnection

```java
Connection
getConnection()
throws
SQLException
```

Retrieves the

Connection

object that was passed to this

RowSet

object.

**Returns:** the

Connection

object passed to the rowset
or

null

if none was passed
**Throws:** SQLException

- if a database access error occurs

- setMetaData

```java
void setMetaData​(
RowSetMetaData
md)
throws
SQLException
```

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object. The

RowSetReader

object associated with the rowset
will use

RowSetMetaData

methods to set the values giving
information about the rowset's columns.

**Parameters:** md

- the

RowSetMetaData

object that will be set with
information about the rowset's columns
**Throws:** SQLException

- if a database access error occurs

- getOriginal

```java
ResultSet
getOriginal()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

**Returns:** the original value of the rowset
**Throws:** SQLException

- if a database access error occurs

- getOriginalRow

```java
ResultSet
getOriginalRow()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original value
of the current row only. If the current row has no original value,
an empty result set is returned. If there is no current row,
an exception is thrown.

**Returns:** the original value of the current row as a

ResultSet

object
**Throws:** SQLException

- if a database access error occurs or this method
is called while the cursor is on the insert row, before the
first row, or after the last row

Method Detail

- getParams

```java
Object
[] getParams()
throws
SQLException
```

Retrieves the parameters that have been set for this

RowSet

object's command.

**Returns:** an array of the current parameter values for this

RowSet

object's command
**Throws:** SQLException

- if a database access error occurs

- getConnection

```java
Connection
getConnection()
throws
SQLException
```

Retrieves the

Connection

object that was passed to this

RowSet

object.

**Returns:** the

Connection

object passed to the rowset
or

null

if none was passed
**Throws:** SQLException

- if a database access error occurs

- setMetaData

```java
void setMetaData​(
RowSetMetaData
md)
throws
SQLException
```

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object. The

RowSetReader

object associated with the rowset
will use

RowSetMetaData

methods to set the values giving
information about the rowset's columns.

**Parameters:** md

- the

RowSetMetaData

object that will be set with
information about the rowset's columns
**Throws:** SQLException

- if a database access error occurs

- getOriginal

```java
ResultSet
getOriginal()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

**Returns:** the original value of the rowset
**Throws:** SQLException

- if a database access error occurs

- getOriginalRow

```java
ResultSet
getOriginalRow()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original value
of the current row only. If the current row has no original value,
an empty result set is returned. If there is no current row,
an exception is thrown.

**Returns:** the original value of the current row as a

ResultSet

object
**Throws:** SQLException

- if a database access error occurs or this method
is called while the cursor is on the insert row, before the
first row, or after the last row

---

#### Method Detail

getParams

```java
Object
[] getParams()
throws
SQLException
```

Retrieves the parameters that have been set for this

RowSet

object's command.

**Returns:** an array of the current parameter values for this

RowSet

object's command
**Throws:** SQLException

- if a database access error occurs

---

#### getParams

Object

[] getParams()
throws

SQLException

Retrieves the parameters that have been set for this

RowSet

object's command.

getConnection

```java
Connection
getConnection()
throws
SQLException
```

Retrieves the

Connection

object that was passed to this

RowSet

object.

**Returns:** the

Connection

object passed to the rowset
or

null

if none was passed
**Throws:** SQLException

- if a database access error occurs

---

#### getConnection

Connection

getConnection()
throws

SQLException

Retrieves the

Connection

object that was passed to this

RowSet

object.

setMetaData

```java
void setMetaData​(
RowSetMetaData
md)
throws
SQLException
```

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object. The

RowSetReader

object associated with the rowset
will use

RowSetMetaData

methods to set the values giving
information about the rowset's columns.

**Parameters:** md

- the

RowSetMetaData

object that will be set with
information about the rowset's columns
**Throws:** SQLException

- if a database access error occurs

---

#### setMetaData

void setMetaData​(

RowSetMetaData

md)
throws

SQLException

Sets the given

RowSetMetaData

object as the

RowSetMetaData

object for this

RowSet

object. The

RowSetReader

object associated with the rowset
will use

RowSetMetaData

methods to set the values giving
information about the rowset's columns.

getOriginal

```java
ResultSet
getOriginal()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

**Returns:** the original value of the rowset
**Throws:** SQLException

- if a database access error occurs

---

#### getOriginal

ResultSet

getOriginal()
throws

SQLException

Retrieves a

ResultSet

object containing the original
value of this

RowSet

object.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

The cursor is positioned before the first row in the result set.
Only rows contained in the result set returned by the method

getOriginal

are said to have an original value.

getOriginalRow

```java
ResultSet
getOriginalRow()
throws
SQLException
```

Retrieves a

ResultSet

object containing the original value
of the current row only. If the current row has no original value,
an empty result set is returned. If there is no current row,
an exception is thrown.

**Returns:** the original value of the current row as a

ResultSet

object
**Throws:** SQLException

- if a database access error occurs or this method
is called while the cursor is on the insert row, before the
first row, or after the last row

---

#### getOriginalRow

ResultSet

getOriginalRow()
throws

SQLException

Retrieves a

ResultSet

object containing the original value
of the current row only. If the current row has no original value,
an empty result set is returned. If there is no current row,
an exception is thrown.

---

