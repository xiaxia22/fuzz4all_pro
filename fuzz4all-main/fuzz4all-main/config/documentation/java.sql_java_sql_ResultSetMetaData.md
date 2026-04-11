# Interface ResultSetMetaData

**Source:** `java.sql\java\sql\ResultSetMetaData.html`

### Class Description

```java
public interface
ResultSetMetaData

extends
Wrapper
```

An object that can be used to get information about the types
and properties of the columns in a

ResultSet

object.
The following code fragment creates the

ResultSet

object rs,
creates the

ResultSetMetaData

object rsmd, and uses rsmd
to find out how many columns rs has and whether the first column in rs
can be used in a

WHERE

clause.

```java
ResultSet rs = stmt.executeQuery("SELECT a, b, c FROM TABLE2");
ResultSetMetaData rsmd = rs.getMetaData();
int numberOfColumns = rsmd.getColumnCount();
boolean b = rsmd.isSearchable(1);
```

**All Superinterfaces:** Wrapper

---

### Field Details

#### static final int columnNoNulls

The constant indicating that a
column does not allow

NULL

values.

**See Also:**
- Constant Field Values

---

#### static final int columnNullable

The constant indicating that a
column allows

NULL

values.

**See Also:**
- Constant Field Values

---

#### static final int columnNullableUnknown

The constant indicating that the
nullability of a column's values is unknown.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getColumnCount()
throws
SQLException

Returns the number of columns in this

ResultSet

object.

**Returns:**
- the number of columns

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isAutoIncrement​(int column)
throws
SQLException

Indicates whether the designated column is automatically numbered.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isCaseSensitive​(int column)
throws
SQLException

Indicates whether a column's case matters.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isSearchable​(int column)
throws
SQLException

Indicates whether the designated column can be used in a where clause.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isCurrency​(int column)
throws
SQLException

Indicates whether the designated column is a cash value.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### int isNullable​(int column)
throws
SQLException

Indicates the nullability of values in the designated column.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- the nullability status of the given column; one of

columnNoNulls

,

columnNullable

or

columnNullableUnknown

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isSigned​(int column)
throws
SQLException

Indicates whether values in the designated column are signed numbers.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### int getColumnDisplaySize​(int column)
throws
SQLException

Indicates the designated column's normal maximum width in characters.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- the normal maximum number of characters allowed as the width
of the designated column

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getColumnLabel​(int column)
throws
SQLException

Gets the designated column's suggested title for use in printouts and
displays. The suggested title is usually specified by the SQL

AS

clause. If a SQL

AS

is not specified, the value returned from

getColumnLabel

will be the same as the value returned by the

getColumnName

method.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- the suggested column title

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getColumnName​(int column)
throws
SQLException

Get the designated column's name.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- column name

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getSchemaName​(int column)
throws
SQLException

Get the designated column's table's schema.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- schema name or "" if not applicable

**Throws:**
- SQLException

- if a database access error occurs

---

#### int getPrecision​(int column)
throws
SQLException

Get the designated column's specified column size.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- precision

**Throws:**
- SQLException

- if a database access error occurs

---

#### int getScale​(int column)
throws
SQLException

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- scale

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getTableName​(int column)
throws
SQLException

Gets the designated column's table name.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- table name or "" if not applicable

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getCatalogName​(int column)
throws
SQLException

Gets the designated column's table's catalog name.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- the name of the catalog for the table in which the given column
appears or "" if not applicable

**Throws:**
- SQLException

- if a database access error occurs

---

#### int getColumnType​(int column)
throws
SQLException

Retrieves the designated column's SQL type.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- SQL type from java.sql.Types

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- Types

---

#### String
getColumnTypeName​(int column)
throws
SQLException

Retrieves the designated column's database-specific type name.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- type name used by the database. If the column type is
a user-defined type, then a fully-qualified type name is returned.

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isReadOnly​(int column)
throws
SQLException

Indicates whether the designated column is definitely not writable.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isWritable​(int column)
throws
SQLException

Indicates whether it is possible for a write on the designated column to succeed.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### boolean isDefinitelyWritable​(int column)
throws
SQLException

Indicates whether a write on the designated column will definitely succeed.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

---

#### String
getColumnClassName​(int column)
throws
SQLException

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

ResultSet.getObject

may return a subclass of the
class returned by this method.

**Parameters:**
- column

- the first column is 1, the second is 2, ...

**Returns:**
- the fully-qualified name of the class in the Java programming
language that would be used by the method

ResultSet.getObject

to retrieve the value in the specified
column. This is the class name used for custom mapping.

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.2

---

### Additional Sections

#### Interface ResultSetMetaData

**All Superinterfaces:** Wrapper

**All Known Subinterfaces:** RowSetMetaData

**All Known Implementing Classes:** RowSetMetaDataImpl

```java
public interface
ResultSetMetaData

extends
Wrapper
```

An object that can be used to get information about the types
and properties of the columns in a

ResultSet

object.
The following code fragment creates the

ResultSet

object rs,
creates the

ResultSetMetaData

object rsmd, and uses rsmd
to find out how many columns rs has and whether the first column in rs
can be used in a

WHERE

clause.

```java
ResultSet rs = stmt.executeQuery("SELECT a, b, c FROM TABLE2");
ResultSetMetaData rsmd = rs.getMetaData();
int numberOfColumns = rsmd.getColumnCount();
boolean b = rsmd.isSearchable(1);
```

**Since:** 1.1

public interface

ResultSetMetaData

extends

Wrapper

An object that can be used to get information about the types
and properties of the columns in a

ResultSet

object.
The following code fragment creates the

ResultSet

object rs,
creates the

ResultSetMetaData

object rsmd, and uses rsmd
to find out how many columns rs has and whether the first column in rs
can be used in a

WHERE

clause.

```java
ResultSet rs = stmt.executeQuery("SELECT a, b, c FROM TABLE2");
ResultSetMetaData rsmd = rs.getMetaData();
int numberOfColumns = rsmd.getColumnCount();
boolean b = rsmd.isSearchable(1);
```

ResultSet rs = stmt.executeQuery("SELECT a, b, c FROM TABLE2");
ResultSetMetaData rsmd = rs.getMetaData();
int numberOfColumns = rsmd.getColumnCount();
boolean b = rsmd.isSearchable(1);

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

columnNoNulls

The constant indicating that a
column does not allow

NULL

values.

static int

columnNullable

The constant indicating that a
column allows

NULL

values.

static int

columnNullableUnknown

The constant indicating that the
nullability of a column's values is unknown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCatalogName

​(int column)

Gets the designated column's table's catalog name.

String

getColumnClassName

​(int column)

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

int

getColumnCount

()

Returns the number of columns in this

ResultSet

object.

int

getColumnDisplaySize

​(int column)

Indicates the designated column's normal maximum width in characters.

String

getColumnLabel

​(int column)

Gets the designated column's suggested title for use in printouts and
displays.

String

getColumnName

​(int column)

Get the designated column's name.

int

getColumnType

​(int column)

Retrieves the designated column's SQL type.

String

getColumnTypeName

​(int column)

Retrieves the designated column's database-specific type name.

int

getPrecision

​(int column)

Get the designated column's specified column size.

int

getScale

​(int column)

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

String

getSchemaName

​(int column)

Get the designated column's table's schema.

String

getTableName

​(int column)

Gets the designated column's table name.

boolean

isAutoIncrement

​(int column)

Indicates whether the designated column is automatically numbered.

boolean

isCaseSensitive

​(int column)

Indicates whether a column's case matters.

boolean

isCurrency

​(int column)

Indicates whether the designated column is a cash value.

boolean

isDefinitelyWritable

​(int column)

Indicates whether a write on the designated column will definitely succeed.

int

isNullable

​(int column)

Indicates the nullability of values in the designated column.

boolean

isReadOnly

​(int column)

Indicates whether the designated column is definitely not writable.

boolean

isSearchable

​(int column)

Indicates whether the designated column can be used in a where clause.

boolean

isSigned

​(int column)

Indicates whether values in the designated column are signed numbers.

boolean

isWritable

​(int column)

Indicates whether it is possible for a write on the designated column to succeed.

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

Field Summary

Fields

Modifier and Type

Field

Description

static int

columnNoNulls

The constant indicating that a
column does not allow

NULL

values.

static int

columnNullable

The constant indicating that a
column allows

NULL

values.

static int

columnNullableUnknown

The constant indicating that the
nullability of a column's values is unknown.

---

#### Field Summary

The constant indicating that a
column does not allow

NULL

values.

The constant indicating that a
column allows

NULL

values.

The constant indicating that the
nullability of a column's values is unknown.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getCatalogName

​(int column)

Gets the designated column's table's catalog name.

String

getColumnClassName

​(int column)

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

int

getColumnCount

()

Returns the number of columns in this

ResultSet

object.

int

getColumnDisplaySize

​(int column)

Indicates the designated column's normal maximum width in characters.

String

getColumnLabel

​(int column)

Gets the designated column's suggested title for use in printouts and
displays.

String

getColumnName

​(int column)

Get the designated column's name.

int

getColumnType

​(int column)

Retrieves the designated column's SQL type.

String

getColumnTypeName

​(int column)

Retrieves the designated column's database-specific type name.

int

getPrecision

​(int column)

Get the designated column's specified column size.

int

getScale

​(int column)

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

String

getSchemaName

​(int column)

Get the designated column's table's schema.

String

getTableName

​(int column)

Gets the designated column's table name.

boolean

isAutoIncrement

​(int column)

Indicates whether the designated column is automatically numbered.

boolean

isCaseSensitive

​(int column)

Indicates whether a column's case matters.

boolean

isCurrency

​(int column)

Indicates whether the designated column is a cash value.

boolean

isDefinitelyWritable

​(int column)

Indicates whether a write on the designated column will definitely succeed.

int

isNullable

​(int column)

Indicates the nullability of values in the designated column.

boolean

isReadOnly

​(int column)

Indicates whether the designated column is definitely not writable.

boolean

isSearchable

​(int column)

Indicates whether the designated column can be used in a where clause.

boolean

isSigned

​(int column)

Indicates whether values in the designated column are signed numbers.

boolean

isWritable

​(int column)

Indicates whether it is possible for a write on the designated column to succeed.

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Method Summary

Gets the designated column's table's catalog name.

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

Returns the number of columns in this

ResultSet

object.

Indicates the designated column's normal maximum width in characters.

Gets the designated column's suggested title for use in printouts and
displays.

Get the designated column's name.

Retrieves the designated column's SQL type.

Retrieves the designated column's database-specific type name.

Get the designated column's specified column size.

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

Get the designated column's table's schema.

Gets the designated column's table name.

Indicates whether the designated column is automatically numbered.

Indicates whether a column's case matters.

Indicates whether the designated column is a cash value.

Indicates whether a write on the designated column will definitely succeed.

Indicates the nullability of values in the designated column.

Indicates whether the designated column is definitely not writable.

Indicates whether the designated column can be used in a where clause.

Indicates whether values in the designated column are signed numbers.

Indicates whether it is possible for a write on the designated column to succeed.

Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Methods declared in interface java.sql. Wrapper

============ FIELD DETAIL ===========

- Field Detail

- columnNoNulls

```java
static final int columnNoNulls
```

The constant indicating that a
column does not allow

NULL

values.

**See Also:** Constant Field Values

- columnNullable

```java
static final int columnNullable
```

The constant indicating that a
column allows

NULL

values.

**See Also:** Constant Field Values

- columnNullableUnknown

```java
static final int columnNullableUnknown
```

The constant indicating that the
nullability of a column's values is unknown.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getColumnCount

```java
int getColumnCount()
throws
SQLException
```

Returns the number of columns in this

ResultSet

object.

**Returns:** the number of columns
**Throws:** SQLException

- if a database access error occurs

- isAutoIncrement

```java
boolean isAutoIncrement​(int column)
throws
SQLException
```

Indicates whether the designated column is automatically numbered.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isCaseSensitive

```java
boolean isCaseSensitive​(int column)
throws
SQLException
```

Indicates whether a column's case matters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isSearchable

```java
boolean isSearchable​(int column)
throws
SQLException
```

Indicates whether the designated column can be used in a where clause.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isCurrency

```java
boolean isCurrency​(int column)
throws
SQLException
```

Indicates whether the designated column is a cash value.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isNullable

```java
int isNullable​(int column)
throws
SQLException
```

Indicates the nullability of values in the designated column.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the nullability status of the given column; one of

columnNoNulls

,

columnNullable

or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs

- isSigned

```java
boolean isSigned​(int column)
throws
SQLException
```

Indicates whether values in the designated column are signed numbers.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- getColumnDisplaySize

```java
int getColumnDisplaySize​(int column)
throws
SQLException
```

Indicates the designated column's normal maximum width in characters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the normal maximum number of characters allowed as the width
of the designated column
**Throws:** SQLException

- if a database access error occurs

- getColumnLabel

```java
String
getColumnLabel​(int column)
throws
SQLException
```

Gets the designated column's suggested title for use in printouts and
displays. The suggested title is usually specified by the SQL

AS

clause. If a SQL

AS

is not specified, the value returned from

getColumnLabel

will be the same as the value returned by the

getColumnName

method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the suggested column title
**Throws:** SQLException

- if a database access error occurs

- getColumnName

```java
String
getColumnName​(int column)
throws
SQLException
```

Get the designated column's name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** column name
**Throws:** SQLException

- if a database access error occurs

- getSchemaName

```java
String
getSchemaName​(int column)
throws
SQLException
```

Get the designated column's table's schema.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** schema name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getPrecision

```java
int getPrecision​(int column)
throws
SQLException
```

Get the designated column's specified column size.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs

- getScale

```java
int getScale​(int column)
throws
SQLException
```

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs

- getTableName

```java
String
getTableName​(int column)
throws
SQLException
```

Gets the designated column's table name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** table name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getCatalogName

```java
String
getCatalogName​(int column)
throws
SQLException
```

Gets the designated column's table's catalog name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the name of the catalog for the table in which the given column
appears or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getColumnType

```java
int getColumnType​(int column)
throws
SQLException
```

Retrieves the designated column's SQL type.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** SQL type from java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

- getColumnTypeName

```java
String
getColumnTypeName​(int column)
throws
SQLException
```

Retrieves the designated column's database-specific type name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** type name used by the database. If the column type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs

- isReadOnly

```java
boolean isReadOnly​(int column)
throws
SQLException
```

Indicates whether the designated column is definitely not writable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isWritable

```java
boolean isWritable​(int column)
throws
SQLException
```

Indicates whether it is possible for a write on the designated column to succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isDefinitelyWritable

```java
boolean isDefinitelyWritable​(int column)
throws
SQLException
```

Indicates whether a write on the designated column will definitely succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- getColumnClassName

```java
String
getColumnClassName​(int column)
throws
SQLException
```

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

ResultSet.getObject

may return a subclass of the
class returned by this method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

ResultSet.getObject

to retrieve the value in the specified
column. This is the class name used for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.2

Field Detail

- columnNoNulls

```java
static final int columnNoNulls
```

The constant indicating that a
column does not allow

NULL

values.

**See Also:** Constant Field Values

- columnNullable

```java
static final int columnNullable
```

The constant indicating that a
column allows

NULL

values.

**See Also:** Constant Field Values

- columnNullableUnknown

```java
static final int columnNullableUnknown
```

The constant indicating that the
nullability of a column's values is unknown.

**See Also:** Constant Field Values

---

#### Field Detail

columnNoNulls

```java
static final int columnNoNulls
```

The constant indicating that a
column does not allow

NULL

values.

**See Also:** Constant Field Values

---

#### columnNoNulls

static final int columnNoNulls

The constant indicating that a
column does not allow

NULL

values.

columnNullable

```java
static final int columnNullable
```

The constant indicating that a
column allows

NULL

values.

**See Also:** Constant Field Values

---

#### columnNullable

static final int columnNullable

The constant indicating that a
column allows

NULL

values.

columnNullableUnknown

```java
static final int columnNullableUnknown
```

The constant indicating that the
nullability of a column's values is unknown.

**See Also:** Constant Field Values

---

#### columnNullableUnknown

static final int columnNullableUnknown

The constant indicating that the
nullability of a column's values is unknown.

Method Detail

- getColumnCount

```java
int getColumnCount()
throws
SQLException
```

Returns the number of columns in this

ResultSet

object.

**Returns:** the number of columns
**Throws:** SQLException

- if a database access error occurs

- isAutoIncrement

```java
boolean isAutoIncrement​(int column)
throws
SQLException
```

Indicates whether the designated column is automatically numbered.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isCaseSensitive

```java
boolean isCaseSensitive​(int column)
throws
SQLException
```

Indicates whether a column's case matters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isSearchable

```java
boolean isSearchable​(int column)
throws
SQLException
```

Indicates whether the designated column can be used in a where clause.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isCurrency

```java
boolean isCurrency​(int column)
throws
SQLException
```

Indicates whether the designated column is a cash value.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isNullable

```java
int isNullable​(int column)
throws
SQLException
```

Indicates the nullability of values in the designated column.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the nullability status of the given column; one of

columnNoNulls

,

columnNullable

or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs

- isSigned

```java
boolean isSigned​(int column)
throws
SQLException
```

Indicates whether values in the designated column are signed numbers.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- getColumnDisplaySize

```java
int getColumnDisplaySize​(int column)
throws
SQLException
```

Indicates the designated column's normal maximum width in characters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the normal maximum number of characters allowed as the width
of the designated column
**Throws:** SQLException

- if a database access error occurs

- getColumnLabel

```java
String
getColumnLabel​(int column)
throws
SQLException
```

Gets the designated column's suggested title for use in printouts and
displays. The suggested title is usually specified by the SQL

AS

clause. If a SQL

AS

is not specified, the value returned from

getColumnLabel

will be the same as the value returned by the

getColumnName

method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the suggested column title
**Throws:** SQLException

- if a database access error occurs

- getColumnName

```java
String
getColumnName​(int column)
throws
SQLException
```

Get the designated column's name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** column name
**Throws:** SQLException

- if a database access error occurs

- getSchemaName

```java
String
getSchemaName​(int column)
throws
SQLException
```

Get the designated column's table's schema.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** schema name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getPrecision

```java
int getPrecision​(int column)
throws
SQLException
```

Get the designated column's specified column size.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs

- getScale

```java
int getScale​(int column)
throws
SQLException
```

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs

- getTableName

```java
String
getTableName​(int column)
throws
SQLException
```

Gets the designated column's table name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** table name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getCatalogName

```java
String
getCatalogName​(int column)
throws
SQLException
```

Gets the designated column's table's catalog name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the name of the catalog for the table in which the given column
appears or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

- getColumnType

```java
int getColumnType​(int column)
throws
SQLException
```

Retrieves the designated column's SQL type.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** SQL type from java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

- getColumnTypeName

```java
String
getColumnTypeName​(int column)
throws
SQLException
```

Retrieves the designated column's database-specific type name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** type name used by the database. If the column type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs

- isReadOnly

```java
boolean isReadOnly​(int column)
throws
SQLException
```

Indicates whether the designated column is definitely not writable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isWritable

```java
boolean isWritable​(int column)
throws
SQLException
```

Indicates whether it is possible for a write on the designated column to succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- isDefinitelyWritable

```java
boolean isDefinitelyWritable​(int column)
throws
SQLException
```

Indicates whether a write on the designated column will definitely succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

- getColumnClassName

```java
String
getColumnClassName​(int column)
throws
SQLException
```

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

ResultSet.getObject

may return a subclass of the
class returned by this method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

ResultSet.getObject

to retrieve the value in the specified
column. This is the class name used for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.2

---

#### Method Detail

getColumnCount

```java
int getColumnCount()
throws
SQLException
```

Returns the number of columns in this

ResultSet

object.

**Returns:** the number of columns
**Throws:** SQLException

- if a database access error occurs

---

#### getColumnCount

int getColumnCount()
throws

SQLException

Returns the number of columns in this

ResultSet

object.

isAutoIncrement

```java
boolean isAutoIncrement​(int column)
throws
SQLException
```

Indicates whether the designated column is automatically numbered.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isAutoIncrement

boolean isAutoIncrement​(int column)
throws

SQLException

Indicates whether the designated column is automatically numbered.

isCaseSensitive

```java
boolean isCaseSensitive​(int column)
throws
SQLException
```

Indicates whether a column's case matters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isCaseSensitive

boolean isCaseSensitive​(int column)
throws

SQLException

Indicates whether a column's case matters.

isSearchable

```java
boolean isSearchable​(int column)
throws
SQLException
```

Indicates whether the designated column can be used in a where clause.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isSearchable

boolean isSearchable​(int column)
throws

SQLException

Indicates whether the designated column can be used in a where clause.

isCurrency

```java
boolean isCurrency​(int column)
throws
SQLException
```

Indicates whether the designated column is a cash value.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isCurrency

boolean isCurrency​(int column)
throws

SQLException

Indicates whether the designated column is a cash value.

isNullable

```java
int isNullable​(int column)
throws
SQLException
```

Indicates the nullability of values in the designated column.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the nullability status of the given column; one of

columnNoNulls

,

columnNullable

or

columnNullableUnknown
**Throws:** SQLException

- if a database access error occurs

---

#### isNullable

int isNullable​(int column)
throws

SQLException

Indicates the nullability of values in the designated column.

isSigned

```java
boolean isSigned​(int column)
throws
SQLException
```

Indicates whether values in the designated column are signed numbers.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isSigned

boolean isSigned​(int column)
throws

SQLException

Indicates whether values in the designated column are signed numbers.

getColumnDisplaySize

```java
int getColumnDisplaySize​(int column)
throws
SQLException
```

Indicates the designated column's normal maximum width in characters.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the normal maximum number of characters allowed as the width
of the designated column
**Throws:** SQLException

- if a database access error occurs

---

#### getColumnDisplaySize

int getColumnDisplaySize​(int column)
throws

SQLException

Indicates the designated column's normal maximum width in characters.

getColumnLabel

```java
String
getColumnLabel​(int column)
throws
SQLException
```

Gets the designated column's suggested title for use in printouts and
displays. The suggested title is usually specified by the SQL

AS

clause. If a SQL

AS

is not specified, the value returned from

getColumnLabel

will be the same as the value returned by the

getColumnName

method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the suggested column title
**Throws:** SQLException

- if a database access error occurs

---

#### getColumnLabel

String

getColumnLabel​(int column)
throws

SQLException

Gets the designated column's suggested title for use in printouts and
displays. The suggested title is usually specified by the SQL

AS

clause. If a SQL

AS

is not specified, the value returned from

getColumnLabel

will be the same as the value returned by the

getColumnName

method.

getColumnName

```java
String
getColumnName​(int column)
throws
SQLException
```

Get the designated column's name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** column name
**Throws:** SQLException

- if a database access error occurs

---

#### getColumnName

String

getColumnName​(int column)
throws

SQLException

Get the designated column's name.

getSchemaName

```java
String
getSchemaName​(int column)
throws
SQLException
```

Get the designated column's table's schema.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** schema name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

---

#### getSchemaName

String

getSchemaName​(int column)
throws

SQLException

Get the designated column's table's schema.

getPrecision

```java
int getPrecision​(int column)
throws
SQLException
```

Get the designated column's specified column size.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs

---

#### getPrecision

int getPrecision​(int column)
throws

SQLException

Get the designated column's specified column size.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

getScale

```java
int getScale​(int column)
throws
SQLException
```

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs

---

#### getScale

int getScale​(int column)
throws

SQLException

Gets the designated column's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

getTableName

```java
String
getTableName​(int column)
throws
SQLException
```

Gets the designated column's table name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** table name or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

---

#### getTableName

String

getTableName​(int column)
throws

SQLException

Gets the designated column's table name.

getCatalogName

```java
String
getCatalogName​(int column)
throws
SQLException
```

Gets the designated column's table's catalog name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the name of the catalog for the table in which the given column
appears or "" if not applicable
**Throws:** SQLException

- if a database access error occurs

---

#### getCatalogName

String

getCatalogName​(int column)
throws

SQLException

Gets the designated column's table's catalog name.

getColumnType

```java
int getColumnType​(int column)
throws
SQLException
```

Retrieves the designated column's SQL type.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** SQL type from java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**See Also:** Types

---

#### getColumnType

int getColumnType​(int column)
throws

SQLException

Retrieves the designated column's SQL type.

getColumnTypeName

```java
String
getColumnTypeName​(int column)
throws
SQLException
```

Retrieves the designated column's database-specific type name.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** type name used by the database. If the column type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs

---

#### getColumnTypeName

String

getColumnTypeName​(int column)
throws

SQLException

Retrieves the designated column's database-specific type name.

isReadOnly

```java
boolean isReadOnly​(int column)
throws
SQLException
```

Indicates whether the designated column is definitely not writable.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isReadOnly

boolean isReadOnly​(int column)
throws

SQLException

Indicates whether the designated column is definitely not writable.

isWritable

```java
boolean isWritable​(int column)
throws
SQLException
```

Indicates whether it is possible for a write on the designated column to succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isWritable

boolean isWritable​(int column)
throws

SQLException

Indicates whether it is possible for a write on the designated column to succeed.

isDefinitelyWritable

```java
boolean isDefinitelyWritable​(int column)
throws
SQLException
```

Indicates whether a write on the designated column will definitely succeed.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs

---

#### isDefinitelyWritable

boolean isDefinitelyWritable​(int column)
throws

SQLException

Indicates whether a write on the designated column will definitely succeed.

getColumnClassName

```java
String
getColumnClassName​(int column)
throws
SQLException
```

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

ResultSet.getObject

may return a subclass of the
class returned by this method.

**Parameters:** column

- the first column is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

ResultSet.getObject

to retrieve the value in the specified
column. This is the class name used for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.2

---

#### getColumnClassName

String

getColumnClassName​(int column)
throws

SQLException

Returns the fully-qualified name of the Java class whose instances
are manufactured if the method

ResultSet.getObject

is called to retrieve a value
from the column.

ResultSet.getObject

may return a subclass of the
class returned by this method.

---

