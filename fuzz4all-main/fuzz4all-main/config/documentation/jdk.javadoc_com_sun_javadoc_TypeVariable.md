# Interface TypeVariable

**Source:** `jdk.javadoc\com\sun\javadoc\TypeVariable.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
TypeVariable

extends
Type
```

Represents a type variable.
For example, the generic interface

List<E>

has a single
type variable

E

.
A type variable may have explicit bounds, as in

C<R extends Remote>

.

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
[] bounds()

Return the bounds of this type variable.
These are the types given by the

extends

clause.
Return an empty array if there are no explicit bounds.

**Returns:**
- the bounds of this type variable.

---

#### ProgramElementDoc
owner()

Return the class, interface, method, or constructor within
which this type variable is declared.

**Returns:**
- the class, interface, method, or constructor within
which this type variable is declared.

---

#### AnnotationDesc
[] annotations()

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:**
- the annotations of this program element or
an empty array if there are none.

---

### Additional Sections

#### Interface TypeVariable

**All Superinterfaces:** Type

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
TypeVariable

extends
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

Represents a type variable.
For example, the generic interface

List<E>

has a single
type variable

E

.
A type variable may have explicit bounds, as in

C<R extends Remote>

.

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

TypeVariable

extends

Type

Represents a type variable.
For example, the generic interface

List<E>

has a single
type variable

E

.
A type variable may have explicit bounds, as in

C<R extends Remote>

.

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

Get the annotations of this program element.

Type

[]

bounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the bounds of this type variable.

ProgramElementDoc

owner

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class, interface, method, or constructor within
which this type variable is declared.

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

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

Get the annotations of this program element.

Type

[]

bounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the bounds of this type variable.

ProgramElementDoc

owner

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class, interface, method, or constructor within
which this type variable is declared.

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

---

#### Method Summary

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.

Return the bounds of this type variable.

Return the class, interface, method, or constructor within
which this type variable is declared.

Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

,

asClassDoc

,

asParameterizedType

,

asTypeVariable

,

asWildcardType

,

dimension

,

getElementType

,

isPrimitive

,

qualifiedTypeName

,

simpleTypeName

,

toString

,

typeName

---

#### Methods declared in interface com.sun.javadoc. Type

============ METHOD DETAIL ==========

- Method Detail

- bounds

```java
Type
[] bounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the bounds of this type variable.
These are the types given by the

extends

clause.
Return an empty array if there are no explicit bounds.

**Returns:** the bounds of this type variable.

- owner

```java
ProgramElementDoc
owner()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class, interface, method, or constructor within
which this type variable is declared.

**Returns:** the class, interface, method, or constructor within
which this type variable is declared.

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element or
an empty array if there are none.

Method Detail

- bounds

```java
Type
[] bounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the bounds of this type variable.
These are the types given by the

extends

clause.
Return an empty array if there are no explicit bounds.

**Returns:** the bounds of this type variable.

- owner

```java
ProgramElementDoc
owner()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class, interface, method, or constructor within
which this type variable is declared.

**Returns:** the class, interface, method, or constructor within
which this type variable is declared.

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element or
an empty array if there are none.

---

#### Method Detail

bounds

```java
Type
[] bounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the bounds of this type variable.
These are the types given by the

extends

clause.
Return an empty array if there are no explicit bounds.

**Returns:** the bounds of this type variable.

---

#### bounds

Type

[] bounds()

Return the bounds of this type variable.
These are the types given by the

extends

clause.
Return an empty array if there are no explicit bounds.

owner

```java
ProgramElementDoc
owner()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class, interface, method, or constructor within
which this type variable is declared.

**Returns:** the class, interface, method, or constructor within
which this type variable is declared.

---

#### owner

ProgramElementDoc

owner()

Return the class, interface, method, or constructor within
which this type variable is declared.

annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Get the annotations of this program element.
Return an empty array if there are none.

**Returns:** the annotations of this program element or
an empty array if there are none.

---

#### annotations

AnnotationDesc

[] annotations()

Get the annotations of this program element.
Return an empty array if there are none.

---

