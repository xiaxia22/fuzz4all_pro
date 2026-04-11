# Interface AnnotatedParameterizedType

**Source:** `java.base\java\lang\reflect\AnnotatedParameterizedType.html`

### Class Description

```java
public interface
AnnotatedParameterizedType

extends
AnnotatedType
```

AnnotatedParameterizedType

represents the potentially annotated use
of a parameterized type, whose type arguments may themselves represent
annotated uses of types.

**All Superinterfaces:** AnnotatedElement

,

AnnotatedType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AnnotatedType
[] getAnnotatedActualTypeArguments()

Returns the potentially annotated actual type arguments of this parameterized type.

**Returns:**
- the potentially annotated actual type arguments of this parameterized type

**See Also:**
- ParameterizedType.getActualTypeArguments()

---

#### AnnotatedType
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

**Specified by:**
- getAnnotatedOwnerType

in interface

AnnotatedType

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

---

### Additional Sections

#### Interface AnnotatedParameterizedType

**All Superinterfaces:** AnnotatedElement

,

AnnotatedType

```java
public interface
AnnotatedParameterizedType

extends
AnnotatedType
```

AnnotatedParameterizedType

represents the potentially annotated use
of a parameterized type, whose type arguments may themselves represent
annotated uses of types.

**Since:** 1.8

public interface

AnnotatedParameterizedType

extends

AnnotatedType

AnnotatedParameterizedType

represents the potentially annotated use
of a parameterized type, whose type arguments may themselves represent
annotated uses of types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AnnotatedType

[]

getAnnotatedActualTypeArguments

()

Returns the potentially annotated actual type arguments of this parameterized type.

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

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

- Methods declared in interface java.lang.reflect.

AnnotatedType

getType

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AnnotatedType

[]

getAnnotatedActualTypeArguments

()

Returns the potentially annotated actual type arguments of this parameterized type.

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

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

- Methods declared in interface java.lang.reflect.

AnnotatedType

getType

---

#### Method Summary

Returns the potentially annotated actual type arguments of this parameterized type.

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

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

Methods declared in interface java.lang.reflect.

AnnotatedType

getType

---

#### Methods declared in interface java.lang.reflect. AnnotatedType

============ METHOD DETAIL ==========

- Method Detail

- getAnnotatedActualTypeArguments

```java
AnnotatedType
[] getAnnotatedActualTypeArguments()
```

Returns the potentially annotated actual type arguments of this parameterized type.

**Returns:** the potentially annotated actual type arguments of this parameterized type
**See Also:** ParameterizedType.getActualTypeArguments()

- getAnnotatedOwnerType

```java
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

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
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

Method Detail

- getAnnotatedActualTypeArguments

```java
AnnotatedType
[] getAnnotatedActualTypeArguments()
```

Returns the potentially annotated actual type arguments of this parameterized type.

**Returns:** the potentially annotated actual type arguments of this parameterized type
**See Also:** ParameterizedType.getActualTypeArguments()

- getAnnotatedOwnerType

```java
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

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
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

#### Method Detail

getAnnotatedActualTypeArguments

```java
AnnotatedType
[] getAnnotatedActualTypeArguments()
```

Returns the potentially annotated actual type arguments of this parameterized type.

**Returns:** the potentially annotated actual type arguments of this parameterized type
**See Also:** ParameterizedType.getActualTypeArguments()

---

#### getAnnotatedActualTypeArguments

AnnotatedType

[] getAnnotatedActualTypeArguments()

Returns the potentially annotated actual type arguments of this parameterized type.

getAnnotatedOwnerType

```java
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

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
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

represents a
top-level type, or a local or anonymous class, or a primitive type, or
void.

---

