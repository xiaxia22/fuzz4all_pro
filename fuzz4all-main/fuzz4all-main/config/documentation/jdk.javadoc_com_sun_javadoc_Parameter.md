# Interface Parameter

**Source:** `jdk.javadoc\com\sun\javadoc\Parameter.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Parameter
```

Parameter information.
This includes a parameter type and parameter name.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
type()

Get the type of this parameter.

**Returns:**
- the type of this parameter.

---

#### String
name()

Get local name of this parameter.
For example if parameter is the short 'index', returns "index".

**Returns:**
- the name of this parameter as a string.

---

#### String
typeName()

Get type name of this parameter.
For example if parameter is the short 'index', returns "short".

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

**Returns:**
- a complete string representation of the type.

---

#### String
toString()

Returns a string representation of the parameter.

For example if parameter is the short 'index', returns "short index".

**Overrides:**
- toString

in class

Object

**Returns:**
- type and parameter name of this parameter.

---

#### AnnotationDesc
[] annotations()

Get the annotations of this parameter.
Return an empty array if there are none.

**Returns:**
- the annotations of this parameter.

**Since:**
- 1.5

---

### Additional Sections

#### Interface Parameter

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Parameter
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Parameter information.
This includes a parameter type and parameter name.

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Parameter

Parameter information.
This includes a parameter type and parameter name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get local name of this parameter.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the parameter.

Type

type

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the type of this parameter.

String

typeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get type name of this parameter.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotationDesc

[]

annotations

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.

String

name

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get local name of this parameter.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the parameter.

Type

type

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get the type of this parameter.

String

typeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Get type name of this parameter.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.

Get local name of this parameter.

Returns a string representation of the parameter.

Get the type of this parameter.

Get type name of this parameter.

============ METHOD DETAIL ==========

- Method Detail

- type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the type of this parameter.

**Returns:** the type of this parameter.

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get local name of this parameter.
For example if parameter is the short 'index', returns "index".

**Returns:** the name of this parameter as a string.

- typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type name of this parameter.
For example if parameter is the short 'index', returns "short".

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

**Returns:** a complete string representation of the type.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the parameter.

For example if parameter is the short 'index', returns "short index".

**Overrides:** toString

in class

Object
**Returns:** type and parameter name of this parameter.

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.
Return an empty array if there are none.

**Returns:** the annotations of this parameter.
**Since:** 1.5

Method Detail

- type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the type of this parameter.

**Returns:** the type of this parameter.

- name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get local name of this parameter.
For example if parameter is the short 'index', returns "index".

**Returns:** the name of this parameter as a string.

- typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type name of this parameter.
For example if parameter is the short 'index', returns "short".

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

**Returns:** a complete string representation of the type.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the parameter.

For example if parameter is the short 'index', returns "short index".

**Overrides:** toString

in class

Object
**Returns:** type and parameter name of this parameter.

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.
Return an empty array if there are none.

**Returns:** the annotations of this parameter.
**Since:** 1.5

---

#### Method Detail

type

```java
Type
type()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the type of this parameter.

**Returns:** the type of this parameter.

---

#### type

Type

type()

Get the type of this parameter.

name

```java
String
name()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get local name of this parameter.
For example if parameter is the short 'index', returns "index".

**Returns:** the name of this parameter as a string.

---

#### name

String

name()

Get local name of this parameter.
For example if parameter is the short 'index', returns "index".

typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get type name of this parameter.
For example if parameter is the short 'index', returns "short".

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

**Returns:** a complete string representation of the type.

---

#### typeName

String

typeName()

Get type name of this parameter.
For example if parameter is the short 'index', returns "short".

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

This method returns a complete string
representation of the type, including the dimensions of arrays and
the type arguments of parameterized types. Names are qualified.

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns a string representation of the parameter.

For example if parameter is the short 'index', returns "short index".

**Overrides:** toString

in class

Object
**Returns:** type and parameter name of this parameter.

---

#### toString

String

toString()

Returns a string representation of the parameter.

For example if parameter is the short 'index', returns "short index".

For example if parameter is the short 'index', returns "short index".

annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this parameter.
Return an empty array if there are none.

**Returns:** the annotations of this parameter.
**Since:** 1.5

---

#### annotations

AnnotationDesc

[] annotations()

Get the annotations of this parameter.
Return an empty array if there are none.

---

