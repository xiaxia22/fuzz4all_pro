# Interface TypeVariable

**Source:** `java.compiler\javax\lang\model\type\TypeVariable.html`

### Class Description

```java
public interface
TypeVariable

extends
ReferenceType
```

Represents a type variable.
A type variable may be explicitly declared by a

type parameter

of a
type, method, or constructor.
A type variable may also be declared implicitly, as by
the capture conversion of a wildcard type argument
(see chapter 5 of

The Java™ Language Specification

).

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

Returns the element corresponding to this type variable.

**Returns:**
- the element corresponding to this type variable

---

#### TypeMirror
getUpperBound()

Returns the upper bound of this type variable.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

**Returns:**
- the upper bound of this type variable

---

#### TypeMirror
getLowerBound()

Returns the lower bound of this type variable. While a type
parameter cannot include an explicit lower bound declaration,
capture conversion can produce a type variable with a
non-trivial lower bound. Type variables otherwise have a
lower bound of

NullType

.

**Returns:**
- the lower bound of this type variable

---

### Additional Sections

#### Interface TypeVariable

**All Superinterfaces:** AnnotatedConstruct

,

ReferenceType

,

TypeMirror

```java
public interface
TypeVariable

extends
ReferenceType
```

Represents a type variable.
A type variable may be explicitly declared by a

type parameter

of a
type, method, or constructor.
A type variable may also be declared implicitly, as by
the capture conversion of a wildcard type argument
(see chapter 5 of

The Java™ Language Specification

).

**Since:** 1.6
**See Also:** TypeParameterElement

public interface

TypeVariable

extends

ReferenceType

Represents a type variable.
A type variable may be explicitly declared by a

type parameter

of a
type, method, or constructor.
A type variable may also be declared implicitly, as by
the capture conversion of a wildcard type argument
(see chapter 5 of

The Java™ Language Specification

).

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

Returns the element corresponding to this type variable.

TypeMirror

getLowerBound

()

Returns the lower bound of this type variable.

TypeMirror

getUpperBound

()

Returns the upper bound of this type variable.

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

Returns the element corresponding to this type variable.

TypeMirror

getLowerBound

()

Returns the lower bound of this type variable.

TypeMirror

getUpperBound

()

Returns the upper bound of this type variable.

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

Returns the element corresponding to this type variable.

Returns the lower bound of this type variable.

Returns the upper bound of this type variable.

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

Returns the element corresponding to this type variable.

**Returns:** the element corresponding to this type variable

- getUpperBound

```java
TypeMirror
getUpperBound()
```

Returns the upper bound of this type variable.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

**Returns:** the upper bound of this type variable

- getLowerBound

```java
TypeMirror
getLowerBound()
```

Returns the lower bound of this type variable. While a type
parameter cannot include an explicit lower bound declaration,
capture conversion can produce a type variable with a
non-trivial lower bound. Type variables otherwise have a
lower bound of

NullType

.

**Returns:** the lower bound of this type variable

Method Detail

- asElement

```java
Element
asElement()
```

Returns the element corresponding to this type variable.

**Returns:** the element corresponding to this type variable

- getUpperBound

```java
TypeMirror
getUpperBound()
```

Returns the upper bound of this type variable.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

**Returns:** the upper bound of this type variable

- getLowerBound

```java
TypeMirror
getLowerBound()
```

Returns the lower bound of this type variable. While a type
parameter cannot include an explicit lower bound declaration,
capture conversion can produce a type variable with a
non-trivial lower bound. Type variables otherwise have a
lower bound of

NullType

.

**Returns:** the lower bound of this type variable

---

#### Method Detail

asElement

```java
Element
asElement()
```

Returns the element corresponding to this type variable.

**Returns:** the element corresponding to this type variable

---

#### asElement

Element

asElement()

Returns the element corresponding to this type variable.

getUpperBound

```java
TypeMirror
getUpperBound()
```

Returns the upper bound of this type variable.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

**Returns:** the upper bound of this type variable

---

#### getUpperBound

TypeMirror

getUpperBound()

Returns the upper bound of this type variable.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

If this type variable was declared with no explicit
upper bounds, the result is

java.lang.Object

.
If it was declared with multiple upper bounds,
the result is an

intersection type

;
individual bounds can be found by examining the result's

bounds

.

getLowerBound

```java
TypeMirror
getLowerBound()
```

Returns the lower bound of this type variable. While a type
parameter cannot include an explicit lower bound declaration,
capture conversion can produce a type variable with a
non-trivial lower bound. Type variables otherwise have a
lower bound of

NullType

.

**Returns:** the lower bound of this type variable

---

#### getLowerBound

TypeMirror

getLowerBound()

Returns the lower bound of this type variable. While a type
parameter cannot include an explicit lower bound declaration,
capture conversion can produce a type variable with a
non-trivial lower bound. Type variables otherwise have a
lower bound of

NullType

.

---

