# Interface ParameterizedType

**Source:** `java.base\java\lang\reflect\ParameterizedType.html`

### Class Description

```java
public interface
ParameterizedType

extends
Type
```

ParameterizedType represents a parameterized type such as
Collection<String>.

A parameterized type is created the first time it is needed by a
reflective method, as specified in this package. When a
parameterized type p is created, the generic type declaration that
p instantiates is resolved, and all type arguments of p are created
recursively. See

TypeVariable

for details on the creation process for type
variables. Repeated creation of a parameterized type has no effect.

Instances of classes that implement this interface must implement
an equals() method that equates any two instances that share the
same generic type declaration and have equal type parameters.

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
[] getActualTypeArguments()

Returns an array of

Type

objects representing the actual type
arguments to this type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

**Returns:**
- an array of

Type

objects representing the actual type
arguments to this type

**Throws:**
- TypeNotPresentException

- if any of the
actual type arguments refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if any of the
actual type parameters refer to a parameterized type that cannot
be instantiated for any reason

**Since:**
- 1.5

---

#### Type
getRawType()

Returns the

Type

object representing the class or interface
that declared this type.

**Returns:**
- the

Type

object representing the class or interface
that declared this type

**Since:**
- 1.5

---

#### Type
getOwnerType()

Returns a

Type

object representing the type that this type
is a member of. For example, if this type is

O<T>.I<S>

,
return a representation of

O<T>

.

If this type is a top-level type,

null

is returned.

**Returns:**
- a

Type

object representing the type that
this type is a member of. If this type is a top-level type,

null

is returned

**Throws:**
- TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason

**Since:**
- 1.5

---

### Additional Sections

#### Interface ParameterizedType

**All Superinterfaces:** Type

```java
public interface
ParameterizedType

extends
Type
```

ParameterizedType represents a parameterized type such as
Collection<String>.

A parameterized type is created the first time it is needed by a
reflective method, as specified in this package. When a
parameterized type p is created, the generic type declaration that
p instantiates is resolved, and all type arguments of p are created
recursively. See

TypeVariable

for details on the creation process for type
variables. Repeated creation of a parameterized type has no effect.

Instances of classes that implement this interface must implement
an equals() method that equates any two instances that share the
same generic type declaration and have equal type parameters.

**Since:** 1.5

public interface

ParameterizedType

extends

Type

ParameterizedType represents a parameterized type such as
Collection<String>.

A parameterized type is created the first time it is needed by a
reflective method, as specified in this package. When a
parameterized type p is created, the generic type declaration that
p instantiates is resolved, and all type arguments of p are created
recursively. See

TypeVariable

for details on the creation process for type
variables. Repeated creation of a parameterized type has no effect.

Instances of classes that implement this interface must implement
an equals() method that equates any two instances that share the
same generic type declaration and have equal type parameters.

A parameterized type is created the first time it is needed by a
reflective method, as specified in this package. When a
parameterized type p is created, the generic type declaration that
p instantiates is resolved, and all type arguments of p are created
recursively. See

TypeVariable

for details on the creation process for type
variables. Repeated creation of a parameterized type has no effect.

Instances of classes that implement this interface must implement
an equals() method that equates any two instances that share the
same generic type declaration and have equal type parameters.

Instances of classes that implement this interface must implement
an equals() method that equates any two instances that share the
same generic type declaration and have equal type parameters.

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

getActualTypeArguments

()

Returns an array of

Type

objects representing the actual type
arguments to this type.

Type

getOwnerType

()

Returns a

Type

object representing the type that this type
is a member of.

Type

getRawType

()

Returns the

Type

object representing the class or interface
that declared this type.

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

getActualTypeArguments

()

Returns an array of

Type

objects representing the actual type
arguments to this type.

Type

getOwnerType

()

Returns a

Type

object representing the type that this type
is a member of.

Type

getRawType

()

Returns the

Type

object representing the class or interface
that declared this type.

- Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Method Summary

Returns an array of

Type

objects representing the actual type
arguments to this type.

Returns a

Type

object representing the type that this type
is a member of.

Returns the

Type

object representing the class or interface
that declared this type.

Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Methods declared in interface java.lang.reflect. Type

============ METHOD DETAIL ==========

- Method Detail

- getActualTypeArguments

```java
Type
[] getActualTypeArguments()
```

Returns an array of

Type

objects representing the actual type
arguments to this type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

**Returns:** an array of

Type

objects representing the actual type
arguments to this type
**Throws:** TypeNotPresentException

- if any of the
actual type arguments refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
actual type parameters refer to a parameterized type that cannot
be instantiated for any reason
**Since:** 1.5

- getRawType

```java
Type
getRawType()
```

Returns the

Type

object representing the class or interface
that declared this type.

**Returns:** the

Type

object representing the class or interface
that declared this type
**Since:** 1.5

- getOwnerType

```java
Type
getOwnerType()
```

Returns a

Type

object representing the type that this type
is a member of. For example, if this type is

O<T>.I<S>

,
return a representation of

O<T>

.

If this type is a top-level type,

null

is returned.

**Returns:** a

Type

object representing the type that
this type is a member of. If this type is a top-level type,

null

is returned
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 1.5

Method Detail

- getActualTypeArguments

```java
Type
[] getActualTypeArguments()
```

Returns an array of

Type

objects representing the actual type
arguments to this type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

**Returns:** an array of

Type

objects representing the actual type
arguments to this type
**Throws:** TypeNotPresentException

- if any of the
actual type arguments refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
actual type parameters refer to a parameterized type that cannot
be instantiated for any reason
**Since:** 1.5

- getRawType

```java
Type
getRawType()
```

Returns the

Type

object representing the class or interface
that declared this type.

**Returns:** the

Type

object representing the class or interface
that declared this type
**Since:** 1.5

- getOwnerType

```java
Type
getOwnerType()
```

Returns a

Type

object representing the type that this type
is a member of. For example, if this type is

O<T>.I<S>

,
return a representation of

O<T>

.

If this type is a top-level type,

null

is returned.

**Returns:** a

Type

object representing the type that
this type is a member of. If this type is a top-level type,

null

is returned
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 1.5

---

#### Method Detail

getActualTypeArguments

```java
Type
[] getActualTypeArguments()
```

Returns an array of

Type

objects representing the actual type
arguments to this type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

**Returns:** an array of

Type

objects representing the actual type
arguments to this type
**Throws:** TypeNotPresentException

- if any of the
actual type arguments refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if any of the
actual type parameters refer to a parameterized type that cannot
be instantiated for any reason
**Since:** 1.5

---

#### getActualTypeArguments

Type

[] getActualTypeArguments()

Returns an array of

Type

objects representing the actual type
arguments to this type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

Note that in some cases, the returned array be empty. This can occur
if this type represents a non-parameterized type nested within
a parameterized type.

getRawType

```java
Type
getRawType()
```

Returns the

Type

object representing the class or interface
that declared this type.

**Returns:** the

Type

object representing the class or interface
that declared this type
**Since:** 1.5

---

#### getRawType

Type

getRawType()

Returns the

Type

object representing the class or interface
that declared this type.

getOwnerType

```java
Type
getOwnerType()
```

Returns a

Type

object representing the type that this type
is a member of. For example, if this type is

O<T>.I<S>

,
return a representation of

O<T>

.

If this type is a top-level type,

null

is returned.

**Returns:** a

Type

object representing the type that
this type is a member of. If this type is a top-level type,

null

is returned
**Throws:** TypeNotPresentException

- if the owner type
refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the owner type
refers to a parameterized type that cannot be instantiated
for any reason
**Since:** 1.5

---

#### getOwnerType

Type

getOwnerType()

Returns a

Type

object representing the type that this type
is a member of. For example, if this type is

O<T>.I<S>

,
return a representation of

O<T>

.

If this type is a top-level type,

null

is returned.

If this type is a top-level type,

null

is returned.

---

