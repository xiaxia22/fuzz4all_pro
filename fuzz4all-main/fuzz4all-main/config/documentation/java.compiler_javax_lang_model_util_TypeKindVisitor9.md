# Class TypeKindVisitor9<R,​P>

**Source:** `java.compiler\javax\lang\model\util\TypeKindVisitor9.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_11
)
public class
TypeKindVisitor9<R,​P>

extends
TypeKindVisitor8
<R,​P>
```

A visitor of types based on their

kind

with
default behavior appropriate for source versions

RELEASE_9

through

RELEASE_11

.

For

types

Xyz

that may have more than one
kind, the

visit

Xyz

methods in this class delegate
to the

visit

Xyz

As

Kind

method corresponding to the
first argument's kind. The

visit

Xyz

As

Kind

methods
call

defaultAction

, passing their arguments
to

defaultAction

's corresponding parameters.

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

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

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

#### protected TypeKindVisitor9()

Constructor for concrete subclasses to call; uses

null

for the default value.

---

#### protected TypeKindVisitor9​(
R
defaultValue)

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:**
- defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

### Method Details

#### public
R
visitNoTypeAsModule​(
NoType
t,

P
p)

Visits a

MODULE

pseudo-type.

**Overrides:**
- visitNoTypeAsModule

in class

TypeKindVisitor6

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

**Since:**
- 10

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

### Additional Sections

#### Class TypeKindVisitor9<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor7

<R,​P>
- - javax.lang.model.util.TypeKindVisitor8

<R,​P>
- - javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor7

<R,​P>
- - javax.lang.model.util.TypeKindVisitor8

<R,​P>
- - javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.SimpleTypeVisitor6

<R,​P>

- javax.lang.model.util.TypeKindVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor7

<R,​P>
- - javax.lang.model.util.TypeKindVisitor8

<R,​P>
- - javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.TypeKindVisitor6

<R,​P>

- javax.lang.model.util.TypeKindVisitor7

<R,​P>
- - javax.lang.model.util.TypeKindVisitor8

<R,​P>
- - javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.TypeKindVisitor7

<R,​P>

- javax.lang.model.util.TypeKindVisitor8

<R,​P>
- - javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.TypeKindVisitor8

<R,​P>

- javax.lang.model.util.TypeKindVisitor9<R,​P>

javax.lang.model.util.TypeKindVisitor9<R,​P>

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
TypeKindVisitor9<R,​P>

extends
TypeKindVisitor8
<R,​P>
```

A visitor of types based on their

kind

with
default behavior appropriate for source versions

RELEASE_9

through

RELEASE_11

.

For

types

Xyz

that may have more than one
kind, the

visit

Xyz

methods in this class delegate
to the

visit

Xyz

As

Kind

method corresponding to the
first argument's kind. The

visit

Xyz

As

Kind

methods
call

defaultAction

, passing their arguments
to

defaultAction

's corresponding parameters.

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

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

**Since:** 9
**See Also:** TypeKindVisitor6

,

TypeKindVisitor7

,

TypeKindVisitor8

@SupportedSourceVersion

(

RELEASE_11

)
public class

TypeKindVisitor9<R,​P>

extends

TypeKindVisitor8

<R,​P>

A visitor of types based on their

kind

with
default behavior appropriate for source versions

RELEASE_9

through

RELEASE_11

.

For

types

Xyz

that may have more than one
kind, the

visit

Xyz

methods in this class delegate
to the

visit

Xyz

As

Kind

method corresponding to the
first argument's kind. The

visit

Xyz

As

Kind

methods
call

defaultAction

, passing their arguments
to

defaultAction

's corresponding parameters.

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

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

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

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

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

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new type kind visitor class
will also be introduced to correspond to the new language level;
this visitor will have different default behavior for the visit
method in question. When the new visitor is introduced, all or
portions of this visitor may be deprecated.

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

TypeKindVisitor9

()

Constructor for concrete subclasses to call; uses

null

for the default value.

protected

TypeKindVisitor9

​(

R

defaultValue)

Constructor for concrete subclasses to call; uses the argument
for the default value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

visitNoTypeAsModule

​(

NoType

t,

P

p)

Visits a

MODULE

pseudo-type.

- Methods declared in class javax.lang.model.util.

TypeKindVisitor8

visitIntersection

- Methods declared in class javax.lang.model.util.

TypeKindVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

TypeKindVisitor6

visitNoType

,

visitNoTypeAsNone

,

visitNoTypeAsPackage

,

visitNoTypeAsVoid

,

visitPrimitive

,

visitPrimitiveAsBoolean

,

visitPrimitiveAsByte

,

visitPrimitiveAsChar

,

visitPrimitiveAsDouble

,

visitPrimitiveAsFloat

,

visitPrimitiveAsInt

,

visitPrimitiveAsLong

,

visitPrimitiveAsShort

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

visitNull

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

TypeKindVisitor9

()

Constructor for concrete subclasses to call; uses

null

for the default value.

protected

TypeKindVisitor9

​(

R

defaultValue)

Constructor for concrete subclasses to call; uses the argument
for the default value.

---

#### Constructor Summary

Constructor for concrete subclasses to call; uses

null

for the default value.

Constructor for concrete subclasses to call; uses the argument
for the default value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

R

visitNoTypeAsModule

​(

NoType

t,

P

p)

Visits a

MODULE

pseudo-type.

- Methods declared in class javax.lang.model.util.

TypeKindVisitor8

visitIntersection

- Methods declared in class javax.lang.model.util.

TypeKindVisitor7

visitUnion

- Methods declared in class javax.lang.model.util.

TypeKindVisitor6

visitNoType

,

visitNoTypeAsNone

,

visitNoTypeAsPackage

,

visitNoTypeAsVoid

,

visitPrimitive

,

visitPrimitiveAsBoolean

,

visitPrimitiveAsByte

,

visitPrimitiveAsChar

,

visitPrimitiveAsDouble

,

visitPrimitiveAsFloat

,

visitPrimitiveAsInt

,

visitPrimitiveAsLong

,

visitPrimitiveAsShort

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

visitNull

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

Visits a

MODULE

pseudo-type.

Methods declared in class javax.lang.model.util.

TypeKindVisitor8

visitIntersection

---

#### Methods declared in class javax.lang.model.util. TypeKindVisitor8

Methods declared in class javax.lang.model.util.

TypeKindVisitor7

visitUnion

---

#### Methods declared in class javax.lang.model.util. TypeKindVisitor7

Methods declared in class javax.lang.model.util.

TypeKindVisitor6

visitNoType

,

visitNoTypeAsNone

,

visitNoTypeAsPackage

,

visitNoTypeAsVoid

,

visitPrimitive

,

visitPrimitiveAsBoolean

,

visitPrimitiveAsByte

,

visitPrimitiveAsChar

,

visitPrimitiveAsDouble

,

visitPrimitiveAsFloat

,

visitPrimitiveAsInt

,

visitPrimitiveAsLong

,

visitPrimitiveAsShort

---

#### Methods declared in class javax.lang.model.util. TypeKindVisitor6

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

visitNull

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

- TypeKindVisitor9

```java
protected TypeKindVisitor9()
```

Constructor for concrete subclasses to call; uses

null

for the default value.

- TypeKindVisitor9

```java
protected TypeKindVisitor9​(
R
defaultValue)
```

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

- visitNoTypeAsModule

```java
public
R
visitNoTypeAsModule​(
NoType
t,

P
p)
```

Visits a

MODULE

pseudo-type.

**Overrides:** visitNoTypeAsModule

in class

TypeKindVisitor6

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
**Since:** 10

Constructor Detail

- TypeKindVisitor9

```java
protected TypeKindVisitor9()
```

Constructor for concrete subclasses to call; uses

null

for the default value.

- TypeKindVisitor9

```java
protected TypeKindVisitor9​(
R
defaultValue)
```

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

TypeKindVisitor9

```java
protected TypeKindVisitor9()
```

Constructor for concrete subclasses to call; uses

null

for the default value.

---

#### TypeKindVisitor9

protected TypeKindVisitor9()

Constructor for concrete subclasses to call; uses

null

for the default value.

TypeKindVisitor9

```java
protected TypeKindVisitor9​(
R
defaultValue)
```

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### TypeKindVisitor9

protected TypeKindVisitor9​(

R

defaultValue)

Constructor for concrete subclasses to call; uses the argument
for the default value.

Method Detail

- visitNoTypeAsModule

```java
public
R
visitNoTypeAsModule​(
NoType
t,

P
p)
```

Visits a

MODULE

pseudo-type.

**Overrides:** visitNoTypeAsModule

in class

TypeKindVisitor6

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
**Since:** 10

---

#### Method Detail

visitNoTypeAsModule

```java
public
R
visitNoTypeAsModule​(
NoType
t,

P
p)
```

Visits a

MODULE

pseudo-type.

**Overrides:** visitNoTypeAsModule

in class

TypeKindVisitor6

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
**Since:** 10

---

#### visitNoTypeAsModule

public

R

visitNoTypeAsModule​(

NoType

t,

P

p)

Visits a

MODULE

pseudo-type.

---

