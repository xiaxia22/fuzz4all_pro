# Class SimpleAnnotationValueVisitor7<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleAnnotationValueVisitor7.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_7
)
public class
SimpleAnnotationValueVisitor7<R,​P>

extends
SimpleAnnotationValueVisitor6
<R,​P>
```

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_7

source version. Visit methods call

defaultAction

passing their arguments to

defaultAction

's
corresponding parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple annotation
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

#### protected SimpleAnnotationValueVisitor7()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected SimpleAnnotationValueVisitor7​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the value to assign to

SimpleAnnotationValueVisitor6.DEFAULT_VALUE

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SimpleAnnotationValueVisitor7<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>
- - javax.lang.model.util.SimpleAnnotationValueVisitor6

<R,​P>
- - javax.lang.model.util.SimpleAnnotationValueVisitor7<R,​P>

javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>

- javax.lang.model.util.SimpleAnnotationValueVisitor6

<R,​P>
- - javax.lang.model.util.SimpleAnnotationValueVisitor7<R,​P>

javax.lang.model.util.SimpleAnnotationValueVisitor6

<R,​P>

- javax.lang.model.util.SimpleAnnotationValueVisitor7<R,​P>

javax.lang.model.util.SimpleAnnotationValueVisitor7<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

**All Implemented Interfaces:** AnnotationValueVisitor

<R,​P>

**Direct Known Subclasses:** SimpleAnnotationValueVisitor8

```java
@SupportedSourceVersion
(
RELEASE_7
)
public class
SimpleAnnotationValueVisitor7<R,​P>

extends
SimpleAnnotationValueVisitor6
<R,​P>
```

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_7

source version. Visit methods call

defaultAction

passing their arguments to

defaultAction

's
corresponding parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

**Since:** 1.7
**See Also:** SimpleAnnotationValueVisitor6

,

SimpleAnnotationValueVisitor8

,

SimpleAnnotationValueVisitor9

@SupportedSourceVersion

(

RELEASE_7

)
public class

SimpleAnnotationValueVisitor7<R,​P>

extends

SimpleAnnotationValueVisitor6

<R,​P>

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_7

source version. Visit methods call

defaultAction

passing their arguments to

defaultAction

's
corresponding parameters.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

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

method. A new simple annotation
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

method. A new simple annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new simple annotation
value visitor class will also be introduced to correspond to the
new language level; this visitor will have different default
behavior for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.lang.model.util.

SimpleAnnotationValueVisitor6

DEFAULT_VALUE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleAnnotationValueVisitor7

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleAnnotationValueVisitor7

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.lang.model.util.

SimpleAnnotationValueVisitor6

defaultAction

,

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

Field Summary

- Fields declared in class javax.lang.model.util.

SimpleAnnotationValueVisitor6

DEFAULT_VALUE

---

#### Field Summary

Fields declared in class javax.lang.model.util.

SimpleAnnotationValueVisitor6

DEFAULT_VALUE

---

#### Fields declared in class javax.lang.model.util. SimpleAnnotationValueVisitor6

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleAnnotationValueVisitor7

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleAnnotationValueVisitor7

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

SimpleAnnotationValueVisitor6

defaultAction

,

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

---

#### Method Summary

Methods declared in class javax.lang.model.util.

SimpleAnnotationValueVisitor6

defaultAction

,

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

#### Methods declared in class javax.lang.model.util. SimpleAnnotationValueVisitor6

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleAnnotationValueVisitor6.DEFAULT_VALUE

Constructor Detail

- SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleAnnotationValueVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleAnnotationValueVisitor7

protected SimpleAnnotationValueVisitor7()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleAnnotationValueVisitor7

```java
protected SimpleAnnotationValueVisitor7​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleAnnotationValueVisitor6.DEFAULT_VALUE

---

#### SimpleAnnotationValueVisitor7

protected SimpleAnnotationValueVisitor7​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

---

