# Class AbstractElementVisitor9<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractElementVisitor9.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_11
)
public abstract class
AbstractElementVisitor9<R,​P>

extends
AbstractElementVisitor8
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

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

#### protected AbstractElementVisitor9()

Constructor for concrete subclasses to call.

---

### Method Details

#### public abstract
R
visitModule​(
ModuleElement
t,

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
- t

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- Visits a

ModuleElement

in a manner defined by a
subclass.

---

### Additional Sections

#### Class AbstractElementVisitor9<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor7

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor8

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor9<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.AbstractElementVisitor7

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor8

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor9<R,​P>

javax.lang.model.util.AbstractElementVisitor7

<R,​P>

- javax.lang.model.util.AbstractElementVisitor8

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor9<R,​P>

javax.lang.model.util.AbstractElementVisitor8

<R,​P>

- javax.lang.model.util.AbstractElementVisitor9<R,​P>

javax.lang.model.util.AbstractElementVisitor9<R,​P>

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
public abstract class
AbstractElementVisitor9<R,​P>

extends
AbstractElementVisitor8
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

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

**Since:** 9
**See Also:** AbstractElementVisitor6

,

AbstractElementVisitor7

,

AbstractElementVisitor8

@SupportedSourceVersion

(

RELEASE_11

)
public abstract class

AbstractElementVisitor9<R,​P>

extends

AbstractElementVisitor8

<R,​P>

A skeletal visitor of program elements with default behavior
appropriate for source versions

RELEASE_9

through

RELEASE_11

.

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

AbstractElementVisitor9

()

Constructor for concrete subclasses to call.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

R

visitModule

​(

ModuleElement

t,

P

p)

Visits a module element.

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

AbstractElementVisitor9

()

Constructor for concrete subclasses to call.

---

#### Constructor Summary

Constructor for concrete subclasses to call.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

R

visitModule

​(

ModuleElement

t,

P

p)

Visits a module element.

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

Visits a module element.

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

- AbstractElementVisitor9

```java
protected AbstractElementVisitor9()
```

Constructor for concrete subclasses to call.

============ METHOD DETAIL ==========

- Method Detail

- visitModule

```java
public abstract
R
visitModule​(
ModuleElement
t,

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
**Implementation Requirements:** Visits a

ModuleElement

in a manner defined by a
subclass.
**Parameters:** t

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

Constructor Detail

- AbstractElementVisitor9

```java
protected AbstractElementVisitor9()
```

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractElementVisitor9

```java
protected AbstractElementVisitor9()
```

Constructor for concrete subclasses to call.

---

#### AbstractElementVisitor9

protected AbstractElementVisitor9()

Constructor for concrete subclasses to call.

Method Detail

- visitModule

```java
public abstract
R
visitModule​(
ModuleElement
t,

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
**Implementation Requirements:** Visits a

ModuleElement

in a manner defined by a
subclass.
**Parameters:** t

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### Method Detail

visitModule

```java
public abstract
R
visitModule​(
ModuleElement
t,

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
**Implementation Requirements:** Visits a

ModuleElement

in a manner defined by a
subclass.
**Parameters:** t

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitModule

public abstract

R

visitModule​(

ModuleElement

t,

P

p)

Visits a module element.

---

