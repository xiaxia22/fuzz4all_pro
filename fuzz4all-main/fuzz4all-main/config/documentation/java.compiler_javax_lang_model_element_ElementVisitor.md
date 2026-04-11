# Interface ElementVisitor<R,​P>

**Source:** `java.compiler\javax\lang\model\element\ElementVisitor.html`

### Class Description

```java
public interface
ElementVisitor<R,​P>
```

A visitor of program elements, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on an element when the kind of element is unknown at compile time.
When a visitor is passed to an element's

accept

method, the

visit

Xyz

method most applicable
to that element is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### R
visit​(
Element
e,

P
p)

Visits an element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### default
R
visit​(
Element
e)

A convenience method equivalent to

visit(e, null)

.

**Parameters:**
- e

- the element to visit

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- The default implementation is

visit(e, null)

.

---

#### R
visitPackage​(
PackageElement
e,

P
p)

Visits a package element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitType​(
TypeElement
e,

P
p)

Visits a type element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitVariable​(
VariableElement
e,

P
p)

Visits a variable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitExecutable​(
ExecutableElement
e,

P
p)

Visits an executable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitTypeParameter​(
TypeParameterElement
e,

P
p)

Visits a type parameter element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
visitUnknown​(
Element
e,

P
p)

Visits an unknown kind of element.
This can occur if the language evolves and new kinds
of elements are added to the

Element

hierarchy.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Throws:**
- UnknownElementException

- a visitor implementation may optionally throw this exception

---

#### default
R
visitModule​(
ModuleElement
e,

P
p)

Visits a module element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Since:**
- 9

**Implementation Requirements:**
- The default implementation visits a

ModuleElement

by calling

visitUnknown(e, p)

.

---

### Additional Sections

#### Interface ElementVisitor<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's
methods. Use

Void

for visitors that do not need an
additional parameter.

**All Known Implementing Classes:** AbstractElementVisitor6

,

AbstractElementVisitor7

,

AbstractElementVisitor8

,

AbstractElementVisitor9

,

ElementKindVisitor6

,

ElementKindVisitor7

,

ElementKindVisitor8

,

ElementKindVisitor9

,

ElementScanner6

,

ElementScanner7

,

ElementScanner8

,

ElementScanner9

,

SimpleElementVisitor6

,

SimpleElementVisitor7

,

SimpleElementVisitor8

,

SimpleElementVisitor9

```java
public interface
ElementVisitor<R,​P>
```

A visitor of program elements, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on an element when the kind of element is unknown at compile time.
When a visitor is passed to an element's

accept

method, the

visit

Xyz

method most applicable
to that element is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

**Since:** 1.6

public interface

ElementVisitor<R,​P>

A visitor of program elements, in the style of the visitor design
pattern. Classes implementing this interface are used to operate
on an element when the kind of element is unknown at compile time.
When a visitor is passed to an element's

accept

method, the

visit

Xyz

method most applicable
to that element is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

Element

e)

A convenience method equivalent to

visit(e, null)

.

R

visit

​(

Element

e,

P

p)

Visits an element.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

default

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

R

visitPackage

​(

PackageElement

e,

P

p)

Visits a package element.

R

visitType

​(

TypeElement

e,

P

p)

Visits a type element.

R

visitTypeParameter

​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

R

visitUnknown

​(

Element

e,

P

p)

Visits an unknown kind of element.

R

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

Element

e)

A convenience method equivalent to

visit(e, null)

.

R

visit

​(

Element

e,

P

p)

Visits an element.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

default

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

R

visitPackage

​(

PackageElement

e,

P

p)

Visits a package element.

R

visitType

​(

TypeElement

e,

P

p)

Visits a type element.

R

visitTypeParameter

​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

R

visitUnknown

​(

Element

e,

P

p)

Visits an unknown kind of element.

R

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

---

#### Method Summary

A convenience method equivalent to

visit(e, null)

.

Visits an element.

Visits an executable element.

Visits a module element.

Visits a package element.

Visits a type element.

Visits a type parameter element.

Visits an unknown kind of element.

Visits a variable element.

============ METHOD DETAIL ==========

- Method Detail

- visit

```java
R
visit​(
Element
e,

P
p)
```

Visits an element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
Element
e)
```

A convenience method equivalent to

visit(e, null)

.

**Implementation Requirements:** The default implementation is

visit(e, null)

.
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

- visitPackage

```java
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitType

```java
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitVariable

```java
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExecutable

```java
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
R
visitUnknown​(
Element
e,

P
p)
```

Visits an unknown kind of element.
This can occur if the language evolves and new kinds
of elements are added to the

Element

hierarchy.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

- visitModule

```java
default
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Implementation Requirements:** The default implementation visits a

ModuleElement

by calling

visitUnknown(e, p)

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 9

Method Detail

- visit

```java
R
visit​(
Element
e,

P
p)
```

Visits an element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
Element
e)
```

A convenience method equivalent to

visit(e, null)

.

**Implementation Requirements:** The default implementation is

visit(e, null)

.
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

- visitPackage

```java
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitType

```java
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitVariable

```java
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExecutable

```java
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
R
visitUnknown​(
Element
e,

P
p)
```

Visits an unknown kind of element.
This can occur if the language evolves and new kinds
of elements are added to the

Element

hierarchy.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

- visitModule

```java
default
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Implementation Requirements:** The default implementation visits a

ModuleElement

by calling

visitUnknown(e, p)

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 9

---

#### Method Detail

visit

```java
R
visit​(
Element
e,

P
p)
```

Visits an element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

R

visit​(

Element

e,

P

p)

Visits an element.

visit

```java
default
R
visit​(
Element
e)
```

A convenience method equivalent to

visit(e, null)

.

**Implementation Requirements:** The default implementation is

visit(e, null)

.
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

---

#### visit

default

R

visit​(

Element

e)

A convenience method equivalent to

visit(e, null)

.

visitPackage

```java
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitPackage

R

visitPackage​(

PackageElement

e,

P

p)

Visits a package element.

visitType

```java
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitType

R

visitType​(

TypeElement

e,

P

p)

Visits a type element.

visitVariable

```java
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitVariable

R

visitVariable​(

VariableElement

e,

P

p)

Visits a variable element.

visitExecutable

```java
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitExecutable

R

visitExecutable​(

ExecutableElement

e,

P

p)

Visits an executable element.

visitTypeParameter

```java
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitTypeParameter

R

visitTypeParameter​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

visitUnknown

```java
R
visitUnknown​(
Element
e,

P
p)
```

Visits an unknown kind of element.
This can occur if the language evolves and new kinds
of elements are added to the

Element

hierarchy.

**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

R

visitUnknown​(

Element

e,

P

p)

Visits an unknown kind of element.
This can occur if the language evolves and new kinds
of elements are added to the

Element

hierarchy.

visitModule

```java
default
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Implementation Requirements:** The default implementation visits a

ModuleElement

by calling

visitUnknown(e, p)

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 9

---

#### visitModule

default

R

visitModule​(

ModuleElement

e,

P

p)

Visits a module element.

---

