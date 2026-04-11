# Enum JDBCType

**Source:** `java.sql\java\sql\JDBCType.html`

### Class Description

```java
public enum
JDBCType

extends
Enum
<
JDBCType
>
implements
SQLType
```

Defines the constants that are used to identify generic
SQL types, called JDBC types.

**All Implemented Interfaces:** Serializable

,

Comparable

<

JDBCType

>

,

SQLType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
JDBCType
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JDBCType c : JDBCType.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
JDBCType
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

#### public
String
getName()

Returns the

SQLType

name that represents a SQL data type.

**Specified by:**
- getName

in interface

SQLType

**Returns:**
- The name of this

SQLType

.

---

#### public
String
getVendor()

Returns the name of the vendor that supports this data type.

**Specified by:**
- getVendor

in interface

SQLType

**Returns:**
- The name of the vendor for this data type which is
java.sql for JDBCType.

---

#### public
Integer
getVendorTypeNumber()

Returns the vendor specific type number for the data type.

**Specified by:**
- getVendorTypeNumber

in interface

SQLType

**Returns:**
- An Integer representing the data type. For

JDBCType

,
the value will be the same value as in

Types

for the data type.

---

#### public static
JDBCType
valueOf​(int type)

Returns the

JDBCType

that corresponds to the specified

Types

value

**Parameters:**
- type

-

Types

value

**Returns:**
- The

JDBCType

constant

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with
the specified

Types

value

**See Also:**
- Types

---

### Additional Sections

#### Enum JDBCType

java.lang.Object

- java.lang.Enum

<

JDBCType

>
- - java.sql.JDBCType

java.lang.Enum

<

JDBCType

>

- java.sql.JDBCType

java.sql.JDBCType

**All Implemented Interfaces:** Serializable

,

Comparable

<

JDBCType

>

,

SQLType

```java
public enum
JDBCType

extends
Enum
<
JDBCType
>
implements
SQLType
```

Defines the constants that are used to identify generic
SQL types, called JDBC types.

**Since:** 1.8
**See Also:** SQLType

public enum

JDBCType

extends

Enum

<

JDBCType

>
implements

SQLType

Defines the constants that are used to identify generic
SQL types, called JDBC types.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ARRAY

Identifies the generic SQL type

ARRAY

.

BIGINT

Identifies the generic SQL type

BIGINT

.

BINARY

Identifies the generic SQL type

BINARY

.

BIT

Identifies the generic SQL type

BIT

.

BLOB

Identifies the generic SQL type

BLOB

.

BOOLEAN

Identifies the generic SQL type

BOOLEAN

.

CHAR

Identifies the generic SQL type

CHAR

.

CLOB

Identifies the generic SQL type

CLOB

.

DATALINK

Identifies the generic SQL type

DATALINK

.

DATE

Identifies the generic SQL type

DATE

.

DECIMAL

Identifies the generic SQL type

DECIMAL

.

DISTINCT

Identifies the generic SQL type

DISTINCT

.

DOUBLE

Identifies the generic SQL type

DOUBLE

.

FLOAT

Identifies the generic SQL type

FLOAT

.

INTEGER

Identifies the generic SQL type

INTEGER

.

JAVA_OBJECT

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

LONGNVARCHAR

Identifies the generic SQL type

LONGNVARCHAR

.

LONGVARBINARY

Identifies the generic SQL type

LONGVARBINARY

.

LONGVARCHAR

Identifies the generic SQL type

LONGVARCHAR

.

NCHAR

Identifies the generic SQL type

NCHAR

.

NCLOB

Identifies the generic SQL type

NCLOB

.

NULL

Identifies the generic SQL value

NULL

.

NUMERIC

Identifies the generic SQL type

NUMERIC

.

NVARCHAR

Identifies the generic SQL type

NVARCHAR

.

OTHER

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

REAL

Identifies the generic SQL type

REAL

.

REF

Identifies the generic SQL type

REF

.

REF_CURSOR

Identifies the generic SQL type

REF_CURSOR

.

ROWID

Identifies the SQL type

ROWID

.

SMALLINT

Identifies the generic SQL type

SMALLINT

.

SQLXML

Identifies the generic SQL type

SQLXML

.

STRUCT

Identifies the generic SQL type

STRUCT

.

TIME

Identifies the generic SQL type

TIME

.

TIME_WITH_TIMEZONE

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

TIMESTAMP

Identifies the generic SQL type

TIMESTAMP

.

TIMESTAMP_WITH_TIMEZONE

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

TINYINT

Identifies the generic SQL type

TINYINT

.

VARBINARY

Identifies the generic SQL type

VARBINARY

.

VARCHAR

Identifies the generic SQL type

VARCHAR

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the

SQLType

name that represents a SQL data type.

String

getVendor

()

Returns the name of the vendor that supports this data type.

Integer

getVendorTypeNumber

()

Returns the vendor specific type number for the data type.

static

JDBCType

valueOf

​(int type)

Returns the

JDBCType

that corresponds to the specified

Types

value

static

JDBCType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JDBCType

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

ARRAY

Identifies the generic SQL type

ARRAY

.

BIGINT

Identifies the generic SQL type

BIGINT

.

BINARY

Identifies the generic SQL type

BINARY

.

BIT

Identifies the generic SQL type

BIT

.

BLOB

Identifies the generic SQL type

BLOB

.

BOOLEAN

Identifies the generic SQL type

BOOLEAN

.

CHAR

Identifies the generic SQL type

CHAR

.

CLOB

Identifies the generic SQL type

CLOB

.

DATALINK

Identifies the generic SQL type

DATALINK

.

DATE

Identifies the generic SQL type

DATE

.

DECIMAL

Identifies the generic SQL type

DECIMAL

.

DISTINCT

Identifies the generic SQL type

DISTINCT

.

DOUBLE

Identifies the generic SQL type

DOUBLE

.

FLOAT

Identifies the generic SQL type

FLOAT

.

INTEGER

Identifies the generic SQL type

INTEGER

.

JAVA_OBJECT

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

LONGNVARCHAR

Identifies the generic SQL type

LONGNVARCHAR

.

LONGVARBINARY

Identifies the generic SQL type

LONGVARBINARY

.

LONGVARCHAR

Identifies the generic SQL type

LONGVARCHAR

.

NCHAR

Identifies the generic SQL type

NCHAR

.

NCLOB

Identifies the generic SQL type

NCLOB

.

NULL

Identifies the generic SQL value

NULL

.

NUMERIC

Identifies the generic SQL type

NUMERIC

.

NVARCHAR

Identifies the generic SQL type

NVARCHAR

.

OTHER

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

REAL

Identifies the generic SQL type

REAL

.

REF

Identifies the generic SQL type

REF

.

REF_CURSOR

Identifies the generic SQL type

REF_CURSOR

.

ROWID

Identifies the SQL type

ROWID

.

SMALLINT

Identifies the generic SQL type

SMALLINT

.

SQLXML

Identifies the generic SQL type

SQLXML

.

STRUCT

Identifies the generic SQL type

STRUCT

.

TIME

Identifies the generic SQL type

TIME

.

TIME_WITH_TIMEZONE

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

TIMESTAMP

Identifies the generic SQL type

TIMESTAMP

.

TIMESTAMP_WITH_TIMEZONE

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

TINYINT

Identifies the generic SQL type

TINYINT

.

VARBINARY

Identifies the generic SQL type

VARBINARY

.

VARCHAR

Identifies the generic SQL type

VARCHAR

.

---

#### Enum Constant Summary

Identifies the generic SQL type

ARRAY

.

Identifies the generic SQL type

BIGINT

.

Identifies the generic SQL type

BINARY

.

Identifies the generic SQL type

BIT

.

Identifies the generic SQL type

BLOB

.

Identifies the generic SQL type

BOOLEAN

.

Identifies the generic SQL type

CHAR

.

Identifies the generic SQL type

CLOB

.

Identifies the generic SQL type

DATALINK

.

Identifies the generic SQL type

DATE

.

Identifies the generic SQL type

DECIMAL

.

Identifies the generic SQL type

DISTINCT

.

Identifies the generic SQL type

DOUBLE

.

Identifies the generic SQL type

FLOAT

.

Identifies the generic SQL type

INTEGER

.

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

Identifies the generic SQL type

LONGNVARCHAR

.

Identifies the generic SQL type

LONGVARBINARY

.

Identifies the generic SQL type

LONGVARCHAR

.

Identifies the generic SQL type

NCHAR

.

Identifies the generic SQL type

NCLOB

.

Identifies the generic SQL value

NULL

.

Identifies the generic SQL type

NUMERIC

.

Identifies the generic SQL type

NVARCHAR

.

Identifies the generic SQL type

REAL

.

Identifies the generic SQL type

REF

.

Identifies the generic SQL type

REF_CURSOR

.

Identifies the SQL type

ROWID

.

Identifies the generic SQL type

SMALLINT

.

Identifies the generic SQL type

SQLXML

.

Identifies the generic SQL type

STRUCT

.

Identifies the generic SQL type

TIME

.

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

Identifies the generic SQL type

TIMESTAMP

.

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

Identifies the generic SQL type

TINYINT

.

Identifies the generic SQL type

VARBINARY

.

Identifies the generic SQL type

VARCHAR

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the

SQLType

name that represents a SQL data type.

String

getVendor

()

Returns the name of the vendor that supports this data type.

Integer

getVendorTypeNumber

()

Returns the vendor specific type number for the data type.

static

JDBCType

valueOf

​(int type)

Returns the

JDBCType

that corresponds to the specified

Types

value

static

JDBCType

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

JDBCType

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

#### Method Summary

Returns the

SQLType

name that represents a SQL data type.

Returns the name of the vendor that supports this data type.

Returns the vendor specific type number for the data type.

Returns the

JDBCType

that corresponds to the specified

Types

value

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- BIT

```java
public static final
JDBCType
BIT
```

Identifies the generic SQL type

BIT

.

- TINYINT

```java
public static final
JDBCType
TINYINT
```

Identifies the generic SQL type

TINYINT

.

- SMALLINT

```java
public static final
JDBCType
SMALLINT
```

Identifies the generic SQL type

SMALLINT

.

- INTEGER

```java
public static final
JDBCType
INTEGER
```

Identifies the generic SQL type

INTEGER

.

- BIGINT

```java
public static final
JDBCType
BIGINT
```

Identifies the generic SQL type

BIGINT

.

- FLOAT

```java
public static final
JDBCType
FLOAT
```

Identifies the generic SQL type

FLOAT

.

- REAL

```java
public static final
JDBCType
REAL
```

Identifies the generic SQL type

REAL

.

- DOUBLE

```java
public static final
JDBCType
DOUBLE
```

Identifies the generic SQL type

DOUBLE

.

- NUMERIC

```java
public static final
JDBCType
NUMERIC
```

Identifies the generic SQL type

NUMERIC

.

- DECIMAL

```java
public static final
JDBCType
DECIMAL
```

Identifies the generic SQL type

DECIMAL

.

- CHAR

```java
public static final
JDBCType
CHAR
```

Identifies the generic SQL type

CHAR

.

- VARCHAR

```java
public static final
JDBCType
VARCHAR
```

Identifies the generic SQL type

VARCHAR

.

- LONGVARCHAR

```java
public static final
JDBCType
LONGVARCHAR
```

Identifies the generic SQL type

LONGVARCHAR

.

- DATE

```java
public static final
JDBCType
DATE
```

Identifies the generic SQL type

DATE

.

- TIME

```java
public static final
JDBCType
TIME
```

Identifies the generic SQL type

TIME

.

- TIMESTAMP

```java
public static final
JDBCType
TIMESTAMP
```

Identifies the generic SQL type

TIMESTAMP

.

- BINARY

```java
public static final
JDBCType
BINARY
```

Identifies the generic SQL type

BINARY

.

- VARBINARY

```java
public static final
JDBCType
VARBINARY
```

Identifies the generic SQL type

VARBINARY

.

- LONGVARBINARY

```java
public static final
JDBCType
LONGVARBINARY
```

Identifies the generic SQL type

LONGVARBINARY

.

- NULL

```java
public static final
JDBCType
NULL
```

Identifies the generic SQL value

NULL

.

- OTHER

```java
public static final
JDBCType
OTHER
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

- JAVA_OBJECT

```java
public static final
JDBCType
JAVA_OBJECT
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

- DISTINCT

```java
public static final
JDBCType
DISTINCT
```

Identifies the generic SQL type

DISTINCT

.

- STRUCT

```java
public static final
JDBCType
STRUCT
```

Identifies the generic SQL type

STRUCT

.

- ARRAY

```java
public static final
JDBCType
ARRAY
```

Identifies the generic SQL type

ARRAY

.

- BLOB

```java
public static final
JDBCType
BLOB
```

Identifies the generic SQL type

BLOB

.

- CLOB

```java
public static final
JDBCType
CLOB
```

Identifies the generic SQL type

CLOB

.

- REF

```java
public static final
JDBCType
REF
```

Identifies the generic SQL type

REF

.

- DATALINK

```java
public static final
JDBCType
DATALINK
```

Identifies the generic SQL type

DATALINK

.

- BOOLEAN

```java
public static final
JDBCType
BOOLEAN
```

Identifies the generic SQL type

BOOLEAN

.

- ROWID

```java
public static final
JDBCType
ROWID
```

Identifies the SQL type

ROWID

.

- NCHAR

```java
public static final
JDBCType
NCHAR
```

Identifies the generic SQL type

NCHAR

.

- NVARCHAR

```java
public static final
JDBCType
NVARCHAR
```

Identifies the generic SQL type

NVARCHAR

.

- LONGNVARCHAR

```java
public static final
JDBCType
LONGNVARCHAR
```

Identifies the generic SQL type

LONGNVARCHAR

.

- NCLOB

```java
public static final
JDBCType
NCLOB
```

Identifies the generic SQL type

NCLOB

.

- SQLXML

```java
public static final
JDBCType
SQLXML
```

Identifies the generic SQL type

SQLXML

.

- REF_CURSOR

```java
public static final
JDBCType
REF_CURSOR
```

Identifies the generic SQL type

REF_CURSOR

.

- TIME_WITH_TIMEZONE

```java
public static final
JDBCType
TIME_WITH_TIMEZONE
```

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

- TIMESTAMP_WITH_TIMEZONE

```java
public static final
JDBCType
TIMESTAMP_WITH_TIMEZONE
```

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
JDBCType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JDBCType c : JDBCType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JDBCType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getName

```java
public
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Specified by:** getName

in interface

SQLType
**Returns:** The name of this

SQLType

.

- getVendor

```java
public
String
getVendor()
```

Returns the name of the vendor that supports this data type.

**Specified by:** getVendor

in interface

SQLType
**Returns:** The name of the vendor for this data type which is
java.sql for JDBCType.

- getVendorTypeNumber

```java
public
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Specified by:** getVendorTypeNumber

in interface

SQLType
**Returns:** An Integer representing the data type. For

JDBCType

,
the value will be the same value as in

Types

for the data type.

- valueOf

```java
public static
JDBCType
valueOf​(int type)
```

Returns the

JDBCType

that corresponds to the specified

Types

value

**Parameters:** type

-

Types

value
**Returns:** The

JDBCType

constant
**Throws:** IllegalArgumentException

- if this enum type has no constant with
the specified

Types

value
**See Also:** Types

Enum Constant Detail

- BIT

```java
public static final
JDBCType
BIT
```

Identifies the generic SQL type

BIT

.

- TINYINT

```java
public static final
JDBCType
TINYINT
```

Identifies the generic SQL type

TINYINT

.

- SMALLINT

```java
public static final
JDBCType
SMALLINT
```

Identifies the generic SQL type

SMALLINT

.

- INTEGER

```java
public static final
JDBCType
INTEGER
```

Identifies the generic SQL type

INTEGER

.

- BIGINT

```java
public static final
JDBCType
BIGINT
```

Identifies the generic SQL type

BIGINT

.

- FLOAT

```java
public static final
JDBCType
FLOAT
```

Identifies the generic SQL type

FLOAT

.

- REAL

```java
public static final
JDBCType
REAL
```

Identifies the generic SQL type

REAL

.

- DOUBLE

```java
public static final
JDBCType
DOUBLE
```

Identifies the generic SQL type

DOUBLE

.

- NUMERIC

```java
public static final
JDBCType
NUMERIC
```

Identifies the generic SQL type

NUMERIC

.

- DECIMAL

```java
public static final
JDBCType
DECIMAL
```

Identifies the generic SQL type

DECIMAL

.

- CHAR

```java
public static final
JDBCType
CHAR
```

Identifies the generic SQL type

CHAR

.

- VARCHAR

```java
public static final
JDBCType
VARCHAR
```

Identifies the generic SQL type

VARCHAR

.

- LONGVARCHAR

```java
public static final
JDBCType
LONGVARCHAR
```

Identifies the generic SQL type

LONGVARCHAR

.

- DATE

```java
public static final
JDBCType
DATE
```

Identifies the generic SQL type

DATE

.

- TIME

```java
public static final
JDBCType
TIME
```

Identifies the generic SQL type

TIME

.

- TIMESTAMP

```java
public static final
JDBCType
TIMESTAMP
```

Identifies the generic SQL type

TIMESTAMP

.

- BINARY

```java
public static final
JDBCType
BINARY
```

Identifies the generic SQL type

BINARY

.

- VARBINARY

```java
public static final
JDBCType
VARBINARY
```

Identifies the generic SQL type

VARBINARY

.

- LONGVARBINARY

```java
public static final
JDBCType
LONGVARBINARY
```

Identifies the generic SQL type

LONGVARBINARY

.

- NULL

```java
public static final
JDBCType
NULL
```

Identifies the generic SQL value

NULL

.

- OTHER

```java
public static final
JDBCType
OTHER
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

- JAVA_OBJECT

```java
public static final
JDBCType
JAVA_OBJECT
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

- DISTINCT

```java
public static final
JDBCType
DISTINCT
```

Identifies the generic SQL type

DISTINCT

.

- STRUCT

```java
public static final
JDBCType
STRUCT
```

Identifies the generic SQL type

STRUCT

.

- ARRAY

```java
public static final
JDBCType
ARRAY
```

Identifies the generic SQL type

ARRAY

.

- BLOB

```java
public static final
JDBCType
BLOB
```

Identifies the generic SQL type

BLOB

.

- CLOB

```java
public static final
JDBCType
CLOB
```

Identifies the generic SQL type

CLOB

.

- REF

```java
public static final
JDBCType
REF
```

Identifies the generic SQL type

REF

.

- DATALINK

```java
public static final
JDBCType
DATALINK
```

Identifies the generic SQL type

DATALINK

.

- BOOLEAN

```java
public static final
JDBCType
BOOLEAN
```

Identifies the generic SQL type

BOOLEAN

.

- ROWID

```java
public static final
JDBCType
ROWID
```

Identifies the SQL type

ROWID

.

- NCHAR

```java
public static final
JDBCType
NCHAR
```

Identifies the generic SQL type

NCHAR

.

- NVARCHAR

```java
public static final
JDBCType
NVARCHAR
```

Identifies the generic SQL type

NVARCHAR

.

- LONGNVARCHAR

```java
public static final
JDBCType
LONGNVARCHAR
```

Identifies the generic SQL type

LONGNVARCHAR

.

- NCLOB

```java
public static final
JDBCType
NCLOB
```

Identifies the generic SQL type

NCLOB

.

- SQLXML

```java
public static final
JDBCType
SQLXML
```

Identifies the generic SQL type

SQLXML

.

- REF_CURSOR

```java
public static final
JDBCType
REF_CURSOR
```

Identifies the generic SQL type

REF_CURSOR

.

- TIME_WITH_TIMEZONE

```java
public static final
JDBCType
TIME_WITH_TIMEZONE
```

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

- TIMESTAMP_WITH_TIMEZONE

```java
public static final
JDBCType
TIMESTAMP_WITH_TIMEZONE
```

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

---

#### Enum Constant Detail

BIT

```java
public static final
JDBCType
BIT
```

Identifies the generic SQL type

BIT

.

---

#### BIT

public static final

JDBCType

BIT

Identifies the generic SQL type

BIT

.

TINYINT

```java
public static final
JDBCType
TINYINT
```

Identifies the generic SQL type

TINYINT

.

---

#### TINYINT

public static final

JDBCType

TINYINT

Identifies the generic SQL type

TINYINT

.

SMALLINT

```java
public static final
JDBCType
SMALLINT
```

Identifies the generic SQL type

SMALLINT

.

---

#### SMALLINT

public static final

JDBCType

SMALLINT

Identifies the generic SQL type

SMALLINT

.

INTEGER

```java
public static final
JDBCType
INTEGER
```

Identifies the generic SQL type

INTEGER

.

---

#### INTEGER

public static final

JDBCType

INTEGER

Identifies the generic SQL type

INTEGER

.

BIGINT

```java
public static final
JDBCType
BIGINT
```

Identifies the generic SQL type

BIGINT

.

---

#### BIGINT

public static final

JDBCType

BIGINT

Identifies the generic SQL type

BIGINT

.

FLOAT

```java
public static final
JDBCType
FLOAT
```

Identifies the generic SQL type

FLOAT

.

---

#### FLOAT

public static final

JDBCType

FLOAT

Identifies the generic SQL type

FLOAT

.

REAL

```java
public static final
JDBCType
REAL
```

Identifies the generic SQL type

REAL

.

---

#### REAL

public static final

JDBCType

REAL

Identifies the generic SQL type

REAL

.

DOUBLE

```java
public static final
JDBCType
DOUBLE
```

Identifies the generic SQL type

DOUBLE

.

---

#### DOUBLE

public static final

JDBCType

DOUBLE

Identifies the generic SQL type

DOUBLE

.

NUMERIC

```java
public static final
JDBCType
NUMERIC
```

Identifies the generic SQL type

NUMERIC

.

---

#### NUMERIC

public static final

JDBCType

NUMERIC

Identifies the generic SQL type

NUMERIC

.

DECIMAL

```java
public static final
JDBCType
DECIMAL
```

Identifies the generic SQL type

DECIMAL

.

---

#### DECIMAL

public static final

JDBCType

DECIMAL

Identifies the generic SQL type

DECIMAL

.

CHAR

```java
public static final
JDBCType
CHAR
```

Identifies the generic SQL type

CHAR

.

---

#### CHAR

public static final

JDBCType

CHAR

Identifies the generic SQL type

CHAR

.

VARCHAR

```java
public static final
JDBCType
VARCHAR
```

Identifies the generic SQL type

VARCHAR

.

---

#### VARCHAR

public static final

JDBCType

VARCHAR

Identifies the generic SQL type

VARCHAR

.

LONGVARCHAR

```java
public static final
JDBCType
LONGVARCHAR
```

Identifies the generic SQL type

LONGVARCHAR

.

---

#### LONGVARCHAR

public static final

JDBCType

LONGVARCHAR

Identifies the generic SQL type

LONGVARCHAR

.

DATE

```java
public static final
JDBCType
DATE
```

Identifies the generic SQL type

DATE

.

---

#### DATE

public static final

JDBCType

DATE

Identifies the generic SQL type

DATE

.

TIME

```java
public static final
JDBCType
TIME
```

Identifies the generic SQL type

TIME

.

---

#### TIME

public static final

JDBCType

TIME

Identifies the generic SQL type

TIME

.

TIMESTAMP

```java
public static final
JDBCType
TIMESTAMP
```

Identifies the generic SQL type

TIMESTAMP

.

---

#### TIMESTAMP

public static final

JDBCType

TIMESTAMP

Identifies the generic SQL type

TIMESTAMP

.

BINARY

```java
public static final
JDBCType
BINARY
```

Identifies the generic SQL type

BINARY

.

---

#### BINARY

public static final

JDBCType

BINARY

Identifies the generic SQL type

BINARY

.

VARBINARY

```java
public static final
JDBCType
VARBINARY
```

Identifies the generic SQL type

VARBINARY

.

---

#### VARBINARY

public static final

JDBCType

VARBINARY

Identifies the generic SQL type

VARBINARY

.

LONGVARBINARY

```java
public static final
JDBCType
LONGVARBINARY
```

Identifies the generic SQL type

LONGVARBINARY

.

---

#### LONGVARBINARY

public static final

JDBCType

LONGVARBINARY

Identifies the generic SQL type

LONGVARBINARY

.

NULL

```java
public static final
JDBCType
NULL
```

Identifies the generic SQL value

NULL

.

---

#### NULL

public static final

JDBCType

NULL

Identifies the generic SQL value

NULL

.

OTHER

```java
public static final
JDBCType
OTHER
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

---

#### OTHER

public static final

JDBCType

OTHER

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

JAVA_OBJECT

```java
public static final
JDBCType
JAVA_OBJECT
```

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

---

#### JAVA_OBJECT

public static final

JDBCType

JAVA_OBJECT

Indicates that the SQL type
is database-specific and gets mapped to a Java object that can be
accessed via the methods getObject and setObject.

DISTINCT

```java
public static final
JDBCType
DISTINCT
```

Identifies the generic SQL type

DISTINCT

.

---

#### DISTINCT

public static final

JDBCType

DISTINCT

Identifies the generic SQL type

DISTINCT

.

STRUCT

```java
public static final
JDBCType
STRUCT
```

Identifies the generic SQL type

STRUCT

.

---

#### STRUCT

public static final

JDBCType

STRUCT

Identifies the generic SQL type

STRUCT

.

ARRAY

```java
public static final
JDBCType
ARRAY
```

Identifies the generic SQL type

ARRAY

.

---

#### ARRAY

public static final

JDBCType

ARRAY

Identifies the generic SQL type

ARRAY

.

BLOB

```java
public static final
JDBCType
BLOB
```

Identifies the generic SQL type

BLOB

.

---

#### BLOB

public static final

JDBCType

BLOB

Identifies the generic SQL type

BLOB

.

CLOB

```java
public static final
JDBCType
CLOB
```

Identifies the generic SQL type

CLOB

.

---

#### CLOB

public static final

JDBCType

CLOB

Identifies the generic SQL type

CLOB

.

REF

```java
public static final
JDBCType
REF
```

Identifies the generic SQL type

REF

.

---

#### REF

public static final

JDBCType

REF

Identifies the generic SQL type

REF

.

DATALINK

```java
public static final
JDBCType
DATALINK
```

Identifies the generic SQL type

DATALINK

.

---

#### DATALINK

public static final

JDBCType

DATALINK

Identifies the generic SQL type

DATALINK

.

BOOLEAN

```java
public static final
JDBCType
BOOLEAN
```

Identifies the generic SQL type

BOOLEAN

.

---

#### BOOLEAN

public static final

JDBCType

BOOLEAN

Identifies the generic SQL type

BOOLEAN

.

ROWID

```java
public static final
JDBCType
ROWID
```

Identifies the SQL type

ROWID

.

---

#### ROWID

public static final

JDBCType

ROWID

Identifies the SQL type

ROWID

.

NCHAR

```java
public static final
JDBCType
NCHAR
```

Identifies the generic SQL type

NCHAR

.

---

#### NCHAR

public static final

JDBCType

NCHAR

Identifies the generic SQL type

NCHAR

.

NVARCHAR

```java
public static final
JDBCType
NVARCHAR
```

Identifies the generic SQL type

NVARCHAR

.

---

#### NVARCHAR

public static final

JDBCType

NVARCHAR

Identifies the generic SQL type

NVARCHAR

.

LONGNVARCHAR

```java
public static final
JDBCType
LONGNVARCHAR
```

Identifies the generic SQL type

LONGNVARCHAR

.

---

#### LONGNVARCHAR

public static final

JDBCType

LONGNVARCHAR

Identifies the generic SQL type

LONGNVARCHAR

.

NCLOB

```java
public static final
JDBCType
NCLOB
```

Identifies the generic SQL type

NCLOB

.

---

#### NCLOB

public static final

JDBCType

NCLOB

Identifies the generic SQL type

NCLOB

.

SQLXML

```java
public static final
JDBCType
SQLXML
```

Identifies the generic SQL type

SQLXML

.

---

#### SQLXML

public static final

JDBCType

SQLXML

Identifies the generic SQL type

SQLXML

.

REF_CURSOR

```java
public static final
JDBCType
REF_CURSOR
```

Identifies the generic SQL type

REF_CURSOR

.

---

#### REF_CURSOR

public static final

JDBCType

REF_CURSOR

Identifies the generic SQL type

REF_CURSOR

.

TIME_WITH_TIMEZONE

```java
public static final
JDBCType
TIME_WITH_TIMEZONE
```

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

---

#### TIME_WITH_TIMEZONE

public static final

JDBCType

TIME_WITH_TIMEZONE

Identifies the generic SQL type

TIME_WITH_TIMEZONE

.

TIMESTAMP_WITH_TIMEZONE

```java
public static final
JDBCType
TIMESTAMP_WITH_TIMEZONE
```

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

---

#### TIMESTAMP_WITH_TIMEZONE

public static final

JDBCType

TIMESTAMP_WITH_TIMEZONE

Identifies the generic SQL type

TIMESTAMP_WITH_TIMEZONE

.

Method Detail

- values

```java
public static
JDBCType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JDBCType c : JDBCType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
JDBCType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

- getName

```java
public
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Specified by:** getName

in interface

SQLType
**Returns:** The name of this

SQLType

.

- getVendor

```java
public
String
getVendor()
```

Returns the name of the vendor that supports this data type.

**Specified by:** getVendor

in interface

SQLType
**Returns:** The name of the vendor for this data type which is
java.sql for JDBCType.

- getVendorTypeNumber

```java
public
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Specified by:** getVendorTypeNumber

in interface

SQLType
**Returns:** An Integer representing the data type. For

JDBCType

,
the value will be the same value as in

Types

for the data type.

- valueOf

```java
public static
JDBCType
valueOf​(int type)
```

Returns the

JDBCType

that corresponds to the specified

Types

value

**Parameters:** type

-

Types

value
**Returns:** The

JDBCType

constant
**Throws:** IllegalArgumentException

- if this enum type has no constant with
the specified

Types

value
**See Also:** Types

---

#### Method Detail

values

```java
public static
JDBCType
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JDBCType c : JDBCType.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

JDBCType

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (JDBCType c : JDBCType.values())
System.out.println(c);
```

for (JDBCType c : JDBCType.values())
System.out.println(c);

valueOf

```java
public static
JDBCType
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

JDBCType

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

getName

```java
public
String
getName()
```

Returns the

SQLType

name that represents a SQL data type.

**Specified by:** getName

in interface

SQLType
**Returns:** The name of this

SQLType

.

---

#### getName

public

String

getName()

Returns the

SQLType

name that represents a SQL data type.

getVendor

```java
public
String
getVendor()
```

Returns the name of the vendor that supports this data type.

**Specified by:** getVendor

in interface

SQLType
**Returns:** The name of the vendor for this data type which is
java.sql for JDBCType.

---

#### getVendor

public

String

getVendor()

Returns the name of the vendor that supports this data type.

getVendorTypeNumber

```java
public
Integer
getVendorTypeNumber()
```

Returns the vendor specific type number for the data type.

**Specified by:** getVendorTypeNumber

in interface

SQLType
**Returns:** An Integer representing the data type. For

JDBCType

,
the value will be the same value as in

Types

for the data type.

---

#### getVendorTypeNumber

public

Integer

getVendorTypeNumber()

Returns the vendor specific type number for the data type.

valueOf

```java
public static
JDBCType
valueOf​(int type)
```

Returns the

JDBCType

that corresponds to the specified

Types

value

**Parameters:** type

-

Types

value
**Returns:** The

JDBCType

constant
**Throws:** IllegalArgumentException

- if this enum type has no constant with
the specified

Types

value
**See Also:** Types

---

#### valueOf

public static

JDBCType

valueOf​(int type)

Returns the

JDBCType

that corresponds to the specified

Types

value

---

