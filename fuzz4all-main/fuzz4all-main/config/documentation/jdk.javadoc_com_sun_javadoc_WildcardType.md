# Interface WildcardType

**Source:** `jdk.javadoc\com\sun\javadoc\WildcardType.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
WildcardType

extends
Type
```

Represents a wildcard type argument.
Examples include:

```java
<?>

<? extends E>

<? super T>
```

A wildcard type can have explicit

extends

bounds
or explicit

super

bounds or neither, but not both.

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
[] extendsBounds()

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:**
- the extends bounds of this wildcard type argument

---

#### Type
[] superBounds()

Return the lower bounds of this wildcard type argument
as given by the

super

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:**
- the super bounds of this wildcard type argument

---

### Additional Sections

#### Interface WildcardType

**All Superinterfaces:** Type

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
WildcardType

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

Represents a wildcard type argument.
Examples include:

```java
<?>

<? extends E>

<? super T>
```

A wildcard type can have explicit

extends

bounds
or explicit

super

bounds or neither, but not both.

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

WildcardType

extends

Type

Represents a wildcard type argument.
Examples include:

```java
<?>

<? extends E>

<? super T>
```

A wildcard type can have explicit

extends

bounds
or explicit

super

bounds or neither, but not both.

<?>

<? extends E>

<? super T>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

Type

[]

extendsBounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.

Type

[]

superBounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.

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

Type

[]

extendsBounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.

Type

[]

superBounds

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.

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

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.

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

- extendsBounds

```java
Type
[] extendsBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the extends bounds of this wildcard type argument

- superBounds

```java
Type
[] superBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the super bounds of this wildcard type argument

Method Detail

- extendsBounds

```java
Type
[] extendsBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the extends bounds of this wildcard type argument

- superBounds

```java
Type
[] superBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the super bounds of this wildcard type argument

---

#### Method Detail

extendsBounds

```java
Type
[] extendsBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the extends bounds of this wildcard type argument

---

#### extendsBounds

Type

[] extendsBounds()

Return the upper bounds of this wildcard type argument
as given by the

extends

clause.
Return an empty array if no such bounds are explicitly given.

superBounds

```java
Type
[] superBounds()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the lower bounds of this wildcard type argument
as given by the

super

clause.
Return an empty array if no such bounds are explicitly given.

**Returns:** the super bounds of this wildcard type argument

---

#### superBounds

Type

[] superBounds()

Return the lower bounds of this wildcard type argument
as given by the

super

clause.
Return an empty array if no such bounds are explicitly given.

---

