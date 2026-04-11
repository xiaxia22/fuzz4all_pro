# Class ElementScanner6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\ElementScanner6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
ElementScanner6<R,​P>

extends
AbstractElementVisitor6
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version. The

visit

Xyz

methods in this
class scan their component elements by calling

scan

on
their

enclosed elements

,

parameters

, etc., as
indicated in the individual method specifications. A subclass can
control the order elements are visited by overriding the

visit

Xyz

methods. Note that clients of a scanner
may get the desired behavior be invoking

v.scan(e, p)

rather
than

v.visit(e, p)

on the root objects of interest.

When a subclass overrides a

visit

Xyz

method, the
new method can cause the enclosed elements to be scanned in the
default way by calling

super.visit

Xyz

. In this
fashion, the concrete visitor can control the ordering of traversal
over the component elements with respect to the additional
processing; for example, consistently calling

super.visit

Xyz

at the start of the overridden
methods will yield a preorder traversal, etc. If the component
elements should be traversed in some other order, instead of
calling

super.visit

Xyz

, an overriding visit method
should call

scan

with the elements in the desired order.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

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

#### protected final
R
DEFAULT_VALUE

The specified default value.

---

### Constructor Details

#### @Deprecated
(
since
="9")
protected ElementScanner6()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### @Deprecated
(
since
="9")
protected ElementScanner6​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the default value

---

### Method Details

#### public final
R
scan​(
Iterable
<? extends
Element
> iterable,

P
p)

Iterates over the given elements and calls

scan(Element, P)

on each one. Returns
the result of the last call to

scan

or

DEFAULT_VALUE

for an empty iterable.

**Parameters:**
- iterable

- the elements to scan
- p

- additional parameter

**Returns:**
- the scan of the last element or

DEFAULT_VALUE

if no elements

---

#### public
R
scan​(
Element
e,

P
p)

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

**Parameters:**
- e

- the element to scan
- p

- a scanner-specified parameter

**Returns:**
- the result of visiting

e

.

---

#### public final
R
scan​(
Element
e)

Convenience method equivalent to

v.scan(e, null)

.

**Parameters:**
- e

- the element to scan

**Returns:**
- the result of scanning

e

.

---

#### public
R
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
- the result of scanning

**Implementation Requirements:**
- This implementation scans the enclosed elements.

---

#### public
R
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
- the result of scanning

**Implementation Requirements:**
- This implementation scans the enclosed elements.

---

#### public
R
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
- the result of scanning

**Implementation Requirements:**
- This implementation scans the enclosed elements, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.

---

#### public
R
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
- the result of scanning

**Implementation Requirements:**
- This implementation scans the parameters.

---

#### public
R
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
- the result of scanning

**Implementation Requirements:**
- This implementation scans the enclosed elements.

---

### Additional Sections

#### Class ElementScanner6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementScanner6<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.ElementScanner6<R,​P>

javax.lang.model.util.ElementScanner6<R,​P>

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

**All Implemented Interfaces:** ElementVisitor

<R,​P>

**Direct Known Subclasses:** ElementScanner7

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
ElementScanner6<R,​P>

extends
AbstractElementVisitor6
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version. The

visit

Xyz

methods in this
class scan their component elements by calling

scan

on
their

enclosed elements

,

parameters

, etc., as
indicated in the individual method specifications. A subclass can
control the order elements are visited by overriding the

visit

Xyz

methods. Note that clients of a scanner
may get the desired behavior be invoking

v.scan(e, p)

rather
than

v.visit(e, p)

on the root objects of interest.

When a subclass overrides a

visit

Xyz

method, the
new method can cause the enclosed elements to be scanned in the
default way by calling

super.visit

Xyz

. In this
fashion, the concrete visitor can control the ordering of traversal
over the component elements with respect to the additional
processing; for example, consistently calling

super.visit

Xyz

at the start of the overridden
methods will yield a preorder traversal, etc. If the component
elements should be traversed in some other order, instead of
calling

super.visit

Xyz

, an overriding visit method
should call

scan

with the elements in the desired order.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.6
**See Also:** ElementScanner7

,

ElementScanner8

,

ElementScanner9

@SupportedSourceVersion

(

RELEASE_6

)
public class

ElementScanner6<R,​P>

extends

AbstractElementVisitor6

<R,​P>

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version. The

visit

Xyz

methods in this
class scan their component elements by calling

scan

on
their

enclosed elements

,

parameters

, etc., as
indicated in the individual method specifications. A subclass can
control the order elements are visited by overriding the

visit

Xyz

methods. Note that clients of a scanner
may get the desired behavior be invoking

v.scan(e, p)

rather
than

v.visit(e, p)

on the root objects of interest.

When a subclass overrides a

visit

Xyz

method, the
new method can cause the enclosed elements to be scanned in the
default way by calling

super.visit

Xyz

. In this
fashion, the concrete visitor can control the ordering of traversal
over the component elements with respect to the additional
processing; for example, consistently calling

super.visit

Xyz

at the start of the overridden
methods will yield a preorder traversal, etc. If the component
elements should be traversed in some other order, instead of
calling

super.visit

Xyz

, an overriding visit method
should call

scan

with the elements in the desired order.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When a subclass overrides a

visit

Xyz

method, the
new method can cause the enclosed elements to be scanned in the
default way by calling

super.visit

Xyz

. In this
fashion, the concrete visitor can control the ordering of traversal
over the component elements with respect to the additional
processing; for example, consistently calling

super.visit

Xyz

at the start of the overridden
methods will yield a preorder traversal, etc. If the component
elements should be traversed in some other order, instead of
calling

super.visit

Xyz

, an overriding visit method
should call

scan

with the elements in the desired order.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it in the
future to accommodate new, currently unknown, language structures
added to future versions of the Java™ programming language.
Therefore, methods whose names begin with

"visit"

may be
added to this class in the future; to avoid incompatibilities,
classes which extend this class should not declare any instance
methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new element scanner visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The specified default value.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementScanner6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

ElementScanner6

​(

R

defaultValue)

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

scan

​(

Iterable

<? extends

Element

> iterable,

P

p)

Iterates over the given elements and calls

scan(Element, P)

on each one.

R

scan

​(

Element

e)

Convenience method equivalent to

v.scan(e, null)

.

R

scan

​(

Element

e,

P

p)

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

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

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

,

visitUnknown

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

The specified default value.

---

#### Field Summary

The specified default value.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementScanner6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

ElementScanner6

​(

R

defaultValue)

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

---

#### Constructor Summary

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

scan

​(

Iterable

<? extends

Element

> iterable,

P

p)

Iterates over the given elements and calls

scan(Element, P)

on each one.

R

scan

​(

Element

e)

Convenience method equivalent to

v.scan(e, null)

.

R

scan

​(

Element

e,

P

p)

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

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

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

,

visitUnknown

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Iterates over the given elements and calls

scan(Element, P)

on each one.

Convenience method equivalent to

v.scan(e, null)

.

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

Visits an executable element.

Visits a package element.

Visits a type element.

Visits a type parameter element.

Visits a variable element.

Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

,

visitUnknown

---

#### Methods declared in class javax.lang.model.util. AbstractElementVisitor6

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The specified default value.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

============ METHOD DETAIL ==========

- Method Detail

- scan

```java
public final
R
scan​(
Iterable
<? extends
Element
> iterable,

P
p)
```

Iterates over the given elements and calls

scan(Element, P)

on each one. Returns
the result of the last call to

scan

or

DEFAULT_VALUE

for an empty iterable.

**Parameters:** iterable

- the elements to scan
**Parameters:** p

- additional parameter
**Returns:** the scan of the last element or

DEFAULT_VALUE

if no elements

- scan

```java
public
R
scan​(
Element
e,

P
p)
```

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

**Parameters:** e

- the element to scan
**Parameters:** p

- a scanner-specified parameter
**Returns:** the result of visiting

e

.

- scan

```java
public final
R
scan​(
Element
e)
```

Convenience method equivalent to

v.scan(e, null)

.

**Parameters:** e

- the element to scan
**Returns:** the result of scanning

e

.

- visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Implementation Requirements:** This implementation scans the enclosed elements, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Implementation Requirements:** This implementation scans the parameters.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The specified default value.

---

#### Field Detail

DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

The specified default value.

---

#### DEFAULT_VALUE

protected final

R

DEFAULT_VALUE

The specified default value.

Constructor Detail

- ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### Constructor Detail

ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### ElementScanner6

@Deprecated

(

since

="9")
protected ElementScanner6()

Constructor for concrete subclasses; uses

null

for the
default value.

ElementScanner6

```java
@Deprecated
(
since
="9")
protected ElementScanner6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### ElementScanner6

@Deprecated

(

since

="9")
protected ElementScanner6​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

- scan

```java
public final
R
scan​(
Iterable
<? extends
Element
> iterable,

P
p)
```

Iterates over the given elements and calls

scan(Element, P)

on each one. Returns
the result of the last call to

scan

or

DEFAULT_VALUE

for an empty iterable.

**Parameters:** iterable

- the elements to scan
**Parameters:** p

- additional parameter
**Returns:** the scan of the last element or

DEFAULT_VALUE

if no elements

- scan

```java
public
R
scan​(
Element
e,

P
p)
```

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

**Parameters:** e

- the element to scan
**Parameters:** p

- a scanner-specified parameter
**Returns:** the result of visiting

e

.

- scan

```java
public final
R
scan​(
Element
e)
```

Convenience method equivalent to

v.scan(e, null)

.

**Parameters:** e

- the element to scan
**Returns:** the result of scanning

e

.

- visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Implementation Requirements:** This implementation scans the enclosed elements, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Implementation Requirements:** This implementation scans the parameters.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### Method Detail

scan

```java
public final
R
scan​(
Iterable
<? extends
Element
> iterable,

P
p)
```

Iterates over the given elements and calls

scan(Element, P)

on each one. Returns
the result of the last call to

scan

or

DEFAULT_VALUE

for an empty iterable.

**Parameters:** iterable

- the elements to scan
**Parameters:** p

- additional parameter
**Returns:** the scan of the last element or

DEFAULT_VALUE

if no elements

---

#### scan

public final

R

scan​(

Iterable

<? extends

Element

> iterable,

P

p)

Iterates over the given elements and calls

scan(Element, P)

on each one. Returns
the result of the last call to

scan

or

DEFAULT_VALUE

for an empty iterable.

scan

```java
public
R
scan​(
Element
e,

P
p)
```

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

**Parameters:** e

- the element to scan
**Parameters:** p

- a scanner-specified parameter
**Returns:** the result of visiting

e

.

---

#### scan

public

R

scan​(

Element

e,

P

p)

Processes an element by calling

e.accept(this, p)

;
this method may be overridden by subclasses.

scan

```java
public final
R
scan​(
Element
e)
```

Convenience method equivalent to

v.scan(e, null)

.

**Parameters:** e

- the element to scan
**Returns:** the result of scanning

e

.

---

#### scan

public final

R

scan​(

Element

e)

Convenience method equivalent to

v.scan(e, null)

.

visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### visitPackage

public

R

visitPackage​(

PackageElement

e,

P

p)

Visits a package element.

visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### visitType

public

R

visitType​(

TypeElement

e,

P

p)

Visits a type element.

visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element.

**Implementation Requirements:** This implementation scans the enclosed elements, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### visitVariable

public

R

visitVariable​(

VariableElement

e,

P

p)

Visits a variable element.

visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Implementation Requirements:** This implementation scans the parameters.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### visitExecutable

public

R

visitExecutable​(

ExecutableElement

e,

P

p)

Visits an executable element.

visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of scanning

---

#### visitTypeParameter

public

R

visitTypeParameter​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

---

