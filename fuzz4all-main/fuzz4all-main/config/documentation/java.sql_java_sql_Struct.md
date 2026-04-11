# Interface Struct

**Source:** `java.sql\java\sql\Struct.html`

### Class Description

```java
public interface
Struct
```

The standard mapping in the Java programming language for an SQL
structured type. A

Struct

object contains a
value for each attribute of the SQL structured type that
it represents.
By default, an instance of

Struct

is valid as long as the
application has a reference to it.

All methods on the

Struct

interface must be fully implemented if the
JDBC driver supports the data type.

**All Known Implementing Classes:** SerialStruct

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getSQLTypeName()
throws
SQLException

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

**Returns:**
- the fully-qualified type name of the SQL structured
type for which this

Struct

object
is the generic representation

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
[] getAttributes()
throws
SQLException

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the type map
associated with the
connection for customizations of the type mappings.
If there is no
entry in the connection's type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Returns:**
- an array containing the ordered attribute values

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
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the given type map
for customizations of the type mappings.
If there is no
entry in the given type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping. This method never
uses the type map associated with the connection.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Parameters:**
- map

- a mapping of SQL type names to Java classes

**Returns:**
- an array containing the ordered attribute values

**Throws:**
- SQLException

- if a database access error occurs
- SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method

**Since:**
- 1.2

---

### Additional Sections

#### Interface Struct

**All Known Implementing Classes:** SerialStruct

```java
public interface
Struct
```

The standard mapping in the Java programming language for an SQL
structured type. A

Struct

object contains a
value for each attribute of the SQL structured type that
it represents.
By default, an instance of

Struct

is valid as long as the
application has a reference to it.

All methods on the

Struct

interface must be fully implemented if the
JDBC driver supports the data type.

**Since:** 1.2

public interface

Struct

The standard mapping in the Java programming language for an SQL
structured type. A

Struct

object contains a
value for each attribute of the SQL structured type that
it represents.
By default, an instance of

Struct

is valid as long as the
application has a reference to it.

All methods on the

Struct

interface must be fully implemented if the
JDBC driver supports the data type.

All methods on the

Struct

interface must be fully implemented if the
JDBC driver supports the data type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

[]

getAttributes

()

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.

Object

[]

getAttributes

​(

Map

<

String

,​

Class

<?>> map)

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.

String

getSQLTypeName

()

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

[]

getAttributes

()

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.

Object

[]

getAttributes

​(

Map

<

String

,​

Class

<?>> map)

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.

String

getSQLTypeName

()

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

---

#### Method Summary

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

============ METHOD DETAIL ==========

- Method Detail

- getSQLTypeName

```java
String
getSQLTypeName()
throws
SQLException
```

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

**Returns:** the fully-qualified type name of the SQL structured
type for which this

Struct

object
is the generic representation
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getAttributes

```java
Object
[] getAttributes()
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the type map
associated with the
connection for customizations of the type mappings.
If there is no
entry in the connection's type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getAttributes

```java
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the given type map
for customizations of the type mappings.
If there is no
entry in the given type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping. This method never
uses the type map associated with the connection.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Parameters:** map

- a mapping of SQL type names to Java classes
**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

Method Detail

- getSQLTypeName

```java
String
getSQLTypeName()
throws
SQLException
```

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

**Returns:** the fully-qualified type name of the SQL structured
type for which this

Struct

object
is the generic representation
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getAttributes

```java
Object
[] getAttributes()
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the type map
associated with the
connection for customizations of the type mappings.
If there is no
entry in the connection's type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

- getAttributes

```java
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the given type map
for customizations of the type mappings.
If there is no
entry in the given type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping. This method never
uses the type map associated with the connection.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Parameters:** map

- a mapping of SQL type names to Java classes
**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### Method Detail

getSQLTypeName

```java
String
getSQLTypeName()
throws
SQLException
```

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

**Returns:** the fully-qualified type name of the SQL structured
type for which this

Struct

object
is the generic representation
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getSQLTypeName

String

getSQLTypeName()
throws

SQLException

Retrieves the SQL type name of the SQL structured type
that this

Struct

object represents.

getAttributes

```java
Object
[] getAttributes()
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the type map
associated with the
connection for customizations of the type mappings.
If there is no
entry in the connection's type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getAttributes

Object

[] getAttributes()
throws

SQLException

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the type map
associated with the
connection for customizations of the type mappings.
If there is no
entry in the connection's type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

getAttributes

```java
Object
[] getAttributes​(
Map
<
String
,​
Class
<?>> map)
throws
SQLException
```

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the given type map
for customizations of the type mappings.
If there is no
entry in the given type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping. This method never
uses the type map associated with the connection.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

**Parameters:** map

- a mapping of SQL type names to Java classes
**Returns:** an array containing the ordered attribute values
**Throws:** SQLException

- if a database access error occurs
**Throws:** SQLFeatureNotSupportedException

- if the JDBC driver does not support
this method
**Since:** 1.2

---

#### getAttributes

Object

[] getAttributes​(

Map

<

String

,​

Class

<?>> map)
throws

SQLException

Produces the ordered values of the attributes of the SQL
structured type that this

Struct

object represents.
As individual attributes are processed, this method uses the given type map
for customizations of the type mappings.
If there is no
entry in the given type map that matches the structured
type that an attribute represents,
the driver uses the standard mapping. This method never
uses the type map associated with the connection.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

Conceptually, this method calls the method

getObject

on each attribute
of the structured type and returns a Java array containing
the result.

---

