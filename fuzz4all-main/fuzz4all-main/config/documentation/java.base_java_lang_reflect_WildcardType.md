# Interface WildcardType

**Source:** `java.base\java\lang\reflect\WildcardType.html`

### Class Description

```java
public interface
WildcardType

extends
Type
```

WildcardType represents a wildcard type expression, such as

?

,

? extends Number

, or

? super Integer

.

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
[] getUpperBounds()

Returns an array of

Type

objects representing the upper
bound(s) of this type variable. If no upper bound is
explicitly declared, the upper bound is

Object

.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:**
- an array of Types representing the upper bound(s) of this
type variable

**Throws:**
- TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

---

#### Type
[] getLowerBounds()

Returns an array of

Type

objects representing the
lower bound(s) of this type variable. If no lower bound is
explicitly declared, the lower bound is the type of

null

.
In this case, a zero length array is returned.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:**
- an array of Types representing the lower bound(s) of this
type variable

**Throws:**
- TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

---

### Additional Sections

#### Interface WildcardType

**All Superinterfaces:** Type

```java
public interface
WildcardType

extends
Type
```

WildcardType represents a wildcard type expression, such as

?

,

? extends Number

, or

? super Integer

.

**Since:** 1.5

public interface

WildcardType

extends

Type

WildcardType represents a wildcard type expression, such as

?

,

? extends Number

, or

? super Integer

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Type

[]

getLowerBounds

()

Returns an array of

Type

objects representing the
lower bound(s) of this type variable.

Type

[]

getUpperBounds

()

Returns an array of

Type

objects representing the upper
bound(s) of this type variable.

- Methods declared in interface java.lang.reflect.

Type

getTypeName

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Type

[]

getLowerBounds

()

Returns an array of

Type

objects representing the
lower bound(s) of this type variable.

Type

[]

getUpperBounds

()

Returns an array of

Type

objects representing the upper
bound(s) of this type variable.

- Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Method Summary

Returns an array of

Type

objects representing the
lower bound(s) of this type variable.

Returns an array of

Type

objects representing the upper
bound(s) of this type variable.

Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Methods declared in interface java.lang.reflect. Type

============ METHOD DETAIL ==========

- Method Detail

- getUpperBounds

```java
Type
[] getUpperBounds()
```

Returns an array of

Type

objects representing the upper
bound(s) of this type variable. If no upper bound is
explicitly declared, the upper bound is

Object

.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the upper bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

- getLowerBounds

```java
Type
[] getLowerBounds()
```

Returns an array of

Type

objects representing the
lower bound(s) of this type variable. If no lower bound is
explicitly declared, the lower bound is the type of

null

.
In this case, a zero length array is returned.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the lower bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

Method Detail

- getUpperBounds

```java
Type
[] getUpperBounds()
```

Returns an array of

Type

objects representing the upper
bound(s) of this type variable. If no upper bound is
explicitly declared, the upper bound is

Object

.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the upper bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

- getLowerBounds

```java
Type
[] getLowerBounds()
```

Returns an array of

Type

objects representing the
lower bound(s) of this type variable. If no lower bound is
explicitly declared, the lower bound is the type of

null

.
In this case, a zero length array is returned.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the lower bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

---

#### Method Detail

getUpperBounds

```java
Type
[] getUpperBounds()
```

Returns an array of

Type

objects representing the upper
bound(s) of this type variable. If no upper bound is
explicitly declared, the upper bound is

Object

.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the upper bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

---

#### getUpperBounds

Type

[] getUpperBounds()

Returns an array of

Type

objects representing the upper
bound(s) of this type variable. If no upper bound is
explicitly declared, the upper bound is

Object

.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

For each upper bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

getLowerBounds

```java
Type
[] getLowerBounds()
```

Returns an array of

Type

objects representing the
lower bound(s) of this type variable. If no lower bound is
explicitly declared, the lower bound is the type of

null

.
In this case, a zero length array is returned.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

**Returns:** an array of Types representing the lower bound(s) of this
type variable
**Throws:** TypeNotPresentException

- if any of the
bounds refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
bounds refer to a parameterized type that cannot be instantiated
for any reason

---

#### getLowerBounds

Type

[] getLowerBounds()

Returns an array of

Type

objects representing the
lower bound(s) of this type variable. If no lower bound is
explicitly declared, the lower bound is the type of

null

.
In this case, a zero length array is returned.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

For each lower bound B :

- if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

if B is a parameterized type or a type variable, it is created,
(see

ParameterizedType

for the details of the creation process for parameterized types).

Otherwise, B is resolved.

---

