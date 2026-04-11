# Class AbstractAnnotationValueVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractAnnotationValueVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractAnnotationValueVisitor6<R,​P>

extends
Object

implements
AnnotationValueVisitor
<R,​P>
```

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version.

WARNING:

The

AnnotationValueVisitor

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

method. A new abstract annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

---

### Field Details

*No entries found.*

### Constructor Details

#### @Deprecated
(
since
="9")
protected AbstractAnnotationValueVisitor6()

Constructor for concrete subclasses to call.

---

### Method Details

#### public final
R
visit​(
AnnotationValue
av,

P
p)

Visits any annotation value as if by passing itself to that
value's

accept

. The invocation

v.visit(av, p)

is equivalent to

av.accept(v, p)

.

**Specified by:**
- visit

in interface

AnnotationValueVisitor

<

R

,​

P

>

**Parameters:**
- av

- the value to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### public final
R
visit​(
AnnotationValue
av)

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter. The invocation

v.visit(av)

is equivalent to

av.accept(v,
null)

.

**Specified by:**
- visit

in interface

AnnotationValueVisitor

<

R

,​

P

>

**Parameters:**
- av

- the value to visit

**Returns:**
- a visitor-specified result

---

#### public
R
visitUnknown​(
AnnotationValue
av,

P
p)

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

**Specified by:**
- visitUnknown

in interface

AnnotationValueVisitor

<

R

,​

P

>

**Parameters:**
- av

- the unknown value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

**Implementation Requirements:**
- The default implementation of this method in

AbstractAnnotationValueVisitor6

will always throw

new UnknownAnnotationValueException(av, p)

. This behavior is not
required of a subclass.

---

### Additional Sections

#### Class AbstractAnnotationValueVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractAnnotationValueVisitor6<R,​P>

javax.lang.model.util.AbstractAnnotationValueVisitor6<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

**All Implemented Interfaces:** AnnotationValueVisitor

<R,​P>

**Direct Known Subclasses:** AbstractAnnotationValueVisitor7

,

SimpleAnnotationValueVisitor6

```java
@SupportedSourceVersion
(
RELEASE_6
)
public abstract class
AbstractAnnotationValueVisitor6<R,​P>

extends
Object

implements
AnnotationValueVisitor
<R,​P>
```

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version.

WARNING:

The

AnnotationValueVisitor

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

method. A new abstract annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

**Since:** 1.6
**See Also:** AbstractAnnotationValueVisitor7

,

AbstractAnnotationValueVisitor8

,

AbstractAnnotationValueVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public abstract class

AbstractAnnotationValueVisitor6<R,​P>

extends

Object

implements

AnnotationValueVisitor

<R,​P>

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version.

WARNING:

The

AnnotationValueVisitor

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

method. A new abstract annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

WARNING:

The

AnnotationValueVisitor

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

method. A new abstract annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractAnnotationValueVisitor6

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

AnnotationValue

av)

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter.

R

visit

​(

AnnotationValue

av,

P

p)

Visits any annotation value as if by passing itself to that
value's

accept

.

R

visitUnknown

​(

AnnotationValue

av,

P

p)

Visits an unknown kind of annotation value.

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

AnnotationValueVisitor

visitAnnotation

,

visitArray

,

visitBoolean

,

visitByte

,

visitChar

,

visitDouble

,

visitEnumConstant

,

visitFloat

,

visitInt

,

visitLong

,

visitShort

,

visitString

,

visitType

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractAnnotationValueVisitor6

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

AnnotationValue

av)

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter.

R

visit

​(

AnnotationValue

av,

P

p)

Visits any annotation value as if by passing itself to that
value's

accept

.

R

visitUnknown

​(

AnnotationValue

av,

P

p)

Visits an unknown kind of annotation value.

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

AnnotationValueVisitor

visitAnnotation

,

visitArray

,

visitBoolean

,

visitByte

,

visitChar

,

visitDouble

,

visitEnumConstant

,

visitFloat

,

visitInt

,

visitLong

,

visitShort

,

visitString

,

visitType

---

#### Method Summary

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter.

Visits any annotation value as if by passing itself to that
value's

accept

.

Visits an unknown kind of annotation value.

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

AnnotationValueVisitor

visitAnnotation

,

visitArray

,

visitBoolean

,

visitByte

,

visitChar

,

visitDouble

,

visitEnumConstant

,

visitFloat

,

visitInt

,

visitLong

,

visitShort

,

visitString

,

visitType

---

#### Methods declared in interface javax.lang.model.element. AnnotationValueVisitor

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractAnnotationValueVisitor6()
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
AnnotationValue
av,

P
p)
```

Visits any annotation value as if by passing itself to that
value's

accept

. The invocation

v.visit(av, p)

is equivalent to

av.accept(v, p)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
AnnotationValue
av)
```

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter. The invocation

v.visit(av)

is equivalent to

av.accept(v,
null)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

- visitUnknown

```java
public
R
visitUnknown​(
AnnotationValue
av,

P
p)
```

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

**Specified by:** visitUnknown

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractAnnotationValueVisitor6

will always throw

new UnknownAnnotationValueException(av, p)

. This behavior is not
required of a subclass.
**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

Constructor Detail

- AbstractAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractAnnotationValueVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected AbstractAnnotationValueVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses to call.

---

#### AbstractAnnotationValueVisitor6

@Deprecated

(

since

="9")
protected AbstractAnnotationValueVisitor6()

Constructor for concrete subclasses to call.

Method Detail

- visit

```java
public final
R
visit​(
AnnotationValue
av,

P
p)
```

Visits any annotation value as if by passing itself to that
value's

accept

. The invocation

v.visit(av, p)

is equivalent to

av.accept(v, p)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
public final
R
visit​(
AnnotationValue
av)
```

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter. The invocation

v.visit(av)

is equivalent to

av.accept(v,
null)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

- visitUnknown

```java
public
R
visitUnknown​(
AnnotationValue
av,

P
p)
```

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

**Specified by:** visitUnknown

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractAnnotationValueVisitor6

will always throw

new UnknownAnnotationValueException(av, p)

. This behavior is not
required of a subclass.
**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### Method Detail

visit

```java
public final
R
visit​(
AnnotationValue
av,

P
p)
```

Visits any annotation value as if by passing itself to that
value's

accept

. The invocation

v.visit(av, p)

is equivalent to

av.accept(v, p)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

AnnotationValue

av,

P

p)

Visits any annotation value as if by passing itself to that
value's

accept

. The invocation

v.visit(av, p)

is equivalent to

av.accept(v, p)

.

visit

```java
public final
R
visit​(
AnnotationValue
av)
```

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter. The invocation

v.visit(av)

is equivalent to

av.accept(v,
null)

.

**Specified by:** visit

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

---

#### visit

public final

R

visit​(

AnnotationValue

av)

Visits an annotation value as if by passing itself to that
value's

accept

method passing

null

for the additional parameter. The invocation

v.visit(av)

is equivalent to

av.accept(v,
null)

.

visitUnknown

```java
public
R
visitUnknown​(
AnnotationValue
av,

P
p)
```

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

**Specified by:** visitUnknown

in interface

AnnotationValueVisitor

<

R

,​

P

>
**Implementation Requirements:** The default implementation of this method in

AbstractAnnotationValueVisitor6

will always throw

new UnknownAnnotationValueException(av, p)

. This behavior is not
required of a subclass.
**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitUnknown

public

R

visitUnknown​(

AnnotationValue

av,

P

p)

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

---

