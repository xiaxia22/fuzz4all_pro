# Class ElementScanner9<R,​P>

**Source:** `java.compiler\javax\lang\model\util\ElementScanner9.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_11
)
public class
ElementScanner9<R,​P>

extends
ElementScanner8
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

The

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

*No entries found.*

### Constructor Details

#### protected ElementScanner9()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected ElementScanner9​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the default value

---

### Method Details

#### public
R
visitModule​(
ModuleElement
e,

P
p)

Visits a module element.

**Specified by:**
- visitModule

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitModule

in class

AbstractElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of the scan

**Implementation Requirements:**
- This implementation scans the enclosed elements.

---

### Additional Sections

#### Class ElementScanner9<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementScanner6

<R,​P>
- - javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8

<R,​P>
- - javax.lang.model.util.ElementScanner9<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.ElementScanner6

<R,​P>
- - javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8

<R,​P>
- - javax.lang.model.util.ElementScanner9<R,​P>

javax.lang.model.util.ElementScanner6

<R,​P>

- javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8

<R,​P>
- - javax.lang.model.util.ElementScanner9<R,​P>

javax.lang.model.util.ElementScanner7

<R,​P>

- javax.lang.model.util.ElementScanner8

<R,​P>
- - javax.lang.model.util.ElementScanner9<R,​P>

javax.lang.model.util.ElementScanner8

<R,​P>

- javax.lang.model.util.ElementScanner9<R,​P>

javax.lang.model.util.ElementScanner9<R,​P>

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

```java
@SupportedSourceVersion
(
RELEASE_11
)
public class
ElementScanner9<R,​P>

extends
ElementScanner8
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

The

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

**Since:** 9
**See Also:** ElementScanner6

,

ElementScanner7

,

ElementScanner8

@SupportedSourceVersion

(

RELEASE_11

)
public class

ElementScanner9<R,​P>

extends

ElementScanner8

<R,​P>

A scanning visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

The

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

- Fields declared in class javax.lang.model.util.

ElementScanner6

DEFAULT_VALUE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementScanner9

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementScanner9

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

- Methods declared in class javax.lang.model.util.

ElementScanner7

visitVariable

- Methods declared in class javax.lang.model.util.

ElementScanner6

scan

,

scan

,

scan

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

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

- Fields declared in class javax.lang.model.util.

ElementScanner6

DEFAULT_VALUE

---

#### Field Summary

Fields declared in class javax.lang.model.util.

ElementScanner6

DEFAULT_VALUE

---

#### Fields declared in class javax.lang.model.util. ElementScanner6

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementScanner9

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementScanner9

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

---

#### Constructor Summary

Constructor for concrete subclasses; uses

null

for the
default value.

Constructor for concrete subclasses; uses the argument for the
default value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

- Methods declared in class javax.lang.model.util.

ElementScanner7

visitVariable

- Methods declared in class javax.lang.model.util.

ElementScanner6

scan

,

scan

,

scan

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

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

Visits a module element.

Methods declared in class javax.lang.model.util.

ElementScanner7

visitVariable

---

#### Methods declared in class javax.lang.model.util. ElementScanner7

Methods declared in class javax.lang.model.util.

ElementScanner6

scan

,

scan

,

scan

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

---

#### Methods declared in class javax.lang.model.util. ElementScanner6

Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementScanner9

```java
protected ElementScanner9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner9

```java
protected ElementScanner9​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

============ METHOD DETAIL ==========

- Method Detail

- visitModule

```java
public
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Specified by:** visitModule

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

AbstractElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the scan

Constructor Detail

- ElementScanner9

```java
protected ElementScanner9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner9

```java
protected ElementScanner9​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### Constructor Detail

ElementScanner9

```java
protected ElementScanner9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### ElementScanner9

protected ElementScanner9()

Constructor for concrete subclasses; uses

null

for the
default value.

ElementScanner9

```java
protected ElementScanner9​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### ElementScanner9

protected ElementScanner9​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

- visitModule

```java
public
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Specified by:** visitModule

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

AbstractElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the scan

---

#### Method Detail

visitModule

```java
public
R
visitModule​(
ModuleElement
e,

P
p)
```

Visits a module element.

**Specified by:** visitModule

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitModule

in class

AbstractElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation scans the enclosed elements.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the scan

---

#### visitModule

public

R

visitModule​(

ModuleElement

e,

P

p)

Visits a module element.

---

