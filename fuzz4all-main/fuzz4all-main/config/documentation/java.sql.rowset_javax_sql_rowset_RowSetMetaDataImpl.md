# Class RowSetMetaDataImpl

**Source:** `java.sql.rowset\javax\sql\rowset\RowSetMetaDataImpl.html`

### Class Description

```java
public class
RowSetMetaDataImpl

extends
Object

implements
RowSetMetaData
,
Serializable
```

Provides implementations for the methods that set and get
metadata information about a

RowSet

object's columns.
A

RowSetMetaDataImpl

object keeps track of the
number of columns in the rowset and maintains an internal array
of column attributes for each column.

A

RowSet

object creates a

RowSetMetaDataImpl

object internally in order to set and retrieve information about
its columns.

NOTE: All metadata in a

RowSetMetaDataImpl

object
should be considered as unavailable until the

RowSet

object
that it describes is populated.
Therefore, any

RowSetMetaDataImpl

method that retrieves information
is defined as having unspecified behavior when it is called
before the

RowSet

object contains data.

**All Implemented Interfaces:** Serializable

,

ResultSetMetaData

,

Wrapper

,

RowSetMetaData

---

### Field Details

*No entries found.*

### Constructor Details

#### public RowSetMetaDataImpl()

*No description found.*

---

### Method Details

#### public void setColumnCount​(int columnCount)
throws
SQLException

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

**Specified by:**
- setColumnCount

in interface

RowSetMetaData

**Parameters:**
- columnCount

- an

int

giving the number of columns in the

RowSet

object

**Throws:**
- SQLException

- if the given number is equal to or less than zero

---

#### public void setAutoIncrement​(int columnIndex,
boolean property)
throws
SQLException

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

**Specified by:**
- setAutoIncrement

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
- property

-

true

if the given column is
automatically incremented;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs or
the given index is out of bounds

---

#### public void setCaseSensitive​(int columnIndex,
boolean property)
throws
SQLException

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

**Specified by:**
- setCaseSensitive

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
- property

-

true

to indicate that the column
name is case sensitive;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs or
the given column number is out of bounds

---

#### public void setSearchable​(int columnIndex,
boolean property)
throws
SQLException

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

**Specified by:**
- setSearchable

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number
of columns in the rowset, inclusive
- property

-

true

to indicate that a column
value can be used in a

WHERE

clause;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs or
the given column number is out of bounds

---

#### public void setCurrency​(int columnIndex,
boolean property)
throws
SQLException

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

**Specified by:**
- setCurrency

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive between

1

and the number of columns, inclusive
- property

- true if the value is a cash value; false otherwise.

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public void setNullable​(int columnIndex,
int property)
throws
SQLException

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

**Specified by:**
- setNullable

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- property

- one of the following

ResultSetMetaData

constants:

columnNoNulls

,

columnNullable

, or

columnNullableUnknown

**Throws:**
- SQLException

- if a database access error occurs,
the given column number is out of bounds, or the value supplied
for the

property

parameter is not one of the following
constants:

ResultSetMetaData.columnNoNulls

,

ResultSetMetaData.columnNullable

, or

ResultSetMetaData.columnNullableUnknown

---

#### public void setSigned​(int columnIndex,
boolean property)
throws
SQLException

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

**Specified by:**
- setSigned

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- property

-

true

to indicate that a column
value is a signed number;

false

to indicate that it is not

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public void setColumnDisplaySize​(int columnIndex,
int size)
throws
SQLException

Sets the normal maximum number of chars in the designated column
to the given number.

**Specified by:**
- setColumnDisplaySize

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- size

- the maximum size of the column in chars; must be

0

or more

**Throws:**
- SQLException

- if a database access error occurs,
the given column number is out of bounds, or

size

is
less than

0

---

#### public void setColumnLabel​(int columnIndex,

String
label)
throws
SQLException

Sets the suggested column label for use in printouts and
displays, if any, to

label

. If

label

is

null

, the column label is set to an empty string
("").

**Specified by:**
- setColumnLabel

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- label

- the column label to be used in printouts and displays; if the
column label is

null

, an empty

String

is
set

**Throws:**
- SQLException

- if a database access error occurs
or the given column index is out of bounds

---

#### public void setColumnName​(int columnIndex,

String
columnName)
throws
SQLException

Sets the column name of the designated column to the given name.

**Specified by:**
- setColumnName

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- columnName

- a

String

object indicating the column name;
if the given name is

null

, an empty

String

is set

**Throws:**
- SQLException

- if a database access error occurs or the given column
index is out of bounds

---

#### public void setSchemaName​(int columnIndex,

String
schemaName)
throws
SQLException

Sets the designated column's table's schema name, if any, to

schemaName

. If

schemaName

is

null

,
the schema name is set to an empty string ("").

**Specified by:**
- setSchemaName

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- schemaName

- the schema name for the table from which a value in the
designated column was derived; may be an empty

String

or

null

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public void setPrecision​(int columnIndex,
int precision)
throws
SQLException

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

**Specified by:**
- setPrecision

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- precision

- the total number of decimal digits; must be

0

or more

**Throws:**
- SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

precision

is less than

0

---

#### public void setScale​(int columnIndex,
int scale)
throws
SQLException

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

**Specified by:**
- setScale

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- scale

- the number of digits to the right of the decimal point; must be
zero or greater

**Throws:**
- SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

scale

is less than

0

---

#### public void setTableName​(int columnIndex,

String
tableName)
throws
SQLException

Sets the name of the table from which the designated column
was derived to the given table name.

**Specified by:**
- setTableName

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- tableName

- the column's table name; may be

null

or an
empty string

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public void setCatalogName​(int columnIndex,

String
catalogName)
throws
SQLException

Sets the catalog name of the table from which the designated
column was derived to

catalogName

. If

catalogName

is

null

, the catalog name is set to an empty string.

**Specified by:**
- setCatalogName

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- catalogName

- the column's table's catalog name; if the catalogName
is

null

, an empty

String

is set

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public void setColumnType​(int columnIndex,
int SQLType)
throws
SQLException

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

**Specified by:**
- setColumnType

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- SQLType

- the designated column's SQL type, which must be one of the
constants in the class

java.sql.Types

**Throws:**
- SQLException

- if a database access error occurs,
the given column number is out of bounds, or the column type
specified is not one of the constants in

java.sql.Types

**See Also:**
- Types

---

#### public void setColumnTypeName​(int columnIndex,

String
typeName)
throws
SQLException

Sets the type name used by the data source for values stored in the
designated column to the given type name.

**Specified by:**
- setColumnTypeName

in interface

RowSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
- typeName

- the data source-specific type name; if

typeName

is

null

, an empty

String

is set

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int getColumnCount()
throws
SQLException

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

**Specified by:**
- getColumnCount

in interface

ResultSetMetaData

**Returns:**
- the number of columns

**Throws:**
- SQLException

- if an error occurs determining the column count

---

#### public boolean isAutoIncrement​(int columnIndex)
throws
SQLException

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

**Specified by:**
- isAutoIncrement

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if the column is automatically numbered;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isCaseSensitive​(int columnIndex)
throws
SQLException

Indicates whether the case of the designated column's name
matters.

**Specified by:**
- isCaseSensitive

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if the column name is case sensitive;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isSearchable​(int columnIndex)
throws
SQLException

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

**Specified by:**
- isSearchable

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if a value in the designated column can be used in a

WHERE

clause;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isCurrency​(int columnIndex)
throws
SQLException

Indicates whether a value stored in the designated column
is a cash value.

**Specified by:**
- isCurrency

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if a value in the designated column is a cash value;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int isNullable​(int columnIndex)
throws
SQLException

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

**Specified by:**
- isNullable

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- a constant from the

ResultSetMetaData

interface;
either

columnNoNulls

,

columnNullable

, or

columnNullableUnknown

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isSigned​(int columnIndex)
throws
SQLException

Indicates whether a value stored in the designated column is
a signed number.

**Specified by:**
- isSigned

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if a value in the designated column is a signed
number;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int getColumnDisplaySize​(int columnIndex)
throws
SQLException

Retrieves the normal maximum width in chars of the designated column.

**Specified by:**
- getColumnDisplaySize

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the maximum number of chars that can be displayed in the designated
column

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getColumnLabel​(int columnIndex)
throws
SQLException

Retrieves the suggested column title for the designated
column for use in printouts and displays.

**Specified by:**
- getColumnLabel

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the suggested column name to use in printouts and displays

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getColumnName​(int columnIndex)
throws
SQLException

Retrieves the name of the designated column.

**Specified by:**
- getColumnName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the column name of the designated column

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getSchemaName​(int columnIndex)
throws
SQLException

Retrieves the schema name of the table from which the value
in the designated column was derived.

**Specified by:**
- getSchemaName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive

**Returns:**
- the schema name or an empty

String

if no schema
name is available

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int getPrecision​(int columnIndex)
throws
SQLException

Retrieves the total number of digits for values stored in
the designated column.

**Specified by:**
- getPrecision

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the precision for values stored in the designated column

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int getScale​(int columnIndex)
throws
SQLException

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

**Specified by:**
- getScale

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the scale for values stored in the designated column

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getTableName​(int columnIndex)
throws
SQLException

Retrieves the name of the table from which the value
in the designated column was derived.

**Specified by:**
- getTableName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the table name or an empty

String

if no table name
is available

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getCatalogName​(int columnIndex)
throws
SQLException

Retrieves the catalog name of the table from which the value
in the designated column was derived.

**Specified by:**
- getCatalogName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the catalog name of the column's table or an empty

String

if no catalog name is available

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public int getColumnType​(int columnIndex)
throws
SQLException

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

**Specified by:**
- getColumnType

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- an

int

representing the SQL type of values
stored in the designated column

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

**See Also:**
- Types

---

#### public
String
getColumnTypeName​(int columnIndex)
throws
SQLException

Retrieves the DBMS-specific type name for values stored in the
designated column.

**Specified by:**
- getColumnTypeName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the type name used by the data source

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isReadOnly​(int columnIndex)
throws
SQLException

Indicates whether the designated column is definitely
not writable, thus readonly.

**Specified by:**
- isReadOnly

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if this

RowSet

object is read-Only
and thus not updatable;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isWritable​(int columnIndex)
throws
SQLException

Indicates whether it is possible for a write operation on
the designated column to succeed. A return value of

true

means that a write operation may or may
not succeed.

**Specified by:**
- isWritable

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if a write operation on the designated column may
will succeed;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public boolean isDefinitelyWritable​(int columnIndex)
throws
SQLException

Indicates whether a write operation on the designated column
will definitely succeed.

**Specified by:**
- isDefinitelyWritable

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- true

if a write operation on the designated column will
definitely succeed;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public
String
getColumnClassName​(int columnIndex)
throws
SQLException

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped. For example, if the value is an

int

,
the class name returned by this method will be

java.lang.Integer

.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

**Specified by:**
- getColumnClassName

in interface

ResultSetMetaData

**Parameters:**
- columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive

**Returns:**
- the fully-qualified name of the class in the Java programming
language that would be used by the method

RowSet.getObject

to
retrieve the value in the specified column. This is the class
name used for custom mapping when there is a custom mapping.

**Throws:**
- SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### public <T> T unwrap​(
Class
<T> iface)
throws
SQLException

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.
The result may be either the object found to implement the interface or a proxy for that object.
If the receiver implements the interface then that is the object. If the receiver is a wrapper
and the wrapped object implements the interface then that is the object. Otherwise the object is
the result of calling

unwrap

recursively on the wrapped object. If the receiver is not a
wrapper and does not implement the interface, then an

SQLException

is thrown.

**Specified by:**
- unwrap

in interface

Wrapper

**Parameters:**
- iface

- A Class defining an interface that the result must implement.

**Returns:**
- an object that implements the interface. May be a proxy for the actual implementing object.

**Throws:**
- SQLException

- If no object found that implements the interface

**Since:**
- 1.6

**Type Parameters:**
- T

- the type of the class modeled by this Class object

---

#### public boolean isWrapperFor​(
Class
<?> interfaces)
throws
SQLException

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does. Returns false otherwise. If this implements the interface then return true,
else if this is a wrapper then return the result of recursively calling

isWrapperFor

on the wrapped
object. If this does not implement the interface and is not a wrapper, return false.
This method should be implemented as a low-cost operation compared to

unwrap

so that
callers can use this method to avoid expensive

unwrap

calls that may fail. If this method
returns true then calling

unwrap

with the same argument should succeed.

**Specified by:**
- isWrapperFor

in interface

Wrapper

**Parameters:**
- interfaces

- a Class defining an interface.

**Returns:**
- true if this implements the interface or directly or indirectly wraps an object that does.

**Throws:**
- SQLException

- if an error occurs while determining whether this is a wrapper
for an object with the given interface.

**Since:**
- 1.6

---

### Additional Sections

#### Class RowSetMetaDataImpl

java.lang.Object

- javax.sql.rowset.RowSetMetaDataImpl

javax.sql.rowset.RowSetMetaDataImpl

**All Implemented Interfaces:** Serializable

,

ResultSetMetaData

,

Wrapper

,

RowSetMetaData

```java
public class
RowSetMetaDataImpl

extends
Object

implements
RowSetMetaData
,
Serializable
```

Provides implementations for the methods that set and get
metadata information about a

RowSet

object's columns.
A

RowSetMetaDataImpl

object keeps track of the
number of columns in the rowset and maintains an internal array
of column attributes for each column.

A

RowSet

object creates a

RowSetMetaDataImpl

object internally in order to set and retrieve information about
its columns.

NOTE: All metadata in a

RowSetMetaDataImpl

object
should be considered as unavailable until the

RowSet

object
that it describes is populated.
Therefore, any

RowSetMetaDataImpl

method that retrieves information
is defined as having unspecified behavior when it is called
before the

RowSet

object contains data.

**Since:** 1.5
**See Also:** Serialized Form

public class

RowSetMetaDataImpl

extends

Object

implements

RowSetMetaData

,

Serializable

Provides implementations for the methods that set and get
metadata information about a

RowSet

object's columns.
A

RowSetMetaDataImpl

object keeps track of the
number of columns in the rowset and maintains an internal array
of column attributes for each column.

A

RowSet

object creates a

RowSetMetaDataImpl

object internally in order to set and retrieve information about
its columns.

NOTE: All metadata in a

RowSetMetaDataImpl

object
should be considered as unavailable until the

RowSet

object
that it describes is populated.
Therefore, any

RowSetMetaDataImpl

method that retrieves information
is defined as having unspecified behavior when it is called
before the

RowSet

object contains data.

A

RowSet

object creates a

RowSetMetaDataImpl

object internally in order to set and retrieve information about
its columns.

NOTE: All metadata in a

RowSetMetaDataImpl

object
should be considered as unavailable until the

RowSet

object
that it describes is populated.
Therefore, any

RowSetMetaDataImpl

method that retrieves information
is defined as having unspecified behavior when it is called
before the

RowSet

object contains data.

NOTE: All metadata in a

RowSetMetaDataImpl

object
should be considered as unavailable until the

RowSet

object
that it describes is populated.
Therefore, any

RowSetMetaDataImpl

method that retrieves information
is defined as having unspecified behavior when it is called
before the

RowSet

object contains data.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.sql.

ResultSetMetaData

columnNoNulls

,

columnNullable

,

columnNullableUnknown

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RowSetMetaDataImpl

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getCatalogName

​(int columnIndex)

Retrieves the catalog name of the table from which the value
in the designated column was derived.

String

getColumnClassName

​(int columnIndex)

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped.

int

getColumnCount

()

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

int

getColumnDisplaySize

​(int columnIndex)

Retrieves the normal maximum width in chars of the designated column.

String

getColumnLabel

​(int columnIndex)

Retrieves the suggested column title for the designated
column for use in printouts and displays.

String

getColumnName

​(int columnIndex)

Retrieves the name of the designated column.

int

getColumnType

​(int columnIndex)

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

String

getColumnTypeName

​(int columnIndex)

Retrieves the DBMS-specific type name for values stored in the
designated column.

int

getPrecision

​(int columnIndex)

Retrieves the total number of digits for values stored in
the designated column.

int

getScale

​(int columnIndex)

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

String

getSchemaName

​(int columnIndex)

Retrieves the schema name of the table from which the value
in the designated column was derived.

String

getTableName

​(int columnIndex)

Retrieves the name of the table from which the value
in the designated column was derived.

boolean

isAutoIncrement

​(int columnIndex)

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

boolean

isCaseSensitive

​(int columnIndex)

Indicates whether the case of the designated column's name
matters.

boolean

isCurrency

​(int columnIndex)

Indicates whether a value stored in the designated column
is a cash value.

boolean

isDefinitelyWritable

​(int columnIndex)

Indicates whether a write operation on the designated column
will definitely succeed.

int

isNullable

​(int columnIndex)

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

boolean

isReadOnly

​(int columnIndex)

Indicates whether the designated column is definitely
not writable, thus readonly.

boolean

isSearchable

​(int columnIndex)

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

boolean

isSigned

​(int columnIndex)

Indicates whether a value stored in the designated column is
a signed number.

boolean

isWrapperFor

​(

Class

<?> interfaces)

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does.

boolean

isWritable

​(int columnIndex)

Indicates whether it is possible for a write operation on
the designated column to succeed.

void

setAutoIncrement

​(int columnIndex,
boolean property)

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

void

setCaseSensitive

​(int columnIndex,
boolean property)

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

void

setCatalogName

​(int columnIndex,

String

catalogName)

Sets the catalog name of the table from which the designated
column was derived to

catalogName

.

void

setColumnCount

​(int columnCount)

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

void

setColumnDisplaySize

​(int columnIndex,
int size)

Sets the normal maximum number of chars in the designated column
to the given number.

void

setColumnLabel

​(int columnIndex,

String

label)

Sets the suggested column label for use in printouts and
displays, if any, to

label

.

void

setColumnName

​(int columnIndex,

String

columnName)

Sets the column name of the designated column to the given name.

void

setColumnType

​(int columnIndex,
int SQLType)

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

void

setColumnTypeName

​(int columnIndex,

String

typeName)

Sets the type name used by the data source for values stored in the
designated column to the given type name.

void

setCurrency

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

void

setNullable

​(int columnIndex,
int property)

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

void

setPrecision

​(int columnIndex,
int precision)

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

void

setScale

​(int columnIndex,
int scale)

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

void

setSchemaName

​(int columnIndex,

String

schemaName)

Sets the designated column's table's schema name, if any, to

schemaName

.

void

setSearchable

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

void

setSigned

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

void

setTableName

​(int columnIndex,

String

tableName)

Sets the name of the table from which the designated column
was derived to the given table name.

<T> T

unwrap

​(

Class

<T> iface)

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.

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

Field Summary

- Fields declared in interface java.sql.

ResultSetMetaData

columnNoNulls

,

columnNullable

,

columnNullableUnknown

---

#### Field Summary

Fields declared in interface java.sql.

ResultSetMetaData

columnNoNulls

,

columnNullable

,

columnNullableUnknown

---

#### Fields declared in interface java.sql. ResultSetMetaData

Constructor Summary

Constructors

Constructor

Description

RowSetMetaDataImpl

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getCatalogName

​(int columnIndex)

Retrieves the catalog name of the table from which the value
in the designated column was derived.

String

getColumnClassName

​(int columnIndex)

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped.

int

getColumnCount

()

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

int

getColumnDisplaySize

​(int columnIndex)

Retrieves the normal maximum width in chars of the designated column.

String

getColumnLabel

​(int columnIndex)

Retrieves the suggested column title for the designated
column for use in printouts and displays.

String

getColumnName

​(int columnIndex)

Retrieves the name of the designated column.

int

getColumnType

​(int columnIndex)

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

String

getColumnTypeName

​(int columnIndex)

Retrieves the DBMS-specific type name for values stored in the
designated column.

int

getPrecision

​(int columnIndex)

Retrieves the total number of digits for values stored in
the designated column.

int

getScale

​(int columnIndex)

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

String

getSchemaName

​(int columnIndex)

Retrieves the schema name of the table from which the value
in the designated column was derived.

String

getTableName

​(int columnIndex)

Retrieves the name of the table from which the value
in the designated column was derived.

boolean

isAutoIncrement

​(int columnIndex)

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

boolean

isCaseSensitive

​(int columnIndex)

Indicates whether the case of the designated column's name
matters.

boolean

isCurrency

​(int columnIndex)

Indicates whether a value stored in the designated column
is a cash value.

boolean

isDefinitelyWritable

​(int columnIndex)

Indicates whether a write operation on the designated column
will definitely succeed.

int

isNullable

​(int columnIndex)

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

boolean

isReadOnly

​(int columnIndex)

Indicates whether the designated column is definitely
not writable, thus readonly.

boolean

isSearchable

​(int columnIndex)

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

boolean

isSigned

​(int columnIndex)

Indicates whether a value stored in the designated column is
a signed number.

boolean

isWrapperFor

​(

Class

<?> interfaces)

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does.

boolean

isWritable

​(int columnIndex)

Indicates whether it is possible for a write operation on
the designated column to succeed.

void

setAutoIncrement

​(int columnIndex,
boolean property)

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

void

setCaseSensitive

​(int columnIndex,
boolean property)

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

void

setCatalogName

​(int columnIndex,

String

catalogName)

Sets the catalog name of the table from which the designated
column was derived to

catalogName

.

void

setColumnCount

​(int columnCount)

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

void

setColumnDisplaySize

​(int columnIndex,
int size)

Sets the normal maximum number of chars in the designated column
to the given number.

void

setColumnLabel

​(int columnIndex,

String

label)

Sets the suggested column label for use in printouts and
displays, if any, to

label

.

void

setColumnName

​(int columnIndex,

String

columnName)

Sets the column name of the designated column to the given name.

void

setColumnType

​(int columnIndex,
int SQLType)

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

void

setColumnTypeName

​(int columnIndex,

String

typeName)

Sets the type name used by the data source for values stored in the
designated column to the given type name.

void

setCurrency

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

void

setNullable

​(int columnIndex,
int property)

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

void

setPrecision

​(int columnIndex,
int precision)

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

void

setScale

​(int columnIndex,
int scale)

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

void

setSchemaName

​(int columnIndex,

String

schemaName)

Sets the designated column's table's schema name, if any, to

schemaName

.

void

setSearchable

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

void

setSigned

​(int columnIndex,
boolean property)

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

void

setTableName

​(int columnIndex,

String

tableName)

Sets the name of the table from which the designated column
was derived to the given table name.

<T> T

unwrap

​(

Class

<T> iface)

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.

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

---

#### Method Summary

Retrieves the catalog name of the table from which the value
in the designated column was derived.

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped.

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

Retrieves the normal maximum width in chars of the designated column.

Retrieves the suggested column title for the designated
column for use in printouts and displays.

Retrieves the name of the designated column.

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

Retrieves the DBMS-specific type name for values stored in the
designated column.

Retrieves the total number of digits for values stored in
the designated column.

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

Retrieves the schema name of the table from which the value
in the designated column was derived.

Retrieves the name of the table from which the value
in the designated column was derived.

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

Indicates whether the case of the designated column's name
matters.

Indicates whether a value stored in the designated column
is a cash value.

Indicates whether a write operation on the designated column
will definitely succeed.

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

Indicates whether the designated column is definitely
not writable, thus readonly.

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

Indicates whether a value stored in the designated column is
a signed number.

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does.

Indicates whether it is possible for a write operation on
the designated column to succeed.

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

Sets the catalog name of the table from which the designated
column was derived to

catalogName

.

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

Sets the normal maximum number of chars in the designated column
to the given number.

Sets the suggested column label for use in printouts and
displays, if any, to

label

.

Sets the column name of the designated column to the given name.

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

Sets the type name used by the data source for values stored in the
designated column to the given type name.

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

Sets the designated column's table's schema name, if any, to

schemaName

.

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

Sets the name of the table from which the designated column
was derived to the given table name.

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RowSetMetaDataImpl

```java
public RowSetMetaDataImpl()
```

============ METHOD DETAIL ==========

- Method Detail

- setColumnCount

```java
public void setColumnCount​(int columnCount)
throws
SQLException
```

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

**Specified by:** setColumnCount

in interface

RowSetMetaData
**Parameters:** columnCount

- an

int

giving the number of columns in the

RowSet

object
**Throws:** SQLException

- if the given number is equal to or less than zero

- setAutoIncrement

```java
public void setAutoIncrement​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

**Specified by:** setAutoIncrement

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

if the given column is
automatically incremented;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given index is out of bounds

- setCaseSensitive

```java
public void setCaseSensitive​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

**Specified by:** setCaseSensitive

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

to indicate that the column
name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

- setSearchable

```java
public void setSearchable​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

**Specified by:** setSearchable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number
of columns in the rowset, inclusive
**Parameters:** property

-

true

to indicate that a column
value can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

- setCurrency

```java
public void setCurrency​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

**Specified by:** setCurrency

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive between

1

and the number of columns, inclusive
**Parameters:** property

- true if the value is a cash value; false otherwise.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setNullable

```java
public void setNullable​(int columnIndex,
int property)
throws
SQLException
```

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

**Specified by:** setNullable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

- one of the following

ResultSetMetaData

constants:

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the value supplied
for the

property

parameter is not one of the following
constants:

ResultSetMetaData.columnNoNulls

,

ResultSetMetaData.columnNullable

, or

ResultSetMetaData.columnNullableUnknown

- setSigned

```java
public void setSigned​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

**Specified by:** setSigned

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

-

true

to indicate that a column
value is a signed number;

false

to indicate that it is not
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setColumnDisplaySize

```java
public void setColumnDisplaySize​(int columnIndex,
int size)
throws
SQLException
```

Sets the normal maximum number of chars in the designated column
to the given number.

**Specified by:** setColumnDisplaySize

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** size

- the maximum size of the column in chars; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or

size

is
less than

0

- setColumnLabel

```java
public void setColumnLabel​(int columnIndex,

String
label)
throws
SQLException
```

Sets the suggested column label for use in printouts and
displays, if any, to

label

. If

label

is

null

, the column label is set to an empty string
("").

**Specified by:** setColumnLabel

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** label

- the column label to be used in printouts and displays; if the
column label is

null

, an empty

String

is
set
**Throws:** SQLException

- if a database access error occurs
or the given column index is out of bounds

- setColumnName

```java
public void setColumnName​(int columnIndex,

String
columnName)
throws
SQLException
```

Sets the column name of the designated column to the given name.

**Specified by:** setColumnName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** columnName

- a

String

object indicating the column name;
if the given name is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs or the given column
index is out of bounds

- setSchemaName

```java
public void setSchemaName​(int columnIndex,

String
schemaName)
throws
SQLException
```

Sets the designated column's table's schema name, if any, to

schemaName

. If

schemaName

is

null

,
the schema name is set to an empty string ("").

**Specified by:** setSchemaName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** schemaName

- the schema name for the table from which a value in the
designated column was derived; may be an empty

String

or

null
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setPrecision

```java
public void setPrecision​(int columnIndex,
int precision)
throws
SQLException
```

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

**Specified by:** setPrecision

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** precision

- the total number of decimal digits; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

precision

is less than

0

- setScale

```java
public void setScale​(int columnIndex,
int scale)
throws
SQLException
```

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

**Specified by:** setScale

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** scale

- the number of digits to the right of the decimal point; must be
zero or greater
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

scale

is less than

0

- setTableName

```java
public void setTableName​(int columnIndex,

String
tableName)
throws
SQLException
```

Sets the name of the table from which the designated column
was derived to the given table name.

**Specified by:** setTableName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** tableName

- the column's table name; may be

null

or an
empty string
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setCatalogName

```java
public void setCatalogName​(int columnIndex,

String
catalogName)
throws
SQLException
```

Sets the catalog name of the table from which the designated
column was derived to

catalogName

. If

catalogName

is

null

, the catalog name is set to an empty string.

**Specified by:** setCatalogName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** catalogName

- the column's table's catalog name; if the catalogName
is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setColumnType

```java
public void setColumnType​(int columnIndex,
int SQLType)
throws
SQLException
```

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

**Specified by:** setColumnType

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** SQLType

- the designated column's SQL type, which must be one of the
constants in the class

java.sql.Types
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the column type
specified is not one of the constants in

java.sql.Types
**See Also:** Types

- setColumnTypeName

```java
public void setColumnTypeName​(int columnIndex,

String
typeName)
throws
SQLException
```

Sets the type name used by the data source for values stored in the
designated column to the given type name.

**Specified by:** setColumnTypeName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** typeName

- the data source-specific type name; if

typeName

is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnCount

```java
public int getColumnCount()
throws
SQLException
```

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

**Specified by:** getColumnCount

in interface

ResultSetMetaData
**Returns:** the number of columns
**Throws:** SQLException

- if an error occurs determining the column count

- isAutoIncrement

```java
public boolean isAutoIncrement​(int columnIndex)
throws
SQLException
```

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

**Specified by:** isAutoIncrement

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column is automatically numbered;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isCaseSensitive

```java
public boolean isCaseSensitive​(int columnIndex)
throws
SQLException
```

Indicates whether the case of the designated column's name
matters.

**Specified by:** isCaseSensitive

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isSearchable

```java
public boolean isSearchable​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

**Specified by:** isSearchable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isCurrency

```java
public boolean isCurrency​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
is a cash value.

**Specified by:** isCurrency

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a cash value;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isNullable

```java
public int isNullable​(int columnIndex)
throws
SQLException
```

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

**Specified by:** isNullable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** a constant from the

ResultSetMetaData

interface;
either

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isSigned

```java
public boolean isSigned​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column is
a signed number.

**Specified by:** isSigned

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a signed
number;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnDisplaySize

```java
public int getColumnDisplaySize​(int columnIndex)
throws
SQLException
```

Retrieves the normal maximum width in chars of the designated column.

**Specified by:** getColumnDisplaySize

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the maximum number of chars that can be displayed in the designated
column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnLabel

```java
public
String
getColumnLabel​(int columnIndex)
throws
SQLException
```

Retrieves the suggested column title for the designated
column for use in printouts and displays.

**Specified by:** getColumnLabel

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the suggested column name to use in printouts and displays
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnName

```java
public
String
getColumnName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the designated column.

**Specified by:** getColumnName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the column name of the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getSchemaName

```java
public
String
getSchemaName​(int columnIndex)
throws
SQLException
```

Retrieves the schema name of the table from which the value
in the designated column was derived.

**Specified by:** getSchemaName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive
**Returns:** the schema name or an empty

String

if no schema
name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getPrecision

```java
public int getPrecision​(int columnIndex)
throws
SQLException
```

Retrieves the total number of digits for values stored in
the designated column.

**Specified by:** getPrecision

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the precision for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getScale

```java
public int getScale​(int columnIndex)
throws
SQLException
```

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

**Specified by:** getScale

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the scale for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getTableName

```java
public
String
getTableName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the table from which the value
in the designated column was derived.

**Specified by:** getTableName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the table name or an empty

String

if no table name
is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getCatalogName

```java
public
String
getCatalogName​(int columnIndex)
throws
SQLException
```

Retrieves the catalog name of the table from which the value
in the designated column was derived.

**Specified by:** getCatalogName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the catalog name of the column's table or an empty

String

if no catalog name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnType

```java
public int getColumnType​(int columnIndex)
throws
SQLException
```

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

**Specified by:** getColumnType

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** an

int

representing the SQL type of values
stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds
**See Also:** Types

- getColumnTypeName

```java
public
String
getColumnTypeName​(int columnIndex)
throws
SQLException
```

Retrieves the DBMS-specific type name for values stored in the
designated column.

**Specified by:** getColumnTypeName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the type name used by the data source
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isReadOnly

```java
public boolean isReadOnly​(int columnIndex)
throws
SQLException
```

Indicates whether the designated column is definitely
not writable, thus readonly.

**Specified by:** isReadOnly

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if this

RowSet

object is read-Only
and thus not updatable;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isWritable

```java
public boolean isWritable​(int columnIndex)
throws
SQLException
```

Indicates whether it is possible for a write operation on
the designated column to succeed. A return value of

true

means that a write operation may or may
not succeed.

**Specified by:** isWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column may
will succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isDefinitelyWritable

```java
public boolean isDefinitelyWritable​(int columnIndex)
throws
SQLException
```

Indicates whether a write operation on the designated column
will definitely succeed.

**Specified by:** isDefinitelyWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column will
definitely succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnClassName

```java
public
String
getColumnClassName​(int columnIndex)
throws
SQLException
```

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped. For example, if the value is an

int

,
the class name returned by this method will be

java.lang.Integer

.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

**Specified by:** getColumnClassName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

RowSet.getObject

to
retrieve the value in the specified column. This is the class
name used for custom mapping when there is a custom mapping.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- unwrap

```java
public <T> T unwrap​(
Class
<T> iface)
throws
SQLException
```

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.
The result may be either the object found to implement the interface or a proxy for that object.
If the receiver implements the interface then that is the object. If the receiver is a wrapper
and the wrapped object implements the interface then that is the object. Otherwise the object is
the result of calling

unwrap

recursively on the wrapped object. If the receiver is not a
wrapper and does not implement the interface, then an

SQLException

is thrown.

**Specified by:** unwrap

in interface

Wrapper
**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** iface

- A Class defining an interface that the result must implement.
**Returns:** an object that implements the interface. May be a proxy for the actual implementing object.
**Throws:** SQLException

- If no object found that implements the interface
**Since:** 1.6

- isWrapperFor

```java
public boolean isWrapperFor​(
Class
<?> interfaces)
throws
SQLException
```

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does. Returns false otherwise. If this implements the interface then return true,
else if this is a wrapper then return the result of recursively calling

isWrapperFor

on the wrapped
object. If this does not implement the interface and is not a wrapper, return false.
This method should be implemented as a low-cost operation compared to

unwrap

so that
callers can use this method to avoid expensive

unwrap

calls that may fail. If this method
returns true then calling

unwrap

with the same argument should succeed.

**Specified by:** isWrapperFor

in interface

Wrapper
**Parameters:** interfaces

- a Class defining an interface.
**Returns:** true if this implements the interface or directly or indirectly wraps an object that does.
**Throws:** SQLException

- if an error occurs while determining whether this is a wrapper
for an object with the given interface.
**Since:** 1.6

Constructor Detail

- RowSetMetaDataImpl

```java
public RowSetMetaDataImpl()
```

---

#### Constructor Detail

RowSetMetaDataImpl

```java
public RowSetMetaDataImpl()
```

---

#### RowSetMetaDataImpl

public RowSetMetaDataImpl()

Method Detail

- setColumnCount

```java
public void setColumnCount​(int columnCount)
throws
SQLException
```

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

**Specified by:** setColumnCount

in interface

RowSetMetaData
**Parameters:** columnCount

- an

int

giving the number of columns in the

RowSet

object
**Throws:** SQLException

- if the given number is equal to or less than zero

- setAutoIncrement

```java
public void setAutoIncrement​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

**Specified by:** setAutoIncrement

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

if the given column is
automatically incremented;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given index is out of bounds

- setCaseSensitive

```java
public void setCaseSensitive​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

**Specified by:** setCaseSensitive

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

to indicate that the column
name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

- setSearchable

```java
public void setSearchable​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

**Specified by:** setSearchable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number
of columns in the rowset, inclusive
**Parameters:** property

-

true

to indicate that a column
value can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

- setCurrency

```java
public void setCurrency​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

**Specified by:** setCurrency

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive between

1

and the number of columns, inclusive
**Parameters:** property

- true if the value is a cash value; false otherwise.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setNullable

```java
public void setNullable​(int columnIndex,
int property)
throws
SQLException
```

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

**Specified by:** setNullable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

- one of the following

ResultSetMetaData

constants:

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the value supplied
for the

property

parameter is not one of the following
constants:

ResultSetMetaData.columnNoNulls

,

ResultSetMetaData.columnNullable

, or

ResultSetMetaData.columnNullableUnknown

- setSigned

```java
public void setSigned​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

**Specified by:** setSigned

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

-

true

to indicate that a column
value is a signed number;

false

to indicate that it is not
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setColumnDisplaySize

```java
public void setColumnDisplaySize​(int columnIndex,
int size)
throws
SQLException
```

Sets the normal maximum number of chars in the designated column
to the given number.

**Specified by:** setColumnDisplaySize

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** size

- the maximum size of the column in chars; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or

size

is
less than

0

- setColumnLabel

```java
public void setColumnLabel​(int columnIndex,

String
label)
throws
SQLException
```

Sets the suggested column label for use in printouts and
displays, if any, to

label

. If

label

is

null

, the column label is set to an empty string
("").

**Specified by:** setColumnLabel

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** label

- the column label to be used in printouts and displays; if the
column label is

null

, an empty

String

is
set
**Throws:** SQLException

- if a database access error occurs
or the given column index is out of bounds

- setColumnName

```java
public void setColumnName​(int columnIndex,

String
columnName)
throws
SQLException
```

Sets the column name of the designated column to the given name.

**Specified by:** setColumnName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** columnName

- a

String

object indicating the column name;
if the given name is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs or the given column
index is out of bounds

- setSchemaName

```java
public void setSchemaName​(int columnIndex,

String
schemaName)
throws
SQLException
```

Sets the designated column's table's schema name, if any, to

schemaName

. If

schemaName

is

null

,
the schema name is set to an empty string ("").

**Specified by:** setSchemaName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** schemaName

- the schema name for the table from which a value in the
designated column was derived; may be an empty

String

or

null
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setPrecision

```java
public void setPrecision​(int columnIndex,
int precision)
throws
SQLException
```

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

**Specified by:** setPrecision

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** precision

- the total number of decimal digits; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

precision

is less than

0

- setScale

```java
public void setScale​(int columnIndex,
int scale)
throws
SQLException
```

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

**Specified by:** setScale

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** scale

- the number of digits to the right of the decimal point; must be
zero or greater
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

scale

is less than

0

- setTableName

```java
public void setTableName​(int columnIndex,

String
tableName)
throws
SQLException
```

Sets the name of the table from which the designated column
was derived to the given table name.

**Specified by:** setTableName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** tableName

- the column's table name; may be

null

or an
empty string
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setCatalogName

```java
public void setCatalogName​(int columnIndex,

String
catalogName)
throws
SQLException
```

Sets the catalog name of the table from which the designated
column was derived to

catalogName

. If

catalogName

is

null

, the catalog name is set to an empty string.

**Specified by:** setCatalogName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** catalogName

- the column's table's catalog name; if the catalogName
is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- setColumnType

```java
public void setColumnType​(int columnIndex,
int SQLType)
throws
SQLException
```

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

**Specified by:** setColumnType

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** SQLType

- the designated column's SQL type, which must be one of the
constants in the class

java.sql.Types
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the column type
specified is not one of the constants in

java.sql.Types
**See Also:** Types

- setColumnTypeName

```java
public void setColumnTypeName​(int columnIndex,

String
typeName)
throws
SQLException
```

Sets the type name used by the data source for values stored in the
designated column to the given type name.

**Specified by:** setColumnTypeName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** typeName

- the data source-specific type name; if

typeName

is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnCount

```java
public int getColumnCount()
throws
SQLException
```

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

**Specified by:** getColumnCount

in interface

ResultSetMetaData
**Returns:** the number of columns
**Throws:** SQLException

- if an error occurs determining the column count

- isAutoIncrement

```java
public boolean isAutoIncrement​(int columnIndex)
throws
SQLException
```

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

**Specified by:** isAutoIncrement

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column is automatically numbered;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isCaseSensitive

```java
public boolean isCaseSensitive​(int columnIndex)
throws
SQLException
```

Indicates whether the case of the designated column's name
matters.

**Specified by:** isCaseSensitive

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isSearchable

```java
public boolean isSearchable​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

**Specified by:** isSearchable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isCurrency

```java
public boolean isCurrency​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
is a cash value.

**Specified by:** isCurrency

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a cash value;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isNullable

```java
public int isNullable​(int columnIndex)
throws
SQLException
```

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

**Specified by:** isNullable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** a constant from the

ResultSetMetaData

interface;
either

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isSigned

```java
public boolean isSigned​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column is
a signed number.

**Specified by:** isSigned

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a signed
number;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnDisplaySize

```java
public int getColumnDisplaySize​(int columnIndex)
throws
SQLException
```

Retrieves the normal maximum width in chars of the designated column.

**Specified by:** getColumnDisplaySize

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the maximum number of chars that can be displayed in the designated
column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnLabel

```java
public
String
getColumnLabel​(int columnIndex)
throws
SQLException
```

Retrieves the suggested column title for the designated
column for use in printouts and displays.

**Specified by:** getColumnLabel

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the suggested column name to use in printouts and displays
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnName

```java
public
String
getColumnName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the designated column.

**Specified by:** getColumnName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the column name of the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getSchemaName

```java
public
String
getSchemaName​(int columnIndex)
throws
SQLException
```

Retrieves the schema name of the table from which the value
in the designated column was derived.

**Specified by:** getSchemaName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive
**Returns:** the schema name or an empty

String

if no schema
name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getPrecision

```java
public int getPrecision​(int columnIndex)
throws
SQLException
```

Retrieves the total number of digits for values stored in
the designated column.

**Specified by:** getPrecision

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the precision for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getScale

```java
public int getScale​(int columnIndex)
throws
SQLException
```

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

**Specified by:** getScale

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the scale for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getTableName

```java
public
String
getTableName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the table from which the value
in the designated column was derived.

**Specified by:** getTableName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the table name or an empty

String

if no table name
is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getCatalogName

```java
public
String
getCatalogName​(int columnIndex)
throws
SQLException
```

Retrieves the catalog name of the table from which the value
in the designated column was derived.

**Specified by:** getCatalogName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the catalog name of the column's table or an empty

String

if no catalog name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnType

```java
public int getColumnType​(int columnIndex)
throws
SQLException
```

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

**Specified by:** getColumnType

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** an

int

representing the SQL type of values
stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds
**See Also:** Types

- getColumnTypeName

```java
public
String
getColumnTypeName​(int columnIndex)
throws
SQLException
```

Retrieves the DBMS-specific type name for values stored in the
designated column.

**Specified by:** getColumnTypeName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the type name used by the data source
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isReadOnly

```java
public boolean isReadOnly​(int columnIndex)
throws
SQLException
```

Indicates whether the designated column is definitely
not writable, thus readonly.

**Specified by:** isReadOnly

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if this

RowSet

object is read-Only
and thus not updatable;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isWritable

```java
public boolean isWritable​(int columnIndex)
throws
SQLException
```

Indicates whether it is possible for a write operation on
the designated column to succeed. A return value of

true

means that a write operation may or may
not succeed.

**Specified by:** isWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column may
will succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- isDefinitelyWritable

```java
public boolean isDefinitelyWritable​(int columnIndex)
throws
SQLException
```

Indicates whether a write operation on the designated column
will definitely succeed.

**Specified by:** isDefinitelyWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column will
definitely succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- getColumnClassName

```java
public
String
getColumnClassName​(int columnIndex)
throws
SQLException
```

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped. For example, if the value is an

int

,
the class name returned by this method will be

java.lang.Integer

.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

**Specified by:** getColumnClassName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

RowSet.getObject

to
retrieve the value in the specified column. This is the class
name used for custom mapping when there is a custom mapping.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

- unwrap

```java
public <T> T unwrap​(
Class
<T> iface)
throws
SQLException
```

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.
The result may be either the object found to implement the interface or a proxy for that object.
If the receiver implements the interface then that is the object. If the receiver is a wrapper
and the wrapped object implements the interface then that is the object. Otherwise the object is
the result of calling

unwrap

recursively on the wrapped object. If the receiver is not a
wrapper and does not implement the interface, then an

SQLException

is thrown.

**Specified by:** unwrap

in interface

Wrapper
**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** iface

- A Class defining an interface that the result must implement.
**Returns:** an object that implements the interface. May be a proxy for the actual implementing object.
**Throws:** SQLException

- If no object found that implements the interface
**Since:** 1.6

- isWrapperFor

```java
public boolean isWrapperFor​(
Class
<?> interfaces)
throws
SQLException
```

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does. Returns false otherwise. If this implements the interface then return true,
else if this is a wrapper then return the result of recursively calling

isWrapperFor

on the wrapped
object. If this does not implement the interface and is not a wrapper, return false.
This method should be implemented as a low-cost operation compared to

unwrap

so that
callers can use this method to avoid expensive

unwrap

calls that may fail. If this method
returns true then calling

unwrap

with the same argument should succeed.

**Specified by:** isWrapperFor

in interface

Wrapper
**Parameters:** interfaces

- a Class defining an interface.
**Returns:** true if this implements the interface or directly or indirectly wraps an object that does.
**Throws:** SQLException

- if an error occurs while determining whether this is a wrapper
for an object with the given interface.
**Since:** 1.6

---

#### Method Detail

setColumnCount

```java
public void setColumnCount​(int columnCount)
throws
SQLException
```

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

**Specified by:** setColumnCount

in interface

RowSetMetaData
**Parameters:** columnCount

- an

int

giving the number of columns in the

RowSet

object
**Throws:** SQLException

- if the given number is equal to or less than zero

---

#### setColumnCount

public void setColumnCount​(int columnCount)
throws

SQLException

Sets to the given number the number of columns in the

RowSet

object for which this

RowSetMetaDataImpl

object was created.

setAutoIncrement

```java
public void setAutoIncrement​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

**Specified by:** setAutoIncrement

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

if the given column is
automatically incremented;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given index is out of bounds

---

#### setAutoIncrement

public void setAutoIncrement​(int columnIndex,
boolean property)
throws

SQLException

Sets whether the designated column is automatically
numbered, thus read-only, to the given

boolean

value.

setCaseSensitive

```java
public void setCaseSensitive​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

**Specified by:** setCaseSensitive

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns
in the rowset, inclusive
**Parameters:** property

-

true

to indicate that the column
name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

---

#### setCaseSensitive

public void setCaseSensitive​(int columnIndex,
boolean property)
throws

SQLException

Sets whether the name of the designated column is case sensitive to
the given

boolean

.

setSearchable

```java
public void setSearchable​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

**Specified by:** setSearchable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number
of columns in the rowset, inclusive
**Parameters:** property

-

true

to indicate that a column
value can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs or
the given column number is out of bounds

---

#### setSearchable

public void setSearchable​(int columnIndex,
boolean property)
throws

SQLException

Sets whether a value stored in the designated column can be used
in a

WHERE

clause to the given

boolean

value.

setCurrency

```java
public void setCurrency​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

**Specified by:** setCurrency

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive between

1

and the number of columns, inclusive
**Parameters:** property

- true if the value is a cash value; false otherwise.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setCurrency

public void setCurrency​(int columnIndex,
boolean property)
throws

SQLException

Sets whether a value stored in the designated column is a cash
value to the given

boolean

.

setNullable

```java
public void setNullable​(int columnIndex,
int property)
throws
SQLException
```

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

**Specified by:** setNullable

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

- one of the following

ResultSetMetaData

constants:

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the value supplied
for the

property

parameter is not one of the following
constants:

ResultSetMetaData.columnNoNulls

,

ResultSetMetaData.columnNullable

, or

ResultSetMetaData.columnNullableUnknown

---

#### setNullable

public void setNullable​(int columnIndex,
int property)
throws

SQLException

Sets whether a value stored in the designated column can be set
to

NULL

to the given constant from the interface

ResultSetMetaData

.

setSigned

```java
public void setSigned​(int columnIndex,
boolean property)
throws
SQLException
```

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

**Specified by:** setSigned

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** property

-

true

to indicate that a column
value is a signed number;

false

to indicate that it is not
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setSigned

public void setSigned​(int columnIndex,
boolean property)
throws

SQLException

Sets whether a value stored in the designated column is a signed
number to the given

boolean

.

setColumnDisplaySize

```java
public void setColumnDisplaySize​(int columnIndex,
int size)
throws
SQLException
```

Sets the normal maximum number of chars in the designated column
to the given number.

**Specified by:** setColumnDisplaySize

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** size

- the maximum size of the column in chars; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or

size

is
less than

0

---

#### setColumnDisplaySize

public void setColumnDisplaySize​(int columnIndex,
int size)
throws

SQLException

Sets the normal maximum number of chars in the designated column
to the given number.

setColumnLabel

```java
public void setColumnLabel​(int columnIndex,

String
label)
throws
SQLException
```

Sets the suggested column label for use in printouts and
displays, if any, to

label

. If

label

is

null

, the column label is set to an empty string
("").

**Specified by:** setColumnLabel

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** label

- the column label to be used in printouts and displays; if the
column label is

null

, an empty

String

is
set
**Throws:** SQLException

- if a database access error occurs
or the given column index is out of bounds

---

#### setColumnLabel

public void setColumnLabel​(int columnIndex,

String

label)
throws

SQLException

Sets the suggested column label for use in printouts and
displays, if any, to

label

. If

label

is

null

, the column label is set to an empty string
("").

setColumnName

```java
public void setColumnName​(int columnIndex,

String
columnName)
throws
SQLException
```

Sets the column name of the designated column to the given name.

**Specified by:** setColumnName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** columnName

- a

String

object indicating the column name;
if the given name is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs or the given column
index is out of bounds

---

#### setColumnName

public void setColumnName​(int columnIndex,

String

columnName)
throws

SQLException

Sets the column name of the designated column to the given name.

setSchemaName

```java
public void setSchemaName​(int columnIndex,

String
schemaName)
throws
SQLException
```

Sets the designated column's table's schema name, if any, to

schemaName

. If

schemaName

is

null

,
the schema name is set to an empty string ("").

**Specified by:** setSchemaName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** schemaName

- the schema name for the table from which a value in the
designated column was derived; may be an empty

String

or

null
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setSchemaName

public void setSchemaName​(int columnIndex,

String

schemaName)
throws

SQLException

Sets the designated column's table's schema name, if any, to

schemaName

. If

schemaName

is

null

,
the schema name is set to an empty string ("").

setPrecision

```java
public void setPrecision​(int columnIndex,
int precision)
throws
SQLException
```

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

**Specified by:** setPrecision

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** precision

- the total number of decimal digits; must be

0

or more
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

precision

is less than

0

---

#### setPrecision

public void setPrecision​(int columnIndex,
int precision)
throws

SQLException

Sets the total number of decimal digits in a value stored in the
designated column to the given number.

setScale

```java
public void setScale​(int columnIndex,
int scale)
throws
SQLException
```

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

**Specified by:** setScale

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** scale

- the number of digits to the right of the decimal point; must be
zero or greater
**Throws:** SQLException

- if a database access error occurs,

columnIndex

is out of bounds, or

scale

is less than

0

---

#### setScale

public void setScale​(int columnIndex,
int scale)
throws

SQLException

Sets the number of digits to the right of the decimal point in a value
stored in the designated column to the given number.

setTableName

```java
public void setTableName​(int columnIndex,

String
tableName)
throws
SQLException
```

Sets the name of the table from which the designated column
was derived to the given table name.

**Specified by:** setTableName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** tableName

- the column's table name; may be

null

or an
empty string
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setTableName

public void setTableName​(int columnIndex,

String

tableName)
throws

SQLException

Sets the name of the table from which the designated column
was derived to the given table name.

setCatalogName

```java
public void setCatalogName​(int columnIndex,

String
catalogName)
throws
SQLException
```

Sets the catalog name of the table from which the designated
column was derived to

catalogName

. If

catalogName

is

null

, the catalog name is set to an empty string.

**Specified by:** setCatalogName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** catalogName

- the column's table's catalog name; if the catalogName
is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setCatalogName

public void setCatalogName​(int columnIndex,

String

catalogName)
throws

SQLException

Sets the catalog name of the table from which the designated
column was derived to

catalogName

. If

catalogName

is

null

, the catalog name is set to an empty string.

setColumnType

```java
public void setColumnType​(int columnIndex,
int SQLType)
throws
SQLException
```

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

**Specified by:** setColumnType

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** SQLType

- the designated column's SQL type, which must be one of the
constants in the class

java.sql.Types
**Throws:** SQLException

- if a database access error occurs,
the given column number is out of bounds, or the column type
specified is not one of the constants in

java.sql.Types
**See Also:** Types

---

#### setColumnType

public void setColumnType​(int columnIndex,
int SQLType)
throws

SQLException

Sets the SQL type code for values stored in the designated column
to the given type code from the class

java.sql.Types

.

setColumnTypeName

```java
public void setColumnTypeName​(int columnIndex,

String
typeName)
throws
SQLException
```

Sets the type name used by the data source for values stored in the
designated column to the given type name.

**Specified by:** setColumnTypeName

in interface

RowSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Parameters:** typeName

- the data source-specific type name; if

typeName

is

null

, an empty

String

is set
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### setColumnTypeName

public void setColumnTypeName​(int columnIndex,

String

typeName)
throws

SQLException

Sets the type name used by the data source for values stored in the
designated column to the given type name.

getColumnCount

```java
public int getColumnCount()
throws
SQLException
```

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

**Specified by:** getColumnCount

in interface

ResultSetMetaData
**Returns:** the number of columns
**Throws:** SQLException

- if an error occurs determining the column count

---

#### getColumnCount

public int getColumnCount()
throws

SQLException

Retrieves the number of columns in the

RowSet

object
for which this

RowSetMetaDataImpl

object was created.

isAutoIncrement

```java
public boolean isAutoIncrement​(int columnIndex)
throws
SQLException
```

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

**Specified by:** isAutoIncrement

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column is automatically numbered;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isAutoIncrement

public boolean isAutoIncrement​(int columnIndex)
throws

SQLException

Retrieves whether a value stored in the designated column is
automatically numbered, and thus readonly.

isCaseSensitive

```java
public boolean isCaseSensitive​(int columnIndex)
throws
SQLException
```

Indicates whether the case of the designated column's name
matters.

**Specified by:** isCaseSensitive

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if the column name is case sensitive;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isCaseSensitive

public boolean isCaseSensitive​(int columnIndex)
throws

SQLException

Indicates whether the case of the designated column's name
matters.

isSearchable

```java
public boolean isSearchable​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

**Specified by:** isSearchable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column can be used in a

WHERE

clause;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isSearchable

public boolean isSearchable​(int columnIndex)
throws

SQLException

Indicates whether a value stored in the designated column
can be used in a

WHERE

clause.

isCurrency

```java
public boolean isCurrency​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column
is a cash value.

**Specified by:** isCurrency

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a cash value;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isCurrency

public boolean isCurrency​(int columnIndex)
throws

SQLException

Indicates whether a value stored in the designated column
is a cash value.

isNullable

```java
public int isNullable​(int columnIndex)
throws
SQLException
```

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

**Specified by:** isNullable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** a constant from the

ResultSetMetaData

interface;
either

columnNoNulls

,

columnNullable

, or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isNullable

public int isNullable​(int columnIndex)
throws

SQLException

Retrieves a constant indicating whether it is possible
to store a

NULL

value in the designated column.

isSigned

```java
public boolean isSigned​(int columnIndex)
throws
SQLException
```

Indicates whether a value stored in the designated column is
a signed number.

**Specified by:** isSigned

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a value in the designated column is a signed
number;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isSigned

public boolean isSigned​(int columnIndex)
throws

SQLException

Indicates whether a value stored in the designated column is
a signed number.

getColumnDisplaySize

```java
public int getColumnDisplaySize​(int columnIndex)
throws
SQLException
```

Retrieves the normal maximum width in chars of the designated column.

**Specified by:** getColumnDisplaySize

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the maximum number of chars that can be displayed in the designated
column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getColumnDisplaySize

public int getColumnDisplaySize​(int columnIndex)
throws

SQLException

Retrieves the normal maximum width in chars of the designated column.

getColumnLabel

```java
public
String
getColumnLabel​(int columnIndex)
throws
SQLException
```

Retrieves the suggested column title for the designated
column for use in printouts and displays.

**Specified by:** getColumnLabel

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the suggested column name to use in printouts and displays
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getColumnLabel

public

String

getColumnLabel​(int columnIndex)
throws

SQLException

Retrieves the suggested column title for the designated
column for use in printouts and displays.

getColumnName

```java
public
String
getColumnName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the designated column.

**Specified by:** getColumnName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the column name of the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getColumnName

public

String

getColumnName​(int columnIndex)
throws

SQLException

Retrieves the name of the designated column.

getSchemaName

```java
public
String
getSchemaName​(int columnIndex)
throws
SQLException
```

Retrieves the schema name of the table from which the value
in the designated column was derived.

**Specified by:** getSchemaName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns,
inclusive
**Returns:** the schema name or an empty

String

if no schema
name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getSchemaName

public

String

getSchemaName​(int columnIndex)
throws

SQLException

Retrieves the schema name of the table from which the value
in the designated column was derived.

getPrecision

```java
public int getPrecision​(int columnIndex)
throws
SQLException
```

Retrieves the total number of digits for values stored in
the designated column.

**Specified by:** getPrecision

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the precision for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getPrecision

public int getPrecision​(int columnIndex)
throws

SQLException

Retrieves the total number of digits for values stored in
the designated column.

getScale

```java
public int getScale​(int columnIndex)
throws
SQLException
```

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

**Specified by:** getScale

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the scale for values stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getScale

public int getScale​(int columnIndex)
throws

SQLException

Retrieves the number of digits to the right of the decimal point
for values stored in the designated column.

getTableName

```java
public
String
getTableName​(int columnIndex)
throws
SQLException
```

Retrieves the name of the table from which the value
in the designated column was derived.

**Specified by:** getTableName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the table name or an empty

String

if no table name
is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getTableName

public

String

getTableName​(int columnIndex)
throws

SQLException

Retrieves the name of the table from which the value
in the designated column was derived.

getCatalogName

```java
public
String
getCatalogName​(int columnIndex)
throws
SQLException
```

Retrieves the catalog name of the table from which the value
in the designated column was derived.

**Specified by:** getCatalogName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the catalog name of the column's table or an empty

String

if no catalog name is available
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getCatalogName

public

String

getCatalogName​(int columnIndex)
throws

SQLException

Retrieves the catalog name of the table from which the value
in the designated column was derived.

getColumnType

```java
public int getColumnType​(int columnIndex)
throws
SQLException
```

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

**Specified by:** getColumnType

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** an

int

representing the SQL type of values
stored in the designated column
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds
**See Also:** Types

---

#### getColumnType

public int getColumnType​(int columnIndex)
throws

SQLException

Retrieves the type code (one of the

java.sql.Types

constants) for the SQL type of the value stored in the
designated column.

getColumnTypeName

```java
public
String
getColumnTypeName​(int columnIndex)
throws
SQLException
```

Retrieves the DBMS-specific type name for values stored in the
designated column.

**Specified by:** getColumnTypeName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the type name used by the data source
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getColumnTypeName

public

String

getColumnTypeName​(int columnIndex)
throws

SQLException

Retrieves the DBMS-specific type name for values stored in the
designated column.

isReadOnly

```java
public boolean isReadOnly​(int columnIndex)
throws
SQLException
```

Indicates whether the designated column is definitely
not writable, thus readonly.

**Specified by:** isReadOnly

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if this

RowSet

object is read-Only
and thus not updatable;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isReadOnly

public boolean isReadOnly​(int columnIndex)
throws

SQLException

Indicates whether the designated column is definitely
not writable, thus readonly.

isWritable

```java
public boolean isWritable​(int columnIndex)
throws
SQLException
```

Indicates whether it is possible for a write operation on
the designated column to succeed. A return value of

true

means that a write operation may or may
not succeed.

**Specified by:** isWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column may
will succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isWritable

public boolean isWritable​(int columnIndex)
throws

SQLException

Indicates whether it is possible for a write operation on
the designated column to succeed. A return value of

true

means that a write operation may or may
not succeed.

isDefinitelyWritable

```java
public boolean isDefinitelyWritable​(int columnIndex)
throws
SQLException
```

Indicates whether a write operation on the designated column
will definitely succeed.

**Specified by:** isDefinitelyWritable

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** true

if a write operation on the designated column will
definitely succeed;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### isDefinitelyWritable

public boolean isDefinitelyWritable​(int columnIndex)
throws

SQLException

Indicates whether a write operation on the designated column
will definitely succeed.

getColumnClassName

```java
public
String
getColumnClassName​(int columnIndex)
throws
SQLException
```

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped. For example, if the value is an

int

,
the class name returned by this method will be

java.lang.Integer

.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

**Specified by:** getColumnClassName

in interface

ResultSetMetaData
**Parameters:** columnIndex

- the first column is 1, the second is 2, and so on;
must be between

1

and the number of columns, inclusive
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

RowSet.getObject

to
retrieve the value in the specified column. This is the class
name used for custom mapping when there is a custom mapping.
**Throws:** SQLException

- if a database access error occurs
or the given column number is out of bounds

---

#### getColumnClassName

public

String

getColumnClassName​(int columnIndex)
throws

SQLException

Retrieves the fully-qualified name of the class in the Java
programming language to which a value in the designated column
will be mapped. For example, if the value is an

int

,
the class name returned by this method will be

java.lang.Integer

.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

If the value in the designated column has a custom mapping,
this method returns the name of the class that implements

SQLData

. When the method

ResultSet.getObject

is called to retrieve a value from the designated column, it will
create an instance of this class or one of its subclasses.

unwrap

```java
public <T> T unwrap​(
Class
<T> iface)
throws
SQLException
```

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.
The result may be either the object found to implement the interface or a proxy for that object.
If the receiver implements the interface then that is the object. If the receiver is a wrapper
and the wrapped object implements the interface then that is the object. Otherwise the object is
the result of calling

unwrap

recursively on the wrapped object. If the receiver is not a
wrapper and does not implement the interface, then an

SQLException

is thrown.

**Specified by:** unwrap

in interface

Wrapper
**Type Parameters:** T

- the type of the class modeled by this Class object
**Parameters:** iface

- A Class defining an interface that the result must implement.
**Returns:** an object that implements the interface. May be a proxy for the actual implementing object.
**Throws:** SQLException

- If no object found that implements the interface
**Since:** 1.6

---

#### unwrap

public <T> T unwrap​(

Class

<T> iface)
throws

SQLException

Returns an object that implements the given interface to allow access to non-standard methods,
or standard methods not exposed by the proxy.
The result may be either the object found to implement the interface or a proxy for that object.
If the receiver implements the interface then that is the object. If the receiver is a wrapper
and the wrapped object implements the interface then that is the object. Otherwise the object is
the result of calling

unwrap

recursively on the wrapped object. If the receiver is not a
wrapper and does not implement the interface, then an

SQLException

is thrown.

isWrapperFor

```java
public boolean isWrapperFor​(
Class
<?> interfaces)
throws
SQLException
```

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does. Returns false otherwise. If this implements the interface then return true,
else if this is a wrapper then return the result of recursively calling

isWrapperFor

on the wrapped
object. If this does not implement the interface and is not a wrapper, return false.
This method should be implemented as a low-cost operation compared to

unwrap

so that
callers can use this method to avoid expensive

unwrap

calls that may fail. If this method
returns true then calling

unwrap

with the same argument should succeed.

**Specified by:** isWrapperFor

in interface

Wrapper
**Parameters:** interfaces

- a Class defining an interface.
**Returns:** true if this implements the interface or directly or indirectly wraps an object that does.
**Throws:** SQLException

- if an error occurs while determining whether this is a wrapper
for an object with the given interface.
**Since:** 1.6

---

#### isWrapperFor

public boolean isWrapperFor​(

Class

<?> interfaces)
throws

SQLException

Returns true if this either implements the interface argument or is directly or indirectly a wrapper
for an object that does. Returns false otherwise. If this implements the interface then return true,
else if this is a wrapper then return the result of recursively calling

isWrapperFor

on the wrapped
object. If this does not implement the interface and is not a wrapper, return false.
This method should be implemented as a low-cost operation compared to

unwrap

so that
callers can use this method to avoid expensive

unwrap

calls that may fail. If this method
returns true then calling

unwrap

with the same argument should succeed.

---

