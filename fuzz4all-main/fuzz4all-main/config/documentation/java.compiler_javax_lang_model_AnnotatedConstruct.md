# Interface AnnotatedConstruct

**Source:** `java.compiler\javax\lang\model\AnnotatedConstruct.html`

### Class Description

```java
public interface
AnnotatedConstruct
```

Represents a construct that can be annotated.

A construct is either an

element

or a

type

. Annotations on an element
are on a

declaration

, whereas annotations on a type are on
a specific

use

of a type name.

The terms

directly present

,

present

,

indirectly present

, and

associated

are used
throughout this interface to describe precisely which annotations
are returned by the methods defined herein.

In the definitions below, an annotation

A

has an
annotation type

AT

. If

AT

is a repeatable annotation
type, the type of the containing annotation is

ATC

.

Annotation

A

is

directly present

on a construct

C

if either:

- A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

**All Known Subinterfaces:** ArrayType

,

DeclaredType

,

Element

,

ErrorType

,

ExecutableElement

,

ExecutableType

,

IntersectionType

,

ModuleElement

,

NoType

,

NullType

,

PackageElement

,

Parameterizable

,

PrimitiveType

,

QualifiedNameable

,

ReferenceType

,

TypeElement

,

TypeMirror

,

TypeParameterElement

,

TypeVariable

,

UnionType

,

VariableElement

,

WildcardType

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
AnnotationMirror
> getAnnotationMirrors()

Returns the annotations that are

directly present

on
this construct.

**Returns:**
- the annotations

directly present

on this
construct; an empty list if there are none

---

#### <A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Parameters:**
- annotationType

- the

Class

object corresponding to
the annotation type

**Returns:**
- this construct's annotation for the specified
annotation type if present, else

null

**See Also:**
- getAnnotationMirrors()

,

AnnotatedElement.getAnnotation(java.lang.Class<T>)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException

**Type Parameters:**
- A

- the annotation type

**See The Java™ Language Specification :**
- 9.6.1 Annotation Type Elements

---

#### <A extends
Annotation
> A[] getAnnotationsByType​(
Class
<A> annotationType)

Returns annotations that are

associated

with this construct.

If there are no annotations associated with this construct, the
return value is an array of length 0.

The order of annotations which are directly or indirectly
present on a construct

C

is computed as if indirectly present
annotations on

C

are directly present on

C

in place of their
container annotation, in the order in which they appear in the
value element of the container annotation.

The difference between this method and

getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

, and if so, attempts to find one or more
annotations of that type by "looking through" a container annotation.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Parameters:**
- annotationType

- the

Class

object corresponding to
the annotation type

**Returns:**
- this construct's annotations for the specified annotation
type if present on this construct, else an empty array

**See Also:**
- getAnnotationMirrors()

,

getAnnotation(Class)

,

AnnotatedElement.getAnnotationsByType(Class)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException

**Type Parameters:**
- A

- the annotation type

**See The Java™ Language Specification :**
- 9.6 Annotation Types, 9.6.1 Annotation Type Elements

---

### Additional Sections

#### Interface AnnotatedConstruct

**All Known Subinterfaces:** ArrayType

,

DeclaredType

,

Element

,

ErrorType

,

ExecutableElement

,

ExecutableType

,

IntersectionType

,

ModuleElement

,

NoType

,

NullType

,

PackageElement

,

Parameterizable

,

PrimitiveType

,

QualifiedNameable

,

ReferenceType

,

TypeElement

,

TypeMirror

,

TypeParameterElement

,

TypeVariable

,

UnionType

,

VariableElement

,

WildcardType

```java
public interface
AnnotatedConstruct
```

Represents a construct that can be annotated.

A construct is either an

element

or a

type

. Annotations on an element
are on a

declaration

, whereas annotations on a type are on
a specific

use

of a type name.

The terms

directly present

,

present

,

indirectly present

, and

associated

are used
throughout this interface to describe precisely which annotations
are returned by the methods defined herein.

In the definitions below, an annotation

A

has an
annotation type

AT

. If

AT

is a repeatable annotation
type, the type of the containing annotation is

ATC

.

Annotation

A

is

directly present

on a construct

C

if either:

- A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

**Since:** 1.8
**See The Java™ Language Specification :** 9.6 Annotation Types, 9.6.3.3 @Inherited

public interface

AnnotatedConstruct

Represents a construct that can be annotated.

A construct is either an

element

or a

type

. Annotations on an element
are on a

declaration

, whereas annotations on a type are on
a specific

use

of a type name.

The terms

directly present

,

present

,

indirectly present

, and

associated

are used
throughout this interface to describe precisely which annotations
are returned by the methods defined herein.

In the definitions below, an annotation

A

has an
annotation type

AT

. If

AT

is a repeatable annotation
type, the type of the containing annotation is

ATC

.

Annotation

A

is

directly present

on a construct

C

if either:

- A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

In the definitions below, an annotation

A

has an
annotation type

AT

. If

AT

is a repeatable annotation
type, the type of the containing annotation is

ATC

.

Annotation

A

is

directly present

on a construct

C

if either:

- A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

Annotation

A

is

directly present

on a construct

C

if either:

- A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

A

is explicitly or implicitly declared as applying to
the source code representation of

C

.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

Typically, if exactly one annotation of type

AT

appears in
the source code of representation of

C

, then

A

is
explicitly declared as applying to

C

.

If there are multiple annotations of type

AT

present on

C

, then if

AT

is repeatable annotation type, an
annotation of type

ATC

is

implicitly declared

on

C

.

A representation of

A

appears in the executable output
for

C

, such as the

RuntimeVisibleAnnotations

or

RuntimeVisibleParameterAnnotations

attributes of a class
file.

An annotation

A

is

present

on a
construct

C

if either:

- A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

An annotation

A

is

indirectly present

on a construct

C

if both:

- AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

An annotation

A

is

associated

with a construct

C

if either:

- A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

A

is directly present on

C

.

No annotation of type

AT

is directly present on

C

, and

C

is a class and

AT

is inheritable
and

A

is present on the superclass of

C

.

AT

is a repeatable annotation type with a containing
annotation type

ATC

.

An annotation of type

ATC

is directly present on

C

and

A

is an annotation included in the result of
calling the

value

method of the directly present annotation
of type

ATC

.

A

is directly or indirectly present on

C

.

No annotation of type

AT

is directly or indirectly
present on

C

, and

C

is a class, and

AT

is
inheritable, and

A

is associated with the superclass of

C

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<A extends

Annotation

>

A

getAnnotation

​(

Class

<A> annotationType)

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

List

<? extends

AnnotationMirror

>

getAnnotationMirrors

()

Returns the annotations that are

directly present

on
this construct.

<A extends

Annotation

>

A[]

getAnnotationsByType

​(

Class

<A> annotationType)

Returns annotations that are

associated

with this construct.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

<A extends

Annotation

>

A

getAnnotation

​(

Class

<A> annotationType)

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

List

<? extends

AnnotationMirror

>

getAnnotationMirrors

()

Returns the annotations that are

directly present

on
this construct.

<A extends

Annotation

>

A[]

getAnnotationsByType

​(

Class

<A> annotationType)

Returns annotations that are

associated

with this construct.

---

#### Method Summary

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

Returns the annotations that are

directly present

on
this construct.

Returns annotations that are

associated

with this construct.

============ METHOD DETAIL ==========

- Method Detail

- getAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAnnotationMirrors()
```

Returns the annotations that are

directly present

on
this construct.

**Returns:** the annotations

directly present

on this
construct; an empty list if there are none

- getAnnotation

```java
<A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotation for the specified
annotation type if present, else

null
**See Also:** getAnnotationMirrors()

,

AnnotatedElement.getAnnotation(java.lang.Class<T>)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6.1 Annotation Type Elements

- getAnnotationsByType

```java
<A extends
Annotation
> A[] getAnnotationsByType​(
Class
<A> annotationType)
```

Returns annotations that are

associated

with this construct.

If there are no annotations associated with this construct, the
return value is an array of length 0.

The order of annotations which are directly or indirectly
present on a construct

C

is computed as if indirectly present
annotations on

C

are directly present on

C

in place of their
container annotation, in the order in which they appear in the
value element of the container annotation.

The difference between this method and

getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

, and if so, attempts to find one or more
annotations of that type by "looking through" a container annotation.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotations for the specified annotation
type if present on this construct, else an empty array
**See Also:** getAnnotationMirrors()

,

getAnnotation(Class)

,

AnnotatedElement.getAnnotationsByType(Class)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6 Annotation Types, 9.6.1 Annotation Type Elements

Method Detail

- getAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAnnotationMirrors()
```

Returns the annotations that are

directly present

on
this construct.

**Returns:** the annotations

directly present

on this
construct; an empty list if there are none

- getAnnotation

```java
<A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotation for the specified
annotation type if present, else

null
**See Also:** getAnnotationMirrors()

,

AnnotatedElement.getAnnotation(java.lang.Class<T>)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6.1 Annotation Type Elements

- getAnnotationsByType

```java
<A extends
Annotation
> A[] getAnnotationsByType​(
Class
<A> annotationType)
```

Returns annotations that are

associated

with this construct.

If there are no annotations associated with this construct, the
return value is an array of length 0.

The order of annotations which are directly or indirectly
present on a construct

C

is computed as if indirectly present
annotations on

C

are directly present on

C

in place of their
container annotation, in the order in which they appear in the
value element of the container annotation.

The difference between this method and

getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

, and if so, attempts to find one or more
annotations of that type by "looking through" a container annotation.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotations for the specified annotation
type if present on this construct, else an empty array
**See Also:** getAnnotationMirrors()

,

getAnnotation(Class)

,

AnnotatedElement.getAnnotationsByType(Class)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6 Annotation Types, 9.6.1 Annotation Type Elements

---

#### Method Detail

getAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAnnotationMirrors()
```

Returns the annotations that are

directly present

on
this construct.

**Returns:** the annotations

directly present

on this
construct; an empty list if there are none

---

#### getAnnotationMirrors

List

<? extends

AnnotationMirror

> getAnnotationMirrors()

Returns the annotations that are

directly present

on
this construct.

getAnnotation

```java
<A extends
Annotation
> A getAnnotation​(
Class
<A> annotationType)
```

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotation for the specified
annotation type if present, else

null
**See Also:** getAnnotationMirrors()

,

AnnotatedElement.getAnnotation(java.lang.Class<T>)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6.1 Annotation Type Elements

---

#### getAnnotation

<A extends

Annotation

> A getAnnotation​(

Class

<A> annotationType)

Returns this construct's annotation of the specified type if
such an annotation is

present

, else

null

.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

The annotation returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

getAnnotationsByType

```java
<A extends
Annotation
> A[] getAnnotationsByType​(
Class
<A> annotationType)
```

Returns annotations that are

associated

with this construct.

If there are no annotations associated with this construct, the
return value is an array of length 0.

The order of annotations which are directly or indirectly
present on a construct

C

is computed as if indirectly present
annotations on

C

are directly present on

C

in place of their
container annotation, in the order in which they appear in the
value element of the container annotation.

The difference between this method and

getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

, and if so, attempts to find one or more
annotations of that type by "looking through" a container annotation.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

**Type Parameters:** A

- the annotation type
**Parameters:** annotationType

- the

Class

object corresponding to
the annotation type
**Returns:** this construct's annotations for the specified annotation
type if present on this construct, else an empty array
**See Also:** getAnnotationMirrors()

,

getAnnotation(Class)

,

AnnotatedElement.getAnnotationsByType(Class)

,

EnumConstantNotPresentException

,

AnnotationTypeMismatchException

,

IncompleteAnnotationException

,

MirroredTypeException

,

MirroredTypesException
**See The Java™ Language Specification :** 9.6 Annotation Types, 9.6.1 Annotation Type Elements

---

#### getAnnotationsByType

<A extends

Annotation

> A[] getAnnotationsByType​(

Class

<A> annotationType)

Returns annotations that are

associated

with this construct.

If there are no annotations associated with this construct, the
return value is an array of length 0.

The order of annotations which are directly or indirectly
present on a construct

C

is computed as if indirectly present
annotations on

C

are directly present on

C

in place of their
container annotation, in the order in which they appear in the
value element of the container annotation.

The difference between this method and

getAnnotation(Class)

is that this method detects if its argument is a

repeatable
annotation type

, and if so, attempts to find one or more
annotations of that type by "looking through" a container annotation.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

The annotations returned by this method could contain an element
whose value is of type

Class

.
This value cannot be returned directly: information necessary to
locate and load a class (such as the class loader to use) is
not available, and the class might not be loadable at all.
Attempting to read a

Class

object by invoking the relevant
method on the returned annotation
will result in a

MirroredTypeException

,
from which the corresponding

TypeMirror

may be extracted.
Similarly, attempting to read a

Class[]

-valued element
will result in a

MirroredTypesException

.

Note:

This method is unlike others in this and related
interfaces. It operates on runtime reflective information —
representations of annotation types currently loaded into the
VM — rather than on the representations defined by and used
throughout these interfaces. Consequently, calling methods on
the returned annotation object can throw many of the exceptions
that can be thrown when calling methods on an annotation object
returned by core reflection. This method is intended for
callers that are written to operate on a known, fixed set of
annotation types.

---

