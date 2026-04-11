# Interface AnnotatedTypeVariable

**Source:** `java.base\java\lang\reflect\AnnotatedTypeVariable.html`

### Class Description

```java
public interface
AnnotatedTypeVariable

extends
AnnotatedType
```

AnnotatedTypeVariable

represents the potentially annotated use of a
type variable, whose declaration may have bounds which themselves represent
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
[] getAnnotatedBounds()

Returns the potentially annotated bounds of this type variable.
If no bound is explicitly declared, the bound is unannotated

Object

.

**Returns:**
- the potentially annotated bounds of this type variable

**See Also:**
- TypeVariable.getBounds()

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

AnnotatedTypeVariable

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

#### Interface AnnotatedTypeVariable

**All Superinterfaces:** AnnotatedElement

,

AnnotatedType

```java
public interface
AnnotatedTypeVariable

extends
AnnotatedType
```

AnnotatedTypeVariable

represents the potentially annotated use of a
type variable, whose declaration may have bounds which themselves represent
annotated uses of types.

**Since:** 1.8

public interface

AnnotatedTypeVariable

extends

AnnotatedType

AnnotatedTypeVariable

represents the potentially annotated use of a
type variable, whose declaration may have bounds which themselves represent
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

getAnnotatedBounds

()

Returns the potentially annotated bounds of this type variable.

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

getAnnotatedBounds

()

Returns the potentially annotated bounds of this type variable.

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

Returns the potentially annotated bounds of this type variable.

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

- getAnnotatedBounds

```java
AnnotatedType
[] getAnnotatedBounds()
```

Returns the potentially annotated bounds of this type variable.
If no bound is explicitly declared, the bound is unannotated

Object

.

**Returns:** the potentially annotated bounds of this type variable
**See Also:** TypeVariable.getBounds()

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

AnnotatedTypeVariable

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

Method Detail

- getAnnotatedBounds

```java
AnnotatedType
[] getAnnotatedBounds()
```

Returns the potentially annotated bounds of this type variable.
If no bound is explicitly declared, the bound is unannotated

Object

.

**Returns:** the potentially annotated bounds of this type variable
**See Also:** TypeVariable.getBounds()

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

AnnotatedTypeVariable

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

---

#### Method Detail

getAnnotatedBounds

```java
AnnotatedType
[] getAnnotatedBounds()
```

Returns the potentially annotated bounds of this type variable.
If no bound is explicitly declared, the bound is unannotated

Object

.

**Returns:** the potentially annotated bounds of this type variable
**See Also:** TypeVariable.getBounds()

---

#### getAnnotatedBounds

AnnotatedType

[] getAnnotatedBounds()

Returns the potentially annotated bounds of this type variable.
If no bound is explicitly declared, the bound is unannotated

Object

.

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

AnnotatedTypeVariable

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

AnnotatedTypeVariable

.

Returns

null

for an

AnnotatedType

that is an instance
of

AnnotatedTypeVariable

.

---

