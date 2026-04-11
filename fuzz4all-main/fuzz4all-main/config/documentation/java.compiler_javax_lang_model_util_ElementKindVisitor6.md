# Class ElementKindVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\ElementKindVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
ElementKindVisitor6<R,​P>

extends
SimpleElementVisitor6
<R,​P>
```

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_6

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

#### @Deprecated
(
since
="9")
protected ElementKindVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### @Deprecated
(
since
="9")
protected ElementKindVisitor6​(
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

#### public
R
visitPackage​(
PackageElement
e,

P
p)

Visits a package element.

The element argument has kind

PACKAGE

.

**Specified by:**
- visitPackage

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitPackage

in class

SimpleElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
visitType​(
TypeElement
e,

P
p)

Visits a type element.

**Specified by:**
- visitType

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitType

in class

SimpleElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of the kind-specific visit method

**Implementation Requirements:**
- This implementation dispatches to the visit method for the
specific

kind

of type,

ANNOTATION_TYPE

,

CLASS

,

ENUM

, or

INTERFACE

.

---

#### public
R
visitTypeAsAnnotationType​(
TypeElement
e,

P
p)

Visits an

ANNOTATION_TYPE

type element.

**Parameters:**
- e

- the element to visit
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
visitTypeAsClass​(
TypeElement
e,

P
p)

Visits a

CLASS

type element.

**Parameters:**
- e

- the element to visit
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
visitTypeAsEnum​(
TypeElement
e,

P
p)

Visits an

ENUM

type element.

**Parameters:**
- e

- the element to visit
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
visitTypeAsInterface​(
TypeElement
e,

P
p)

Visits an

INTERFACE

type element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.
.

---

#### public
R
visitVariable​(
VariableElement
e,

P
p)

Visits a variable element

**Specified by:**
- visitVariable

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitVariable

in class

SimpleElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of the kind-specific visit method

**Implementation Requirements:**
- This implementation dispatches to the visit method for
the specific

kind

of variable,

ENUM_CONSTANT

,

EXCEPTION_PARAMETER

,

FIELD

,

LOCAL_VARIABLE

,

PARAMETER

, or

RESOURCE_VARIABLE

.

---

#### public
R
visitVariableAsEnumConstant​(
VariableElement
e,

P
p)

Visits an

ENUM_CONSTANT

variable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.
.

---

#### public
R
visitVariableAsExceptionParameter​(
VariableElement
e,

P
p)

Visits an

EXCEPTION_PARAMETER

variable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.
.

---

#### public
R
visitVariableAsField​(
VariableElement
e,

P
p)

Visits a

FIELD

variable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.
.

---

#### public
R
visitVariableAsLocalVariable​(
VariableElement
e,

P
p)

Visits a

LOCAL_VARIABLE

variable element.

**Parameters:**
- e

- the element to visit
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
visitVariableAsParameter​(
VariableElement
e,

P
p)

Visits a

PARAMETER

variable element.

**Parameters:**
- e

- the element to visit
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
visitVariableAsResourceVariable​(
VariableElement
e,

P
p)

Visits a

RESOURCE_VARIABLE

variable element.

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of

visitUnknown

**Since:**
- 1.7

**Implementation Requirements:**
- This implementation calls

visitUnknown

.

---

#### public
R
visitExecutable​(
ExecutableElement
e,

P
p)

Visits an executable element.

**Specified by:**
- visitExecutable

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitExecutable

in class

SimpleElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- the result of the kind-specific visit method

**Implementation Requirements:**
- This implementation dispatches to the visit method
for the specific

kind

of executable,

CONSTRUCTOR

,

INSTANCE_INIT

,

METHOD

, or

STATIC_INIT

.

---

#### public
R
visitExecutableAsConstructor​(
ExecutableElement
e,

P
p)

Visits a

CONSTRUCTOR

executable element.

**Parameters:**
- e

- the element to visit
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
visitExecutableAsInstanceInit​(
ExecutableElement
e,

P
p)

Visits an

INSTANCE_INIT

executable element.

**Parameters:**
- e

- the element to visit
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
visitExecutableAsMethod​(
ExecutableElement
e,

P
p)

Visits a

METHOD

executable element.

**Parameters:**
- e

- the element to visit
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
visitExecutableAsStaticInit​(
ExecutableElement
e,

P
p)

Visits a

STATIC_INIT

executable element.

**Parameters:**
- e

- the element to visit
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
visitTypeParameter​(
TypeParameterElement
e,

P
p)

Visits a type parameter element.

The element argument has kind

TYPE_PARAMETER

.

**Specified by:**
- visitTypeParameter

in interface

ElementVisitor

<

R

,​

P

>

**Overrides:**
- visitTypeParameter

in class

SimpleElementVisitor6

<

R

,​

P

>

**Parameters:**
- e

- the element to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

### Additional Sections

#### Class ElementKindVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor6<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.ElementKindVisitor6<R,​P>

javax.lang.model.util.SimpleElementVisitor6

<R,​P>

- javax.lang.model.util.ElementKindVisitor6<R,​P>

javax.lang.model.util.ElementKindVisitor6<R,​P>

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

**Direct Known Subclasses:** ElementKindVisitor7

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
ElementKindVisitor6<R,​P>

extends
SimpleElementVisitor6
<R,​P>
```

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_6

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

**Since:** 1.6
**See Also:** ElementKindVisitor7

,

ElementKindVisitor8

,

ElementKindVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public class

ElementKindVisitor6<R,​P>

extends

SimpleElementVisitor6

<R,​P>

A visitor of program elements based on their

kind

with default behavior appropriate for the

RELEASE_6

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

ElementKindVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

ElementKindVisitor6

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

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

R

visitExecutableAsConstructor

​(

ExecutableElement

e,

P

p)

Visits a

CONSTRUCTOR

executable element.

R

visitExecutableAsInstanceInit

​(

ExecutableElement

e,

P

p)

Visits an

INSTANCE_INIT

executable element.

R

visitExecutableAsMethod

​(

ExecutableElement

e,

P

p)

Visits a

METHOD

executable element.

R

visitExecutableAsStaticInit

​(

ExecutableElement

e,

P

p)

Visits a

STATIC_INIT

executable element.

R

visitPackage

​(

PackageElement

e,

P

p)

Visits a package element.

R

visitType

​(

TypeElement

e,

P

p)

Visits a type element.

R

visitTypeAsAnnotationType

​(

TypeElement

e,

P

p)

Visits an

ANNOTATION_TYPE

type element.

R

visitTypeAsClass

​(

TypeElement

e,

P

p)

Visits a

CLASS

type element.

R

visitTypeAsEnum

​(

TypeElement

e,

P

p)

Visits an

ENUM

type element.

R

visitTypeAsInterface

​(

TypeElement

e,

P

p)

Visits an

INTERFACE

type element.

R

visitTypeParameter

​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

R

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element

R

visitVariableAsEnumConstant

​(

VariableElement

e,

P

p)

Visits an

ENUM_CONSTANT

variable element.

R

visitVariableAsExceptionParameter

​(

VariableElement

e,

P

p)

Visits an

EXCEPTION_PARAMETER

variable element.

R

visitVariableAsField

​(

VariableElement

e,

P

p)

Visits a

FIELD

variable element.

R

visitVariableAsLocalVariable

​(

VariableElement

e,

P

p)

Visits a

LOCAL_VARIABLE

variable element.

R

visitVariableAsParameter

​(

VariableElement

e,

P

p)

Visits a

PARAMETER

variable element.

R

visitVariableAsResourceVariable

​(

VariableElement

e,

P

p)

Visits a

RESOURCE_VARIABLE

variable element.

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

ElementKindVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

ElementKindVisitor6

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

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

R

visitExecutableAsConstructor

​(

ExecutableElement

e,

P

p)

Visits a

CONSTRUCTOR

executable element.

R

visitExecutableAsInstanceInit

​(

ExecutableElement

e,

P

p)

Visits an

INSTANCE_INIT

executable element.

R

visitExecutableAsMethod

​(

ExecutableElement

e,

P

p)

Visits a

METHOD

executable element.

R

visitExecutableAsStaticInit

​(

ExecutableElement

e,

P

p)

Visits a

STATIC_INIT

executable element.

R

visitPackage

​(

PackageElement

e,

P

p)

Visits a package element.

R

visitType

​(

TypeElement

e,

P

p)

Visits a type element.

R

visitTypeAsAnnotationType

​(

TypeElement

e,

P

p)

Visits an

ANNOTATION_TYPE

type element.

R

visitTypeAsClass

​(

TypeElement

e,

P

p)

Visits a

CLASS

type element.

R

visitTypeAsEnum

​(

TypeElement

e,

P

p)

Visits an

ENUM

type element.

R

visitTypeAsInterface

​(

TypeElement

e,

P

p)

Visits an

INTERFACE

type element.

R

visitTypeParameter

​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

R

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element

R

visitVariableAsEnumConstant

​(

VariableElement

e,

P

p)

Visits an

ENUM_CONSTANT

variable element.

R

visitVariableAsExceptionParameter

​(

VariableElement

e,

P

p)

Visits an

EXCEPTION_PARAMETER

variable element.

R

visitVariableAsField

​(

VariableElement

e,

P

p)

Visits a

FIELD

variable element.

R

visitVariableAsLocalVariable

​(

VariableElement

e,

P

p)

Visits a

LOCAL_VARIABLE

variable element.

R

visitVariableAsParameter

​(

VariableElement

e,

P

p)

Visits a

PARAMETER

variable element.

R

visitVariableAsResourceVariable

​(

VariableElement

e,

P

p)

Visits a

RESOURCE_VARIABLE

variable element.

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

Visits an executable element.

Visits a

CONSTRUCTOR

executable element.

Visits an

INSTANCE_INIT

executable element.

Visits a

METHOD

executable element.

Visits a

STATIC_INIT

executable element.

Visits a package element.

Visits a type element.

Visits an

ANNOTATION_TYPE

type element.

Visits a

CLASS

type element.

Visits an

ENUM

type element.

Visits an

INTERFACE

type element.

Visits a type parameter element.

Visits a variable element

Visits an

ENUM_CONSTANT

variable element.

Visits an

EXCEPTION_PARAMETER

variable element.

Visits a

FIELD

variable element.

Visits a

LOCAL_VARIABLE

variable element.

Visits a

PARAMETER

variable element.

Visits a

RESOURCE_VARIABLE

variable element.

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

- ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

- visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

The element argument has kind

PACKAGE

.

**Specified by:** visitPackage

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitPackage

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Specified by:** visitType

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitType

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for the
specific

kind

of type,

ANNOTATION_TYPE

,

CLASS

,

ENUM

, or

INTERFACE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitTypeAsAnnotationType

```java
public
R
visitTypeAsAnnotationType​(
TypeElement
e,

P
p)
```

Visits an

ANNOTATION_TYPE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsClass

```java
public
R
visitTypeAsClass​(
TypeElement
e,

P
p)
```

Visits a

CLASS

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsEnum

```java
public
R
visitTypeAsEnum​(
TypeElement
e,

P
p)
```

Visits an

ENUM

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsInterface

```java
public
R
visitTypeAsInterface​(
TypeElement
e,

P
p)
```

Visits an

INTERFACE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element

**Specified by:** visitVariable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitVariable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of variable,

ENUM_CONSTANT

,

EXCEPTION_PARAMETER

,

FIELD

,

LOCAL_VARIABLE

,

PARAMETER

, or

RESOURCE_VARIABLE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitVariableAsEnumConstant

```java
public
R
visitVariableAsEnumConstant​(
VariableElement
e,

P
p)
```

Visits an

ENUM_CONSTANT

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsExceptionParameter

```java
public
R
visitVariableAsExceptionParameter​(
VariableElement
e,

P
p)
```

Visits an

EXCEPTION_PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsField

```java
public
R
visitVariableAsField​(
VariableElement
e,

P
p)
```

Visits a

FIELD

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsLocalVariable

```java
public
R
visitVariableAsLocalVariable​(
VariableElement
e,

P
p)
```

Visits a

LOCAL_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsParameter

```java
public
R
visitVariableAsParameter​(
VariableElement
e,

P
p)
```

Visits a

PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsResourceVariable

```java
public
R
visitVariableAsResourceVariable​(
VariableElement
e,

P
p)
```

Visits a

RESOURCE_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Specified by:** visitExecutable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitExecutable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method
for the specific

kind

of executable,

CONSTRUCTOR

,

INSTANCE_INIT

,

METHOD

, or

STATIC_INIT

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitExecutableAsConstructor

```java
public
R
visitExecutableAsConstructor​(
ExecutableElement
e,

P
p)
```

Visits a

CONSTRUCTOR

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsInstanceInit

```java
public
R
visitExecutableAsInstanceInit​(
ExecutableElement
e,

P
p)
```

Visits an

INSTANCE_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsMethod

```java
public
R
visitExecutableAsMethod​(
ExecutableElement
e,

P
p)
```

Visits a

METHOD

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsStaticInit

```java
public
R
visitExecutableAsStaticInit​(
ExecutableElement
e,

P
p)
```

Visits a

STATIC_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

The element argument has kind

TYPE_PARAMETER

.

**Specified by:** visitTypeParameter

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitTypeParameter

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

Constructor Detail

- ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

#### Constructor Detail

ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### ElementKindVisitor6

@Deprecated

(

since

="9")
protected ElementKindVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

ElementKindVisitor6

```java
@Deprecated
(
since
="9")
protected ElementKindVisitor6​(
R
defaultValue)
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

#### ElementKindVisitor6

@Deprecated

(

since

="9")
protected ElementKindVisitor6​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

- visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

The element argument has kind

PACKAGE

.

**Specified by:** visitPackage

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitPackage

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Specified by:** visitType

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitType

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for the
specific

kind

of type,

ANNOTATION_TYPE

,

CLASS

,

ENUM

, or

INTERFACE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitTypeAsAnnotationType

```java
public
R
visitTypeAsAnnotationType​(
TypeElement
e,

P
p)
```

Visits an

ANNOTATION_TYPE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsClass

```java
public
R
visitTypeAsClass​(
TypeElement
e,

P
p)
```

Visits a

CLASS

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsEnum

```java
public
R
visitTypeAsEnum​(
TypeElement
e,

P
p)
```

Visits an

ENUM

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeAsInterface

```java
public
R
visitTypeAsInterface​(
TypeElement
e,

P
p)
```

Visits an

INTERFACE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element

**Specified by:** visitVariable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitVariable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of variable,

ENUM_CONSTANT

,

EXCEPTION_PARAMETER

,

FIELD

,

LOCAL_VARIABLE

,

PARAMETER

, or

RESOURCE_VARIABLE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitVariableAsEnumConstant

```java
public
R
visitVariableAsEnumConstant​(
VariableElement
e,

P
p)
```

Visits an

ENUM_CONSTANT

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsExceptionParameter

```java
public
R
visitVariableAsExceptionParameter​(
VariableElement
e,

P
p)
```

Visits an

EXCEPTION_PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsField

```java
public
R
visitVariableAsField​(
VariableElement
e,

P
p)
```

Visits a

FIELD

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsLocalVariable

```java
public
R
visitVariableAsLocalVariable​(
VariableElement
e,

P
p)
```

Visits a

LOCAL_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsParameter

```java
public
R
visitVariableAsParameter​(
VariableElement
e,

P
p)
```

Visits a

PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitVariableAsResourceVariable

```java
public
R
visitVariableAsResourceVariable​(
VariableElement
e,

P
p)
```

Visits a

RESOURCE_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Specified by:** visitExecutable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitExecutable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method
for the specific

kind

of executable,

CONSTRUCTOR

,

INSTANCE_INIT

,

METHOD

, or

STATIC_INIT

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

- visitExecutableAsConstructor

```java
public
R
visitExecutableAsConstructor​(
ExecutableElement
e,

P
p)
```

Visits a

CONSTRUCTOR

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsInstanceInit

```java
public
R
visitExecutableAsInstanceInit​(
ExecutableElement
e,

P
p)
```

Visits an

INSTANCE_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsMethod

```java
public
R
visitExecutableAsMethod​(
ExecutableElement
e,

P
p)
```

Visits a

METHOD

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutableAsStaticInit

```java
public
R
visitExecutableAsStaticInit​(
ExecutableElement
e,

P
p)
```

Visits a

STATIC_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

The element argument has kind

TYPE_PARAMETER

.

**Specified by:** visitTypeParameter

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitTypeParameter

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### Method Detail

visitPackage

```java
public
R
visitPackage​(
PackageElement
e,

P
p)
```

Visits a package element.

The element argument has kind

PACKAGE

.

**Specified by:** visitPackage

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitPackage

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitPackage

public

R

visitPackage​(

PackageElement

e,

P

p)

Visits a package element.

The element argument has kind

PACKAGE

.

visitType

```java
public
R
visitType​(
TypeElement
e,

P
p)
```

Visits a type element.

**Specified by:** visitType

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitType

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for the
specific

kind

of type,

ANNOTATION_TYPE

,

CLASS

,

ENUM

, or

INTERFACE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

---

#### visitType

public

R

visitType​(

TypeElement

e,

P

p)

Visits a type element.

visitTypeAsAnnotationType

```java
public
R
visitTypeAsAnnotationType​(
TypeElement
e,

P
p)
```

Visits an

ANNOTATION_TYPE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitTypeAsAnnotationType

public

R

visitTypeAsAnnotationType​(

TypeElement

e,

P

p)

Visits an

ANNOTATION_TYPE

type element.

visitTypeAsClass

```java
public
R
visitTypeAsClass​(
TypeElement
e,

P
p)
```

Visits a

CLASS

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitTypeAsClass

public

R

visitTypeAsClass​(

TypeElement

e,

P

p)

Visits a

CLASS

type element.

visitTypeAsEnum

```java
public
R
visitTypeAsEnum​(
TypeElement
e,

P
p)
```

Visits an

ENUM

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitTypeAsEnum

public

R

visitTypeAsEnum​(

TypeElement

e,

P

p)

Visits an

ENUM

type element.

visitTypeAsInterface

```java
public
R
visitTypeAsInterface​(
TypeElement
e,

P
p)
```

Visits an

INTERFACE

type element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitTypeAsInterface

public

R

visitTypeAsInterface​(

TypeElement

e,

P

p)

Visits an

INTERFACE

type element.

visitVariable

```java
public
R
visitVariable​(
VariableElement
e,

P
p)
```

Visits a variable element

**Specified by:** visitVariable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitVariable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method for
the specific

kind

of variable,

ENUM_CONSTANT

,

EXCEPTION_PARAMETER

,

FIELD

,

LOCAL_VARIABLE

,

PARAMETER

, or

RESOURCE_VARIABLE

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

---

#### visitVariable

public

R

visitVariable​(

VariableElement

e,

P

p)

Visits a variable element

visitVariableAsEnumConstant

```java
public
R
visitVariableAsEnumConstant​(
VariableElement
e,

P
p)
```

Visits an

ENUM_CONSTANT

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitVariableAsEnumConstant

public

R

visitVariableAsEnumConstant​(

VariableElement

e,

P

p)

Visits an

ENUM_CONSTANT

variable element.

visitVariableAsExceptionParameter

```java
public
R
visitVariableAsExceptionParameter​(
VariableElement
e,

P
p)
```

Visits an

EXCEPTION_PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitVariableAsExceptionParameter

public

R

visitVariableAsExceptionParameter​(

VariableElement

e,

P

p)

Visits an

EXCEPTION_PARAMETER

variable element.

visitVariableAsField

```java
public
R
visitVariableAsField​(
VariableElement
e,

P
p)
```

Visits a

FIELD

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitVariableAsField

public

R

visitVariableAsField​(

VariableElement

e,

P

p)

Visits a

FIELD

variable element.

visitVariableAsLocalVariable

```java
public
R
visitVariableAsLocalVariable​(
VariableElement
e,

P
p)
```

Visits a

LOCAL_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitVariableAsLocalVariable

public

R

visitVariableAsLocalVariable​(

VariableElement

e,

P

p)

Visits a

LOCAL_VARIABLE

variable element.

visitVariableAsParameter

```java
public
R
visitVariableAsParameter​(
VariableElement
e,

P
p)
```

Visits a

PARAMETER

variable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitVariableAsParameter

public

R

visitVariableAsParameter​(

VariableElement

e,

P

p)

Visits a

PARAMETER

variable element.

visitVariableAsResourceVariable

```java
public
R
visitVariableAsResourceVariable​(
VariableElement
e,

P
p)
```

Visits a

RESOURCE_VARIABLE

variable element.

**Implementation Requirements:** This implementation calls

visitUnknown

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

visitUnknown
**Since:** 1.7

---

#### visitVariableAsResourceVariable

public

R

visitVariableAsResourceVariable​(

VariableElement

e,

P

p)

Visits a

RESOURCE_VARIABLE

variable element.

visitExecutable

```java
public
R
visitExecutable​(
ExecutableElement
e,

P
p)
```

Visits an executable element.

**Specified by:** visitExecutable

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitExecutable

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation dispatches to the visit method
for the specific

kind

of executable,

CONSTRUCTOR

,

INSTANCE_INIT

,

METHOD

, or

STATIC_INIT

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the kind-specific visit method

---

#### visitExecutable

public

R

visitExecutable​(

ExecutableElement

e,

P

p)

Visits an executable element.

visitExecutableAsConstructor

```java
public
R
visitExecutableAsConstructor​(
ExecutableElement
e,

P
p)
```

Visits a

CONSTRUCTOR

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitExecutableAsConstructor

public

R

visitExecutableAsConstructor​(

ExecutableElement

e,

P

p)

Visits a

CONSTRUCTOR

executable element.

visitExecutableAsInstanceInit

```java
public
R
visitExecutableAsInstanceInit​(
ExecutableElement
e,

P
p)
```

Visits an

INSTANCE_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitExecutableAsInstanceInit

public

R

visitExecutableAsInstanceInit​(

ExecutableElement

e,

P

p)

Visits an

INSTANCE_INIT

executable element.

visitExecutableAsMethod

```java
public
R
visitExecutableAsMethod​(
ExecutableElement
e,

P
p)
```

Visits a

METHOD

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitExecutableAsMethod

public

R

visitExecutableAsMethod​(

ExecutableElement

e,

P

p)

Visits a

METHOD

executable element.

visitExecutableAsStaticInit

```java
public
R
visitExecutableAsStaticInit​(
ExecutableElement
e,

P
p)
```

Visits a

STATIC_INIT

executable element.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitExecutableAsStaticInit

public

R

visitExecutableAsStaticInit​(

ExecutableElement

e,

P

p)

Visits a

STATIC_INIT

executable element.

visitTypeParameter

```java
public
R
visitTypeParameter​(
TypeParameterElement
e,

P
p)
```

Visits a type parameter element.

The element argument has kind

TYPE_PARAMETER

.

**Specified by:** visitTypeParameter

in interface

ElementVisitor

<

R

,​

P

>
**Overrides:** visitTypeParameter

in class

SimpleElementVisitor6

<

R

,​

P

>
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitTypeParameter

public

R

visitTypeParameter​(

TypeParameterElement

e,

P

p)

Visits a type parameter element.

The element argument has kind

TYPE_PARAMETER

.

---

