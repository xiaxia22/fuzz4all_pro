# Class AbstractTypeVisitor7<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractTypeVisitor7.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_7
)
public abstract class
AbstractTypeVisitor7<R,​P>

extends
AbstractTypeVisitor6
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_7

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

#### protected AbstractTypeVisitor7()

Constructor for concrete subclasses to call.

---

### Method Details

#### public abstract
R
visitUnion​(
UnionType
t,

P
p)

Visits a

UnionType

in a manner defined by a subclass.

**Specified by:**
- visitUnion

in interface

TypeVisitor

<

R

,​

P

>

**Overrides:**
- visitUnion

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

#### Class AbstractTypeVisitor7<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.AbstractTypeVisitor7<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.AbstractTypeVisitor7<R,​P>

javax.lang.model.util.AbstractTypeVisitor7<R,​P>

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

**Direct Known Subclasses:** AbstractTypeVisitor8

```java
@SupportedSourceVersion
(
RELEASE_7
)
public abstract class
AbstractTypeVisitor7<R,​P>

extends
AbstractTypeVisitor6
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_7

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

**Since:** 1.7
**See Also:** AbstractTypeVisitor6

,

AbstractTypeVisitor8

,

AbstractTypeVisitor9

@SupportedSourceVersion

(

RELEASE_7

)
public abstract class

AbstractTypeVisitor7<R,​P>

extends

AbstractTypeVisitor6

<R,​P>

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_7

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

AbstractTypeVisitor7

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

visitUnion

​(

UnionType

t,

P

p)

Visits a

UnionType

in a manner defined by a subclass.

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

visit

,

visit

,

visitIntersection

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

AbstractTypeVisitor7

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

visitUnion

​(

UnionType

t,

P

p)

Visits a

UnionType

in a manner defined by a subclass.

- Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

visit

,

visit

,

visitIntersection

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

Visits a

UnionType

in a manner defined by a subclass.

Methods declared in class javax.lang.model.util.

AbstractTypeVisitor6

visit

,

visit

,

visitIntersection

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

- AbstractTypeVisitor7

```java
protected AbstractTypeVisitor7()
```

Constructor for concrete subclasses to call.

============ METHOD DETAIL ==========

- Method Detail

- visitUnion

```java
public abstract
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a

UnionType

in a manner defined by a subclass.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitUnion

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

- AbstractTypeVisitor7

```java
protected AbstractTypeVisitor7()
```

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractTypeVisitor7

```java
protected AbstractTypeVisitor7()
```

Constructor for concrete subclasses to call.

---

#### AbstractTypeVisitor7

protected AbstractTypeVisitor7()

Constructor for concrete subclasses to call.

Method Detail

- visitUnion

```java
public abstract
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a

UnionType

in a manner defined by a subclass.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitUnion

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

visitUnion

```java
public abstract
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a

UnionType

in a manner defined by a subclass.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitUnion

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

#### visitUnion

public abstract

R

visitUnion​(

UnionType

t,

P

p)

Visits a

UnionType

in a manner defined by a subclass.

---

