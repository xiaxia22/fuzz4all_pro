# Interface TypeParameterElement

**Source:** `java.compiler\javax\lang\model\element\TypeParameterElement.html`

### Class Description

```java
public interface
TypeParameterElement

extends
Element
```

Represents a formal type parameter of a generic class, interface, method,
or constructor element.
A type parameter declares a

TypeVariable

.

**All Superinterfaces:** AnnotatedConstruct

,

Element

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Element
getGenericElement()

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

**Returns:**
- the generic class, interface, method, or constructor that is
parameterized by this type parameter

---

#### List
<? extends
TypeMirror
> getBounds()

Returns the bounds of this type parameter.
These are the types given by the

extends

clause
used to declare this type parameter.
If no explicit

extends

clause was used,
then

java.lang.Object

is considered to be the sole bound.

**Returns:**
- the bounds of this type parameter, or an empty list if
there are none

---

#### Element
getEnclosingElement()

Returns the

generic element

of this type parameter.

**Specified by:**
- getEnclosingElement

in interface

Element

**Returns:**
- the generic element of this type parameter

**See Also:**
- Elements.getPackageOf(javax.lang.model.element.Element)

---

### Additional Sections

#### Interface TypeParameterElement

**All Superinterfaces:** AnnotatedConstruct

,

Element

```java
public interface
TypeParameterElement

extends
Element
```

Represents a formal type parameter of a generic class, interface, method,
or constructor element.
A type parameter declares a

TypeVariable

.

**Since:** 1.6
**See Also:** TypeVariable

public interface

TypeParameterElement

extends

Element

Represents a formal type parameter of a generic class, interface, method,
or constructor element.
A type parameter declares a

TypeVariable

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

TypeMirror

>

getBounds

()

Returns the bounds of this type parameter.

Element

getEnclosingElement

()

Returns the

generic element

of this type parameter.

Element

getGenericElement

()

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getKind

,

getModifiers

,

getSimpleName

,

hashCode

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<? extends

TypeMirror

>

getBounds

()

Returns the bounds of this type parameter.

Element

getEnclosingElement

()

Returns the

generic element

of this type parameter.

Element

getGenericElement

()

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

- Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getKind

,

getModifiers

,

getSimpleName

,

hashCode

---

#### Method Summary

Returns the bounds of this type parameter.

Returns the

generic element

of this type parameter.

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

Methods declared in interface javax.lang.model.element.

Element

accept

,

asType

,

equals

,

getAnnotation

,

getAnnotationMirrors

,

getEnclosedElements

,

getKind

,

getModifiers

,

getSimpleName

,

hashCode

---

#### Methods declared in interface javax.lang.model.element. Element

============ METHOD DETAIL ==========

- Method Detail

- getGenericElement

```java
Element
getGenericElement()
```

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

**Returns:** the generic class, interface, method, or constructor that is
parameterized by this type parameter

- getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Returns the bounds of this type parameter.
These are the types given by the

extends

clause
used to declare this type parameter.
If no explicit

extends

clause was used,
then

java.lang.Object

is considered to be the sole bound.

**Returns:** the bounds of this type parameter, or an empty list if
there are none

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the

generic element

of this type parameter.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the generic element of this type parameter
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

Method Detail

- getGenericElement

```java
Element
getGenericElement()
```

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

**Returns:** the generic class, interface, method, or constructor that is
parameterized by this type parameter

- getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Returns the bounds of this type parameter.
These are the types given by the

extends

clause
used to declare this type parameter.
If no explicit

extends

clause was used,
then

java.lang.Object

is considered to be the sole bound.

**Returns:** the bounds of this type parameter, or an empty list if
there are none

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the

generic element

of this type parameter.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the generic element of this type parameter
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### Method Detail

getGenericElement

```java
Element
getGenericElement()
```

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

**Returns:** the generic class, interface, method, or constructor that is
parameterized by this type parameter

---

#### getGenericElement

Element

getGenericElement()

Returns the generic class, interface, method, or constructor that is
parameterized by this type parameter.

getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Returns the bounds of this type parameter.
These are the types given by the

extends

clause
used to declare this type parameter.
If no explicit

extends

clause was used,
then

java.lang.Object

is considered to be the sole bound.

**Returns:** the bounds of this type parameter, or an empty list if
there are none

---

#### getBounds

List

<? extends

TypeMirror

> getBounds()

Returns the bounds of this type parameter.
These are the types given by the

extends

clause
used to declare this type parameter.
If no explicit

extends

clause was used,
then

java.lang.Object

is considered to be the sole bound.

getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the

generic element

of this type parameter.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the generic element of this type parameter
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### getEnclosingElement

Element

getEnclosingElement()

Returns the

generic element

of this type parameter.

---

