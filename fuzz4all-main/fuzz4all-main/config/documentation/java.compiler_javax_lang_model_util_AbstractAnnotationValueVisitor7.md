# Class AbstractAnnotationValueVisitor7<R,​P>

**Source:** `java.compiler\javax\lang\model\util\AbstractAnnotationValueVisitor7.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_7
)
public abstract class
AbstractAnnotationValueVisitor7<R,​P>

extends
AbstractAnnotationValueVisitor6
<R,​P>
```

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_7

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

#### protected AbstractAnnotationValueVisitor7()

Constructor for concrete subclasses to call.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AbstractAnnotationValueVisitor7<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>
- - javax.lang.model.util.AbstractAnnotationValueVisitor7<R,​P>

javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>

- javax.lang.model.util.AbstractAnnotationValueVisitor7<R,​P>

javax.lang.model.util.AbstractAnnotationValueVisitor7<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

**All Implemented Interfaces:** AnnotationValueVisitor

<R,​P>

**Direct Known Subclasses:** AbstractAnnotationValueVisitor8

```java
@SupportedSourceVersion
(
RELEASE_7
)
public abstract class
AbstractAnnotationValueVisitor7<R,​P>

extends
AbstractAnnotationValueVisitor6
<R,​P>
```

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_7

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

**Since:** 1.7
**See Also:** AbstractAnnotationValueVisitor6

,

AbstractAnnotationValueVisitor8

,

AbstractAnnotationValueVisitor9

@SupportedSourceVersion

(

RELEASE_7

)
public abstract class

AbstractAnnotationValueVisitor7<R,​P>

extends

AbstractAnnotationValueVisitor6

<R,​P>

A skeletal visitor for annotation values with default behavior
appropriate for the

RELEASE_7

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

AbstractAnnotationValueVisitor7

()

Constructor for concrete subclasses to call.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.lang.model.util.

AbstractAnnotationValueVisitor6

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

AbstractAnnotationValueVisitor7

()

Constructor for concrete subclasses to call.

---

#### Constructor Summary

Constructor for concrete subclasses to call.

Method Summary

- Methods declared in class javax.lang.model.util.

AbstractAnnotationValueVisitor6

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

Methods declared in class javax.lang.model.util.

AbstractAnnotationValueVisitor6

visit

,

visit

,

visitUnknown

---

#### Methods declared in class javax.lang.model.util. AbstractAnnotationValueVisitor6

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

- AbstractAnnotationValueVisitor7

```java
protected AbstractAnnotationValueVisitor7()
```

Constructor for concrete subclasses to call.

Constructor Detail

- AbstractAnnotationValueVisitor7

```java
protected AbstractAnnotationValueVisitor7()
```

Constructor for concrete subclasses to call.

---

#### Constructor Detail

AbstractAnnotationValueVisitor7

```java
protected AbstractAnnotationValueVisitor7()
```

Constructor for concrete subclasses to call.

---

#### AbstractAnnotationValueVisitor7

protected AbstractAnnotationValueVisitor7()

Constructor for concrete subclasses to call.

---

