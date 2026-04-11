# Interface Type

**Source:** `java.base\java\lang\reflect\Type.html`

### Class Description

```java
public interface
Type
```

Type is the common superinterface for all types in the Java
programming language. These include raw types, parameterized types,
array types, type variables and primitive types.

**All Known Subinterfaces:** GenericArrayType

,

ParameterizedType

,

TypeVariable

<D>

,

WildcardType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default
String
getTypeName()

Returns a string describing this type, including information
about any type parameters.

**Returns:**
- a string describing this type

**Since:**
- 1.8

**Implementation Requirements:**
- The default implementation calls

toString

.

---

### Additional Sections

#### Interface Type

**All Known Subinterfaces:** GenericArrayType

,

ParameterizedType

,

TypeVariable

<D>

,

WildcardType

**All Known Implementing Classes:** Class

```java
public interface
Type
```

Type is the common superinterface for all types in the Java
programming language. These include raw types, parameterized types,
array types, type variables and primitive types.

**Since:** 1.5

public interface

Type

Type is the common superinterface for all types in the Java
programming language. These include raw types, parameterized types,
array types, type variables and primitive types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

String

getTypeName

()

Returns a string describing this type, including information
about any type parameters.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

String

getTypeName

()

Returns a string describing this type, including information
about any type parameters.

---

#### Method Summary

Returns a string describing this type, including information
about any type parameters.

============ METHOD DETAIL ==========

- Method Detail

- getTypeName

```java
default
String
getTypeName()
```

Returns a string describing this type, including information
about any type parameters.

**Implementation Requirements:** The default implementation calls

toString

.
**Returns:** a string describing this type
**Since:** 1.8

Method Detail

- getTypeName

```java
default
String
getTypeName()
```

Returns a string describing this type, including information
about any type parameters.

**Implementation Requirements:** The default implementation calls

toString

.
**Returns:** a string describing this type
**Since:** 1.8

---

#### Method Detail

getTypeName

```java
default
String
getTypeName()
```

Returns a string describing this type, including information
about any type parameters.

**Implementation Requirements:** The default implementation calls

toString

.
**Returns:** a string describing this type
**Since:** 1.8

---

#### getTypeName

default

String

getTypeName()

Returns a string describing this type, including information
about any type parameters.

---

