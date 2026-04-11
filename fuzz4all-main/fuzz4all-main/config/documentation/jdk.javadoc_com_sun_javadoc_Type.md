# Interface Type

**Source:** `jdk.javadoc\com\sun\javadoc\Type.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Type
```

Represents a type. A type can be a class or interface, an
invocation (like

List<String>

) of a generic class or interface,
a type variable, a wildcard type ("

?

"),
or a primitive data type (like

char

).

**All Known Subinterfaces:** AnnotatedType

,

AnnotationTypeDoc

,

ClassDoc

,

ParameterizedType

,

TypeVariable

,

WildcardType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
typeName()

Return unqualified name of type excluding any dimension information.

For example, a two dimensional array of String returns
"

String

".

**Returns:**
- unqualified name of type excluding any dimension information.

---

#### String
qualifiedTypeName()

Return qualified name of type excluding any dimension information.

For example, a two dimensional array of String
returns "

java.lang.String

".

**Returns:**
- qualified name of this type excluding any dimension information.

---

#### String
simpleTypeName()

Return the simple name of this type excluding any dimension information.
This is the unqualified name of the type, except that for nested types
only the identifier of the innermost type is included.

For example, the class

Outer.Inner

returns
"

Inner

".

**Returns:**
- the simple name of this type excluding any dimension information.

**Since:**
- 1.5

---

#### String
dimension()

Return the type's dimension information, as a string.

For example, a two dimensional array of String returns
"

[][]

".

**Returns:**
- the type's dimension information as a string.

---

#### String
toString()

Return a string representation of the type.
This includes any dimension information and type arguments.

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the type.

---

#### boolean isPrimitive()

Return true if this type represents a primitive type.

**Returns:**
- true if this type represents a primitive type.

**Since:**
- 1.5

---

#### ClassDoc
asClassDoc()

Return this type as a

ClassDoc

if it represents a class
or interface. Array dimensions are ignored.
If this type is a

ParameterizedType

,

TypeVariable

, or

WildcardType

, return
the

ClassDoc

of the type's erasure. If this is an

AnnotationTypeDoc

, return this as a

ClassDoc

(but see

asAnnotationTypeDoc()

).
If this is a primitive type, return null.

**Returns:**
- the

ClassDoc

of this type,
or null if it is a primitive type.

---

#### ParameterizedType
asParameterizedType()

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface. Array dimensions
are ignored.

**Returns:**
- a

ParameterizedType

if the type is an
invocation of a generic type, or null if it is not.

**Since:**
- 1.5

---

#### TypeVariable
asTypeVariable()

Return this type as a

TypeVariable

if it represents
a type variable. Array dimensions are ignored.

**Returns:**
- a

TypeVariable

if the type is a type variable,
or null if it is not.

**Since:**
- 1.5

---

#### WildcardType
asWildcardType()

Return this type as a

WildcardType

if it represents
a wildcard type.

**Returns:**
- a

WildcardType

if the type is a wildcard type,
or null if it is not.

**Since:**
- 1.5

---

#### AnnotatedType
asAnnotatedType()

Returns this type as a

AnnotatedType

if it represents
an annotated type.

**Returns:**
- a

AnnotatedType

if the type if an annotated type,
or null if it is not

**Since:**
- 1.8

---

#### AnnotationTypeDoc
asAnnotationTypeDoc()

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type. Array dimensions are ignored.

**Returns:**
- an

AnnotationTypeDoc

if the type is an annotation
type, or null if it is not.

**Since:**
- 1.5

---

#### Type
getElementType()

If this type is an array type, return the element type of the
array. Otherwise, return null.

**Returns:**
- a

Type

representing the element type or null.

**Since:**
- 1.8

---

### Additional Sections

#### Interface Type

**All Known Subinterfaces:** AnnotatedType

,

AnnotationTypeDoc

,

ClassDoc

,

ParameterizedType

,

TypeVariable

,

WildcardType

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
Type
```

Deprecated, for removal: This API element is subject to removal in a future version.

The declarations in this package have been superseded by those
in the package

jdk.javadoc.doclet

.
For more information, see the

Migration Guide

in the documentation for that package.

Represents a type. A type can be a class or interface, an
invocation (like

List<String>

) of a generic class or interface,
a type variable, a wildcard type ("

?

"),
or a primitive data type (like

char

).

**Since:** 1.2

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

Type

Represents a type. A type can be a class or interface, an
invocation (like

List<String>

) of a generic class or interface,
a type variable, a wildcard type ("

?

"),
or a primitive data type (like

char

).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotatedType

asAnnotatedType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

AnnotationTypeDoc

asAnnotationTypeDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type.

ClassDoc

asClassDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ClassDoc

if it represents a class
or interface.

ParameterizedType

asParameterizedType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface.

TypeVariable

asTypeVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

TypeVariable

if it represents
a type variable.

WildcardType

asWildcardType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

WildcardType

if it represents
a wildcard type.

String

dimension

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type's dimension information, as a string.

Type

getElementType

()

Deprecated, for removal: This API element is subject to removal in a future version.

If this type is an array type, return the element type of the
array.

boolean

isPrimitive

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this type represents a primitive type.

String

qualifiedTypeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return qualified name of type excluding any dimension information.

String

simpleTypeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the simple name of this type excluding any dimension information.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return a string representation of the type.

String

typeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return unqualified name of type excluding any dimension information.

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

AnnotatedType

asAnnotatedType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

AnnotationTypeDoc

asAnnotationTypeDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type.

ClassDoc

asClassDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ClassDoc

if it represents a class
or interface.

ParameterizedType

asParameterizedType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface.

TypeVariable

asTypeVariable

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

TypeVariable

if it represents
a type variable.

WildcardType

asWildcardType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

WildcardType

if it represents
a wildcard type.

String

dimension

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type's dimension information, as a string.

Type

getElementType

()

Deprecated, for removal: This API element is subject to removal in a future version.

If this type is an array type, return the element type of the
array.

boolean

isPrimitive

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this type represents a primitive type.

String

qualifiedTypeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return qualified name of type excluding any dimension information.

String

simpleTypeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the simple name of this type excluding any dimension information.

String

toString

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return a string representation of the type.

String

typeName

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return unqualified name of type excluding any dimension information.

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type.

Return this type as a

ClassDoc

if it represents a class
or interface.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface.

Return this type as a

TypeVariable

if it represents
a type variable.

Return this type as a

WildcardType

if it represents
a wildcard type.

Return the type's dimension information, as a string.

If this type is an array type, return the element type of the
array.

Return true if this type represents a primitive type.

Return qualified name of type excluding any dimension information.

Return the simple name of this type excluding any dimension information.

Return a string representation of the type.

Return unqualified name of type excluding any dimension information.

============ METHOD DETAIL ==========

- Method Detail

- typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return unqualified name of type excluding any dimension information.

For example, a two dimensional array of String returns
"

String

".

**Returns:** unqualified name of type excluding any dimension information.

- qualifiedTypeName

```java
String
qualifiedTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return qualified name of type excluding any dimension information.

For example, a two dimensional array of String
returns "

java.lang.String

".

**Returns:** qualified name of this type excluding any dimension information.

- simpleTypeName

```java
String
simpleTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the simple name of this type excluding any dimension information.
This is the unqualified name of the type, except that for nested types
only the identifier of the innermost type is included.

For example, the class

Outer.Inner

returns
"

Inner

".

**Returns:** the simple name of this type excluding any dimension information.
**Since:** 1.5

- dimension

```java
String
dimension()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type's dimension information, as a string.

For example, a two dimensional array of String returns
"

[][]

".

**Returns:** the type's dimension information as a string.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a string representation of the type.
This includes any dimension information and type arguments.

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the type.

- isPrimitive

```java
boolean isPrimitive()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this type represents a primitive type.

**Returns:** true if this type represents a primitive type.
**Since:** 1.5

- asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ClassDoc

if it represents a class
or interface. Array dimensions are ignored.
If this type is a

ParameterizedType

,

TypeVariable

, or

WildcardType

, return
the

ClassDoc

of the type's erasure. If this is an

AnnotationTypeDoc

, return this as a

ClassDoc

(but see

asAnnotationTypeDoc()

).
If this is a primitive type, return null.

**Returns:** the

ClassDoc

of this type,
or null if it is a primitive type.

- asParameterizedType

```java
ParameterizedType
asParameterizedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface. Array dimensions
are ignored.

**Returns:** a

ParameterizedType

if the type is an
invocation of a generic type, or null if it is not.
**Since:** 1.5

- asTypeVariable

```java
TypeVariable
asTypeVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

TypeVariable

if it represents
a type variable. Array dimensions are ignored.

**Returns:** a

TypeVariable

if the type is a type variable,
or null if it is not.
**Since:** 1.5

- asWildcardType

```java
WildcardType
asWildcardType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

WildcardType

if it represents
a wildcard type.

**Returns:** a

WildcardType

if the type is a wildcard type,
or null if it is not.
**Since:** 1.5

- asAnnotatedType

```java
AnnotatedType
asAnnotatedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

**Returns:** a

AnnotatedType

if the type if an annotated type,
or null if it is not
**Since:** 1.8

- asAnnotationTypeDoc

```java
AnnotationTypeDoc
asAnnotationTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type. Array dimensions are ignored.

**Returns:** an

AnnotationTypeDoc

if the type is an annotation
type, or null if it is not.
**Since:** 1.5

- getElementType

```java
Type
getElementType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

If this type is an array type, return the element type of the
array. Otherwise, return null.

**Returns:** a

Type

representing the element type or null.
**Since:** 1.8

Method Detail

- typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return unqualified name of type excluding any dimension information.

For example, a two dimensional array of String returns
"

String

".

**Returns:** unqualified name of type excluding any dimension information.

- qualifiedTypeName

```java
String
qualifiedTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return qualified name of type excluding any dimension information.

For example, a two dimensional array of String
returns "

java.lang.String

".

**Returns:** qualified name of this type excluding any dimension information.

- simpleTypeName

```java
String
simpleTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the simple name of this type excluding any dimension information.
This is the unqualified name of the type, except that for nested types
only the identifier of the innermost type is included.

For example, the class

Outer.Inner

returns
"

Inner

".

**Returns:** the simple name of this type excluding any dimension information.
**Since:** 1.5

- dimension

```java
String
dimension()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type's dimension information, as a string.

For example, a two dimensional array of String returns
"

[][]

".

**Returns:** the type's dimension information as a string.

- toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a string representation of the type.
This includes any dimension information and type arguments.

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the type.

- isPrimitive

```java
boolean isPrimitive()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this type represents a primitive type.

**Returns:** true if this type represents a primitive type.
**Since:** 1.5

- asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ClassDoc

if it represents a class
or interface. Array dimensions are ignored.
If this type is a

ParameterizedType

,

TypeVariable

, or

WildcardType

, return
the

ClassDoc

of the type's erasure. If this is an

AnnotationTypeDoc

, return this as a

ClassDoc

(but see

asAnnotationTypeDoc()

).
If this is a primitive type, return null.

**Returns:** the

ClassDoc

of this type,
or null if it is a primitive type.

- asParameterizedType

```java
ParameterizedType
asParameterizedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface. Array dimensions
are ignored.

**Returns:** a

ParameterizedType

if the type is an
invocation of a generic type, or null if it is not.
**Since:** 1.5

- asTypeVariable

```java
TypeVariable
asTypeVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

TypeVariable

if it represents
a type variable. Array dimensions are ignored.

**Returns:** a

TypeVariable

if the type is a type variable,
or null if it is not.
**Since:** 1.5

- asWildcardType

```java
WildcardType
asWildcardType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

WildcardType

if it represents
a wildcard type.

**Returns:** a

WildcardType

if the type is a wildcard type,
or null if it is not.
**Since:** 1.5

- asAnnotatedType

```java
AnnotatedType
asAnnotatedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

**Returns:** a

AnnotatedType

if the type if an annotated type,
or null if it is not
**Since:** 1.8

- asAnnotationTypeDoc

```java
AnnotationTypeDoc
asAnnotationTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type. Array dimensions are ignored.

**Returns:** an

AnnotationTypeDoc

if the type is an annotation
type, or null if it is not.
**Since:** 1.5

- getElementType

```java
Type
getElementType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

If this type is an array type, return the element type of the
array. Otherwise, return null.

**Returns:** a

Type

representing the element type or null.
**Since:** 1.8

---

#### Method Detail

typeName

```java
String
typeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return unqualified name of type excluding any dimension information.

For example, a two dimensional array of String returns
"

String

".

**Returns:** unqualified name of type excluding any dimension information.

---

#### typeName

String

typeName()

Return unqualified name of type excluding any dimension information.

For example, a two dimensional array of String returns
"

String

".

For example, a two dimensional array of String returns
"

String

".

qualifiedTypeName

```java
String
qualifiedTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return qualified name of type excluding any dimension information.

For example, a two dimensional array of String
returns "

java.lang.String

".

**Returns:** qualified name of this type excluding any dimension information.

---

#### qualifiedTypeName

String

qualifiedTypeName()

Return qualified name of type excluding any dimension information.

For example, a two dimensional array of String
returns "

java.lang.String

".

For example, a two dimensional array of String
returns "

java.lang.String

".

simpleTypeName

```java
String
simpleTypeName()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the simple name of this type excluding any dimension information.
This is the unqualified name of the type, except that for nested types
only the identifier of the innermost type is included.

For example, the class

Outer.Inner

returns
"

Inner

".

**Returns:** the simple name of this type excluding any dimension information.
**Since:** 1.5

---

#### simpleTypeName

String

simpleTypeName()

Return the simple name of this type excluding any dimension information.
This is the unqualified name of the type, except that for nested types
only the identifier of the innermost type is included.

For example, the class

Outer.Inner

returns
"

Inner

".

For example, the class

Outer.Inner

returns
"

Inner

".

dimension

```java
String
dimension()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type's dimension information, as a string.

For example, a two dimensional array of String returns
"

[][]

".

**Returns:** the type's dimension information as a string.

---

#### dimension

String

dimension()

Return the type's dimension information, as a string.

For example, a two dimensional array of String returns
"

[][]

".

For example, a two dimensional array of String returns
"

[][]

".

toString

```java
String
toString()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return a string representation of the type.
This includes any dimension information and type arguments.

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

**Overrides:** toString

in class

Object
**Returns:** a string representation of the type.

---

#### toString

String

toString()

Return a string representation of the type.
This includes any dimension information and type arguments.

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

For example, a two dimensional array of String may return
"

java.lang.String[][]

",
and the parameterized type

List<Integer>

may return
"

java.util.List<java.lang.Integer>

".

isPrimitive

```java
boolean isPrimitive()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return true if this type represents a primitive type.

**Returns:** true if this type represents a primitive type.
**Since:** 1.5

---

#### isPrimitive

boolean isPrimitive()

Return true if this type represents a primitive type.

asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ClassDoc

if it represents a class
or interface. Array dimensions are ignored.
If this type is a

ParameterizedType

,

TypeVariable

, or

WildcardType

, return
the

ClassDoc

of the type's erasure. If this is an

AnnotationTypeDoc

, return this as a

ClassDoc

(but see

asAnnotationTypeDoc()

).
If this is a primitive type, return null.

**Returns:** the

ClassDoc

of this type,
or null if it is a primitive type.

---

#### asClassDoc

ClassDoc

asClassDoc()

Return this type as a

ClassDoc

if it represents a class
or interface. Array dimensions are ignored.
If this type is a

ParameterizedType

,

TypeVariable

, or

WildcardType

, return
the

ClassDoc

of the type's erasure. If this is an

AnnotationTypeDoc

, return this as a

ClassDoc

(but see

asAnnotationTypeDoc()

).
If this is a primitive type, return null.

asParameterizedType

```java
ParameterizedType
asParameterizedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface. Array dimensions
are ignored.

**Returns:** a

ParameterizedType

if the type is an
invocation of a generic type, or null if it is not.
**Since:** 1.5

---

#### asParameterizedType

ParameterizedType

asParameterizedType()

Return this type as a

ParameterizedType

if it represents
an invocation of a generic class or interface. Array dimensions
are ignored.

asTypeVariable

```java
TypeVariable
asTypeVariable()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

TypeVariable

if it represents
a type variable. Array dimensions are ignored.

**Returns:** a

TypeVariable

if the type is a type variable,
or null if it is not.
**Since:** 1.5

---

#### asTypeVariable

TypeVariable

asTypeVariable()

Return this type as a

TypeVariable

if it represents
a type variable. Array dimensions are ignored.

asWildcardType

```java
WildcardType
asWildcardType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as a

WildcardType

if it represents
a wildcard type.

**Returns:** a

WildcardType

if the type is a wildcard type,
or null if it is not.
**Since:** 1.5

---

#### asWildcardType

WildcardType

asWildcardType()

Return this type as a

WildcardType

if it represents
a wildcard type.

asAnnotatedType

```java
AnnotatedType
asAnnotatedType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns this type as a

AnnotatedType

if it represents
an annotated type.

**Returns:** a

AnnotatedType

if the type if an annotated type,
or null if it is not
**Since:** 1.8

---

#### asAnnotatedType

AnnotatedType

asAnnotatedType()

Returns this type as a

AnnotatedType

if it represents
an annotated type.

asAnnotationTypeDoc

```java
AnnotationTypeDoc
asAnnotationTypeDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type. Array dimensions are ignored.

**Returns:** an

AnnotationTypeDoc

if the type is an annotation
type, or null if it is not.
**Since:** 1.5

---

#### asAnnotationTypeDoc

AnnotationTypeDoc

asAnnotationTypeDoc()

Return this type as an

AnnotationTypeDoc

if it represents
an annotation type. Array dimensions are ignored.

getElementType

```java
Type
getElementType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

If this type is an array type, return the element type of the
array. Otherwise, return null.

**Returns:** a

Type

representing the element type or null.
**Since:** 1.8

---

#### getElementType

Type

getElementType()

If this type is an array type, return the element type of the
array. Otherwise, return null.

---

