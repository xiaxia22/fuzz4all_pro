# Class AbstractElementVisitor8<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractElementVisitor8.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_8
)
public abstract class
AbstractElementVisitor8<R,​P>

extends
AbstractElementVisitor7
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

#### protected AbstractElementVisitor8()

Constructor for concrete subclasses to call.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AbstractElementVisitor8<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor7

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor8<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.AbstractElementVisitor7

<R,​P>
- - javax.lang.model.util.AbstractElementVisitor8<R,​P>

javax.lang.model.util.AbstractElementVisitor7

<R,​P>

- javax.lang.model.util.AbstractElementVisitor8<R,​P>

javax.lang.model.util.AbstractElementVisitor8<R,​P>

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

**Direct Known Subclasses:** AbstractElementVisitor9

```java
@SupportedSourceVersion
(
RELEASE_8
)
public abstract class
AbstractElementVisitor8<R,​P>

extends
AbstractElementVisitor7
<R,​P>
```

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

**Since:** 1.8
**See Also:** AbstractElementVisitor6

,

AbstractElementVisitor7

,

AbstractElementVisitor9

@SupportedSourceVersion

(

RELEASE_8

)
public abstract class

AbstractElementVisitor8<R,​P>

extends

AbstractElementVisitor7

<R,​P>

A skeletal visitor of program elements with default behavior
appropriate for the

RELEASE_8

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

AbstractElementVisitor8

()

Constructor for concrete subclasses to call.

========== METHOD SUMMARY ===========

- Method Summary

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

AbstractElementVisitor8

()

Constructor for concrete subclasses to call.

---

#### Constructor Summary

Constructor for concrete subclasses to call.

Method Summary

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

- AbstractElementVisitor8

```java
protected AbstractElementVisitor8()
```

Constructor for concrete subclasses to call.

Constructor Detail

- AbstractElementVisitor8

```java
protected AbstractElementVisitor8()
```

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractElementVisitor8

```java
protected AbstractElementVisitor8()
```

Constructor for concrete subclasses to call.

---

#### AbstractElementVisitor8

protected AbstractElementVisitor8()

Constructor for concrete subclasses to call.

---

