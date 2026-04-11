# Class AbstractTypeVisitor8<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractTypeVisitor8.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_8
)
public abstract class
AbstractTypeVisitor8<R,​P>

extends
AbstractTypeVisitor7
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_8

source version.

WARNING:

The

TypeVisitor

interface implemented
by this class may have methods added to it in the future to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.
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

method. A new abstract type visitor
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

#### protected AbstractTypeVisitor8()

Constructor for concrete subclasses to call.

---

### Method Details

#### public abstract
R
visitIntersection​(
IntersectionType
t,

P
p)

Visits an

IntersectionType

in a manner defined by a subclass.

**Specified by:**
- visitIntersection

in interface

TypeVisitor

<

R

,​

P

>

**Overrides:**
- visitIntersection

in class

AbstractTypeVisitor6

<

R

,​

P

>

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit as defined by a subclass

---

### Additional Sections

#### Class AbstractTypeVisitor8<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.AbstractTypeVisitor7

<R,​P>
- - javax.lang.model.util.AbstractTypeVisitor8<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.AbstractTypeVisitor7

<R,​P>
- - javax.lang.model.util.AbstractTypeVisitor8<R,​P>

javax.lang.model.util.AbstractTypeVisitor7

<R,​P>

- javax.lang.model.util.AbstractTypeVisitor8<R,​P>

javax.lang.model.util.AbstractTypeVisitor8<R,​P>

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

**All Implemented Interfaces:** TypeVisitor

<R,​P>

**Direct Known Subclasses:** AbstractTypeVisitor9

```java
@SupportedSourceVersion
(
RELEASE_8
)
public abstract class
AbstractTypeVisitor8<R,​P>

extends
AbstractTypeVisitor7
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_8

source version.

WARNING:

The

TypeVisitor

interface implemented
by this class may have methods added to it in the future to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.
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

method. A new abstract type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.8
**See Also:** AbstractTypeVisitor6

,

AbstractTypeVisitor7

,

AbstractTypeVisitor9

@SupportedSourceVersion

(

RELEASE_8

)
public abstract class

AbstractTypeVisitor8<R,​P>

extends

AbstractTypeVisitor7

<R,​P>

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_8

source version.

WARNING:

The

TypeVisitor

interface implemented
by this class may have methods added to it in the future to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.
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

method. A new abstract type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

WARNING:

The

TypeVisitor

interface implemented
by this class may have methods added to it in the future to
accommodate new, currently unknown, language structures added to
future versions of the Java™ programming language.
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

method. A new abstract type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract type visitor
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

AbstractTypeVisitor8

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an

IntersectionType

in a manner defined by a subclass.

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

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

- Methods declared in interface javax.lang.model.type.

TypeVisitor

visitArray

,

visitDeclared

,

visitError

,

visitExecutable

,

visitNoType

,

visitNull

,

visitPrimitive

,

visitTypeVariable

,

visitWildcard

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractTypeVisitor8

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an

IntersectionType

in a manner defined by a subclass.

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

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

- Methods declared in interface javax.lang.model.type.

TypeVisitor

visitArray

,

visitDeclared

,

visitError

,

visitExecutable

,

visitNoType

,

visitNull

,

visitPrimitive

,

visitTypeVariable

,

visitWildcard

---

#### Method Summary

Visits an

IntersectionType

in a manner defined by a subclass.

Methods declared in class javax.lang.model.util.

AbstractTypeVisitor7

visitUnion

---

#### Methods declared in class javax.lang.model.util. AbstractTypeVisitor7

Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

visit

,

visit

,

visitUnknown

---

#### Methods declared in class javax.lang.model.util. AbstractTypeVisitor6

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

Methods declared in interface javax.lang.model.type.

TypeVisitor

visitArray

,

visitDeclared

,

visitError

,

visitExecutable

,

visitNoType

,

visitNull

,

visitPrimitive

,

visitTypeVariable

,

visitWildcard

---

#### Methods declared in interface javax.lang.model.type. TypeVisitor

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractTypeVisitor8

```java
protected AbstractTypeVisitor8()
```

Constructor for concrete subclasses to call.

============ METHOD DETAIL ==========

- Method Detail

- visitIntersection

```java
public abstract
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an

IntersectionType

in a manner defined by a subclass.

**Specified by:** visitIntersection

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitIntersection

in class

AbstractTypeVisitor6

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit as defined by a subclass

Constructor Detail

- AbstractTypeVisitor8

```java
protected AbstractTypeVisitor8()
```

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractTypeVisitor8

```java
protected AbstractTypeVisitor8()
```

Constructor for concrete subclasses to call.

---

#### AbstractTypeVisitor8

protected AbstractTypeVisitor8()

Constructor for concrete subclasses to call.

Method Detail

- visitIntersection

```java
public abstract
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an

IntersectionType

in a manner defined by a subclass.

**Specified by:** visitIntersection

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitIntersection

in class

AbstractTypeVisitor6

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit as defined by a subclass

---

#### Method Detail

visitIntersection

```java
public abstract
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an

IntersectionType

in a manner defined by a subclass.

**Specified by:** visitIntersection

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitIntersection

in class

AbstractTypeVisitor6

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit as defined by a subclass

---

#### visitIntersection

public abstract

R

visitIntersection​(

IntersectionType

t,

P

p)

Visits an

IntersectionType

in a manner defined by a subclass.

---

