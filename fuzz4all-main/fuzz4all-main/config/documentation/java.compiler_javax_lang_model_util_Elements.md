# Interface Elements

**Source:** `java.compiler\javax\lang\model\util\Elements.html`

### Class Description

```java
public interface
Elements
```

Utility methods for operating on program elements.

Compatibility Note:

Methods may be added to this interface
in future releases of the platform.

**Since:** 1.6
**See Also:** ProcessingEnvironment.getElementUtils()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### PackageElement
getPackageElement​(
CharSequence
name)

Returns a package given its fully qualified name if the package is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching packages.

**Parameters:**
- name

- fully qualified package name, or an empty string for an unnamed package

**Returns:**
- the specified package, or

null

if it cannot be uniquely found

---

#### default
PackageElement
getPackageElement​(
ModuleElement
module,

CharSequence
name)

Returns a package given its fully qualified name, as seen from the given module.

**Parameters:**
- name

- fully qualified package name, or an empty string for an unnamed package
- module

- module relative to which the lookup should happen

**Returns:**
- the specified package, or

null

if it cannot be found

**See Also:**
- getAllPackageElements(java.lang.CharSequence)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

null

.

---

#### default
Set
<? extends
PackageElement
> getAllPackageElements​(
CharSequence
name)

Returns all package elements with the given canonical name.

There may be more than one package element with the same canonical
name if the package elements are in different modules.

**Parameters:**
- name

- the canonical name

**Returns:**
- the package elements, or an empty set if no package with the name can be found

**See Also:**
- getPackageElement(ModuleElement, CharSequence)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getPackageElement(name)

is
called passing through the name argument. If

getPackageElement(name)

is

null

, an empty set of
package elements is returned; otherwise, a single-element set
with the found package element is returned. If the set of
modules is nonempty, the modules are iterated over and any
non-

null

results of

getPackageElement(module, name)

are accumulated into a
set. The set is then returned.

---

#### TypeElement
getTypeElement​(
CharSequence
name)

Returns a type element given its canonical name if the type element is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching
type elements.

**Parameters:**
- name

- the canonical name

**Returns:**
- the named type element, or

null

if it cannot be uniquely found

---

#### default
TypeElement
getTypeElement​(
ModuleElement
module,

CharSequence
name)

Returns a type element given its canonical name, as seen from the given module.

**Parameters:**
- name

- the canonical name
- module

- module relative to which the lookup should happen

**Returns:**
- the named type element, or

null

if it cannot be found

**See Also:**
- getAllTypeElements(java.lang.CharSequence)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

null

.

---

#### default
Set
<? extends
TypeElement
> getAllTypeElements​(
CharSequence
name)

Returns all type elements with the given canonical name.

There may be more than one type element with the same canonical
name if the type elements are in different modules.

**Parameters:**
- name

- the canonical name

**Returns:**
- the type elements, or an empty set if no type with the name can be found

**See Also:**
- getTypeElement(ModuleElement, CharSequence)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getTypeElement(name)

is called
passing through the name argument. If

getTypeElement(name)

is

null

, an empty set of type
elements is returned; otherwise, a single-element set with the
found type element is returned. If the set of modules is
nonempty, the modules are iterated over and any non-

null

results of

getTypeElement(module, name)

are accumulated
into a set. The set is then returned.

---

#### default
ModuleElement
getModuleElement​(
CharSequence
name)

Returns a module element given its fully qualified name.

If the named module cannot be found,

null

is
returned. One situation where a module cannot be found is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Parameters:**
- name

- the name

**Returns:**
- the named module element, or

null

if it cannot be found

**See Also:**
- getAllModuleElements()

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

null

.

---

#### default
Set
<? extends
ModuleElement
> getAllModuleElements()

Returns all module elements in the current environment.

If no modules are present, an empty set is returned. One
situation where no modules are present occurs when the
environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Returns:**
- the known module elements, or an empty set if there are no modules

**See Also:**
- getModuleElement(CharSequence)

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns
an empty set.

---

#### Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValuesWithDefaults​(
AnnotationMirror
a)

Returns the values of an annotation's elements, including defaults.

**Parameters:**
- a

- annotation to examine

**Returns:**
- the values of the annotation's elements, including defaults

**See Also:**
- AnnotationMirror.getElementValues()

---

#### String
getDocComment​(
Element
e)

Returns the text of the documentation ("Javadoc")
comment of an element.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

**Parameters:**
- e

- the element being examined

**Returns:**
- the documentation comment of the element, or

null

if there is none

**See The Java™ Language Specification :**
- 3.6 White Space

---

#### boolean isDeprecated​(
Element
e)

Returns

true

if the element is deprecated,

false

otherwise.

**Parameters:**
- e

- the element being examined

**Returns:**
- true

if the element is deprecated,

false

otherwise

---

#### default
Elements.Origin
getOrigin​(
Element
e)

Returns the

origin

of the given element.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

**Parameters:**
- e

- the element being examined

**Returns:**
- the origin of the given element

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

EXPLICIT

.

---

#### default
Elements.Origin
getOrigin​(
AnnotatedConstruct
c,

AnnotationMirror
a)

Returns the

origin

of the given annotation mirror.

An annotation mirror is

mandated

if it is an implicitly declared

container annotation

used to hold repeated annotations of a repeatable annotation
type.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

**Parameters:**
- c

- the construct the annotation mirror modifies
- a

- the annotation mirror being examined

**Returns:**
- the origin of the given annotation mirror

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

EXPLICIT

.

**See The Java™ Language Specification :**
- 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

---

#### default
Elements.Origin
getOrigin​(
ModuleElement
m,

ModuleElement.Directive
directive)

Returns the

origin

of the given module directive.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

**Parameters:**
- m

- the module of the directive
- directive

- the module directive being examined

**Returns:**
- the origin of the given directive

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

EXPLICIT

.

---

#### default boolean isBridge​(
ExecutableElement
e)

Returns

true

if the executable element is a bridge
method,

false

otherwise.

**Parameters:**
- e

- the executable being examined

**Returns:**
- true

if the executable element is a bridge
method,

false

otherwise

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

false

.

---

#### Name
getBinaryName​(
TypeElement
type)

Returns the

binary name

of a type element.

**Parameters:**
- type

- the type element being examined

**Returns:**
- the binary name

**See Also:**
- TypeElement.getQualifiedName()

**See The Java™ Language Specification :**
- 13.1 The Form of a Binary

---

#### PackageElement
getPackageOf​(
Element
type)

Returns the package of an element. The package of a package is
itself.

**Parameters:**
- type

- the element being examined

**Returns:**
- the package of an element

---

#### default
ModuleElement
getModuleOf​(
Element
type)

Returns the module of an element. The module of a module is
itself.
If there is no module for the element, null is returned. One situation where there is
no module for an element is if the environment does not include modules, such as
an annotation processing environment configured for
a

source version

without modules.

**Parameters:**
- type

- the element being examined

**Returns:**
- the module of an element

**Since:**
- 9

**Implementation Requirements:**
- The default implementation of this method returns

null

.

---

#### List
<? extends
Element
> getAllMembers​(
TypeElement
type)

Returns all members of a type element, whether inherited or
declared directly. For a class the result also includes its
constructors, but not local or anonymous classes.

**Parameters:**
- type

- the type being examined

**Returns:**
- all members of the type

**See Also:**
- Element.getEnclosedElements()

**API Note:**
- Elements of certain kinds can be isolated using
methods in

ElementFilter

.

---

#### List
<? extends
AnnotationMirror
> getAllAnnotationMirrors​(
Element
e)

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

**Parameters:**
- e

- the element being examined

**Returns:**
- all annotations of the element

**See Also:**
- Element.getAnnotationMirrors()

,

AnnotatedConstruct

---

#### boolean hides​(
Element
hider,

Element
hidden)

Tests whether one type, method, or field hides another.

**Parameters:**
- hider

- the first element
- hidden

- the second element

**Returns:**
- true

if and only if the first element hides
the second

---

#### boolean overrides​(
ExecutableElement
overrider,

ExecutableElement
overridden,

TypeElement
type)

Tests whether one method, as a member of a given type,
overrides another method.
When a non-abstract method overrides an abstract one, the
former is also said to

implement

the latter.

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

**Parameters:**
- overrider

- the first method, possible overrider
- overridden

- the second method, possibly being overridden
- type

- the type of which the first method is a member

**Returns:**
- true

if and only if the first method overrides
the second

**See The Java™ Language Specification :**
- 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding

---

#### String
getConstantExpression​(
Object
value)

Returns the text of a

constant expression

representing a
primitive value or a string.
The text returned is in a form suitable for representing the value
in source code.

**Parameters:**
- value

- a primitive value or string

**Returns:**
- the text of a constant expression

**Throws:**
- IllegalArgumentException

- if the argument is not a primitive
value or string

**See Also:**
- VariableElement.getConstantValue()

---

#### void printElements​(
Writer
w,

Element
... elements)

Prints a representation of the elements to the given writer in
the specified order. The main purpose of this method is for
diagnostics. The exact format of the output is

not

specified and is subject to change.

**Parameters:**
- w

- the writer to print the output to
- elements

- the elements to print

---

#### Name
getName​(
CharSequence
cs)

Return a name with the same sequence of characters as the
argument.

**Parameters:**
- cs

- the character sequence to return as a name

**Returns:**
- a name with the same sequence of characters as the argument

---

#### boolean isFunctionalInterface​(
TypeElement
type)

Returns

true

if the type element is a functional interface,

false

otherwise.

**Parameters:**
- type

- the type element being examined

**Returns:**
- true

if the element is a functional interface,

false

otherwise

**Since:**
- 1.8

**See The Java™ Language Specification :**
- 9.8 Functional Interfaces

---

### Additional Sections

#### Interface Elements

```java
public interface
Elements
```

Utility methods for operating on program elements.

Compatibility Note:

Methods may be added to this interface
in future releases of the platform.

**Since:** 1.6
**See Also:** ProcessingEnvironment.getElementUtils()

public interface

Elements

Utility methods for operating on program elements.

Compatibility Note:

Methods may be added to this interface
in future releases of the platform.

Compatibility Note:

Methods may be added to this interface
in future releases of the platform.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Elements.Origin

The

origin

of an element or other language model
item.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<? extends

AnnotationMirror

>

getAllAnnotationMirrors

​(

Element

e)

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

List

<? extends

Element

>

getAllMembers

​(

TypeElement

type)

Returns all members of a type element, whether inherited or
declared directly.

default

Set

<? extends

ModuleElement

>

getAllModuleElements

()

Returns all module elements in the current environment.

default

Set

<? extends

PackageElement

>

getAllPackageElements

​(

CharSequence

name)

Returns all package elements with the given canonical name.

default

Set

<? extends

TypeElement

>

getAllTypeElements

​(

CharSequence

name)

Returns all type elements with the given canonical name.

Name

getBinaryName

​(

TypeElement

type)

Returns the

binary name

of a type element.

String

getConstantExpression

​(

Object

value)

Returns the text of a

constant expression

representing a
primitive value or a string.

String

getDocComment

​(

Element

e)

Returns the text of the documentation ("Javadoc")
comment of an element.

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

>

getElementValuesWithDefaults

​(

AnnotationMirror

a)

Returns the values of an annotation's elements, including defaults.

default

ModuleElement

getModuleElement

​(

CharSequence

name)

Returns a module element given its fully qualified name.

default

ModuleElement

getModuleOf

​(

Element

type)

Returns the module of an element.

Name

getName

​(

CharSequence

cs)

Return a name with the same sequence of characters as the
argument.

default

Elements.Origin

getOrigin

​(

AnnotatedConstruct

c,

AnnotationMirror

a)

Returns the

origin

of the given annotation mirror.

default

Elements.Origin

getOrigin

​(

Element

e)

Returns the

origin

of the given element.

default

Elements.Origin

getOrigin

​(

ModuleElement

m,

ModuleElement.Directive

directive)

Returns the

origin

of the given module directive.

PackageElement

getPackageElement

​(

CharSequence

name)

Returns a package given its fully qualified name if the package is unique in the environment.

default

PackageElement

getPackageElement

​(

ModuleElement

module,

CharSequence

name)

Returns a package given its fully qualified name, as seen from the given module.

PackageElement

getPackageOf

​(

Element

type)

Returns the package of an element.

TypeElement

getTypeElement

​(

CharSequence

name)

Returns a type element given its canonical name if the type element is unique in the environment.

default

TypeElement

getTypeElement

​(

ModuleElement

module,

CharSequence

name)

Returns a type element given its canonical name, as seen from the given module.

boolean

hides

​(

Element

hider,

Element

hidden)

Tests whether one type, method, or field hides another.

default boolean

isBridge

​(

ExecutableElement

e)

Returns

true

if the executable element is a bridge
method,

false

otherwise.

boolean

isDeprecated

​(

Element

e)

Returns

true

if the element is deprecated,

false

otherwise.

boolean

isFunctionalInterface

​(

TypeElement

type)

Returns

true

if the type element is a functional interface,

false

otherwise.

boolean

overrides

​(

ExecutableElement

overrider,

ExecutableElement

overridden,

TypeElement

type)

Tests whether one method, as a member of a given type,
overrides another method.

void

printElements

​(

Writer

w,

Element

... elements)

Prints a representation of the elements to the given writer in
the specified order.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static class

Elements.Origin

The

origin

of an element or other language model
item.

---

#### Nested Class Summary

The

origin

of an element or other language model
item.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

List

<? extends

AnnotationMirror

>

getAllAnnotationMirrors

​(

Element

e)

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

List

<? extends

Element

>

getAllMembers

​(

TypeElement

type)

Returns all members of a type element, whether inherited or
declared directly.

default

Set

<? extends

ModuleElement

>

getAllModuleElements

()

Returns all module elements in the current environment.

default

Set

<? extends

PackageElement

>

getAllPackageElements

​(

CharSequence

name)

Returns all package elements with the given canonical name.

default

Set

<? extends

TypeElement

>

getAllTypeElements

​(

CharSequence

name)

Returns all type elements with the given canonical name.

Name

getBinaryName

​(

TypeElement

type)

Returns the

binary name

of a type element.

String

getConstantExpression

​(

Object

value)

Returns the text of a

constant expression

representing a
primitive value or a string.

String

getDocComment

​(

Element

e)

Returns the text of the documentation ("Javadoc")
comment of an element.

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

>

getElementValuesWithDefaults

​(

AnnotationMirror

a)

Returns the values of an annotation's elements, including defaults.

default

ModuleElement

getModuleElement

​(

CharSequence

name)

Returns a module element given its fully qualified name.

default

ModuleElement

getModuleOf

​(

Element

type)

Returns the module of an element.

Name

getName

​(

CharSequence

cs)

Return a name with the same sequence of characters as the
argument.

default

Elements.Origin

getOrigin

​(

AnnotatedConstruct

c,

AnnotationMirror

a)

Returns the

origin

of the given annotation mirror.

default

Elements.Origin

getOrigin

​(

Element

e)

Returns the

origin

of the given element.

default

Elements.Origin

getOrigin

​(

ModuleElement

m,

ModuleElement.Directive

directive)

Returns the

origin

of the given module directive.

PackageElement

getPackageElement

​(

CharSequence

name)

Returns a package given its fully qualified name if the package is unique in the environment.

default

PackageElement

getPackageElement

​(

ModuleElement

module,

CharSequence

name)

Returns a package given its fully qualified name, as seen from the given module.

PackageElement

getPackageOf

​(

Element

type)

Returns the package of an element.

TypeElement

getTypeElement

​(

CharSequence

name)

Returns a type element given its canonical name if the type element is unique in the environment.

default

TypeElement

getTypeElement

​(

ModuleElement

module,

CharSequence

name)

Returns a type element given its canonical name, as seen from the given module.

boolean

hides

​(

Element

hider,

Element

hidden)

Tests whether one type, method, or field hides another.

default boolean

isBridge

​(

ExecutableElement

e)

Returns

true

if the executable element is a bridge
method,

false

otherwise.

boolean

isDeprecated

​(

Element

e)

Returns

true

if the element is deprecated,

false

otherwise.

boolean

isFunctionalInterface

​(

TypeElement

type)

Returns

true

if the type element is a functional interface,

false

otherwise.

boolean

overrides

​(

ExecutableElement

overrider,

ExecutableElement

overridden,

TypeElement

type)

Tests whether one method, as a member of a given type,
overrides another method.

void

printElements

​(

Writer

w,

Element

... elements)

Prints a representation of the elements to the given writer in
the specified order.

---

#### Method Summary

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

Returns all members of a type element, whether inherited or
declared directly.

Returns all module elements in the current environment.

Returns all package elements with the given canonical name.

Returns all type elements with the given canonical name.

Returns the

binary name

of a type element.

Returns the text of a

constant expression

representing a
primitive value or a string.

Returns the text of the documentation ("Javadoc")
comment of an element.

Returns the values of an annotation's elements, including defaults.

Returns a module element given its fully qualified name.

Returns the module of an element.

Return a name with the same sequence of characters as the
argument.

Returns the

origin

of the given annotation mirror.

Returns the

origin

of the given element.

Returns the

origin

of the given module directive.

Returns a package given its fully qualified name if the package is unique in the environment.

Returns a package given its fully qualified name, as seen from the given module.

Returns the package of an element.

Returns a type element given its canonical name if the type element is unique in the environment.

Returns a type element given its canonical name, as seen from the given module.

Tests whether one type, method, or field hides another.

Returns

true

if the executable element is a bridge
method,

false

otherwise.

Returns

true

if the element is deprecated,

false

otherwise.

Returns

true

if the type element is a functional interface,

false

otherwise.

Tests whether one method, as a member of a given type,
overrides another method.

Prints a representation of the elements to the given writer in
the specified order.

============ METHOD DETAIL ==========

- Method Detail

- getPackageElement

```java
PackageElement
getPackageElement​(
CharSequence
name)
```

Returns a package given its fully qualified name if the package is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching packages.

**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Returns:** the specified package, or

null

if it cannot be uniquely found

- getPackageElement

```java
default
PackageElement
getPackageElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a package given its fully qualified name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the specified package, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllPackageElements(java.lang.CharSequence)

- getAllPackageElements

```java
default
Set
<? extends
PackageElement
> getAllPackageElements​(
CharSequence
name)
```

Returns all package elements with the given canonical name.

There may be more than one package element with the same canonical
name if the package elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getPackageElement(name)

is
called passing through the name argument. If

getPackageElement(name)

is

null

, an empty set of
package elements is returned; otherwise, a single-element set
with the found package element is returned. If the set of
modules is nonempty, the modules are iterated over and any
non-

null

results of

getPackageElement(module, name)

are accumulated into a
set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the package elements, or an empty set if no package with the name can be found
**Since:** 9
**See Also:** getPackageElement(ModuleElement, CharSequence)

- getTypeElement

```java
TypeElement
getTypeElement​(
CharSequence
name)
```

Returns a type element given its canonical name if the type element is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching
type elements.

**Parameters:** name

- the canonical name
**Returns:** the named type element, or

null

if it cannot be uniquely found

- getTypeElement

```java
default
TypeElement
getTypeElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a type element given its canonical name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the canonical name
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the named type element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllTypeElements(java.lang.CharSequence)

- getAllTypeElements

```java
default
Set
<? extends
TypeElement
> getAllTypeElements​(
CharSequence
name)
```

Returns all type elements with the given canonical name.

There may be more than one type element with the same canonical
name if the type elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getTypeElement(name)

is called
passing through the name argument. If

getTypeElement(name)

is

null

, an empty set of type
elements is returned; otherwise, a single-element set with the
found type element is returned. If the set of modules is
nonempty, the modules are iterated over and any non-

null

results of

getTypeElement(module, name)

are accumulated
into a set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the type elements, or an empty set if no type with the name can be found
**Since:** 9
**See Also:** getTypeElement(ModuleElement, CharSequence)

- getModuleElement

```java
default
ModuleElement
getModuleElement​(
CharSequence
name)
```

Returns a module element given its fully qualified name.

If the named module cannot be found,

null

is
returned. One situation where a module cannot be found is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the name
**Returns:** the named module element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllModuleElements()

- getAllModuleElements

```java
default
Set
<? extends
ModuleElement
> getAllModuleElements()
```

Returns all module elements in the current environment.

If no modules are present, an empty set is returned. One
situation where no modules are present occurs when the
environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns
an empty set.
**Returns:** the known module elements, or an empty set if there are no modules
**Since:** 9
**See Also:** getModuleElement(CharSequence)

- getElementValuesWithDefaults

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValuesWithDefaults​(
AnnotationMirror
a)
```

Returns the values of an annotation's elements, including defaults.

**Parameters:** a

- annotation to examine
**Returns:** the values of the annotation's elements, including defaults
**See Also:** AnnotationMirror.getElementValues()

- getDocComment

```java
String
getDocComment​(
Element
e)
```

Returns the text of the documentation ("Javadoc")
comment of an element.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

**Parameters:** e

- the element being examined
**Returns:** the documentation comment of the element, or

null

if there is none
**See The Java™ Language Specification :** 3.6 White Space

- isDeprecated

```java
boolean isDeprecated​(
Element
e)
```

Returns

true

if the element is deprecated,

false

otherwise.

**Parameters:** e

- the element being examined
**Returns:** true

if the element is deprecated,

false

otherwise

- getOrigin

```java
default
Elements.Origin
getOrigin​(
Element
e)
```

Returns the

origin

of the given element.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** e

- the element being examined
**Returns:** the origin of the given element
**Since:** 9

- getOrigin

```java
default
Elements.Origin
getOrigin​(
AnnotatedConstruct
c,

AnnotationMirror
a)
```

Returns the

origin

of the given annotation mirror.

An annotation mirror is

mandated

if it is an implicitly declared

container annotation

used to hold repeated annotations of a repeatable annotation
type.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** c

- the construct the annotation mirror modifies
**Parameters:** a

- the annotation mirror being examined
**Returns:** the origin of the given annotation mirror
**Since:** 9
**See The Java™ Language Specification :** 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

- getOrigin

```java
default
Elements.Origin
getOrigin​(
ModuleElement
m,

ModuleElement.Directive
directive)
```

Returns the

origin

of the given module directive.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** m

- the module of the directive
**Parameters:** directive

- the module directive being examined
**Returns:** the origin of the given directive
**Since:** 9

- isBridge

```java
default boolean isBridge​(
ExecutableElement
e)
```

Returns

true

if the executable element is a bridge
method,

false

otherwise.

**Implementation Requirements:** The default implementation of this method returns

false

.
**Parameters:** e

- the executable being examined
**Returns:** true

if the executable element is a bridge
method,

false

otherwise
**Since:** 9

- getBinaryName

```java
Name
getBinaryName​(
TypeElement
type)
```

Returns the

binary name

of a type element.

**Parameters:** type

- the type element being examined
**Returns:** the binary name
**See Also:** TypeElement.getQualifiedName()
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getPackageOf

```java
PackageElement
getPackageOf​(
Element
type)
```

Returns the package of an element. The package of a package is
itself.

**Parameters:** type

- the element being examined
**Returns:** the package of an element

- getModuleOf

```java
default
ModuleElement
getModuleOf​(
Element
type)
```

Returns the module of an element. The module of a module is
itself.
If there is no module for the element, null is returned. One situation where there is
no module for an element is if the environment does not include modules, such as
an annotation processing environment configured for
a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** type

- the element being examined
**Returns:** the module of an element
**Since:** 9

- getAllMembers

```java
List
<? extends
Element
> getAllMembers​(
TypeElement
type)
```

Returns all members of a type element, whether inherited or
declared directly. For a class the result also includes its
constructors, but not local or anonymous classes.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Parameters:** type

- the type being examined
**Returns:** all members of the type
**See Also:** Element.getEnclosedElements()

- getAllAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAllAnnotationMirrors​(
Element
e)
```

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

**Parameters:** e

- the element being examined
**Returns:** all annotations of the element
**See Also:** Element.getAnnotationMirrors()

,

AnnotatedConstruct

- hides

```java
boolean hides​(
Element
hider,

Element
hidden)
```

Tests whether one type, method, or field hides another.

**Parameters:** hider

- the first element
**Parameters:** hidden

- the second element
**Returns:** true

if and only if the first element hides
the second

- overrides

```java
boolean overrides​(
ExecutableElement
overrider,

ExecutableElement
overridden,

TypeElement
type)
```

Tests whether one method, as a member of a given type,
overrides another method.
When a non-abstract method overrides an abstract one, the
former is also said to

implement

the latter.

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

**Parameters:** overrider

- the first method, possible overrider
**Parameters:** overridden

- the second method, possibly being overridden
**Parameters:** type

- the type of which the first method is a member
**Returns:** true

if and only if the first method overrides
the second
**See The Java™ Language Specification :** 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding

- getConstantExpression

```java
String
getConstantExpression​(
Object
value)
```

Returns the text of a

constant expression

representing a
primitive value or a string.
The text returned is in a form suitable for representing the value
in source code.

**Parameters:** value

- a primitive value or string
**Returns:** the text of a constant expression
**Throws:** IllegalArgumentException

- if the argument is not a primitive
value or string
**See Also:** VariableElement.getConstantValue()

- printElements

```java
void printElements​(
Writer
w,

Element
... elements)
```

Prints a representation of the elements to the given writer in
the specified order. The main purpose of this method is for
diagnostics. The exact format of the output is

not

specified and is subject to change.

**Parameters:** w

- the writer to print the output to
**Parameters:** elements

- the elements to print

- getName

```java
Name
getName​(
CharSequence
cs)
```

Return a name with the same sequence of characters as the
argument.

**Parameters:** cs

- the character sequence to return as a name
**Returns:** a name with the same sequence of characters as the argument

- isFunctionalInterface

```java
boolean isFunctionalInterface​(
TypeElement
type)
```

Returns

true

if the type element is a functional interface,

false

otherwise.

**Parameters:** type

- the type element being examined
**Returns:** true

if the element is a functional interface,

false

otherwise
**Since:** 1.8
**See The Java™ Language Specification :** 9.8 Functional Interfaces

Method Detail

- getPackageElement

```java
PackageElement
getPackageElement​(
CharSequence
name)
```

Returns a package given its fully qualified name if the package is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching packages.

**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Returns:** the specified package, or

null

if it cannot be uniquely found

- getPackageElement

```java
default
PackageElement
getPackageElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a package given its fully qualified name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the specified package, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllPackageElements(java.lang.CharSequence)

- getAllPackageElements

```java
default
Set
<? extends
PackageElement
> getAllPackageElements​(
CharSequence
name)
```

Returns all package elements with the given canonical name.

There may be more than one package element with the same canonical
name if the package elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getPackageElement(name)

is
called passing through the name argument. If

getPackageElement(name)

is

null

, an empty set of
package elements is returned; otherwise, a single-element set
with the found package element is returned. If the set of
modules is nonempty, the modules are iterated over and any
non-

null

results of

getPackageElement(module, name)

are accumulated into a
set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the package elements, or an empty set if no package with the name can be found
**Since:** 9
**See Also:** getPackageElement(ModuleElement, CharSequence)

- getTypeElement

```java
TypeElement
getTypeElement​(
CharSequence
name)
```

Returns a type element given its canonical name if the type element is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching
type elements.

**Parameters:** name

- the canonical name
**Returns:** the named type element, or

null

if it cannot be uniquely found

- getTypeElement

```java
default
TypeElement
getTypeElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a type element given its canonical name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the canonical name
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the named type element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllTypeElements(java.lang.CharSequence)

- getAllTypeElements

```java
default
Set
<? extends
TypeElement
> getAllTypeElements​(
CharSequence
name)
```

Returns all type elements with the given canonical name.

There may be more than one type element with the same canonical
name if the type elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getTypeElement(name)

is called
passing through the name argument. If

getTypeElement(name)

is

null

, an empty set of type
elements is returned; otherwise, a single-element set with the
found type element is returned. If the set of modules is
nonempty, the modules are iterated over and any non-

null

results of

getTypeElement(module, name)

are accumulated
into a set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the type elements, or an empty set if no type with the name can be found
**Since:** 9
**See Also:** getTypeElement(ModuleElement, CharSequence)

- getModuleElement

```java
default
ModuleElement
getModuleElement​(
CharSequence
name)
```

Returns a module element given its fully qualified name.

If the named module cannot be found,

null

is
returned. One situation where a module cannot be found is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the name
**Returns:** the named module element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllModuleElements()

- getAllModuleElements

```java
default
Set
<? extends
ModuleElement
> getAllModuleElements()
```

Returns all module elements in the current environment.

If no modules are present, an empty set is returned. One
situation where no modules are present occurs when the
environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns
an empty set.
**Returns:** the known module elements, or an empty set if there are no modules
**Since:** 9
**See Also:** getModuleElement(CharSequence)

- getElementValuesWithDefaults

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValuesWithDefaults​(
AnnotationMirror
a)
```

Returns the values of an annotation's elements, including defaults.

**Parameters:** a

- annotation to examine
**Returns:** the values of the annotation's elements, including defaults
**See Also:** AnnotationMirror.getElementValues()

- getDocComment

```java
String
getDocComment​(
Element
e)
```

Returns the text of the documentation ("Javadoc")
comment of an element.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

**Parameters:** e

- the element being examined
**Returns:** the documentation comment of the element, or

null

if there is none
**See The Java™ Language Specification :** 3.6 White Space

- isDeprecated

```java
boolean isDeprecated​(
Element
e)
```

Returns

true

if the element is deprecated,

false

otherwise.

**Parameters:** e

- the element being examined
**Returns:** true

if the element is deprecated,

false

otherwise

- getOrigin

```java
default
Elements.Origin
getOrigin​(
Element
e)
```

Returns the

origin

of the given element.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** e

- the element being examined
**Returns:** the origin of the given element
**Since:** 9

- getOrigin

```java
default
Elements.Origin
getOrigin​(
AnnotatedConstruct
c,

AnnotationMirror
a)
```

Returns the

origin

of the given annotation mirror.

An annotation mirror is

mandated

if it is an implicitly declared

container annotation

used to hold repeated annotations of a repeatable annotation
type.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** c

- the construct the annotation mirror modifies
**Parameters:** a

- the annotation mirror being examined
**Returns:** the origin of the given annotation mirror
**Since:** 9
**See The Java™ Language Specification :** 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

- getOrigin

```java
default
Elements.Origin
getOrigin​(
ModuleElement
m,

ModuleElement.Directive
directive)
```

Returns the

origin

of the given module directive.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** m

- the module of the directive
**Parameters:** directive

- the module directive being examined
**Returns:** the origin of the given directive
**Since:** 9

- isBridge

```java
default boolean isBridge​(
ExecutableElement
e)
```

Returns

true

if the executable element is a bridge
method,

false

otherwise.

**Implementation Requirements:** The default implementation of this method returns

false

.
**Parameters:** e

- the executable being examined
**Returns:** true

if the executable element is a bridge
method,

false

otherwise
**Since:** 9

- getBinaryName

```java
Name
getBinaryName​(
TypeElement
type)
```

Returns the

binary name

of a type element.

**Parameters:** type

- the type element being examined
**Returns:** the binary name
**See Also:** TypeElement.getQualifiedName()
**See The Java™ Language Specification :** 13.1 The Form of a Binary

- getPackageOf

```java
PackageElement
getPackageOf​(
Element
type)
```

Returns the package of an element. The package of a package is
itself.

**Parameters:** type

- the element being examined
**Returns:** the package of an element

- getModuleOf

```java
default
ModuleElement
getModuleOf​(
Element
type)
```

Returns the module of an element. The module of a module is
itself.
If there is no module for the element, null is returned. One situation where there is
no module for an element is if the environment does not include modules, such as
an annotation processing environment configured for
a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** type

- the element being examined
**Returns:** the module of an element
**Since:** 9

- getAllMembers

```java
List
<? extends
Element
> getAllMembers​(
TypeElement
type)
```

Returns all members of a type element, whether inherited or
declared directly. For a class the result also includes its
constructors, but not local or anonymous classes.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Parameters:** type

- the type being examined
**Returns:** all members of the type
**See Also:** Element.getEnclosedElements()

- getAllAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAllAnnotationMirrors​(
Element
e)
```

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

**Parameters:** e

- the element being examined
**Returns:** all annotations of the element
**See Also:** Element.getAnnotationMirrors()

,

AnnotatedConstruct

- hides

```java
boolean hides​(
Element
hider,

Element
hidden)
```

Tests whether one type, method, or field hides another.

**Parameters:** hider

- the first element
**Parameters:** hidden

- the second element
**Returns:** true

if and only if the first element hides
the second

- overrides

```java
boolean overrides​(
ExecutableElement
overrider,

ExecutableElement
overridden,

TypeElement
type)
```

Tests whether one method, as a member of a given type,
overrides another method.
When a non-abstract method overrides an abstract one, the
former is also said to

implement

the latter.

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

**Parameters:** overrider

- the first method, possible overrider
**Parameters:** overridden

- the second method, possibly being overridden
**Parameters:** type

- the type of which the first method is a member
**Returns:** true

if and only if the first method overrides
the second
**See The Java™ Language Specification :** 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding

- getConstantExpression

```java
String
getConstantExpression​(
Object
value)
```

Returns the text of a

constant expression

representing a
primitive value or a string.
The text returned is in a form suitable for representing the value
in source code.

**Parameters:** value

- a primitive value or string
**Returns:** the text of a constant expression
**Throws:** IllegalArgumentException

- if the argument is not a primitive
value or string
**See Also:** VariableElement.getConstantValue()

- printElements

```java
void printElements​(
Writer
w,

Element
... elements)
```

Prints a representation of the elements to the given writer in
the specified order. The main purpose of this method is for
diagnostics. The exact format of the output is

not

specified and is subject to change.

**Parameters:** w

- the writer to print the output to
**Parameters:** elements

- the elements to print

- getName

```java
Name
getName​(
CharSequence
cs)
```

Return a name with the same sequence of characters as the
argument.

**Parameters:** cs

- the character sequence to return as a name
**Returns:** a name with the same sequence of characters as the argument

- isFunctionalInterface

```java
boolean isFunctionalInterface​(
TypeElement
type)
```

Returns

true

if the type element is a functional interface,

false

otherwise.

**Parameters:** type

- the type element being examined
**Returns:** true

if the element is a functional interface,

false

otherwise
**Since:** 1.8
**See The Java™ Language Specification :** 9.8 Functional Interfaces

---

#### Method Detail

getPackageElement

```java
PackageElement
getPackageElement​(
CharSequence
name)
```

Returns a package given its fully qualified name if the package is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching packages.

**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Returns:** the specified package, or

null

if it cannot be uniquely found

---

#### getPackageElement

PackageElement

getPackageElement​(

CharSequence

name)

Returns a package given its fully qualified name if the package is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching packages.

getPackageElement

```java
default
PackageElement
getPackageElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a package given its fully qualified name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- fully qualified package name, or an empty string for an unnamed package
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the specified package, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllPackageElements(java.lang.CharSequence)

---

#### getPackageElement

default

PackageElement

getPackageElement​(

ModuleElement

module,

CharSequence

name)

Returns a package given its fully qualified name, as seen from the given module.

getAllPackageElements

```java
default
Set
<? extends
PackageElement
> getAllPackageElements​(
CharSequence
name)
```

Returns all package elements with the given canonical name.

There may be more than one package element with the same canonical
name if the package elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getPackageElement(name)

is
called passing through the name argument. If

getPackageElement(name)

is

null

, an empty set of
package elements is returned; otherwise, a single-element set
with the found package element is returned. If the set of
modules is nonempty, the modules are iterated over and any
non-

null

results of

getPackageElement(module, name)

are accumulated into a
set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the package elements, or an empty set if no package with the name can be found
**Since:** 9
**See Also:** getPackageElement(ModuleElement, CharSequence)

---

#### getAllPackageElements

default

Set

<? extends

PackageElement

> getAllPackageElements​(

CharSequence

name)

Returns all package elements with the given canonical name.

There may be more than one package element with the same canonical
name if the package elements are in different modules.

getTypeElement

```java
TypeElement
getTypeElement​(
CharSequence
name)
```

Returns a type element given its canonical name if the type element is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching
type elements.

**Parameters:** name

- the canonical name
**Returns:** the named type element, or

null

if it cannot be uniquely found

---

#### getTypeElement

TypeElement

getTypeElement​(

CharSequence

name)

Returns a type element given its canonical name if the type element is unique in the environment.
If running with modules, all modules in the modules graph are searched for matching
type elements.

getTypeElement

```java
default
TypeElement
getTypeElement​(
ModuleElement
module,

CharSequence
name)
```

Returns a type element given its canonical name, as seen from the given module.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the canonical name
**Parameters:** module

- module relative to which the lookup should happen
**Returns:** the named type element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllTypeElements(java.lang.CharSequence)

---

#### getTypeElement

default

TypeElement

getTypeElement​(

ModuleElement

module,

CharSequence

name)

Returns a type element given its canonical name, as seen from the given module.

getAllTypeElements

```java
default
Set
<? extends
TypeElement
> getAllTypeElements​(
CharSequence
name)
```

Returns all type elements with the given canonical name.

There may be more than one type element with the same canonical
name if the type elements are in different modules.

**Implementation Requirements:** The default implementation of this method calls

getAllModuleElements

and stores
the result. If the set of modules is empty,

getTypeElement(name)

is called
passing through the name argument. If

getTypeElement(name)

is

null

, an empty set of type
elements is returned; otherwise, a single-element set with the
found type element is returned. If the set of modules is
nonempty, the modules are iterated over and any non-

null

results of

getTypeElement(module, name)

are accumulated
into a set. The set is then returned.
**Parameters:** name

- the canonical name
**Returns:** the type elements, or an empty set if no type with the name can be found
**Since:** 9
**See Also:** getTypeElement(ModuleElement, CharSequence)

---

#### getAllTypeElements

default

Set

<? extends

TypeElement

> getAllTypeElements​(

CharSequence

name)

Returns all type elements with the given canonical name.

There may be more than one type element with the same canonical
name if the type elements are in different modules.

getModuleElement

```java
default
ModuleElement
getModuleElement​(
CharSequence
name)
```

Returns a module element given its fully qualified name.

If the named module cannot be found,

null

is
returned. One situation where a module cannot be found is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** name

- the name
**Returns:** the named module element, or

null

if it cannot be found
**Since:** 9
**See Also:** getAllModuleElements()

---

#### getModuleElement

default

ModuleElement

getModuleElement​(

CharSequence

name)

Returns a module element given its fully qualified name.

If the named module cannot be found,

null

is
returned. One situation where a module cannot be found is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

getAllModuleElements

```java
default
Set
<? extends
ModuleElement
> getAllModuleElements()
```

Returns all module elements in the current environment.

If no modules are present, an empty set is returned. One
situation where no modules are present occurs when the
environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns
an empty set.
**Returns:** the known module elements, or an empty set if there are no modules
**Since:** 9
**See Also:** getModuleElement(CharSequence)

---

#### getAllModuleElements

default

Set

<? extends

ModuleElement

> getAllModuleElements()

Returns all module elements in the current environment.

If no modules are present, an empty set is returned. One
situation where no modules are present occurs when the
environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

getElementValuesWithDefaults

```java
Map
<? extends
ExecutableElement
,​? extends
AnnotationValue
> getElementValuesWithDefaults​(
AnnotationMirror
a)
```

Returns the values of an annotation's elements, including defaults.

**Parameters:** a

- annotation to examine
**Returns:** the values of the annotation's elements, including defaults
**See Also:** AnnotationMirror.getElementValues()

---

#### getElementValuesWithDefaults

Map

<? extends

ExecutableElement

,​? extends

AnnotationValue

> getElementValuesWithDefaults​(

AnnotationMirror

a)

Returns the values of an annotation's elements, including defaults.

getDocComment

```java
String
getDocComment​(
Element
e)
```

Returns the text of the documentation ("Javadoc")
comment of an element.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

**Parameters:** e

- the element being examined
**Returns:** the documentation comment of the element, or

null

if there is none
**See The Java™ Language Specification :** 3.6 White Space

---

#### getDocComment

String

getDocComment​(

Element

e)

Returns the text of the documentation ("Javadoc")
comment of an element.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

A documentation comment of an element is a comment that
begins with "

/**

" , ends with a separate
"

*/

", and immediately precedes the element,
ignoring white space. Therefore, a documentation comment
contains at least three"

*

" characters. The text
returned for the documentation comment is a processed form of
the comment as it appears in source code. The leading "

/**

" and trailing "

*/

" are removed. For lines
of the comment starting after the initial "

/**

",
leading white space characters are discarded as are any
consecutive "

*

" characters appearing after the white
space or starting the line. The processed lines are then
concatenated together (including line terminators) and
returned.

isDeprecated

```java
boolean isDeprecated​(
Element
e)
```

Returns

true

if the element is deprecated,

false

otherwise.

**Parameters:** e

- the element being examined
**Returns:** true

if the element is deprecated,

false

otherwise

---

#### isDeprecated

boolean isDeprecated​(

Element

e)

Returns

true

if the element is deprecated,

false

otherwise.

getOrigin

```java
default
Elements.Origin
getOrigin​(
Element
e)
```

Returns the

origin

of the given element.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** e

- the element being examined
**Returns:** the origin of the given element
**Since:** 9

---

#### getOrigin

default

Elements.Origin

getOrigin​(

Element

e)

Returns the

origin

of the given element.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

Note that if this method returns

EXPLICIT

and the element was created from a class file, then
the element may not, in fact, correspond to an explicitly
declared construct in source code. This is due to limitations
of the fidelity of the class file format in preserving
information from source code. For example, at least some
versions of the class file format do not preserve whether a
constructor was explicitly declared by the programmer or was
implicitly declared as the

default constructor

.

getOrigin

```java
default
Elements.Origin
getOrigin​(
AnnotatedConstruct
c,

AnnotationMirror
a)
```

Returns the

origin

of the given annotation mirror.

An annotation mirror is

mandated

if it is an implicitly declared

container annotation

used to hold repeated annotations of a repeatable annotation
type.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** c

- the construct the annotation mirror modifies
**Parameters:** a

- the annotation mirror being examined
**Returns:** the origin of the given annotation mirror
**Since:** 9
**See The Java™ Language Specification :** 9.6.3 Repeatable Annotation Types, 9.7.5 Multiple Annotations of the Same Type

---

#### getOrigin

default

Elements.Origin

getOrigin​(

AnnotatedConstruct

c,

AnnotationMirror

a)

Returns the

origin

of the given annotation mirror.

An annotation mirror is

mandated

if it is an implicitly declared

container annotation

used to hold repeated annotations of a repeatable annotation
type.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

Note that if this method returns

EXPLICIT

and the annotation mirror was created from a class
file, then the element may not, in fact, correspond to an
explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
an annotation was explicitly declared by the programmer or was
implicitly declared as a

container annotation

.

getOrigin

```java
default
Elements.Origin
getOrigin​(
ModuleElement
m,

ModuleElement.Directive
directive)
```

Returns the

origin

of the given module directive.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

**Implementation Requirements:** The default implementation of this method returns

EXPLICIT

.
**Parameters:** m

- the module of the directive
**Parameters:** directive

- the module directive being examined
**Returns:** the origin of the given directive
**Since:** 9

---

#### getOrigin

default

Elements.Origin

getOrigin​(

ModuleElement

m,

ModuleElement.Directive

directive)

Returns the

origin

of the given module directive.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

Note that if this method returns

EXPLICIT

and the module directive was created from a class
file, then the module directive may not, in fact, correspond to
an explicitly declared construct in source code. This is due to
limitations of the fidelity of the class file format in
preserving information from source code. For example, at least
some versions of the class file format do not preserve whether
a

uses

directive was explicitly declared by the
programmer or was added as a synthetic construct.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

Note that an implementation may not be able to reliably
determine the origin status of the directive if the directive
is created from a class file due to limitations of the fidelity
of the class file format in preserving information from source
code.

isBridge

```java
default boolean isBridge​(
ExecutableElement
e)
```

Returns

true

if the executable element is a bridge
method,

false

otherwise.

**Implementation Requirements:** The default implementation of this method returns

false

.
**Parameters:** e

- the executable being examined
**Returns:** true

if the executable element is a bridge
method,

false

otherwise
**Since:** 9

---

#### isBridge

default boolean isBridge​(

ExecutableElement

e)

Returns

true

if the executable element is a bridge
method,

false

otherwise.

getBinaryName

```java
Name
getBinaryName​(
TypeElement
type)
```

Returns the

binary name

of a type element.

**Parameters:** type

- the type element being examined
**Returns:** the binary name
**See Also:** TypeElement.getQualifiedName()
**See The Java™ Language Specification :** 13.1 The Form of a Binary

---

#### getBinaryName

Name

getBinaryName​(

TypeElement

type)

Returns the

binary name

of a type element.

getPackageOf

```java
PackageElement
getPackageOf​(
Element
type)
```

Returns the package of an element. The package of a package is
itself.

**Parameters:** type

- the element being examined
**Returns:** the package of an element

---

#### getPackageOf

PackageElement

getPackageOf​(

Element

type)

Returns the package of an element. The package of a package is
itself.

getModuleOf

```java
default
ModuleElement
getModuleOf​(
Element
type)
```

Returns the module of an element. The module of a module is
itself.
If there is no module for the element, null is returned. One situation where there is
no module for an element is if the environment does not include modules, such as
an annotation processing environment configured for
a

source version

without modules.

**Implementation Requirements:** The default implementation of this method returns

null

.
**Parameters:** type

- the element being examined
**Returns:** the module of an element
**Since:** 9

---

#### getModuleOf

default

ModuleElement

getModuleOf​(

Element

type)

Returns the module of an element. The module of a module is
itself.
If there is no module for the element, null is returned. One situation where there is
no module for an element is if the environment does not include modules, such as
an annotation processing environment configured for
a

source version

without modules.

getAllMembers

```java
List
<? extends
Element
> getAllMembers​(
TypeElement
type)
```

Returns all members of a type element, whether inherited or
declared directly. For a class the result also includes its
constructors, but not local or anonymous classes.

**API Note:** Elements of certain kinds can be isolated using
methods in

ElementFilter

.
**Parameters:** type

- the type being examined
**Returns:** all members of the type
**See Also:** Element.getEnclosedElements()

---

#### getAllMembers

List

<? extends

Element

> getAllMembers​(

TypeElement

type)

Returns all members of a type element, whether inherited or
declared directly. For a class the result also includes its
constructors, but not local or anonymous classes.

getAllAnnotationMirrors

```java
List
<? extends
AnnotationMirror
> getAllAnnotationMirrors​(
Element
e)
```

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

**Parameters:** e

- the element being examined
**Returns:** all annotations of the element
**See Also:** Element.getAnnotationMirrors()

,

AnnotatedConstruct

---

#### getAllAnnotationMirrors

List

<? extends

AnnotationMirror

> getAllAnnotationMirrors​(

Element

e)

Returns all annotations

present

on an element, whether
directly present or present via inheritance.

hides

```java
boolean hides​(
Element
hider,

Element
hidden)
```

Tests whether one type, method, or field hides another.

**Parameters:** hider

- the first element
**Parameters:** hidden

- the second element
**Returns:** true

if and only if the first element hides
the second

---

#### hides

boolean hides​(

Element

hider,

Element

hidden)

Tests whether one type, method, or field hides another.

overrides

```java
boolean overrides​(
ExecutableElement
overrider,

ExecutableElement
overridden,

TypeElement
type)
```

Tests whether one method, as a member of a given type,
overrides another method.
When a non-abstract method overrides an abstract one, the
former is also said to

implement

the latter.

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

**Parameters:** overrider

- the first method, possible overrider
**Parameters:** overridden

- the second method, possibly being overridden
**Parameters:** type

- the type of which the first method is a member
**Returns:** true

if and only if the first method overrides
the second
**See The Java™ Language Specification :** 8.4.8 Inheritance, Overriding, and Hiding, 9.4.1 Inheritance and Overriding

---

#### overrides

boolean overrides​(

ExecutableElement

overrider,

ExecutableElement

overridden,

TypeElement

type)

Tests whether one method, as a member of a given type,
overrides another method.
When a non-abstract method overrides an abstract one, the
former is also said to

implement

the latter.

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

In the simplest and most typical usage, the value of the

type

parameter will simply be the class or interface
directly enclosing

overrider

(the possibly-overriding
method). For example, suppose

m1

represents the method

String.hashCode

and

m2

represents

Object.hashCode

. We can then ask whether

m1

overrides

m2

within the class

String

(it does):

assert elements.overrides(m1, m2,
elements.getTypeElement("java.lang.String"));

A more interesting case can be illustrated by the following example
in which a method in type

A

does not override a
like-named method in type

B

:

class A { public void m() {} }

interface B { void m(); }

...

m1 = ...; // A.m

m2 = ...; // B.m

assert ! elements.overrides(m1, m2,
elements.getTypeElement("A"));

When viewed as a member of a third type

C

, however,
the method in

A

does override the one in

B

:

class C extends A implements B {}

...

assert elements.overrides(m1, m2,
elements.getTypeElement("C"));

getConstantExpression

```java
String
getConstantExpression​(
Object
value)
```

Returns the text of a

constant expression

representing a
primitive value or a string.
The text returned is in a form suitable for representing the value
in source code.

**Parameters:** value

- a primitive value or string
**Returns:** the text of a constant expression
**Throws:** IllegalArgumentException

- if the argument is not a primitive
value or string
**See Also:** VariableElement.getConstantValue()

---

#### getConstantExpression

String

getConstantExpression​(

Object

value)

Returns the text of a

constant expression

representing a
primitive value or a string.
The text returned is in a form suitable for representing the value
in source code.

printElements

```java
void printElements​(
Writer
w,

Element
... elements)
```

Prints a representation of the elements to the given writer in
the specified order. The main purpose of this method is for
diagnostics. The exact format of the output is

not

specified and is subject to change.

**Parameters:** w

- the writer to print the output to
**Parameters:** elements

- the elements to print

---

#### printElements

void printElements​(

Writer

w,

Element

... elements)

Prints a representation of the elements to the given writer in
the specified order. The main purpose of this method is for
diagnostics. The exact format of the output is

not

specified and is subject to change.

getName

```java
Name
getName​(
CharSequence
cs)
```

Return a name with the same sequence of characters as the
argument.

**Parameters:** cs

- the character sequence to return as a name
**Returns:** a name with the same sequence of characters as the argument

---

#### getName

Name

getName​(

CharSequence

cs)

Return a name with the same sequence of characters as the
argument.

isFunctionalInterface

```java
boolean isFunctionalInterface​(
TypeElement
type)
```

Returns

true

if the type element is a functional interface,

false

otherwise.

**Parameters:** type

- the type element being examined
**Returns:** true

if the element is a functional interface,

false

otherwise
**Since:** 1.8
**See The Java™ Language Specification :** 9.8 Functional Interfaces

---

#### isFunctionalInterface

boolean isFunctionalInterface​(

TypeElement

type)

Returns

true

if the type element is a functional interface,

false

otherwise.

---

