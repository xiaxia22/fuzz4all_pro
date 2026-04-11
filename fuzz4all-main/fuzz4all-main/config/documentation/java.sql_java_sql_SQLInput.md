# Interface SQLInput

**Source:** `java.sql\java\sql\SQLInput.html`

### Class Description

```java
public interface
SQLInput
```

An input stream that contains a stream of values representing an
instance of an SQL structured type or an SQL distinct type.
This interface, used only for custom mapping, is used by the driver
behind the scenes, and a programmer never directly invokes

SQLInput

methods. The

reader

methods
(

readLong

,

readBytes

, and so on)
provide a way for an implementation of the

SQLData

interface to read the values in an

SQLInput

object.
And as described in

SQLData

, calls to reader methods must
be made in the order that their corresponding attributes appear in the
SQL definition of the type.
The method

wasNull

is used to determine whether
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

to determine the SQL type of the user-defined type (UDT)
being custom mapped. The driver
creates an instance of

SQLInput

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInput

reader methods
in its implementation for reading the
attributes from the input stream.

**All Known Implementing Classes:** SQLInputImpl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
readString()
throws
SQLException

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### boolean readBoolean()
throws
SQLException

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

false

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### byte readByte()
throws
SQLException

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### short readShort()
throws
SQLException

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### int readInt()
throws
SQLException

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### long readLong()
throws
SQLException

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### float readFloat()
throws
SQLException

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### double readDouble()
throws
SQLException

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

0

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### BigDecimal
readBigDecimal()
throws
SQLException

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### byte[] readBytes()
throws
SQLException

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Date
readDate()
throws
SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Time
readTime()
throws
SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Timestamp
readTimestamp()
throws
SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Reader
readCharacterStream()
throws
SQLException

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### InputStream
readAsciiStream()
throws
SQLException

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### InputStream
readBinaryStream()
throws
SQLException

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Object
readObject()
throws
SQLException

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default type
mapping, and any customizations present in this stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

**Returns:**
- the datum at the head of the stream as an

Object

in the
Java programming language;

null

if the datum is SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Ref
readRef()
throws
SQLException

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

**Returns:**
- a

Ref

object representing the SQL

REF

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Blob
readBlob()
throws
SQLException

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

**Returns:**
- a

Blob

object representing data of the SQL

BLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Clob
readClob()
throws
SQLException

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Returns:**
- a

Clob

object representing data of the SQL

CLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Array
readArray()
throws
SQLException

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

**Returns:**
- an

Array

object representing data of the SQL

ARRAY

value at the head of the stream;

null

if the value read is SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### boolean wasNull()
throws
SQLException

Retrieves whether the last value read was SQL

NULL

.

**Returns:**
- true

if the most recently read SQL value was SQL

NULL

;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### URL
readURL()
throws
SQLException

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

**Returns:**
- a

java.net.URL

object.

**Throws:**
- SQLException

- if a database access error occurs,
or if a URL is malformed
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### NClob
readNClob()
throws
SQLException

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

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
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### String
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

**Returns:**
- the attribute; if the value is SQL

NULL

, returns

null

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### SQLXML
readSQLXML()
throws
SQLException

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

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
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### RowId
readRowId()
throws
SQLException

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

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
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### default <T> T readObject​(
Class
<T> type)
throws
SQLException

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the specified
Java data type, and any customizations present in this
stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- type

- Class representing the Java data type to convert the attribute to.

**Returns:**
- the attribute at the head of the stream as an

Object

in the
Java programming language;

null

if the attribute is SQL

NULL

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.8

**Type Parameters:**
- T

- the type of the class modeled by this Class object

---

### Additional Sections

#### Interface SQLInput

**All Known Implementing Classes:** SQLInputImpl

```java
public interface
SQLInput
```

An input stream that contains a stream of values representing an
instance of an SQL structured type or an SQL distinct type.
This interface, used only for custom mapping, is used by the driver
behind the scenes, and a programmer never directly invokes

SQLInput

methods. The

reader

methods
(

readLong

,

readBytes

, and so on)
provide a way for an implementation of the

SQLData

interface to read the values in an

SQLInput

object.
And as described in

SQLData

, calls to reader methods must
be made in the order that their corresponding attributes appear in the
SQL definition of the type.
The method

wasNull

is used to determine whether
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

to determine the SQL type of the user-defined type (UDT)
being custom mapped. The driver
creates an instance of

SQLInput

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInput

reader methods
in its implementation for reading the
attributes from the input stream.

**Since:** 1.2

public interface

SQLInput

An input stream that contains a stream of values representing an
instance of an SQL structured type or an SQL distinct type.
This interface, used only for custom mapping, is used by the driver
behind the scenes, and a programmer never directly invokes

SQLInput

methods. The

reader

methods
(

readLong

,

readBytes

, and so on)
provide a way for an implementation of the

SQLData

interface to read the values in an

SQLInput

object.
And as described in

SQLData

, calls to reader methods must
be made in the order that their corresponding attributes appear in the
SQL definition of the type.
The method

wasNull

is used to determine whether
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

to determine the SQL type of the user-defined type (UDT)
being custom mapped. The driver
creates an instance of

SQLInput

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInput

reader methods
in its implementation for reading the
attributes from the input stream.

When the method

getObject

is called with an
object of a class implementing the interface

SQLData

,
the JDBC driver calls the method

SQLData.getSQLType

to determine the SQL type of the user-defined type (UDT)
being custom mapped. The driver
creates an instance of

SQLInput

, populating it with the
attributes of the UDT. The driver then passes the input
stream to the method

SQLData.readSQL

, which in turn
calls the

SQLInput

reader methods
in its implementation for reading the
attributes from the input stream.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Array

readArray

()

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

InputStream

readAsciiStream

()

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

BigDecimal

readBigDecimal

()

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

InputStream

readBinaryStream

()

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

Blob

readBlob

()

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

boolean

readBoolean

()

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

byte

readByte

()

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

byte[]

readBytes

()

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

Reader

readCharacterStream

()

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

Clob

readClob

()

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

Date

readDate

()

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

double

readDouble

()

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

float

readFloat

()

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

int

readInt

()

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

long

readLong

()

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

NClob

readNClob

()

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

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

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language.

default <T> T

readObject

​(

Class

<T> type)

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language.

Ref

readRef

()

Reads an SQL

REF

value from the stream and returns it as a

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

Reads the next attribute in the stream and returns it as a

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

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Time

readTime

()

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

Timestamp

readTimestamp

()

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

URL

readURL

()

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

boolean

wasNull

()

Retrieves whether the last value read was SQL

NULL

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

Array

readArray

()

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

InputStream

readAsciiStream

()

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

BigDecimal

readBigDecimal

()

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

InputStream

readBinaryStream

()

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

Blob

readBlob

()

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

boolean

readBoolean

()

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

byte

readByte

()

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

byte[]

readBytes

()

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

Reader

readCharacterStream

()

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

Clob

readClob

()

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

Date

readDate

()

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

double

readDouble

()

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

float

readFloat

()

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

int

readInt

()

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

long

readLong

()

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

NClob

readNClob

()

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

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

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language.

default <T> T

readObject

​(

Class

<T> type)

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language.

Ref

readRef

()

Reads an SQL

REF

value from the stream and returns it as a

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

Reads the next attribute in the stream and returns it as a

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

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Time

readTime

()

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

Timestamp

readTimestamp

()

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

URL

readURL

()

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

boolean

wasNull

()

Retrieves whether the last value read was SQL

NULL

.

---

#### Method Summary

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language.

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language.

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

Reads an SQL

XML

value from the stream and returns it as a

SQLXML

object in the Java programming language.

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

Retrieves whether the last value read was SQL

NULL

.

============ METHOD DETAIL ==========

- Method Detail

- readString

```java
String
readString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBoolean

```java
boolean readBoolean()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

false
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readByte

```java
byte readByte()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readShort

```java
short readShort()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readInt

```java
int readInt()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readLong

```java
long readLong()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readFloat

```java
float readFloat()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readDouble

```java
double readDouble()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBigDecimal

```java
BigDecimal
readBigDecimal()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBytes

```java
byte[] readBytes()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readDate

```java
Date
readDate()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readTime

```java
Time
readTime()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readTimestamp

```java
Timestamp
readTimestamp()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readCharacterStream

```java
Reader
readCharacterStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readAsciiStream

```java
InputStream
readAsciiStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBinaryStream

```java
InputStream
readBinaryStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readObject

```java
Object
readObject()
throws
SQLException
```

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default type
mapping, and any customizations present in this stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

**Returns:** the datum at the head of the stream as an

Object

in the
Java programming language;

null

if the datum is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readRef

```java
Ref
readRef()
throws
SQLException
```

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

**Returns:** a

Ref

object representing the SQL

REF

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBlob

```java
Blob
readBlob()
throws
SQLException
```

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

**Returns:** a

Blob

object representing data of the SQL

BLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readClob

```java
Clob
readClob()
throws
SQLException
```

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Returns:** a

Clob

object representing data of the SQL

CLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readArray

```java
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

**Returns:** an

Array

object representing data of the SQL

ARRAY

value at the head of the stream;

null

if the value read is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last value read was SQL

NULL

.

**Returns:** true

if the most recently read SQL value was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readURL

```java
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

**Returns:** a

java.net.URL

object.
**Throws:** SQLException

- if a database access error occurs,
or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- readNClob

```java
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readNString

```java
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

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readSQLXML

```java
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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readRowId

```java
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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readObject

```java
default <T> T readObject​(
Class
<T> type)
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the specified
Java data type, and any customizations present in this
stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** type

- Class representing the Java data type to convert the attribute to.
**Returns:** the attribute at the head of the stream as an

Object

in the
Java programming language;

null

if the attribute is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.8

Method Detail

- readString

```java
String
readString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBoolean

```java
boolean readBoolean()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

false
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readByte

```java
byte readByte()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readShort

```java
short readShort()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readInt

```java
int readInt()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readLong

```java
long readLong()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readFloat

```java
float readFloat()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readDouble

```java
double readDouble()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBigDecimal

```java
BigDecimal
readBigDecimal()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBytes

```java
byte[] readBytes()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readDate

```java
Date
readDate()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readTime

```java
Time
readTime()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readTimestamp

```java
Timestamp
readTimestamp()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readCharacterStream

```java
Reader
readCharacterStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readAsciiStream

```java
InputStream
readAsciiStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBinaryStream

```java
InputStream
readBinaryStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readObject

```java
Object
readObject()
throws
SQLException
```

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default type
mapping, and any customizations present in this stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

**Returns:** the datum at the head of the stream as an

Object

in the
Java programming language;

null

if the datum is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readRef

```java
Ref
readRef()
throws
SQLException
```

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

**Returns:** a

Ref

object representing the SQL

REF

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readBlob

```java
Blob
readBlob()
throws
SQLException
```

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

**Returns:** a

Blob

object representing data of the SQL

BLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readClob

```java
Clob
readClob()
throws
SQLException
```

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Returns:** a

Clob

object representing data of the SQL

CLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readArray

```java
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

**Returns:** an

Array

object representing data of the SQL

ARRAY

value at the head of the stream;

null

if the value read is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last value read was SQL

NULL

.

**Returns:** true

if the most recently read SQL value was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- readURL

```java
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

**Returns:** a

java.net.URL

object.
**Throws:** SQLException

- if a database access error occurs,
or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- readNClob

```java
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readNString

```java
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

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readSQLXML

```java
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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readRowId

```java
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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- readObject

```java
default <T> T readObject​(
Class
<T> type)
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the specified
Java data type, and any customizations present in this
stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** type

- Class representing the Java data type to convert the attribute to.
**Returns:** the attribute at the head of the stream as an

Object

in the
Java programming language;

null

if the attribute is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.8

---

#### Method Detail

readString

```java
String
readString()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readString

String

readString()
throws

SQLException

Reads the next attribute in the stream and returns it as a

String

in the Java programming language.

readBoolean

```java
boolean readBoolean()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

false
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readBoolean

boolean readBoolean()
throws

SQLException

Reads the next attribute in the stream and returns it as a

boolean

in the Java programming language.

readByte

```java
byte readByte()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readByte

byte readByte()
throws

SQLException

Reads the next attribute in the stream and returns it as a

byte

in the Java programming language.

readShort

```java
short readShort()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readShort

short readShort()
throws

SQLException

Reads the next attribute in the stream and returns it as a

short

in the Java programming language.

readInt

```java
int readInt()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readInt

int readInt()
throws

SQLException

Reads the next attribute in the stream and returns it as an

int

in the Java programming language.

readLong

```java
long readLong()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readLong

long readLong()
throws

SQLException

Reads the next attribute in the stream and returns it as a

long

in the Java programming language.

readFloat

```java
float readFloat()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readFloat

float readFloat()
throws

SQLException

Reads the next attribute in the stream and returns it as a

float

in the Java programming language.

readDouble

```java
double readDouble()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

0
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readDouble

double readDouble()
throws

SQLException

Reads the next attribute in the stream and returns it as a

double

in the Java programming language.

readBigDecimal

```java
BigDecimal
readBigDecimal()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readBigDecimal

BigDecimal

readBigDecimal()
throws

SQLException

Reads the next attribute in the stream and returns it as a

java.math.BigDecimal

object in the Java programming language.

readBytes

```java
byte[] readBytes()
throws
SQLException
```

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readBytes

byte[] readBytes()
throws

SQLException

Reads the next attribute in the stream and returns it as an array of bytes
in the Java programming language.

readDate

```java
Date
readDate()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readDate

Date

readDate()
throws

SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Date

object.

readTime

```java
Time
readTime()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readTime

Time

readTime()
throws

SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Time

object.

readTimestamp

```java
Timestamp
readTimestamp()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readTimestamp

Timestamp

readTimestamp()
throws

SQLException

Reads the next attribute in the stream and returns it as a

java.sql.Timestamp

object.

readCharacterStream

```java
Reader
readCharacterStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readCharacterStream

Reader

readCharacterStream()
throws

SQLException

Reads the next attribute in the stream and returns it as a stream of Unicode characters.

readAsciiStream

```java
InputStream
readAsciiStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readAsciiStream

InputStream

readAsciiStream()
throws

SQLException

Reads the next attribute in the stream and returns it as a stream of ASCII characters.

readBinaryStream

```java
InputStream
readBinaryStream()
throws
SQLException
```

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readBinaryStream

InputStream

readBinaryStream()
throws

SQLException

Reads the next attribute in the stream and returns it as a stream of uninterpreted
bytes.

readObject

```java
Object
readObject()
throws
SQLException
```

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default type
mapping, and any customizations present in this stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

**Returns:** the datum at the head of the stream as an

Object

in the
Java programming language;

null

if the datum is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readObject

Object

readObject()
throws

SQLException

Reads the datum at the head of the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the default type
mapping, and any customizations present in this stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

When the datum at the head of the stream is an SQL

NULL

,
the method returns

null

. If the datum is an SQL structured or distinct
type, it determines the SQL type of the datum at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

readRef

```java
Ref
readRef()
throws
SQLException
```

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

**Returns:** a

Ref

object representing the SQL

REF

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readRef

Ref

readRef()
throws

SQLException

Reads an SQL

REF

value from the stream and returns it as a

Ref

object in the Java programming language.

readBlob

```java
Blob
readBlob()
throws
SQLException
```

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

**Returns:** a

Blob

object representing data of the SQL

BLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readBlob

Blob

readBlob()
throws

SQLException

Reads an SQL

BLOB

value from the stream and returns it as a

Blob

object in the Java programming language.

readClob

```java
Clob
readClob()
throws
SQLException
```

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

**Returns:** a

Clob

object representing data of the SQL

CLOB

value
at the head of the stream;

null

if the value read is
SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readClob

Clob

readClob()
throws

SQLException

Reads an SQL

CLOB

value from the stream and returns it as a

Clob

object in the Java programming language.

readArray

```java
Array
readArray()
throws
SQLException
```

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

**Returns:** an

Array

object representing data of the SQL

ARRAY

value at the head of the stream;

null

if the value read is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### readArray

Array

readArray()
throws

SQLException

Reads an SQL

ARRAY

value from the stream and returns it as an

Array

object in the Java programming language.

wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last value read was SQL

NULL

.

**Returns:** true

if the most recently read SQL value was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### wasNull

boolean wasNull()
throws

SQLException

Retrieves whether the last value read was SQL

NULL

.

readURL

```java
URL
readURL()
throws
SQLException
```

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

**Returns:** a

java.net.URL

object.
**Throws:** SQLException

- if a database access error occurs,
or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### readURL

URL

readURL()
throws

SQLException

Reads an SQL

DATALINK

value from the stream and returns it as a

java.net.URL

object in the Java programming language.

readNClob

```java
NClob
readNClob()
throws
SQLException
```

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### readNClob

NClob

readNClob()
throws

SQLException

Reads an SQL

NCLOB

value from the stream and returns it as a

NClob

object in the Java programming language.

readNString

```java
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

**Returns:** the attribute; if the value is SQL

NULL

, returns

null
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### readNString

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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### readSQLXML

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
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### readRowId

RowId

readRowId()
throws

SQLException

Reads an SQL

ROWID

value from the stream and returns it as a

RowId

object in the Java programming language.

readObject

```java
default <T> T readObject​(
Class
<T> type)
throws
SQLException
```

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the specified
Java data type, and any customizations present in this
stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** type

- Class representing the Java data type to convert the attribute to.
**Returns:** the attribute at the head of the stream as an

Object

in the
Java programming language;

null

if the attribute is SQL

NULL
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.8

---

#### readObject

default <T> T readObject​(

Class

<T> type)
throws

SQLException

Reads the next attribute in the stream and returns it as an

Object

in the Java programming language. The
actual type of the object returned is determined by the specified
Java data type, and any customizations present in this
stream's type map.

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

A type map is registered with the stream by the JDBC driver before the
stream is passed to the application.

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

When the attribute at the head of the stream is an SQL

NULL

the method returns

null

. If the attribute is an SQL
structured or distinct
type, it determines the SQL type of the attribute at the head of the stream.
If the stream's type map has an entry for that SQL type, the driver
constructs an object of the appropriate class and calls the method

SQLData.readSQL

on that object, which reads additional data from the
stream, using the protocol described for that method.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

---

