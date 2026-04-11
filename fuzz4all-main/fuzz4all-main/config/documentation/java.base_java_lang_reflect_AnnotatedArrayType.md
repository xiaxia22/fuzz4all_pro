# Interface AnnotatedArrayType

**Source:** `java.base\java\lang\reflect\AnnotatedArrayType.html`

### Class Description

```java
public interface
AnnotatedArrayType

extends
AnnotatedType
```

AnnotatedArrayType

represents the potentially annotated use of an
array type, whose component type may itself represent the annotated use of a
type.

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
getAnnotatedGenericComponentType()

Returns the potentially annotated generic component type of this array type.

**Returns:**
- the potentially annotated generic component type of this array type

**See Also:**
- GenericArrayType.getGenericComponentType()

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

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

**Specified by:**
- getAnnotatedOwnerType

in interface

AnnotatedType

**Returns:**
- null

**Since:**
- 9

---

### Additional Sections

#### Interface AnnotatedArrayType

**All Superinterfaces:** AnnotatedElement

,

AnnotatedType

```java
public interface
AnnotatedArrayType

extends
AnnotatedType
```

AnnotatedArrayType

represents the potentially annotated use of an
array type, whose component type may itself represent the annotated use of a
type.

**Since:** 1.8

public interface

AnnotatedArrayType

extends

AnnotatedType

AnnotatedArrayType

represents the potentially annotated use of an
array type, whose component type may itself represent the annotated use of a
type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AnnotatedType

getAnnotatedGenericComponentType

()

Returns the potentially annotated generic component type of this array type.

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

getAnnotatedGenericComponentType

()

Returns the potentially annotated generic component type of this array type.

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

Returns the potentially annotated generic component type of this array type.

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

- getAnnotatedGenericComponentType

```java
AnnotatedType
getAnnotatedGenericComponentType()
```

Returns the potentially annotated generic component type of this array type.

**Returns:** the potentially annotated generic component type of this array type
**See Also:** GenericArrayType.getGenericComponentType()

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

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

Method Detail

- getAnnotatedGenericComponentType

```java
AnnotatedType
getAnnotatedGenericComponentType()
```

Returns the potentially annotated generic component type of this array type.

**Returns:** the potentially annotated generic component type of this array type
**See Also:** GenericArrayType.getGenericComponentType()

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

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

---

#### Method Detail

getAnnotatedGenericComponentType

```java
AnnotatedType
getAnnotatedGenericComponentType()
```

Returns the potentially annotated generic component type of this array type.

**Returns:** the potentially annotated generic component type of this array type
**See Also:** GenericArrayType.getGenericComponentType()

---

#### getAnnotatedGenericComponentType

AnnotatedType

getAnnotatedGenericComponentType()

Returns the potentially annotated generic component type of this array type.

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

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
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

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

Returns

null

for an

AnnotatedType

that is an instance
of

AnnotatedArrayType

.

---

