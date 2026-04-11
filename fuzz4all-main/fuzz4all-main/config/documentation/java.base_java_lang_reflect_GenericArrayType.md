# Interface GenericArrayType

**Source:** `java.base\java\lang\reflect\GenericArrayType.html`

### Class Description

```java
public interface
GenericArrayType

extends
Type
```

GenericArrayType

represents an array type whose component
type is either a parameterized type or a type variable.

**All Superinterfaces:** Type

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Type
getGenericComponentType()

Returns a

Type

object representing the component type
of this array. This method creates the component type of the
array. See the declaration of

ParameterizedType

for the
semantics of the creation process for parameterized types and
see

TypeVariable

for the
creation process for type variables.

**Returns:**
- a

Type

object representing the component type
of this array

**Throws:**
- TypeNotPresentException

- if the underlying array type's
component type refers to a non-existent type declaration
- MalformedParameterizedTypeException

- if the
underlying array type's component type refers to a
parameterized type that cannot be instantiated for any reason

---

### Additional Sections

#### Interface GenericArrayType

**All Superinterfaces:** Type

```java
public interface
GenericArrayType

extends
Type
```

GenericArrayType

represents an array type whose component
type is either a parameterized type or a type variable.

**Since:** 1.5

public interface

GenericArrayType

extends

Type

GenericArrayType

represents an array type whose component
type is either a parameterized type or a type variable.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Type

getGenericComponentType

()

Returns a

Type

object representing the component type
of this array.

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

getGenericComponentType

()

Returns a

Type

object representing the component type
of this array.

- Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Method Summary

Returns a

Type

object representing the component type
of this array.

Methods declared in interface java.lang.reflect.

Type

getTypeName

---

#### Methods declared in interface java.lang.reflect. Type

============ METHOD DETAIL ==========

- Method Detail

- getGenericComponentType

```java
Type
getGenericComponentType()
```

Returns a

Type

object representing the component type
of this array. This method creates the component type of the
array. See the declaration of

ParameterizedType

for the
semantics of the creation process for parameterized types and
see

TypeVariable

for the
creation process for type variables.

**Returns:** a

Type

object representing the component type
of this array
**Throws:** TypeNotPresentException

- if the underlying array type's
component type refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the
underlying array type's component type refers to a
parameterized type that cannot be instantiated for any reason

Method Detail

- getGenericComponentType

```java
Type
getGenericComponentType()
```

Returns a

Type

object representing the component type
of this array. This method creates the component type of the
array. See the declaration of

ParameterizedType

for the
semantics of the creation process for parameterized types and
see

TypeVariable

for the
creation process for type variables.

**Returns:** a

Type

object representing the component type
of this array
**Throws:** TypeNotPresentException

- if the underlying array type's
component type refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the
underlying array type's component type refers to a
parameterized type that cannot be instantiated for any reason

---

#### Method Detail

getGenericComponentType

```java
Type
getGenericComponentType()
```

Returns a

Type

object representing the component type
of this array. This method creates the component type of the
array. See the declaration of

ParameterizedType

for the
semantics of the creation process for parameterized types and
see

TypeVariable

for the
creation process for type variables.

**Returns:** a

Type

object representing the component type
of this array
**Throws:** TypeNotPresentException

- if the underlying array type's
component type refers to a non-existent type declaration
**Throws:** MalformedParameterizedTypeException

- if the
underlying array type's component type refers to a
parameterized type that cannot be instantiated for any reason

---

#### getGenericComponentType

Type

getGenericComponentType()

Returns a

Type

object representing the component type
of this array. This method creates the component type of the
array. See the declaration of

ParameterizedType

for the
semantics of the creation process for parameterized types and
see

TypeVariable

for the
creation process for type variables.

---

