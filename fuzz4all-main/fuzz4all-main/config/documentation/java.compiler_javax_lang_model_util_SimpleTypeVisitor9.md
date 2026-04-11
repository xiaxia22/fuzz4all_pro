# Class SimpleTypeVisitor9<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleTypeVisitor9.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_11
)
public class
SimpleTypeVisitor9<R,​P>

extends
SimpleTypeVisitor8
<R,​P>
```

A simple visitor of types with default behavior appropriate for
source versions

RELEASE_9

through

RELEASE_11

.

Visit methods corresponding to

RELEASE_9

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

#### protected SimpleTypeVisitor9()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected SimpleTypeVisitor9​(
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

*No entries found.*

### Additional Sections

#### Class SimpleTypeVisitor9<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor9<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor9<R,​P>

javax.lang.model.util.SimpleTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor7

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor8

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor9<R,​P>

javax.lang.model.util.SimpleTypeVisitor7

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor8

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor9<R,​P>

javax.lang.model.util.SimpleTypeVisitor8

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor9<R,​P>

javax.lang.model.util.SimpleTypeVisitor9<R,​P>

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

```java
@SupportedSourceVersion
(
RELEASE_11
)
public class
SimpleTypeVisitor9<R,​P>

extends
SimpleTypeVisitor8
<R,​P>
```

A simple visitor of types with default behavior appropriate for
source versions

RELEASE_9

through

RELEASE_11

.

Visit methods corresponding to

RELEASE_9

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

**Since:** 9
**See Also:** SimpleTypeVisitor6

,

SimpleTypeVisitor7

,

SimpleTypeVisitor8

@SupportedSourceVersion

(

RELEASE_11

)
public class

SimpleTypeVisitor9<R,​P>

extends

SimpleTypeVisitor8

<R,​P>

A simple visitor of types with default behavior appropriate for
source versions

RELEASE_9

through

RELEASE_11

.

Visit methods corresponding to

RELEASE_9

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

SimpleTypeVisitor9

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleTypeVisitor9

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.lang.model.util.

SimpleTypeVisitor8

visitIntersection

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

SimpleTypeVisitor9

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleTypeVisitor9

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

SimpleTypeVisitor8

visitIntersection

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

Methods declared in class javax.lang.model.util.

SimpleTypeVisitor8

visitIntersection

---

#### Methods declared in class javax.lang.model.util. SimpleTypeVisitor8

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

- SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

Constructor Detail

- SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9​(
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

SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleTypeVisitor9

protected SimpleTypeVisitor9()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleTypeVisitor9

```java
protected SimpleTypeVisitor9​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### SimpleTypeVisitor9

protected SimpleTypeVisitor9​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

---

