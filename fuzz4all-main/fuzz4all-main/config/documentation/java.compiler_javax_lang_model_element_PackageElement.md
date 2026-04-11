# Interface PackageElement

**Source:** `java.compiler\javax\lang\model\element\PackageElement.html`

### Class Description

```java
public interface
PackageElement

extends
Element
,
QualifiedNameable
```

Represents a package program element. Provides access to information
about the package and its members.

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

QualifiedNameable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Name
getQualifiedName()

Returns the fully qualified name of this package.
This is also known as the package's

canonical

name.
For an

unnamed package

, an empty name is returned.

**Specified by:**
- getQualifiedName

in interface

QualifiedNameable

**Returns:**
- the fully qualified name of this package, or an
empty name if this is an unnamed package

**API Note:**
- The fully qualified name of a named package that is
not a subpackage of a named package is its simple name. The
fully qualified name of a named package that is a subpackage of
another named package consists of the fully qualified name of
the containing package, followed by "

.

", followed by the simple
(member) name of the subpackage.

**See The Java™ Language Specification :**
- 6.7 Fully Qualified Names and Canonical Names

---

#### Name
getSimpleName()

Returns the simple name of this package. For an

unnamed package

, an empty name is returned.

**Specified by:**
- getSimpleName

in interface

Element

**Returns:**
- the simple name of this package or an empty name if
this is an unnamed package

**See Also:**
- getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

---

#### List
<? extends
Element
> getEnclosedElements()

Returns the

top-level

classes and interfaces within this package. Note that
subpackages are

not

considered to be enclosed by a
package.

**Specified by:**
- getEnclosedElements

in interface

Element

**Returns:**
- the top-level classes and interfaces within this
package

**See Also:**
- TypeElement.getEnclosedElements()

,

getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

---

#### boolean isUnnamed()

Returns

true

if this is an unnamed package and

false

otherwise.

**Returns:**
- true

if this is an unnamed package and

false

otherwise

**See The Java™ Language Specification :**
- 7.4.2 Unnamed Packages

---

#### Element
getEnclosingElement()

Returns the enclosing module if such a module exists; otherwise
returns

null

.

One situation where a module does not exist for a package is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Specified by:**
- getEnclosingElement

in interface

Element

**Returns:**
- the enclosing module or

null

if no such module exists

**See Also:**
- Elements.getPackageOf(javax.lang.model.element.Element)

---

### Additional Sections

#### Interface PackageElement

**All Superinterfaces:** AnnotatedConstruct

,

Element

,

QualifiedNameable

```java
public interface
PackageElement

extends
Element
,
QualifiedNameable
```

Represents a package program element. Provides access to information
about the package and its members.

**Since:** 1.6
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

public interface

PackageElement

extends

Element

,

QualifiedNameable

Represents a package program element. Provides access to information
about the package and its members.

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

Returns the

top-level

classes and interfaces within this package.

Element

getEnclosingElement

()

Returns the enclosing module if such a module exists; otherwise
returns

null

.

Name

getQualifiedName

()

Returns the fully qualified name of this package.

Name

getSimpleName

()

Returns the simple name of this package.

boolean

isUnnamed

()

Returns

true

if this is an unnamed package and

false

otherwise.

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

Returns the

top-level

classes and interfaces within this package.

Element

getEnclosingElement

()

Returns the enclosing module if such a module exists; otherwise
returns

null

.

Name

getQualifiedName

()

Returns the fully qualified name of this package.

Name

getSimpleName

()

Returns the simple name of this package.

boolean

isUnnamed

()

Returns

true

if this is an unnamed package and

false

otherwise.

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

Returns the

top-level

classes and interfaces within this package.

Returns the enclosing module if such a module exists; otherwise
returns

null

.

Returns the fully qualified name of this package.

Returns the simple name of this package.

Returns

true

if this is an unnamed package and

false

otherwise.

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

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this package.
This is also known as the package's

canonical

name.
For an

unnamed package

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** The fully qualified name of a named package that is
not a subpackage of a named package is its simple name. The
fully qualified name of a named package that is a subpackage of
another named package consists of the fully qualified name of
the containing package, followed by "

.

", followed by the simple
(member) name of the subpackage.
**Returns:** the fully qualified name of this package, or an
empty name if this is an unnamed package
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this package. For an

unnamed package

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this package or an empty name if
this is an unnamed package
**See Also:** getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the

top-level

classes and interfaces within this package. Note that
subpackages are

not

considered to be enclosed by a
package.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the top-level classes and interfaces within this
package
**See Also:** TypeElement.getEnclosedElements()

,

getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

- isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed package and

false

otherwise.

**Returns:** true

if this is an unnamed package and

false

otherwise
**See The Java™ Language Specification :** 7.4.2 Unnamed Packages

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the enclosing module if such a module exists; otherwise
returns

null

.

One situation where a module does not exist for a package is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the enclosing module or

null

if no such module exists
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

Method Detail

- getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this package.
This is also known as the package's

canonical

name.
For an

unnamed package

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** The fully qualified name of a named package that is
not a subpackage of a named package is its simple name. The
fully qualified name of a named package that is a subpackage of
another named package consists of the fully qualified name of
the containing package, followed by "

.

", followed by the simple
(member) name of the subpackage.
**Returns:** the fully qualified name of this package, or an
empty name if this is an unnamed package
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

- getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this package. For an

unnamed package

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this package or an empty name if
this is an unnamed package
**See Also:** getSimpleName()

,

ExecutableElement.getSimpleName()

,

TypeElement.getSimpleName()

,

VariableElement.getSimpleName()

,

ModuleElement.getSimpleName()

- getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the

top-level

classes and interfaces within this package. Note that
subpackages are

not

considered to be enclosed by a
package.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the top-level classes and interfaces within this
package
**See Also:** TypeElement.getEnclosedElements()

,

getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

- isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed package and

false

otherwise.

**Returns:** true

if this is an unnamed package and

false

otherwise
**See The Java™ Language Specification :** 7.4.2 Unnamed Packages

- getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the enclosing module if such a module exists; otherwise
returns

null

.

One situation where a module does not exist for a package is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the enclosing module or

null

if no such module exists
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### Method Detail

getQualifiedName

```java
Name
getQualifiedName()
```

Returns the fully qualified name of this package.
This is also known as the package's

canonical

name.
For an

unnamed package

, an empty name is returned.

**Specified by:** getQualifiedName

in interface

QualifiedNameable
**API Note:** The fully qualified name of a named package that is
not a subpackage of a named package is its simple name. The
fully qualified name of a named package that is a subpackage of
another named package consists of the fully qualified name of
the containing package, followed by "

.

", followed by the simple
(member) name of the subpackage.
**Returns:** the fully qualified name of this package, or an
empty name if this is an unnamed package
**See The Java™ Language Specification :** 6.7 Fully Qualified Names and Canonical Names

---

#### getQualifiedName

Name

getQualifiedName()

Returns the fully qualified name of this package.
This is also known as the package's

canonical

name.
For an

unnamed package

, an empty name is returned.

getSimpleName

```java
Name
getSimpleName()
```

Returns the simple name of this package. For an

unnamed package

, an empty name is returned.

**Specified by:** getSimpleName

in interface

Element
**Returns:** the simple name of this package or an empty name if
this is an unnamed package
**See Also:** getSimpleName()

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

Returns the simple name of this package. For an

unnamed package

, an empty name is returned.

getEnclosedElements

```java
List
<? extends
Element
> getEnclosedElements()
```

Returns the

top-level

classes and interfaces within this package. Note that
subpackages are

not

considered to be enclosed by a
package.

**Specified by:** getEnclosedElements

in interface

Element
**Returns:** the top-level classes and interfaces within this
package
**See Also:** TypeElement.getEnclosedElements()

,

getEnclosedElements()

,

ModuleElement.getEnclosedElements()

,

Elements.getAllMembers(javax.lang.model.element.TypeElement)

---

#### getEnclosedElements

List

<? extends

Element

> getEnclosedElements()

Returns the

top-level

classes and interfaces within this package. Note that
subpackages are

not

considered to be enclosed by a
package.

isUnnamed

```java
boolean isUnnamed()
```

Returns

true

if this is an unnamed package and

false

otherwise.

**Returns:** true

if this is an unnamed package and

false

otherwise
**See The Java™ Language Specification :** 7.4.2 Unnamed Packages

---

#### isUnnamed

boolean isUnnamed()

Returns

true

if this is an unnamed package and

false

otherwise.

getEnclosingElement

```java
Element
getEnclosingElement()
```

Returns the enclosing module if such a module exists; otherwise
returns

null

.

One situation where a module does not exist for a package is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

**Specified by:** getEnclosingElement

in interface

Element
**Returns:** the enclosing module or

null

if no such module exists
**See Also:** Elements.getPackageOf(javax.lang.model.element.Element)

---

#### getEnclosingElement

Element

getEnclosingElement()

Returns the enclosing module if such a module exists; otherwise
returns

null

.

One situation where a module does not exist for a package is if
the environment does not include modules, such as an annotation
processing environment configured for a

source version

without modules.

---

