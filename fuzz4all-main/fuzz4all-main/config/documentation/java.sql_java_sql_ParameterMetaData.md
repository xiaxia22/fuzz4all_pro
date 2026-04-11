# Interface ParameterMetaData

**Source:** `java.sql\java\sql\ParameterMetaData.html`

### Class Description

```java
public interface
ParameterMetaData

extends
Wrapper
```

An object that can be used to get information about the types
and properties for each parameter marker in a

PreparedStatement

object. For some queries and driver
implementations, the data that would be returned by a

ParameterMetaData

object may not be available until the

PreparedStatement

has
been executed.

Some driver implementations may not be able to provide information about the
types and properties for each parameter marker in a

CallableStatement

object.

**All Superinterfaces:** Wrapper

---

### Field Details

#### static final int parameterNoNulls

The constant indicating that a
parameter will not allow

NULL

values.

**See Also:**
- Constant Field Values

---

#### static final int parameterNullable

The constant indicating that a
parameter will allow

NULL

values.

**See Also:**
- Constant Field Values

---

#### static final int parameterNullableUnknown

The constant indicating that the
nullability of a parameter is unknown.

**See Also:**
- Constant Field Values

---

#### static final int parameterModeUnknown

The constant indicating that the mode of the parameter is unknown.

**See Also:**
- Constant Field Values

---

#### static final int parameterModeIn

The constant indicating that the parameter's mode is IN.

**See Also:**
- Constant Field Values

---

#### static final int parameterModeInOut

The constant indicating that the parameter's mode is INOUT.

**See Also:**
- Constant Field Values

---

#### static final int parameterModeOut

The constant indicating that the parameter's mode is OUT.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getParameterCount()
throws
SQLException

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

**Returns:**
- the number of parameters

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### int isNullable​(int param)
throws
SQLException

Retrieves whether null values are allowed in the designated parameter.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- the nullability status of the given parameter; one of

ParameterMetaData.parameterNoNulls

,

ParameterMetaData.parameterNullable

, or

ParameterMetaData.parameterNullableUnknown

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### boolean isSigned​(int param)
throws
SQLException

Retrieves whether values for the designated parameter can be signed numbers.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- true

if so;

false

otherwise

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### int getPrecision​(int param)
throws
SQLException

Retrieves the designated parameter's specified column size.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- precision

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### int getScale​(int param)
throws
SQLException

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- scale

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### int getParameterType​(int param)
throws
SQLException

Retrieves the designated parameter's SQL type.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- SQL type from

java.sql.Types

**Throws:**
- SQLException

- if a database access error occurs

**See Also:**
- Types

**Since:**
- 1.4

---

#### String
getParameterTypeName​(int param)
throws
SQLException

Retrieves the designated parameter's database-specific type name.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- type the name used by the database. If the parameter type is
a user-defined type, then a fully-qualified type name is returned.

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### String
getParameterClassName​(int param)
throws
SQLException

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- the fully-qualified name of the class in the Java programming
language that would be used by the method

PreparedStatement.setObject

to set the value
in the specified parameter. This is the class name used
for custom mapping.

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

#### int getParameterMode​(int param)
throws
SQLException

Retrieves the designated parameter's mode.

**Parameters:**
- param

- the first parameter is 1, the second is 2, ...

**Returns:**
- mode of the parameter; one of

ParameterMetaData.parameterModeIn

,

ParameterMetaData.parameterModeOut

, or

ParameterMetaData.parameterModeInOut

ParameterMetaData.parameterModeUnknown

.

**Throws:**
- SQLException

- if a database access error occurs

**Since:**
- 1.4

---

### Additional Sections

#### Interface ParameterMetaData

**All Superinterfaces:** Wrapper

```java
public interface
ParameterMetaData

extends
Wrapper
```

An object that can be used to get information about the types
and properties for each parameter marker in a

PreparedStatement

object. For some queries and driver
implementations, the data that would be returned by a

ParameterMetaData

object may not be available until the

PreparedStatement

has
been executed.

Some driver implementations may not be able to provide information about the
types and properties for each parameter marker in a

CallableStatement

object.

**Since:** 1.4

public interface

ParameterMetaData

extends

Wrapper

An object that can be used to get information about the types
and properties for each parameter marker in a

PreparedStatement

object. For some queries and driver
implementations, the data that would be returned by a

ParameterMetaData

object may not be available until the

PreparedStatement

has
been executed.

Some driver implementations may not be able to provide information about the
types and properties for each parameter marker in a

CallableStatement

object.

Some driver implementations may not be able to provide information about the
types and properties for each parameter marker in a

CallableStatement

object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

parameterModeIn

The constant indicating that the parameter's mode is IN.

static int

parameterModeInOut

The constant indicating that the parameter's mode is INOUT.

static int

parameterModeOut

The constant indicating that the parameter's mode is OUT.

static int

parameterModeUnknown

The constant indicating that the mode of the parameter is unknown.

static int

parameterNoNulls

The constant indicating that a
parameter will not allow

NULL

values.

static int

parameterNullable

The constant indicating that a
parameter will allow

NULL

values.

static int

parameterNullableUnknown

The constant indicating that the
nullability of a parameter is unknown.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getParameterClassName

​(int param)

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

int

getParameterCount

()

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

int

getParameterMode

​(int param)

Retrieves the designated parameter's mode.

int

getParameterType

​(int param)

Retrieves the designated parameter's SQL type.

String

getParameterTypeName

​(int param)

Retrieves the designated parameter's database-specific type name.

int

getPrecision

​(int param)

Retrieves the designated parameter's specified column size.

int

getScale

​(int param)

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

int

isNullable

​(int param)

Retrieves whether null values are allowed in the designated parameter.

boolean

isSigned

​(int param)

Retrieves whether values for the designated parameter can be signed numbers.

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

parameterModeIn

The constant indicating that the parameter's mode is IN.

static int

parameterModeInOut

The constant indicating that the parameter's mode is INOUT.

static int

parameterModeOut

The constant indicating that the parameter's mode is OUT.

static int

parameterModeUnknown

The constant indicating that the mode of the parameter is unknown.

static int

parameterNoNulls

The constant indicating that a
parameter will not allow

NULL

values.

static int

parameterNullable

The constant indicating that a
parameter will allow

NULL

values.

static int

parameterNullableUnknown

The constant indicating that the
nullability of a parameter is unknown.

---

#### Field Summary

The constant indicating that the parameter's mode is IN.

The constant indicating that the parameter's mode is INOUT.

The constant indicating that the parameter's mode is OUT.

The constant indicating that the mode of the parameter is unknown.

The constant indicating that a
parameter will not allow

NULL

values.

The constant indicating that a
parameter will allow

NULL

values.

The constant indicating that the
nullability of a parameter is unknown.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getParameterClassName

​(int param)

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

int

getParameterCount

()

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

int

getParameterMode

​(int param)

Retrieves the designated parameter's mode.

int

getParameterType

​(int param)

Retrieves the designated parameter's SQL type.

String

getParameterTypeName

​(int param)

Retrieves the designated parameter's database-specific type name.

int

getPrecision

​(int param)

Retrieves the designated parameter's specified column size.

int

getScale

​(int param)

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

int

isNullable

​(int param)

Retrieves whether null values are allowed in the designated parameter.

boolean

isSigned

​(int param)

Retrieves whether values for the designated parameter can be signed numbers.

- Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Method Summary

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

Retrieves the designated parameter's mode.

Retrieves the designated parameter's SQL type.

Retrieves the designated parameter's database-specific type name.

Retrieves the designated parameter's specified column size.

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

Retrieves whether null values are allowed in the designated parameter.

Retrieves whether values for the designated parameter can be signed numbers.

Methods declared in interface java.sql.

Wrapper

isWrapperFor

,

unwrap

---

#### Methods declared in interface java.sql. Wrapper

============ FIELD DETAIL ===========

- Field Detail

- parameterNoNulls

```java
static final int parameterNoNulls
```

The constant indicating that a
parameter will not allow

NULL

values.

**See Also:** Constant Field Values

- parameterNullable

```java
static final int parameterNullable
```

The constant indicating that a
parameter will allow

NULL

values.

**See Also:** Constant Field Values

- parameterNullableUnknown

```java
static final int parameterNullableUnknown
```

The constant indicating that the
nullability of a parameter is unknown.

**See Also:** Constant Field Values

- parameterModeUnknown

```java
static final int parameterModeUnknown
```

The constant indicating that the mode of the parameter is unknown.

**See Also:** Constant Field Values

- parameterModeIn

```java
static final int parameterModeIn
```

The constant indicating that the parameter's mode is IN.

**See Also:** Constant Field Values

- parameterModeInOut

```java
static final int parameterModeInOut
```

The constant indicating that the parameter's mode is INOUT.

**See Also:** Constant Field Values

- parameterModeOut

```java
static final int parameterModeOut
```

The constant indicating that the parameter's mode is OUT.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getParameterCount

```java
int getParameterCount()
throws
SQLException
```

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

**Returns:** the number of parameters
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- isNullable

```java
int isNullable​(int param)
throws
SQLException
```

Retrieves whether null values are allowed in the designated parameter.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the nullability status of the given parameter; one of

ParameterMetaData.parameterNoNulls

,

ParameterMetaData.parameterNullable

, or

ParameterMetaData.parameterNullableUnknown
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- isSigned

```java
boolean isSigned​(int param)
throws
SQLException
```

Retrieves whether values for the designated parameter can be signed numbers.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getPrecision

```java
int getPrecision​(int param)
throws
SQLException
```

Retrieves the designated parameter's specified column size.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getScale

```java
int getScale​(int param)
throws
SQLException
```

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterType

```java
int getParameterType​(int param)
throws
SQLException
```

Retrieves the designated parameter's SQL type.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** SQL type from

java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** Types

- getParameterTypeName

```java
String
getParameterTypeName​(int param)
throws
SQLException
```

Retrieves the designated parameter's database-specific type name.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** type the name used by the database. If the parameter type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterClassName

```java
String
getParameterClassName​(int param)
throws
SQLException
```

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

PreparedStatement.setObject

to set the value
in the specified parameter. This is the class name used
for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterMode

```java
int getParameterMode​(int param)
throws
SQLException
```

Retrieves the designated parameter's mode.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** mode of the parameter; one of

ParameterMetaData.parameterModeIn

,

ParameterMetaData.parameterModeOut

, or

ParameterMetaData.parameterModeInOut

ParameterMetaData.parameterModeUnknown

.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

Field Detail

- parameterNoNulls

```java
static final int parameterNoNulls
```

The constant indicating that a
parameter will not allow

NULL

values.

**See Also:** Constant Field Values

- parameterNullable

```java
static final int parameterNullable
```

The constant indicating that a
parameter will allow

NULL

values.

**See Also:** Constant Field Values

- parameterNullableUnknown

```java
static final int parameterNullableUnknown
```

The constant indicating that the
nullability of a parameter is unknown.

**See Also:** Constant Field Values

- parameterModeUnknown

```java
static final int parameterModeUnknown
```

The constant indicating that the mode of the parameter is unknown.

**See Also:** Constant Field Values

- parameterModeIn

```java
static final int parameterModeIn
```

The constant indicating that the parameter's mode is IN.

**See Also:** Constant Field Values

- parameterModeInOut

```java
static final int parameterModeInOut
```

The constant indicating that the parameter's mode is INOUT.

**See Also:** Constant Field Values

- parameterModeOut

```java
static final int parameterModeOut
```

The constant indicating that the parameter's mode is OUT.

**See Also:** Constant Field Values

---

#### Field Detail

parameterNoNulls

```java
static final int parameterNoNulls
```

The constant indicating that a
parameter will not allow

NULL

values.

**See Also:** Constant Field Values

---

#### parameterNoNulls

static final int parameterNoNulls

The constant indicating that a
parameter will not allow

NULL

values.

parameterNullable

```java
static final int parameterNullable
```

The constant indicating that a
parameter will allow

NULL

values.

**See Also:** Constant Field Values

---

#### parameterNullable

static final int parameterNullable

The constant indicating that a
parameter will allow

NULL

values.

parameterNullableUnknown

```java
static final int parameterNullableUnknown
```

The constant indicating that the
nullability of a parameter is unknown.

**See Also:** Constant Field Values

---

#### parameterNullableUnknown

static final int parameterNullableUnknown

The constant indicating that the
nullability of a parameter is unknown.

parameterModeUnknown

```java
static final int parameterModeUnknown
```

The constant indicating that the mode of the parameter is unknown.

**See Also:** Constant Field Values

---

#### parameterModeUnknown

static final int parameterModeUnknown

The constant indicating that the mode of the parameter is unknown.

parameterModeIn

```java
static final int parameterModeIn
```

The constant indicating that the parameter's mode is IN.

**See Also:** Constant Field Values

---

#### parameterModeIn

static final int parameterModeIn

The constant indicating that the parameter's mode is IN.

parameterModeInOut

```java
static final int parameterModeInOut
```

The constant indicating that the parameter's mode is INOUT.

**See Also:** Constant Field Values

---

#### parameterModeInOut

static final int parameterModeInOut

The constant indicating that the parameter's mode is INOUT.

parameterModeOut

```java
static final int parameterModeOut
```

The constant indicating that the parameter's mode is OUT.

**See Also:** Constant Field Values

---

#### parameterModeOut

static final int parameterModeOut

The constant indicating that the parameter's mode is OUT.

Method Detail

- getParameterCount

```java
int getParameterCount()
throws
SQLException
```

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

**Returns:** the number of parameters
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- isNullable

```java
int isNullable​(int param)
throws
SQLException
```

Retrieves whether null values are allowed in the designated parameter.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the nullability status of the given parameter; one of

ParameterMetaData.parameterNoNulls

,

ParameterMetaData.parameterNullable

, or

ParameterMetaData.parameterNullableUnknown
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- isSigned

```java
boolean isSigned​(int param)
throws
SQLException
```

Retrieves whether values for the designated parameter can be signed numbers.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getPrecision

```java
int getPrecision​(int param)
throws
SQLException
```

Retrieves the designated parameter's specified column size.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getScale

```java
int getScale​(int param)
throws
SQLException
```

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterType

```java
int getParameterType​(int param)
throws
SQLException
```

Retrieves the designated parameter's SQL type.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** SQL type from

java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** Types

- getParameterTypeName

```java
String
getParameterTypeName​(int param)
throws
SQLException
```

Retrieves the designated parameter's database-specific type name.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** type the name used by the database. If the parameter type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterClassName

```java
String
getParameterClassName​(int param)
throws
SQLException
```

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

PreparedStatement.setObject

to set the value
in the specified parameter. This is the class name used
for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

- getParameterMode

```java
int getParameterMode​(int param)
throws
SQLException
```

Retrieves the designated parameter's mode.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** mode of the parameter; one of

ParameterMetaData.parameterModeIn

,

ParameterMetaData.parameterModeOut

, or

ParameterMetaData.parameterModeInOut

ParameterMetaData.parameterModeUnknown

.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### Method Detail

getParameterCount

```java
int getParameterCount()
throws
SQLException
```

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

**Returns:** the number of parameters
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getParameterCount

int getParameterCount()
throws

SQLException

Retrieves the number of parameters in the

PreparedStatement

object for which this

ParameterMetaData

object contains
information.

isNullable

```java
int isNullable​(int param)
throws
SQLException
```

Retrieves whether null values are allowed in the designated parameter.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the nullability status of the given parameter; one of

ParameterMetaData.parameterNoNulls

,

ParameterMetaData.parameterNullable

, or

ParameterMetaData.parameterNullableUnknown
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### isNullable

int isNullable​(int param)
throws

SQLException

Retrieves whether null values are allowed in the designated parameter.

isSigned

```java
boolean isSigned​(int param)
throws
SQLException
```

Retrieves whether values for the designated parameter can be signed numbers.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** true

if so;

false

otherwise
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### isSigned

boolean isSigned​(int param)
throws

SQLException

Retrieves whether values for the designated parameter can be signed numbers.

getPrecision

```java
int getPrecision​(int param)
throws
SQLException
```

Retrieves the designated parameter's specified column size.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** precision
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getPrecision

int getPrecision​(int param)
throws

SQLException

Retrieves the designated parameter's specified column size.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

The returned value represents the maximum column size for the given parameter.
For numeric data, this is the maximum precision. For character data, this is the length in characters.
For datetime datatypes, this is the length in characters of the String representation (assuming the
maximum allowed precision of the fractional seconds component). For binary data, this is the length in bytes. For the ROWID datatype,
this is the length in bytes. 0 is returned for data types where the
column size is not applicable.

getScale

```java
int getScale​(int param)
throws
SQLException
```

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** scale
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getScale

int getScale​(int param)
throws

SQLException

Retrieves the designated parameter's number of digits to right of the decimal point.
0 is returned for data types where the scale is not applicable.

getParameterType

```java
int getParameterType​(int param)
throws
SQLException
```

Retrieves the designated parameter's SQL type.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** SQL type from

java.sql.Types
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4
**See Also:** Types

---

#### getParameterType

int getParameterType​(int param)
throws

SQLException

Retrieves the designated parameter's SQL type.

getParameterTypeName

```java
String
getParameterTypeName​(int param)
throws
SQLException
```

Retrieves the designated parameter's database-specific type name.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** type the name used by the database. If the parameter type is
a user-defined type, then a fully-qualified type name is returned.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getParameterTypeName

String

getParameterTypeName​(int param)
throws

SQLException

Retrieves the designated parameter's database-specific type name.

getParameterClassName

```java
String
getParameterClassName​(int param)
throws
SQLException
```

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** the fully-qualified name of the class in the Java programming
language that would be used by the method

PreparedStatement.setObject

to set the value
in the specified parameter. This is the class name used
for custom mapping.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getParameterClassName

String

getParameterClassName​(int param)
throws

SQLException

Retrieves the fully-qualified name of the Java class whose instances
should be passed to the method

PreparedStatement.setObject

.

getParameterMode

```java
int getParameterMode​(int param)
throws
SQLException
```

Retrieves the designated parameter's mode.

**Parameters:** param

- the first parameter is 1, the second is 2, ...
**Returns:** mode of the parameter; one of

ParameterMetaData.parameterModeIn

,

ParameterMetaData.parameterModeOut

, or

ParameterMetaData.parameterModeInOut

ParameterMetaData.parameterModeUnknown

.
**Throws:** SQLException

- if a database access error occurs
**Since:** 1.4

---

#### getParameterMode

int getParameterMode​(int param)
throws

SQLException

Retrieves the designated parameter's mode.

---

