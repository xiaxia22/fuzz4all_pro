# Interface AnnotatedType

**Source:** `jdk.javadoc\com\sun\javadoc\AnnotatedType.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotatedType

extends
Type
```

Represents an annotated type.
For example:

```java
@NonNull String

@Positive int
```

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AnnotationDesc
[] annotations()

Returns the annotations associated with this type.

**Returns:**
- the annotations associated with this type

---

#### Type
underlyingType()

Returns the underlying type.

**Returns:**
- the underlying type

---

### Additional Sections

#### Interface AnnotatedType

**All Superinterfaces:** Type

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
AnnotatedType

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

Represents an annotated type.
For example:

```java
@NonNull String

@Positive int
```

**Since:** 1.8

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

AnnotatedType

extends

Type

Represents an annotated type.
For example:

```java
@NonNull String

@Positive int
```

@NonNull String

@Positive int

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

Returns the annotations associated with this type.

Type

underlyingType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the underlying type.

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

Returns the annotations associated with this type.

Type

underlyingType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the underlying type.

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

Returns the annotations associated with this type.

Returns the underlying type.

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

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotations associated with this type.

**Returns:** the annotations associated with this type

- underlyingType

```java
Type
underlyingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the underlying type.

**Returns:** the underlying type

Method Detail

- annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotations associated with this type.

**Returns:** the annotations associated with this type

- underlyingType

```java
Type
underlyingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the underlying type.

**Returns:** the underlying type

---

#### Method Detail

annotations

```java
AnnotationDesc
[] annotations()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the annotations associated with this type.

**Returns:** the annotations associated with this type

---

#### annotations

AnnotationDesc

[] annotations()

Returns the annotations associated with this type.

underlyingType

```java
Type
underlyingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Returns the underlying type.

**Returns:** the underlying type

---

#### underlyingType

Type

underlyingType()

Returns the underlying type.

---

