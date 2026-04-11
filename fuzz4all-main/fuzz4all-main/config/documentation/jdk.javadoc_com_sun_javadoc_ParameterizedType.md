# Interface ParameterizedType

**Source:** `jdk.javadoc\com\sun\javadoc\ParameterizedType.html`

### Class Description

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ParameterizedType

extends
Type
```

Represents an invocation of a generic class or interface. For example,
given the generic interface

List<E>

, possible invocations
include:

```java
List<String>

List<T extends Number>

List<?>
```

A generic inner class

Outer<T>.Inner<S>

might be invoked as:

```java
Outer<Number>.Inner<String>
```

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ClassDoc
asClassDoc()

Return the generic class or interface that declared this type.

**Specified by:**
- asClassDoc

in interface

Type

**Returns:**
- the generic class or interface that declared this type.

---

#### Type
[] typeArguments()

Return the actual type arguments of this type.
For a generic type that is nested within some other generic type
(such as

Outer<T>.Inner<S>

),
only the type arguments of the innermost type are included.

**Returns:**
- the actual type arguments of this type.

---

#### Type
superclassType()

Return the class type that is a direct supertype of this one.
This is the superclass of this type's declaring class,
with type arguments substituted in.
Return null if this is an interface type.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

**Returns:**
- the class type that is a direct supertype of this one.

---

#### Type
[] interfaceTypes()

Return the interface types directly implemented by or extended by this
parameterized type.
These are the interfaces directly implemented or extended
by this type's declaring class or interface,
with type arguments substituted in.
Return an empty array if there are no interfaces.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

**Returns:**
- the interface types directly implemented by or extended by this
parameterized type.

---

#### Type
containingType()

Return the type that contains this type as a member.
Return null is this is a top-level type.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

**Returns:**
- the type that contains this type as a member.

---

### Additional Sections

#### Interface ParameterizedType

**All Superinterfaces:** Type

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public interface
ParameterizedType

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

Represents an invocation of a generic class or interface. For example,
given the generic interface

List<E>

, possible invocations
include:

```java
List<String>

List<T extends Number>

List<?>
```

A generic inner class

Outer<T>.Inner<S>

might be invoked as:

```java
Outer<Number>.Inner<String>
```

**Since:** 1.5

@Deprecated

(

since

="9",

forRemoval

=true)
public interface

ParameterizedType

extends

Type

Represents an invocation of a generic class or interface. For example,
given the generic interface

List<E>

, possible invocations
include:

```java
List<String>

List<T extends Number>

List<?>
```

A generic inner class

Outer<T>.Inner<S>

might be invoked as:

```java
Outer<Number>.Inner<String>
```

List<String>

List<T extends Number>

List<?>

Outer<Number>.Inner<String>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

ClassDoc

asClassDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the generic class or interface that declared this type.

Type

containingType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type that contains this type as a member.

Type

[]

interfaceTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the interface types directly implemented by or extended by this
parameterized type.

Type

superclassType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class type that is a direct supertype of this one.

Type

[]

typeArguments

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the actual type arguments of this type.

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

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

ClassDoc

asClassDoc

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the generic class or interface that declared this type.

Type

containingType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type that contains this type as a member.

Type

[]

interfaceTypes

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the interface types directly implemented by or extended by this
parameterized type.

Type

superclassType

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class type that is a direct supertype of this one.

Type

[]

typeArguments

()

Deprecated, for removal: This API element is subject to removal in a future version.

Return the actual type arguments of this type.

- Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

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

Return the generic class or interface that declared this type.

Return the type that contains this type as a member.

Return the interface types directly implemented by or extended by this
parameterized type.

Return the class type that is a direct supertype of this one.

Return the actual type arguments of this type.

Methods declared in interface com.sun.javadoc.

Type

asAnnotatedType

,

asAnnotationTypeDoc

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

- asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the generic class or interface that declared this type.

**Specified by:** asClassDoc

in interface

Type
**Returns:** the generic class or interface that declared this type.

- typeArguments

```java
Type
[] typeArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the actual type arguments of this type.
For a generic type that is nested within some other generic type
(such as

Outer<T>.Inner<S>

),
only the type arguments of the innermost type are included.

**Returns:** the actual type arguments of this type.

- superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class type that is a direct supertype of this one.
This is the superclass of this type's declaring class,
with type arguments substituted in.
Return null if this is an interface type.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

**Returns:** the class type that is a direct supertype of this one.

- interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the interface types directly implemented by or extended by this
parameterized type.
These are the interfaces directly implemented or extended
by this type's declaring class or interface,
with type arguments substituted in.
Return an empty array if there are no interfaces.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

**Returns:** the interface types directly implemented by or extended by this
parameterized type.

- containingType

```java
Type
containingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type that contains this type as a member.
Return null is this is a top-level type.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

**Returns:** the type that contains this type as a member.

Method Detail

- asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the generic class or interface that declared this type.

**Specified by:** asClassDoc

in interface

Type
**Returns:** the generic class or interface that declared this type.

- typeArguments

```java
Type
[] typeArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the actual type arguments of this type.
For a generic type that is nested within some other generic type
(such as

Outer<T>.Inner<S>

),
only the type arguments of the innermost type are included.

**Returns:** the actual type arguments of this type.

- superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class type that is a direct supertype of this one.
This is the superclass of this type's declaring class,
with type arguments substituted in.
Return null if this is an interface type.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

**Returns:** the class type that is a direct supertype of this one.

- interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the interface types directly implemented by or extended by this
parameterized type.
These are the interfaces directly implemented or extended
by this type's declaring class or interface,
with type arguments substituted in.
Return an empty array if there are no interfaces.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

**Returns:** the interface types directly implemented by or extended by this
parameterized type.

- containingType

```java
Type
containingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type that contains this type as a member.
Return null is this is a top-level type.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

**Returns:** the type that contains this type as a member.

---

#### Method Detail

asClassDoc

```java
ClassDoc
asClassDoc()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the generic class or interface that declared this type.

**Specified by:** asClassDoc

in interface

Type
**Returns:** the generic class or interface that declared this type.

---

#### asClassDoc

ClassDoc

asClassDoc()

Return the generic class or interface that declared this type.

typeArguments

```java
Type
[] typeArguments()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the actual type arguments of this type.
For a generic type that is nested within some other generic type
(such as

Outer<T>.Inner<S>

),
only the type arguments of the innermost type are included.

**Returns:** the actual type arguments of this type.

---

#### typeArguments

Type

[] typeArguments()

Return the actual type arguments of this type.
For a generic type that is nested within some other generic type
(such as

Outer<T>.Inner<S>

),
only the type arguments of the innermost type are included.

superclassType

```java
Type
superclassType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the class type that is a direct supertype of this one.
This is the superclass of this type's declaring class,
with type arguments substituted in.
Return null if this is an interface type.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

**Returns:** the class type that is a direct supertype of this one.

---

#### superclassType

Type

superclassType()

Return the class type that is a direct supertype of this one.
This is the superclass of this type's declaring class,
with type arguments substituted in.
Return null if this is an interface type.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

For example, if this parameterized type is

java.util.ArrayList<String>

, the result will be

java.util.AbstractList<String>

.

interfaceTypes

```java
Type
[] interfaceTypes()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the interface types directly implemented by or extended by this
parameterized type.
These are the interfaces directly implemented or extended
by this type's declaring class or interface,
with type arguments substituted in.
Return an empty array if there are no interfaces.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

**Returns:** the interface types directly implemented by or extended by this
parameterized type.

---

#### interfaceTypes

Type

[] interfaceTypes()

Return the interface types directly implemented by or extended by this
parameterized type.
These are the interfaces directly implemented or extended
by this type's declaring class or interface,
with type arguments substituted in.
Return an empty array if there are no interfaces.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

For example, the interface extended by

java.util.Set<String>

is

java.util.Collection<String>

.

containingType

```java
Type
containingType()
```

Deprecated, for removal: This API element is subject to removal in a future version.

Return the type that contains this type as a member.
Return null is this is a top-level type.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

**Returns:** the type that contains this type as a member.

---

#### containingType

Type

containingType()

Return the type that contains this type as a member.
Return null is this is a top-level type.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

For example, the containing type of

AnInterface.Nested<Number>

is the

ClassDoc

representing

AnInterface

, and the containing type of

Outer<String>.Inner<Number>

is the

ParameterizedType

representing

Outer<String>

.

---

