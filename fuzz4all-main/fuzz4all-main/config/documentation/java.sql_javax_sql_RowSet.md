# Interface RowSet

**Source:** `java.sql\javax\sql\RowSet.html`

### Class Description

```java
public interface
RowSet

extends
ResultSet
```

The interface that adds support to the JDBC API for the
JavaBeans™ component model.
A rowset, which can be used as a JavaBeans component in
a visual Bean development environment, can be created and
configured at design time and executed at run time.

The

RowSet

interface provides a set of JavaBeans properties that allow a

RowSet

instance to be configured to connect to a JDBC data source and read
some data from the data source. A group of setter methods (

setInt

,

setBytes

,

setString

, and so on)
provide a way to pass input parameters to a rowset's command property.
This command is the SQL query the rowset uses when it gets its data from
a relational database, which is generally the case.

The

RowSet

interface supports JavaBeans events, allowing other components in an
application to be notified when an event occurs on a rowset,
such as a change in its value.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

**All Superinterfaces:** AutoCloseable

,

ResultSet

,

Wrapper

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getUrl()
throws
SQLException

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.
The default value is

null

.

**Returns:**
- a string url

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setUrl(java.lang.String)

---

#### void setUrl​(
String
url)
throws
SQLException

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Setting this property is optional. If a URL is used, a JDBC driver
that accepts the URL must be loaded before the
rowset is used to connect to a database. The rowset will use the URL
internally to create a database connection when reading or writing
data. Either a URL or a data source name is used to create a
connection, whichever was set to non null value most recently.

**Parameters:**
- url

- a string value; may be

null

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getUrl()

---

#### String
getDataSourceName()

Retrieves the logical name that identifies the data source for this

RowSet

object.

**Returns:**
- a data source name

**See Also:**
- setDataSourceName(java.lang.String)

,

setUrl(java.lang.String)

---

#### void setDataSourceName​(
String
name)
throws
SQLException

Sets the data source name property for this

RowSet

object to the
given

String

.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

**Parameters:**
- name

- the logical name of the data source for this

RowSet

object; may be

null

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getDataSourceName()

---

#### String
getUsername()

Retrieves the username used to create a database connection for this

RowSet

object.
The username property is set at run time before calling the method

execute

. It is
not usually part of the serialized state of a

RowSet

object.

**Returns:**
- the username property

**See Also:**
- setUsername(java.lang.String)

---

#### void setUsername​(
String
name)
throws
SQLException

Sets the username property for this

RowSet

object to the
given

String

.

**Parameters:**
- name

- a user name

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getUsername()

---

#### String
getPassword()

Retrieves the password used to create a database connection.
The password property is set at run time before calling the method

execute

. It is not usually part of the serialized state
of a

RowSet

object.

**Returns:**
- the password for making a database connection

**See Also:**
- setPassword(java.lang.String)

---

#### void setPassword​(
String
password)
throws
SQLException

Sets the database password for this

RowSet

object to
the given

String

.

**Parameters:**
- password

- the password string

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getPassword()

---

#### int getTransactionIsolation()

Retrieves the transaction isolation level set for this

RowSet

object.

**Returns:**
- the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE

**See Also:**
- setTransactionIsolation(int)

---

#### void setTransactionIsolation​(int level)
throws
SQLException

Sets the transaction isolation level for this

RowSet

object.

**Parameters:**
- level

- the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getTransactionIsolation()

---

#### Map
<
String
,​
Class
<?>> getTypeMap()
throws
SQLException

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any. The default is for the
type map to be empty.

**Returns:**
- a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setTypeMap(java.util.Map<java.lang.String, java.lang.Class<?>>)

---

#### void setTypeMap​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object. This type map will be
used unless another type map is supplied as a method parameter.

**Parameters:**
- map

- a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getTypeMap()

---

#### String
getCommand()

Retrieves this

RowSet

object's command property.

The command property contains a command string, which must be an SQL
query, that can be executed to fill the rowset with data.
The default value is

null

.

**Returns:**
- the command string; may be

null

**See Also:**
- setCommand(java.lang.String)

---

#### void setCommand​(
String
cmd)
throws
SQLException

Sets this

RowSet

object's command property to the given
SQL query.

This property is optional
when a rowset gets its data from a data source that does not support
commands, such as a spreadsheet.

**Parameters:**
- cmd

- the SQL query that will be used to get the data for this

RowSet

object; may be

null

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getCommand()

---

#### boolean isReadOnly()

Retrieves whether this

RowSet

object is read-only.
If updates are possible, the default is for a rowset to be
updatable.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

**Returns:**
- true

if this

RowSet

object is
read-only;

false

if it is updatable

**See Also:**
- setReadOnly(boolean)

---

#### void setReadOnly​(boolean value)
throws
SQLException

Sets whether this

RowSet

object is read-only to the
given

boolean

.

**Parameters:**
- value

-

true

if read-only;

false

if
updatable

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- isReadOnly()

---

#### int getMaxFieldSize()
throws
SQLException

Retrieves the maximum number of bytes that may be returned
for certain column values.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.

**Returns:**
- the current maximum column size limit; zero means that there
is no limit

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setMaxFieldSize(int)

---

#### void setMaxFieldSize​(int max)
throws
SQLException

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.
For maximum portability, use values greater than 256.

**Parameters:**
- max

- the new max column size limit in bytes; zero means unlimited

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getMaxFieldSize()

---

#### int getMaxRows()
throws
SQLException

Retrieves the maximum number of rows that this

RowSet

object can contain.
If the limit is exceeded, the excess rows are silently dropped.

**Returns:**
- the current maximum number of rows that this

RowSet

object can contain; zero means unlimited

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setMaxRows(int)

---

#### void setMaxRows​(int max)
throws
SQLException

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.
If the limit is exceeded, the excess rows are silently dropped.

**Parameters:**
- max

- the new maximum number of rows; zero means unlimited

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getMaxRows()

---

#### boolean getEscapeProcessing()
throws
SQLException

Retrieves whether escape processing is enabled for this

RowSet

object.
If escape scanning is enabled, which is the default, the driver will do
escape substitution before sending an SQL statement to the database.

**Returns:**
- true

if escape processing is enabled;

false

if it is disabled

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setEscapeProcessing(boolean)

---

#### void setEscapeProcessing​(boolean enable)
throws
SQLException

Sets escape processing for this

RowSet

object on or
off. If escape scanning is on (the default), the driver will do
escape substitution before sending an SQL statement to the database.

**Parameters:**
- enable

-

true

to enable escape processing;

false

to disable it

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getEscapeProcessing()

---

#### int getQueryTimeout()
throws
SQLException

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.
If this limit is exceeded, an

SQLException

is thrown.

**Returns:**
- the current query timeout limit in seconds; zero means
unlimited

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- setQueryTimeout(int)

---

#### void setQueryTimeout​(int seconds)
throws
SQLException

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.
If this limit is exceeded, an

SQLException

is thrown.

**Parameters:**
- seconds

- the new query timeout limit in seconds; zero means
that there is no limit

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- getQueryTimeout()

---

#### void setType​(int type)
throws
SQLException

Sets the type of this

RowSet

object to the given type.
This method is used to change the type of a rowset, which is by
default read-only and non-scrollable.

**Parameters:**
- type

- one of the

ResultSet

constants specifying a type:

ResultSet.TYPE_FORWARD_ONLY

,

ResultSet.TYPE_SCROLL_INSENSITIVE

, or

ResultSet.TYPE_SCROLL_SENSITIVE

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- ResultSet.getType()

---

#### void setConcurrency​(int concurrency)
throws
SQLException

Sets the concurrency of this

RowSet

object to the given
concurrency level. This method is used to change the concurrency level
of a rowset, which is by default

ResultSet.CONCUR_READ_ONLY

**Parameters:**
- concurrency

- one of the

ResultSet

constants specifying a
concurrency level:

ResultSet.CONCUR_READ_ONLY

or

ResultSet.CONCUR_UPDATABLE

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- ResultSet.getConcurrency()

---

#### void setNull​(int parameterIndex,
int sqlType)
throws
SQLException

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- sqlType

- a SQL type code defined by

java.sql.Types

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setNull​(int paramIndex,
int sqlType,

String
typeName)
throws
SQLException

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

. This version of the method

setNull

should be used for SQL user-defined types (UDTs) and

REF

type
parameters. Examples of UDTs include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

**Parameters:**
- paramIndex

- the first parameter is 1, the second is 2, ...
- sqlType

- a value from

java.sql.Types
- typeName

- the fully qualified name of an SQL UDT or the type
name of the SQL structured type being referenced by a

REF

type; ignored if the parameter is not a UDT or

REF

type

**Throws:**
- SQLException

- if a database access error occurs

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
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setBoolean​(int parameterIndex,
boolean x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value. The driver converts this to
an SQL

BIT

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getBoolean(int)

**Since:**
- 1.4

---

#### void setByte​(int parameterIndex,
byte x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value. The driver converts this to
an SQL

TINYINT

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getByte(int)

**Since:**
- 1.4

---

#### void setShort​(int parameterIndex,
short x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value. The driver converts this to
an SQL

SMALLINT

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getShort(int)

**Since:**
- 1.4

---

#### void setInt​(int parameterIndex,
int x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value. The driver converts this to
an SQL

INTEGER

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getInt(int)

**Since:**
- 1.4

---

#### void setLong​(int parameterIndex,
long x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value. The driver converts this to
an SQL

BIGINT

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getLong(int)

**Since:**
- 1.4

---

#### void setFloat​(int parameterIndex,
float x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value. The driver converts this to
an SQL

REAL

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getFloat(int)

**Since:**
- 1.4

---

#### void setDouble​(int parameterIndex,
double x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value. The driver converts this to
an SQL

DOUBLE

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getDouble(int)

**Since:**
- 1.4

---

#### void setBigDecimal​(int parameterIndex,

BigDecimal
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.
The driver converts this to
an SQL

NUMERIC

value before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getBigDecimal(int, int)

**Since:**
- 1.4

---

#### void setString​(int parameterIndex,

String
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value. Before sending it to the
database, the driver converts this to an SQL

VARCHAR

or

LONGVARCHAR

value, depending on the argument's size relative
to the driver's limits on

VARCHAR

values.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getString(int)

**Since:**
- 1.4

---

#### void setBytes​(int parameterIndex,
byte[] x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values. Before sending it to the
database, the driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

value, depending on the argument's size relative
to the driver's limits on

VARBINARY

values.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getBytes(int)

**Since:**
- 1.4

---

#### void setDate​(int parameterIndex,

Date
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value. The driver converts this to
an SQL

DATE

value before sending it to the database, using the
default

java.util.Calendar

to calculate the date.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setTime​(int parameterIndex,

Time
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value. The driver converts this to
an SQL

TIME

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setTimestamp​(int parameterIndex,

Timestamp
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value. The driver converts this to
an SQL

TIMESTAMP

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getTimestamp(int)

**Since:**
- 1.4

---

#### void setAsciiStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large ASCII value via a

java.io.InputStream

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the Java input stream that contains the ASCII parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setBinaryStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large binary value via a

java.io.InputStream

rather than as a

LONGVARBINARY

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the java input stream which contains the binary parameter value
- length

- the number of bytes in the stream

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setCharacterStream​(int parameterIndex,

Reader
reader,
int length)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.
It may be more practical to send a very large UNICODE value via a

java.io.Reader

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- reader

- the

Reader

object that contains the UNICODE data
to be set
- length

- the number of characters in the stream

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.4

---

#### void setAsciiStream​(int parameterIndex,

InputStream
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the Java input stream that contains the ASCII parameter value

**Throws:**
- SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setBinaryStream​(int parameterIndex,

InputStream
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the java input stream which contains the binary parameter value

**Throws:**
- SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setCharacterStream​(int parameterIndex,

Reader
reader)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

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
- parameterIndex

- the first parameter is 1, the second is 2, ...
- reader

- the

java.io.Reader

object that contains the
Unicode data

**Throws:**
- SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setNCharacterStream​(int parameterIndex,

Reader
value)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
to a

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
- parameterIndex

- of the first parameter is 1, the second is 2, ...
- value

- the parameter value

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
this method is called on a closed

PreparedStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setObject​(int parameterIndex,

Object
x,
int targetSqlType,
int scaleOrLength)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

. For integral values, the

java.lang

equivalent objects should be used (for example,
an instance of the class

Integer

for an

int

).

If the second argument is an

InputStream

then the stream must contain
the number of bytes specified by scaleOrLength. If the second argument is a

Reader

then the

Reader

must contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database. The scale argument may further qualify this
type.
- scaleOrLength

- for

java.sql.Types.DECIMAL

or

java.sql.Types.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or

Reader

. For all other types,
this value will be ignored.

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- Types

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

Sets the value of the designated parameter with the given object. The second
argument must be an object type; for integral values, the

java.lang

equivalent objects should be used.

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

Note that this method may be used to pass database-
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

targetSqlType

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

,

ResultSet.getObject(int)

**Since:**
- 1.4

---

#### void setObject​(int parameterIndex,

Object
x,
int targetSqlType)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.
This method is like

setObject

above, but the scale used is the scale
of the second parameter. Scalar values have a scale of zero. Literal
values have the scale present in the literal.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the object containing the input parameter value
- targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database

**Throws:**
- SQLException

- if a database access error occurs

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
This method is like the method

setObject

above, except that it assumes a scale of zero.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if

targetSqlType

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
- ResultSet.getObject(int)

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
The second parameter must be of type

Object

; therefore, the

java.lang

equivalent objects should be used for built-in types.

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

**Parameters:**
- parameterName

- the name of the parameter
- x

- the object containing the input parameter value

**Throws:**
- SQLException

- if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getObject(int)

**Since:**
- 1.4

---

#### void setObject​(int parameterIndex,

Object
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

**Parameters:**
- parameterIndex

- The first parameter is 1, the second is 2, ...
- x

- The object containing the input parameter value

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setRef​(int i,

Ref
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value. The driver will convert this
to the appropriate

REF(<structured-type>)

value.

**Parameters:**
- i

- the first parameter is 1, the second is 2, ...
- x

- an object representing data of an SQL

REF

type

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setBlob​(int i,

Blob
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value. The driver will convert this
to the

BLOB

value that the

Blob

object
represents before sending it to the database.

**Parameters:**
- i

- the first parameter is 1, the second is 2, ...
- x

- an object representing a BLOB

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setBlob​(int parameterIndex,

InputStream
inputStream,
long length)
throws
SQLException

Sets the designated parameter to a

InputStream

object.
The

InputStream

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
- parameterIndex

- index of the first parameter is 1,
the second is 2, ...
- inputStream

- An object that contains the data to set the parameter
value to.
- length

- the number of bytes in the parameter data.

**Throws:**
- SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

,
if parameterIndex does not correspond
to a parameter marker in the SQL statement, if the length specified
is less than zero or if the number of bytes in the

InputStream

does not match
the specified length.
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setBlob​(int parameterIndex,

InputStream
inputStream)
throws
SQLException

Sets the designated parameter to a

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
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:**
- parameterIndex

- index of the first parameter is 1,
the second is 2, ...
- inputStream

- An object that contains the data to set the parameter
value to.

**Throws:**
- SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

or
if parameterIndex does not correspond
to a parameter marker in the SQL statement,
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

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

Sets the designated parameter to a

InputStream

object.
The

InputStream

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

- if parameterIndex does not correspond
to a parameter marker in the SQL statement, or if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match
the specified length; if a database access error occurs or
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

- if a database access error occurs or
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
inputStream)
throws
SQLException

Sets the designated parameter to a

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setClob​(int i,

Clob
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value. The driver will convert this
to the

CLOB

value that the

Clob

object
represents before sending it to the database.

**Parameters:**
- i

- the first parameter is 1, the second is 2, ...
- x

- an object representing a CLOB

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...
- reader

- An object that contains the data to set the parameter value to.
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

, if parameterIndex does not correspond to a parameter
marker in the SQL statement, or if the length specified is less than zero.
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setClob​(int parameterIndex,

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...
- reader

- An object that contains the data to set the parameter value to.

**Throws:**
- SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

or if parameterIndex does not correspond to a parameter
marker in the SQL statement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

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

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
a database access error occurs or
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

- if a database access error occurs or
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

- if a database access error occurs or this method is called on
a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setArray​(int i,

Array
x)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value. The driver will convert this
to the

ARRAY

value that the

Array

object
represents before sending it to the database.

**Parameters:**
- i

- the first parameter is 1, the second is 2, ...
- x

- an object representing an SQL array

**Throws:**
- SQLException

- if a database access error occurs

---

#### void setDate​(int parameterIndex,

Date
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value. The driver will convert this
to an SQL

DATE

value, using the given

java.util.Calendar

object to calculate the date.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value
- cal

- the

java.util.Calendar

object to use for calculating the date

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getDate(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getDate(int)

**Since:**
- 1.4

---

#### void setTime​(int parameterIndex,

Time
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

value. The driver will convert this
to an SQL

TIME

value, using the given

java.util.Calendar

object to calculate it, before sending it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value
- cal

- the

java.util.Calendar

object to use for calculating the time

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getTime(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getTime(int)

**Since:**
- 1.4

---

#### void setTimestamp​(int parameterIndex,

Timestamp
x,

Calendar
cal)
throws
SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value. The driver will
convert this to an SQL

TIMESTAMP

value, using the given

java.util.Calendar

object to calculate it, before sending it to the
database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value
- cal

- the

java.util.Calendar

object to use for calculating the
timestamp

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**See Also:**
- ResultSet.getTimestamp(int)

**Since:**
- 1.4

---

#### void clearParameters()
throws
SQLException

Clears the parameters set for this

RowSet

object's command.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

**Throws:**
- SQLException

- if a database access error occurs

---

#### void execute()
throws
SQLException

Fills this

RowSet

object with data.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

**Throws:**
- SQLException

- if a database access error occurs or any of the
properties necessary for making a connection and creating
a statement have not been set

---

#### void addRowSetListener​(
RowSetListener
listener)

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

**Parameters:**
- listener

- a component that has implemented the

RowSetListener

interface and wants to be notified when events occur on this

RowSet

object

**See Also:**
- removeRowSetListener(javax.sql.RowSetListener)

---

#### void removeRowSetListener​(
RowSetListener
listener)

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

**Parameters:**
- listener

- a component that has been registered as a listener for this

RowSet

object

**See Also:**
- addRowSetListener(javax.sql.RowSetListener)

---

#### void setSQLXML​(int parameterIndex,

SQLXML
xmlObject)
throws
SQLException

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an
SQL

XML

value when it sends it to the database.

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...
- xmlObject

- a

SQLXML

object that maps an SQL

XML

value

**Throws:**
- SQLException

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.

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

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.

**Since:**
- 1.6

---

#### void setRowId​(int parameterIndex,

RowId
x)
throws
SQLException

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

value when it sends it
to the database

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the parameter value

**Throws:**
- SQLException

- if a database access error occurs

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

- if a database access error occurs

**Since:**
- 1.6

---

#### void setNString​(int parameterIndex,

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

value
(depending on the argument's
size relative to the driver's limits on

NVARCHAR

values)
when it sends it to the database.

**Parameters:**
- parameterIndex

- of the first parameter is 1, the second is 2, ...
- value

- the parameter value

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs

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

- the name of the column to be set
- value

- the parameter value

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs

**Since:**
- 1.6

---

#### void setNCharacterStream​(int parameterIndex,

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
- parameterIndex

- of the first parameter is 1, the second is 2, ...
- value

- the parameter value
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs

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

- the name of the column to be set
- value

- the parameter value
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs

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

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
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

- the name of the column to be set
- value

- the parameter value

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs

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

object.
The

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
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

- if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setNClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...
- reader

- An object that contains the data to set the parameter value to.
- length

- the number of characters in the parameter data.

**Throws:**
- SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setNClob​(int parameterIndex,

NClob
value)
throws
SQLException

Sets the designated parameter to a

java.sql.NClob

object. The driver converts this to a
SQL

NCLOB

value when it sends it to the database.

**Parameters:**
- parameterIndex

- of the first parameter is 1, the second is 2, ...
- value

- the parameter value

**Throws:**
- SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs

**Since:**
- 1.6

---

#### void setNClob​(int parameterIndex,

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:**
- parameterIndex

- index of the first parameter is 1, the second is 2, ...
- reader

- An object that contains the data to set the parameter value to.

**Throws:**
- SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.6

---

#### void setURL​(int parameterIndex,

URL
x)
throws
SQLException

Sets the designated parameter to the given

java.net.URL

value.
The driver converts this to an SQL

DATALINK

value
when it sends it to the database.

**Parameters:**
- parameterIndex

- the first parameter is 1, the second is 2, ...
- x

- the

java.net.URL

object to be set

**Throws:**
- SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
- SQLFeatureNotSupportedException

- if the JDBC driver does not support this method

**Since:**
- 1.4

---

### Additional Sections

#### Interface RowSet

**All Superinterfaces:** AutoCloseable

,

ResultSet

,

Wrapper

**All Known Subinterfaces:** CachedRowSet

,

FilteredRowSet

,

JdbcRowSet

,

JoinRowSet

,

SyncResolver

,

WebRowSet

```java
public interface
RowSet

extends
ResultSet
```

The interface that adds support to the JDBC API for the
JavaBeans™ component model.
A rowset, which can be used as a JavaBeans component in
a visual Bean development environment, can be created and
configured at design time and executed at run time.

The

RowSet

interface provides a set of JavaBeans properties that allow a

RowSet

instance to be configured to connect to a JDBC data source and read
some data from the data source. A group of setter methods (

setInt

,

setBytes

,

setString

, and so on)
provide a way to pass input parameters to a rowset's command property.
This command is the SQL query the rowset uses when it gets its data from
a relational database, which is generally the case.

The

RowSet

interface supports JavaBeans events, allowing other components in an
application to be notified when an event occurs on a rowset,
such as a change in its value.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

**Since:** 1.4

public interface

RowSet

extends

ResultSet

The interface that adds support to the JDBC API for the
JavaBeans™ component model.
A rowset, which can be used as a JavaBeans component in
a visual Bean development environment, can be created and
configured at design time and executed at run time.

The

RowSet

interface provides a set of JavaBeans properties that allow a

RowSet

instance to be configured to connect to a JDBC data source and read
some data from the data source. A group of setter methods (

setInt

,

setBytes

,

setString

, and so on)
provide a way to pass input parameters to a rowset's command property.
This command is the SQL query the rowset uses when it gets its data from
a relational database, which is generally the case.

The

RowSet

interface supports JavaBeans events, allowing other components in an
application to be notified when an event occurs on a rowset,
such as a change in its value.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

The

RowSet

interface provides a set of JavaBeans properties that allow a

RowSet

instance to be configured to connect to a JDBC data source and read
some data from the data source. A group of setter methods (

setInt

,

setBytes

,

setString

, and so on)
provide a way to pass input parameters to a rowset's command property.
This command is the SQL query the rowset uses when it gets its data from
a relational database, which is generally the case.

The

RowSet

interface supports JavaBeans events, allowing other components in an
application to be notified when an event occurs on a rowset,
such as a change in its value.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

The

RowSet

interface supports JavaBeans events, allowing other components in an
application to be notified when an event occurs on a rowset,
such as a change in its value.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

The

RowSet

interface is unique in that it is intended to be
implemented using the rest of the JDBC API. In other words, a

RowSet

implementation is a layer of software that executes "on top"
of a JDBC driver. Implementations of the

RowSet

interface can
be provided by anyone, including JDBC driver vendors who want to
provide a

RowSet

implementation as part of their JDBC products.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

A

RowSet

object may make a connection with a data source and
maintain that connection throughout its life cycle, in which case it is
called a

connected

rowset. A rowset may also make a connection with
a data source, get data from it, and then close the connection. Such a rowset
is called a

disconnected

rowset. A disconnected rowset may make
changes to its data while it is disconnected and then send the changes back
to the original source of the data, but it must reestablish a connection to do so.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

A disconnected rowset may have a

Reader

(a

RowSetReader

object)
and a writer (a

RowSetWriter

object) associated with it.
The

Reader

may be implemented in many different ways to populate a rowset
with data, including getting data from a non-relational data source. The
writer can also be implemented in many different ways to propagate changes
made to the rowset's data back to the underlying data source.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

Rowsets are easy to use. The

RowSet

interface extends the standard

java.sql.ResultSet

interface. The

RowSetMetaData

interface extends the

java.sql.ResultSetMetaData

interface.
Thus, developers familiar
with the JDBC API will have to learn a minimal number of new APIs to
use rowsets. In addition, third-party software tools that work with
JDBC

ResultSet

objects will also easily be made to work with rowsets.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.sql.

ResultSet

CLOSE_CURSORS_AT_COMMIT

,

CONCUR_READ_ONLY

,

CONCUR_UPDATABLE

,

FETCH_FORWARD

,

FETCH_REVERSE

,

FETCH_UNKNOWN

,

HOLD_CURSORS_OVER_COMMIT

,

TYPE_FORWARD_ONLY

,

TYPE_SCROLL_INSENSITIVE

,

TYPE_SCROLL_SENSITIVE

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addRowSetListener

​(

RowSetListener

listener)

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

void

clearParameters

()

Clears the parameters set for this

RowSet

object's command.

void

execute

()

Fills this

RowSet

object with data.

String

getCommand

()

Retrieves this

RowSet

object's command property.

String

getDataSourceName

()

Retrieves the logical name that identifies the data source for this

RowSet

object.

boolean

getEscapeProcessing

()

Retrieves whether escape processing is enabled for this

RowSet

object.

int

getMaxFieldSize

()

Retrieves the maximum number of bytes that may be returned
for certain column values.

int

getMaxRows

()

Retrieves the maximum number of rows that this

RowSet

object can contain.

String

getPassword

()

Retrieves the password used to create a database connection.

int

getQueryTimeout

()

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.

int

getTransactionIsolation

()

Retrieves the transaction isolation level set for this

RowSet

object.

Map

<

String

,​

Class

<?>>

getTypeMap

()

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any.

String

getUrl

()

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.

String

getUsername

()

Retrieves the username used to create a database connection for this

RowSet

object.

boolean

isReadOnly

()

Retrieves whether this

RowSet

object is read-only.

void

removeRowSetListener

​(

RowSetListener

listener)

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

void

setArray

​(int i,

Array

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value.

void

setAsciiStream

​(int parameterIndex,

InputStream

x)

Sets the designated parameter in this

RowSet

object's command
to the given input stream.

void

setAsciiStream

​(int parameterIndex,

InputStream

x,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.

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

setBigDecimal

​(int parameterIndex,

BigDecimal

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.

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

​(int parameterIndex,

InputStream

x)

Sets the designated parameter in this

RowSet

object's command
to the given input stream.

void

setBinaryStream

​(int parameterIndex,

InputStream

x,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

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

setBlob

​(int parameterIndex,

InputStream

inputStream)

Sets the designated parameter to a

InputStream

object.

void

setBlob

​(int parameterIndex,

InputStream

inputStream,
long length)

Sets the designated parameter to a

InputStream

object.

void

setBlob

​(int i,

Blob

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value.

void

setBlob

​(

String

parameterName,

InputStream

inputStream)

Sets the designated parameter to a

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

Sets the designated parameter to a

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

​(int parameterIndex,
boolean x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value.

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

​(int parameterIndex,
byte x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

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

​(int parameterIndex,
byte[] x)

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values.

void

setBytes

​(

String

parameterName,
byte[] x)

Sets the designated parameter to the given Java array of bytes.

void

setCharacterStream

​(int parameterIndex,

Reader

reader)

Sets the designated parameter in this

RowSet

object's command
to the given

Reader

object.

void

setCharacterStream

​(int parameterIndex,

Reader

reader,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.

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

setClob

​(int parameterIndex,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setClob

​(int parameterIndex,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setClob

​(int i,

Clob

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value.

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

setCommand

​(

String

cmd)

Sets this

RowSet

object's command property to the given
SQL query.

void

setConcurrency

​(int concurrency)

Sets the concurrency of this

RowSet

object to the given
concurrency level.

void

setDataSourceName

​(

String

name)

Sets the data source name property for this

RowSet

object to the
given

String

.

void

setDate

​(int parameterIndex,

Date

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value.

void

setDate

​(int parameterIndex,

Date

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value.

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

​(int parameterIndex,
double x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value.

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

setEscapeProcessing

​(boolean enable)

Sets escape processing for this

RowSet

object on or
off.

void

setFloat

​(int parameterIndex,
float x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

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

​(int parameterIndex,
int x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

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

​(int parameterIndex,
long x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

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

setMaxFieldSize

​(int max)

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.

void

setMaxRows

​(int max)

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.

void

setNCharacterStream

​(int parameterIndex,

Reader

value)

Sets the designated parameter in this

RowSet

object's command
to a

Reader

object.

void

setNCharacterStream

​(int parameterIndex,

Reader

value,
long length)

Sets the designated parameter to a

Reader

object.

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

​(int parameterIndex,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(int parameterIndex,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(int parameterIndex,

NClob

value)

Sets the designated parameter to a

java.sql.NClob

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

​(int parameterIndex,

String

value)

Sets the designated parameter to the given

String

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

​(int parameterIndex,
int sqlType)

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

void

setNull

​(int paramIndex,
int sqlType,

String

typeName)

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

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

​(int parameterIndex,

Object

x)

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

.

void

setObject

​(int parameterIndex,

Object

x,
int targetSqlType)

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

.

void

setObject

​(int parameterIndex,

Object

x,
int targetSqlType,
int scaleOrLength)

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

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

void

setPassword

​(

String

password)

Sets the database password for this

RowSet

object to
the given

String

.

void

setQueryTimeout

​(int seconds)

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.

void

setReadOnly

​(boolean value)

Sets whether this

RowSet

object is read-only to the
given

boolean

.

void

setRef

​(int i,

Ref

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value.

void

setRowId

​(int parameterIndex,

RowId

x)

Sets the designated parameter to the given

java.sql.RowId

object.

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

​(int parameterIndex,
short x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value.

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

​(int parameterIndex,

SQLXML

xmlObject)

Sets the designated parameter to the given

java.sql.SQLXML

object.

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

​(int parameterIndex,

String

x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value.

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

​(int parameterIndex,

Time

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value.

void

setTime

​(int parameterIndex,

Time

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

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

​(int parameterIndex,

Timestamp

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value.

void

setTimestamp

​(int parameterIndex,

Timestamp

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value.

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

setTransactionIsolation

​(int level)

Sets the transaction isolation level for this

RowSet

object.

void

setType

​(int type)

Sets the type of this

RowSet

object to the given type.

void

setTypeMap

​(

Map

<

String

,​

Class

<?>> map)

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object.

void

setUrl

​(

String

url)

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

void

setURL

​(int parameterIndex,

URL

x)

Sets the designated parameter to the given

java.net.URL

value.

void

setUsername

​(

String

name)

Sets the username property for this

RowSet

object to the
given

String

.

- Methods declared in interface java.sql.

ResultSet

absolute

,

afterLast

,

beforeFirst

,

cancelRowUpdates

,

clearWarnings

,

close

,

deleteRow

,

findColumn

,

first

,

getArray

,

getArray

,

getAsciiStream

,

getAsciiStream

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBinaryStream

,

getBinaryStream

,

getBlob

,

getBlob

,

getBoolean

,

getBoolean

,

getByte

,

getByte

,

getBytes

,

getBytes

,

getCharacterStream

,

getCharacterStream

,

getClob

,

getClob

,

getConcurrency

,

getCursorName

,

getDate

,

getDate

,

getDate

,

getDate

,

getDouble

,

getDouble

,

getFetchDirection

,

getFetchSize

,

getFloat

,

getFloat

,

getHoldability

,

getInt

,

getInt

,

getLong

,

getLong

,

getMetaData

,

getNCharacterStream

,

getNCharacterStream

,

getNClob

,

getNClob

,

getNString

,

getNString

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getRef

,

getRef

,

getRow

,

getRowId

,

getRowId

,

getShort

,

getShort

,

getSQLXML

,

getSQLXML

,

getStatement

,

getString

,

getString

,

getTime

,

getTime

,

getTime

,

getTime

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getType

,

getUnicodeStream

,

getUnicodeStream

,

getURL

,

getURL

,

getWarnings

,

insertRow

,

isAfterLast

,

isBeforeFirst

,

isClosed

,

isFirst

,

isLast

,

last

,

moveToCurrentRow

,

moveToInsertRow

,

next

,

previous

,

refreshRow

,

relative

,

rowDeleted

,

rowInserted

,

rowUpdated

,

setFetchDirection

,

setFetchSize

,

updateArray

,

updateArray

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateBigDecimal

,

updateBigDecimal

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBoolean

,

updateBoolean

,

updateByte

,

updateByte

,

updateBytes

,

updateBytes

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateDate

,

updateDate

,

updateDouble

,

updateDouble

,

updateFloat

,

updateFloat

,

updateInt

,

updateInt

,

updateLong

,

updateLong

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNString

,

updateNString

,

updateNull

,

updateNull

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateRef

,

updateRef

,

updateRow

,

updateRowId

,

updateRowId

,

updateShort

,

updateShort

,

updateSQLXML

,

updateSQLXML

,

updateString

,

updateString

,

updateTime

,

updateTime

,

updateTimestamp

,

updateTimestamp

,

wasNull

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

Field Summary

- Fields declared in interface java.sql.

ResultSet

CLOSE_CURSORS_AT_COMMIT

,

CONCUR_READ_ONLY

,

CONCUR_UPDATABLE

,

FETCH_FORWARD

,

FETCH_REVERSE

,

FETCH_UNKNOWN

,

HOLD_CURSORS_OVER_COMMIT

,

TYPE_FORWARD_ONLY

,

TYPE_SCROLL_INSENSITIVE

,

TYPE_SCROLL_SENSITIVE

---

#### Field Summary

Fields declared in interface java.sql.

ResultSet

CLOSE_CURSORS_AT_COMMIT

,

CONCUR_READ_ONLY

,

CONCUR_UPDATABLE

,

FETCH_FORWARD

,

FETCH_REVERSE

,

FETCH_UNKNOWN

,

HOLD_CURSORS_OVER_COMMIT

,

TYPE_FORWARD_ONLY

,

TYPE_SCROLL_INSENSITIVE

,

TYPE_SCROLL_SENSITIVE

---

#### Fields declared in interface java.sql. ResultSet

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addRowSetListener

​(

RowSetListener

listener)

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

void

clearParameters

()

Clears the parameters set for this

RowSet

object's command.

void

execute

()

Fills this

RowSet

object with data.

String

getCommand

()

Retrieves this

RowSet

object's command property.

String

getDataSourceName

()

Retrieves the logical name that identifies the data source for this

RowSet

object.

boolean

getEscapeProcessing

()

Retrieves whether escape processing is enabled for this

RowSet

object.

int

getMaxFieldSize

()

Retrieves the maximum number of bytes that may be returned
for certain column values.

int

getMaxRows

()

Retrieves the maximum number of rows that this

RowSet

object can contain.

String

getPassword

()

Retrieves the password used to create a database connection.

int

getQueryTimeout

()

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.

int

getTransactionIsolation

()

Retrieves the transaction isolation level set for this

RowSet

object.

Map

<

String

,​

Class

<?>>

getTypeMap

()

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any.

String

getUrl

()

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.

String

getUsername

()

Retrieves the username used to create a database connection for this

RowSet

object.

boolean

isReadOnly

()

Retrieves whether this

RowSet

object is read-only.

void

removeRowSetListener

​(

RowSetListener

listener)

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

void

setArray

​(int i,

Array

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value.

void

setAsciiStream

​(int parameterIndex,

InputStream

x)

Sets the designated parameter in this

RowSet

object's command
to the given input stream.

void

setAsciiStream

​(int parameterIndex,

InputStream

x,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.

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

setBigDecimal

​(int parameterIndex,

BigDecimal

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.

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

​(int parameterIndex,

InputStream

x)

Sets the designated parameter in this

RowSet

object's command
to the given input stream.

void

setBinaryStream

​(int parameterIndex,

InputStream

x,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

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

setBlob

​(int parameterIndex,

InputStream

inputStream)

Sets the designated parameter to a

InputStream

object.

void

setBlob

​(int parameterIndex,

InputStream

inputStream,
long length)

Sets the designated parameter to a

InputStream

object.

void

setBlob

​(int i,

Blob

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value.

void

setBlob

​(

String

parameterName,

InputStream

inputStream)

Sets the designated parameter to a

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

Sets the designated parameter to a

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

​(int parameterIndex,
boolean x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value.

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

​(int parameterIndex,
byte x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

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

​(int parameterIndex,
byte[] x)

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values.

void

setBytes

​(

String

parameterName,
byte[] x)

Sets the designated parameter to the given Java array of bytes.

void

setCharacterStream

​(int parameterIndex,

Reader

reader)

Sets the designated parameter in this

RowSet

object's command
to the given

Reader

object.

void

setCharacterStream

​(int parameterIndex,

Reader

reader,
int length)

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.

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

setClob

​(int parameterIndex,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setClob

​(int parameterIndex,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setClob

​(int i,

Clob

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value.

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

setCommand

​(

String

cmd)

Sets this

RowSet

object's command property to the given
SQL query.

void

setConcurrency

​(int concurrency)

Sets the concurrency of this

RowSet

object to the given
concurrency level.

void

setDataSourceName

​(

String

name)

Sets the data source name property for this

RowSet

object to the
given

String

.

void

setDate

​(int parameterIndex,

Date

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value.

void

setDate

​(int parameterIndex,

Date

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value.

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

​(int parameterIndex,
double x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value.

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

setEscapeProcessing

​(boolean enable)

Sets escape processing for this

RowSet

object on or
off.

void

setFloat

​(int parameterIndex,
float x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

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

​(int parameterIndex,
int x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

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

​(int parameterIndex,
long x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

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

setMaxFieldSize

​(int max)

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.

void

setMaxRows

​(int max)

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.

void

setNCharacterStream

​(int parameterIndex,

Reader

value)

Sets the designated parameter in this

RowSet

object's command
to a

Reader

object.

void

setNCharacterStream

​(int parameterIndex,

Reader

value,
long length)

Sets the designated parameter to a

Reader

object.

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

​(int parameterIndex,

Reader

reader)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(int parameterIndex,

Reader

reader,
long length)

Sets the designated parameter to a

Reader

object.

void

setNClob

​(int parameterIndex,

NClob

value)

Sets the designated parameter to a

java.sql.NClob

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

​(int parameterIndex,

String

value)

Sets the designated parameter to the given

String

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

​(int parameterIndex,
int sqlType)

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

void

setNull

​(int paramIndex,
int sqlType,

String

typeName)

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

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

​(int parameterIndex,

Object

x)

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

.

void

setObject

​(int parameterIndex,

Object

x,
int targetSqlType)

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

.

void

setObject

​(int parameterIndex,

Object

x,
int targetSqlType,
int scaleOrLength)

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

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

void

setPassword

​(

String

password)

Sets the database password for this

RowSet

object to
the given

String

.

void

setQueryTimeout

​(int seconds)

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.

void

setReadOnly

​(boolean value)

Sets whether this

RowSet

object is read-only to the
given

boolean

.

void

setRef

​(int i,

Ref

x)

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value.

void

setRowId

​(int parameterIndex,

RowId

x)

Sets the designated parameter to the given

java.sql.RowId

object.

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

​(int parameterIndex,
short x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value.

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

​(int parameterIndex,

SQLXML

xmlObject)

Sets the designated parameter to the given

java.sql.SQLXML

object.

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

​(int parameterIndex,

String

x)

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value.

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

​(int parameterIndex,

Time

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value.

void

setTime

​(int parameterIndex,

Time

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

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

​(int parameterIndex,

Timestamp

x)

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value.

void

setTimestamp

​(int parameterIndex,

Timestamp

x,

Calendar

cal)

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value.

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

setTransactionIsolation

​(int level)

Sets the transaction isolation level for this

RowSet

object.

void

setType

​(int type)

Sets the type of this

RowSet

object to the given type.

void

setTypeMap

​(

Map

<

String

,​

Class

<?>> map)

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object.

void

setUrl

​(

String

url)

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

void

setURL

​(int parameterIndex,

URL

x)

Sets the designated parameter to the given

java.net.URL

value.

void

setUsername

​(

String

name)

Sets the username property for this

RowSet

object to the
given

String

.

- Methods declared in interface java.sql.

ResultSet

absolute

,

afterLast

,

beforeFirst

,

cancelRowUpdates

,

clearWarnings

,

close

,

deleteRow

,

findColumn

,

first

,

getArray

,

getArray

,

getAsciiStream

,

getAsciiStream

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBinaryStream

,

getBinaryStream

,

getBlob

,

getBlob

,

getBoolean

,

getBoolean

,

getByte

,

getByte

,

getBytes

,

getBytes

,

getCharacterStream

,

getCharacterStream

,

getClob

,

getClob

,

getConcurrency

,

getCursorName

,

getDate

,

getDate

,

getDate

,

getDate

,

getDouble

,

getDouble

,

getFetchDirection

,

getFetchSize

,

getFloat

,

getFloat

,

getHoldability

,

getInt

,

getInt

,

getLong

,

getLong

,

getMetaData

,

getNCharacterStream

,

getNCharacterStream

,

getNClob

,

getNClob

,

getNString

,

getNString

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getRef

,

getRef

,

getRow

,

getRowId

,

getRowId

,

getShort

,

getShort

,

getSQLXML

,

getSQLXML

,

getStatement

,

getString

,

getString

,

getTime

,

getTime

,

getTime

,

getTime

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getType

,

getUnicodeStream

,

getUnicodeStream

,

getURL

,

getURL

,

getWarnings

,

insertRow

,

isAfterLast

,

isBeforeFirst

,

isClosed

,

isFirst

,

isLast

,

last

,

moveToCurrentRow

,

moveToInsertRow

,

next

,

previous

,

refreshRow

,

relative

,

rowDeleted

,

rowInserted

,

rowUpdated

,

setFetchDirection

,

setFetchSize

,

updateArray

,

updateArray

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateBigDecimal

,

updateBigDecimal

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBoolean

,

updateBoolean

,

updateByte

,

updateByte

,

updateBytes

,

updateBytes

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateDate

,

updateDate

,

updateDouble

,

updateDouble

,

updateFloat

,

updateFloat

,

updateInt

,

updateInt

,

updateLong

,

updateLong

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNString

,

updateNString

,

updateNull

,

updateNull

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateRef

,

updateRef

,

updateRow

,

updateRowId

,

updateRowId

,

updateShort

,

updateShort

,

updateSQLXML

,

updateSQLXML

,

updateString

,

updateString

,

updateTime

,

updateTime

,

updateTimestamp

,

updateTimestamp

,

wasNull

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Method Summary

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

Clears the parameters set for this

RowSet

object's command.

Fills this

RowSet

object with data.

Retrieves this

RowSet

object's command property.

Retrieves the logical name that identifies the data source for this

RowSet

object.

Retrieves whether escape processing is enabled for this

RowSet

object.

Retrieves the maximum number of bytes that may be returned
for certain column values.

Retrieves the maximum number of rows that this

RowSet

object can contain.

Retrieves the password used to create a database connection.

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.

Retrieves the transaction isolation level set for this

RowSet

object.

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any.

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.

Retrieves the username used to create a database connection for this

RowSet

object.

Retrieves whether this

RowSet

object is read-only.

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value.

Sets the designated parameter in this

RowSet

object's command
to the given input stream.

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.

Sets the designated parameter to the given input stream.

Sets the designated parameter to the given input stream, which will have
the specified number of bytes.

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.

Sets the designated parameter to the given

java.math.BigDecimal

value.

Sets the designated parameter to a

InputStream

object.

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value.

Sets the designated parameter to the given

java.sql.Blob

object.

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value.

Sets the designated parameter to the given Java

boolean

value.

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value.

Sets the designated parameter to the given Java

byte

value.

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values.

Sets the designated parameter to the given Java array of bytes.

Sets the designated parameter in this

RowSet

object's command
to the given

Reader

object.

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.

Sets the designated parameter to the given

Reader

object.

Sets the designated parameter to the given

Reader

object, which is the given number of characters long.

Sets the designated parameter to a

Reader

object.

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value.

Sets the designated parameter to the given

java.sql.Clob

object.

Sets this

RowSet

object's command property to the given
SQL query.

Sets the concurrency of this

RowSet

object to the given
concurrency level.

Sets the data source name property for this

RowSet

object to the
given

String

.

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value.

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value.

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

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value.

Sets the designated parameter to the given Java

double

value.

Sets escape processing for this

RowSet

object on or
off.

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value.

Sets the designated parameter to the given Java

float

value.

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value.

Sets the designated parameter to the given Java

int

value.

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value.

Sets the designated parameter to the given Java

long

value.

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.

Sets the designated parameter in this

RowSet

object's command
to a

Reader

object.

Sets the designated parameter to a

java.sql.NClob

object.

Sets the designated parameter to the given

String

object.

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Sets the designated parameter to SQL

NULL

.

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

.

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

.

Sets the value of the designated parameter with the given object.

Sets the database password for this

RowSet

object to
the given

String

.

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.

Sets whether this

RowSet

object is read-only to the
given

boolean

.

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value.

Sets the designated parameter to the given

java.sql.RowId

object.

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value.

Sets the designated parameter to the given Java

short

value.

Sets the designated parameter to the given

java.sql.SQLXML

object.

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value.

Sets the designated parameter to the given Java

String

value.

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value.

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

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

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value.

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value.

Sets the designated parameter to the given

java.sql.Timestamp

value.

Sets the designated parameter to the given

java.sql.Timestamp

value,
using the given

Calendar

object.

Sets the transaction isolation level for this

RowSet

object.

Sets the type of this

RowSet

object to the given type.

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object.

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Sets the designated parameter to the given

java.net.URL

value.

Sets the username property for this

RowSet

object to the
given

String

.

Methods declared in interface java.sql.

ResultSet

absolute

,

afterLast

,

beforeFirst

,

cancelRowUpdates

,

clearWarnings

,

close

,

deleteRow

,

findColumn

,

first

,

getArray

,

getArray

,

getAsciiStream

,

getAsciiStream

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBigDecimal

,

getBinaryStream

,

getBinaryStream

,

getBlob

,

getBlob

,

getBoolean

,

getBoolean

,

getByte

,

getByte

,

getBytes

,

getBytes

,

getCharacterStream

,

getCharacterStream

,

getClob

,

getClob

,

getConcurrency

,

getCursorName

,

getDate

,

getDate

,

getDate

,

getDate

,

getDouble

,

getDouble

,

getFetchDirection

,

getFetchSize

,

getFloat

,

getFloat

,

getHoldability

,

getInt

,

getInt

,

getLong

,

getLong

,

getMetaData

,

getNCharacterStream

,

getNCharacterStream

,

getNClob

,

getNClob

,

getNString

,

getNString

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getObject

,

getRef

,

getRef

,

getRow

,

getRowId

,

getRowId

,

getShort

,

getShort

,

getSQLXML

,

getSQLXML

,

getStatement

,

getString

,

getString

,

getTime

,

getTime

,

getTime

,

getTime

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getTimestamp

,

getType

,

getUnicodeStream

,

getUnicodeStream

,

getURL

,

getURL

,

getWarnings

,

insertRow

,

isAfterLast

,

isBeforeFirst

,

isClosed

,

isFirst

,

isLast

,

last

,

moveToCurrentRow

,

moveToInsertRow

,

next

,

previous

,

refreshRow

,

relative

,

rowDeleted

,

rowInserted

,

rowUpdated

,

setFetchDirection

,

setFetchSize

,

updateArray

,

updateArray

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateAsciiStream

,

updateBigDecimal

,

updateBigDecimal

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBinaryStream

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBlob

,

updateBoolean

,

updateBoolean

,

updateByte

,

updateByte

,

updateBytes

,

updateBytes

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateCharacterStream

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateClob

,

updateDate

,

updateDate

,

updateDouble

,

updateDouble

,

updateFloat

,

updateFloat

,

updateInt

,

updateInt

,

updateLong

,

updateLong

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNCharacterStream

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNClob

,

updateNString

,

updateNString

,

updateNull

,

updateNull

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateObject

,

updateRef

,

updateRef

,

updateRow

,

updateRowId

,

updateRowId

,

updateShort

,

updateShort

,

updateSQLXML

,

updateSQLXML

,

updateString

,

updateString

,

updateTime

,

updateTime

,

updateTimestamp

,

updateTimestamp

,

wasNull

---

#### Methods declared in interface java.sql. ResultSet

Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Methods declared in interface java.sql. Wrapper

============ METHOD DETAIL ==========

- Method Detail

- getUrl

```java
String
getUrl()
throws
SQLException
```

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.
The default value is

null

.

**Returns:** a string url
**Throws:** SQLException

- if a database access error occurs
**See Also:** setUrl(java.lang.String)

- setUrl

```java
void setUrl​(
String
url)
throws
SQLException
```

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Setting this property is optional. If a URL is used, a JDBC driver
that accepts the URL must be loaded before the
rowset is used to connect to a database. The rowset will use the URL
internally to create a database connection when reading or writing
data. Either a URL or a data source name is used to create a
connection, whichever was set to non null value most recently.

**Parameters:** url

- a string value; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUrl()

- getDataSourceName

```java
String
getDataSourceName()
```

Retrieves the logical name that identifies the data source for this

RowSet

object.

**Returns:** a data source name
**See Also:** setDataSourceName(java.lang.String)

,

setUrl(java.lang.String)

- setDataSourceName

```java
void setDataSourceName​(
String
name)
throws
SQLException
```

Sets the data source name property for this

RowSet

object to the
given

String

.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

**Parameters:** name

- the logical name of the data source for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getDataSourceName()

- getUsername

```java
String
getUsername()
```

Retrieves the username used to create a database connection for this

RowSet

object.
The username property is set at run time before calling the method

execute

. It is
not usually part of the serialized state of a

RowSet

object.

**Returns:** the username property
**See Also:** setUsername(java.lang.String)

- setUsername

```java
void setUsername​(
String
name)
throws
SQLException
```

Sets the username property for this

RowSet

object to the
given

String

.

**Parameters:** name

- a user name
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUsername()

- getPassword

```java
String
getPassword()
```

Retrieves the password used to create a database connection.
The password property is set at run time before calling the method

execute

. It is not usually part of the serialized state
of a

RowSet

object.

**Returns:** the password for making a database connection
**See Also:** setPassword(java.lang.String)

- setPassword

```java
void setPassword​(
String
password)
throws
SQLException
```

Sets the database password for this

RowSet

object to
the given

String

.

**Parameters:** password

- the password string
**Throws:** SQLException

- if a database access error occurs
**See Also:** getPassword()

- getTransactionIsolation

```java
int getTransactionIsolation()
```

Retrieves the transaction isolation level set for this

RowSet

object.

**Returns:** the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**See Also:** setTransactionIsolation(int)

- setTransactionIsolation

```java
void setTransactionIsolation​(int level)
throws
SQLException
```

Sets the transaction isolation level for this

RowSet

object.

**Parameters:** level

- the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTransactionIsolation()

- getTypeMap

```java
Map
<
String
,​
Class
<?>> getTypeMap()
throws
SQLException
```

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any. The default is for the
type map to be empty.

**Returns:** a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** setTypeMap(java.util.Map<java.lang.String, java.lang.Class<?>>)

- setTypeMap

```java
void setTypeMap​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object. This type map will be
used unless another type map is supplied as a method parameter.

**Parameters:** map

- a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTypeMap()

- getCommand

```java
String
getCommand()
```

Retrieves this

RowSet

object's command property.

The command property contains a command string, which must be an SQL
query, that can be executed to fill the rowset with data.
The default value is

null

.

**Returns:** the command string; may be

null
**See Also:** setCommand(java.lang.String)

- setCommand

```java
void setCommand​(
String
cmd)
throws
SQLException
```

Sets this

RowSet

object's command property to the given
SQL query.

This property is optional
when a rowset gets its data from a data source that does not support
commands, such as a spreadsheet.

**Parameters:** cmd

- the SQL query that will be used to get the data for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getCommand()

- isReadOnly

```java
boolean isReadOnly()
```

Retrieves whether this

RowSet

object is read-only.
If updates are possible, the default is for a rowset to be
updatable.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

**Returns:** true

if this

RowSet

object is
read-only;

false

if it is updatable
**See Also:** setReadOnly(boolean)

- setReadOnly

```java
void setReadOnly​(boolean value)
throws
SQLException
```

Sets whether this

RowSet

object is read-only to the
given

boolean

.

**Parameters:** value

-

true

if read-only;

false

if
updatable
**Throws:** SQLException

- if a database access error occurs
**See Also:** isReadOnly()

- getMaxFieldSize

```java
int getMaxFieldSize()
throws
SQLException
```

Retrieves the maximum number of bytes that may be returned
for certain column values.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.

**Returns:** the current maximum column size limit; zero means that there
is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxFieldSize(int)

- setMaxFieldSize

```java
void setMaxFieldSize​(int max)
throws
SQLException
```

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.
For maximum portability, use values greater than 256.

**Parameters:** max

- the new max column size limit in bytes; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxFieldSize()

- getMaxRows

```java
int getMaxRows()
throws
SQLException
```

Retrieves the maximum number of rows that this

RowSet

object can contain.
If the limit is exceeded, the excess rows are silently dropped.

**Returns:** the current maximum number of rows that this

RowSet

object can contain; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxRows(int)

- setMaxRows

```java
void setMaxRows​(int max)
throws
SQLException
```

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.
If the limit is exceeded, the excess rows are silently dropped.

**Parameters:** max

- the new maximum number of rows; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxRows()

- getEscapeProcessing

```java
boolean getEscapeProcessing()
throws
SQLException
```

Retrieves whether escape processing is enabled for this

RowSet

object.
If escape scanning is enabled, which is the default, the driver will do
escape substitution before sending an SQL statement to the database.

**Returns:** true

if escape processing is enabled;

false

if it is disabled
**Throws:** SQLException

- if a database access error occurs
**See Also:** setEscapeProcessing(boolean)

- setEscapeProcessing

```java
void setEscapeProcessing​(boolean enable)
throws
SQLException
```

Sets escape processing for this

RowSet

object on or
off. If escape scanning is on (the default), the driver will do
escape substitution before sending an SQL statement to the database.

**Parameters:** enable

-

true

to enable escape processing;

false

to disable it
**Throws:** SQLException

- if a database access error occurs
**See Also:** getEscapeProcessing()

- getQueryTimeout

```java
int getQueryTimeout()
throws
SQLException
```

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.
If this limit is exceeded, an

SQLException

is thrown.

**Returns:** the current query timeout limit in seconds; zero means
unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setQueryTimeout(int)

- setQueryTimeout

```java
void setQueryTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.
If this limit is exceeded, an

SQLException

is thrown.

**Parameters:** seconds

- the new query timeout limit in seconds; zero means
that there is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** getQueryTimeout()

- setType

```java
void setType​(int type)
throws
SQLException
```

Sets the type of this

RowSet

object to the given type.
This method is used to change the type of a rowset, which is by
default read-only and non-scrollable.

**Parameters:** type

- one of the

ResultSet

constants specifying a type:

ResultSet.TYPE_FORWARD_ONLY

,

ResultSet.TYPE_SCROLL_INSENSITIVE

, or

ResultSet.TYPE_SCROLL_SENSITIVE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getType()

- setConcurrency

```java
void setConcurrency​(int concurrency)
throws
SQLException
```

Sets the concurrency of this

RowSet

object to the given
concurrency level. This method is used to change the concurrency level
of a rowset, which is by default

ResultSet.CONCUR_READ_ONLY

**Parameters:** concurrency

- one of the

ResultSet

constants specifying a
concurrency level:

ResultSet.CONCUR_READ_ONLY

or

ResultSet.CONCUR_UPDATABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getConcurrency()

- setNull

```java
void setNull​(int parameterIndex,
int sqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a SQL type code defined by

java.sql.Types
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setNull

```java
void setNull​(int paramIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

. This version of the method

setNull

should be used for SQL user-defined types (UDTs) and

REF

type
parameters. Examples of UDTs include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

**Parameters:** paramIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully qualified name of an SQL UDT or the type
name of the SQL structured type being referenced by a

REF

type; ignored if the parameter is not a UDT or

REF

type
**Throws:** SQLException

- if a database access error occurs

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
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBoolean

```java
void setBoolean​(int parameterIndex,
boolean x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value. The driver converts this to
an SQL

BIT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBoolean(int)

- setByte

```java
void setByte​(int parameterIndex,
byte x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value. The driver converts this to
an SQL

TINYINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getByte(int)

- setShort

```java
void setShort​(int parameterIndex,
short x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value. The driver converts this to
an SQL

SMALLINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getShort(int)

- setInt

```java
void setInt​(int parameterIndex,
int x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value. The driver converts this to
an SQL

INTEGER

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getInt(int)

- setLong

```java
void setLong​(int parameterIndex,
long x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value. The driver converts this to
an SQL

BIGINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getLong(int)

- setFloat

```java
void setFloat​(int parameterIndex,
float x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value. The driver converts this to
an SQL

REAL

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getFloat(int)

- setDouble

```java
void setDouble​(int parameterIndex,
double x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value. The driver converts this to
an SQL

DOUBLE

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDouble(int)

- setBigDecimal

```java
void setBigDecimal​(int parameterIndex,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.
The driver converts this to
an SQL

NUMERIC

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBigDecimal(int, int)

- setString

```java
void setString​(int parameterIndex,

String
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value. Before sending it to the
database, the driver converts this to an SQL

VARCHAR

or

LONGVARCHAR

value, depending on the argument's size relative
to the driver's limits on

VARCHAR

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getString(int)

- setBytes

```java
void setBytes​(int parameterIndex,
byte[] x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values. Before sending it to the
database, the driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

value, depending on the argument's size relative
to the driver's limits on

VARBINARY

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBytes(int)

- setDate

```java
void setDate​(int parameterIndex,

Date
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value. The driver converts this to
an SQL

DATE

value before sending it to the database, using the
default

java.util.Calendar

to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

- setTime

```java
void setTime​(int parameterIndex,

Time
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value. The driver converts this to
an SQL

TIME

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

- setTimestamp

```java
void setTimestamp​(int parameterIndex,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value. The driver converts this to
an SQL

TIMESTAMP

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

- setAsciiStream

```java
void setAsciiStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large ASCII value via a

java.io.InputStream

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBinaryStream

```java
void setBinaryStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large binary value via a

java.io.InputStream

rather than as a

LONGVARBINARY

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setCharacterStream

```java
void setCharacterStream​(int parameterIndex,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.
It may be more practical to send a very large UNICODE value via a

java.io.Reader

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

Reader

object that contains the UNICODE data
to be set
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setAsciiStream

```java
void setAsciiStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(int parameterIndex,

Reader
reader)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(int parameterIndex,

Reader
value)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to a

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

. For integral values, the

java.lang

equivalent objects should be used (for example,
an instance of the class

Integer

for an

int

).

If the second argument is an

InputStream

then the stream must contain
the number of bytes specified by scaleOrLength. If the second argument is a

Reader

then the

Reader

must contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database. The scale argument may further qualify this
type.
**Parameters:** scaleOrLength

- for

java.sql.Types.DECIMAL

or

java.sql.Types.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or

Reader

. For all other types,
this value will be ignored.
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

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

Sets the value of the designated parameter with the given object. The second
argument must be an object type; for integral values, the

java.lang

equivalent objects should be used.

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

Note that this method may be used to pass database-
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** Types

,

ResultSet.getObject(int)

- setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.
This method is like

setObject

above, but the scale used is the scale
of the second parameter. Scalar values have a scale of zero. Literal
values have the scale present in the literal.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database
**Throws:** SQLException

- if a database access error occurs

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
This method is like the method

setObject

above, except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

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
The second parameter must be of type

Object

; therefore, the

java.lang

equivalent objects should be used for built-in types.

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

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

- setObject

```java
void setObject​(int parameterIndex,

Object
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

**Parameters:** parameterIndex

- The first parameter is 1, the second is 2, ...
**Parameters:** x

- The object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs

- setRef

```java
void setRef​(int i,

Ref
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value. The driver will convert this
to the appropriate

REF(<structured-type>)

value.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing data of an SQL

REF

type
**Throws:** SQLException

- if a database access error occurs

- setBlob

```java
void setBlob​(int i,

Blob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value. The driver will convert this
to the

BLOB

value that the

Blob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a BLOB
**Throws:** SQLException

- if a database access error occurs

- setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to a

InputStream

object.
The

InputStream

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

,
if parameterIndex does not correspond
to a parameter marker in the SQL statement, if the length specified
is less than zero or if the number of bytes in the

InputStream

does not match
the specified length.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to a

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
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

or
if parameterIndex does not correspond
to a parameter marker in the SQL statement,
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

Sets the designated parameter to a

InputStream

object.
The

InputStream

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

- if parameterIndex does not correspond
to a parameter marker in the SQL statement, or if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match
the specified length; if a database access error occurs or
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

- if a database access error occurs or
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
inputStream)
throws
SQLException
```

Sets the designated parameter to a

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(int i,

Clob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value. The driver will convert this
to the

CLOB

value that the

Clob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a CLOB
**Throws:** SQLException

- if a database access error occurs

- setClob

```java
void setClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

, if parameterIndex does not correspond to a parameter
marker in the SQL statement, or if the length specified is less than zero.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(int parameterIndex,

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

or if parameterIndex does not correspond to a parameter
marker in the SQL statement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
a database access error occurs or
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

- if a database access error occurs or
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

- if a database access error occurs or this method is called on
a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setArray

```java
void setArray​(int i,

Array
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value. The driver will convert this
to the

ARRAY

value that the

Array

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing an SQL array
**Throws:** SQLException

- if a database access error occurs

- setDate

```java
void setDate​(int parameterIndex,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value. The driver will convert this
to an SQL

DATE

value, using the given

java.util.Calendar

object to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the date
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

- setTime

```java
void setTime​(int parameterIndex,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

value. The driver will convert this
to an SQL

TIME

value, using the given

java.util.Calendar

object to calculate it, before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the time
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

- setTimestamp

```java
void setTimestamp​(int parameterIndex,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value. The driver will
convert this to an SQL

TIMESTAMP

value, using the given

java.util.Calendar

object to calculate it, before sending it to the
database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the
timestamp
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

- clearParameters

```java
void clearParameters()
throws
SQLException
```

Clears the parameters set for this

RowSet

object's command.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

**Throws:** SQLException

- if a database access error occurs

- execute

```java
void execute()
throws
SQLException
```

Fills this

RowSet

object with data.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

**Throws:** SQLException

- if a database access error occurs or any of the
properties necessary for making a connection and creating
a statement have not been set

- addRowSetListener

```java
void addRowSetListener​(
RowSetListener
listener)
```

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

**Parameters:** listener

- a component that has implemented the

RowSetListener

interface and wants to be notified when events occur on this

RowSet

object
**See Also:** removeRowSetListener(javax.sql.RowSetListener)

- removeRowSetListener

```java
void removeRowSetListener​(
RowSetListener
listener)
```

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

**Parameters:** listener

- a component that has been registered as a listener for this

RowSet

object
**See Also:** addRowSetListener(javax.sql.RowSetListener)

- setSQLXML

```java
void setSQLXML​(int parameterIndex,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an
SQL

XML

value when it sends it to the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** xmlObject

- a

SQLXML

object that maps an SQL

XML

value
**Throws:** SQLException

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
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

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
**Since:** 1.6

- setRowId

```java
void setRowId​(int parameterIndex,

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

value when it sends it
to the database

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs
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

- if a database access error occurs
**Since:** 1.6

- setNString

```java
void setNString​(int parameterIndex,

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

value
(depending on the argument's
size relative to the driver's limits on

NVARCHAR

values)
when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(int parameterIndex,

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

object.
The

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national
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

- if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The driver converts this to a
SQL

NCLOB

value when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setURL

```java
void setURL​(int parameterIndex,

URL
x)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

value.
The driver converts this to an SQL

DATALINK

value
when it sends it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the

java.net.URL

object to be set
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.4

Method Detail

- getUrl

```java
String
getUrl()
throws
SQLException
```

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.
The default value is

null

.

**Returns:** a string url
**Throws:** SQLException

- if a database access error occurs
**See Also:** setUrl(java.lang.String)

- setUrl

```java
void setUrl​(
String
url)
throws
SQLException
```

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Setting this property is optional. If a URL is used, a JDBC driver
that accepts the URL must be loaded before the
rowset is used to connect to a database. The rowset will use the URL
internally to create a database connection when reading or writing
data. Either a URL or a data source name is used to create a
connection, whichever was set to non null value most recently.

**Parameters:** url

- a string value; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUrl()

- getDataSourceName

```java
String
getDataSourceName()
```

Retrieves the logical name that identifies the data source for this

RowSet

object.

**Returns:** a data source name
**See Also:** setDataSourceName(java.lang.String)

,

setUrl(java.lang.String)

- setDataSourceName

```java
void setDataSourceName​(
String
name)
throws
SQLException
```

Sets the data source name property for this

RowSet

object to the
given

String

.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

**Parameters:** name

- the logical name of the data source for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getDataSourceName()

- getUsername

```java
String
getUsername()
```

Retrieves the username used to create a database connection for this

RowSet

object.
The username property is set at run time before calling the method

execute

. It is
not usually part of the serialized state of a

RowSet

object.

**Returns:** the username property
**See Also:** setUsername(java.lang.String)

- setUsername

```java
void setUsername​(
String
name)
throws
SQLException
```

Sets the username property for this

RowSet

object to the
given

String

.

**Parameters:** name

- a user name
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUsername()

- getPassword

```java
String
getPassword()
```

Retrieves the password used to create a database connection.
The password property is set at run time before calling the method

execute

. It is not usually part of the serialized state
of a

RowSet

object.

**Returns:** the password for making a database connection
**See Also:** setPassword(java.lang.String)

- setPassword

```java
void setPassword​(
String
password)
throws
SQLException
```

Sets the database password for this

RowSet

object to
the given

String

.

**Parameters:** password

- the password string
**Throws:** SQLException

- if a database access error occurs
**See Also:** getPassword()

- getTransactionIsolation

```java
int getTransactionIsolation()
```

Retrieves the transaction isolation level set for this

RowSet

object.

**Returns:** the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**See Also:** setTransactionIsolation(int)

- setTransactionIsolation

```java
void setTransactionIsolation​(int level)
throws
SQLException
```

Sets the transaction isolation level for this

RowSet

object.

**Parameters:** level

- the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTransactionIsolation()

- getTypeMap

```java
Map
<
String
,​
Class
<?>> getTypeMap()
throws
SQLException
```

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any. The default is for the
type map to be empty.

**Returns:** a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** setTypeMap(java.util.Map<java.lang.String, java.lang.Class<?>>)

- setTypeMap

```java
void setTypeMap​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object. This type map will be
used unless another type map is supplied as a method parameter.

**Parameters:** map

- a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTypeMap()

- getCommand

```java
String
getCommand()
```

Retrieves this

RowSet

object's command property.

The command property contains a command string, which must be an SQL
query, that can be executed to fill the rowset with data.
The default value is

null

.

**Returns:** the command string; may be

null
**See Also:** setCommand(java.lang.String)

- setCommand

```java
void setCommand​(
String
cmd)
throws
SQLException
```

Sets this

RowSet

object's command property to the given
SQL query.

This property is optional
when a rowset gets its data from a data source that does not support
commands, such as a spreadsheet.

**Parameters:** cmd

- the SQL query that will be used to get the data for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getCommand()

- isReadOnly

```java
boolean isReadOnly()
```

Retrieves whether this

RowSet

object is read-only.
If updates are possible, the default is for a rowset to be
updatable.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

**Returns:** true

if this

RowSet

object is
read-only;

false

if it is updatable
**See Also:** setReadOnly(boolean)

- setReadOnly

```java
void setReadOnly​(boolean value)
throws
SQLException
```

Sets whether this

RowSet

object is read-only to the
given

boolean

.

**Parameters:** value

-

true

if read-only;

false

if
updatable
**Throws:** SQLException

- if a database access error occurs
**See Also:** isReadOnly()

- getMaxFieldSize

```java
int getMaxFieldSize()
throws
SQLException
```

Retrieves the maximum number of bytes that may be returned
for certain column values.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.

**Returns:** the current maximum column size limit; zero means that there
is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxFieldSize(int)

- setMaxFieldSize

```java
void setMaxFieldSize​(int max)
throws
SQLException
```

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.
For maximum portability, use values greater than 256.

**Parameters:** max

- the new max column size limit in bytes; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxFieldSize()

- getMaxRows

```java
int getMaxRows()
throws
SQLException
```

Retrieves the maximum number of rows that this

RowSet

object can contain.
If the limit is exceeded, the excess rows are silently dropped.

**Returns:** the current maximum number of rows that this

RowSet

object can contain; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxRows(int)

- setMaxRows

```java
void setMaxRows​(int max)
throws
SQLException
```

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.
If the limit is exceeded, the excess rows are silently dropped.

**Parameters:** max

- the new maximum number of rows; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxRows()

- getEscapeProcessing

```java
boolean getEscapeProcessing()
throws
SQLException
```

Retrieves whether escape processing is enabled for this

RowSet

object.
If escape scanning is enabled, which is the default, the driver will do
escape substitution before sending an SQL statement to the database.

**Returns:** true

if escape processing is enabled;

false

if it is disabled
**Throws:** SQLException

- if a database access error occurs
**See Also:** setEscapeProcessing(boolean)

- setEscapeProcessing

```java
void setEscapeProcessing​(boolean enable)
throws
SQLException
```

Sets escape processing for this

RowSet

object on or
off. If escape scanning is on (the default), the driver will do
escape substitution before sending an SQL statement to the database.

**Parameters:** enable

-

true

to enable escape processing;

false

to disable it
**Throws:** SQLException

- if a database access error occurs
**See Also:** getEscapeProcessing()

- getQueryTimeout

```java
int getQueryTimeout()
throws
SQLException
```

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.
If this limit is exceeded, an

SQLException

is thrown.

**Returns:** the current query timeout limit in seconds; zero means
unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setQueryTimeout(int)

- setQueryTimeout

```java
void setQueryTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.
If this limit is exceeded, an

SQLException

is thrown.

**Parameters:** seconds

- the new query timeout limit in seconds; zero means
that there is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** getQueryTimeout()

- setType

```java
void setType​(int type)
throws
SQLException
```

Sets the type of this

RowSet

object to the given type.
This method is used to change the type of a rowset, which is by
default read-only and non-scrollable.

**Parameters:** type

- one of the

ResultSet

constants specifying a type:

ResultSet.TYPE_FORWARD_ONLY

,

ResultSet.TYPE_SCROLL_INSENSITIVE

, or

ResultSet.TYPE_SCROLL_SENSITIVE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getType()

- setConcurrency

```java
void setConcurrency​(int concurrency)
throws
SQLException
```

Sets the concurrency of this

RowSet

object to the given
concurrency level. This method is used to change the concurrency level
of a rowset, which is by default

ResultSet.CONCUR_READ_ONLY

**Parameters:** concurrency

- one of the

ResultSet

constants specifying a
concurrency level:

ResultSet.CONCUR_READ_ONLY

or

ResultSet.CONCUR_UPDATABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getConcurrency()

- setNull

```java
void setNull​(int parameterIndex,
int sqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a SQL type code defined by

java.sql.Types
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setNull

```java
void setNull​(int paramIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

. This version of the method

setNull

should be used for SQL user-defined types (UDTs) and

REF

type
parameters. Examples of UDTs include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

**Parameters:** paramIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully qualified name of an SQL UDT or the type
name of the SQL structured type being referenced by a

REF

type; ignored if the parameter is not a UDT or

REF

type
**Throws:** SQLException

- if a database access error occurs

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
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBoolean

```java
void setBoolean​(int parameterIndex,
boolean x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value. The driver converts this to
an SQL

BIT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBoolean(int)

- setByte

```java
void setByte​(int parameterIndex,
byte x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value. The driver converts this to
an SQL

TINYINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getByte(int)

- setShort

```java
void setShort​(int parameterIndex,
short x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value. The driver converts this to
an SQL

SMALLINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getShort(int)

- setInt

```java
void setInt​(int parameterIndex,
int x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value. The driver converts this to
an SQL

INTEGER

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getInt(int)

- setLong

```java
void setLong​(int parameterIndex,
long x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value. The driver converts this to
an SQL

BIGINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getLong(int)

- setFloat

```java
void setFloat​(int parameterIndex,
float x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value. The driver converts this to
an SQL

REAL

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getFloat(int)

- setDouble

```java
void setDouble​(int parameterIndex,
double x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value. The driver converts this to
an SQL

DOUBLE

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDouble(int)

- setBigDecimal

```java
void setBigDecimal​(int parameterIndex,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.
The driver converts this to
an SQL

NUMERIC

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBigDecimal(int, int)

- setString

```java
void setString​(int parameterIndex,

String
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value. Before sending it to the
database, the driver converts this to an SQL

VARCHAR

or

LONGVARCHAR

value, depending on the argument's size relative
to the driver's limits on

VARCHAR

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getString(int)

- setBytes

```java
void setBytes​(int parameterIndex,
byte[] x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values. Before sending it to the
database, the driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

value, depending on the argument's size relative
to the driver's limits on

VARBINARY

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBytes(int)

- setDate

```java
void setDate​(int parameterIndex,

Date
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value. The driver converts this to
an SQL

DATE

value before sending it to the database, using the
default

java.util.Calendar

to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

- setTime

```java
void setTime​(int parameterIndex,

Time
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value. The driver converts this to
an SQL

TIME

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

- setTimestamp

```java
void setTimestamp​(int parameterIndex,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value. The driver converts this to
an SQL

TIMESTAMP

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

- setAsciiStream

```java
void setAsciiStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large ASCII value via a

java.io.InputStream

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setBinaryStream

```java
void setBinaryStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large binary value via a

java.io.InputStream

rather than as a

LONGVARBINARY

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setCharacterStream

```java
void setCharacterStream​(int parameterIndex,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.
It may be more practical to send a very large UNICODE value via a

java.io.Reader

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

Reader

object that contains the UNICODE data
to be set
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4

- setAsciiStream

```java
void setAsciiStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBinaryStream

```java
void setBinaryStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setCharacterStream

```java
void setCharacterStream​(int parameterIndex,

Reader
reader)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(int parameterIndex,

Reader
value)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to a

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

. For integral values, the

java.lang

equivalent objects should be used (for example,
an instance of the class

Integer

for an

int

).

If the second argument is an

InputStream

then the stream must contain
the number of bytes specified by scaleOrLength. If the second argument is a

Reader

then the

Reader

must contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database. The scale argument may further qualify this
type.
**Parameters:** scaleOrLength

- for

java.sql.Types.DECIMAL

or

java.sql.Types.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or

Reader

. For all other types,
this value will be ignored.
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

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

Sets the value of the designated parameter with the given object. The second
argument must be an object type; for integral values, the

java.lang

equivalent objects should be used.

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

Note that this method may be used to pass database-
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** Types

,

ResultSet.getObject(int)

- setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.
This method is like

setObject

above, but the scale used is the scale
of the second parameter. Scalar values have a scale of zero. Literal
values have the scale present in the literal.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database
**Throws:** SQLException

- if a database access error occurs

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
This method is like the method

setObject

above, except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

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
The second parameter must be of type

Object

; therefore, the

java.lang

equivalent objects should be used for built-in types.

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

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

- setObject

```java
void setObject​(int parameterIndex,

Object
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

**Parameters:** parameterIndex

- The first parameter is 1, the second is 2, ...
**Parameters:** x

- The object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs

- setRef

```java
void setRef​(int i,

Ref
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value. The driver will convert this
to the appropriate

REF(<structured-type>)

value.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing data of an SQL

REF

type
**Throws:** SQLException

- if a database access error occurs

- setBlob

```java
void setBlob​(int i,

Blob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value. The driver will convert this
to the

BLOB

value that the

Blob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a BLOB
**Throws:** SQLException

- if a database access error occurs

- setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to a

InputStream

object.
The

InputStream

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

,
if parameterIndex does not correspond
to a parameter marker in the SQL statement, if the length specified
is less than zero or if the number of bytes in the

InputStream

does not match
the specified length.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to a

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
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

or
if parameterIndex does not correspond
to a parameter marker in the SQL statement,
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

Sets the designated parameter to a

InputStream

object.
The

InputStream

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

- if parameterIndex does not correspond
to a parameter marker in the SQL statement, or if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match
the specified length; if a database access error occurs or
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

- if a database access error occurs or
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
inputStream)
throws
SQLException
```

Sets the designated parameter to a

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(int i,

Clob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value. The driver will convert this
to the

CLOB

value that the

Clob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a CLOB
**Throws:** SQLException

- if a database access error occurs

- setClob

```java
void setClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

, if parameterIndex does not correspond to a parameter
marker in the SQL statement, or if the length specified is less than zero.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setClob

```java
void setClob​(int parameterIndex,

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

or if parameterIndex does not correspond to a parameter
marker in the SQL statement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
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

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
a database access error occurs or
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

- if a database access error occurs or
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

- if a database access error occurs or this method is called on
a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setArray

```java
void setArray​(int i,

Array
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value. The driver will convert this
to the

ARRAY

value that the

Array

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing an SQL array
**Throws:** SQLException

- if a database access error occurs

- setDate

```java
void setDate​(int parameterIndex,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value. The driver will convert this
to an SQL

DATE

value, using the given

java.util.Calendar

object to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the date
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

- setTime

```java
void setTime​(int parameterIndex,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

value. The driver will convert this
to an SQL

TIME

value, using the given

java.util.Calendar

object to calculate it, before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the time
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

- setTimestamp

```java
void setTimestamp​(int parameterIndex,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value. The driver will
convert this to an SQL

TIMESTAMP

value, using the given

java.util.Calendar

object to calculate it, before sending it to the
database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the
timestamp
**Throws:** SQLException

- if a database access error occurs

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

- clearParameters

```java
void clearParameters()
throws
SQLException
```

Clears the parameters set for this

RowSet

object's command.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

**Throws:** SQLException

- if a database access error occurs

- execute

```java
void execute()
throws
SQLException
```

Fills this

RowSet

object with data.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

**Throws:** SQLException

- if a database access error occurs or any of the
properties necessary for making a connection and creating
a statement have not been set

- addRowSetListener

```java
void addRowSetListener​(
RowSetListener
listener)
```

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

**Parameters:** listener

- a component that has implemented the

RowSetListener

interface and wants to be notified when events occur on this

RowSet

object
**See Also:** removeRowSetListener(javax.sql.RowSetListener)

- removeRowSetListener

```java
void removeRowSetListener​(
RowSetListener
listener)
```

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

**Parameters:** listener

- a component that has been registered as a listener for this

RowSet

object
**See Also:** addRowSetListener(javax.sql.RowSetListener)

- setSQLXML

```java
void setSQLXML​(int parameterIndex,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an
SQL

XML

value when it sends it to the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** xmlObject

- a

SQLXML

object that maps an SQL

XML

value
**Throws:** SQLException

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
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

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
**Since:** 1.6

- setRowId

```java
void setRowId​(int parameterIndex,

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

value when it sends it
to the database

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs
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

- if a database access error occurs
**Since:** 1.6

- setNString

```java
void setNString​(int parameterIndex,

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

value
(depending on the argument's
size relative to the driver's limits on

NVARCHAR

values)
when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
**Since:** 1.6

- setNCharacterStream

```java
void setNCharacterStream​(int parameterIndex,

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

object.
The

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national
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

- if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The driver converts this to a
SQL

NCLOB

value when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
**Since:** 1.6

- setNClob

```java
void setNClob​(int parameterIndex,

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

- setURL

```java
void setURL​(int parameterIndex,

URL
x)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

value.
The driver converts this to an SQL

DATALINK

value
when it sends it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the

java.net.URL

object to be set
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.4

---

#### Method Detail

getUrl

```java
String
getUrl()
throws
SQLException
```

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.
The default value is

null

.

**Returns:** a string url
**Throws:** SQLException

- if a database access error occurs
**See Also:** setUrl(java.lang.String)

---

#### getUrl

String

getUrl()
throws

SQLException

Retrieves the url property this

RowSet

object will use to
create a connection if it uses the

DriverManager

instead of a

DataSource

object to establish the connection.
The default value is

null

.

setUrl

```java
void setUrl​(
String
url)
throws
SQLException
```

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Setting this property is optional. If a URL is used, a JDBC driver
that accepts the URL must be loaded before the
rowset is used to connect to a database. The rowset will use the URL
internally to create a database connection when reading or writing
data. Either a URL or a data source name is used to create a
connection, whichever was set to non null value most recently.

**Parameters:** url

- a string value; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUrl()

---

#### setUrl

void setUrl​(

String

url)
throws

SQLException

Sets the URL this

RowSet

object will use when it uses the

DriverManager

to create a connection.

Setting this property is optional. If a URL is used, a JDBC driver
that accepts the URL must be loaded before the
rowset is used to connect to a database. The rowset will use the URL
internally to create a database connection when reading or writing
data. Either a URL or a data source name is used to create a
connection, whichever was set to non null value most recently.

getDataSourceName

```java
String
getDataSourceName()
```

Retrieves the logical name that identifies the data source for this

RowSet

object.

**Returns:** a data source name
**See Also:** setDataSourceName(java.lang.String)

,

setUrl(java.lang.String)

---

#### getDataSourceName

String

getDataSourceName()

Retrieves the logical name that identifies the data source for this

RowSet

object.

setDataSourceName

```java
void setDataSourceName​(
String
name)
throws
SQLException
```

Sets the data source name property for this

RowSet

object to the
given

String

.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

**Parameters:** name

- the logical name of the data source for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getDataSourceName()

---

#### setDataSourceName

void setDataSourceName​(

String

name)
throws

SQLException

Sets the data source name property for this

RowSet

object to the
given

String

.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

The value of the data source name property can be used to do a lookup of
a

DataSource

object that has been registered with a naming
service. After being retrieved, the

DataSource

object can be
used to create a connection to the data source that it represents.

getUsername

```java
String
getUsername()
```

Retrieves the username used to create a database connection for this

RowSet

object.
The username property is set at run time before calling the method

execute

. It is
not usually part of the serialized state of a

RowSet

object.

**Returns:** the username property
**See Also:** setUsername(java.lang.String)

---

#### getUsername

String

getUsername()

Retrieves the username used to create a database connection for this

RowSet

object.
The username property is set at run time before calling the method

execute

. It is
not usually part of the serialized state of a

RowSet

object.

setUsername

```java
void setUsername​(
String
name)
throws
SQLException
```

Sets the username property for this

RowSet

object to the
given

String

.

**Parameters:** name

- a user name
**Throws:** SQLException

- if a database access error occurs
**See Also:** getUsername()

---

#### setUsername

void setUsername​(

String

name)
throws

SQLException

Sets the username property for this

RowSet

object to the
given

String

.

getPassword

```java
String
getPassword()
```

Retrieves the password used to create a database connection.
The password property is set at run time before calling the method

execute

. It is not usually part of the serialized state
of a

RowSet

object.

**Returns:** the password for making a database connection
**See Also:** setPassword(java.lang.String)

---

#### getPassword

String

getPassword()

Retrieves the password used to create a database connection.
The password property is set at run time before calling the method

execute

. It is not usually part of the serialized state
of a

RowSet

object.

setPassword

```java
void setPassword​(
String
password)
throws
SQLException
```

Sets the database password for this

RowSet

object to
the given

String

.

**Parameters:** password

- the password string
**Throws:** SQLException

- if a database access error occurs
**See Also:** getPassword()

---

#### setPassword

void setPassword​(

String

password)
throws

SQLException

Sets the database password for this

RowSet

object to
the given

String

.

getTransactionIsolation

```java
int getTransactionIsolation()
```

Retrieves the transaction isolation level set for this

RowSet

object.

**Returns:** the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**See Also:** setTransactionIsolation(int)

---

#### getTransactionIsolation

int getTransactionIsolation()

Retrieves the transaction isolation level set for this

RowSet

object.

setTransactionIsolation

```java
void setTransactionIsolation​(int level)
throws
SQLException
```

Sets the transaction isolation level for this

RowSet

object.

**Parameters:** level

- the transaction isolation level; one of

Connection.TRANSACTION_READ_UNCOMMITTED

,

Connection.TRANSACTION_READ_COMMITTED

,

Connection.TRANSACTION_REPEATABLE_READ

, or

Connection.TRANSACTION_SERIALIZABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTransactionIsolation()

---

#### setTransactionIsolation

void setTransactionIsolation​(int level)
throws

SQLException

Sets the transaction isolation level for this

RowSet

object.

getTypeMap

```java
Map
<
String
,​
Class
<?>> getTypeMap()
throws
SQLException
```

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any. The default is for the
type map to be empty.

**Returns:** a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** setTypeMap(java.util.Map<java.lang.String, java.lang.Class<?>>)

---

#### getTypeMap

Map

<

String

,​

Class

<?>> getTypeMap()
throws

SQLException

Retrieves the

Map

object associated with this

RowSet

object, which specifies the custom mapping
of SQL user-defined types, if any. The default is for the
type map to be empty.

setTypeMap

```java
void setTypeMap​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object. This type map will be
used unless another type map is supplied as a method parameter.

**Parameters:** map

- a

java.util.Map

object containing the names of
SQL user-defined types and the Java classes to which they are
to be mapped
**Throws:** SQLException

- if a database access error occurs
**See Also:** getTypeMap()

---

#### setTypeMap

void setTypeMap​(

Map

<

String

,​

Class

<?>> map)
throws

SQLException

Installs the given

java.util.Map

object as the default
type map for this

RowSet

object. This type map will be
used unless another type map is supplied as a method parameter.

getCommand

```java
String
getCommand()
```

Retrieves this

RowSet

object's command property.

The command property contains a command string, which must be an SQL
query, that can be executed to fill the rowset with data.
The default value is

null

.

**Returns:** the command string; may be

null
**See Also:** setCommand(java.lang.String)

---

#### getCommand

String

getCommand()

Retrieves this

RowSet

object's command property.

The command property contains a command string, which must be an SQL
query, that can be executed to fill the rowset with data.
The default value is

null

.

setCommand

```java
void setCommand​(
String
cmd)
throws
SQLException
```

Sets this

RowSet

object's command property to the given
SQL query.

This property is optional
when a rowset gets its data from a data source that does not support
commands, such as a spreadsheet.

**Parameters:** cmd

- the SQL query that will be used to get the data for this

RowSet

object; may be

null
**Throws:** SQLException

- if a database access error occurs
**See Also:** getCommand()

---

#### setCommand

void setCommand​(

String

cmd)
throws

SQLException

Sets this

RowSet

object's command property to the given
SQL query.

This property is optional
when a rowset gets its data from a data source that does not support
commands, such as a spreadsheet.

isReadOnly

```java
boolean isReadOnly()
```

Retrieves whether this

RowSet

object is read-only.
If updates are possible, the default is for a rowset to be
updatable.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

**Returns:** true

if this

RowSet

object is
read-only;

false

if it is updatable
**See Also:** setReadOnly(boolean)

---

#### isReadOnly

boolean isReadOnly()

Retrieves whether this

RowSet

object is read-only.
If updates are possible, the default is for a rowset to be
updatable.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

Attempts to update a read-only rowset will result in an

SQLException

being thrown.

setReadOnly

```java
void setReadOnly​(boolean value)
throws
SQLException
```

Sets whether this

RowSet

object is read-only to the
given

boolean

.

**Parameters:** value

-

true

if read-only;

false

if
updatable
**Throws:** SQLException

- if a database access error occurs
**See Also:** isReadOnly()

---

#### setReadOnly

void setReadOnly​(boolean value)
throws

SQLException

Sets whether this

RowSet

object is read-only to the
given

boolean

.

getMaxFieldSize

```java
int getMaxFieldSize()
throws
SQLException
```

Retrieves the maximum number of bytes that may be returned
for certain column values.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.

**Returns:** the current maximum column size limit; zero means that there
is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxFieldSize(int)

---

#### getMaxFieldSize

int getMaxFieldSize()
throws

SQLException

Retrieves the maximum number of bytes that may be returned
for certain column values.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.

setMaxFieldSize

```java
void setMaxFieldSize​(int max)
throws
SQLException
```

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.
For maximum portability, use values greater than 256.

**Parameters:** max

- the new max column size limit in bytes; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxFieldSize()

---

#### setMaxFieldSize

void setMaxFieldSize​(int max)
throws

SQLException

Sets the maximum number of bytes that can be returned for a column
value to the given number of bytes.
This limit applies only to

BINARY

,

VARBINARY

,

LONGVARBINARYBINARY

,

CHAR

,

VARCHAR

,

LONGVARCHAR

,

NCHAR

and

NVARCHAR

columns.
If the limit is exceeded, the excess data is silently discarded.
For maximum portability, use values greater than 256.

getMaxRows

```java
int getMaxRows()
throws
SQLException
```

Retrieves the maximum number of rows that this

RowSet

object can contain.
If the limit is exceeded, the excess rows are silently dropped.

**Returns:** the current maximum number of rows that this

RowSet

object can contain; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setMaxRows(int)

---

#### getMaxRows

int getMaxRows()
throws

SQLException

Retrieves the maximum number of rows that this

RowSet

object can contain.
If the limit is exceeded, the excess rows are silently dropped.

setMaxRows

```java
void setMaxRows​(int max)
throws
SQLException
```

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.
If the limit is exceeded, the excess rows are silently dropped.

**Parameters:** max

- the new maximum number of rows; zero means unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** getMaxRows()

---

#### setMaxRows

void setMaxRows​(int max)
throws

SQLException

Sets the maximum number of rows that this

RowSet

object can contain to the specified number.
If the limit is exceeded, the excess rows are silently dropped.

getEscapeProcessing

```java
boolean getEscapeProcessing()
throws
SQLException
```

Retrieves whether escape processing is enabled for this

RowSet

object.
If escape scanning is enabled, which is the default, the driver will do
escape substitution before sending an SQL statement to the database.

**Returns:** true

if escape processing is enabled;

false

if it is disabled
**Throws:** SQLException

- if a database access error occurs
**See Also:** setEscapeProcessing(boolean)

---

#### getEscapeProcessing

boolean getEscapeProcessing()
throws

SQLException

Retrieves whether escape processing is enabled for this

RowSet

object.
If escape scanning is enabled, which is the default, the driver will do
escape substitution before sending an SQL statement to the database.

setEscapeProcessing

```java
void setEscapeProcessing​(boolean enable)
throws
SQLException
```

Sets escape processing for this

RowSet

object on or
off. If escape scanning is on (the default), the driver will do
escape substitution before sending an SQL statement to the database.

**Parameters:** enable

-

true

to enable escape processing;

false

to disable it
**Throws:** SQLException

- if a database access error occurs
**See Also:** getEscapeProcessing()

---

#### setEscapeProcessing

void setEscapeProcessing​(boolean enable)
throws

SQLException

Sets escape processing for this

RowSet

object on or
off. If escape scanning is on (the default), the driver will do
escape substitution before sending an SQL statement to the database.

getQueryTimeout

```java
int getQueryTimeout()
throws
SQLException
```

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.
If this limit is exceeded, an

SQLException

is thrown.

**Returns:** the current query timeout limit in seconds; zero means
unlimited
**Throws:** SQLException

- if a database access error occurs
**See Also:** setQueryTimeout(int)

---

#### getQueryTimeout

int getQueryTimeout()
throws

SQLException

Retrieves the maximum number of seconds the driver will wait for
a statement to execute.
If this limit is exceeded, an

SQLException

is thrown.

setQueryTimeout

```java
void setQueryTimeout​(int seconds)
throws
SQLException
```

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.
If this limit is exceeded, an

SQLException

is thrown.

**Parameters:** seconds

- the new query timeout limit in seconds; zero means
that there is no limit
**Throws:** SQLException

- if a database access error occurs
**See Also:** getQueryTimeout()

---

#### setQueryTimeout

void setQueryTimeout​(int seconds)
throws

SQLException

Sets the maximum time the driver will wait for
a statement to execute to the given number of seconds.
If this limit is exceeded, an

SQLException

is thrown.

setType

```java
void setType​(int type)
throws
SQLException
```

Sets the type of this

RowSet

object to the given type.
This method is used to change the type of a rowset, which is by
default read-only and non-scrollable.

**Parameters:** type

- one of the

ResultSet

constants specifying a type:

ResultSet.TYPE_FORWARD_ONLY

,

ResultSet.TYPE_SCROLL_INSENSITIVE

, or

ResultSet.TYPE_SCROLL_SENSITIVE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getType()

---

#### setType

void setType​(int type)
throws

SQLException

Sets the type of this

RowSet

object to the given type.
This method is used to change the type of a rowset, which is by
default read-only and non-scrollable.

setConcurrency

```java
void setConcurrency​(int concurrency)
throws
SQLException
```

Sets the concurrency of this

RowSet

object to the given
concurrency level. This method is used to change the concurrency level
of a rowset, which is by default

ResultSet.CONCUR_READ_ONLY

**Parameters:** concurrency

- one of the

ResultSet

constants specifying a
concurrency level:

ResultSet.CONCUR_READ_ONLY

or

ResultSet.CONCUR_UPDATABLE
**Throws:** SQLException

- if a database access error occurs
**See Also:** ResultSet.getConcurrency()

---

#### setConcurrency

void setConcurrency​(int concurrency)
throws

SQLException

Sets the concurrency of this

RowSet

object to the given
concurrency level. This method is used to change the concurrency level
of a rowset, which is by default

ResultSet.CONCUR_READ_ONLY

setNull

```java
void setNull​(int parameterIndex,
int sqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a SQL type code defined by

java.sql.Types
**Throws:** SQLException

- if a database access error occurs

---

#### setNull

void setNull​(int parameterIndex,
int sqlType)
throws

SQLException

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

.

Note:

You must specify the parameter's SQL type.

Note:

You must specify the parameter's SQL type.

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

- if a database access error occurs or
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

setNull

```java
void setNull​(int paramIndex,
int sqlType,

String
typeName)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

. This version of the method

setNull

should be used for SQL user-defined types (UDTs) and

REF

type
parameters. Examples of UDTs include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

**Parameters:** paramIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** sqlType

- a value from

java.sql.Types
**Parameters:** typeName

- the fully qualified name of an SQL UDT or the type
name of the SQL structured type being referenced by a

REF

type; ignored if the parameter is not a UDT or

REF

type
**Throws:** SQLException

- if a database access error occurs

---

#### setNull

void setNull​(int paramIndex,
int sqlType,

String

typeName)
throws

SQLException

Sets the designated parameter in this

RowSet

object's SQL
command to SQL

NULL

. This version of the method

setNull

should be used for SQL user-defined types (UDTs) and

REF

type
parameters. Examples of UDTs include:

STRUCT

,

DISTINCT

,

JAVA_OBJECT

, and named array types.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

Note:

To be portable, applications must give the
SQL type code and the fully qualified SQL type name when specifying
a NULL UDT or

REF

parameter. In the case of a UDT,
the name is the type name of the parameter itself. For a

REF

parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for UDT and

REF

parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or

REF

type,
the typeName parameter is ignored.

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
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

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

- if a database access error occurs or
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
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

Note:

To be portable, applications must give the
SQL type code and the fully-qualified SQL type name when specifying
a NULL user-defined or REF parameter. In the case of a user-defined type
the name is the type name of the parameter itself. For a REF
parameter, the name is the type name of the referenced type. If
a JDBC driver does not need the type code or type name information,
it may ignore it.

Although it is intended for user-defined and Ref parameters,
this method may be used to set a null parameter of any JDBC type.
If the parameter does not have a user-defined or REF type, the given
typeName is ignored.

setBoolean

```java
void setBoolean​(int parameterIndex,
boolean x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value. The driver converts this to
an SQL

BIT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setBoolean

void setBoolean​(int parameterIndex,
boolean x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

boolean

value. The driver converts this to
an SQL

BIT

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBoolean(int)

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
void setByte​(int parameterIndex,
byte x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value. The driver converts this to
an SQL

TINYINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setByte

void setByte​(int parameterIndex,
byte x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

byte

value. The driver converts this to
an SQL

TINYINT

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getByte(int)

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
void setShort​(int parameterIndex,
short x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value. The driver converts this to
an SQL

SMALLINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setShort

void setShort​(int parameterIndex,
short x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

short

value. The driver converts this to
an SQL

SMALLINT

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getShort(int)

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
void setInt​(int parameterIndex,
int x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value. The driver converts this to
an SQL

INTEGER

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setInt

void setInt​(int parameterIndex,
int x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

int

value. The driver converts this to
an SQL

INTEGER

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getInt(int)

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
void setLong​(int parameterIndex,
long x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value. The driver converts this to
an SQL

BIGINT

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setLong

void setLong​(int parameterIndex,
long x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

long

value. The driver converts this to
an SQL

BIGINT

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getLong(int)

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
void setFloat​(int parameterIndex,
float x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value. The driver converts this to
an SQL

REAL

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setFloat

void setFloat​(int parameterIndex,
float x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

float

value. The driver converts this to
an SQL

REAL

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getFloat(int)

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
void setDouble​(int parameterIndex,
double x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value. The driver converts this to
an SQL

DOUBLE

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setDouble

void setDouble​(int parameterIndex,
double x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

double

value. The driver converts this to
an SQL

DOUBLE

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDouble(int)

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
void setBigDecimal​(int parameterIndex,

BigDecimal
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.
The driver converts this to
an SQL

NUMERIC

value before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setBigDecimal

void setBigDecimal​(int parameterIndex,

BigDecimal

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.math.BigDecimal

value.
The driver converts this to
an SQL

NUMERIC

value before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBigDecimal(int, int)

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
void setString​(int parameterIndex,

String
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value. Before sending it to the
database, the driver converts this to an SQL

VARCHAR

or

LONGVARCHAR

value, depending on the argument's size relative
to the driver's limits on

VARCHAR

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setString

void setString​(int parameterIndex,

String

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java

String

value. Before sending it to the
database, the driver converts this to an SQL

VARCHAR

or

LONGVARCHAR

value, depending on the argument's size relative
to the driver's limits on

VARCHAR

values.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getString(int)

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
void setBytes​(int parameterIndex,
byte[] x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values. Before sending it to the
database, the driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

value, depending on the argument's size relative
to the driver's limits on

VARBINARY

values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setBytes

void setBytes​(int parameterIndex,
byte[] x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given Java array of

byte

values. Before sending it to the
database, the driver converts this to an SQL

VARBINARY

or

LONGVARBINARY

value, depending on the argument's size relative
to the driver's limits on

VARBINARY

values.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getBytes(int)

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
void setDate​(int parameterIndex,

Date
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value. The driver converts this to
an SQL

DATE

value before sending it to the database, using the
default

java.util.Calendar

to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setDate

void setDate​(int parameterIndex,

Date

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Date

value. The driver converts this to
an SQL

DATE

value before sending it to the database, using the
default

java.util.Calendar

to calculate the date.

setTime

```java
void setTime​(int parameterIndex,

Time
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value. The driver converts this to
an SQL

TIME

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setTime

void setTime​(int parameterIndex,

Time

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Time

value. The driver converts this to
an SQL

TIME

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

setTimestamp

```java
void setTimestamp​(int parameterIndex,

Timestamp
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value. The driver converts this to
an SQL

TIMESTAMP

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setTimestamp

void setTimestamp​(int parameterIndex,

Timestamp

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.sql.Timestamp

value. The driver converts this to
an SQL

TIMESTAMP

value before sending it to the database, using the
default

java.util.Calendar

to calculate it.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

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
void setAsciiStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large ASCII value via a

java.io.InputStream

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

---

#### setAsciiStream

void setAsciiStream​(int parameterIndex,

InputStream

x,
int length)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large ASCII value via a

java.io.InputStream

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

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

- if a database access error occurs or
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
void setBinaryStream​(int parameterIndex,

InputStream
x,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large binary value via a

java.io.InputStream

rather than as a

LONGVARBINARY

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Parameters:** length

- the number of bytes in the stream
**Throws:** SQLException

- if a database access error occurs

---

#### setBinaryStream

void setBinaryStream​(int parameterIndex,

InputStream

x,
int length)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.InputStream

value.
It may be more practical to send a very large binary value via a

java.io.InputStream

rather than as a

LONGVARBINARY

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

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

- if a database access error occurs or
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

setCharacterStream

```java
void setCharacterStream​(int parameterIndex,

Reader
reader,
int length)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.
It may be more practical to send a very large UNICODE value via a

java.io.Reader

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

Note:

This stream object can either be a standard
Java stream object or your own subclass that implements the
standard interface.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

Reader

object that contains the UNICODE data
to be set
**Parameters:** length

- the number of characters in the stream
**Throws:** SQLException

- if a database access error occurs

---

#### setCharacterStream

void setCharacterStream​(int parameterIndex,

Reader

reader,
int length)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

java.io.Reader

value.
It may be more practical to send a very large UNICODE value via a

java.io.Reader

rather than as a

LONGVARCHAR

parameter. The driver will read the data from the stream
as needed until it reaches end-of-file.

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

- if a database access error occurs or
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

setAsciiStream

```java
void setAsciiStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the Java input stream that contains the ASCII parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setAsciiStream

void setAsciiStream​(int parameterIndex,

InputStream

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

- if a database access error occurs or
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
void setBinaryStream​(int parameterIndex,

InputStream
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the java input stream which contains the binary parameter value
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setBinaryStream

void setBinaryStream​(int parameterIndex,

InputStream

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given input stream.
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

- if a database access error occurs or
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
void setCharacterStream​(int parameterIndex,

Reader
reader)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to the given

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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** reader

- the

java.io.Reader

object that contains the
Unicode data
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setCharacterStream

void setCharacterStream​(int parameterIndex,

Reader

reader)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to the given

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

- if a database access error occurs or
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
void setNCharacterStream​(int parameterIndex,

Reader
value)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
to a

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setNCharacterStream

void setNCharacterStream​(int parameterIndex,

Reader

value)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
to a

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

setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType,
int scaleOrLength)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

. For integral values, the

java.lang

equivalent objects should be used (for example,
an instance of the class

Integer

for an

int

).

If the second argument is an

InputStream

then the stream must contain
the number of bytes specified by scaleOrLength. If the second argument is a

Reader

then the

Reader

must contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database. The scale argument may further qualify this
type.
**Parameters:** scaleOrLength

- for

java.sql.Types.DECIMAL

or

java.sql.Types.NUMERIC types

,
this is the number of digits after the decimal point. For
Java Object types

InputStream

and

Reader

,
this is the length
of the data in the stream or

Reader

. For all other types,
this value will be ignored.
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

---

#### setObject

void setObject​(int parameterIndex,

Object

x,
int targetSqlType,
int scaleOrLength)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given Java

Object

. For integral values, the

java.lang

equivalent objects should be used (for example,
an instance of the class

Integer

for an

int

).

If the second argument is an

InputStream

then the stream must contain
the number of bytes specified by scaleOrLength. If the second argument is a

Reader

then the

Reader

must contain the number of characters specified
by scaleOrLength. If these conditions are not true the driver will generate a

SQLException

when the prepared statement is executed.

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

The given Java object will be converted to the targetSqlType
before being sent to the database.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

Note that this method may be used to pass database-specific
abstract data types.

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

Sets the value of the designated parameter with the given object. The second
argument must be an object type; for integral values, the

java.lang

equivalent objects should be used.

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

Note that this method may be used to pass database-
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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** Types

,

ResultSet.getObject(int)

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

Sets the value of the designated parameter with the given object. The second
argument must be an object type; for integral values, the

java.lang

equivalent objects should be used.

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

Note that this method may be used to pass database-
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

Note that this method may be used to pass database-
specific abstract data types.

Note that this method may be used to pass database-
specific abstract data types.

setObject

```java
void setObject​(int parameterIndex,

Object
x,
int targetSqlType)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.
This method is like

setObject

above, but the scale used is the scale
of the second parameter. Scalar values have a scale of zero. Literal
values have the scale present in the literal.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in

java.sql.Types

)
to be sent to the database
**Throws:** SQLException

- if a database access error occurs

---

#### setObject

void setObject​(int parameterIndex,

Object

x,
int targetSqlType)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.
This method is like

setObject

above, but the scale used is the scale
of the second parameter. Scalar values have a scale of zero. Literal
values have the scale present in the literal.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

Even though it is supported, it is not recommended that this method
be called with floating point input values.

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
This method is like the method

setObject

above, except that it assumes a scale of zero.

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Parameters:** targetSqlType

- the SQL type (as defined in java.sql.Types) to be
sent to the database
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if

targetSqlType

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
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

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
This method is like the method

setObject

above, except that it assumes a scale of zero.

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
The second parameter must be of type

Object

; therefore, the

java.lang

equivalent objects should be used for built-in types.

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

**Parameters:** parameterName

- the name of the parameter
**Parameters:** x

- the object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

CallableStatement

or if the given

Object

parameter is ambiguous
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getObject(int)

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
The second parameter must be of type

Object

; therefore, the

java.lang

equivalent objects should be used for built-in types.

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

This method throws an exception if there is an ambiguity, for example, if the
object is of a class implementing more than one of the interfaces named above.

setObject

```java
void setObject​(int parameterIndex,

Object
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

**Parameters:** parameterIndex

- The first parameter is 1, the second is 2, ...
**Parameters:** x

- The object containing the input parameter value
**Throws:** SQLException

- if a database access error occurs

---

#### setObject

void setObject​(int parameterIndex,

Object

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with a Java

Object

. For integral values, the

java.lang

equivalent objects should be used.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

The JDBC specification provides a standard mapping from
Java Object types to SQL types. The driver will convert the
given Java object to its standard SQL mapping before sending it
to the database.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

Note that this method may be used to pass database-specific
abstract data types by using a driver-specific Java type.

If the object is of a class implementing

SQLData

,
the rowset should call the method

SQLData.writeSQL

to write the object to an

SQLOutput

data stream.
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

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

An exception is thrown if there is an ambiguity, for example, if the
object is of a class implementing more than one of these interfaces.

setRef

```java
void setRef​(int i,

Ref
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value. The driver will convert this
to the appropriate

REF(<structured-type>)

value.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing data of an SQL

REF

type
**Throws:** SQLException

- if a database access error occurs

---

#### setRef

void setRef​(int i,

Ref

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Ref

value. The driver will convert this
to the appropriate

REF(<structured-type>)

value.

setBlob

```java
void setBlob​(int i,

Blob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value. The driver will convert this
to the

BLOB

value that the

Blob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a BLOB
**Throws:** SQLException

- if a database access error occurs

---

#### setBlob

void setBlob​(int i,

Blob

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Blob

value. The driver will convert this
to the

BLOB

value that the

Blob

object
represents before sending it to the database.

setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream,
long length)
throws
SQLException
```

Sets the designated parameter to a

InputStream

object.
The

InputStream

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Parameters:** length

- the number of bytes in the parameter data.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

,
if parameterIndex does not correspond
to a parameter marker in the SQL statement, if the length specified
is less than zero or if the number of bytes in the

InputStream

does not match
the specified length.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setBlob

void setBlob​(int parameterIndex,

InputStream

inputStream,
long length)
throws

SQLException

Sets the designated parameter to a

InputStream

object.
The

InputStream

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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

setBlob

```java
void setBlob​(int parameterIndex,

InputStream
inputStream)
throws
SQLException
```

Sets the designated parameter to a

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
data should be sent to the server as a

LONGVARBINARY

or a

BLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setBlob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1,
the second is 2, ...
**Parameters:** inputStream

- An object that contains the data to set the parameter
value to.
**Throws:** SQLException

- if a database access error occurs,
this method is called on a closed

PreparedStatement

or
if parameterIndex does not correspond
to a parameter marker in the SQL statement,
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setBlob

void setBlob​(int parameterIndex,

InputStream

inputStream)
throws

SQLException

Sets the designated parameter to a

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
data should be sent to the server as a

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

Sets the designated parameter to a

InputStream

object.
The

InputStream

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

- if parameterIndex does not correspond
to a parameter marker in the SQL statement, or if the length specified
is less than zero; if the number of bytes in the

InputStream

does not match
the specified length; if a database access error occurs or
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

Sets the designated parameter to a

InputStream

object.
The

InputStream

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

- if a database access error occurs or
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

Sets the designated parameter to a

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

- if a database access error occurs or
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

Sets the designated parameter to a

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

setClob

```java
void setClob​(int i,

Clob
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value. The driver will convert this
to the

CLOB

value that the

Clob

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing a CLOB
**Throws:** SQLException

- if a database access error occurs

---

#### setClob

void setClob​(int i,

Clob

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Clob

value. The driver will convert this
to the

CLOB

value that the

Clob

object
represents before sending it to the database.

setClob

```java
void setClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

, if parameterIndex does not correspond to a parameter
marker in the SQL statement, or if the length specified is less than zero.
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setClob

void setClob​(int parameterIndex,

Reader

reader,
long length)
throws

SQLException

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

setClob

```java
void setClob​(int parameterIndex,

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
data should be sent to the server as a

LONGVARCHAR

or a

CLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if a database access error occurs, this method is called on
a closed

PreparedStatement

or if parameterIndex does not correspond to a parameter
marker in the SQL statement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setClob

void setClob​(int parameterIndex,

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
data should be sent to the server as a

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

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
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

Reader

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

- if a database access error occurs or
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

- if a database access error occurs or this method is called on
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

setArray

```java
void setArray​(int i,

Array
x)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value. The driver will convert this
to the

ARRAY

value that the

Array

object
represents before sending it to the database.

**Parameters:** i

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- an object representing an SQL array
**Throws:** SQLException

- if a database access error occurs

---

#### setArray

void setArray​(int i,

Array

x)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

Array

value. The driver will convert this
to the

ARRAY

value that the

Array

object
represents before sending it to the database.

setDate

```java
void setDate​(int parameterIndex,

Date
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value. The driver will convert this
to an SQL

DATE

value, using the given

java.util.Calendar

object to calculate the date.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the date
**Throws:** SQLException

- if a database access error occurs

---

#### setDate

void setDate​(int parameterIndex,

Date

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Date

value. The driver will convert this
to an SQL

DATE

value, using the given

java.util.Calendar

object to calculate the date.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getDate(int)

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
void setTime​(int parameterIndex,

Time
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

value. The driver will convert this
to an SQL

TIME

value, using the given

java.util.Calendar

object to calculate it, before sending it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the time
**Throws:** SQLException

- if a database access error occurs

---

#### setTime

void setTime​(int parameterIndex,

Time

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Time

value. The driver will convert this
to an SQL

TIME

value, using the given

java.util.Calendar

object to calculate it, before sending it to the database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTime(int)

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
void setTimestamp​(int parameterIndex,

Timestamp
x,

Calendar
cal)
throws
SQLException
```

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value. The driver will
convert this to an SQL

TIMESTAMP

value, using the given

java.util.Calendar

object to calculate it, before sending it to the
database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Parameters:** cal

- the

java.util.Calendar

object to use for calculating the
timestamp
**Throws:** SQLException

- if a database access error occurs

---

#### setTimestamp

void setTimestamp​(int parameterIndex,

Timestamp

x,

Calendar

cal)
throws

SQLException

Sets the designated parameter in this

RowSet

object's command
with the given

java.sql.Timestamp

value. The driver will
convert this to an SQL

TIMESTAMP

value, using the given

java.util.Calendar

object to calculate it, before sending it to the
database.

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

- if a database access error occurs or
this method is called on a closed

CallableStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.4
**See Also:** ResultSet.getTimestamp(int)

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

clearParameters

```java
void clearParameters()
throws
SQLException
```

Clears the parameters set for this

RowSet

object's command.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

**Throws:** SQLException

- if a database access error occurs

---

#### clearParameters

void clearParameters()
throws

SQLException

Clears the parameters set for this

RowSet

object's command.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

In general, parameter values remain in force for repeated use of a

RowSet

object. Setting a parameter value automatically clears its
previous value. However, in some cases it is useful to immediately
release the resources used by the current parameter values, which can
be done by calling the method

clearParameters

.

execute

```java
void execute()
throws
SQLException
```

Fills this

RowSet

object with data.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

**Throws:** SQLException

- if a database access error occurs or any of the
properties necessary for making a connection and creating
a statement have not been set

---

#### execute

void execute()
throws

SQLException

Fills this

RowSet

object with data.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

The

execute

method may use the following properties
to create a connection for reading data: url, data source name,
user name, password, transaction isolation, and type map.

The

execute

method may use the following properties
to create a statement to execute a command:
command, read only, maximum field size,
maximum rows, escape processing, and query timeout.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

If the required properties have not been set, an exception is
thrown. If this method is successful, the current contents of the rowset are
discarded and the rowset's metadata is also (re)set. If there are
outstanding updates, they are ignored.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

If this

RowSet

object does not maintain a continuous connection
with its source of data, it may use a

Reader

(a

RowSetReader

object) to fill itself with data. In this case, a

Reader

will have been
registered with this

RowSet

object, and the method

execute

will call on the

Reader

's

readData

method as part of its implementation.

addRowSetListener

```java
void addRowSetListener​(
RowSetListener
listener)
```

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

**Parameters:** listener

- a component that has implemented the

RowSetListener

interface and wants to be notified when events occur on this

RowSet

object
**See Also:** removeRowSetListener(javax.sql.RowSetListener)

---

#### addRowSetListener

void addRowSetListener​(

RowSetListener

listener)

Registers the given listener so that it will be notified of events
that occur on this

RowSet

object.

removeRowSetListener

```java
void removeRowSetListener​(
RowSetListener
listener)
```

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

**Parameters:** listener

- a component that has been registered as a listener for this

RowSet

object
**See Also:** addRowSetListener(javax.sql.RowSetListener)

---

#### removeRowSetListener

void removeRowSetListener​(

RowSetListener

listener)

Removes the specified listener from the list of components that will be
notified when an event occurs on this

RowSet

object.

setSQLXML

```java
void setSQLXML​(int parameterIndex,

SQLXML
xmlObject)
throws
SQLException
```

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an
SQL

XML

value when it sends it to the database.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** xmlObject

- a

SQLXML

object that maps an SQL

XML

value
**Throws:** SQLException

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
**Since:** 1.6

---

#### setSQLXML

void setSQLXML​(int parameterIndex,

SQLXML

xmlObject)
throws

SQLException

Sets the designated parameter to the given

java.sql.SQLXML

object. The driver converts this to an
SQL

XML

value when it sends it to the database.

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

- if a database access error occurs, this method
is called on a closed result set,
the

java.xml.transform.Result

,

Writer

or

OutputStream

has not been closed
for the

SQLXML

object or
if there is an error processing the XML value. The

getCause

method
of the exception may provide a more detailed exception, for example, if the
stream does not contain valid XML.
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

setRowId

```java
void setRowId​(int parameterIndex,

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

value when it sends it
to the database

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the parameter value
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.6

---

#### setRowId

void setRowId​(int parameterIndex,

RowId

x)
throws

SQLException

Sets the designated parameter to the given

java.sql.RowId

object. The
driver converts this to a SQL

ROWID

value when it sends it
to the database

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

- if a database access error occurs
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
void setNString​(int parameterIndex,

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

value
(depending on the argument's
size relative to the driver's limits on

NVARCHAR

values)
when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
**Since:** 1.6

---

#### setNString

void setNString​(int parameterIndex,

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

value
(depending on the argument's
size relative to the driver's limits on

NVARCHAR

values)
when it sends it to the database.

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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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
void setNCharacterStream​(int parameterIndex,

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

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
**Since:** 1.6

---

#### setNCharacterStream

void setNCharacterStream​(int parameterIndex,

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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; if a database access error occurs; or
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

- the name of the column to be set
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur; or if a database access error occurs
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

object.
The

Reader

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

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
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

object.
The

Reader

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

- if the driver does not support national character sets;
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

setNClob

```java
void setNClob​(int parameterIndex,

Reader
reader,
long length)
throws
SQLException
```

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Parameters:** length

- the number of characters in the parameter data.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement; if the length specified is less than zero;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setNClob

void setNClob​(int parameterIndex,

Reader

reader,
long length)
throws

SQLException

Sets the designated parameter to a

Reader

object.
The

Reader

must contain the number
of characters specified by length otherwise a

SQLException

will be
generated when the

PreparedStatement

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

setNClob

```java
void setNClob​(int parameterIndex,

NClob
value)
throws
SQLException
```

Sets the designated parameter to a

java.sql.NClob

object. The driver converts this to a
SQL

NCLOB

value when it sends it to the database.

**Parameters:** parameterIndex

- of the first parameter is 1, the second is 2, ...
**Parameters:** value

- the parameter value
**Throws:** SQLException

- if the driver does not support national
character sets; if the driver can detect that a data conversion
error could occur ; or if a database access error occurs
**Since:** 1.6

---

#### setNClob

void setNClob​(int parameterIndex,

NClob

value)
throws

SQLException

Sets the designated parameter to a

java.sql.NClob

object. The driver converts this to a
SQL

NCLOB

value when it sends it to the database.

setNClob

```java
void setNClob​(int parameterIndex,

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
data should be sent to the server as a

LONGNVARCHAR

or a

NCLOB

Note:

Consult your JDBC driver documentation to determine if
it might be more efficient to use a version of

setNClob

which takes a length parameter.

**Parameters:** parameterIndex

- index of the first parameter is 1, the second is 2, ...
**Parameters:** reader

- An object that contains the data to set the parameter value to.
**Throws:** SQLException

- if parameterIndex does not correspond to a parameter
marker in the SQL statement;
if the driver does not support national character sets;
if the driver can detect that a data conversion
error could occur; if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.6

---

#### setNClob

void setNClob​(int parameterIndex,

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
data should be sent to the server as a

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

setURL

```java
void setURL​(int parameterIndex,

URL
x)
throws
SQLException
```

Sets the designated parameter to the given

java.net.URL

value.
The driver converts this to an SQL

DATALINK

value
when it sends it to the database.

**Parameters:** parameterIndex

- the first parameter is 1, the second is 2, ...
**Parameters:** x

- the

java.net.URL

object to be set
**Throws:** SQLException

- if a database access error occurs or
this method is called on a closed

PreparedStatement
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support this method
**Since:** 1.4

---

#### setURL

void setURL​(int parameterIndex,

URL

x)
throws

SQLException

Sets the designated parameter to the given

java.net.URL

value.
The driver converts this to an SQL

DATALINK

value
when it sends it to the database.

---

