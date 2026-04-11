# Interface AnnotatedType

**Source:** `java.base\java\lang\reflect\AnnotatedType.html`

### Class Description

```java
public interface
AnnotatedType

extends
AnnotatedElement
```

AnnotatedType

represents the potentially annotated use of a type in
the program currently running in this VM. The use may be of any type in the
Java programming language, including an array type, a parameterized type, a
type variable, or a wildcard type.

**All Superinterfaces:** AnnotatedElement

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default
AnnotatedType
getAnnotatedOwnerType()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type. For example, if this type is

@TA O<T>.I<S>

, return a representation of

@TA O<T>

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

**Returns:**
- an

AnnotatedType

object representing the potentially
annotated type that this type is a member of, or

null

**Throws:**
- TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason

**Since:**
- 9

**Implementation Requirements:**
- This default implementation returns

null

and performs no other
action.

---

#### Type
getType()

Returns the underlying type that this annotated type represents.

**Returns:**
- the type this annotated type represents

---

### Additional Sections

#### Interface AnnotatedType

**All Superinterfaces:** AnnotatedElement

**All Known Subinterfaces:** AnnotatedArrayType

,

AnnotatedParameterizedType

,

AnnotatedTypeVariable

,

AnnotatedWildcardType

```java
public interface
AnnotatedType

extends
AnnotatedElement
```

AnnotatedType

represents the potentially annotated use of a type in
the program currently running in this VM. The use may be of any type in the
Java programming language, including an array type, a parameterized type, a
type variable, or a wildcard type.

**Since:** 1.8

public interface

AnnotatedType

extends

AnnotatedElement

AnnotatedType

represents the potentially annotated use of a type in
the program currently running in this VM. The use may be of any type in the
Java programming language, including an array type, a parameterized type, a
type variable, or a wildcard type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

Type

getType

()

Returns the underlying type that this annotated type represents.

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotation

,

getAnnotations

,

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

Type

getType

()

Returns the underlying type that this annotated type represents.

- Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotation

,

getAnnotations

,

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Method Summary

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

Returns the underlying type that this annotated type represents.

Methods declared in interface java.lang.reflect.

AnnotatedElement

getAnnotation

,

getAnnotations

,

getAnnotationsByType

,

getDeclaredAnnotation

,

getDeclaredAnnotations

,

getDeclaredAnnotationsByType

,

isAnnotationPresent

---

#### Methods declared in interface java.lang.reflect. AnnotatedElement

============ METHOD DETAIL ==========

- Method Detail

- getAnnotatedOwnerType

```java
default
AnnotatedType
getAnnotatedOwnerType()
```

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type. For example, if this type is

@TA O<T>.I<S>

, return a representation of

@TA O<T>

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

**Implementation Requirements:** This default implementation returns

null

and performs no other
action.
**Returns:** an

AnnotatedType

object representing the potentially
annotated type that this type is a member of, or

null
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 9

- getType

```java
Type
getType()
```

Returns the underlying type that this annotated type represents.

**Returns:** the type this annotated type represents

Method Detail

- getAnnotatedOwnerType

```java
default
AnnotatedType
getAnnotatedOwnerType()
```

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type. For example, if this type is

@TA O<T>.I<S>

, return a representation of

@TA O<T>

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

**Implementation Requirements:** This default implementation returns

null

and performs no other
action.
**Returns:** an

AnnotatedType

object representing the potentially
annotated type that this type is a member of, or

null
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 9

- getType

```java
Type
getType()
```

Returns the underlying type that this annotated type represents.

**Returns:** the type this annotated type represents

---

#### Method Detail

getAnnotatedOwnerType

```java
default
AnnotatedType
getAnnotatedOwnerType()
```

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type. For example, if this type is

@TA O<T>.I<S>

, return a representation of

@TA O<T>

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

**Implementation Requirements:** This default implementation returns

null

and performs no other
action.
**Returns:** an

AnnotatedType

object representing the potentially
annotated type that this type is a member of, or

null
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 9

---

#### getAnnotatedOwnerType

default

AnnotatedType

getAnnotatedOwnerType()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type. For example, if this type is

@TA O<T>.I<S>

, return a representation of

@TA O<T>

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

Returns

null

if this

AnnotatedType

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

Returns

null

if this

AnnotatedType

is an instance of

AnnotatedArrayType

,

AnnotatedTypeVariable

, or

AnnotatedWildcardType

.

getType

```java
Type
getType()
```

Returns the underlying type that this annotated type represents.

**Returns:** the type this annotated type represents

---

#### getType

Type

getType()

Returns the underlying type that this annotated type represents.

---

