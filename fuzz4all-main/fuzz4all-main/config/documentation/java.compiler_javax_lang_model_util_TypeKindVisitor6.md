# Class TypeKindVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\TypeKindVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
TypeKindVisitor6<R,​P>

extends
SimpleTypeVisitor6
<R,​P>
```

A visitor of types based on their

kind

with
default behavior appropriate for the

RELEASE_6

source version. For

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

#### @Deprecated
(
since
="9")
protected TypeKindVisitor6()

Constructor for concrete subclasses to call; uses

null

for the default value.

---

#### @Deprecated
(
since
="9")
protected TypeKindVisitor6​(
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
visitPrimitive​(
PrimitiveType
t,

P
p)

Visits a primitive type.

**Specified by:**
- visitPrimitive

in interface

TypeVisitor

<

R

,​

P

>

**Overrides:**
- visitPrimitive

in class

SimpleTypeVisitor6

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
- the result of the kind-specific visit method

**Implementation Requirements:**
- This implementation dispatches to the visit method for
the specific

kind

of primitive type:

BOOLEAN

,

BYTE

, etc.

---

#### public
R
visitPrimitiveAsBoolean​(
PrimitiveType
t,

P
p)

Visits a

BOOLEAN

primitive type.

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

#### public
R
visitPrimitiveAsByte​(
PrimitiveType
t,

P
p)

Visits a

BYTE

primitive type.

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

#### public
R
visitPrimitiveAsShort​(
PrimitiveType
t,

P
p)

Visits a

SHORT

primitive type.

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

#### public
R
visitPrimitiveAsInt​(
PrimitiveType
t,

P
p)

Visits an

INT

primitive type.

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

#### public
R
visitPrimitiveAsLong​(
PrimitiveType
t,

P
p)

Visits a

LONG

primitive type.

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

#### public
R
visitPrimitiveAsChar​(
PrimitiveType
t,

P
p)

Visits a

CHAR

primitive type.

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

#### public
R
visitPrimitiveAsFloat​(
PrimitiveType
t,

P
p)

Visits a

FLOAT

primitive type.

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

#### public
R
visitPrimitiveAsDouble​(
PrimitiveType
t,

P
p)

Visits a

DOUBLE

primitive type.

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

#### public
R
visitNoType​(
NoType
t,

P
p)

Visits a

NoType

instance.

**Specified by:**
- visitNoType

in interface

TypeVisitor

<

R

,​

P

>

**Overrides:**
- visitNoType

in class

SimpleTypeVisitor6

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
- the result of the kind-specific visit method

**Implementation Requirements:**
- This implementation dispatches to the visit method for
the specific

kind

of pseudo-type:

VOID

,

PACKAGE

,

MODULE

, or

NONE

.

---

#### public
R
visitNoTypeAsVoid​(
NoType
t,

P
p)

Visits a

VOID

pseudo-type.

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

#### public
R
visitNoTypeAsPackage​(
NoType
t,

P
p)

Visits a

PACKAGE

pseudo-type.

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

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

visitUnknown

**Since:**
- 10

**Implementation Requirements:**
- This implementation calls

visitUnknown

.

---

#### public
R
visitNoTypeAsNone​(
NoType
t,

P
p)

Visits a

NONE

pseudo-type.

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

#### Class TypeKindVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor6<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor6

<R,​P>
- - javax.lang.model.util.TypeKindVisitor6<R,​P>

javax.lang.model.util.SimpleTypeVisitor6

<R,​P>

- javax.lang.model.util.TypeKindVisitor6<R,​P>

javax.lang.model.util.TypeKindVisitor6<R,​P>

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

**Direct Known Subclasses:** TypeKindVisitor7

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
TypeKindVisitor6<R,​P>

extends
SimpleTypeVisitor6
<R,​P>
```

A visitor of types based on their

kind

with
default behavior appropriate for the

RELEASE_6

source version. For

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

**Since:** 1.6
**See Also:** TypeKindVisitor7

,

TypeKindVisitor8

@SupportedSourceVersion

(

RELEASE_6

)
public class

TypeKindVisitor6<R,​P>

extends

SimpleTypeVisitor6

<R,​P>

A visitor of types based on their

kind

with
default behavior appropriate for the

RELEASE_6

source version. For

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

TypeKindVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

TypeKindVisitor6

​(

R

defaultValue)

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

visitNoType

​(

NoType

t,

P

p)

Visits a

NoType

instance.

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

R

visitNoTypeAsNone

​(

NoType

t,

P

p)

Visits a

NONE

pseudo-type.

R

visitNoTypeAsPackage

​(

NoType

t,

P

p)

Visits a

PACKAGE

pseudo-type.

R

visitNoTypeAsVoid

​(

NoType

t,

P

p)

Visits a

VOID

pseudo-type.

R

visitPrimitive

​(

PrimitiveType

t,

P

p)

Visits a primitive type.

R

visitPrimitiveAsBoolean

​(

PrimitiveType

t,

P

p)

Visits a

BOOLEAN

primitive type.

R

visitPrimitiveAsByte

​(

PrimitiveType

t,

P

p)

Visits a

BYTE

primitive type.

R

visitPrimitiveAsChar

​(

PrimitiveType

t,

P

p)

Visits a

CHAR

primitive type.

R

visitPrimitiveAsDouble

​(

PrimitiveType

t,

P

p)

Visits a

DOUBLE

primitive type.

R

visitPrimitiveAsFloat

​(

PrimitiveType

t,

P

p)

Visits a

FLOAT

primitive type.

R

visitPrimitiveAsInt

​(

PrimitiveType

t,

P

p)

Visits an

INT

primitive type.

R

visitPrimitiveAsLong

​(

PrimitiveType

t,

P

p)

Visits a

LONG

primitive type.

R

visitPrimitiveAsShort

​(

PrimitiveType

t,

P

p)

Visits a

SHORT

primitive type.

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

visitIntersection

,

visitUnion

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

TypeKindVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

TypeKindVisitor6

​(

R

defaultValue)

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

visitNoType

​(

NoType

t,

P

p)

Visits a

NoType

instance.

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

R

visitNoTypeAsNone

​(

NoType

t,

P

p)

Visits a

NONE

pseudo-type.

R

visitNoTypeAsPackage

​(

NoType

t,

P

p)

Visits a

PACKAGE

pseudo-type.

R

visitNoTypeAsVoid

​(

NoType

t,

P

p)

Visits a

VOID

pseudo-type.

R

visitPrimitive

​(

PrimitiveType

t,

P

p)

Visits a primitive type.

R

visitPrimitiveAsBoolean

​(

PrimitiveType

t,

P

p)

Visits a

BOOLEAN

primitive type.

R

visitPrimitiveAsByte

​(

PrimitiveType

t,

P

p)

Visits a

BYTE

primitive type.

R

visitPrimitiveAsChar

​(

PrimitiveType

t,

P

p)

Visits a

CHAR

primitive type.

R

visitPrimitiveAsDouble

​(

PrimitiveType

t,

P

p)

Visits a

DOUBLE

primitive type.

R

visitPrimitiveAsFloat

​(

PrimitiveType

t,

P

p)

Visits a

FLOAT

primitive type.

R

visitPrimitiveAsInt

​(

PrimitiveType

t,

P

p)

Visits an

INT

primitive type.

R

visitPrimitiveAsLong

​(

PrimitiveType

t,

P

p)

Visits a

LONG

primitive type.

R

visitPrimitiveAsShort

​(

PrimitiveType

t,

P

p)

Visits a

SHORT

primitive type.

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

visitIntersection

,

visitUnion

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

NoType

instance.

Visits a

MODULE

pseudo-type.

Visits a

NONE

pseudo-type.

Visits a

PACKAGE

pseudo-type.

Visits a

VOID

pseudo-type.

Visits a primitive type.

Visits a

BOOLEAN

primitive type.

Visits a

BYTE

primitive type.

Visits a

CHAR

primitive type.

Visits a

DOUBLE

primitive type.

Visits a

FLOAT

primitive type.

Visits an

INT

primitive type.

Visits a

LONG

primitive type.

Visits a

SHORT

primitive type.

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

visitIntersection

,

visitUnion

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

- TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses

null

for the default value.

- TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

- visitPrimitive

```java
public
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Specified by:** visitPrimitive

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitPrimitive

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of primitive type:

BOOLEAN

,

BYTE

, etc.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitPrimitiveAsBoolean

```java
public
R
visitPrimitiveAsBoolean​(
PrimitiveType
t,

P
p)
```

Visits a

BOOLEAN

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsByte

```java
public
R
visitPrimitiveAsByte​(
PrimitiveType
t,

P
p)
```

Visits a

BYTE

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsShort

```java
public
R
visitPrimitiveAsShort​(
PrimitiveType
t,

P
p)
```

Visits a

SHORT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsInt

```java
public
R
visitPrimitiveAsInt​(
PrimitiveType
t,

P
p)
```

Visits an

INT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsLong

```java
public
R
visitPrimitiveAsLong​(
PrimitiveType
t,

P
p)
```

Visits a

LONG

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsChar

```java
public
R
visitPrimitiveAsChar​(
PrimitiveType
t,

P
p)
```

Visits a

CHAR

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsFloat

```java
public
R
visitPrimitiveAsFloat​(
PrimitiveType
t,

P
p)
```

Visits a

FLOAT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsDouble

```java
public
R
visitPrimitiveAsDouble​(
PrimitiveType
t,

P
p)
```

Visits a

DOUBLE

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNoType

```java
public
R
visitNoType​(
NoType
t,

P
p)
```

Visits a

NoType

instance.

**Specified by:** visitNoType

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitNoType

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of pseudo-type:

VOID

,

PACKAGE

,

MODULE

, or

NONE

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitNoTypeAsVoid

```java
public
R
visitNoTypeAsVoid​(
NoType
t,

P
p)
```

Visits a

VOID

pseudo-type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNoTypeAsPackage

```java
public
R
visitNoTypeAsPackage​(
NoType
t,

P
p)
```

Visits a

PACKAGE

pseudo-type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

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

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 10

- visitNoTypeAsNone

```java
public
R
visitNoTypeAsNone​(
NoType
t,

P
p)
```

Visits a

NONE

pseudo-type.

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

- TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses

null

for the default value.

- TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses

null

for the default value.

---

#### TypeKindVisitor6

@Deprecated

(

since

="9")
protected TypeKindVisitor6()

Constructor for concrete subclasses to call; uses

null

for the default value.

TypeKindVisitor6

```java
@Deprecated
(
since
="9")
protected TypeKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call; uses the argument
for the default value.

**Parameters:** defaultValue

- the value to assign to

SimpleTypeVisitor6.DEFAULT_VALUE

---

#### TypeKindVisitor6

@Deprecated

(

since

="9")
protected TypeKindVisitor6​(

R

defaultValue)

Constructor for concrete subclasses to call; uses the argument
for the default value.

Method Detail

- visitPrimitive

```java
public
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Specified by:** visitPrimitive

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitPrimitive

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of primitive type:

BOOLEAN

,

BYTE

, etc.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitPrimitiveAsBoolean

```java
public
R
visitPrimitiveAsBoolean​(
PrimitiveType
t,

P
p)
```

Visits a

BOOLEAN

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsByte

```java
public
R
visitPrimitiveAsByte​(
PrimitiveType
t,

P
p)
```

Visits a

BYTE

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsShort

```java
public
R
visitPrimitiveAsShort​(
PrimitiveType
t,

P
p)
```

Visits a

SHORT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsInt

```java
public
R
visitPrimitiveAsInt​(
PrimitiveType
t,

P
p)
```

Visits an

INT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsLong

```java
public
R
visitPrimitiveAsLong​(
PrimitiveType
t,

P
p)
```

Visits a

LONG

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsChar

```java
public
R
visitPrimitiveAsChar​(
PrimitiveType
t,

P
p)
```

Visits a

CHAR

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsFloat

```java
public
R
visitPrimitiveAsFloat​(
PrimitiveType
t,

P
p)
```

Visits a

FLOAT

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitPrimitiveAsDouble

```java
public
R
visitPrimitiveAsDouble​(
PrimitiveType
t,

P
p)
```

Visits a

DOUBLE

primitive type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNoType

```java
public
R
visitNoType​(
NoType
t,

P
p)
```

Visits a

NoType

instance.

**Specified by:** visitNoType

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitNoType

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of pseudo-type:

VOID

,

PACKAGE

,

MODULE

, or

NONE

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitNoTypeAsVoid

```java
public
R
visitNoTypeAsVoid​(
NoType
t,

P
p)
```

Visits a

VOID

pseudo-type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNoTypeAsPackage

```java
public
R
visitNoTypeAsPackage​(
NoType
t,

P
p)
```

Visits a

PACKAGE

pseudo-type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

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

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 10

- visitNoTypeAsNone

```java
public
R
visitNoTypeAsNone​(
NoType
t,

P
p)
```

Visits a

NONE

pseudo-type.

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

visitPrimitive

```java
public
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Specified by:** visitPrimitive

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitPrimitive

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of primitive type:

BOOLEAN

,

BYTE

, etc.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

---

#### visitPrimitive

public

R

visitPrimitive​(

PrimitiveType

t,

P

p)

Visits a primitive type.

visitPrimitiveAsBoolean

```java
public
R
visitPrimitiveAsBoolean​(
PrimitiveType
t,

P
p)
```

Visits a

BOOLEAN

primitive type.

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

#### visitPrimitiveAsBoolean

public

R

visitPrimitiveAsBoolean​(

PrimitiveType

t,

P

p)

Visits a

BOOLEAN

primitive type.

visitPrimitiveAsByte

```java
public
R
visitPrimitiveAsByte​(
PrimitiveType
t,

P
p)
```

Visits a

BYTE

primitive type.

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

#### visitPrimitiveAsByte

public

R

visitPrimitiveAsByte​(

PrimitiveType

t,

P

p)

Visits a

BYTE

primitive type.

visitPrimitiveAsShort

```java
public
R
visitPrimitiveAsShort​(
PrimitiveType
t,

P
p)
```

Visits a

SHORT

primitive type.

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

#### visitPrimitiveAsShort

public

R

visitPrimitiveAsShort​(

PrimitiveType

t,

P

p)

Visits a

SHORT

primitive type.

visitPrimitiveAsInt

```java
public
R
visitPrimitiveAsInt​(
PrimitiveType
t,

P
p)
```

Visits an

INT

primitive type.

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

#### visitPrimitiveAsInt

public

R

visitPrimitiveAsInt​(

PrimitiveType

t,

P

p)

Visits an

INT

primitive type.

visitPrimitiveAsLong

```java
public
R
visitPrimitiveAsLong​(
PrimitiveType
t,

P
p)
```

Visits a

LONG

primitive type.

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

#### visitPrimitiveAsLong

public

R

visitPrimitiveAsLong​(

PrimitiveType

t,

P

p)

Visits a

LONG

primitive type.

visitPrimitiveAsChar

```java
public
R
visitPrimitiveAsChar​(
PrimitiveType
t,

P
p)
```

Visits a

CHAR

primitive type.

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

#### visitPrimitiveAsChar

public

R

visitPrimitiveAsChar​(

PrimitiveType

t,

P

p)

Visits a

CHAR

primitive type.

visitPrimitiveAsFloat

```java
public
R
visitPrimitiveAsFloat​(
PrimitiveType
t,

P
p)
```

Visits a

FLOAT

primitive type.

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

#### visitPrimitiveAsFloat

public

R

visitPrimitiveAsFloat​(

PrimitiveType

t,

P

p)

Visits a

FLOAT

primitive type.

visitPrimitiveAsDouble

```java
public
R
visitPrimitiveAsDouble​(
PrimitiveType
t,

P
p)
```

Visits a

DOUBLE

primitive type.

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

#### visitPrimitiveAsDouble

public

R

visitPrimitiveAsDouble​(

PrimitiveType

t,

P

p)

Visits a

DOUBLE

primitive type.

visitNoType

```java
public
R
visitNoType​(
NoType
t,

P
p)
```

Visits a

NoType

instance.

**Specified by:** visitNoType

in interface

TypeVisitor

<

R

,​

P

>
**Overrides:** visitNoType

in class

SimpleTypeVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of pseudo-type:

VOID

,

PACKAGE

,

MODULE

, or

NONE

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

---

#### visitNoType

public

R

visitNoType​(

NoType

t,

P

p)

Visits a

NoType

instance.

visitNoTypeAsVoid

```java
public
R
visitNoTypeAsVoid​(
NoType
t,

P
p)
```

Visits a

VOID

pseudo-type.

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

#### visitNoTypeAsVoid

public

R

visitNoTypeAsVoid​(

NoType

t,

P

p)

Visits a

VOID

pseudo-type.

visitNoTypeAsPackage

```java
public
R
visitNoTypeAsPackage​(
NoType
t,

P
p)
```

Visits a

PACKAGE

pseudo-type.

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

#### visitNoTypeAsPackage

public

R

visitNoTypeAsPackage​(

NoType

t,

P

p)

Visits a

PACKAGE

pseudo-type.

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

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
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

visitNoTypeAsNone

```java
public
R
visitNoTypeAsNone​(
NoType
t,

P
p)
```

Visits a

NONE

pseudo-type.

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

#### visitNoTypeAsNone

public

R

visitNoTypeAsNone​(

NoType

t,

P

p)

Visits a

NONE

pseudo-type.

---

