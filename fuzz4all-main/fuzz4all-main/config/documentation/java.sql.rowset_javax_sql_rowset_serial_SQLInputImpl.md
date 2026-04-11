# Class SQLInputImpl

**Source:** `java.sql.rowset\javax\sql\rowset\serial\SQLInputImpl.html`

### Class Description

```java
public class
SQLInputImpl

extends
Object

implements
SQLInput
```

An input stream used for custom mapping user-defined types (UDTs).
An

SQLInputImpl

object is an input stream that contains a
stream of values that are the attributes of a UDT.

This class is used by the driver behind the scenes when the method

getObject

is called on an SQL structured or distinct type
that has a custom mapping; a programmer never invokes

SQLInputImpl

methods directly. They are provided here as a
convenience for those who write

RowSet

implementations.

The

SQLInputImpl

class provides a set of
reader methods analogous to the

ResultSet

getter
methods. These methods make it possible to read the values in an

SQLInputImpl

object.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

**All Implemented Interfaces:** SQLInput

---

### Field Details

*No entries found.*

### Constructor Details

#### public SQLInputImpl​(
Object
[] attributes,

Map
<
String
,​
Class
<?>> map)
throws
SQLException

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map. If any of the
attributes is a UDT whose name is in an entry in the type map,
the attribute will be mapped according to the corresponding

SQLData

implementation.

**Parameters:**
- attributes

- an array of

Object

instances in which
each element is an attribute of a UDT. The order of the
attributes in the array is the same order in which
the attributes were defined in the UDT definition.
- map

- a

java.util.Map

object containing zero or more
entries, with each entry consisting of 1) a

String

giving the fully
qualified name of the UDT and 2) the

Class

object
for the

SQLData

implementation that defines how
the UDT is to be mapped

**Throws:**
- SQLException

- if the

attributes

or the

map

is a

null

value

---

### Method Details

#### public
String
readString()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readString

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

---

#### public boolean readBoolean()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readBoolean

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

---

#### public byte readByte()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readByte

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream

---

#### public short readShort()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readShort

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public int readInt()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readInt

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public long readLong()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readLong

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public float readFloat()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readFloat

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public double readDouble()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readDouble

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public
BigDecimal
readBigDecimal()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readBigDecimal

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public byte[] readBytes()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readBytes

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public
Date
readDate()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:**
- readDate

in interface

SQLInput

**Returns:**
- the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### public
Time
readTime()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readTime

in interface

SQLInput

**Returns:**
- the attribute; if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Timestamp
readTimestamp()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

**Specified by:**
- readTimestamp

in interface

SQLInput

**Returns:**
- the attribute; if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Reader
readCharacterStream()
throws
SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readCharacterStream

in interface

SQLInput

**Returns:**
- the attribute; if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
InputStream
readAsciiStream()
throws
SQLException

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readAsciiStream

in interface

SQLInput

**Returns:**
- the attribute; if the value is

SQL NULL

,
return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
InputStream
readBinaryStream()
throws
SQLException

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readBinaryStream

in interface

SQLInput

**Returns:**
- the attribute; if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Object
readObject()
throws
SQLException

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default
mapping of SQL types to types in the Java programming language unless
there is a custom mapping, in which case the type of the object
returned is determined by this stream's type map.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

**Specified by:**
- readObject

in interface

SQLInput

**Returns:**
- the value at the head of the stream as an

Object

in the Java programming language;

null

if
the value is SQL

NULL

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Ref
readRef()
throws
SQLException

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

**Specified by:**
- readRef

in interface

SQLInput

**Returns:**
- a

Ref

object representing the SQL

REF

value at the head of the stream; if the value
is

SQL NULL

return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Blob
readBlob()
throws
SQLException

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readBlob

in interface

SQLInput

**Returns:**
- a

Blob

object representing the SQL

BLOB

value at the head of this stream;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Clob
readClob()
throws
SQLException

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readClob

in interface

SQLInput

**Returns:**
- a

Clob

object representing the SQL

CLOB

value at the head of the stream;
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
Array
readArray()
throws
SQLException

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readArray

in interface

SQLInput

**Returns:**
- an

Array

object representing the SQL

ARRAY

value at the head of the stream; *
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public boolean wasNull()
throws
SQLException

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

**Specified by:**
- wasNull

in interface

SQLInput

**Returns:**
- true

if the SQL value read most recently was

null

; otherwise,

false

; by default it
will return false

**Throws:**
- SQLException

- if an error occurs determining the last value
read was a

null

value or not;

---

#### public
URL
readURL()
throws
SQLException

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:**
- readURL

in interface

SQLInput

**Returns:**
- an

URL

object representing the SQL

DATALINK

value at the head of the stream; *
if the value is

SQL NULL

, return

null

**Throws:**
- SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### public
NClob
readNClob()
throws
SQLException

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Specified by:**
- readNClob

in interface

SQLInput

**Returns:**
- a

NClob

object representing data of the SQL

NCLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.6

---

#### public
String
readNString()
throws
SQLException

Reads the next attribute in the stream and returns it as a

String

in the Java programming language. It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

columns.

**Specified by:**
- readNString

in interface

SQLInput

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.6

---

#### public
SQLXML
readSQLXML()
throws
SQLException

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

**Specified by:**
- readSQLXML

in interface

SQLInput

**Returns:**
- a

SQLXML

object representing data of the SQL

XML

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.6

---

#### public
RowId
readRowId()
throws
SQLException

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

**Specified by:**
- readRowId

in interface

SQLInput

**Returns:**
- a

RowId

object representing data of the SQL

ROWID

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.6

---

### Additional Sections

#### Class SQLInputImpl

java.lang.Object

- javax.sql.rowset.serial.SQLInputImpl

javax.sql.rowset.serial.SQLInputImpl

**All Implemented Interfaces:** SQLInput

```java
public class
SQLInputImpl

extends
Object

implements
SQLInput
```

An input stream used for custom mapping user-defined types (UDTs).
An

SQLInputImpl

object is an input stream that contains a
stream of values that are the attributes of a UDT.

This class is used by the driver behind the scenes when the method

getObject

is called on an SQL structured or distinct type
that has a custom mapping; a programmer never invokes

SQLInputImpl

methods directly. They are provided here as a
convenience for those who write

RowSet

implementations.

The

SQLInputImpl

class provides a set of
reader methods analogous to the

ResultSet

getter
methods. These methods make it possible to read the values in an

SQLInputImpl

object.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

**Since:** 1.5
**See Also:** SQLData

public class

SQLInputImpl

extends

Object

implements

SQLInput

An input stream used for custom mapping user-defined types (UDTs).
An

SQLInputImpl

object is an input stream that contains a
stream of values that are the attributes of a UDT.

This class is used by the driver behind the scenes when the method

getObject

is called on an SQL structured or distinct type
that has a custom mapping; a programmer never invokes

SQLInputImpl

methods directly. They are provided here as a
convenience for those who write

RowSet

implementations.

The

SQLInputImpl

class provides a set of
reader methods analogous to the

ResultSet

getter
methods. These methods make it possible to read the values in an

SQLInputImpl

object.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

This class is used by the driver behind the scenes when the method

getObject

is called on an SQL structured or distinct type
that has a custom mapping; a programmer never invokes

SQLInputImpl

methods directly. They are provided here as a
convenience for those who write

RowSet

implementations.

The

SQLInputImpl

class provides a set of
reader methods analogous to the

ResultSet

getter
methods. These methods make it possible to read the values in an

SQLInputImpl

object.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

The

SQLInputImpl

class provides a set of
reader methods analogous to the

ResultSet

getter
methods. These methods make it possible to read the values in an

SQLInputImpl

object.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

The method

wasNull

is used to determine whether the
the last value read was SQL

NULL

.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the UDT being custom mapped. The driver
creates an instance of

SQLInputImpl

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInputImpl

reader methods
to read the attributes from the input stream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SQLInputImpl

​(

Object

[] attributes,

Map

<

String

,​

Class

<?>> map)

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Array

readArray

()

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

InputStream

readAsciiStream

()

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

BigDecimal

readBigDecimal

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

InputStream

readBinaryStream

()

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

Blob

readBlob

()

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

boolean

readBoolean

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

byte

readByte

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

byte[]

readBytes

()

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

Reader

readCharacterStream

()

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

Clob

readClob

()

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

Date

readDate

()

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

double

readDouble

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

float

readFloat

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

int

readInt

()

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

long

readLong

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

NClob

readNClob

()

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

String

readNString

()

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Object

readObject

()

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language.

Ref

readRef

()

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

RowId

readRowId

()

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

short

readShort

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

SQLXML

readSQLXML

()

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

String

readString

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

Time

readTime

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

Timestamp

readTimestamp

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

URL

readURL

()

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

boolean

wasNull

()

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.sql.

SQLInput

readObject

Constructor Summary

Constructors

Constructor

Description

SQLInputImpl

​(

Object

[] attributes,

Map

<

String

,​

Class

<?>> map)

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map.

---

#### Constructor Summary

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Array

readArray

()

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

InputStream

readAsciiStream

()

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

BigDecimal

readBigDecimal

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

InputStream

readBinaryStream

()

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

Blob

readBlob

()

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

boolean

readBoolean

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

byte

readByte

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

byte[]

readBytes

()

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

Reader

readCharacterStream

()

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

Clob

readClob

()

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

Date

readDate

()

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

double

readDouble

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

float

readFloat

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

int

readInt

()

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

long

readLong

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

NClob

readNClob

()

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

String

readNString

()

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Object

readObject

()

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language.

Ref

readRef

()

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

RowId

readRowId

()

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

short

readShort

()

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

SQLXML

readSQLXML

()

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

String

readString

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

Time

readTime

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

Timestamp

readTimestamp

()

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

URL

readURL

()

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

boolean

wasNull

()

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.sql.

SQLInput

readObject

---

#### Method Summary

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language.

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.sql.

SQLInput

readObject

---

#### Methods declared in interface java.sql. SQLInput

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SQLInputImpl

```java
public SQLInputImpl​(
Object
[] attributes,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map. If any of the
attributes is a UDT whose name is in an entry in the type map,
the attribute will be mapped according to the corresponding

SQLData

implementation.

**Parameters:** attributes

- an array of

Object

instances in which
each element is an attribute of a UDT. The order of the
attributes in the array is the same order in which
the attributes were defined in the UDT definition.
**Parameters:** map

- a

java.util.Map

object containing zero or more
entries, with each entry consisting of 1) a

String

giving the fully
qualified name of the UDT and 2) the

Class

object
for the

SQLData

implementation that defines how
the UDT is to be mapped
**Throws:** SQLException

- if the

attributes

or the

map

is a

null

value

============ METHOD DETAIL ==========

- Method Detail

- readString

```java
public
String
readString()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readString

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

- readBoolean

```java
public boolean readBoolean()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBoolean

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

- readByte

```java
public byte readByte()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readByte

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream

- readShort

```java
public short readShort()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readShort

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readInt

```java
public int readInt()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readInt

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readLong

```java
public long readLong()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readLong

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readFloat

```java
public float readFloat()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readFloat

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readDouble

```java
public double readDouble()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDouble

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readBigDecimal

```java
public
BigDecimal
readBigDecimal()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBigDecimal

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readBytes

```java
public byte[] readBytes()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBytes

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readDate

```java
public
Date
readDate()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDate

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readTime

```java
public
Time
readTime()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readTime

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readTimestamp

```java
public
Timestamp
readTimestamp()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

**Specified by:** readTimestamp

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readCharacterStream

```java
public
Reader
readCharacterStream()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readCharacterStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readAsciiStream

```java
public
InputStream
readAsciiStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readAsciiStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

,
return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readBinaryStream

```java
public
InputStream
readBinaryStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBinaryStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readObject

```java
public
Object
readObject()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default
mapping of SQL types to types in the Java programming language unless
there is a custom mapping, in which case the type of the object
returned is determined by this stream's type map.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

**Specified by:** readObject

in interface

SQLInput
**Returns:** the value at the head of the stream as an

Object

in the Java programming language;

null

if
the value is SQL

NULL
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readRef

```java
public
Ref
readRef()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

**Specified by:** readRef

in interface

SQLInput
**Returns:** a

Ref

object representing the SQL

REF

value at the head of the stream; if the value
is

SQL NULL

return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readBlob

```java
public
Blob
readBlob()
throws
SQLException
```

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBlob

in interface

SQLInput
**Returns:** a

Blob

object representing the SQL

BLOB

value at the head of this stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readClob

```java
public
Clob
readClob()
throws
SQLException
```

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readClob

in interface

SQLInput
**Returns:** a

Clob

object representing the SQL

CLOB

value at the head of the stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readArray

```java
public
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readArray

in interface

SQLInput
**Returns:** an

Array

object representing the SQL

ARRAY

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- wasNull

```java
public boolean wasNull()
throws
SQLException
```

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

**Specified by:** wasNull

in interface

SQLInput
**Returns:** true

if the SQL value read most recently was

null

; otherwise,

false

; by default it
will return false
**Throws:** SQLException

- if an error occurs determining the last value
read was a

null

value or not;

- readURL

```java
public
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readURL

in interface

SQLInput
**Returns:** an

URL

object representing the SQL

DATALINK

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readNClob

```java
public
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Specified by:** readNClob

in interface

SQLInput
**Returns:** a

NClob

object representing data of the SQL

NCLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readNString

```java
public
String
readNString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language. It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

columns.

**Specified by:** readNString

in interface

SQLInput
**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readSQLXML

```java
public
SQLXML
readSQLXML()
throws
SQLException
```

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

**Specified by:** readSQLXML

in interface

SQLInput
**Returns:** a

SQLXML

object representing data of the SQL

XML

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readRowId

```java
public
RowId
readRowId()
throws
SQLException
```

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

**Specified by:** readRowId

in interface

SQLInput
**Returns:** a

RowId

object representing data of the SQL

ROWID

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

Constructor Detail

- SQLInputImpl

```java
public SQLInputImpl​(
Object
[] attributes,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map. If any of the
attributes is a UDT whose name is in an entry in the type map,
the attribute will be mapped according to the corresponding

SQLData

implementation.

**Parameters:** attributes

- an array of

Object

instances in which
each element is an attribute of a UDT. The order of the
attributes in the array is the same order in which
the attributes were defined in the UDT definition.
**Parameters:** map

- a

java.util.Map

object containing zero or more
entries, with each entry consisting of 1) a

String

giving the fully
qualified name of the UDT and 2) the

Class

object
for the

SQLData

implementation that defines how
the UDT is to be mapped
**Throws:** SQLException

- if the

attributes

or the

map

is a

null

value

---

#### Constructor Detail

SQLInputImpl

```java
public SQLInputImpl​(
Object
[] attributes,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map. If any of the
attributes is a UDT whose name is in an entry in the type map,
the attribute will be mapped according to the corresponding

SQLData

implementation.

**Parameters:** attributes

- an array of

Object

instances in which
each element is an attribute of a UDT. The order of the
attributes in the array is the same order in which
the attributes were defined in the UDT definition.
**Parameters:** map

- a

java.util.Map

object containing zero or more
entries, with each entry consisting of 1) a

String

giving the fully
qualified name of the UDT and 2) the

Class

object
for the

SQLData

implementation that defines how
the UDT is to be mapped
**Throws:** SQLException

- if the

attributes

or the

map

is a

null

value

---

#### SQLInputImpl

public SQLInputImpl​(

Object

[] attributes,

Map

<

String

,​

Class

<?>> map)
throws

SQLException

Creates an

SQLInputImpl

object initialized with the
given array of attributes and the given type map. If any of the
attributes is a UDT whose name is in an entry in the type map,
the attribute will be mapped according to the corresponding

SQLData

implementation.

Method Detail

- readString

```java
public
String
readString()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readString

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

- readBoolean

```java
public boolean readBoolean()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBoolean

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

- readByte

```java
public byte readByte()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readByte

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream

- readShort

```java
public short readShort()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readShort

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readInt

```java
public int readInt()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readInt

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readLong

```java
public long readLong()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readLong

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readFloat

```java
public float readFloat()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readFloat

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readDouble

```java
public double readDouble()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDouble

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readBigDecimal

```java
public
BigDecimal
readBigDecimal()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBigDecimal

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readBytes

```java
public byte[] readBytes()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBytes

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readDate

```java
public
Date
readDate()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDate

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

- readTime

```java
public
Time
readTime()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readTime

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readTimestamp

```java
public
Timestamp
readTimestamp()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

**Specified by:** readTimestamp

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readCharacterStream

```java
public
Reader
readCharacterStream()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readCharacterStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readAsciiStream

```java
public
InputStream
readAsciiStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readAsciiStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

,
return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readBinaryStream

```java
public
InputStream
readBinaryStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBinaryStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readObject

```java
public
Object
readObject()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default
mapping of SQL types to types in the Java programming language unless
there is a custom mapping, in which case the type of the object
returned is determined by this stream's type map.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

**Specified by:** readObject

in interface

SQLInput
**Returns:** the value at the head of the stream as an

Object

in the Java programming language;

null

if
the value is SQL

NULL
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readRef

```java
public
Ref
readRef()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

**Specified by:** readRef

in interface

SQLInput
**Returns:** a

Ref

object representing the SQL

REF

value at the head of the stream; if the value
is

SQL NULL

return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readBlob

```java
public
Blob
readBlob()
throws
SQLException
```

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBlob

in interface

SQLInput
**Returns:** a

Blob

object representing the SQL

BLOB

value at the head of this stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readClob

```java
public
Clob
readClob()
throws
SQLException
```

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readClob

in interface

SQLInput
**Returns:** a

Clob

object representing the SQL

CLOB

value at the head of the stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readArray

```java
public
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readArray

in interface

SQLInput
**Returns:** an

Array

object representing the SQL

ARRAY

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- wasNull

```java
public boolean wasNull()
throws
SQLException
```

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

**Specified by:** wasNull

in interface

SQLInput
**Returns:** true

if the SQL value read most recently was

null

; otherwise,

false

; by default it
will return false
**Throws:** SQLException

- if an error occurs determining the last value
read was a

null

value or not;

- readURL

```java
public
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readURL

in interface

SQLInput
**Returns:** an

URL

object representing the SQL

DATALINK

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

- readNClob

```java
public
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Specified by:** readNClob

in interface

SQLInput
**Returns:** a

NClob

object representing data of the SQL

NCLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readNString

```java
public
String
readNString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language. It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

columns.

**Specified by:** readNString

in interface

SQLInput
**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readSQLXML

```java
public
SQLXML
readSQLXML()
throws
SQLException
```

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

**Specified by:** readSQLXML

in interface

SQLInput
**Returns:** a

SQLXML

object representing data of the SQL

XML

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

- readRowId

```java
public
RowId
readRowId()
throws
SQLException
```

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

**Specified by:** readRowId

in interface

SQLInput
**Returns:** a

RowId

object representing data of the SQL

ROWID

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### Method Detail

readString

```java
public
String
readString()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readString

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

---

#### readString

public

String

readString()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

String

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readBoolean

```java
public boolean readBoolean()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBoolean

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream.

---

#### readBoolean

public boolean readBoolean()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

boolean

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readByte

```java
public byte readByte()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readByte

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no further values in the stream

---

#### readByte

public byte readByte()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

byte

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readShort

```java
public short readShort()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readShort

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readShort

public short readShort()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

short

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readInt

```java
public int readInt()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readInt

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readInt

public int readInt()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as an

int

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readLong

```java
public long readLong()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readLong

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readLong

public long readLong()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

long

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readFloat

```java
public float readFloat()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readFloat

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readFloat

public float readFloat()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

float

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readDouble

```java
public double readDouble()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDouble

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readDouble

public double readDouble()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

double

in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readBigDecimal

```java
public
BigDecimal
readBigDecimal()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBigDecimal

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readBigDecimal

public

BigDecimal

readBigDecimal()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a

java.math.BigDecimal

.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readBytes

```java
public byte[] readBytes()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readBytes

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readBytes

public byte[] readBytes()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as an array of bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readDate

```java
public
Date
readDate()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

**Specified by:** readDate

in interface

SQLInput
**Returns:** the next attribute in this

SQLInputImpl

object;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position or if there are no more values in the stream

---

#### readDate

public

Date

readDate()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

as
a

java.sql.Date

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type; this responsibility is delegated
to the UDT mapping as defined by a

SQLData

implementation.

readTime

```java
public
Time
readTime()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readTime

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readTime

public

Time

readTime()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Time

object.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readTimestamp

```java
public
Timestamp
readTimestamp()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

**Specified by:** readTimestamp

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readTimestamp

public

Timestamp

readTimestamp()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object as
a

java.sql.Timestamp

object.

readCharacterStream

```java
public
Reader
readCharacterStream()
throws
SQLException
```

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readCharacterStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readCharacterStream

public

Reader

readCharacterStream()
throws

SQLException

Retrieves the next attribute in this

SQLInputImpl

object
as a stream of Unicode characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readAsciiStream

```java
public
InputStream
readAsciiStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readAsciiStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

,
return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readAsciiStream

public

InputStream

readAsciiStream()
throws

SQLException

Returns the next attribute in this

SQLInputImpl

object
as a stream of ASCII characters.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readBinaryStream

```java
public
InputStream
readBinaryStream()
throws
SQLException
```

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBinaryStream

in interface

SQLInput
**Returns:** the attribute; if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readBinaryStream

public

InputStream

readBinaryStream()
throws

SQLException

Returns the next attribute in this

SQLInputImpl

object
as a stream of uninterpreted bytes.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readObject

```java
public
Object
readObject()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default
mapping of SQL types to types in the Java programming language unless
there is a custom mapping, in which case the type of the object
returned is determined by this stream's type map.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

**Specified by:** readObject

in interface

SQLInput
**Returns:** the value at the head of the stream as an

Object

in the Java programming language;

null

if
the value is SQL

NULL
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readObject

public

Object

readObject()
throws

SQLException

Retrieves the value at the head of this

SQLInputImpl

object as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default
mapping of SQL types to types in the Java programming language unless
there is a custom mapping, in which case the type of the object
returned is determined by this stream's type map.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

The JDBC technology-enabled driver registers a type map with the stream
before passing the stream to the application.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

When the datum at the head of the stream is an SQL

NULL

,
this method returns

null

. If the datum is an SQL
structured or distinct type with a custom mapping, this method
determines the SQL type of the datum at the head of the stream,
constructs an object of the appropriate class, and calls the method

SQLData.readSQL

on that object. The

readSQL

method then calls the appropriate

SQLInputImpl.readXXX

methods to retrieve the attribute values from the stream.

readRef

```java
public
Ref
readRef()
throws
SQLException
```

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

**Specified by:** readRef

in interface

SQLInput
**Returns:** a

Ref

object representing the SQL

REF

value at the head of the stream; if the value
is

SQL NULL

return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readRef

public

Ref

readRef()
throws

SQLException

Retrieves the value at the head of this

SQLInputImpl

object
as a

Ref

object in the Java programming language.

readBlob

```java
public
Blob
readBlob()
throws
SQLException
```

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readBlob

in interface

SQLInput
**Returns:** a

Blob

object representing the SQL

BLOB

value at the head of this stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readBlob

public

Blob

readBlob()
throws

SQLException

Retrieves the

BLOB

value at the head of this

SQLInputImpl

object as a

Blob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readClob

```java
public
Clob
readClob()
throws
SQLException
```

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readClob

in interface

SQLInput
**Returns:** a

Clob

object representing the SQL

CLOB

value at the head of the stream;
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readClob

public

Clob

readClob()
throws

SQLException

Retrieves the

CLOB

value at the head of this

SQLInputImpl

object as a

Clob

object
in the Java programming language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readArray

```java
public
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readArray

in interface

SQLInput
**Returns:** an

Array

object representing the SQL

ARRAY

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readArray

public

Array

readArray()
throws

SQLException

Reads an SQL

ARRAY

value from the stream and
returns it as an

Array

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

wasNull

```java
public boolean wasNull()
throws
SQLException
```

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

**Specified by:** wasNull

in interface

SQLInput
**Returns:** true

if the SQL value read most recently was

null

; otherwise,

false

; by default it
will return false
**Throws:** SQLException

- if an error occurs determining the last value
read was a

null

value or not;

---

#### wasNull

public boolean wasNull()
throws

SQLException

Ascertains whether the last value read from this

SQLInputImpl

object was

null

.

readURL

```java
public
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

**Specified by:** readURL

in interface

SQLInput
**Returns:** an

URL

object representing the SQL

DATALINK

value at the head of the stream; *
if the value is

SQL NULL

, return

null
**Throws:** SQLException

- if the read position is located at an invalid
position; or if there are no further values in the stream.

---

#### readURL

public

URL

readURL()
throws

SQLException

Reads an SQL

DATALINK

value from the stream and
returns it as an

URL

object in the Java programming
language.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

This method does not perform type-safe checking to determine if the
returned type is the expected type as this responsibility is delegated
to the UDT mapping as implemented by a

SQLData

implementation.

readNClob

```java
public
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Specified by:** readNClob

in interface

SQLInput
**Returns:** a

NClob

object representing data of the SQL

NCLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### readNClob

public

NClob

readNClob()
throws

SQLException

Reads an SQL

NCLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

readNString

```java
public
String
readNString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language. It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

columns.

**Specified by:** readNString

in interface

SQLInput
**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### readNString

public

String

readNString()
throws

SQLException

Reads the next attribute in the stream and returns it as a

String

in the Java programming language. It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

columns.

readSQLXML

```java
public
SQLXML
readSQLXML()
throws
SQLException
```

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

**Specified by:** readSQLXML

in interface

SQLInput
**Returns:** a

SQLXML

object representing data of the SQL

XML

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### readSQLXML

public

SQLXML

readSQLXML()
throws

SQLException

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

readRowId

```java
public
RowId
readRowId()
throws
SQLException
```

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

**Specified by:** readRowId

in interface

SQLInput
**Returns:** a

RowId

object representing data of the SQL

ROWID

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### readRowId

public

RowId

readRowId()
throws

SQLException

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

---

