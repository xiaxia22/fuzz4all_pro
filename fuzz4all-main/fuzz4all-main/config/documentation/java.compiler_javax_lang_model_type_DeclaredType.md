# Interface DeclaredType

**Source:** `java.compiler\javax\lang\model\type\DeclaredType.html`

### Class Description

```java
public interface
DeclaredType

extends
ReferenceType
```

Represents a declared type, either a class type or an interface type.
This includes parameterized types such as

java.util.Set<String>

as well as raw types.

While a

TypeElement

represents a class or interface

element

, a

DeclaredType

represents a class
or interface

type

, the latter being a use
(or

invocation

) of the former.
See

TypeElement

for more on this distinction.

The supertypes (both class and interface types) of a declared
type may be found using the

Types.directSupertypes(TypeMirror)

method. This returns the
supertypes with any type arguments substituted in.

**All Superinterfaces:** AnnotatedConstruct

,

ReferenceType

,

TypeMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Element
asElement()

Returns the element corresponding to this type.

**Returns:**
- the element corresponding to this type

---

#### TypeMirror
getEnclosingType()

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance. Only types corresponding to inner classes have an
enclosing instance.

**Returns:**
- a type mirror for the enclosing type

**See The Java™ Language Specification :**
- 8.1.3 Inner Classes and Enclosing Instances, 15.9.2 Determining Enclosing Instances

---

#### List
<? extends
TypeMirror
> getTypeArguments()

Returns the actual type arguments of this type.
For a type nested within a parameterized type
(such as

Outer<String>.Inner<Number>

), only the type
arguments of the innermost type are included.

**Returns:**
- the actual type arguments of this type, or an empty list
if none

---

### Additional Sections

#### Interface DeclaredType

**All Superinterfaces:** AnnotatedConstruct

,

ReferenceType

,

TypeMirror

**All Known Subinterfaces:** ErrorType

```java
public interface
DeclaredType

extends
ReferenceType
```

Represents a declared type, either a class type or an interface type.
This includes parameterized types such as

java.util.Set<String>

as well as raw types.

While a

TypeElement

represents a class or interface

element

, a

DeclaredType

represents a class
or interface

type

, the latter being a use
(or

invocation

) of the former.
See

TypeElement

for more on this distinction.

The supertypes (both class and interface types) of a declared
type may be found using the

Types.directSupertypes(TypeMirror)

method. This returns the
supertypes with any type arguments substituted in.

**Since:** 1.6
**See Also:** TypeElement

public interface

DeclaredType

extends

ReferenceType

Represents a declared type, either a class type or an interface type.
This includes parameterized types such as

java.util.Set<String>

as well as raw types.

While a

TypeElement

represents a class or interface

element

, a

DeclaredType

represents a class
or interface

type

, the latter being a use
(or

invocation

) of the former.
See

TypeElement

for more on this distinction.

The supertypes (both class and interface types) of a declared
type may be found using the

Types.directSupertypes(TypeMirror)

method. This returns the
supertypes with any type arguments substituted in.

While a

TypeElement

represents a class or interface

element

, a

DeclaredType

represents a class
or interface

type

, the latter being a use
(or

invocation

) of the former.
See

TypeElement

for more on this distinction.

The supertypes (both class and interface types) of a declared
type may be found using the

Types.directSupertypes(TypeMirror)

method. This returns the
supertypes with any type arguments substituted in.

The supertypes (both class and interface types) of a declared
type may be found using the

Types.directSupertypes(TypeMirror)

method. This returns the
supertypes with any type arguments substituted in.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Element

asElement

()

Returns the element corresponding to this type.

TypeMirror

getEnclosingType

()

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance.

List

<? extends

TypeMirror

>

getTypeArguments

()

Returns the actual type arguments of this type.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Element

asElement

()

Returns the element corresponding to this type.

TypeMirror

getEnclosingType

()

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance.

List

<? extends

TypeMirror

>

getTypeArguments

()

Returns the actual type arguments of this type.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

- Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Method Summary

Returns the element corresponding to this type.

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance.

Returns the actual type arguments of this type.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.type.

TypeMirror

accept

,

equals

,

getKind

,

hashCode

,

toString

---

#### Methods declared in interface javax.lang.model.type. TypeMirror

============ METHOD DETAIL ==========

- Method Detail

- asElement

```java
Element
asElement()
```

Returns the element corresponding to this type.

**Returns:** the element corresponding to this type

- getEnclosingType

```java
TypeMirror
getEnclosingType()
```

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance. Only types corresponding to inner classes have an
enclosing instance.

**Returns:** a type mirror for the enclosing type
**See The Java™ Language Specification :** 8.1.3 Inner Classes and Enclosing Instances, 15.9.2 Determining Enclosing Instances

- getTypeArguments

```java
List
<? extends
TypeMirror
> getTypeArguments()
```

Returns the actual type arguments of this type.
For a type nested within a parameterized type
(such as

Outer<String>.Inner<Number>

), only the type
arguments of the innermost type are included.

**Returns:** the actual type arguments of this type, or an empty list
if none

Method Detail

- asElement

```java
Element
asElement()
```

Returns the element corresponding to this type.

**Returns:** the element corresponding to this type

- getEnclosingType

```java
TypeMirror
getEnclosingType()
```

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance. Only types corresponding to inner classes have an
enclosing instance.

**Returns:** a type mirror for the enclosing type
**See The Java™ Language Specification :** 8.1.3 Inner Classes and Enclosing Instances, 15.9.2 Determining Enclosing Instances

- getTypeArguments

```java
List
<? extends
TypeMirror
> getTypeArguments()
```

Returns the actual type arguments of this type.
For a type nested within a parameterized type
(such as

Outer<String>.Inner<Number>

), only the type
arguments of the innermost type are included.

**Returns:** the actual type arguments of this type, or an empty list
if none

---

#### Method Detail

asElement

```java
Element
asElement()
```

Returns the element corresponding to this type.

**Returns:** the element corresponding to this type

---

#### asElement

Element

asElement()

Returns the element corresponding to this type.

getEnclosingType

```java
TypeMirror
getEnclosingType()
```

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance. Only types corresponding to inner classes have an
enclosing instance.

**Returns:** a type mirror for the enclosing type
**See The Java™ Language Specification :** 8.1.3 Inner Classes and Enclosing Instances, 15.9.2 Determining Enclosing Instances

---

#### getEnclosingType

TypeMirror

getEnclosingType()

Returns the type of the innermost enclosing instance or a

NoType

of kind

NONE

if there is no enclosing
instance. Only types corresponding to inner classes have an
enclosing instance.

getTypeArguments

```java
List
<? extends
TypeMirror
> getTypeArguments()
```

Returns the actual type arguments of this type.
For a type nested within a parameterized type
(such as

Outer<String>.Inner<Number>

), only the type
arguments of the innermost type are included.

**Returns:** the actual type arguments of this type, or an empty list
if none

---

#### getTypeArguments

List

<? extends

TypeMirror

> getTypeArguments()

Returns the actual type arguments of this type.
For a type nested within a parameterized type
(such as

Outer<String>.Inner<Number>

), only the type
arguments of the innermost type are included.

---

