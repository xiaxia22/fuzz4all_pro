# Interface IntersectionType

**Source:** `java.compiler\javax\lang\model\type\IntersectionType.html`

### Class Description

```java
public interface
IntersectionType

extends
TypeMirror
```

Represents an intersection type.

An intersection type can be either implicitly or explicitly
declared in a program. For example, the bound of the type parameter

<T extends Number & Runnable>

is an (implicit) intersection
type. This is represented by an

IntersectionType

with

Number

and

Runnable

as its bounds.

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
TypeMirror
> getBounds()

Return the bounds comprising this intersection type.

**Returns:**
- the bounds of this intersection type

---

### Additional Sections

#### Interface IntersectionType

**All Superinterfaces:** AnnotatedConstruct

,

TypeMirror

```java
public interface
IntersectionType

extends
TypeMirror
```

Represents an intersection type.

An intersection type can be either implicitly or explicitly
declared in a program. For example, the bound of the type parameter

<T extends Number & Runnable>

is an (implicit) intersection
type. This is represented by an

IntersectionType

with

Number

and

Runnable

as its bounds.

**Implementation Note:** In the reference implementation an

IntersectionType

is used to model the explicit target type of a
cast expression.
**Since:** 1.8

public interface

IntersectionType

extends

TypeMirror

Represents an intersection type.

An intersection type can be either implicitly or explicitly
declared in a program. For example, the bound of the type parameter

<T extends Number & Runnable>

is an (implicit) intersection
type. This is represented by an

IntersectionType

with

Number

and

Runnable

as its bounds.

An intersection type can be either implicitly or explicitly
declared in a program. For example, the bound of the type parameter

<T extends Number & Runnable>

is an (implicit) intersection
type. This is represented by an

IntersectionType

with

Number

and

Runnable

as its bounds.

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

Return the bounds comprising this intersection type.

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

List

<? extends

TypeMirror

>

getBounds

()

Return the bounds comprising this intersection type.

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

Return the bounds comprising this intersection type.

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

- getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Return the bounds comprising this intersection type.

**Returns:** the bounds of this intersection type

Method Detail

- getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Return the bounds comprising this intersection type.

**Returns:** the bounds of this intersection type

---

#### Method Detail

getBounds

```java
List
<? extends
TypeMirror
> getBounds()
```

Return the bounds comprising this intersection type.

**Returns:** the bounds of this intersection type

---

#### getBounds

List

<? extends

TypeMirror

> getBounds()

Return the bounds comprising this intersection type.

---

