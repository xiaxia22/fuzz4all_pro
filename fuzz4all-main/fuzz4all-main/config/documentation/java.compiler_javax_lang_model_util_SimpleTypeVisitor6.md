# Class SimpleTypeVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleTypeVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleTypeVisitor6<R,​P>

extends
AbstractTypeVisitor6
<R,​P>
```

A simple visitor of types with default behavior appropriate for the

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

method. A new simple type visitor
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
protected SimpleTypeVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### @Deprecated
(
since
="9")
protected SimpleTypeVisitor6​(
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
TypeMirror
e,

P
p)

The default action for visit methods.

**Parameters:**
- e

- the type to process
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
visitPrimitive​(
PrimitiveType
t,

P
p)

Visits a primitive type.

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
visitNull​(
NullType
t,

P
p)

Visits the null type. This implementation calls

defaultAction

.

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
visitArray​(
ArrayType
t,

P
p)

Visits an array type.

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
visitDeclared​(
DeclaredType
t,

P
p)

Visits a declared type.

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
visitError​(
ErrorType
t,

P
p)

Visits an error type.

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
visitTypeVariable​(
TypeVariable
t,

P
p)

Visits a type variable.

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
visitWildcard​(
WildcardType
t,

P
p)

Visits a wildcard type.

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
visitExecutable​(
ExecutableType
t,

P
p)

Visits an executable type.

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

#### Class SimpleTypeVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractTypeVisitor6

<R,​P>
- - javax.lang.model.util.SimpleTypeVisitor6<R,​P>

javax.lang.model.util.AbstractTypeVisitor6

<R,​P>

- javax.lang.model.util.SimpleTypeVisitor6<R,​P>

javax.lang.model.util.SimpleTypeVisitor6<R,​P>

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

**Direct Known Subclasses:** SimpleTypeVisitor7

,

TypeKindVisitor6

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleTypeVisitor6<R,​P>

extends
AbstractTypeVisitor6
<R,​P>
```

A simple visitor of types with default behavior appropriate for the

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

method. A new simple type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

**Since:** 1.6
**See Also:** SimpleTypeVisitor7

,

SimpleTypeVisitor8

,

SimpleTypeVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public class

SimpleTypeVisitor6<R,​P>

extends

AbstractTypeVisitor6

<R,​P>

A simple visitor of types with default behavior appropriate for the

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

method. A new simple type visitor
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

method. A new simple type visitor
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

method. A new simple type visitor
class will also be introduced to correspond to the new language
level; this visitor will have different default behavior for the
visit method in question. When the new visitor is introduced, all
or portions of this visitor may be deprecated.

When such a new visit method is added, the default
implementation in this class will be to call the

visitUnknown

method. A new simple type visitor
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

SimpleTypeVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleTypeVisitor6

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

TypeMirror

e,

P

p)

The default action for visit methods.

R

visitArray

​(

ArrayType

t,

P

p)

Visits an array type.

R

visitDeclared

​(

DeclaredType

t,

P

p)

Visits a declared type.

R

visitError

​(

ErrorType

t,

P

p)

Visits an error type.

R

visitExecutable

​(

ExecutableType

t,

P

p)

Visits an executable type.

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

visitNull

​(

NullType

t,

P

p)

Visits the null type.

R

visitPrimitive

​(

PrimitiveType

t,

P

p)

Visits a primitive type.

R

visitTypeVariable

​(

TypeVariable

t,

P

p)

Visits a type variable.

R

visitWildcard

​(

WildcardType

t,

P

p)

Visits a wildcard type.

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

SimpleTypeVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleTypeVisitor6

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

TypeMirror

e,

P

p)

The default action for visit methods.

R

visitArray

​(

ArrayType

t,

P

p)

Visits an array type.

R

visitDeclared

​(

DeclaredType

t,

P

p)

Visits a declared type.

R

visitError

​(

ErrorType

t,

P

p)

Visits an error type.

R

visitExecutable

​(

ExecutableType

t,

P

p)

Visits an executable type.

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

visitNull

​(

NullType

t,

P

p)

Visits the null type.

R

visitPrimitive

​(

PrimitiveType

t,

P

p)

Visits a primitive type.

R

visitTypeVariable

​(

TypeVariable

t,

P

p)

Visits a type variable.

R

visitWildcard

​(

WildcardType

t,

P

p)

Visits a wildcard type.

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

The default action for visit methods.

Visits an array type.

Visits a declared type.

Visits an error type.

Visits an executable type.

Visits a

NoType

instance.

Visits the null type.

Visits a primitive type.

Visits a type variable.

Visits a wildcard type.

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

- SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6​(
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
TypeMirror
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the type to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNull

```java
public
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type. This implementation calls

defaultAction

.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitArray

```java
public
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitDeclared

```java
public
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitError

```java
public
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeVariable

```java
public
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitWildcard

```java
public
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

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

- SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6​(
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

SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleTypeVisitor6

@Deprecated

(

since

="9")
protected SimpleTypeVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleTypeVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleTypeVisitor6​(
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

#### SimpleTypeVisitor6

@Deprecated

(

since

="9")
protected SimpleTypeVisitor6​(

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
TypeMirror
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the type to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitNull

```java
public
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type. This implementation calls

defaultAction

.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitArray

```java
public
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitDeclared

```java
public
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitError

```java
public
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitTypeVariable

```java
public
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitWildcard

```java
public
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitExecutable

```java
public
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

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

defaultAction

```java
protected
R
defaultAction​(
TypeMirror
e,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** e

- the type to process
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

---

#### defaultAction

protected

R

defaultAction​(

TypeMirror

e,

P

p)

The default action for visit methods.

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

#### visitPrimitive

public

R

visitPrimitive​(

PrimitiveType

t,

P

p)

Visits a primitive type.

visitNull

```java
public
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type. This implementation calls

defaultAction

.

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

#### visitNull

public

R

visitNull​(

NullType

t,

P

p)

Visits the null type. This implementation calls

defaultAction

.

visitArray

```java
public
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

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

#### visitArray

public

R

visitArray​(

ArrayType

t,

P

p)

Visits an array type.

visitDeclared

```java
public
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

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

#### visitDeclared

public

R

visitDeclared​(

DeclaredType

t,

P

p)

Visits a declared type.

visitError

```java
public
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

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

#### visitError

public

R

visitError​(

ErrorType

t,

P

p)

Visits an error type.

visitTypeVariable

```java
public
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

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

#### visitTypeVariable

public

R

visitTypeVariable​(

TypeVariable

t,

P

p)

Visits a type variable.

visitWildcard

```java
public
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

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

#### visitWildcard

public

R

visitWildcard​(

WildcardType

t,

P

p)

Visits a wildcard type.

visitExecutable

```java
public
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

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

#### visitExecutable

public

R

visitExecutable​(

ExecutableType

t,

P

p)

Visits an executable type.

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

---

