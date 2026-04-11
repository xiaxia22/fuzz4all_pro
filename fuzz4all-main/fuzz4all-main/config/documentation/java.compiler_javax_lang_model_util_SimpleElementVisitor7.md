# Class SimpleElementVisitor7<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleElementVisitor7.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_7
)
public class
SimpleElementVisitor7<R,​P>

extends
SimpleElementVisitor6
<R,​P>
```

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_7

source version.

Visit methods corresponding to

RELEASE_7

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

ElementVisitor

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

method. A new simple element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods. Use

Void

for visitors that do not need an additional parameter.

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SimpleElementVisitor7()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### protected SimpleElementVisitor7​(
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
visitVariable​(
VariableElement
e,

P
p)

Visits a variable element.

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
- a visitor-specified result

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

### Additional Sections

#### Class SimpleElementVisitor7<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor7<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.SimpleElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor7<R,​P>

javax.lang.model.util.SimpleElementVisitor6

<R,​P>

- javax.lang.model.util.SimpleElementVisitor7<R,​P>

javax.lang.model.util.SimpleElementVisitor7<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods. Use

Void

for visitors that do not need to return results.
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods. Use

Void

for visitors that do not need an additional parameter.

**All Implemented Interfaces:** ElementVisitor

<R,​P>

**Direct Known Subclasses:** SimpleElementVisitor8

```java
@SupportedSourceVersion
(
RELEASE_7
)
public class
SimpleElementVisitor7<R,​P>

extends
SimpleElementVisitor6
<R,​P>
```

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_7

source version.

Visit methods corresponding to

RELEASE_7

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

ElementVisitor

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

method. A new simple element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.7
**See Also:** SimpleElementVisitor6

,

SimpleElementVisitor8

,

SimpleElementVisitor9

@SupportedSourceVersion

(

RELEASE_7

)
public class

SimpleElementVisitor7<R,​P>

extends

SimpleElementVisitor6

<R,​P>

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_7

source version.

Visit methods corresponding to

RELEASE_7

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

ElementVisitor

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

method. A new simple element visitor
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

ElementVisitor

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

method. A new simple element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

WARNING:

The

ElementVisitor

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

method. A new simple element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new simple element visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

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

SimpleElementVisitor7

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleElementVisitor7

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

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

- Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

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

SimpleElementVisitor7

()

Constructor for concrete subclasses; uses

null

for the
default value.

protected

SimpleElementVisitor7

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

visitVariable

​(

VariableElement

e,

P

p)

Visits a variable element.

- Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

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

Visits a variable element.

Methods declared in class javax.lang.model.util.

SimpleElementVisitor6

defaultAction

,

visitExecutable

,

visitPackage

,

visitType

,

visitTypeParameter

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

- SimpleElementVisitor7

```java
protected SimpleElementVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleElementVisitor7

```java
protected SimpleElementVisitor7​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

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

Visits a variable element.

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
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

Constructor Detail

- SimpleElementVisitor7

```java
protected SimpleElementVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleElementVisitor7

```java
protected SimpleElementVisitor7​(
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

SimpleElementVisitor7

```java
protected SimpleElementVisitor7()
```

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleElementVisitor7

protected SimpleElementVisitor7()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleElementVisitor7

```java
protected SimpleElementVisitor7​(
R
defaultValue)
```

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:** defaultValue

- the value to assign to

SimpleElementVisitor6.DEFAULT_VALUE

---

#### SimpleElementVisitor7

protected SimpleElementVisitor7​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

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

Visits a variable element.

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

Visits a variable element.

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
**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitVariable

public

R

visitVariable​(

VariableElement

e,

P

p)

Visits a variable element.

---

