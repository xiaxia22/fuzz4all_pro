# Class SimpleTypeVisitor8<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleTypeVisitor8.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
SimpleTypeVisitor8<R,​P>

extends
SimpleTypeVisitor7
<R,​P>
```

A simple visitor of types with default behavior appropriate for the

RELEASE_8

source version.

Visit methods corresponding to

RELEASE_8

and earlier
language constructs call

defaultAction

,
passing their arguments to

defaultAction

's corresponding
parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple type visitor
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

#### protected SimpleTypeVisitor8()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected SimpleTypeVisitor8​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

### Method Details

#### public
R
visitIntersection​(
IntersectionType
t,

P
p)

Visits an intersection type.

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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

### Additional Sections

#### Class SimpleTypeVisitor8<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8<R,​P>

javax.lang.model.util.SimpleTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8<R,​P>

javax.lang.model.util.SimpleTypeVisitor7

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor8<R,​P>

javax.lang.model.util.SimpleTypeVisitor8<R,​P>

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

**Direct Known Subclasses:** SimpleTypeVisitor9

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
SimpleTypeVisitor8<R,​P>

extends
SimpleTypeVisitor7
<R,​P>
```

A simple visitor of types with default behavior appropriate for the

RELEASE_8

source version.

Visit methods corresponding to

RELEASE_8

and earlier
language constructs call

defaultAction

,
passing their arguments to

defaultAction

's corresponding
parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.8
**See Also:** SimpleTypeVisitor6

,

SimpleTypeVisitor7

,

SimpleTypeVisitor9

@SupportedSourceVersion

(

RELEASE_8

)
public class

SimpleTypeVisitor8<R,​P>

extends

SimpleTypeVisitor7

<R,​P>

A simple visitor of types with default behavior appropriate for the

RELEASE_8

source version.

Visit methods corresponding to

RELEASE_8

and earlier
language constructs call

defaultAction

,
passing their arguments to

defaultAction

's corresponding
parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple type visitor
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

method. A new simple type visitor
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

method. A new simple type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new simple type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.lang.model.util.

SimpleTypeVisitor6

DEFAULT_VALUE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleTypeVisitor8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleTypeVisitor8

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

- Methods declared in class javax.lang.model.util.

SimpleTypeVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

SimpleTypeVisitor6

defaultAction

,

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

Field Summary

- Fields declared in class javax.lang.model.util.

SimpleTypeVisitor6

DEFAULT_VALUE

---

#### Field Summary

Fields declared in class javax.lang.model.util.

SimpleTypeVisitor6

DEFAULT_VALUE

---

#### Fields declared in class javax.lang.model.util. SimpleTypeVisitor6

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleTypeVisitor8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleTypeVisitor8

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

- Methods declared in class javax.lang.model.util.

SimpleTypeVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

SimpleTypeVisitor6

defaultAction

,

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

---

#### Method Summary

Visits an intersection type.

Methods declared in class javax.lang.model.util.

SimpleTypeVisitor7

visitUnion

---

#### Methods declared in class javax.lang.model.util. SimpleTypeVisitor7

Methods declared in class javax.lang.model.util.

SimpleTypeVisitor6

defaultAction

,

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

#### Methods declared in class javax.lang.model.util. SimpleTypeVisitor6

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

- visitIntersection

```java
public
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

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
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

Constructor Detail

- SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleTypeVisitor8

protected SimpleTypeVisitor8()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleTypeVisitor8

```java
protected SimpleTypeVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### SimpleTypeVisitor8

protected SimpleTypeVisitor8​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

- visitIntersection

```java
public
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

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
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### Method Detail

visitIntersection

```java
public
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

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
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitIntersection

public

R

visitIntersection​(

IntersectionType

t,

P

p)

Visits an intersection type.

---

