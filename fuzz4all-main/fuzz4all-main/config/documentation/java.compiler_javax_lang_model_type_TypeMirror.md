# Interface TypeMirror

**Source:** `java.compiler\javax\lang\model\type\TypeMirror.html`

### Class Description

```java
public interface
TypeMirror

extends
AnnotatedConstruct
```

Represents a type in the Java programming language.
Types include primitive types, declared types (class and interface types),
array types, type variables, and the null type.
Also represented are wildcard type arguments, the signature and
return types of executables, and pseudo-types corresponding to
packages, modules, and the keyword

void

.

Types should be compared using the utility methods in

Types

. There is no guarantee that any particular type will always
be represented by the same object.

To implement operations based on the class of an

TypeMirror

object, either use a

visitor

or use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single
object implement multiple

TypeMirror

subinterfaces.

**All Superinterfaces:** AnnotatedConstruct

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### TypeKind
getKind()

Returns the

kind

of this type.

**Returns:**
- the kind of this type

---

#### boolean equals​(
Object
obj)

Obeys the general contract of

Object.equals

.
This method does not, however, indicate whether two types represent
the same type.
Semantic comparisons of type equality should instead use

Types.isSameType(TypeMirror, TypeMirror)

.
The results of

t1.equals(t2)

and

Types.isSameType(t1, t2)

may differ.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to be compared with this type

**Returns:**
- true

if the specified object is equal to this one

**See Also:**
- Object.hashCode()

,

HashMap

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

#### String
toString()

Returns an informative string representation of this type. If
possible, the string should be of a form suitable for
representing this type in source code. Any names embedded in
the result are qualified if possible.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this type

---

#### <R,​P> R accept​(
TypeVisitor
<R,​P> v,
P p)

Applies a visitor to this type.

**Parameters:**
- v

- the visitor operating on this type
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

#### Interface TypeMirror

**All Superinterfaces:** AnnotatedConstruct

**All Known Subinterfaces:** ArrayType

,

DeclaredType

,

ErrorType

,

ExecutableType

,

IntersectionType

,

NoType

,

NullType

,

PrimitiveType

,

ReferenceType

,

TypeVariable

,

UnionType

,

WildcardType

```java
public interface
TypeMirror

extends
AnnotatedConstruct
```

Represents a type in the Java programming language.
Types include primitive types, declared types (class and interface types),
array types, type variables, and the null type.
Also represented are wildcard type arguments, the signature and
return types of executables, and pseudo-types corresponding to
packages, modules, and the keyword

void

.

Types should be compared using the utility methods in

Types

. There is no guarantee that any particular type will always
be represented by the same object.

To implement operations based on the class of an

TypeMirror

object, either use a

visitor

or use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single
object implement multiple

TypeMirror

subinterfaces.

**Since:** 1.6
**See Also:** Element

,

Types

public interface

TypeMirror

extends

AnnotatedConstruct

Represents a type in the Java programming language.
Types include primitive types, declared types (class and interface types),
array types, type variables, and the null type.
Also represented are wildcard type arguments, the signature and
return types of executables, and pseudo-types corresponding to
packages, modules, and the keyword

void

.

Types should be compared using the utility methods in

Types

. There is no guarantee that any particular type will always
be represented by the same object.

To implement operations based on the class of an

TypeMirror

object, either use a

visitor

or use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single
object implement multiple

TypeMirror

subinterfaces.

Types should be compared using the utility methods in

Types

. There is no guarantee that any particular type will always
be represented by the same object.

To implement operations based on the class of an

TypeMirror

object, either use a

visitor

or use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single
object implement multiple

TypeMirror

subinterfaces.

To implement operations based on the class of an

TypeMirror

object, either use a

visitor

or use the result of the

getKind()

method. Using

instanceof

is

not

necessarily a reliable idiom for
determining the effective class of an object in this modeling
hierarchy since an implementation may choose to have a single
object implement multiple

TypeMirror

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

TypeVisitor

<R,​P> v,
P p)

Applies a visitor to this type.

boolean

equals

​(

Object

obj)

Obeys the general contract of

Object.equals

.

TypeKind

getKind

()

Returns the

kind

of this type.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

String

toString

()

Returns an informative string representation of this type.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

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

TypeVisitor

<R,​P> v,
P p)

Applies a visitor to this type.

boolean

equals

​(

Object

obj)

Obeys the general contract of

Object.equals

.

TypeKind

getKind

()

Returns the

kind

of this type.

int

hashCode

()

Obeys the general contract of

Object.hashCode

.

String

toString

()

Returns an informative string representation of this type.

- Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

---

#### Method Summary

Applies a visitor to this type.

Obeys the general contract of

Object.equals

.

Returns the

kind

of this type.

Obeys the general contract of

Object.hashCode

.

Returns an informative string representation of this type.

Methods declared in interface javax.lang.model.

AnnotatedConstruct

getAnnotation

,

getAnnotationMirrors

,

getAnnotationsByType

---

#### Methods declared in interface javax.lang.model. AnnotatedConstruct

============ METHOD DETAIL ==========

- Method Detail

- getKind

```java
TypeKind
getKind()
```

Returns the

kind

of this type.

**Returns:** the kind of this type

- equals

```java
boolean equals​(
Object
obj)
```

Obeys the general contract of

Object.equals

.
This method does not, however, indicate whether two types represent
the same type.
Semantic comparisons of type equality should instead use

Types.isSameType(TypeMirror, TypeMirror)

.
The results of

t1.equals(t2)

and

Types.isSameType(t1, t2)

may differ.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this type
**Returns:** true

if the specified object is equal to this one
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

- toString

```java
String
toString()
```

Returns an informative string representation of this type. If
possible, the string should be of a form suitable for
representing this type in source code. Any names embedded in
the result are qualified if possible.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this type

- accept

```java
<R,​P> R accept​(
TypeVisitor
<R,​P> v,
P p)
```

Applies a visitor to this type.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this type
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

Method Detail

- getKind

```java
TypeKind
getKind()
```

Returns the

kind

of this type.

**Returns:** the kind of this type

- equals

```java
boolean equals​(
Object
obj)
```

Obeys the general contract of

Object.equals

.
This method does not, however, indicate whether two types represent
the same type.
Semantic comparisons of type equality should instead use

Types.isSameType(TypeMirror, TypeMirror)

.
The results of

t1.equals(t2)

and

Types.isSameType(t1, t2)

may differ.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this type
**Returns:** true

if the specified object is equal to this one
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

- toString

```java
String
toString()
```

Returns an informative string representation of this type. If
possible, the string should be of a form suitable for
representing this type in source code. Any names embedded in
the result are qualified if possible.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this type

- accept

```java
<R,​P> R accept​(
TypeVisitor
<R,​P> v,
P p)
```

Applies a visitor to this type.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this type
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### Method Detail

getKind

```java
TypeKind
getKind()
```

Returns the

kind

of this type.

**Returns:** the kind of this type

---

#### getKind

TypeKind

getKind()

Returns the

kind

of this type.

equals

```java
boolean equals​(
Object
obj)
```

Obeys the general contract of

Object.equals

.
This method does not, however, indicate whether two types represent
the same type.
Semantic comparisons of type equality should instead use

Types.isSameType(TypeMirror, TypeMirror)

.
The results of

t1.equals(t2)

and

Types.isSameType(t1, t2)

may differ.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to be compared with this type
**Returns:** true

if the specified object is equal to this one
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Obeys the general contract of

Object.equals

.
This method does not, however, indicate whether two types represent
the same type.
Semantic comparisons of type equality should instead use

Types.isSameType(TypeMirror, TypeMirror)

.
The results of

t1.equals(t2)

and

Types.isSameType(t1, t2)

may differ.

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

toString

```java
String
toString()
```

Returns an informative string representation of this type. If
possible, the string should be of a form suitable for
representing this type in source code. Any names embedded in
the result are qualified if possible.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this type

---

#### toString

String

toString()

Returns an informative string representation of this type. If
possible, the string should be of a form suitable for
representing this type in source code. Any names embedded in
the result are qualified if possible.

accept

```java
<R,​P> R accept​(
TypeVisitor
<R,​P> v,
P p)
```

Applies a visitor to this type.

**Type Parameters:** R

- the return type of the visitor's methods
**Type Parameters:** P

- the type of the additional parameter to the visitor's methods
**Parameters:** v

- the visitor operating on this type
**Parameters:** p

- additional parameter to the visitor
**Returns:** a visitor-specified result

---

#### accept

<R,​P> R accept​(

TypeVisitor

<R,​P> v,
P p)

Applies a visitor to this type.

---

