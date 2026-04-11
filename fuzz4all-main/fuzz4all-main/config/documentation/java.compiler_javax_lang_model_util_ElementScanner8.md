# Class ElementScanner8<R,​P>

**Source:** `java.compiler\javax\lang\model\util\ElementScanner8.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
ElementScanner8<R,​P>

extends
ElementScanner7
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

*No entries found.*

### Constructor Details

#### protected ElementScanner8()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected ElementScanner8​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the default value

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ElementScanner8<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementScanner6

<R,​P>
- - javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.ElementScanner6

<R,​P>
- - javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8<R,​P>

javax.lang.model.util.ElementScanner6

<R,​P>

- javax.lang.model.util.ElementScanner7

<R,​P>
- - javax.lang.model.util.ElementScanner8<R,​P>

javax.lang.model.util.ElementScanner7

<R,​P>

- javax.lang.model.util.ElementScanner8<R,​P>

javax.lang.model.util.ElementScanner8<R,​P>

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

**Direct Known Subclasses:** ElementScanner9

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
ElementScanner8<R,​P>

extends
ElementScanner7
<R,​P>
```

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

**Since:** 1.8
**See Also:** ElementScanner6

,

ElementScanner7

,

ElementScanner9

@SupportedSourceVersion

(

RELEASE_8

)
public class

ElementScanner8<R,​P>

extends

ElementScanner7

<R,​P>

A scanning visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

ElementScanner8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementScanner8

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

========== METHOD SUMMARY ===========

- Method Summary

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

ElementScanner8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementScanner8

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ElementScanner8

```java
protected ElementScanner8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner8

```java
protected ElementScanner8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

Constructor Detail

- ElementScanner8

```java
protected ElementScanner8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementScanner8

```java
protected ElementScanner8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### Constructor Detail

ElementScanner8

```java
protected ElementScanner8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### ElementScanner8

protected ElementScanner8()

Constructor for concrete subclasses; uses

null

for the
default value.

ElementScanner8

```java
protected ElementScanner8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the default value

---

#### ElementScanner8

protected ElementScanner8​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

---

