# Interface NClob

**Source:** `java.sql\java\sql\NClob.html`

### Class Description

```java
public interface
NClob

extends
Clob
```

The mapping in the Java™ programming language
for the SQL

NCLOB

type.
An SQL

NCLOB

is a built-in type
that stores a Character Large Object using the National Character Set
as a column value in a row of a database table.

The

NClob

interface extends the

Clob

interface
which provides methods for getting the
length of an SQL

NCLOB

value,
for materializing a

NCLOB

value on the client, and for
searching for a substring or

NCLOB

object within a

NCLOB

value. A

NClob

object, just like a

Clob

object, is valid for the duration
of the transaction in which it was created.
Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getNClob

and

setNClob

allow a programmer to
access an SQL

NCLOB

value. In addition, this interface
has methods for updating a

NCLOB

value.

All methods on the

NClob

interface must be fully implemented if the
JDBC driver supports the data type.

**All Superinterfaces:** Clob

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface NClob

**All Superinterfaces:** Clob

```java
public interface
NClob

extends
Clob
```

The mapping in the Java™ programming language
for the SQL

NCLOB

type.
An SQL

NCLOB

is a built-in type
that stores a Character Large Object using the National Character Set
as a column value in a row of a database table.

The

NClob

interface extends the

Clob

interface
which provides methods for getting the
length of an SQL

NCLOB

value,
for materializing a

NCLOB

value on the client, and for
searching for a substring or

NCLOB

object within a

NCLOB

value. A

NClob

object, just like a

Clob

object, is valid for the duration
of the transaction in which it was created.
Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getNClob

and

setNClob

allow a programmer to
access an SQL

NCLOB

value. In addition, this interface
has methods for updating a

NCLOB

value.

All methods on the

NClob

interface must be fully implemented if the
JDBC driver supports the data type.

**Since:** 1.6

public interface

NClob

extends

Clob

The mapping in the Java™ programming language
for the SQL

NCLOB

type.
An SQL

NCLOB

is a built-in type
that stores a Character Large Object using the National Character Set
as a column value in a row of a database table.

The

NClob

interface extends the

Clob

interface
which provides methods for getting the
length of an SQL

NCLOB

value,
for materializing a

NCLOB

value on the client, and for
searching for a substring or

NCLOB

object within a

NCLOB

value. A

NClob

object, just like a

Clob

object, is valid for the duration
of the transaction in which it was created.
Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getNClob

and

setNClob

allow a programmer to
access an SQL

NCLOB

value. In addition, this interface
has methods for updating a

NCLOB

value.

All methods on the

NClob

interface must be fully implemented if the
JDBC driver supports the data type.

The

NClob

interface extends the

Clob

interface
which provides methods for getting the
length of an SQL

NCLOB

value,
for materializing a

NCLOB

value on the client, and for
searching for a substring or

NCLOB

object within a

NCLOB

value. A

NClob

object, just like a

Clob

object, is valid for the duration
of the transaction in which it was created.
Methods in the interfaces

ResultSet

,

CallableStatement

, and

PreparedStatement

, such as

getNClob

and

setNClob

allow a programmer to
access an SQL

NCLOB

value. In addition, this interface
has methods for updating a

NCLOB

value.

All methods on the

NClob

interface must be fully implemented if the
JDBC driver supports the data type.

All methods on the

NClob

interface must be fully implemented if the
JDBC driver supports the data type.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface java.sql.

Clob

free

,

getAsciiStream

,

getCharacterStream

,

getCharacterStream

,

getSubString

,

length

,

position

,

position

,

setAsciiStream

,

setCharacterStream

,

setString

,

setString

,

truncate

Method Summary

- Methods declared in interface java.sql.

Clob

free

,

getAsciiStream

,

getCharacterStream

,

getCharacterStream

,

getSubString

,

length

,

position

,

position

,

setAsciiStream

,

setCharacterStream

,

setString

,

setString

,

truncate

---

#### Method Summary

Methods declared in interface java.sql.

Clob

free

,

getAsciiStream

,

getCharacterStream

,

getCharacterStream

,

getSubString

,

length

,

position

,

position

,

setAsciiStream

,

setCharacterStream

,

setString

,

setString

,

truncate

---

