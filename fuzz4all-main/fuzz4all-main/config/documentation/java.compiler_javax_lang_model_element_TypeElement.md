# Interface TypeElement

**Source:** `java.compiler\javax\lang\model\element\TypeElement.html`

### Class Description

```java
public interface
TypeElement

extends
Element
,
Parameterizable
,
QualifiedNameable
```

Represents a class or interface program element. Provides access
to information about the type and its members. Note that an enum
type is a kind of class and an annotation type is a kind of
interface.

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
The distinction is most apparent with generic types,
for which a single element can define a whole
family of types. For example, the element

java.util.Set

corresponds to the parameterized types

java.util.Set<String>

and

java.util.Set<Number>

(and many others), and to the raw type

java.util.Set

.

Each method of this interface that returns a list of elements
will return them in the order that is natural for the underlying
source of program information. For example, if the underlying
source of information is Java source code, then the elements will be
returned in source code order.

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

Parameterizable

,

QualifiedNameable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<? extends
Element
> getEnclosedElements()

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

This includes any

mandated

elements such as the (implicit) default constructor
and the implicit

values

and

valueOf

methods of
an enum type.

**Specified by:**
- getEnclosedElements

in interface

Element

**Returns:**
- the enclosed elements in proper order, or an empty list if none

**See Also:**
- getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

**API Note:**
- As a particular instance of the

general accuracy requirements

and the
ordering behavior required of this interface, the list of
enclosed elements will be returned in the natural order for the
originating source of information about the type. For example,
if the information about the type is originating from a source
file, the elements will be returned in source code order.
(However, in that case the the ordering of

implicitly declared

elements, such as
default constructors, is not specified.)

**See The Java™ Language Specification :**
- 8.8.9 Default Constructor, 8.9.3 Enum Members

---

#### NestingKind
getNestingKind()

Returns the

nesting kind

of this type element.

**Returns:**
- the nesting kind of this type element

---

#### Name
getQualifiedName()

Returns the fully qualified name of this type element.
More precisely, it returns the

canonical

name.
For local and anonymous classes, which do not have canonical names,
an empty name is returned.

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

**Specified by:**
- getQualifiedName

in interface

QualifiedNameable

**Returns:**
- the fully qualified name of this class or interface, or
an empty name if none

**See Also:**
- Elements.getBinaryName(javax.lang.model.element.TypeElement)

**See The Java™ Language Specification :**
- 6.7 Fully Qualified Names and Canonical Names

---

#### Name
getSimpleName()

Returns the simple name of this type element.

For an anonymous class, an empty name is returned.

**Specified by:**
- getSimpleName

in interface

Element

**Returns:**
- the simple name of this class or interface,
an empty name for an anonymous class

**See Also:**
- PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### TypeMirror
getSuperclass()

Returns the direct superclass of this type element.
If this type element represents an interface or the class

java.lang.Object

, then a

NoType

with kind

NONE

is returned.

**Returns:**
- the direct superclass, or a

NoType

if there is none

---

#### List
<? extends
TypeMirror
> getInterfaces()

Returns the interface types directly implemented by this class
or extended by this interface.

**Returns:**
- the interface types directly implemented by this class
or extended by this interface, or an empty list if there are none

---

#### List
<? extends
TypeParameterElement
> getTypeParameters()

Returns the formal type parameters of this type element
in declaration order.

**Specified by:**
- getTypeParameters

in interface

Parameterizable

**Returns:**
- the formal type parameters, or an empty list
if there are none

---

#### Element
getEnclosingElement()

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

**Specified by:**
- getEnclosingElement

in interface

Element

**Returns:**
- the package of a top-level type, the immediately
lexically enclosing element for a nested type

**See Also:**
- Elements.getPackageOf(javax.lang.model.element.Element)

---

### Additional Sections

#### Interface TypeElement

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

Parameterizable

,

QualifiedNameable

```java
public interface
TypeElement

extends
Element
,
Parameterizable
,
QualifiedNameable
```

Represents a class or interface program element. Provides access
to information about the type and its members. Note that an enum
type is a kind of class and an annotation type is a kind of
interface.

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
The distinction is most apparent with generic types,
for which a single element can define a whole
family of types. For example, the element

java.util.Set

corresponds to the parameterized types

java.util.Set<String>

and

java.util.Set<Number>

(and many others), and to the raw type

java.util.Set

.

Each method of this interface that returns a list of elements
will return them in the order that is natural for the underlying
source of program information. For example, if the underlying
source of information is Java source code, then the elements will be
returned in source code order.

**Since:** 1.6
**See Also:** DeclaredType

public interface

TypeElement

extends

Element

,

Parameterizable

,

QualifiedNameable

Represents a class or interface program element. Provides access
to information about the type and its members. Note that an enum
type is a kind of class and an annotation type is a kind of
interface.

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
The distinction is most apparent with generic types,
for which a single element can define a whole
family of types. For example, the element

java.util.Set

corresponds to the parameterized types

java.util.Set<String>

and

java.util.Set<Number>

(and many others), and to the raw type

java.util.Set

.

Each method of this interface that returns a list of elements
will return them in the order that is natural for the underlying
source of program information. For example, if the underlying
source of information is Java source code, then the elements will be
returned in source code order.

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
The distinction is most apparent with generic types,
for which a single element can define a whole
family of types. For example, the element

java.util.Set

corresponds to the parameterized types

java.util.Set<String>

and

java.util.Set<Number>

(and many others), and to the raw type

java.util.Set

.

Each method of this interface that returns a list of elements
will return them in the order that is natural for the underlying
source of program information. For example, if the underlying
source of information is Java source code, then the elements will be
returned in source code order.

Each method of this interface that returns a list of elements
will return them in the order that is natural for the underlying
source of program information. For example, if the underlying
source of information is Java source code, then the elements will be
returned in source code order.

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

Element

>

getEnclosedElements

()

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

Element

getEnclosingElement

()

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

List

<? extends

TypeMirror

>

getInterfaces

()

Returns the interface types directly implemented by this class
or extended by this interface.

NestingKind

getNestingKind

()

Returns the

nesting kind

of this type element.

Name

getQualifiedName

()

Returns the fully qualified name of this type element.

Name

getSimpleName

()

Returns the simple name of this type element.

TypeMirror

getSuperclass

()

Returns the direct superclass of this type element.

List

<? extends

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of this type element
in declaration order.

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

getKind

,

getModifiers

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

Element

>

getEnclosedElements

()

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

Element

getEnclosingElement

()

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

List

<? extends

TypeMirror

>

getInterfaces

()

Returns the interface types directly implemented by this class
or extended by this interface.

NestingKind

getNestingKind

()

Returns the

nesting kind

of this type element.

Name

getQualifiedName

()

Returns the fully qualified name of this type element.

Name

getSimpleName

()

Returns the simple name of this type element.

TypeMirror

getSuperclass

()

Returns the direct superclass of this type element.

List

<? extends

TypeParameterElement

>

getTypeParameters

()

Returns the formal type parameters of this type element
in declaration order.

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

getKind

,

getModifiers

,

hashCode

---

#### Method Summary

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

Returns the interface types directly implemented by this class
or extended by this interface.

Returns the

nesting kind

of this type element.

Returns the fully qualified name of this type element.

Returns the simple name of this type element.

Returns the direct superclass of this type element.

Returns the formal type parameters of this type element
in declaration order.

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

getKind

,

getModifiers

,

hashCode

---

#### Methods declared in interface javax.lang.model.element. Element

============ METHOD DETAIL ==========

- Method Detail

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

This includes any

mandated

elements such as the (implicit) default constructor
and the implicit

values

and

valueOf

methods of
an enum type.

**Specified by:** getEnclosedElements

in interface

Element
**API Note:** As a particular instance of the

general accuracy requirements

and the
ordering behavior required of this interface, the list of
enclosed elements will be returned in the natural order for the
originating source of information about the type. For example,
if the information about the type is originating from a source
file, the elements will be returned in source code order.
(However, in that case the the ordering of

implicitly declared

elements, such as
default constructors, is not specified.)
**Returns:** the enclosed elements in proper order, or an empty list if none
**See Also:** getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members

- getNestingKind

```java
NestingKind
getNestingKind()
```

Returns the

nesting kind

of this type element.

**Returns:** the nesting kind of this type element

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this type element.
More precisely, it returns the

canonical

name.
For local and anonymous classes, which do not have canonical names,
an empty name is returned.

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**Returns:** the fully qualified name of this class or interface, or
an empty name if none
**See Also:** Elements.getBinaryName(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type element.

For an anonymous class, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this class or interface,
an empty name for an anonymous class
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getSuperclass

```java
TypeMirror
getSuperclass()
```

Returns the direct superclass of this type element.
If this type element represents an interface or the class

java.lang.Object

, then a

NoType

with kind

NONE

is returned.

**Returns:** the direct superclass, or a

NoType

if there is none

- getInterfaces

```java
List
<? extends
TypeMirror
> getInterfaces()
```

Returns the interface types directly implemented by this class
or extended by this interface.

**Returns:** the interface types directly implemented by this class
or extended by this interface, or an empty list if there are none

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this type element
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the package of a top-level type, the immediately
lexically enclosing element for a nested type
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

Method Detail

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

This includes any

mandated

elements such as the (implicit) default constructor
and the implicit

values

and

valueOf

methods of
an enum type.

**Specified by:** getEnclosedElements

in interface

Element
**API Note:** As a particular instance of the

general accuracy requirements

and the
ordering behavior required of this interface, the list of
enclosed elements will be returned in the natural order for the
originating source of information about the type. For example,
if the information about the type is originating from a source
file, the elements will be returned in source code order.
(However, in that case the the ordering of

implicitly declared

elements, such as
default constructors, is not specified.)
**Returns:** the enclosed elements in proper order, or an empty list if none
**See Also:** getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members

- getNestingKind

```java
NestingKind
getNestingKind()
```

Returns the

nesting kind

of this type element.

**Returns:** the nesting kind of this type element

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this type element.
More precisely, it returns the

canonical

name.
For local and anonymous classes, which do not have canonical names,
an empty name is returned.

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**Returns:** the fully qualified name of this class or interface, or
an empty name if none
**See Also:** Elements.getBinaryName(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type element.

For an anonymous class, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this class or interface,
an empty name for an anonymous class
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getSuperclass

```java
TypeMirror
getSuperclass()
```

Returns the direct superclass of this type element.
If this type element represents an interface or the class

java.lang.Object

, then a

NoType

with kind

NONE

is returned.

**Returns:** the direct superclass, or a

NoType

if there is none

- getInterfaces

```java
List
<? extends
TypeMirror
> getInterfaces()
```

Returns the interface types directly implemented by this class
or extended by this interface.

**Returns:** the interface types directly implemented by this class
or extended by this interface, or an empty list if there are none

- getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this type element
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the package of a top-level type, the immediately
lexically enclosing element for a nested type
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### Method Detail

getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

This includes any

mandated

elements such as the (implicit) default constructor
and the implicit

values

and

valueOf

methods of
an enum type.

**Specified by:** getEnclosedElements

in interface

Element
**API Note:** As a particular instance of the

general accuracy requirements

and the
ordering behavior required of this interface, the list of
enclosed elements will be returned in the natural order for the
originating source of information about the type. For example,
if the information about the type is originating from a source
file, the elements will be returned in source code order.
(However, in that case the the ordering of

implicitly declared

elements, such as
default constructors, is not specified.)
**Returns:** the enclosed elements in proper order, or an empty list if none
**See Also:** getEnclosedElements()

,

PackageElement.getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 8.8.9 Default Constructor, 8.9.3 Enum Members

---

#### getEnclosedElements

List

<? extends

Element

> getEnclosedElements()

Returns the fields, methods, constructors, and member types
that are directly declared in this class or interface.

This includes any

mandated

elements such as the (implicit) default constructor
and the implicit

values

and

valueOf

methods of
an enum type.

getNestingKind

```java
NestingKind
getNestingKind()
```

Returns the

nesting kind

of this type element.

**Returns:** the nesting kind of this type element

---

#### getNestingKind

NestingKind

getNestingKind()

Returns the

nesting kind

of this type element.

getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this type element.
More precisely, it returns the

canonical

name.
For local and anonymous classes, which do not have canonical names,
an empty name is returned.

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**Returns:** the fully qualified name of this class or interface, or
an empty name if none
**See Also:** Elements.getBinaryName(javax.lang.model.element.TypeElement)
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

---

#### getQualifiedName

Name

getQualifiedName()

Returns the fully qualified name of this type element.
More precisely, it returns the

canonical

name.
For local and anonymous classes, which do not have canonical names,
an empty name is returned.

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

The name of a generic type does not include any reference
to its formal type parameters.
For example, the fully qualified name of the interface

java.util.Set<E>

is "

java.util.Set

".
Nested types use "

.

" as a separator, as in
"

java.util.Map.Entry

".

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this type element.

For an anonymous class, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this class or interface,
an empty name for an anonymous class
**See Also:** PackageElement.getSimpleName()

,

ExecutableElement.getSimpleName()

,

getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### getSimpleName

Name

getSimpleName()

Returns the simple name of this type element.

For an anonymous class, an empty name is returned.

getSuperclass

```java
TypeMirror
getSuperclass()
```

Returns the direct superclass of this type element.
If this type element represents an interface or the class

java.lang.Object

, then a

NoType

with kind

NONE

is returned.

**Returns:** the direct superclass, or a

NoType

if there is none

---

#### getSuperclass

TypeMirror

getSuperclass()

Returns the direct superclass of this type element.
If this type element represents an interface or the class

java.lang.Object

, then a

NoType

with kind

NONE

is returned.

getInterfaces

```java
List
<? extends
TypeMirror
> getInterfaces()
```

Returns the interface types directly implemented by this class
or extended by this interface.

**Returns:** the interface types directly implemented by this class
or extended by this interface, or an empty list if there are none

---

#### getInterfaces

List

<? extends

TypeMirror

> getInterfaces()

Returns the interface types directly implemented by this class
or extended by this interface.

getTypeParameters

```java
List
<? extends
TypeParameterElement
> getTypeParameters()
```

Returns the formal type parameters of this type element
in declaration order.

**Specified by:** getTypeParameters

in interface

Parameterizable
**Returns:** the formal type parameters, or an empty list
if there are none

---

#### getTypeParameters

List

<? extends

TypeParameterElement

> getTypeParameters()

Returns the formal type parameters of this type element
in declaration order.

getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the package of a top-level type, the immediately
lexically enclosing element for a nested type
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### getEnclosingElement

Element

getEnclosingElement()

Returns the package of a top-level type and returns the
immediately lexically enclosing element for a

nested

type.

---

