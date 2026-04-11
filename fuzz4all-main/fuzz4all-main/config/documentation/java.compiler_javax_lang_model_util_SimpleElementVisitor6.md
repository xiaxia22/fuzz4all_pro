# Class SimpleElementVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleElementVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleElementVisitor6<R,​P>

extends
AbstractElementVisitor6
<R,​P>
```

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

Visit methods corresponding to

RELEASE_6

language
constructs call

defaultAction

, passing their
arguments to

defaultAction

's corresponding parameters.

For constructs introduced in

RELEASE_7

and later,

visitUnknown

is called instead.

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

#### protected final
R
DEFAULT_VALUE

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

---

### Constructor Details

#### @Deprecated
(
since
="9")
protected SimpleElementVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### @Deprecated
(
since
="9")
protected SimpleElementVisitor6​(
R
defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

**Parameters:**
- defaultValue

- the value to assign to

DEFAULT_VALUE

---

### Method Details

#### protected
R
defaultAction​(
Element
e,

P
p)

The default action for visit methods.

**Parameters:**
- e

- the element to process
- p

- a visitor-specified parameter

**Returns:**
- DEFAULT_VALUE

unless overridden

**Implementation Requirements:**
- The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.

---

#### public
R
visitPackage​(
PackageElement
e,

P
p)

Visits a package element.

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
visitVariable​(
VariableElement
e,

P
p)

Visits a variable element.

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

, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.

---

#### public
R
visitExecutable​(
ExecutableElement
e,

P
p)

Visits an executable element.

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
visitTypeParameter​(
TypeParameterElement
e,

P
p)

Visits a type parameter element.

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

#### Class SimpleElementVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractElementVisitor6

<R,​P>
- - javax.lang.model.util.SimpleElementVisitor6<R,​P>

javax.lang.model.util.AbstractElementVisitor6

<R,​P>

- javax.lang.model.util.SimpleElementVisitor6<R,​P>

javax.lang.model.util.SimpleElementVisitor6<R,​P>

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

**Direct Known Subclasses:** ElementKindVisitor6

,

SimpleElementVisitor7

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleElementVisitor6<R,​P>

extends
AbstractElementVisitor6
<R,​P>
```

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

Visit methods corresponding to

RELEASE_6

language
constructs call

defaultAction

, passing their
arguments to

defaultAction

's corresponding parameters.

For constructs introduced in

RELEASE_7

and later,

visitUnknown

is called instead.

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

**Since:** 1.6
**See Also:** SimpleElementVisitor7

,

SimpleElementVisitor8

,

SimpleElementVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public class

SimpleElementVisitor6<R,​P>

extends

AbstractElementVisitor6

<R,​P>

A simple visitor of program elements with default behavior
appropriate for the

RELEASE_6

source version.

Visit methods corresponding to

RELEASE_6

language
constructs call

defaultAction

, passing their
arguments to

defaultAction

's corresponding parameters.

For constructs introduced in

RELEASE_7

and later,

visitUnknown

is called instead.

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

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleElementVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleElementVisitor6

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

protected

R

defaultAction

​(

Element

e,

P

p)

The default action for visit methods.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

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

Visits a variable element.

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

Fields

Modifier and Type

Field

Description

protected

R

DEFAULT_VALUE

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

---

#### Field Summary

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SimpleElementVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleElementVisitor6

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

protected

R

defaultAction

​(

Element

e,

P

p)

The default action for visit methods.

R

visitExecutable

​(

ExecutableElement

e,

P

p)

Visits an executable element.

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

Visits a variable element.

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

The default action for visit methods.

Visits an executable element.

Visits a package element.

Visits a type element.

Visits a type parameter element.

Visits a variable element.

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

============ FIELD DETAIL ===========

- Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6​(
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

DEFAULT_VALUE

============ METHOD DETAIL ==========

- Method Detail

- defaultAction

```java
protected
R
defaultAction​(
Element
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the element to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

Field Detail

- DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

---

#### Field Detail

DEFAULT_VALUE

```java
protected final
R
DEFAULT_VALUE
```

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

---

#### DEFAULT_VALUE

protected final

R

DEFAULT_VALUE

Default value to be returned;

defaultAction

returns this value unless the method is
overridden.

Constructor Detail

- SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6​(
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

DEFAULT_VALUE

---

#### Constructor Detail

SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleElementVisitor6

@Deprecated

(

since

="9")
protected SimpleElementVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleElementVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleElementVisitor6​(
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

DEFAULT_VALUE

---

#### SimpleElementVisitor6

@Deprecated

(

since

="9")
protected SimpleElementVisitor6​(

R

defaultValue)

Constructor for concrete subclasses; uses the argument for the
default value.

Method Detail

- defaultAction

```java
protected
R
defaultAction​(
Element
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the element to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

defaultAction

```java
protected
R
defaultAction​(
Element
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the element to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

---

#### defaultAction

protected

R

defaultAction​(

Element

e,

P

p)

The default action for visit methods.

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

**Implementation Requirements:** This implementation calls

defaultAction

, unless the
element is a

RESOURCE_VARIABLE

in which case

visitUnknown

is called.
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** e

- the element to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

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

---

