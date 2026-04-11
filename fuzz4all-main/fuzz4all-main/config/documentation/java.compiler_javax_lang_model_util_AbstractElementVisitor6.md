# Class AbstractElementVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractElementVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractElementVisitor6<R,​P>

extends
Object

implements
ElementVisitor
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

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

method. A new abstract element visitor
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

#### @Deprecated
(
since
="9")
protected AbstractElementVisitor6()

Constructor for concrete subclasses to call.

---

### Method Details

#### public final
R
visit​(
Element
e,

P
p)

Visits any program element as if by passing itself to that
element's

accept

method. The invocation

v.visit(elem, p)

is equivalent to

elem.accept(v,
p)

.

**Specified by:**
- visit

in interface

ElementVisitor

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
- a visitor-specified result

---

#### public final
R
visit​(
Element
e)

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(elem)

is equivalent to

elem.accept(v,
null)

.

**Specified by:**
- visit

in interface

ElementVisitor

<

R

,​

P

>

**Parameters:**
- e

- the element to visit

**Returns:**
- a visitor-specified result

---

#### public
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

**Specified by:**
- visitUnknown

in interface

ElementVisitor

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
- a visitor-specified result

**Throws:**
- UnknownElementException

- a visitor implementation may optionally throw this exception

**Implementation Requirements:**
- The default implementation of this method in

AbstractElementVisitor6

will always throw

new UnknownElementException(e, p)

.
This behavior is not required of a subclass.

---

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
- Visits a

ModuleElement

by calling

visitUnknown

.

---

### Additional Sections

#### Class AbstractElementVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6<R,​P>

javax.lang.model.util.AbstractElementVisitor6<R,​P>

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

**Direct Known Subclasses:** AbstractElementVisitor7

,

ElementScanner6

,

SimpleElementVisitor6

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractElementVisitor6<R,​P>

extends
Object

implements
ElementVisitor
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

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

method. A new abstract element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.6
**See Also:** AbstractElementVisitor7

,

AbstractElementVisitor8

,

AbstractElementVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public abstract class

AbstractElementVisitor6<R,​P>

extends

Object

implements

ElementVisitor

<R,​P>

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

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

method. A new abstract element visitor
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

method. A new abstract element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractElementVisitor6

()

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

visit

​(

Element

e)

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter.

R

visit

​(

Element

e,

P

p)

Visits any program element as if by passing itself to that
element's

accept

method.

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

R

visitUnknown

​(

Element

e,

P

p)

Visits an unknown kind of element.

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

- Methods declared in interface javax.lang.model.element.

ElementVisitor

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

,

visitVariable

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractElementVisitor6

()

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

visit

​(

Element

e)

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter.

R

visit

​(

Element

e,

P

p)

Visits any program element as if by passing itself to that
element's

accept

method.

R

visitModule

​(

ModuleElement

e,

P

p)

Visits a module element.

R

visitUnknown

​(

Element

e,

P

p)

Visits an unknown kind of element.

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

- Methods declared in interface javax.lang.model.element.

ElementVisitor

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

,

visitVariable

---

#### Method Summary

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter.

Visits any program element as if by passing itself to that
element's

accept

method.

Visits a module element.

Visits an unknown kind of element.

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

Methods declared in interface javax.lang.model.element.

ElementVisitor

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

,

visitVariable

---

#### Methods declared in interface javax.lang.model.element. ElementVisitor

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractElementVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

============ METHOD DETAIL ==========

- Method Detail

- visit

```java
public final
R
visit​(
Element
e,

P
p)
```

Visits any program element as if by passing itself to that
element's

accept

method. The invocation

v.visit(elem, p)

is equivalent to

elem.accept(v,
p)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
Element
e)
```

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(elem)

is equivalent to

elem.accept(v,
null)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

- visitUnknown

```java
public
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

**Specified by:** visitUnknown

in interface

ElementVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractElementVisitor6

will always throw

new UnknownElementException(e, p)

.
This behavior is not required of a subclass.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

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
**Implementation Requirements:** Visits a

ModuleElement

by calling

visitUnknown

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 9

Constructor Detail

- AbstractElementVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractElementVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### AbstractElementVisitor6

@Deprecated

(

since

="9")
protected AbstractElementVisitor6()

Constructor for concrete subclasses to call.

Method Detail

- visit

```java
public final
R
visit​(
Element
e,

P
p)
```

Visits any program element as if by passing itself to that
element's

accept

method. The invocation

v.visit(elem, p)

is equivalent to

elem.accept(v,
p)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
Element
e)
```

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(elem)

is equivalent to

elem.accept(v,
null)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

- visitUnknown

```java
public
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

**Specified by:** visitUnknown

in interface

ElementVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractElementVisitor6

will always throw

new UnknownElementException(e, p)

.
This behavior is not required of a subclass.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

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
**Implementation Requirements:** Visits a

ModuleElement

by calling

visitUnknown

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
public final
R
visit​(
Element
e,

P
p)
```

Visits any program element as if by passing itself to that
element's

accept

method. The invocation

v.visit(elem, p)

is equivalent to

elem.accept(v,
p)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

Element

e,

P

p)

Visits any program element as if by passing itself to that
element's

accept

method. The invocation

v.visit(elem, p)

is equivalent to

elem.accept(v,
p)

.

visit

```java
public final
R
visit​(
Element
e)
```

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(elem)

is equivalent to

elem.accept(v,
null)

.

**Specified by:** visit

in interface

ElementVisitor

<

R

,​

P

>
**Parameters:** e

- the element to visit
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

Element

e)

Visits any program element as if by passing itself to that
element's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(elem)

is equivalent to

elem.accept(v,
null)

.

visitUnknown

```java
public
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

**Specified by:** visitUnknown

in interface

ElementVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractElementVisitor6

will always throw

new UnknownElementException(e, p)

.
This behavior is not required of a subclass.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownElementException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

public

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
**Implementation Requirements:** Visits a

ModuleElement

by calling

visitUnknown

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 9

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

