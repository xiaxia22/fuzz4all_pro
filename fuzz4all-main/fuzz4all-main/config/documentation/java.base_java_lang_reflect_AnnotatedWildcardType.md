# Interface AnnotatedWildcardType

**Source:** `java.base\java\lang\reflect\AnnotatedWildcardType.html`

### Class Description

```java
public interface
AnnotatedWildcardType

extends
AnnotatedType
```

AnnotatedWildcardType

represents the potentially annotated use of a
wildcard type argument, whose upper or lower bounds may themselves represent
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
[] getAnnotatedLowerBounds()

Returns the potentially annotated lower bounds of this wildcard type.
If no lower bound is explicitly declared, the lower bound is the
type of null. In this case, a zero length array is returned.

**Returns:**
- the potentially annotated lower bounds of this wildcard type or
an empty array if no lower bound is explicitly declared.

**See Also:**
- WildcardType.getLowerBounds()

---

#### AnnotatedType
[] getAnnotatedUpperBounds()

Returns the potentially annotated upper bounds of this wildcard type.
If no upper bound is explicitly declared, the upper bound is
unannotated

Object

**Returns:**
- the potentially annotated upper bounds of this wildcard type

**See Also:**
- WildcardType.getUpperBounds()

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

AnnotatedWildcardType

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

#### Interface AnnotatedWildcardType

**All Superinterfaces:** AnnotatedElement

,

AnnotatedType

```java
public interface
AnnotatedWildcardType

extends
AnnotatedType
```

AnnotatedWildcardType

represents the potentially annotated use of a
wildcard type argument, whose upper or lower bounds may themselves represent
annotated uses of types.

**Since:** 1.8

public interface

AnnotatedWildcardType

extends

AnnotatedType

AnnotatedWildcardType

represents the potentially annotated use of a
wildcard type argument, whose upper or lower bounds may themselves represent
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

getAnnotatedLowerBounds

()

Returns the potentially annotated lower bounds of this wildcard type.

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

AnnotatedType

[]

getAnnotatedUpperBounds

()

Returns the potentially annotated upper bounds of this wildcard type.

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

getAnnotatedLowerBounds

()

Returns the potentially annotated lower bounds of this wildcard type.

AnnotatedType

getAnnotatedOwnerType

()

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

AnnotatedType

[]

getAnnotatedUpperBounds

()

Returns the potentially annotated upper bounds of this wildcard type.

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

Returns the potentially annotated lower bounds of this wildcard type.

Returns the potentially annotated type that this type is a member of, if
this type represents a nested type.

Returns the potentially annotated upper bounds of this wildcard type.

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

- getAnnotatedLowerBounds

```java
AnnotatedType
[] getAnnotatedLowerBounds()
```

Returns the potentially annotated lower bounds of this wildcard type.
If no lower bound is explicitly declared, the lower bound is the
type of null. In this case, a zero length array is returned.

**Returns:** the potentially annotated lower bounds of this wildcard type or
an empty array if no lower bound is explicitly declared.
**See Also:** WildcardType.getLowerBounds()

- getAnnotatedUpperBounds

```java
AnnotatedType
[] getAnnotatedUpperBounds()
```

Returns the potentially annotated upper bounds of this wildcard type.
If no upper bound is explicitly declared, the upper bound is
unannotated

Object

**Returns:** the potentially annotated upper bounds of this wildcard type
**See Also:** WildcardType.getUpperBounds()

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

AnnotatedWildcardType

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

Method Detail

- getAnnotatedLowerBounds

```java
AnnotatedType
[] getAnnotatedLowerBounds()
```

Returns the potentially annotated lower bounds of this wildcard type.
If no lower bound is explicitly declared, the lower bound is the
type of null. In this case, a zero length array is returned.

**Returns:** the potentially annotated lower bounds of this wildcard type or
an empty array if no lower bound is explicitly declared.
**See Also:** WildcardType.getLowerBounds()

- getAnnotatedUpperBounds

```java
AnnotatedType
[] getAnnotatedUpperBounds()
```

Returns the potentially annotated upper bounds of this wildcard type.
If no upper bound is explicitly declared, the upper bound is
unannotated

Object

**Returns:** the potentially annotated upper bounds of this wildcard type
**See Also:** WildcardType.getUpperBounds()

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

AnnotatedWildcardType

.

**Specified by:** getAnnotatedOwnerType

in interface

AnnotatedType
**Returns:** null
**Since:** 9

---

#### Method Detail

getAnnotatedLowerBounds

```java
AnnotatedType
[] getAnnotatedLowerBounds()
```

Returns the potentially annotated lower bounds of this wildcard type.
If no lower bound is explicitly declared, the lower bound is the
type of null. In this case, a zero length array is returned.

**Returns:** the potentially annotated lower bounds of this wildcard type or
an empty array if no lower bound is explicitly declared.
**See Also:** WildcardType.getLowerBounds()

---

#### getAnnotatedLowerBounds

AnnotatedType

[] getAnnotatedLowerBounds()

Returns the potentially annotated lower bounds of this wildcard type.
If no lower bound is explicitly declared, the lower bound is the
type of null. In this case, a zero length array is returned.

getAnnotatedUpperBounds

```java
AnnotatedType
[] getAnnotatedUpperBounds()
```

Returns the potentially annotated upper bounds of this wildcard type.
If no upper bound is explicitly declared, the upper bound is
unannotated

Object

**Returns:** the potentially annotated upper bounds of this wildcard type
**See Also:** WildcardType.getUpperBounds()

---

#### getAnnotatedUpperBounds

AnnotatedType

[] getAnnotatedUpperBounds()

Returns the potentially annotated upper bounds of this wildcard type.
If no upper bound is explicitly declared, the upper bound is
unannotated

Object

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

AnnotatedWildcardType

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

AnnotatedWildcardType

.

Returns

null

for an

AnnotatedType

that is an instance
of

AnnotatedWildcardType

.

---

