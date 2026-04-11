# Interface GenericDeclaration

**Source:** `java.base\java\lang\reflect\GenericDeclaration.html`

### Class Description

```java
public interface
GenericDeclaration

extends
AnnotatedElement
```

A common interface for all entities that declare type variables.

**All Superinterfaces:** AnnotatedElement

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeVariable
<?>[] getTypeParameters()

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order. Returns an array of length 0 if
the underlying generic declaration declares no type variables.

**Returns:**
- an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration

**Throws:**
- GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

---

### Additional Sections

#### Interface GenericDeclaration

**All Superinterfaces:** AnnotatedElement

**All Known Implementing Classes:** Class

,

Constructor

,

Executable

,

Method

```java
public interface
GenericDeclaration

extends
AnnotatedElement
```

A common interface for all entities that declare type variables.

**Since:** 1.5

public interface

GenericDeclaration

extends

AnnotatedElement

A common interface for all entities that declare type variables.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

TypeVariable

<?>[]

getTypeParameters

()

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order.

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

Modifier and Type

Method

Description

TypeVariable

<?>[]

getTypeParameters

()

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order.

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

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order.

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

- getTypeParameters

```java
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order. Returns an array of length 0 if
the underlying generic declaration declares no type variables.

**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

Method Detail

- getTypeParameters

```java
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order. Returns an array of length 0 if
the underlying generic declaration declares no type variables.

**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

---

#### Method Detail

getTypeParameters

```java
TypeVariable
<?>[] getTypeParameters()
```

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order. Returns an array of length 0 if
the underlying generic declaration declares no type variables.

**Returns:** an array of

TypeVariable

objects that represent
the type variables declared by this generic declaration
**Throws:** GenericSignatureFormatError

- if the generic
signature of this generic declaration does not conform to
the format specified in

The Java™ Virtual Machine Specification

---

#### getTypeParameters

TypeVariable

<?>[] getTypeParameters()

Returns an array of

TypeVariable

objects that
represent the type variables declared by the generic
declaration represented by this

GenericDeclaration

object, in declaration order. Returns an array of length 0 if
the underlying generic declaration declares no type variables.

---

