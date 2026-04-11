# Interface CallableStatement

**Source:** `java.sql\java\sql\CallableStatement.html`

### Class Description

```java
public interface
CallableStatement

extends
PreparedStatement
```

The interface used to execute SQL stored procedures. The JDBC API
provides a stored procedure SQL escape syntax that allows stored procedures
to be called in a standard way for all RDBMSs. This escape syntax has one
form that includes a result parameter and one that does not. If used, the result
parameter must be registered as an OUT parameter. The other parameters
can be used for input, output or both. Parameters are referred to
sequentially, by number, with the first parameter being 1.

```java
{?= call <procedure-name>[(<arg1>,<arg2>, ...)]}
{call <procedure-name>[(<arg1>,<arg2>, ...)]}
```

IN parameter values are set using the

set

methods inherited from

PreparedStatement

. The type of all OUT parameters must be
registered prior to executing the stored procedure; their values
are retrieved after execution via the

get

methods provided here.

A

CallableStatement

can return one

ResultSet

object or
multiple

ResultSet

objects. Multiple

ResultSet

objects are handled using operations
inherited from

Statement

.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

**All Superinterfaces:** AutoCloseable

,

PreparedStatement

,

Statement

,

Wrapper

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void registerOutParameter​(int parameterIndex,
int sqlType)
throws
SQLException

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type

**See Also:**
- Types

---

#### void registerOutParameter​(int parameterIndex,
int sqlType,
int scale)
throws
SQLException

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- sqlType

- the SQL type code defined by

java.sql.Types

.
- scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type

**See Also:**
- Types

---

#### boolean wasNull()
throws
SQLException

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

. Note that this method should be called only after
calling a getter method; otherwise, there is no value to use in
determining whether it is

null

or not.

**Returns:**
- true

if the last parameter read was SQL

NULL

;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement

---

#### String
getString​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setString(java.lang.String, java.lang.String)

---

#### boolean getBoolean​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

false

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setBoolean(java.lang.String, boolean)

---

#### byte getByte​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setByte(java.lang.String, byte)

---

#### short getShort​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setShort(java.lang.String, short)

---

#### int getInt​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setInt(java.lang.String, int)

---

#### long getLong​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setLong(java.lang.String, long)

---

#### float getFloat​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setFloat(java.lang.String, float)

---

#### double getDouble​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setDouble(java.lang.String, double)

---

#### @Deprecated
(
since
="1.2")

BigDecimal
getBigDecimal​(int parameterIndex,
int scale)
throws
SQLException

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with

scale

digits to
the right of the decimal point.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- scale

- the number of digits to the right of the decimal point

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setBigDecimal(java.lang.String, java.math.BigDecimal)

---

#### byte[] getBytes​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setBytes(java.lang.String, byte[])

---

#### Date
getDate​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setDate(java.lang.String, java.sql.Date)

---

#### Time
getTime​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setTime(java.lang.String, java.sql.Time)

---

#### Timestamp
getTimestamp​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setTimestamp(java.lang.String, java.sql.Timestamp)

---

#### Object
getObject​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated parameter as an

Object

in the Java programming language. If the value is an SQL

NULL

,
the driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- A

java.lang.Object

holding the OUT parameter value

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- Types

,

setObject(java.lang.String, java.lang.Object, int, int)

---

#### BigDecimal
getBigDecimal​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setBigDecimal(java.lang.String, java.math.BigDecimal)

**Since:**
- 1.2

---

#### Object
getObject​(int parameterIndex,

Map
<
String
,​
Class
<?>> map)
throws
SQLException

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and so on
- map

- the mapping from SQL type names to Java classes

**Returns:**
- a

java.lang.Object

holding the OUT parameter value

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setObject(java.lang.String, java.lang.Object, int, int)

**Since:**
- 1.2

---

#### Ref
getRef​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on

**Returns:**
- the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Blob
getBlob​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and so on

**Returns:**
- the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Clob
getClob​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and
so on

**Returns:**
- the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Array
getArray​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and
so on

**Returns:**
- the parameter value as an

Array

object in
the Java programming language. If the value was SQL

NULL

, the
value

null

is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

#### Date
getDate​(int parameterIndex,

Calendar
cal)
throws
SQLException

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- cal

- the

Calendar

object the driver will use
to construct the date

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setDate(java.lang.String, java.sql.Date)

**Since:**
- 1.2

---

#### Time
getTime​(int parameterIndex,

Calendar
cal)
throws
SQLException

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- cal

- the

Calendar

object the driver will use
to construct the time

**Returns:**
- the parameter value; if the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setTime(java.lang.String, java.sql.Time)

**Since:**
- 1.2

---

#### Timestamp
getTimestamp​(int parameterIndex,

Calendar
cal)
throws
SQLException

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- cal

- the

Calendar

object the driver will use
to construct the timestamp

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement

**See Also:**
- setTimestamp(java.lang.String, java.sql.Timestamp)

**Since:**
- 1.2

---

#### void registerOutParameter​(int parameterIndex,
int sqlType,

String
typeName)
throws
SQLException

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter. Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,...
- sqlType

- a value from

Types
- typeName

- the fully-qualified name of an SQL structured type

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type

**See Also:**
- Types

**Since:**
- 1.2

---

#### void registerOutParameter​(
String
parameterName,
int sqlType)
throws
SQLException

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method

**See Also:**
- Types

**Since:**
- 1.4

---

#### void registerOutParameter​(
String
parameterName,
int sqlType,
int scale)
throws
SQLException

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- SQL type code defined by

java.sql.Types

.
- scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method

**See Also:**
- Types

**Since:**
- 1.4

---

#### void registerOutParameter​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- a value from

Types
- typeName

- the fully-qualified name of an SQL structured type

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method

**See Also:**
- Types

**Since:**
- 1.4

---

#### URL
getURL​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,...

**Returns:**
- a

java.net.URL

object that represents the
JDBC

DATALINK

value used as the designated
parameter

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if the URL being returned is
not a valid URL on the Java platform
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setURL(java.lang.String, java.net.URL)

**Since:**
- 1.4

---

#### void setURL​(
String
parameterName,

URL
val)
throws
SQLException

Sets the designated parameter to the given

java.net.URL

object.
The driver converts this to an SQL

DATALINK

value when
it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- val

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or if a URL is malformed
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getURL(int)

**Since:**
- 1.4

---

#### void setNull​(
String
parameterName,
int sqlType)
throws
SQLException

Sets the designated parameter to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- the SQL type code defined in

java.sql.Types

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setBoolean​(
String
parameterName,
boolean x)
throws
SQLException

Sets the designated parameter to the given Java

boolean

value.
The driver converts this
to an SQL

BIT

or

BOOLEAN

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getBoolean(int)

**Since:**
- 1.4

---

#### void setByte​(
String
parameterName,
byte x)
throws
SQLException

Sets the designated parameter to the given Java

byte

value.
The driver converts this
to an SQL

TINYINT

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getByte(int)

**Since:**
- 1.4

---

#### void setShort​(
String
parameterName,
short x)
throws
SQLException

Sets the designated parameter to the given Java

short

value.
The driver converts this
to an SQL

SMALLINT

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getShort(int)

**Since:**
- 1.4

---

#### void setInt​(
String
parameterName,
int x)
throws
SQLException

Sets the designated parameter to the given Java

int

value.
The driver converts this
to an SQL

INTEGER

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getInt(int)

**Since:**
- 1.4

---

#### void setLong​(
String
parameterName,
long x)
throws
SQLException

Sets the designated parameter to the given Java

long

value.
The driver converts this
to an SQL

BIGINT

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getLong(int)

**Since:**
- 1.4

---

#### void setFloat​(
String
parameterName,
float x)
throws
SQLException

Sets the designated parameter to the given Java

float

value.
The driver converts this
to an SQL

FLOAT

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getFloat(int)

**Since:**
- 1.4

---

#### void setDouble​(
String
parameterName,
double x)
throws
SQLException

Sets the designated parameter to the given Java

double

value.
The driver converts this
to an SQL

DOUBLE

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getDouble(int)

**Since:**
- 1.4

---

#### void setBigDecimal​(
String
parameterName,

BigDecimal
x)
throws
SQLException

Sets the designated parameter to the given

java.math.BigDecimal

value.
The driver converts this to an SQL

NUMERIC

value when
it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getBigDecimal(int, int)

**Since:**
- 1.4

---

#### void setString​(
String
parameterName,

String
x)
throws
SQLException

Sets the designated parameter to the given Java

String

value.
The driver converts this
to an SQL

VARCHAR

or

LONGVARCHAR

value
(depending on the argument's
size relative to the driver's limits on

VARCHAR

values)
when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getString(int)

**Since:**
- 1.4

---

#### void setBytes​(
String
parameterName,
byte[] x)
throws
SQLException

Sets the designated parameter to the given Java array of bytes.
The driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

(depending on the argument's size relative
to the driver's limits on

VARBINARY

values) when it sends
it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getBytes(int)

**Since:**
- 1.4

---

#### void setDate​(
String
parameterName,

Date
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.
The driver converts this
to an SQL

DATE

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getDate(int)

**Since:**
- 1.4

---

#### void setTime​(
String
parameterName,

Time
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.Time

value.
The driver converts this
to an SQL

TIME

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getTime(int)

**Since:**
- 1.4

---

#### void setTimestamp​(
String
parameterName,

Timestamp
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.Timestamp

value.
The driver
converts this to an SQL

TIMESTAMP

value when it sends it to the
database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getTimestamp(int)

**Since:**
- 1.4

---

#### void setAsciiStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the Java input stream that contains the ASCII parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setBinaryStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the java input stream which contains the binary parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setObject​(
String
parameterName,

Object
x,
int targetSqlType,
int scale)
throws
SQLException

Sets the value of the designated parameter with the given object.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database. The scale argument may further qualify this type.
- scale

- for java.sql.Types.DECIMAL or java.sql.Types.NUMERIC types,
this is the number of digits after the decimal point. For all other
types, this value will be ignored.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType

**See Also:**
- Types

,

getObject(int)

**Since:**
- 1.4

---

#### void setObject​(
String
parameterName,

Object
x,
int targetSqlType)
throws
SQLException

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, int targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType

**See Also:**
- getObject(int)

**Since:**
- 1.4

---

#### void setObject​(
String
parameterName,

Object
x)
throws
SQLException

Sets the value of the designated parameter with the given object.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getObject(int)

**Since:**
- 1.4

---

#### void setCharacterStream​(
String
parameterName,

Reader
reader,
int length)
throws
SQLException

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
- length

- the number of characters in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setDate​(
String
parameterName,

Date
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

DATE

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the date
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value
- cal

- the

Calendar

object the driver will use
to construct the date

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getDate(int)

**Since:**
- 1.4

---

#### void setTime​(
String
parameterName,

Time
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIME

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the time
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value
- cal

- the

Calendar

object the driver will use
to construct the time

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getTime(int)

**Since:**
- 1.4

---

#### void setTimestamp​(
String
parameterName,

Timestamp
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIMESTAMP

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the timestamp
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value
- cal

- the

Calendar

object the driver will use
to construct the timestamp

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- getTimestamp(int)

**Since:**
- 1.4

---

#### void setNull​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException

Sets the designated parameter to SQL

NULL

.
This version of the method

setNull

should
be used for user-defined types and REF type parameters. Examples
of user-defined types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- a value from

java.sql.Types
- typeName

- the fully-qualified name of an SQL user-defined type;
ignored if the parameter is not a user-defined type or
SQL

REF

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### String
getString​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setString(java.lang.String, java.lang.String)

**Since:**
- 1.4

---

#### boolean getBoolean​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

false

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setBoolean(java.lang.String, boolean)

**Since:**
- 1.4

---

#### byte getByte​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setByte(java.lang.String, byte)

**Since:**
- 1.4

---

#### short getShort​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setShort(java.lang.String, short)

**Since:**
- 1.4

---

#### int getInt​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setInt(java.lang.String, int)

**Since:**
- 1.4

---

#### long getLong​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setLong(java.lang.String, long)

**Since:**
- 1.4

---

#### float getFloat​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setFloat(java.lang.String, float)

**Since:**
- 1.4

---

#### double getDouble​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

0

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setDouble(java.lang.String, double)

**Since:**
- 1.4

---

#### byte[] getBytes​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setBytes(java.lang.String, byte[])

**Since:**
- 1.4

---

#### Date
getDate​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setDate(java.lang.String, java.sql.Date)

**Since:**
- 1.4

---

#### Time
getTime​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setTime(java.lang.String, java.sql.Time)

**Since:**
- 1.4

---

#### Timestamp
getTimestamp​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result
is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setTimestamp(java.lang.String, java.sql.Timestamp)

**Since:**
- 1.4

---

#### Object
getObject​(
String
parameterName)
throws
SQLException

Retrieves the value of a parameter as an

Object

in the Java
programming language. If the value is an SQL

NULL

, the
driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- A

java.lang.Object

holding the OUT parameter value.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- Types

,

setObject(java.lang.String, java.lang.Object, int, int)

**Since:**
- 1.4

---

#### BigDecimal
getBigDecimal​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setBigDecimal(java.lang.String, java.math.BigDecimal)

**Since:**
- 1.4

---

#### Object
getObject​(
String
parameterName,

Map
<
String
,​
Class
<?>> map)
throws
SQLException

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:**
- parameterName

- the name of the parameter
- map

- the mapping from SQL type names to Java classes

**Returns:**
- a

java.lang.Object

holding the OUT parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setObject(java.lang.String, java.lang.Object, int, int)

**Since:**
- 1.4

---

#### Ref
getRef​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### Blob
getBlob​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### Clob
getClob​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### Array
getArray​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as an

Array

object in
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### Date
getDate​(
String
parameterName,

Calendar
cal)
throws
SQLException

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterName

- the name of the parameter
- cal

- the

Calendar

object the driver will use
to construct the date

**Returns:**
- the parameter value. If the value is SQL

NULL

,
the result is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setDate(java.lang.String, java.sql.Date)

**Since:**
- 1.4

---

#### Time
getTime​(
String
parameterName,

Calendar
cal)
throws
SQLException

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterName

- the name of the parameter
- cal

- the

Calendar

object the driver will use
to construct the time

**Returns:**
- the parameter value; if the value is SQL

NULL

, the result is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setTime(java.lang.String, java.sql.Time)

**Since:**
- 1.4

---

#### Timestamp
getTimestamp​(
String
parameterName,

Calendar
cal)
throws
SQLException

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:**
- parameterName

- the name of the parameter
- cal

- the

Calendar

object the driver will use
to construct the timestamp

**Returns:**
- the parameter value. If the value is SQL

NULL

, the result is

null

.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setTimestamp(java.lang.String, java.sql.Timestamp)

**Since:**
- 1.4

---

#### URL
getURL​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as a

java.net.URL

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if there is a problem with the URL
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setURL(java.lang.String, java.net.URL)

**Since:**
- 1.4

---

#### RowId
getRowId​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,...

**Returns:**
- a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### RowId
getRowId​(
String
parameterName)
throws
SQLException

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setRowId​(
String
parameterName,

RowId
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

when it sends it to the
database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setNString​(
String
parameterName,

String
value)
throws
SQLException

Sets the designated parameter to the given

String

object.
The driver converts this to a SQL

NCHAR

or

NVARCHAR

or

LONGNVARCHAR

**Parameters:**
- parameterName

- the name of the parameter to be set
- value

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setNCharacterStream​(
String
parameterName,

Reader
value,
long length)
throws
SQLException

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

**Parameters:**
- parameterName

- the name of the parameter to be set
- value

- the parameter value
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setNClob​(
String
parameterName,

NClob
value)
throws
SQLException

Sets the designated parameter to a

java.sql.NClob

object. The object
implements the

java.sql.NClob

interface. This

NClob

object maps to a SQL

NCLOB

.

**Parameters:**
- parameterName

- the name of the parameter to be set
- value

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:**
- parameterName

- the name of the parameter to be set
- reader

- An object that contains the data to set the parameter value to.
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setBlob​(
String
parameterName,

InputStream
inputStream,
long length)
throws
SQLException

Sets the designated parameter to an

InputStream

object.
The

Inputstream

must contain the number
of characters specified by length, otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setBinaryStream (int, InputStream, int)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

**Parameters:**
- parameterName

- the name of the parameter to be set
the second is 2, ...
- inputStream

- An object that contains the data to set the parameter
value to.
- length

- the number of bytes in the parameter data.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match the specified length; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setNClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:**
- parameterName

- the name of the parameter to be set
- reader

- An object that contains the data to set the parameter value to.
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### NClob
getNClob​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and
so on

**Returns:**
- the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### NClob
getNClob​(
String
parameterName)
throws
SQLException

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setSQLXML​(
String
parameterName,

SQLXML
xmlObject)
throws
SQLException

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an

SQL XML

value when it sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- xmlObject

- a

SQLXML

object that maps an

SQL XML

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed for the

SQLXML

object
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### SQLXML
getSQLXML​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...

**Returns:**
- a

SQLXML

object that maps an

SQL XML

value

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### SQLXML
getSQLXML​(
String
parameterName)
throws
SQLException

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- a

SQLXML

object that maps an

SQL XML

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### String
getNString​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...

**Returns:**
- a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setNString(java.lang.String, java.lang.String)

**Since:**
- 1.6

---

#### String
getNString​(
String
parameterName)
throws
SQLException

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- setNString(java.lang.String, java.lang.String)

**Since:**
- 1.6

---

#### Reader
getNCharacterStream​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...

**Returns:**
- a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### Reader
getNCharacterStream​(
String
parameterName)
throws
SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### Reader
getCharacterStream​(int parameterIndex)
throws
SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...

**Returns:**
- a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.

**Throws:**
- SQLException

- if the parameterIndex is not valid; if a database access error occurs or
this method is called on a closed

CallableStatement

**Since:**
- 1.6

---

#### Reader
getCharacterStream​(
String
parameterName)
throws
SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:**
- parameterName

- the name of the parameter

**Returns:**
- a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setBlob​(
String
parameterName,

Blob
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.Blob

object.
The driver converts this to an SQL

BLOB

value when it
sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- a

Blob

object that maps an SQL

BLOB

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setClob​(
String
parameterName,

Clob
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.Clob

object.
The driver converts this to an SQL

CLOB

value when it
sends it to the database.

**Parameters:**
- parameterName

- the name of the parameter
- x

- a

Clob

object that maps an SQL

CLOB

value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setAsciiStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the Java input stream that contains the ASCII parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setBinaryStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the java input stream which contains the binary parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setCharacterStream​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterName

- the name of the parameter
- reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
- length

- the number of characters in the stream

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.6

---

#### void setAsciiStream​(
String
parameterName,

InputStream
x)
throws
SQLException

Sets the designated parameter to the given input stream.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the Java input stream that contains the ASCII parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setBinaryStream​(
String
parameterName,

InputStream
x)
throws
SQLException

Sets the designated parameter to the given input stream.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the
stream as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- x

- the java input stream which contains the binary parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setCharacterStream​(
String
parameterName,

Reader
reader)
throws
SQLException

Sets the designated parameter to the given

Reader

object.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- reader

- the

java.io.Reader

object that contains the
Unicode data

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setNCharacterStream​(
String
parameterName,

Reader
value)
throws
SQLException

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- value

- the parameter value

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs; or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setClob​(
String
parameterName,

Reader
reader)
throws
SQLException

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- reader

- An object that contains the data to set the parameter value to.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or this method is called on
a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setBlob​(
String
parameterName,

InputStream
inputStream)
throws
SQLException

Sets the designated parameter to an

InputStream

object.
This method differs from the

setBinaryStream (int, InputStream)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- inputStream

- An object that contains the data to set the parameter
value to.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setNClob​(
String
parameterName,

Reader
reader)
throws
SQLException

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:**
- parameterName

- the name of the parameter
- reader

- An object that contains the data to set the parameter value to.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### <T> T getObject​(int parameterIndex,

Class
<T> type)
throws
SQLException

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, and so on
- type

- Class representing the Java data type to convert the
designated parameter to.

**Returns:**
- an instance of

type

holding the OUT parameter value

**Throws:**
- SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.7

**Type Parameters:**
- T

- the type of the class modeled by this Class object

---

#### <T> T getObject​(
String
parameterName,

Class
<T> type)
throws
SQLException

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Parameters:**
- parameterName

- the name of the parameter
- type

- Class representing the Java data type to convert
the designated parameter to.

**Returns:**
- an instance of

type

holding the OUT parameter
value

**Throws:**
- SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.7

**Type Parameters:**
- T

- the type of the class modeled by this Class object

---

#### default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType,
int scaleOrLength)
throws
SQLException

Sets the value of the designated parameter with the given object.

If the second argument is an

InputStream

then the stream
must contain the number of bytes specified by scaleOrLength.
If the second argument is a

Reader

then the reader must
contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver
will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type to be
sent to the database. The scale argument may further qualify this type.
- scaleOrLength

- for

java.sql.JDBCType.DECIMAL

or

java.sql.JDBCType.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or reader. For all other types,
this value will be ignored.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement

or
if the Java Object specified by x is an InputStream
or Reader object and the value of the scale parameter is less
than zero
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType)
throws
SQLException

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, SQLType targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type to be sent to the database

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(int parameterIndex,

SQLType
sqlType)
throws
SQLException

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,
int scale)
throws
SQLException

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,
and so on
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
- scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,

String
typeName)
throws
SQLException

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter.
Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2,...
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
- typeName

- the fully-qualified name of an SQL structured type

**Throws:**
- SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(
String
parameterName,

SQLType
sqlType)
throws
SQLException

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,
int scale)
throws
SQLException

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
- scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

#### default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,

String
typeName)
throws
SQLException

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:**
- parameterName

- the name of the parameter
- sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
- typeName

- the fully-qualified name of an SQL structured type

**Throws:**
- SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support this method

**See Also:**
- JDBCType

,

SQLType

**Since:**
- 1.8

---

### Additional Sections

#### Interface CallableStatement

**All Superinterfaces:** AutoCloseable

,

PreparedStatement

,

Statement

,

Wrapper

```java
public interface
CallableStatement

extends
PreparedStatement
```

The interface used to execute SQL stored procedures. The JDBC API
provides a stored procedure SQL escape syntax that allows stored procedures
to be called in a standard way for all RDBMSs. This escape syntax has one
form that includes a result parameter and one that does not. If used, the result
parameter must be registered as an OUT parameter. The other parameters
can be used for input, output or both. Parameters are referred to
sequentially, by number, with the first parameter being 1.

```java
{?= call <procedure-name>[(<arg1>,<arg2>, ...)]}
{call <procedure-name>[(<arg1>,<arg2>, ...)]}
```

IN parameter values are set using the

set

methods inherited from

PreparedStatement

. The type of all OUT parameters must be
registered prior to executing the stored procedure; their values
are retrieved after execution via the

get

methods provided here.

A

CallableStatement

can return one

ResultSet

object or
multiple

ResultSet

objects. Multiple

ResultSet

objects are handled using operations
inherited from

Statement

.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

**Since:** 1.1
**See Also:** Connection.prepareCall(java.lang.String)

,

ResultSet

public interface

CallableStatement

extends

PreparedStatement

The interface used to execute SQL stored procedures. The JDBC API
provides a stored procedure SQL escape syntax that allows stored procedures
to be called in a standard way for all RDBMSs. This escape syntax has one
form that includes a result parameter and one that does not. If used, the result
parameter must be registered as an OUT parameter. The other parameters
can be used for input, output or both. Parameters are referred to
sequentially, by number, with the first parameter being 1.

```java
{?= call <procedure-name>[(<arg1>,<arg2>, ...)]}
{call <procedure-name>[(<arg1>,<arg2>, ...)]}
```

IN parameter values are set using the

set

methods inherited from

PreparedStatement

. The type of all OUT parameters must be
registered prior to executing the stored procedure; their values
are retrieved after execution via the

get

methods provided here.

A

CallableStatement

can return one

ResultSet

object or
multiple

ResultSet

objects. Multiple

ResultSet

objects are handled using operations
inherited from

Statement

.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

{?= call <procedure-name>[(<arg1>,<arg2>, ...)]}
{call <procedure-name>[(<arg1>,<arg2>, ...)]}

IN parameter values are set using the

set

methods inherited from

PreparedStatement

. The type of all OUT parameters must be
registered prior to executing the stored procedure; their values
are retrieved after execution via the

get

methods provided here.

A

CallableStatement

can return one

ResultSet

object or
multiple

ResultSet

objects. Multiple

ResultSet

objects are handled using operations
inherited from

Statement

.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

A

CallableStatement

can return one

ResultSet

object or
multiple

ResultSet

objects. Multiple

ResultSet

objects are handled using operations
inherited from

Statement

.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

For maximum portability, a call's

ResultSet

objects and
update counts should be processed prior to getting the values of output
parameters.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.sql.

Statement

CLOSE_ALL_RESULTS

,

CLOSE_CURRENT_RESULT

,

EXECUTE_FAILED

,

KEEP_CURRENT_RESULT

,

NO_GENERATED_KEYS

,

RETURN_GENERATED_KEYS

,

SUCCESS_NO_INFO

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

Array

getArray

​(int parameterIndex)

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

Array

getArray

​(

String

parameterName)

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

BigDecimal

getBigDecimal

​(int parameterIndex)

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

BigDecimal

getBigDecimal

​(int parameterIndex,
int scale)

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

BigDecimal

getBigDecimal

​(

String

parameterName)

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

Blob

getBlob

​(int parameterIndex)

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

Blob

getBlob

​(

String

parameterName)

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

boolean

getBoolean

​(int parameterIndex)

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

boolean

getBoolean

​(

String

parameterName)

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

byte

getByte

​(int parameterIndex)

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

byte

getByte

​(

String

parameterName)

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

byte[]

getBytes

​(int parameterIndex)

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

byte[]

getBytes

​(

String

parameterName)

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

Reader

getCharacterStream

​(int parameterIndex)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Reader

getCharacterStream

​(

String

parameterName)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Clob

getClob

​(int parameterIndex)

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Clob

getClob

​(

String

parameterName)

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Date

getDate

​(int parameterIndex)

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

Date

getDate

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

Date

getDate

​(

String

parameterName)

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

Date

getDate

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

double

getDouble

​(int parameterIndex)

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

double

getDouble

​(

String

parameterName)

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

float

getFloat

​(int parameterIndex)

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

float

getFloat

​(

String

parameterName)

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

int

getInt

​(int parameterIndex)

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

int

getInt

​(

String

parameterName)

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

long

getLong

​(int parameterIndex)

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

long

getLong

​(

String

parameterName)

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

Reader

getNCharacterStream

​(int parameterIndex)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Reader

getNCharacterStream

​(

String

parameterName)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

NClob

getNClob

​(int parameterIndex)

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

NClob

getNClob

​(

String

parameterName)

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

String

getNString

​(int parameterIndex)

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

String

getNString

​(

String

parameterName)

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

Object

getObject

​(int parameterIndex)

Retrieves the value of the designated parameter as an

Object

in the Java programming language.

<T> T

getObject

​(int parameterIndex,

Class

<T> type)

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Object

getObject

​(int parameterIndex,

Map

<

String

,​

Class

<?>> map)

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

Object

getObject

​(

String

parameterName)

Retrieves the value of a parameter as an

Object

in the Java
programming language.

<T> T

getObject

​(

String

parameterName,

Class

<T> type)

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Object

getObject

​(

String

parameterName,

Map

<

String

,​

Class

<?>> map)

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

Ref

getRef

​(int parameterIndex)

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

Ref

getRef

​(

String

parameterName)

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

RowId

getRowId

​(int parameterIndex)

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

RowId

getRowId

​(

String

parameterName)

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

short

getShort

​(int parameterIndex)

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

short

getShort

​(

String

parameterName)

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

SQLXML

getSQLXML

​(int parameterIndex)

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

SQLXML

getSQLXML

​(

String

parameterName)

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

String

getString

​(int parameterIndex)

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

String

getString

​(

String

parameterName)

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

Time

getTime

​(int parameterIndex)

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

Time

getTime

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Time

getTime

​(

String

parameterName)

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

Time

getTime

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Timestamp

getTimestamp

​(int parameterIndex)

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Timestamp

getTimestamp

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

Timestamp

getTimestamp

​(

String

parameterName)

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Timestamp

getTimestamp

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

URL

getURL

​(int parameterIndex)

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

URL

getURL

​(

String

parameterName)

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

void

registerOutParameter

​(int parameterIndex,
int sqlType)

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

.

void

registerOutParameter

​(int parameterIndex,
int sqlType,
int scale)

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

.

void

registerOutParameter

​(int parameterIndex,
int sqlType,

String

typeName)

Registers the designated output parameter.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType)

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType,
int scale)

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType,

String

typeName)

Registers the designated output parameter.

void

registerOutParameter

​(

String

parameterName,
int sqlType)

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

.

void

registerOutParameter

​(

String

parameterName,
int sqlType,
int scale)

Registers the parameter named

parameterName

to be of JDBC type

sqlType

.

void

registerOutParameter

​(

String

parameterName,
int sqlType,

String

typeName)

Registers the designated output parameter.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType)

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType,
int scale)

Registers the parameter named

parameterName

to be of JDBC type

sqlType

.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType,

String

typeName)

Registers the designated output parameter.

void

setAsciiStream

​(

String

parameterName,

InputStream

x)

Sets the designated parameter to the given input stream.

void

setAsciiStream

​(

String

parameterName,

InputStream

x,
int length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setAsciiStream

​(

String

parameterName,

InputStream

x,
long length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBigDecimal

​(

String

parameterName,

BigDecimal

x)

Sets the designated parameter to the given

java.math.BigDecimal

value.

void

setBinaryStream

​(

String

parameterName,

InputStream

x)

Sets the designated parameter to the given input stream.

void

setBinaryStream

​(

String

parameterName,

InputStream

x,
int length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBinaryStream

​(

String

parameterName,

InputStream

x,
long length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBlob

​(

String

parameterName,

InputStream

inputStream)

Sets the designated parameter to an

InputStream

object.

void

setBlob

​(

String

parameterName,

InputStream

inputStream,
long length)

Sets the designated parameter to an

InputStream

object.

void

setBlob

​(

String

parameterName,

Blob

x)

Sets the designated parameter to the given

java.sql.Blob

object.

void

setBoolean

​(

String

parameterName,
boolean x)

Sets the designated parameter to the given Java

boolean

value.

void

setByte

​(

String

parameterName,
byte x)

Sets the designated parameter to the given Java

byte

value.

void

setBytes

​(

String

parameterName,
byte[] x)

Sets the designated parameter to the given Java array of bytes.

void

setCharacterStream

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to the given

Reader

object.

void

setCharacterStream

​(

String

parameterName,

Reader

reader,
int length)

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

void

setCharacterStream

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

void

setClob

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setClob

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setClob

​(

String

parameterName,

Clob

x)

Sets the designated parameter to the given

java.sql.Clob

object.

void

setDate

​(

String

parameterName,

Date

x)

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.

void

setDate

​(

String

parameterName,

Date

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object.

void

setDouble

​(

String

parameterName,
double x)

Sets the designated parameter to the given Java

double

value.

void

setFloat

​(

String

parameterName,
float x)

Sets the designated parameter to the given Java

float

value.

void

setInt

​(

String

parameterName,
int x)

Sets the designated parameter to the given Java

int

value.

void

setLong

​(

String

parameterName,
long x)

Sets the designated parameter to the given Java

long

value.

void

setNCharacterStream

​(

String

parameterName,

Reader

value)

Sets the designated parameter to a

Reader

object.

void

setNCharacterStream

​(

String

parameterName,

Reader

value,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

NClob

value)

Sets the designated parameter to a

java.sql.NClob

object.

void

setNString

​(

String

parameterName,

String

value)

Sets the designated parameter to the given

String

object.

void

setNull

​(

String

parameterName,
int sqlType)

Sets the designated parameter to SQL

NULL

.

void

setNull

​(

String

parameterName,
int sqlType,

String

typeName)

Sets the designated parameter to SQL

NULL

.

void

setObject

​(

String

parameterName,

Object

x)

Sets the value of the designated parameter with the given object.

void

setObject

​(

String

parameterName,

Object

x,
int targetSqlType)

Sets the value of the designated parameter with the given object.

void

setObject

​(

String

parameterName,

Object

x,
int targetSqlType,
int scale)

Sets the value of the designated parameter with the given object.

default void

setObject

​(

String

parameterName,

Object

x,

SQLType

targetSqlType)

Sets the value of the designated parameter with the given object.

default void

setObject

​(

String

parameterName,

Object

x,

SQLType

targetSqlType,
int scaleOrLength)

Sets the value of the designated parameter with the given object.

void

setRowId

​(

String

parameterName,

RowId

x)

Sets the designated parameter to the given

java.sql.RowId

object.

void

setShort

​(

String

parameterName,
short x)

Sets the designated parameter to the given Java

short

value.

void

setSQLXML

​(

String

parameterName,

SQLXML

xmlObject)

Sets the designated parameter to the given

java.sql.SQLXML

object.

void

setString

​(

String

parameterName,

String

x)

Sets the designated parameter to the given Java

String

value.

void

setTime

​(

String

parameterName,

Time

x)

Sets the designated parameter to the given

java.sql.Time

value.

void

setTime

​(

String

parameterName,

Time

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object.

void

setTimestamp

​(

String

parameterName,

Timestamp

x)

Sets the designated parameter to the given

java.sql.Timestamp

value.

void

setTimestamp

​(

String

parameterName,

Timestamp

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object.

void

setURL

​(

String

parameterName,

URL

val)

Sets the designated parameter to the given

java.net.URL

object.

boolean

wasNull

()

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

.

- Methods declared in interface java.sql.

PreparedStatement

addBatch

,

clearParameters

,

execute

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

getMetaData

,

getParameterMetaData

,

setArray

,

setAsciiStream

,

setAsciiStream

,

setAsciiStream

,

setBigDecimal

,

setBinaryStream

,

setBinaryStream

,

setBinaryStream

,

setBlob

,

setBlob

,

setBlob

,

setBoolean

,

setByte

,

setBytes

,

setCharacterStream

,

setCharacterStream

,

setCharacterStream

,

setClob

,

setClob

,

setClob

,

setDate

,

setDate

,

setDouble

,

setFloat

,

setInt

,

setLong

,

setNCharacterStream

,

setNCharacterStream

,

setNClob

,

setNClob

,

setNClob

,

setNString

,

setNull

,

setNull

,

setObject

,

setObject

,

setObject

,

setObject

,

setObject

,

setRef

,

setRowId

,

setShort

,

setSQLXML

,

setString

,

setTime

,

setTime

,

setTimestamp

,

setTimestamp

,

setUnicodeStream

,

setURL

- Methods declared in interface java.sql.

Statement

addBatch

,

cancel

,

clearBatch

,

clearWarnings

,

close

,

closeOnCompletion

,

enquoteIdentifier

,

enquoteLiteral

,

enquoteNCharLiteral

,

execute

,

execute

,

execute

,

execute

,

executeBatch

,

executeLargeBatch

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

getConnection

,

getFetchDirection

,

getFetchSize

,

getGeneratedKeys

,

getLargeMaxRows

,

getLargeUpdateCount

,

getMaxFieldSize

,

getMaxRows

,

getMoreResults

,

getMoreResults

,

getQueryTimeout

,

getResultSet

,

getResultSetConcurrency

,

getResultSetHoldability

,

getResultSetType

,

getUpdateCount

,

getWarnings

,

isClosed

,

isCloseOnCompletion

,

isPoolable

,

isSimpleIdentifier

,

setCursorName

,

setEscapeProcessing

,

setFetchDirection

,

setFetchSize

,

setLargeMaxRows

,

setMaxFieldSize

,

setMaxRows

,

setPoolable

,

setQueryTimeout

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

Field Summary

- Fields declared in interface java.sql.

Statement

CLOSE_ALL_RESULTS

,

CLOSE_CURRENT_RESULT

,

EXECUTE_FAILED

,

KEEP_CURRENT_RESULT

,

NO_GENERATED_KEYS

,

RETURN_GENERATED_KEYS

,

SUCCESS_NO_INFO

---

#### Field Summary

Fields declared in interface java.sql.

Statement

CLOSE_ALL_RESULTS

,

CLOSE_CURRENT_RESULT

,

EXECUTE_FAILED

,

KEEP_CURRENT_RESULT

,

NO_GENERATED_KEYS

,

RETURN_GENERATED_KEYS

,

SUCCESS_NO_INFO

---

#### Fields declared in interface java.sql. Statement

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Deprecated Methods

Modifier and Type

Method

Description

Array

getArray

​(int parameterIndex)

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

Array

getArray

​(

String

parameterName)

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

BigDecimal

getBigDecimal

​(int parameterIndex)

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

BigDecimal

getBigDecimal

​(int parameterIndex,
int scale)

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

BigDecimal

getBigDecimal

​(

String

parameterName)

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

Blob

getBlob

​(int parameterIndex)

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

Blob

getBlob

​(

String

parameterName)

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

boolean

getBoolean

​(int parameterIndex)

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

boolean

getBoolean

​(

String

parameterName)

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

byte

getByte

​(int parameterIndex)

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

byte

getByte

​(

String

parameterName)

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

byte[]

getBytes

​(int parameterIndex)

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

byte[]

getBytes

​(

String

parameterName)

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

Reader

getCharacterStream

​(int parameterIndex)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Reader

getCharacterStream

​(

String

parameterName)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Clob

getClob

​(int parameterIndex)

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Clob

getClob

​(

String

parameterName)

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Date

getDate

​(int parameterIndex)

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

Date

getDate

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

Date

getDate

​(

String

parameterName)

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

Date

getDate

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

double

getDouble

​(int parameterIndex)

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

double

getDouble

​(

String

parameterName)

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

float

getFloat

​(int parameterIndex)

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

float

getFloat

​(

String

parameterName)

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

int

getInt

​(int parameterIndex)

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

int

getInt

​(

String

parameterName)

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

long

getLong

​(int parameterIndex)

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

long

getLong

​(

String

parameterName)

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

Reader

getNCharacterStream

​(int parameterIndex)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Reader

getNCharacterStream

​(

String

parameterName)

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

NClob

getNClob

​(int parameterIndex)

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

NClob

getNClob

​(

String

parameterName)

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

String

getNString

​(int parameterIndex)

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

String

getNString

​(

String

parameterName)

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

Object

getObject

​(int parameterIndex)

Retrieves the value of the designated parameter as an

Object

in the Java programming language.

<T> T

getObject

​(int parameterIndex,

Class

<T> type)

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Object

getObject

​(int parameterIndex,

Map

<

String

,​

Class

<?>> map)

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

Object

getObject

​(

String

parameterName)

Retrieves the value of a parameter as an

Object

in the Java
programming language.

<T> T

getObject

​(

String

parameterName,

Class

<T> type)

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Object

getObject

​(

String

parameterName,

Map

<

String

,​

Class

<?>> map)

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

Ref

getRef

​(int parameterIndex)

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

Ref

getRef

​(

String

parameterName)

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

RowId

getRowId

​(int parameterIndex)

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

RowId

getRowId

​(

String

parameterName)

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

short

getShort

​(int parameterIndex)

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

short

getShort

​(

String

parameterName)

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

SQLXML

getSQLXML

​(int parameterIndex)

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

SQLXML

getSQLXML

​(

String

parameterName)

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

String

getString

​(int parameterIndex)

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

String

getString

​(

String

parameterName)

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

Time

getTime

​(int parameterIndex)

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

Time

getTime

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Time

getTime

​(

String

parameterName)

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

Time

getTime

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Timestamp

getTimestamp

​(int parameterIndex)

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Timestamp

getTimestamp

​(int parameterIndex,

Calendar

cal)

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

Timestamp

getTimestamp

​(

String

parameterName)

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Timestamp

getTimestamp

​(

String

parameterName,

Calendar

cal)

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

URL

getURL

​(int parameterIndex)

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

URL

getURL

​(

String

parameterName)

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

void

registerOutParameter

​(int parameterIndex,
int sqlType)

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

.

void

registerOutParameter

​(int parameterIndex,
int sqlType,
int scale)

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

.

void

registerOutParameter

​(int parameterIndex,
int sqlType,

String

typeName)

Registers the designated output parameter.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType)

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType,
int scale)

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

.

default void

registerOutParameter

​(int parameterIndex,

SQLType

sqlType,

String

typeName)

Registers the designated output parameter.

void

registerOutParameter

​(

String

parameterName,
int sqlType)

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

.

void

registerOutParameter

​(

String

parameterName,
int sqlType,
int scale)

Registers the parameter named

parameterName

to be of JDBC type

sqlType

.

void

registerOutParameter

​(

String

parameterName,
int sqlType,

String

typeName)

Registers the designated output parameter.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType)

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType,
int scale)

Registers the parameter named

parameterName

to be of JDBC type

sqlType

.

default void

registerOutParameter

​(

String

parameterName,

SQLType

sqlType,

String

typeName)

Registers the designated output parameter.

void

setAsciiStream

​(

String

parameterName,

InputStream

x)

Sets the designated parameter to the given input stream.

void

setAsciiStream

​(

String

parameterName,

InputStream

x,
int length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setAsciiStream

​(

String

parameterName,

InputStream

x,
long length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBigDecimal

​(

String

parameterName,

BigDecimal

x)

Sets the designated parameter to the given

java.math.BigDecimal

value.

void

setBinaryStream

​(

String

parameterName,

InputStream

x)

Sets the designated parameter to the given input stream.

void

setBinaryStream

​(

String

parameterName,

InputStream

x,
int length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBinaryStream

​(

String

parameterName,

InputStream

x,
long length)

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

void

setBlob

​(

String

parameterName,

InputStream

inputStream)

Sets the designated parameter to an

InputStream

object.

void

setBlob

​(

String

parameterName,

InputStream

inputStream,
long length)

Sets the designated parameter to an

InputStream

object.

void

setBlob

​(

String

parameterName,

Blob

x)

Sets the designated parameter to the given

java.sql.Blob

object.

void

setBoolean

​(

String

parameterName,
boolean x)

Sets the designated parameter to the given Java

boolean

value.

void

setByte

​(

String

parameterName,
byte x)

Sets the designated parameter to the given Java

byte

value.

void

setBytes

​(

String

parameterName,
byte[] x)

Sets the designated parameter to the given Java array of bytes.

void

setCharacterStream

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to the given

Reader

object.

void

setCharacterStream

​(

String

parameterName,

Reader

reader,
int length)

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

void

setCharacterStream

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

void

setClob

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setClob

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setClob

​(

String

parameterName,

Clob

x)

Sets the designated parameter to the given

java.sql.Clob

object.

void

setDate

​(

String

parameterName,

Date

x)

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.

void

setDate

​(

String

parameterName,

Date

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object.

void

setDouble

​(

String

parameterName,
double x)

Sets the designated parameter to the given Java

double

value.

void

setFloat

​(

String

parameterName,
float x)

Sets the designated parameter to the given Java

float

value.

void

setInt

​(

String

parameterName,
int x)

Sets the designated parameter to the given Java

int

value.

void

setLong

​(

String

parameterName,
long x)

Sets the designated parameter to the given Java

long

value.

void

setNCharacterStream

​(

String

parameterName,

Reader

value)

Sets the designated parameter to a

Reader

object.

void

setNCharacterStream

​(

String

parameterName,

Reader

value,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(

String

parameterName,

NClob

value)

Sets the designated parameter to a

java.sql.NClob

object.

void

setNString

​(

String

parameterName,

String

value)

Sets the designated parameter to the given

String

object.

void

setNull

​(

String

parameterName,
int sqlType)

Sets the designated parameter to SQL

NULL

.

void

setNull

​(

String

parameterName,
int sqlType,

String

typeName)

Sets the designated parameter to SQL

NULL

.

void

setObject

​(

String

parameterName,

Object

x)

Sets the value of the designated parameter with the given object.

void

setObject

​(

String

parameterName,

Object

x,
int targetSqlType)

Sets the value of the designated parameter with the given object.

void

setObject

​(

String

parameterName,

Object

x,
int targetSqlType,
int scale)

Sets the value of the designated parameter with the given object.

default void

setObject

​(

String

parameterName,

Object

x,

SQLType

targetSqlType)

Sets the value of the designated parameter with the given object.

default void

setObject

​(

String

parameterName,

Object

x,

SQLType

targetSqlType,
int scaleOrLength)

Sets the value of the designated parameter with the given object.

void

setRowId

​(

String

parameterName,

RowId

x)

Sets the designated parameter to the given

java.sql.RowId

object.

void

setShort

​(

String

parameterName,
short x)

Sets the designated parameter to the given Java

short

value.

void

setSQLXML

​(

String

parameterName,

SQLXML

xmlObject)

Sets the designated parameter to the given

java.sql.SQLXML

object.

void

setString

​(

String

parameterName,

String

x)

Sets the designated parameter to the given Java

String

value.

void

setTime

​(

String

parameterName,

Time

x)

Sets the designated parameter to the given

java.sql.Time

value.

void

setTime

​(

String

parameterName,

Time

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object.

void

setTimestamp

​(

String

parameterName,

Timestamp

x)

Sets the designated parameter to the given

java.sql.Timestamp

value.

void

setTimestamp

​(

String

parameterName,

Timestamp

x,

Calendar

cal)

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object.

void

setURL

​(

String

parameterName,

URL

val)

Sets the designated parameter to the given

java.net.URL

object.

boolean

wasNull

()

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

.

- Methods declared in interface java.sql.

PreparedStatement

addBatch

,

clearParameters

,

execute

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

getMetaData

,

getParameterMetaData

,

setArray

,

setAsciiStream

,

setAsciiStream

,

setAsciiStream

,

setBigDecimal

,

setBinaryStream

,

setBinaryStream

,

setBinaryStream

,

setBlob

,

setBlob

,

setBlob

,

setBoolean

,

setByte

,

setBytes

,

setCharacterStream

,

setCharacterStream

,

setCharacterStream

,

setClob

,

setClob

,

setClob

,

setDate

,

setDate

,

setDouble

,

setFloat

,

setInt

,

setLong

,

setNCharacterStream

,

setNCharacterStream

,

setNClob

,

setNClob

,

setNClob

,

setNString

,

setNull

,

setNull

,

setObject

,

setObject

,

setObject

,

setObject

,

setObject

,

setRef

,

setRowId

,

setShort

,

setSQLXML

,

setString

,

setTime

,

setTime

,

setTimestamp

,

setTimestamp

,

setUnicodeStream

,

setURL

- Methods declared in interface java.sql.

Statement

addBatch

,

cancel

,

clearBatch

,

clearWarnings

,

close

,

closeOnCompletion

,

enquoteIdentifier

,

enquoteLiteral

,

enquoteNCharLiteral

,

execute

,

execute

,

execute

,

execute

,

executeBatch

,

executeLargeBatch

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

getConnection

,

getFetchDirection

,

getFetchSize

,

getGeneratedKeys

,

getLargeMaxRows

,

getLargeUpdateCount

,

getMaxFieldSize

,

getMaxRows

,

getMoreResults

,

getMoreResults

,

getQueryTimeout

,

getResultSet

,

getResultSetConcurrency

,

getResultSetHoldability

,

getResultSetType

,

getUpdateCount

,

getWarnings

,

isClosed

,

isCloseOnCompletion

,

isPoolable

,

isSimpleIdentifier

,

setCursorName

,

setEscapeProcessing

,

setFetchDirection

,

setFetchSize

,

setLargeMaxRows

,

setMaxFieldSize

,

setMaxRows

,

setPoolable

,

setQueryTimeout

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Method Summary

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

Retrieves the value of the designated parameter as an

Object

in the Java programming language.

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

Retrieves the value of a parameter as an

Object

in the Java
programming language.

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported.

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

.

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

.

Registers the designated output parameter.

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

.

Registers the parameter named

parameterName

to be of JDBC type

sqlType

.

Sets the designated parameter to the given input stream.

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

Sets the designated parameter to the given

java.math.BigDecimal

value.

Sets the designated parameter to an

InputStream

object.

Sets the designated parameter to the given

java.sql.Blob

object.

Sets the designated parameter to the given Java

boolean

value.

Sets the designated parameter to the given Java

byte

value.

Sets the designated parameter to the given Java array of bytes.

Sets the designated parameter to the given

Reader

object.

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

Sets the designated parameter to a

Reader

object.

Sets the designated parameter to the given

java.sql.Clob

object.

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object.

Sets the designated parameter to the given Java

double

value.

Sets the designated parameter to the given Java

float

value.

Sets the designated parameter to the given Java

int

value.

Sets the designated parameter to the given Java

long

value.

Sets the designated parameter to a

java.sql.NClob

object.

Sets the designated parameter to the given

String

object.

Sets the designated parameter to SQL

NULL

.

Sets the value of the designated parameter with the given object.

Sets the designated parameter to the given

java.sql.RowId

object.

Sets the designated parameter to the given Java

short

value.

Sets the designated parameter to the given

java.sql.SQLXML

object.

Sets the designated parameter to the given Java

String

value.

Sets the designated parameter to the given

java.sql.Time

value.

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object.

Sets the designated parameter to the given

java.sql.Timestamp

value.

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object.

Sets the designated parameter to the given

java.net.URL

object.

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

.

Methods declared in interface java.sql.

PreparedStatement

addBatch

,

clearParameters

,

execute

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

getMetaData

,

getParameterMetaData

,

setArray

,

setAsciiStream

,

setAsciiStream

,

setAsciiStream

,

setBigDecimal

,

setBinaryStream

,

setBinaryStream

,

setBinaryStream

,

setBlob

,

setBlob

,

setBlob

,

setBoolean

,

setByte

,

setBytes

,

setCharacterStream

,

setCharacterStream

,

setCharacterStream

,

setClob

,

setClob

,

setClob

,

setDate

,

setDate

,

setDouble

,

setFloat

,

setInt

,

setLong

,

setNCharacterStream

,

setNCharacterStream

,

setNClob

,

setNClob

,

setNClob

,

setNString

,

setNull

,

setNull

,

setObject

,

setObject

,

setObject

,

setObject

,

setObject

,

setRef

,

setRowId

,

setShort

,

setSQLXML

,

setString

,

setTime

,

setTime

,

setTimestamp

,

setTimestamp

,

setUnicodeStream

,

setURL

---

#### Methods declared in interface java.sql. PreparedStatement

Methods declared in interface java.sql.

Statement

addBatch

,

cancel

,

clearBatch

,

clearWarnings

,

close

,

closeOnCompletion

,

enquoteIdentifier

,

enquoteLiteral

,

enquoteNCharLiteral

,

execute

,

execute

,

execute

,

execute

,

executeBatch

,

executeLargeBatch

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeLargeUpdate

,

executeQuery

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

executeUpdate

,

getConnection

,

getFetchDirection

,

getFetchSize

,

getGeneratedKeys

,

getLargeMaxRows

,

getLargeUpdateCount

,

getMaxFieldSize

,

getMaxRows

,

getMoreResults

,

getMoreResults

,

getQueryTimeout

,

getResultSet

,

getResultSetConcurrency

,

getResultSetHoldability

,

getResultSetType

,

getUpdateCount

,

getWarnings

,

isClosed

,

isCloseOnCompletion

,

isPoolable

,

isSimpleIdentifier

,

setCursorName

,

setEscapeProcessing

,

setFetchDirection

,

setFetchSize

,

setLargeMaxRows

,

setMaxFieldSize

,

setMaxRows

,

setPoolable

,

setQueryTimeout

---

#### Methods declared in interface java.sql. Statement

Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Methods declared in interface java.sql. Wrapper

============ METHOD DETAIL ==========

- Method Detail

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

- wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

. Note that this method should be called only after
calling a getter method; otherwise, there is no value to use in
determining whether it is

null

or not.

**Returns:** true

if the last parameter read was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement

- getString

```java
String
getString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setString(java.lang.String, java.lang.String)

- getBoolean

```java
boolean getBoolean​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

false

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBoolean(java.lang.String, boolean)

- getByte

```java
byte getByte​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setByte(java.lang.String, byte)

- getShort

```java
short getShort​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setShort(java.lang.String, short)

- getInt

```java
int getInt​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setInt(java.lang.String, int)

- getLong

```java
long getLong​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setLong(java.lang.String, long)

- getFloat

```java
float getFloat​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setFloat(java.lang.String, float)

- getDouble

```java
double getDouble​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDouble(java.lang.String, double)

- getBigDecimal

```java
@Deprecated
(
since
="1.2")

BigDecimal
getBigDecimal​(int parameterIndex,
int scale)
throws
SQLException
```

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with

scale

digits to
the right of the decimal point.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** scale

- the number of digits to the right of the decimal point
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getBytes

```java
byte[] getBytes​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBytes(java.lang.String, byte[])

- getDate

```java
Date
getDate​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getObject

```java
Object
getObject​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as an

Object

in the Java programming language. If the value is an SQL

NULL

,
the driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** A

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

- getBigDecimal

```java
BigDecimal
getBigDecimal​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getObject

```java
Object
getObject​(int parameterIndex,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

- getRef

```java
Ref
getRef​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getBlob

```java
Blob
getBlob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getClob

```java
Clob
getClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getArray

```java
Array
getArray​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as an

Array

object in
the Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getDate

```java
Date
getDate​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter. Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**Since:** 1.2
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- getURL

```java
URL
getURL​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

java.net.URL

object that represents the
JDBC

DATALINK

value used as the designated
parameter
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if the URL being returned is
not a valid URL on the Java platform
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

- setURL

```java
void setURL​(
String
parameterName,

URL
val)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

object.
The driver converts this to an SQL

DATALINK

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** val

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getURL(int)

- setNull

```java
void setNull​(
String
parameterName,
int sqlType)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the SQL type code defined in

java.sql.Types
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBoolean

```java
void setBoolean​(
String
parameterName,
boolean x)
throws
SQLException
```

Sets the designated parameter to the given Java

boolean

value.
The driver converts this
to an SQL

BIT

or

BOOLEAN

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBoolean(int)

- setByte

```java
void setByte​(
String
parameterName,
byte x)
throws
SQLException
```

Sets the designated parameter to the given Java

byte

value.
The driver converts this
to an SQL

TINYINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getByte(int)

- setShort

```java
void setShort​(
String
parameterName,
short x)
throws
SQLException
```

Sets the designated parameter to the given Java

short

value.
The driver converts this
to an SQL

SMALLINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getShort(int)

- setInt

```java
void setInt​(
String
parameterName,
int x)
throws
SQLException
```

Sets the designated parameter to the given Java

int

value.
The driver converts this
to an SQL

INTEGER

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getInt(int)

- setLong

```java
void setLong​(
String
parameterName,
long x)
throws
SQLException
```

Sets the designated parameter to the given Java

long

value.
The driver converts this
to an SQL

BIGINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getLong(int)

- setFloat

```java
void setFloat​(
String
parameterName,
float x)
throws
SQLException
```

Sets the designated parameter to the given Java

float

value.
The driver converts this
to an SQL

FLOAT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getFloat(int)

- setDouble

```java
void setDouble​(
String
parameterName,
double x)
throws
SQLException
```

Sets the designated parameter to the given Java

double

value.
The driver converts this
to an SQL

DOUBLE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDouble(int)

- setBigDecimal

```java
void setBigDecimal​(
String
parameterName,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter to the given

java.math.BigDecimal

value.
The driver converts this to an SQL

NUMERIC

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBigDecimal(int, int)

- setString

```java
void setString​(
String
parameterName,

String
x)
throws
SQLException
```

Sets the designated parameter to the given Java

String

value.
The driver converts this
to an SQL

VARCHAR

or

LONGVARCHAR

value
(depending on the argument's
size relative to the driver's limits on

VARCHAR

values)
when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getString(int)

- setBytes

```java
void setBytes​(
String
parameterName,
byte[] x)
throws
SQLException
```

Sets the designated parameter to the given Java array of bytes.
The driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

(depending on the argument's size relative
to the driver's limits on

VARBINARY

values) when it sends
it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBytes(int)

- setDate

```java
void setDate​(
String
parameterName,

Date
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.
The driver converts this
to an SQL

DATE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

- setTime

```java
void setTime​(
String
parameterName,

Time
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value.
The driver converts this
to an SQL

TIME

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

- setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value.
The driver
converts this to an SQL

TIMESTAMP

value when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType,
int scale)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scale

- for java.sql.Types.DECIMAL or java.sql.Types.NUMERIC types,
this is the number of digits after the decimal point. For all other
types, this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** Types

,

getObject(int)

- setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, int targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** getObject(int)

- setObject

```java
void setObject​(
String
parameterName,

Object
x)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getObject(int)

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setDate

```java
void setDate​(
String
parameterName,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

DATE

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the date
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

- setTime

```java
void setTime​(
String
parameterName,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIME

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the time
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

- setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIMESTAMP

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the timestamp
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

- setNull

```java
void setNull​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.
This version of the method

setNull

should
be used for user-defined types and REF type parameters. Examples
of user-defined types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully-qualified name of an SQL user-defined type;
ignored if the parameter is not a user-defined type or
SQL

REF

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getString

```java
String
getString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setString(java.lang.String, java.lang.String)

- getBoolean

```java
boolean getBoolean​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

false

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBoolean(java.lang.String, boolean)

- getByte

```java
byte getByte​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setByte(java.lang.String, byte)

- getShort

```java
short getShort​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setShort(java.lang.String, short)

- getInt

```java
int getInt​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setInt(java.lang.String, int)

- getLong

```java
long getLong​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setLong(java.lang.String, long)

- getFloat

```java
float getFloat​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setFloat(java.lang.String, float)

- getDouble

```java
double getDouble​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDouble(java.lang.String, double)

- getBytes

```java
byte[] getBytes​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBytes(java.lang.String, byte[])

- getDate

```java
Date
getDate​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getObject

```java
Object
getObject​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a parameter as an

Object

in the Java
programming language. If the value is an SQL

NULL

, the
driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Returns:** A

java.lang.Object

holding the OUT parameter value.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

- getBigDecimal

```java
BigDecimal
getBigDecimal​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getObject

```java
Object
getObject​(
String
parameterName,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

- getRef

```java
Ref
getRef​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getBlob

```java
Blob
getBlob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getClob

```java
Clob
getClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getArray

```java
Array
getArray​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as an

Array

object in
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getDate

```java
Date
getDate​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getURL

```java
URL
getURL​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

java.net.URL

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if there is a problem with the URL
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

- getRowId

```java
RowId
getRowId​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getRowId

```java
RowId
getRowId​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setRowId

```java
void setRowId​(
String
parameterName,

RowId
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNString

```java
void setNString​(
String
parameterName,

String
value)
throws
SQLException
```

Sets the designated parameter to the given

String

object.
The driver converts this to a SQL

NCHAR

or

NVARCHAR

or

LONGNVARCHAR

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The object
implements the

java.sql.NClob

interface. This

NClob

object maps to a SQL

NCLOB

.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
The

Inputstream

must contain the number
of characters specified by length, otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setBinaryStream (int, InputStream, int)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

**Parameters:** parameterName

- the name of the parameter to be set
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match the specified length; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNClob

```java
NClob
getNClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNClob

```java
NClob
getNClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setSQLXML

```java
void setSQLXML​(
String
parameterName,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an

SQL XML

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** xmlObject

- a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed for the

SQLXML

object
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getSQLXML

```java
SQLXML
getSQLXML​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getSQLXML

```java
SQLXML
getSQLXML​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNString

```java
String
getNString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

- getNString

```java
String
getNString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

- getNCharacterStream

```java
Reader
getNCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNCharacterStream

```java
Reader
getNCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getCharacterStream

```java
Reader
getCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid; if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.6

- getCharacterStream

```java
Reader
getCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

Blob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Blob

object.
The driver converts this to an SQL

BLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Blob

object that maps an SQL

BLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Clob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Clob

object.
The driver converts this to an SQL

CLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Clob

object that maps an SQL

CLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the
stream as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs; or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or this method is called on
a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
This method differs from the

setBinaryStream (int, InputStream)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- getObject

```java
<T> T getObject​(int parameterIndex,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** type

- Class representing the Java data type to convert the
designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

- getObject

```java
<T> T getObject​(
String
parameterName,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterName

- the name of the parameter
**Parameters:** type

- Class representing the Java data type to convert
the designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter
value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

- setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

If the second argument is an

InputStream

then the stream
must contain the number of bytes specified by scaleOrLength.
If the second argument is a

Reader

then the reader must
contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver
will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scaleOrLength

- for

java.sql.JDBCType.DECIMAL

or

java.sql.JDBCType.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or reader. For all other types,
this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement

or
if the Java Object specified by x is an InputStream
or Reader object and the value of the scale parameter is less
than zero
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, SQLType targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter.
Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

Method Detail

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

- wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

. Note that this method should be called only after
calling a getter method; otherwise, there is no value to use in
determining whether it is

null

or not.

**Returns:** true

if the last parameter read was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement

- getString

```java
String
getString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setString(java.lang.String, java.lang.String)

- getBoolean

```java
boolean getBoolean​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

false

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBoolean(java.lang.String, boolean)

- getByte

```java
byte getByte​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setByte(java.lang.String, byte)

- getShort

```java
short getShort​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setShort(java.lang.String, short)

- getInt

```java
int getInt​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setInt(java.lang.String, int)

- getLong

```java
long getLong​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setLong(java.lang.String, long)

- getFloat

```java
float getFloat​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setFloat(java.lang.String, float)

- getDouble

```java
double getDouble​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDouble(java.lang.String, double)

- getBigDecimal

```java
@Deprecated
(
since
="1.2")

BigDecimal
getBigDecimal​(int parameterIndex,
int scale)
throws
SQLException
```

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with

scale

digits to
the right of the decimal point.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** scale

- the number of digits to the right of the decimal point
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getBytes

```java
byte[] getBytes​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBytes(java.lang.String, byte[])

- getDate

```java
Date
getDate​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getObject

```java
Object
getObject​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as an

Object

in the Java programming language. If the value is an SQL

NULL

,
the driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** A

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

- getBigDecimal

```java
BigDecimal
getBigDecimal​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getObject

```java
Object
getObject​(int parameterIndex,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

- getRef

```java
Ref
getRef​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getBlob

```java
Blob
getBlob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getClob

```java
Clob
getClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getArray

```java
Array
getArray​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as an

Array

object in
the Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getDate

```java
Date
getDate​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter. Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**Since:** 1.2
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

- getURL

```java
URL
getURL​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

java.net.URL

object that represents the
JDBC

DATALINK

value used as the designated
parameter
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if the URL being returned is
not a valid URL on the Java platform
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

- setURL

```java
void setURL​(
String
parameterName,

URL
val)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

object.
The driver converts this to an SQL

DATALINK

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** val

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getURL(int)

- setNull

```java
void setNull​(
String
parameterName,
int sqlType)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the SQL type code defined in

java.sql.Types
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBoolean

```java
void setBoolean​(
String
parameterName,
boolean x)
throws
SQLException
```

Sets the designated parameter to the given Java

boolean

value.
The driver converts this
to an SQL

BIT

or

BOOLEAN

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBoolean(int)

- setByte

```java
void setByte​(
String
parameterName,
byte x)
throws
SQLException
```

Sets the designated parameter to the given Java

byte

value.
The driver converts this
to an SQL

TINYINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getByte(int)

- setShort

```java
void setShort​(
String
parameterName,
short x)
throws
SQLException
```

Sets the designated parameter to the given Java

short

value.
The driver converts this
to an SQL

SMALLINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getShort(int)

- setInt

```java
void setInt​(
String
parameterName,
int x)
throws
SQLException
```

Sets the designated parameter to the given Java

int

value.
The driver converts this
to an SQL

INTEGER

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getInt(int)

- setLong

```java
void setLong​(
String
parameterName,
long x)
throws
SQLException
```

Sets the designated parameter to the given Java

long

value.
The driver converts this
to an SQL

BIGINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getLong(int)

- setFloat

```java
void setFloat​(
String
parameterName,
float x)
throws
SQLException
```

Sets the designated parameter to the given Java

float

value.
The driver converts this
to an SQL

FLOAT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getFloat(int)

- setDouble

```java
void setDouble​(
String
parameterName,
double x)
throws
SQLException
```

Sets the designated parameter to the given Java

double

value.
The driver converts this
to an SQL

DOUBLE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDouble(int)

- setBigDecimal

```java
void setBigDecimal​(
String
parameterName,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter to the given

java.math.BigDecimal

value.
The driver converts this to an SQL

NUMERIC

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBigDecimal(int, int)

- setString

```java
void setString​(
String
parameterName,

String
x)
throws
SQLException
```

Sets the designated parameter to the given Java

String

value.
The driver converts this
to an SQL

VARCHAR

or

LONGVARCHAR

value
(depending on the argument's
size relative to the driver's limits on

VARCHAR

values)
when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getString(int)

- setBytes

```java
void setBytes​(
String
parameterName,
byte[] x)
throws
SQLException
```

Sets the designated parameter to the given Java array of bytes.
The driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

(depending on the argument's size relative
to the driver's limits on

VARBINARY

values) when it sends
it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBytes(int)

- setDate

```java
void setDate​(
String
parameterName,

Date
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.
The driver converts this
to an SQL

DATE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

- setTime

```java
void setTime​(
String
parameterName,

Time
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value.
The driver converts this
to an SQL

TIME

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

- setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value.
The driver
converts this to an SQL

TIMESTAMP

value when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType,
int scale)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scale

- for java.sql.Types.DECIMAL or java.sql.Types.NUMERIC types,
this is the number of digits after the decimal point. For all other
types, this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** Types

,

getObject(int)

- setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, int targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** getObject(int)

- setObject

```java
void setObject​(
String
parameterName,

Object
x)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getObject(int)

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setDate

```java
void setDate​(
String
parameterName,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

DATE

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the date
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

- setTime

```java
void setTime​(
String
parameterName,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIME

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the time
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

- setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIMESTAMP

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the timestamp
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

- setNull

```java
void setNull​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.
This version of the method

setNull

should
be used for user-defined types and REF type parameters. Examples
of user-defined types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully-qualified name of an SQL user-defined type;
ignored if the parameter is not a user-defined type or
SQL

REF

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getString

```java
String
getString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setString(java.lang.String, java.lang.String)

- getBoolean

```java
boolean getBoolean​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

false

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBoolean(java.lang.String, boolean)

- getByte

```java
byte getByte​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setByte(java.lang.String, byte)

- getShort

```java
short getShort​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setShort(java.lang.String, short)

- getInt

```java
int getInt​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setInt(java.lang.String, int)

- getLong

```java
long getLong​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setLong(java.lang.String, long)

- getFloat

```java
float getFloat​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setFloat(java.lang.String, float)

- getDouble

```java
double getDouble​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDouble(java.lang.String, double)

- getBytes

```java
byte[] getBytes​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBytes(java.lang.String, byte[])

- getDate

```java
Date
getDate​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getObject

```java
Object
getObject​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a parameter as an

Object

in the Java
programming language. If the value is an SQL

NULL

, the
driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Returns:** A

java.lang.Object

holding the OUT parameter value.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

- getBigDecimal

```java
BigDecimal
getBigDecimal​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

- getObject

```java
Object
getObject​(
String
parameterName,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

- getRef

```java
Ref
getRef​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getBlob

```java
Blob
getBlob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getClob

```java
Clob
getClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getArray

```java
Array
getArray​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as an

Array

object in
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- getDate

```java
Date
getDate​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

- getTime

```java
Time
getTime​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

- getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

- getURL

```java
URL
getURL​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

java.net.URL

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if there is a problem with the URL
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

- getRowId

```java
RowId
getRowId​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getRowId

```java
RowId
getRowId​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setRowId

```java
void setRowId​(
String
parameterName,

RowId
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNString

```java
void setNString​(
String
parameterName,

String
value)
throws
SQLException
```

Sets the designated parameter to the given

String

object.
The driver converts this to a SQL

NCHAR

or

NVARCHAR

or

LONGNVARCHAR

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The object
implements the

java.sql.NClob

interface. This

NClob

object maps to a SQL

NCLOB

.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
The

Inputstream

must contain the number
of characters specified by length, otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setBinaryStream (int, InputStream, int)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

**Parameters:** parameterName

- the name of the parameter to be set
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match the specified length; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNClob

```java
NClob
getNClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNClob

```java
NClob
getNClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setSQLXML

```java
void setSQLXML​(
String
parameterName,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an

SQL XML

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** xmlObject

- a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed for the

SQLXML

object
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getSQLXML

```java
SQLXML
getSQLXML​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getSQLXML

```java
SQLXML
getSQLXML​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNString

```java
String
getNString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

- getNString

```java
String
getNString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

- getNCharacterStream

```java
Reader
getNCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getNCharacterStream

```java
Reader
getNCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- getCharacterStream

```java
Reader
getCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid; if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.6

- getCharacterStream

```java
Reader
getCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

Blob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Blob

object.
The driver converts this to an SQL

BLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Blob

object that maps an SQL

BLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Clob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Clob

object.
The driver converts this to an SQL

CLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Clob

object that maps an SQL

CLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

- setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the
stream as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs; or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or this method is called on
a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
This method differs from the

setBinaryStream (int, InputStream)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- getObject

```java
<T> T getObject​(int parameterIndex,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** type

- Class representing the Java data type to convert the
designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

- getObject

```java
<T> T getObject​(
String
parameterName,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterName

- the name of the parameter
**Parameters:** type

- Class representing the Java data type to convert
the designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter
value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

- setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

If the second argument is an

InputStream

then the stream
must contain the number of bytes specified by scaleOrLength.
If the second argument is a

Reader

then the reader must
contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver
will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scaleOrLength

- for

java.sql.JDBCType.DECIMAL

or

java.sql.JDBCType.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or reader. For all other types,
this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement

or
if the Java Object specified by x is an InputStream
or Reader object and the value of the scale parameter is less
than zero
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, SQLType targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter.
Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

- registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### Method Detail

registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(int parameterIndex,
int sqlType)
throws

SQLException

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(int parameterIndex,
int sqlType,
int scale)
throws

SQLException

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

wasNull

```java
boolean wasNull()
throws
SQLException
```

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

. Note that this method should be called only after
calling a getter method; otherwise, there is no value to use in
determining whether it is

null

or not.

**Returns:** true

if the last parameter read was SQL

NULL

;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement

---

#### wasNull

boolean wasNull()
throws

SQLException

Retrieves whether the last OUT parameter read had the value of
SQL

NULL

. Note that this method should be called only after
calling a getter method; otherwise, there is no value to use in
determining whether it is

null

or not.

getString

```java
String
getString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setString(java.lang.String, java.lang.String)

---

#### getString

String

getString​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

CHAR

,

VARCHAR

, or

LONGVARCHAR

parameter as a

String

in the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

getBoolean

```java
boolean getBoolean​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

false

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBoolean(java.lang.String, boolean)

---

#### getBoolean

boolean getBoolean​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

getByte

```java
byte getByte​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setByte(java.lang.String, byte)

---

#### getByte

byte getByte​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

TINYINT

parameter
as a

byte

in the Java programming language.

getShort

```java
short getShort​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setShort(java.lang.String, short)

---

#### getShort

short getShort​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

SMALLINT

parameter
as a

short

in the Java programming language.

getInt

```java
int getInt​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setInt(java.lang.String, int)

---

#### getInt

int getInt​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

INTEGER

parameter
as an

int

in the Java programming language.

getLong

```java
long getLong​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setLong(java.lang.String, long)

---

#### getLong

long getLong​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

BIGINT

parameter
as a

long

in the Java programming language.

getFloat

```java
float getFloat​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setFloat(java.lang.String, float)

---

#### getFloat

float getFloat​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

FLOAT

parameter
as a

float

in the Java programming language.

getDouble

```java
double getDouble​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDouble(java.lang.String, double)

---

#### getDouble

double getDouble​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

DOUBLE

parameter as a

double

in the Java programming language.

getBigDecimal

```java
@Deprecated
(
since
="1.2")

BigDecimal
getBigDecimal​(int parameterIndex,
int scale)
throws
SQLException
```

Deprecated.

use

getBigDecimal(int parameterIndex)

or

getBigDecimal(String parameterName)

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with

scale

digits to
the right of the decimal point.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** scale

- the number of digits to the right of the decimal point
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

---

#### getBigDecimal

@Deprecated

(

since

="1.2")

BigDecimal

getBigDecimal​(int parameterIndex,
int scale)
throws

SQLException

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with

scale

digits to
the right of the decimal point.

getBytes

```java
byte[] getBytes​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setBytes(java.lang.String, byte[])

---

#### getBytes

byte[] getBytes​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java programming language.

getDate

```java
Date
getDate​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setDate(java.lang.String, java.sql.Date)

---

#### getDate

Date

getDate​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object.

getTime

```java
Time
getTime​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTime(java.lang.String, java.sql.Time)

---

#### getTime

Time

getTime​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object.

getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

---

#### getTimestamp

Timestamp

getTimestamp​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

getObject

```java
Object
getObject​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as an

Object

in the Java programming language. If the value is an SQL

NULL

,
the driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** A

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

---

#### getObject

Object

getObject​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated parameter as an

Object

in the Java programming language. If the value is an SQL

NULL

,
the driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

getBigDecimal

```java
BigDecimal
getBigDecimal​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

---

#### getBigDecimal

BigDecimal

getBigDecimal​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

getObject

```java
Object
getObject​(int parameterIndex,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

---

#### getObject

Object

getObject​(int parameterIndex,

Map

<

String

,​

Class

<?>> map)
throws

SQLException

Returns an object representing the value of OUT parameter

parameterIndex

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

getRef

```java
Ref
getRef​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getRef

Ref

getRef​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

getBlob

```java
Blob
getBlob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

, the value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getBlob

Blob

getBlob​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

getClob

```java
Clob
getClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getClob

Clob

getClob​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

getArray

```java
Array
getArray​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as an

Array

object in
the Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getArray

Array

getArray​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

getDate

```java
Date
getDate​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setDate(java.lang.String, java.sql.Date)

---

#### getDate

Date

getDate​(int parameterIndex,

Calendar

cal)
throws

SQLException

Retrieves the value of the designated JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

getTime

```java
Time
getTime​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTime(java.lang.String, java.sql.Time)

---

#### getTime

Time

getTime​(int parameterIndex,

Calendar

cal)
throws

SQLException

Retrieves the value of the designated JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

getTimestamp

```java
Timestamp
getTimestamp​(int parameterIndex,

Calendar
cal)
throws
SQLException
```

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.2
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

---

#### getTimestamp

Timestamp

getTimestamp​(int parameterIndex,

Calendar

cal)
throws

SQLException

Retrieves the value of the designated JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

registerOutParameter

```java
void registerOutParameter​(int parameterIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter. Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type
**Since:** 1.2
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(int parameterIndex,
int sqlType,

String

typeName)
throws

SQLException

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter. Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

java.sql.Types

.
If the parameter is of JDBC type

NUMERIC

or

DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(

String

parameterName,
int sqlType)
throws

SQLException

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

java.sql.Types.OTHER

. The method

getObject(int)

retrieves the value.

registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- SQL type code defined by

java.sql.Types

.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(

String

parameterName,
int sqlType,
int scale)
throws

SQLException

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

NUMERIC

or

DECIMAL

.

registerOutParameter

```java
void registerOutParameter​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

Types
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

sqlType

is
a

ARRAY

,

BLOB

,

CLOB

,

DATALINK

,

JAVA_OBJECT

,

NCHAR

,

NCLOB

,

NVARCHAR

,

LONGNVARCHAR

,

REF

,

ROWID

,

SQLXML

or

STRUCT

data type and the JDBC driver does not support
this data type or if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

---

#### registerOutParameter

void registerOutParameter​(

String

parameterName,
int sqlType,

String

typeName)
throws

SQLException

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

getURL

```java
URL
getURL​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

java.net.URL

object that represents the
JDBC

DATALINK

value used as the designated
parameter
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if the URL being returned is
not a valid URL on the Java platform
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

---

#### getURL

URL

getURL​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

DATALINK

parameter as a

java.net.URL

object.

setURL

```java
void setURL​(
String
parameterName,

URL
val)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

object.
The driver converts this to an SQL

DATALINK

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** val

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or if a URL is malformed
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getURL(int)

---

#### setURL

void setURL​(

String

parameterName,

URL

val)
throws

SQLException

Sets the designated parameter to the given

java.net.URL

object.
The driver converts this to an SQL

DATALINK

value when
it sends it to the database.

setNull

```java
void setNull​(
String
parameterName,
int sqlType)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the SQL type code defined in

java.sql.Types
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### setNull

void setNull​(

String

parameterName,
int sqlType)
throws

SQLException

Sets the designated parameter to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

Note:

You must specify the parameter's SQL type.

setBoolean

```java
void setBoolean​(
String
parameterName,
boolean x)
throws
SQLException
```

Sets the designated parameter to the given Java

boolean

value.
The driver converts this
to an SQL

BIT

or

BOOLEAN

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBoolean(int)

---

#### setBoolean

void setBoolean​(

String

parameterName,
boolean x)
throws

SQLException

Sets the designated parameter to the given Java

boolean

value.
The driver converts this
to an SQL

BIT

or

BOOLEAN

value when it sends it to the database.

setByte

```java
void setByte​(
String
parameterName,
byte x)
throws
SQLException
```

Sets the designated parameter to the given Java

byte

value.
The driver converts this
to an SQL

TINYINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getByte(int)

---

#### setByte

void setByte​(

String

parameterName,
byte x)
throws

SQLException

Sets the designated parameter to the given Java

byte

value.
The driver converts this
to an SQL

TINYINT

value when it sends it to the database.

setShort

```java
void setShort​(
String
parameterName,
short x)
throws
SQLException
```

Sets the designated parameter to the given Java

short

value.
The driver converts this
to an SQL

SMALLINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getShort(int)

---

#### setShort

void setShort​(

String

parameterName,
short x)
throws

SQLException

Sets the designated parameter to the given Java

short

value.
The driver converts this
to an SQL

SMALLINT

value when it sends it to the database.

setInt

```java
void setInt​(
String
parameterName,
int x)
throws
SQLException
```

Sets the designated parameter to the given Java

int

value.
The driver converts this
to an SQL

INTEGER

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getInt(int)

---

#### setInt

void setInt​(

String

parameterName,
int x)
throws

SQLException

Sets the designated parameter to the given Java

int

value.
The driver converts this
to an SQL

INTEGER

value when it sends it to the database.

setLong

```java
void setLong​(
String
parameterName,
long x)
throws
SQLException
```

Sets the designated parameter to the given Java

long

value.
The driver converts this
to an SQL

BIGINT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getLong(int)

---

#### setLong

void setLong​(

String

parameterName,
long x)
throws

SQLException

Sets the designated parameter to the given Java

long

value.
The driver converts this
to an SQL

BIGINT

value when it sends it to the database.

setFloat

```java
void setFloat​(
String
parameterName,
float x)
throws
SQLException
```

Sets the designated parameter to the given Java

float

value.
The driver converts this
to an SQL

FLOAT

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getFloat(int)

---

#### setFloat

void setFloat​(

String

parameterName,
float x)
throws

SQLException

Sets the designated parameter to the given Java

float

value.
The driver converts this
to an SQL

FLOAT

value when it sends it to the database.

setDouble

```java
void setDouble​(
String
parameterName,
double x)
throws
SQLException
```

Sets the designated parameter to the given Java

double

value.
The driver converts this
to an SQL

DOUBLE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDouble(int)

---

#### setDouble

void setDouble​(

String

parameterName,
double x)
throws

SQLException

Sets the designated parameter to the given Java

double

value.
The driver converts this
to an SQL

DOUBLE

value when it sends it to the database.

setBigDecimal

```java
void setBigDecimal​(
String
parameterName,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter to the given

java.math.BigDecimal

value.
The driver converts this to an SQL

NUMERIC

value when
it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBigDecimal(int, int)

---

#### setBigDecimal

void setBigDecimal​(

String

parameterName,

BigDecimal

x)
throws

SQLException

Sets the designated parameter to the given

java.math.BigDecimal

value.
The driver converts this to an SQL

NUMERIC

value when
it sends it to the database.

setString

```java
void setString​(
String
parameterName,

String
x)
throws
SQLException
```

Sets the designated parameter to the given Java

String

value.
The driver converts this
to an SQL

VARCHAR

or

LONGVARCHAR

value
(depending on the argument's
size relative to the driver's limits on

VARCHAR

values)
when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getString(int)

---

#### setString

void setString​(

String

parameterName,

String

x)
throws

SQLException

Sets the designated parameter to the given Java

String

value.
The driver converts this
to an SQL

VARCHAR

or

LONGVARCHAR

value
(depending on the argument's
size relative to the driver's limits on

VARCHAR

values)
when it sends it to the database.

setBytes

```java
void setBytes​(
String
parameterName,
byte[] x)
throws
SQLException
```

Sets the designated parameter to the given Java array of bytes.
The driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

(depending on the argument's size relative
to the driver's limits on

VARBINARY

values) when it sends
it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getBytes(int)

---

#### setBytes

void setBytes​(

String

parameterName,
byte[] x)
throws

SQLException

Sets the designated parameter to the given Java array of bytes.
The driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

(depending on the argument's size relative
to the driver's limits on

VARBINARY

values) when it sends
it to the database.

setDate

```java
void setDate​(
String
parameterName,

Date
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.
The driver converts this
to an SQL

DATE

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

---

#### setDate

void setDate​(

String

parameterName,

Date

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.Date

value
using the default time zone of the virtual machine that is running
the application.
The driver converts this
to an SQL

DATE

value when it sends it to the database.

setTime

```java
void setTime​(
String
parameterName,

Time
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value.
The driver converts this
to an SQL

TIME

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

---

#### setTime

void setTime​(

String

parameterName,

Time

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.Time

value.
The driver converts this
to an SQL

TIME

value when it sends it to the database.

setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value.
The driver
converts this to an SQL

TIMESTAMP

value when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

---

#### setTimestamp

void setTimestamp​(

String

parameterName,

Timestamp

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.Timestamp

value.
The driver
converts this to an SQL

TIMESTAMP

value when it sends it to the
database.

setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### setAsciiStream

void setAsciiStream​(

String

parameterName,

InputStream

x,
int length)
throws

SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### setBinaryStream

void setBinaryStream​(

String

parameterName,

InputStream

x,
int length)
throws

SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType,
int scale)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scale

- for java.sql.Types.DECIMAL or java.sql.Types.NUMERIC types,
this is the number of digits after the decimal point. For all other
types, this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** Types

,

getObject(int)

---

#### setObject

void setObject​(

String

parameterName,

Object

x,
int targetSqlType,
int scale)
throws

SQLException

Sets the value of the designated parameter with the given object.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to write it
to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass datatabase-
specific abstract data types.

Note that this method may be used to pass datatabase-
specific abstract data types.

setObject

```java
void setObject​(
String
parameterName,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, int targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.4
**See Also:** getObject(int)

---

#### setObject

void setObject​(

String

parameterName,

Object

x,
int targetSqlType)
throws

SQLException

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, int targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

setObject

```java
void setObject​(
String
parameterName,

Object
x)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getObject(int)

---

#### setObject

void setObject​(

String

parameterName,

Object

x)
throws

SQLException

Sets the value of the designated parameter with the given object.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

The JDBC specification specifies a standard mapping from
Java

Object

types to SQL types. The given argument
will be converted to the corresponding SQL type before being
sent to the database.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

Note that this method may be used to pass database-
specific abstract data types, by using a driver-specific Java
type.

If the object is of a class implementing the interface

SQLData

,
the JDBC driver should call the method

SQLData.writeSQL

to write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

Note:

Not all databases allow for a non-typed Null to be sent to
the backend. For maximum portability, the

setNull

or the

setObject(String parameterName, Object x, int sqlType)

method should be used
instead of

setObject(String parameterName, Object x)

.

setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### setCharacterStream

void setCharacterStream​(

String

parameterName,

Reader

reader,
int length)
throws

SQLException

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setDate

```java
void setDate​(
String
parameterName,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

DATE

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the date
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getDate(int)

---

#### setDate

void setDate​(

String

parameterName,

Date

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter to the given

java.sql.Date

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

DATE

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the date
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

setTime

```java
void setTime​(
String
parameterName,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIME

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the time
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTime(int)

---

#### setTime

void setTime​(

String

parameterName,

Time

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter to the given

java.sql.Time

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIME

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the time
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

setTimestamp

```java
void setTimestamp​(
String
parameterName,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIMESTAMP

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the timestamp
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** getTimestamp(int)

---

#### setTimestamp

void setTimestamp​(

String

parameterName,

Timestamp

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object. The driver uses
the

Calendar

object to construct an SQL

TIMESTAMP

value,
which the driver then sends to the database. With a
a

Calendar

object, the driver can calculate the timestamp
taking into account a custom timezone. If no

Calendar

object is specified, the driver uses the default
timezone, which is that of the virtual machine running the application.

setNull

```java
void setNull​(
String
parameterName,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter to SQL

NULL

.
This version of the method

setNull

should
be used for user-defined types and REF type parameters. Examples
of user-defined types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully-qualified name of an SQL user-defined type;
ignored if the parameter is not a user-defined type or
SQL

REF

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### setNull

void setNull​(

String

parameterName,
int sqlType,

String

typeName)
throws

SQLException

Sets the designated parameter to SQL

NULL

.
This version of the method

setNull

should
be used for user-defined types and REF type parameters. Examples
of user-defined types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

getString

```java
String
getString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setString(java.lang.String, java.lang.String)

---

#### getString

String

getString​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

CHAR

,

VARCHAR

,
or

LONGVARCHAR

parameter as a

String

in
the Java programming language.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

For the fixed-length type JDBC

CHAR

,
the

String

object
returned has exactly the same value the SQL

CHAR

value had in the
database, including any padding added by the database.

getBoolean

```java
boolean getBoolean​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

false

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBoolean(java.lang.String, boolean)

---

#### getBoolean

boolean getBoolean​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

BIT

or

BOOLEAN

parameter as a

boolean

in the Java programming language.

getByte

```java
byte getByte​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setByte(java.lang.String, byte)

---

#### getByte

byte getByte​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

TINYINT

parameter as a

byte

in the Java programming language.

getShort

```java
short getShort​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setShort(java.lang.String, short)

---

#### getShort

short getShort​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

SMALLINT

parameter as a

short

in the Java programming language.

getInt

```java
int getInt​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setInt(java.lang.String, int)

---

#### getInt

int getInt​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

INTEGER

parameter as an

int

in the Java programming language.

getLong

```java
long getLong​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setLong(java.lang.String, long)

---

#### getLong

long getLong​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

BIGINT

parameter as a

long

in the Java programming language.

getFloat

```java
float getFloat​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setFloat(java.lang.String, float)

---

#### getFloat

float getFloat​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

FLOAT

parameter as a

float

in the Java programming language.

getDouble

```java
double getDouble​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

0

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDouble(java.lang.String, double)

---

#### getDouble

double getDouble​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

DOUBLE

parameter as a

double

in the Java programming language.

getBytes

```java
byte[] getBytes​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBytes(java.lang.String, byte[])

---

#### getBytes

byte[] getBytes​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

BINARY

or

VARBINARY

parameter as an array of

byte

values in the Java
programming language.

getDate

```java
Date
getDate​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

---

#### getDate

Date

getDate​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object.

getTime

```java
Time
getTime​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

---

#### getTime

Time

getTime​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object.

getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value. If the value is SQL

NULL

, the result
is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

---

#### getTimestamp

Timestamp

getTimestamp​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object.

getObject

```java
Object
getObject​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a parameter as an

Object

in the Java
programming language. If the value is an SQL

NULL

, the
driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Returns:** A

java.lang.Object

holding the OUT parameter value.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** Types

,

setObject(java.lang.String, java.lang.Object, int, int)

---

#### getObject

Object

getObject​(

String

parameterName)
throws

SQLException

Retrieves the value of a parameter as an

Object

in the Java
programming language. If the value is an SQL

NULL

, the
driver returns a Java

null

.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

This method returns a Java object whose type corresponds to the JDBC
type that was registered for this parameter using the method

registerOutParameter

. By registering the target JDBC
type as

java.sql.Types.OTHER

, this method can be used
to read database-specific abstract data types.

getBigDecimal

```java
BigDecimal
getBigDecimal​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value in full precision. If the value is
SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setBigDecimal(java.lang.String, java.math.BigDecimal)

---

#### getBigDecimal

BigDecimal

getBigDecimal​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

NUMERIC

parameter as a

java.math.BigDecimal

object with as many digits to the
right of the decimal point as the value contains.

getObject

```java
Object
getObject​(
String
parameterName,

Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** map

- the mapping from SQL type names to Java classes
**Returns:** a

java.lang.Object

holding the OUT parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setObject(java.lang.String, java.lang.Object, int, int)

---

#### getObject

Object

getObject​(

String

parameterName,

Map

<

String

,​

Class

<?>> map)
throws

SQLException

Returns an object representing the value of OUT parameter

parameterName

and uses

map

for the custom
mapping of the parameter value.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

This method returns a Java object whose type corresponds to the
JDBC type that was registered for this parameter using the method

registerOutParameter

. By registering the target
JDBC type as

java.sql.Types.OTHER

, this method can
be used to read database-specific abstract data types.

getRef

```java
Ref
getRef​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Ref

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### getRef

Ref

getRef​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

REF(<structured-type>)

parameter as a

Ref

object in the Java programming language.

getBlob

```java
Blob
getBlob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Blob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### getBlob

Blob

getBlob​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

BLOB

parameter as a

Blob

object in the Java programming language.

getClob

```java
Clob
getClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

Clob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### getClob

Clob

getClob​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

CLOB

parameter as a

java.sql.Clob

object in the Java programming language.

getArray

```java
Array
getArray​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as an

Array

object in
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

---

#### getArray

Array

getArray​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

ARRAY

parameter as an

Array

object in the Java programming language.

getDate

```java
Date
getDate​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the date
**Returns:** the parameter value. If the value is SQL

NULL

,
the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setDate(java.lang.String, java.sql.Date)

---

#### getDate

Date

getDate​(

String

parameterName,

Calendar

cal)
throws

SQLException

Retrieves the value of a JDBC

DATE

parameter as a

java.sql.Date

object, using
the given

Calendar

object
to construct the date.
With a

Calendar

object, the driver
can calculate the date taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

getTime

```java
Time
getTime​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the time
**Returns:** the parameter value; if the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTime(java.lang.String, java.sql.Time)

---

#### getTime

Time

getTime​(

String

parameterName,

Calendar

cal)
throws

SQLException

Retrieves the value of a JDBC

TIME

parameter as a

java.sql.Time

object, using
the given

Calendar

object
to construct the time.
With a

Calendar

object, the driver
can calculate the time taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

getTimestamp

```java
Timestamp
getTimestamp​(
String
parameterName,

Calendar
cal)
throws
SQLException
```

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** cal

- the

Calendar

object the driver will use
to construct the timestamp
**Returns:** the parameter value. If the value is SQL

NULL

, the result is

null

.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setTimestamp(java.lang.String, java.sql.Timestamp)

---

#### getTimestamp

Timestamp

getTimestamp​(

String

parameterName,

Calendar

cal)
throws

SQLException

Retrieves the value of a JDBC

TIMESTAMP

parameter as a

java.sql.Timestamp

object, using
the given

Calendar

object to construct
the

Timestamp

object.
With a

Calendar

object, the driver
can calculate the timestamp taking into account a custom timezone and locale.
If no

Calendar

object is specified, the driver uses the
default timezone and locale.

getURL

```java
URL
getURL​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

java.net.URL

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs,
this method is called on a closed

CallableStatement

,
or if there is a problem with the URL
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** setURL(java.lang.String, java.net.URL)

---

#### getURL

URL

getURL​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

DATALINK

parameter as a

java.net.URL

object.

getRowId

```java
RowId
getRowId​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getRowId

RowId

getRowId​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

getRowId

```java
RowId
getRowId​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

RowId

object that represents the JDBC

ROWID

value is used as the designated parameter. If the parameter contains
a SQL

NULL

, then a

null

value is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getRowId

RowId

getRowId​(

String

parameterName)
throws

SQLException

Retrieves the value of the designated JDBC

ROWID

parameter as a

java.sql.RowId

object.

setRowId

```java
void setRowId​(
String
parameterName,

RowId
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

when it sends it to the
database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setRowId

void setRowId​(

String

parameterName,

RowId

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

when it sends it to the
database.

setNString

```java
void setNString​(
String
parameterName,

String
value)
throws
SQLException
```

Sets the designated parameter to the given

String

object.
The driver converts this to a SQL

NCHAR

or

NVARCHAR

or

LONGNVARCHAR

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setNString

void setNString​(

String

parameterName,

String

value)
throws

SQLException

Sets the designated parameter to the given

String

object.
The driver converts this to a SQL

NCHAR

or

NVARCHAR

or

LONGNVARCHAR

setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setNCharacterStream

void setNCharacterStream​(

String

parameterName,

Reader

value,
long length)
throws

SQLException

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

setNClob

```java
void setNClob​(
String
parameterName,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The object
implements the

java.sql.NClob

interface. This

NClob

object maps to a SQL

NCLOB

.

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setNClob

void setNClob​(

String

parameterName,

NClob

value)
throws

SQLException

Sets the designated parameter to a

java.sql.NClob

object. The object
implements the

java.sql.NClob

interface. This

NClob

object maps to a SQL

NCLOB

.

setClob

```java
void setClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setClob

void setClob​(

String

parameterName,

Reader

reader,
long length)
throws

SQLException

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
The

Inputstream

must contain the number
of characters specified by length, otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setBinaryStream (int, InputStream, int)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

**Parameters:** parameterName

- the name of the parameter to be set
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match the specified length; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setBlob

void setBlob​(

String

parameterName,

InputStream

inputStream,
long length)
throws

SQLException

Sets the designated parameter to an

InputStream

object.
The

Inputstream

must contain the number
of characters specified by length, otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setBinaryStream (int, InputStream, int)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterName

- the name of the parameter to be set
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the length specified is less than zero;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setNClob

void setNClob​(

String

parameterName,

Reader

reader,
long length)
throws

SQLException

Sets the designated parameter to a

Reader

object. The

reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

CallableStatement

is executed.
This method differs from the

setCharacterStream (int, Reader, int)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

getNClob

```java
NClob
getNClob​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and
so on
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

, the
value

null

is returned.
**Throws:** SQLException

- if the parameterIndex is not valid;
if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getNClob

NClob

getNClob​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

getNClob

```java
NClob
getNClob​(
String
parameterName)
throws
SQLException
```

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** the parameter value as a

NClob

object in the
Java programming language. If the value was SQL

NULL

,
the value

null

is returned.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getNClob

NClob

getNClob​(

String

parameterName)
throws

SQLException

Retrieves the value of a JDBC

NCLOB

parameter as a

java.sql.NClob

object in the Java programming language.

setSQLXML

```java
void setSQLXML​(
String
parameterName,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an

SQL XML

value when it sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** xmlObject

- a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs;
this method is called on a closed

CallableStatement

or
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed for the

SQLXML

object
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setSQLXML

void setSQLXML​(

String

parameterName,

SQLXML

xmlObject)
throws

SQLException

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an

SQL XML

value when it sends it to the database.

getSQLXML

```java
SQLXML
getSQLXML​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getSQLXML

SQLXML

getSQLXML​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

getSQLXML

```java
SQLXML
getSQLXML​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

SQLXML

object that maps an

SQL XML

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getSQLXML

SQLXML

getSQLXML​(

String

parameterName)
throws

SQLException

Retrieves the value of the designated

SQL XML

parameter as a

java.sql.SQLXML

object in the Java programming language.

getNString

```java
String
getNString​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

---

#### getNString

String

getNString​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

getNString

```java
String
getNString​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

String

object that maps an

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6
**See Also:** setNString(java.lang.String, java.lang.String)

---

#### getNString

String

getNString​(

String

parameterName)
throws

SQLException

Retrieves the value of the designated

NCHAR

,

NVARCHAR

or

LONGNVARCHAR

parameter as
a

String

in the Java programming language.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

For the fixed-length type JDBC

NCHAR

,
the

String

object
returned has exactly the same value the SQL

NCHAR

value had in the
database, including any padding added by the database.

getNCharacterStream

```java
Reader
getNCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getNCharacterStream

Reader

getNCharacterStream​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

getNCharacterStream

```java
Reader
getNCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getNCharacterStream

Reader

getNCharacterStream​(

String

parameterName)
throws

SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.
It is intended for use when
accessing

NCHAR

,

NVARCHAR

and

LONGNVARCHAR

parameters.

getCharacterStream

```java
Reader
getCharacterStream​(int parameterIndex)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language.
**Throws:** SQLException

- if the parameterIndex is not valid; if a database access error occurs or
this method is called on a closed

CallableStatement
**Since:** 1.6

---

#### getCharacterStream

Reader

getCharacterStream​(int parameterIndex)
throws

SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

getCharacterStream

```java
Reader
getCharacterStream​(
String
parameterName)
throws
SQLException
```

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

**Parameters:** parameterName

- the name of the parameter
**Returns:** a

java.io.Reader

object that contains the parameter
value; if the value is SQL

NULL

, the value returned is

null

in the Java programming language
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### getCharacterStream

Reader

getCharacterStream​(

String

parameterName)
throws

SQLException

Retrieves the value of the designated parameter as a

java.io.Reader

object in the Java programming language.

setBlob

```java
void setBlob​(
String
parameterName,

Blob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Blob

object.
The driver converts this to an SQL

BLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Blob

object that maps an SQL

BLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setBlob

void setBlob​(

String

parameterName,

Blob

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.Blob

object.
The driver converts this to an SQL

BLOB

value when it
sends it to the database.

setClob

```java
void setClob​(
String
parameterName,

Clob
x)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.Clob

object.
The driver converts this to an SQL

CLOB

value when it
sends it to the database.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- a

Clob

object that maps an SQL

CLOB

value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setClob

void setClob​(

String

parameterName,

Clob

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.Clob

object.
The driver converts this to an SQL

CLOB

value when it
sends it to the database.

setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setAsciiStream

void setAsciiStream​(

String

parameterName,

InputStream

x,
long length)
throws

SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x,
long length)
throws
SQLException
```

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setBinaryStream

void setBinaryStream​(

String

parameterName,

InputStream

x,
long length)
throws

SQLException

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the stream
as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that
contains the UNICODE data used as the designated parameter
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.6

---

#### setCharacterStream

void setCharacterStream​(

String

parameterName,

Reader

reader,
long length)
throws

SQLException

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

setAsciiStream

```java
void setAsciiStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setAsciiStream

void setAsciiStream​(

String

parameterName,

InputStream

x)
throws

SQLException

Sets the designated parameter to the given input stream.
When a very large ASCII value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.InputStream

. Data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from ASCII to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setAsciiStream

which takes a length parameter.

setBinaryStream

```java
void setBinaryStream​(
String
parameterName,

InputStream
x)
throws
SQLException
```

Sets the designated parameter to the given input stream.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the
stream as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setBinaryStream

void setBinaryStream​(

String

parameterName,

InputStream

x)
throws

SQLException

Sets the designated parameter to the given input stream.
When a very large binary value is input to a

LONGVARBINARY

parameter, it may be more practical to send it via a

java.io.InputStream

object. The data will be read from the
stream as needed until end-of-file is reached.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBinaryStream

which takes a length parameter.

setCharacterStream

```java
void setCharacterStream​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to the given

Reader

object.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setCharacterStream

void setCharacterStream​(

String

parameterName,

Reader

reader)
throws

SQLException

Sets the designated parameter to the given

Reader

object.
When a very large UNICODE value is input to a

LONGVARCHAR

parameter, it may be more practical to send it via a

java.io.Reader

object. The data will be read from the stream
as needed until end-of-file is reached. The JDBC driver will
do any necessary conversion from UNICODE to the database char format.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setCharacterStream

which takes a length parameter.

setNCharacterStream

```java
void setNCharacterStream​(
String
parameterName,

Reader
value)
throws
SQLException
```

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; if a database access error occurs; or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setNCharacterStream

void setNCharacterStream​(

String

parameterName,

Reader

value)
throws

SQLException

Sets the designated parameter to a

Reader

object. The

Reader

reads the data till end-of-file is reached. The
driver does the necessary conversion from Java character format to
the national character set in the database.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNCharacterStream

which takes a length parameter.

setClob

```java
void setClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or this method is called on
a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setClob

void setClob​(

String

parameterName,

Reader

reader)
throws

SQLException

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

CLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

setBlob

```java
void setBlob​(
String
parameterName,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to an

InputStream

object.
This method differs from the

setBinaryStream (int, InputStream)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setBlob

void setBlob​(

String

parameterName,

InputStream

inputStream)
throws

SQLException

Sets the designated parameter to an

InputStream

object.
This method differs from the

setBinaryStream (int, InputStream)

method because it informs the driver that the parameter value should be
sent to the server as a

BLOB

. When the

setBinaryStream

method is used,
the driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

setNClob

```java
void setNClob​(
String
parameterName,

Reader
reader)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setNClob

void setNClob​(

String

parameterName,

Reader

reader)
throws

SQLException

Sets the designated parameter to a

Reader

object.
This method differs from the

setCharacterStream (int, Reader)

method
because it informs the driver that the parameter value should be sent to
the server as a

NCLOB

. When the

setCharacterStream

method is used, the
driver may have to do extra work to determine whether the parameter
data should be send to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

getObject

```java
<T> T getObject​(int parameterIndex,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, and so on
**Parameters:** type

- Class representing the Java data type to convert the
designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

---

#### getObject

<T> T getObject​(int parameterIndex,

Class

<T> type)
throws

SQLException

Returns an object representing the value of OUT parameter

parameterIndex

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

getObject

```java
<T> T getObject​(
String
parameterName,

Class
<T> type)
throws
SQLException
```

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** parameterName

- the name of the parameter
**Parameters:** type

- Class representing the Java data type to convert
the designated parameter to.
**Returns:** an instance of

type

holding the OUT parameter
value
**Throws:** SQLException

- if conversion is not supported, type is null or
another error occurs. The getCause() method of the
exception may provide a more detailed exception, for example, if
a conversion error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.7

---

#### getObject

<T> T getObject​(

String

parameterName,

Class

<T> type)
throws

SQLException

Returns an object representing the value of OUT parameter

parameterName

and will convert from the
SQL type of the parameter to the requested Java data type, if the
conversion is supported. If the conversion is not
supported or null is specified for the type, a

SQLException

is thrown.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

At a minimum, an implementation must support the conversions defined in
Appendix B, Table B-3 and conversion of appropriate user defined SQL
types to a Java type which implements

SQLData

, or

Struct

.
Additional conversions may be supported and are vendor defined.

setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

If the second argument is an

InputStream

then the stream
must contain the number of bytes specified by scaleOrLength.
If the second argument is a

Reader

then the reader must
contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver
will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be
sent to the database. The scale argument may further qualify this type.
**Parameters:** scaleOrLength

- for

java.sql.JDBCType.DECIMAL

or

java.sql.JDBCType.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or reader. For all other types,
this value will be ignored.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement

or
if the Java Object specified by x is an InputStream
or Reader object and the value of the scale parameter is less
than zero
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### setObject

default void setObject​(

String

parameterName,

Object

x,

SQLType

targetSqlType,
int scaleOrLength)
throws

SQLException

Sets the value of the designated parameter with the given object.

If the second argument is an

InputStream

then the stream
must contain the number of bytes specified by scaleOrLength.
If the second argument is a

Reader

then the reader must
contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver
will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

The given Java object will be converted to the given targetSqlType
before being sent to the database.

If the object has a custom mapping (is of a class implementing the
interface

SQLData

),
the JDBC driver should call the method

SQLData.writeSQL

to
write it to the SQL data stream.
If, on the other hand, the object is of a class implementing

Ref

,

Blob

,

Clob

,

NClob

,

Struct

,

java.net.URL

,
or

Array

, the driver should pass it to the database as a
value of the corresponding SQL type.

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

Note that this method may be used to pass database-specific
abstract data types.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

setObject

```java
default void setObject​(
String
parameterName,

Object
x,

SQLType
targetSqlType)
throws
SQLException
```

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, SQLType targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type to be sent to the database
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs
or this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified targetSqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### setObject

default void setObject​(

String

parameterName,

Object

x,

SQLType

targetSqlType)
throws

SQLException

Sets the value of the designated parameter with the given object.

This method is similar to

setObject(String parameterName,
Object x, SQLType targetSqlType, int scaleOrLength)

,
except that it assumes a scale of zero.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(int parameterIndex,

SQLType

sqlType)
throws

SQLException

Registers the OUT parameter in ordinal position

parameterIndex

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

may be

JDBCType.OTHER

or a

SQLType

that is supported by
the JDBC driver. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,
and so on
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(int parameterIndex,

SQLType

sqlType,
int scale)
throws

SQLException

Registers the parameter in ordinal position

parameterIndex

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(int parameterIndex,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter.
Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2,...
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if the parameterIndex is not valid;
if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(int parameterIndex,

SQLType

sqlType,

String

typeName)
throws

SQLException

Registers the designated output parameter.
This version of
the method

registerOutParameter

should be used for a user-defined or

REF

output parameter.
Examples
of user-defined types include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

All OUT parameters must be registered
before a stored procedure is executed.

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

For a user-defined parameter, the fully-qualified SQL
type name of the parameter should also be given, while a

REF

parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-defined and

REF

parameters.

Although it is intended for user-defined and

REF

parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type, the

typeName

parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

Note:

When reading the value of an out parameter, you
must use the getter method whose Java type corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType)
throws
SQLException
```

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
If the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

, the version of

registerOutParameter

that accepts a scale value
should be used.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(

String

parameterName,

SQLType

sqlType)
throws

SQLException

Registers the OUT parameter named

parameterName

to the JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

If the JDBC type expected to be returned to this output parameter
is specific to this particular database,

sqlType

should be

JDBCType.OTHER

or a

SQLType

that is supported
by the JDBC driver.. The method

getObject(int)

retrieves the value.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,
int scale)
throws
SQLException
```

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** scale

- the desired number of digits to the right of the
decimal point. It must be greater than or equal to zero.
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support
this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(

String

parameterName,

SQLType

sqlType,
int scale)
throws

SQLException

Registers the parameter named

parameterName

to be of JDBC type

sqlType

. All OUT parameters must be registered
before a stored procedure is executed.

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

The JDBC type specified by

sqlType

for an OUT
parameter determines the Java type that must be used
in the

get

method to read the value of that parameter.

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

This version of

registerOutParameter

should be
used when the parameter is of JDBC type

JDBCType.NUMERIC

or

JDBCType.DECIMAL

.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

registerOutParameter

```java
default void registerOutParameter​(
String
parameterName,

SQLType
sqlType,

String
typeName)
throws
SQLException
```

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

**Parameters:** parameterName

- the name of the parameter
**Parameters:** sqlType

- the JDBC type code defined by

SQLType

to use to
register the OUT Parameter.
**Parameters:** typeName

- the fully-qualified name of an SQL structured type
**Throws:** SQLException

- if parameterName does not correspond to a named
parameter; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if
the JDBC driver does not support the specified sqlType
or if the JDBC driver does not support this method
**Since:** 1.8
**See Also:** JDBCType

,

SQLType

---

#### registerOutParameter

default void registerOutParameter​(

String

parameterName,

SQLType

sqlType,

String

typeName)
throws

SQLException

Registers the designated output parameter. This version of
the method

registerOutParameter

should be used for a user-named or REF output parameter. Examples
of user-named types include: STRUCT, DISTINCT, JAVA_OBJECT, and
named array types.

All OUT parameters must be registered
before a stored procedure is executed.

For a user-named parameter the fully-qualified SQL
type name of the parameter should also be given, while a REF
parameter requires that the fully-qualified type name of the
referenced type be given. A JDBC driver that does not need the
type code and type name information may ignore it. To be portable,
however, applications should always provide these values for
user-named and REF parameters.

Although it is intended for user-named and REF parameters,
this method may be used to register a parameter of any JDBC type.
If the parameter does not have a user-named or REF type, the
typeName parameter is ignored.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

All OUT parameters must be registered
before a stored procedure is executed.

Note:

When reading the value of an out parameter, you
must use the

getXXX

method whose Java type XXX corresponds to the
parameter's registered SQL type.

The default implementation will throw

SQLFeatureNotSupportedException

The default implementation will throw

SQLFeatureNotSupportedException

---

