# Interface AnnotationValue

**Source:** `java.compiler\javax\lang\model\element\AnnotationValue.html`

### Class Description

```java
public interface
AnnotationValue
```

Represents a value of an annotation type element.
A value is of one of the following types:

- a wrapper class (such as

Integer

) for a primitive type

String

TypeMirror

VariableElement

(representing an enum constant)

AnnotationMirror

List<? extends AnnotationValue>

(representing the elements, in declared order, if the value is an array)

**Since:** 1.6

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
getValue()

Returns the value.

**Returns:**
- the value

---

#### String
toString()

Returns a string representation of this value.
This is returned in a form suitable for representing this value
in the source code of an annotation.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this value

---

#### <R,​P> R accept​(
AnnotationValueVisitor
<R,​P> v,
P p)

Applies a visitor to this value.

**Parameters:**
- v

- the visitor operating on this value
- p

- additional parameter to the visitor

**Returns:**
- a visitor-specified result

**Type Parameters:**
- R

- the return type of the visitor's methods
- P

- the type of the additional parameter to the visitor's methods

---

### Additional Sections

#### Interface AnnotationValue

```java
public interface
AnnotationValue
```

Represents a value of an annotation type element.
A value is of one of the following types:

- a wrapper class (such as

Integer

) for a primitive type

String

TypeMirror

VariableElement

(representing an enum constant)

AnnotationMirror

List<? extends AnnotationValue>

(representing the elements, in declared order, if the value is an array)

**Since:** 1.6

public interface

AnnotationValue

Represents a value of an annotation type element.
A value is of one of the following types:

- a wrapper class (such as

Integer

) for a primitive type

String

TypeMirror

VariableElement

(representing an enum constant)

AnnotationMirror

List<? extends AnnotationValue>

(representing the elements, in declared order, if the value is an array)

a wrapper class (such as

Integer

) for a primitive type

String

TypeMirror

VariableElement

(representing an enum constant)

AnnotationMirror

List<? extends AnnotationValue>

(representing the elements, in declared order, if the value is an array)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​P>

R

accept

​(

AnnotationValueVisitor

<R,​P> v,
P p)

Applies a visitor to this value.

Object

getValue

()

Returns the value.

String

toString

()

Returns a string representation of this value.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<R,​P>

R

accept

​(

AnnotationValueVisitor

<R,​P> v,
P p)

Applies a visitor to this value.

Object

getValue

()

Returns the value.

String

toString

()

Returns a string representation of this value.

---

#### Method Summary

Applies a visitor to this value.

Returns the value.

Returns a string representation of this value.

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
Object
getValue()
```

Returns the value.

**Returns:** the value

- toString

```java
String
toString()
```

Returns a string representation of this value.
This is returned in a form suitable for representing this value
in the source code of an annotation.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this value

- accept

```java
<R,​P> R accept​(
AnnotationValueVisitor
<R,​P> v,
P p)
```

Applies a visitor to this value.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this value
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

Method Detail

- getValue

```java
Object
getValue()
```

Returns the value.

**Returns:** the value

- toString

```java
String
toString()
```

Returns a string representation of this value.
This is returned in a form suitable for representing this value
in the source code of an annotation.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this value

- accept

```java
<R,​P> R accept​(
AnnotationValueVisitor
<R,​P> v,
P p)
```

Applies a visitor to this value.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this value
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### Method Detail

getValue

```java
Object
getValue()
```

Returns the value.

**Returns:** the value

---

#### getValue

Object

getValue()

Returns the value.

toString

```java
String
toString()
```

Returns a string representation of this value.
This is returned in a form suitable for representing this value
in the source code of an annotation.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this value

---

#### toString

String

toString()

Returns a string representation of this value.
This is returned in a form suitable for representing this value
in the source code of an annotation.

accept

```java
<R,​P> R accept​(
AnnotationValueVisitor
<R,​P> v,
P p)
```

Applies a visitor to this value.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this value
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### accept

<R,​P> R accept​(

AnnotationValueVisitor

<R,​P> v,
P p)

Applies a visitor to this value.

---

