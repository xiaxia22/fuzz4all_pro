# Interface Parameterizable

**Source:** `java.compiler\javax\lang\model\element\Parameterizable.html`

### Class Description

```java
public interface
Parameterizable

extends
Element
```

A mixin interface for an element that has type parameters.

**All Superinterfaces:** AnnotatedConstruct

,

Element

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
TypeParameterElement
> getTypeParameters()

Returns the formal type parameters of an element in
declaration order.

**Returns:**
- the formal type parameters, or an empty list
if there are none

---

### Additional Sections

#### Interface Parameterizable

**All Superinterfaces:** AnnotatedConstruct

,

Element

**All Known Subinterfaces:** ExecutableElement

,

TypeElement

```java
public interface
Parameterizable

extends
Element
```

A mixin interface for an element that has type parameters.

**Since:** 1.7

public interface

Parameterizable

extends

Element

A mixin interface for an element that has type parameters.

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

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of an element in
declaration order.

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

getEnclosingElement

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

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of an element in
declaration order.

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

getEnclosingElement

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

Returns the formal type parameters of an element in
declaration order.

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

getEnclosingElement

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

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of an element in
declaration order.

**Returns:** the formal type parameters, or an empty list
if there are none

Method Detail

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of an element in
declaration order.

**Returns:** the formal type parameters, or an empty list
if there are none

---

#### Method Detail

getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of an element in
declaration order.

**Returns:** the formal type parameters, or an empty list
if there are none

---

#### getTypeParameters

List

<? extends

TypeParameterElement

> getTypeParameters()

Returns the formal type parameters of an element in
declaration order.

---

