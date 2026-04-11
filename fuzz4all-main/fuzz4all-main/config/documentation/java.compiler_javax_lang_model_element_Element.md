# Interface Element

**Source:** `java.compiler\javax\lang\model\element\Element.html`

### Class Description

```java
public interface
Element

extends
AnnotatedConstruct
```

Represents a program element such as a module, package, class, or method.
Each element represents a static, language-level construct
(and not, for example, a runtime construct of the virtual machine).

Elements should be compared using the

equals(Object)

method. There is no guarantee that any particular element will
always be represented by the same object.

To implement operations based on the class of an

Element

object, either use a

visitor

or
use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single object
implement multiple

Element

subinterfaces.

**All Superinterfaces:** AnnotatedConstruct

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeMirror
asType()

Returns the type defined by this element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

**Returns:**
- the type defined by this element

**See Also:**
- Types

---

#### ElementKind
getKind()

Returns the

kind

of this element.

**Returns:**
- the kind of this element

---

#### Set
<
Modifier
> getModifiers()

Returns the modifiers of this element, excluding annotations.
Implicit modifiers, such as the

public

and

static

modifiers of interface members, are included.

**Returns:**
- the modifiers of this element, or an empty set if there are none

---

#### Name
getSimpleName()

Returns the simple (unqualified) name of this element. The
name of a generic type does not include any reference to its
formal type parameters.

For example, the simple name of the type element

java.util.Set<E>

is

"Set"

.

If this element represents an unnamed

package

or unnamed

module

, an empty name is returned.

If it represents a

constructor

, the name "

<init>

" is returned. If it
represents a

static
initializer

, the name "

<clinit>

" is returned.

If it represents an

anonymous class

or

instance initializer

, an empty name is returned.

**Returns:**
- the simple name of this element

**See Also:**
- PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### Element
getEnclosingElement()

Returns the innermost element
within which this element is, loosely speaking, enclosed.

- If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

**Returns:**
- the enclosing element, or

null

if there is none

**See Also:**
- Elements.getPackageOf(javax.lang.model.element.Element)

---

#### List
<? extends
Element
> getEnclosedElements()

Returns the elements that are, loosely speaking, directly
enclosed by this element.

A

class or
interface

is considered to enclose the fields, methods,
constructors, and member types that it directly declares.

A

package

encloses the top-level classes and interfaces within it, but is
not considered to enclose subpackages.

A

module

encloses packages within it.

Enclosed elements may include implicitly declared

mandated

elements.

Other kinds of elements are not currently considered to enclose
any elements; however, that may change as this API or the
programming language evolves.

**Returns:**
- the enclosed elements, or an empty list if none

**See Also:**
- TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

**API Note:**
- Elements of certain kinds can be isolated using
methods in

ElementFilter

.

**See The Java™ Language Specification :**
- 8.8.9 Default Constructor, 8.9 Enums

---

#### boolean equals​(
Object
obj)

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared with this element

**Returns:**
- true

if the specified object represents the same
element as this

**See Also:**
- Object.hashCode()

,

HashMap

**API Note:**
- The identity of an element involves implicit state
not directly accessible from the element's methods, including
state about the presence of unrelated types. Element objects
created by different implementations of these interfaces should

not

be expected to be equal even if "the same"
element is being modeled; this is analogous to the inequality
of

Class

objects for the same class file loaded through
different class loaders.

---

#### int hashCode()

Obeys the general contract of

Object.hashCode

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- equals(java.lang.Object)

---

#### List
<? extends
AnnotationMirror
> getAnnotationMirrors()

Returns the annotations that are

directly present

on
this construct.

To get inherited annotations as well, use

getAllAnnotationMirrors

.

**Specified by:**
- getAnnotationMirrors

in interface

AnnotatedConstruct

**Returns:**
- the annotations

directly present

on this
construct; an empty list if there are none

**Since:**
- 1.6

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

**Specified by:**
- getAnnotation

in interface

AnnotatedConstruct

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
- AnnotatedConstruct.getAnnotationMirrors()

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

**Since:**
- 1.6

**Type Parameters:**
- A

- the annotation type

---

#### <R,​P> R accept​(
ElementVisitor
<R,​P> v,
P p)

Applies a visitor to this element.

**Parameters:**
- v

- the visitor operating on this element
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

#### Interface Element

**All Superinterfaces:** AnnotatedConstruct

**All Known Subinterfaces:** ExecutableElement

,

ModuleElement

,

PackageElement

,

Parameterizable

,

QualifiedNameable

,

TypeElement

,

TypeParameterElement

,

VariableElement

```java
public interface
Element

extends
AnnotatedConstruct
```

Represents a program element such as a module, package, class, or method.
Each element represents a static, language-level construct
(and not, for example, a runtime construct of the virtual machine).

Elements should be compared using the

equals(Object)

method. There is no guarantee that any particular element will
always be represented by the same object.

To implement operations based on the class of an

Element

object, either use a

visitor

or
use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single object
implement multiple

Element

subinterfaces.

**Since:** 1.6
**See Also:** Elements

,

TypeMirror

public interface

Element

extends

AnnotatedConstruct

Represents a program element such as a module, package, class, or method.
Each element represents a static, language-level construct
(and not, for example, a runtime construct of the virtual machine).

Elements should be compared using the

equals(Object)

method. There is no guarantee that any particular element will
always be represented by the same object.

To implement operations based on the class of an

Element

object, either use a

visitor

or
use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single object
implement multiple

Element

subinterfaces.

Elements should be compared using the

equals(Object)

method. There is no guarantee that any particular element will
always be represented by the same object.

To implement operations based on the class of an

Element

object, either use a

visitor

or
use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single object
implement multiple

Element

subinterfaces.

To implement operations based on the class of an

Element

object, either use a

visitor

or
use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single object
implement multiple

Element

subinterfaces.

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

ElementVisitor

<R,​P> v,
P p)

Applies a visitor to this element.

TypeMirror

asType

()

Returns the type defined by this element.

boolean

equals

​(

Object

obj)

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

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

List

<? extends

Element

>

getEnclosedElements

()

Returns the elements that are, loosely speaking, directly
enclosed by this element.

Element

getEnclosingElement

()

Returns the innermost element
within which this element is, loosely speaking, enclosed.

ElementKind

getKind

()

Returns the

kind

of this element.

Set

<

Modifier

>

getModifiers

()

Returns the modifiers of this element, excluding annotations.

Name

getSimpleName

()

Returns the simple (unqualified) name of this element.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

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

ElementVisitor

<R,​P> v,
P p)

Applies a visitor to this element.

TypeMirror

asType

()

Returns the type defined by this element.

boolean

equals

​(

Object

obj)

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

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

List

<? extends

Element

>

getEnclosedElements

()

Returns the elements that are, loosely speaking, directly
enclosed by this element.

Element

getEnclosingElement

()

Returns the innermost element
within which this element is, loosely speaking, enclosed.

ElementKind

getKind

()

Returns the

kind

of this element.

Set

<

Modifier

>

getModifiers

()

Returns the modifiers of this element, excluding annotations.

Name

getSimpleName

()

Returns the simple (unqualified) name of this element.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

---

#### Method Summary

Applies a visitor to this element.

Returns the type defined by this element.

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

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

Returns the elements that are, loosely speaking, directly
enclosed by this element.

Returns the innermost element
within which this element is, loosely speaking, enclosed.

Returns the

kind

of this element.

Returns the modifiers of this element, excluding annotations.

Returns the simple (unqualified) name of this element.

Obeys the general contract of

Object.hashCode

.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

============ METHOD DETAIL ==========

- Method Detail

- asType

```java
TypeMirror
asType()
```

Returns the type defined by this element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

**Returns:** the type defined by this element
**See Also:** Types

- getKind

```java
ElementKind
getKind()
```

Returns the

kind

of this element.

**Returns:** the kind of this element

- getModifiers

```java
Set
<
Modifier
> getModifiers()
```

Returns the modifiers of this element, excluding annotations.
Implicit modifiers, such as the

public

and

static

modifiers of interface members, are included.

**Returns:** the modifiers of this element, or an empty set if there are none

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple (unqualified) name of this element. The
name of a generic type does not include any reference to its
formal type parameters.

For example, the simple name of the type element

java.util.Set<E>

is

"Set"

.

If this element represents an unnamed

package

or unnamed

module

, an empty name is returned.

If it represents a

constructor

, the name "

<init>

" is returned. If it
represents a

static
initializer

, the name "

<clinit>

" is returned.

If it represents an

anonymous class

or

instance initializer

, an empty name is returned.

**Returns:** the simple name of this element
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the innermost element
within which this element is, loosely speaking, enclosed.

- If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

**Returns:** the enclosing element, or

null

if there is none
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the elements that are, loosely speaking, directly
enclosed by this element.

A

class or
interface

is considered to enclose the fields, methods,
constructors, and member types that it directly declares.

A

package

encloses the top-level classes and interfaces within it, but is
not considered to enclose subpackages.

A

module

encloses packages within it.

Enclosed elements may include implicitly declared

mandated

elements.

Other kinds of elements are not currently considered to enclose
any elements; however, that may change as this API or the
programming language evolves.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Returns:** the enclosed elements, or an empty list if none
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9 Enums

- equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

**Overrides:** equals

in class

Object
**API Note:** The identity of an element involves implicit state
not directly accessible from the element's methods, including
state about the presence of unrelated types. Element objects
created by different implementations of these interfaces should

not

be expected to be equal even if "the same"
element is being modeled; this is analogous to the inequality
of

Class

objects for the same class file loaded through
different class loaders.
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
element as this
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

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

To get inherited annotations as well, use

getAllAnnotationMirrors

.

**Specified by:** getAnnotationMirrors

in interface

AnnotatedConstruct
**Returns:** the annotations

directly present

on this
construct; an empty list if there are none
**Since:** 1.6

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

**Specified by:** getAnnotation

in interface

AnnotatedConstruct
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
**Since:** 1.6
**See Also:** AnnotatedConstruct.getAnnotationMirrors()

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

- accept

```java
<R,​P> R accept​(
ElementVisitor
<R,​P> v,
P p)
```

Applies a visitor to this element.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this element
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

Method Detail

- asType

```java
TypeMirror
asType()
```

Returns the type defined by this element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

**Returns:** the type defined by this element
**See Also:** Types

- getKind

```java
ElementKind
getKind()
```

Returns the

kind

of this element.

**Returns:** the kind of this element

- getModifiers

```java
Set
<
Modifier
> getModifiers()
```

Returns the modifiers of this element, excluding annotations.
Implicit modifiers, such as the

public

and

static

modifiers of interface members, are included.

**Returns:** the modifiers of this element, or an empty set if there are none

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple (unqualified) name of this element. The
name of a generic type does not include any reference to its
formal type parameters.

For example, the simple name of the type element

java.util.Set<E>

is

"Set"

.

If this element represents an unnamed

package

or unnamed

module

, an empty name is returned.

If it represents a

constructor

, the name "

<init>

" is returned. If it
represents a

static
initializer

, the name "

<clinit>

" is returned.

If it represents an

anonymous class

or

instance initializer

, an empty name is returned.

**Returns:** the simple name of this element
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the innermost element
within which this element is, loosely speaking, enclosed.

- If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

**Returns:** the enclosing element, or

null

if there is none
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the elements that are, loosely speaking, directly
enclosed by this element.

A

class or
interface

is considered to enclose the fields, methods,
constructors, and member types that it directly declares.

A

package

encloses the top-level classes and interfaces within it, but is
not considered to enclose subpackages.

A

module

encloses packages within it.

Enclosed elements may include implicitly declared

mandated

elements.

Other kinds of elements are not currently considered to enclose
any elements; however, that may change as this API or the
programming language evolves.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Returns:** the enclosed elements, or an empty list if none
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9 Enums

- equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

**Overrides:** equals

in class

Object
**API Note:** The identity of an element involves implicit state
not directly accessible from the element's methods, including
state about the presence of unrelated types. Element objects
created by different implementations of these interfaces should

not

be expected to be equal even if "the same"
element is being modeled; this is analogous to the inequality
of

Class

objects for the same class file loaded through
different class loaders.
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
element as this
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

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

To get inherited annotations as well, use

getAllAnnotationMirrors

.

**Specified by:** getAnnotationMirrors

in interface

AnnotatedConstruct
**Returns:** the annotations

directly present

on this
construct; an empty list if there are none
**Since:** 1.6

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

**Specified by:** getAnnotation

in interface

AnnotatedConstruct
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
**Since:** 1.6
**See Also:** AnnotatedConstruct.getAnnotationMirrors()

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

- accept

```java
<R,​P> R accept​(
ElementVisitor
<R,​P> v,
P p)
```

Applies a visitor to this element.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this element
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### Method Detail

asType

```java
TypeMirror
asType()
```

Returns the type defined by this element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

**Returns:** the type defined by this element
**See Also:** Types

---

#### asType

TypeMirror

asType()

Returns the type defined by this element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

A generic element defines a family of types, not just one.
If this is a generic element, a

prototypical

type is
returned. This is the element's invocation on the
type variables corresponding to its own formal type parameters.
For example,
for the generic class element

C<N extends Number>

,
the parameterized type

C<N>

is returned.
The

Types

utility interface has more general methods
for obtaining the full range of types defined by an element.

getKind

```java
ElementKind
getKind()
```

Returns the

kind

of this element.

**Returns:** the kind of this element

---

#### getKind

ElementKind

getKind()

Returns the

kind

of this element.

getModifiers

```java
Set
<
Modifier
> getModifiers()
```

Returns the modifiers of this element, excluding annotations.
Implicit modifiers, such as the

public

and

static

modifiers of interface members, are included.

**Returns:** the modifiers of this element, or an empty set if there are none

---

#### getModifiers

Set

<

Modifier

> getModifiers()

Returns the modifiers of this element, excluding annotations.
Implicit modifiers, such as the

public

and

static

modifiers of interface members, are included.

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple (unqualified) name of this element. The
name of a generic type does not include any reference to its
formal type parameters.

For example, the simple name of the type element

java.util.Set<E>

is

"Set"

.

If this element represents an unnamed

package

or unnamed

module

, an empty name is returned.

If it represents a

constructor

, the name "

<init>

" is returned. If it
represents a

static
initializer

, the name "

<clinit>

" is returned.

If it represents an

anonymous class

or

instance initializer

, an empty name is returned.

**Returns:** the simple name of this element
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### getSimpleName

Name

getSimpleName()

Returns the simple (unqualified) name of this element. The
name of a generic type does not include any reference to its
formal type parameters.

For example, the simple name of the type element

java.util.Set<E>

is

"Set"

.

If this element represents an unnamed

package

or unnamed

module

, an empty name is returned.

If it represents a

constructor

, the name "

<init>

" is returned. If it
represents a

static
initializer

, the name "

<clinit>

" is returned.

If it represents an

anonymous class

or

instance initializer

, an empty name is returned.

getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the innermost element
within which this element is, loosely speaking, enclosed.

- If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

**Returns:** the enclosing element, or

null

if there is none
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### getEnclosingElement

Element

getEnclosingElement()

Returns the innermost element
within which this element is, loosely speaking, enclosed.

- If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

If this element is one whose declaration is lexically enclosed
immediately within the declaration of another element, that other
element is returned.

If this is a

top-level type

, its package is returned.

If this is a

package

, its module is
returned if such a module exists. Otherwise,

null

is returned.

If this is a

type parameter

,

the
generic element

of the type parameter is returned.

If this is a

method or constructor
parameter

,

the executable
element

which declares the parameter is returned.

If this is a

module

,

null

is returned.

getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the elements that are, loosely speaking, directly
enclosed by this element.

A

class or
interface

is considered to enclose the fields, methods,
constructors, and member types that it directly declares.

A

package

encloses the top-level classes and interfaces within it, but is
not considered to enclose subpackages.

A

module

encloses packages within it.

Enclosed elements may include implicitly declared

mandated

elements.

Other kinds of elements are not currently considered to enclose
any elements; however, that may change as this API or the
programming language evolves.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Returns:** the enclosed elements, or an empty list if none
**See Also:** TypeElement.getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9 Enums

---

#### getEnclosedElements

List

<? extends

Element

> getEnclosedElements()

Returns the elements that are, loosely speaking, directly
enclosed by this element.

A

class or
interface

is considered to enclose the fields, methods,
constructors, and member types that it directly declares.

A

package

encloses the top-level classes and interfaces within it, but is
not considered to enclose subpackages.

A

module

encloses packages within it.

Enclosed elements may include implicitly declared

mandated

elements.

Other kinds of elements are not currently considered to enclose
any elements; however, that may change as this API or the
programming language evolves.

equals

```java
boolean equals​(
Object
obj)
```

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

**Overrides:** equals

in class

Object
**API Note:** The identity of an element involves implicit state
not directly accessible from the element's methods, including
state about the presence of unrelated types. Element objects
created by different implementations of these interfaces should

not

be expected to be equal even if "the same"
element is being modeled; this is analogous to the inequality
of

Class

objects for the same class file loaded through
different class loaders.
**Parameters:** obj

- the object to be compared with this element
**Returns:** true

if the specified object represents the same
element as this
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Returns

true

if the argument represents the same
element as

this

, or

false

otherwise.

hashCode

```java
int hashCode()
```

Obeys the general contract of

Object.hashCode

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** equals(java.lang.Object)

---

#### hashCode

int hashCode()

Obeys the general contract of

Object.hashCode

.

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

To get inherited annotations as well, use

getAllAnnotationMirrors

.

**Specified by:** getAnnotationMirrors

in interface

AnnotatedConstruct
**Returns:** the annotations

directly present

on this
construct; an empty list if there are none
**Since:** 1.6

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

To get inherited annotations as well, use

getAllAnnotationMirrors

.

To get inherited annotations as well, use

getAllAnnotationMirrors

.

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

**Specified by:** getAnnotation

in interface

AnnotatedConstruct
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
**Since:** 1.6
**See Also:** AnnotatedConstruct.getAnnotationMirrors()

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

accept

```java
<R,​P> R accept​(
ElementVisitor
<R,​P> v,
P p)
```

Applies a visitor to this element.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this element
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### accept

<R,​P> R accept​(

ElementVisitor

<R,​P> v,
P p)

Applies a visitor to this element.

---

