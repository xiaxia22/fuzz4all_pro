# Class ElementKindVisitor8<R,​P>

**Source:** `java.compiler\javax\lang\model\util\ElementKindVisitor8.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
ElementKindVisitor8<R,​P>

extends
ElementKindVisitor7
<R,​P>
```

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_8

source version. For

elements

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

ElementVisitor

interface
implemented by this class may have methods added to it or the

ElementKind

enum

used in this case may have
constants added to it in the future to accommodate new, currently
unknown, language structures added to future versions of the
Java™ programming language. Therefore, methods whose names
begin with

"visit"

may be added to this class in the
future; to avoid incompatibilities, classes which extend this class
should not declare any instance methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

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

#### protected ElementKindVisitor8()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected ElementKindVisitor8​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ElementKindVisitor8<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor7

<R,​P>
- - javax.lang.model.util.ElementKindVisitor8<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor7

<R,​P>
- - javax.lang.model.util.ElementKindVisitor8<R,​P>

javax.lang.model.util.SimpleElementVisitor6

<R,​P>

- javax.lang.model.util.ElementKindVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor7

<R,​P>
- - javax.lang.model.util.ElementKindVisitor8<R,​P>

javax.lang.model.util.ElementKindVisitor6

<R,​P>

- javax.lang.model.util.ElementKindVisitor7

<R,​P>
- - javax.lang.model.util.ElementKindVisitor8<R,​P>

javax.lang.model.util.ElementKindVisitor7

<R,​P>

- javax.lang.model.util.ElementKindVisitor8<R,​P>

javax.lang.model.util.ElementKindVisitor8<R,​P>

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

**All Implemented Interfaces:** ElementVisitor

<R,​P>

**Direct Known Subclasses:** ElementKindVisitor9

```java
@SupportedSourceVersion
(
RELEASE_8
)
public class
ElementKindVisitor8<R,​P>

extends
ElementKindVisitor7
<R,​P>
```

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_8

source version. For

elements

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

ElementVisitor

interface
implemented by this class may have methods added to it or the

ElementKind

enum

used in this case may have
constants added to it in the future to accommodate new, currently
unknown, language structures added to future versions of the
Java™ programming language. Therefore, methods whose names
begin with

"visit"

may be added to this class in the
future; to avoid incompatibilities, classes which extend this class
should not declare any instance methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

**Since:** 1.8
**See Also:** ElementKindVisitor6

,

ElementKindVisitor7

,

ElementKindVisitor9

@SupportedSourceVersion

(

RELEASE_8

)
public class

ElementKindVisitor8<R,​P>

extends

ElementKindVisitor7

<R,​P>

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_8

source version. For

elements

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

ElementVisitor

interface
implemented by this class may have methods added to it or the

ElementKind

enum

used in this case may have
constants added to it in the future to accommodate new, currently
unknown, language structures added to future versions of the
Java™ programming language. Therefore, methods whose names
begin with

"visit"

may be added to this class in the
future; to avoid incompatibilities, classes which extend this class
should not declare any instance methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

Methods in this class may be overridden subject to their
general contract. Note that annotating methods in concrete
subclasses with

@Override

will help
ensure that methods are overridden as intended.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it or the

ElementKind

enum

used in this case may have
constants added to it in the future to accommodate new, currently
unknown, language structures added to future versions of the
Java™ programming language. Therefore, methods whose names
begin with

"visit"

may be added to this class in the
future; to avoid incompatibilities, classes which extend this class
should not declare any instance methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

WARNING:

The

ElementVisitor

interface
implemented by this class may have methods added to it or the

ElementKind

enum

used in this case may have
constants added to it in the future to accommodate new, currently
unknown, language structures added to future versions of the
Java™ programming language. Therefore, methods whose names
begin with

"visit"

may be added to this class in the
future; to avoid incompatibilities, classes which extend this class
should not declare any instance methods with names beginning with

"visit"

.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new abstract element kind
visitor class will also be introduced to correspond to the new
language level; this visitor will have different default behavior
for the visit method in question. When the new visitor is
introduced, all or portions of this visitor may be deprecated.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.lang.model.util.

SimpleElementVisitor6

DEFAULT_VALUE

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementKindVisitor8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementKindVisitor8

​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.lang.model.util.

ElementKindVisitor7

visitVariableAsResourceVariable

- Methods declared in class javax.lang.model.util.

ElementKindVisitor6

visitExecutable

,

visitExecutableAsConstructor

,

visitExecutableAsInstanceInit

,

visitExecutableAsMethod

,

visitExecutableAsStaticInit

,

visitPackage

,

visitType

,

visitTypeAsAnnotationType

,

visitTypeAsClass

,

visitTypeAsEnum

,

visitTypeAsInterface

,

visitTypeParameter

,

visitVariable

,

visitVariableAsEnumConstant

,

visitVariableAsExceptionParameter

,

visitVariableAsField

,

visitVariableAsLocalVariable

,

visitVariableAsParameter

- Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

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

SimpleElementVisitor6

DEFAULT_VALUE

---

#### Field Summary

Fields declared in class javax.lang.model.util.

SimpleElementVisitor6

DEFAULT_VALUE

---

#### Fields declared in class javax.lang.model.util. SimpleElementVisitor6

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ElementKindVisitor8

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

ElementKindVisitor8

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

ElementKindVisitor7

visitVariableAsResourceVariable

- Methods declared in class javax.lang.model.util.

ElementKindVisitor6

visitExecutable

,

visitExecutableAsConstructor

,

visitExecutableAsInstanceInit

,

visitExecutableAsMethod

,

visitExecutableAsStaticInit

,

visitPackage

,

visitType

,

visitTypeAsAnnotationType

,

visitTypeAsClass

,

visitTypeAsEnum

,

visitTypeAsInterface

,

visitTypeParameter

,

visitVariable

,

visitVariableAsEnumConstant

,

visitVariableAsExceptionParameter

,

visitVariableAsField

,

visitVariableAsLocalVariable

,

visitVariableAsParameter

- Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

- Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

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

ElementKindVisitor7

visitVariableAsResourceVariable

---

#### Methods declared in class javax.lang.model.util. ElementKindVisitor7

Methods declared in class javax.lang.model.util.

ElementKindVisitor6

visitExecutable

,

visitExecutableAsConstructor

,

visitExecutableAsInstanceInit

,

visitExecutableAsMethod

,

visitExecutableAsStaticInit

,

visitPackage

,

visitType

,

visitTypeAsAnnotationType

,

visitTypeAsClass

,

visitTypeAsEnum

,

visitTypeAsInterface

,

visitTypeParameter

,

visitVariable

,

visitVariableAsEnumConstant

,

visitVariableAsExceptionParameter

,

visitVariableAsField

,

visitVariableAsLocalVariable

,

visitVariableAsParameter

---

#### Methods declared in class javax.lang.model.util. ElementKindVisitor6

Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

---

#### Methods declared in class javax.lang.model.util. SimpleElementVisitor6

Methods declared in class javax.lang.model.util.

AbstractElementVisitor6

visit

,

visit

,

visitModule

,

visitUnknown

---

#### Methods declared in class javax.lang.model.util. AbstractElementVisitor6

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

- ElementKindVisitor8

```java
protected ElementKindVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementKindVisitor8

```java
protected ElementKindVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

Constructor Detail

- ElementKindVisitor8

```java
protected ElementKindVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementKindVisitor8

```java
protected ElementKindVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

ElementKindVisitor8

```java
protected ElementKindVisitor8()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### ElementKindVisitor8

protected ElementKindVisitor8()

Constructor for concrete subclasses; uses

null

for the
default value.

ElementKindVisitor8

```java
protected ElementKindVisitor8​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

#### ElementKindVisitor8

protected ElementKindVisitor8​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

---

