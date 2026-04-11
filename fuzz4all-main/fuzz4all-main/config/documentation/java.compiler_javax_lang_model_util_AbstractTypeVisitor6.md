# Class AbstractTypeVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractTypeVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractTypeVisitor6<R,​P>

extends
Object

implements
TypeVisitor
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_6

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

#### @Deprecated
(
since
="9")
protected AbstractTypeVisitor6()

Constructor for concrete subclasses to call.

---

### Method Details

#### public final
R
visit​(
TypeMirror
t,

P
p)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method. The
invocation

v.visit(t, p)

is equivalent to

t.accept(v, p)

.

**Specified by:**
- visit

in interface

TypeVisitor

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
- a visitor-specified result

---

#### public final
R
visit​(
TypeMirror
t)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(t)

is equivalent to

t.accept(v, null)

.

**Specified by:**
- visit

in interface

TypeVisitor

<

R

,​

P

>

**Parameters:**
- t

- the type to visit

**Returns:**
- a visitor-specified result

---

#### public
R
visitUnion​(
UnionType
t,

P
p)

Visits a union type.

**Specified by:**
- visitUnion

in interface

TypeVisitor

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

visitUnknown

**Since:**
- 1.7

**Implementation Requirements:**
- Visits a

UnionType

element by calling

visitUnknown

.

---

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

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

visitUnknown

**Since:**
- 1.8

**Implementation Requirements:**
- Visits an

IntersectionType

element by calling

visitUnknown

.

---

#### public
R
visitUnknown​(
TypeMirror
t,

P
p)

Visits an unknown kind of type.
This can occur if the language evolves and new kinds
of types are added to the

TypeMirror

hierarchy.

**Specified by:**
- visitUnknown

in interface

TypeVisitor

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
- a visitor-specified result

**Throws:**
- UnknownTypeException

- a visitor implementation may optionally throw this exception

**Implementation Requirements:**
- The default implementation of this method in

AbstractTypeVisitor6

will always throw

new UnknownTypeException(t, p)

. This behavior is not required of a
subclass.

---

### Additional Sections

#### Class AbstractTypeVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6<R,​P>

javax.lang.model.util.AbstractTypeVisitor6<R,​P>

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

**Direct Known Subclasses:** AbstractTypeVisitor7

,

SimpleTypeVisitor6

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractTypeVisitor6<R,​P>

extends
Object

implements
TypeVisitor
<R,​P>
```

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_6

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

**Since:** 1.6
**See Also:** AbstractTypeVisitor7

,

AbstractTypeVisitor8

,

AbstractTypeVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public abstract class

AbstractTypeVisitor6<R,​P>

extends

Object

implements

TypeVisitor

<R,​P>

A skeletal visitor of types with default behavior appropriate for
the

RELEASE_6

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

AbstractTypeVisitor6

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

TypeMirror

t)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter.

R

visit

​(

TypeMirror

t,

P

p)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method.

R

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

R

visitUnion

​(

UnionType

t,

P

p)

Visits a union type.

R

visitUnknown

​(

TypeMirror

t,

P

p)

Visits an unknown kind of type.

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

AbstractTypeVisitor6

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

TypeMirror

t)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter.

R

visit

​(

TypeMirror

t,

P

p)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method.

R

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

R

visitUnion

​(

UnionType

t,

P

p)

Visits a union type.

R

visitUnknown

​(

TypeMirror

t,

P

p)

Visits an unknown kind of type.

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

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter.

Visits any type mirror as if by passing itself to that type
mirror's

accept

method.

Visits an intersection type.

Visits a union type.

Visits an unknown kind of type.

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

- AbstractTypeVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractTypeVisitor6()
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
TypeMirror
t,

P
p)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method. The
invocation

v.visit(t, p)

is equivalent to

t.accept(v, p)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
TypeMirror
t)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(t)

is equivalent to

t.accept(v, null)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Returns:** a visitor-specified result

- visitUnion

```java
public
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** Visits a

UnionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

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
**Implementation Requirements:** Visits an

IntersectionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.8

- visitUnknown

```java
public
R
visitUnknown​(
TypeMirror
t,

P
p)
```

Visits an unknown kind of type.
This can occur if the language evolves and new kinds
of types are added to the

TypeMirror

hierarchy.

**Specified by:** visitUnknown

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractTypeVisitor6

will always throw

new UnknownTypeException(t, p)

. This behavior is not required of a
subclass.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

Constructor Detail

- AbstractTypeVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractTypeVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractTypeVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractTypeVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### AbstractTypeVisitor6

@Deprecated

(

since

="9")
protected AbstractTypeVisitor6()

Constructor for concrete subclasses to call.

Method Detail

- visit

```java
public final
R
visit​(
TypeMirror
t,

P
p)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method. The
invocation

v.visit(t, p)

is equivalent to

t.accept(v, p)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
TypeMirror
t)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(t)

is equivalent to

t.accept(v, null)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Returns:** a visitor-specified result

- visitUnion

```java
public
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** Visits a

UnionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

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
**Implementation Requirements:** Visits an

IntersectionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.8

- visitUnknown

```java
public
R
visitUnknown​(
TypeMirror
t,

P
p)
```

Visits an unknown kind of type.
This can occur if the language evolves and new kinds
of types are added to the

TypeMirror

hierarchy.

**Specified by:** visitUnknown

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractTypeVisitor6

will always throw

new UnknownTypeException(t, p)

. This behavior is not required of a
subclass.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

---

#### Method Detail

visit

```java
public final
R
visit​(
TypeMirror
t,

P
p)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method. The
invocation

v.visit(t, p)

is equivalent to

t.accept(v, p)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

TypeMirror

t,

P

p)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method. The
invocation

v.visit(t, p)

is equivalent to

t.accept(v, p)

.

visit

```java
public final
R
visit​(
TypeMirror
t)
```

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(t)

is equivalent to

t.accept(v, null)

.

**Specified by:** visit

in interface

TypeVisitor

<

R

,​

P

>
**Parameters:** t

- the type to visit
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

TypeMirror

t)

Visits any type mirror as if by passing itself to that type
mirror's

accept

method and passing

null

for the additional parameter. The invocation

v.visit(t)

is equivalent to

t.accept(v, null)

.

visitUnion

```java
public
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Specified by:** visitUnion

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** Visits a

UnionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

---

#### visitUnion

public

R

visitUnion​(

UnionType

t,

P

p)

Visits a union type.

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
**Implementation Requirements:** Visits an

IntersectionType

element by calling

visitUnknown

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.8

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

visitUnknown

```java
public
R
visitUnknown​(
TypeMirror
t,

P
p)
```

Visits an unknown kind of type.
This can occur if the language evolves and new kinds
of types are added to the

TypeMirror

hierarchy.

**Specified by:** visitUnknown

in interface

TypeVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractTypeVisitor6

will always throw

new UnknownTypeException(t, p)

. This behavior is not required of a
subclass.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

public

R

visitUnknown​(

TypeMirror

t,

P

p)

Visits an unknown kind of type.
This can occur if the language evolves and new kinds
of types are added to the

TypeMirror

hierarchy.

---

