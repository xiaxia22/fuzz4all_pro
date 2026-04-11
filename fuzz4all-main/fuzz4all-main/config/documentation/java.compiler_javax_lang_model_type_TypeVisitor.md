# Interface TypeVisitor<R,​P>

**Source:** `java.compiler\javax\lang\model\type\TypeVisitor.html`

### Class Description

```java
public interface
TypeVisitor<R,​P>
```

A visitor of types, in the style of the
visitor design pattern. Classes implementing this
interface are used to operate on a type when the kind of
type is unknown at compile time. When a visitor is passed to a
type's

accept

method, the

visit

Xyz

method most applicable to that type is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

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

*No entries found.*

### Method Details

#### R
visit​(
TypeMirror
t,

P
p)

Visits a type.

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### default
R
visit​(
TypeMirror
t)

A convenience method equivalent to

visit(t, null)

.

**Parameters:**
- t

- the element to visit

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- The default implementation is

visit(t, null)

.

---

#### R
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
- a visitor-specified result

---

#### R
visitNull​(
NullType
t,

P
p)

Visits the null type.

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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
- a visitor-specified result

---

#### R
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

---

#### R
visitUnion​(
UnionType
t,

P
p)

Visits a union type.

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Since:**
- 1.7

---

#### R
visitIntersection​(
IntersectionType
t,

P
p)

Visits an intersection type.

**Parameters:**
- t

- the type to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

**Since:**
- 1.8

---

### Additional Sections

#### Interface TypeVisitor<R,​P>

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

**All Known Implementing Classes:** AbstractTypeVisitor6

,

AbstractTypeVisitor7

,

AbstractTypeVisitor8

,

AbstractTypeVisitor9

,

SimpleTypeVisitor6

,

SimpleTypeVisitor7

,

SimpleTypeVisitor8

,

SimpleTypeVisitor9

,

TypeKindVisitor6

,

TypeKindVisitor7

,

TypeKindVisitor8

,

TypeKindVisitor9

```java
public interface
TypeVisitor<R,​P>
```

A visitor of types, in the style of the
visitor design pattern. Classes implementing this
interface are used to operate on a type when the kind of
type is unknown at compile time. When a visitor is passed to a
type's

accept

method, the

visit

Xyz

method most applicable to that type is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

**Since:** 1.6

public interface

TypeVisitor<R,​P>

A visitor of types, in the style of the
visitor design pattern. Classes implementing this
interface are used to operate on a type when the kind of
type is unknown at compile time. When a visitor is passed to a
type's

accept

method, the

visit

Xyz

method most applicable to that type is invoked.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

Classes implementing this interface may or may not throw a

NullPointerException

if the additional parameter

p

is

null

; see documentation of the implementing class for
details.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

WARNING:

It is possible that methods will be added to
this interface to accommodate new, currently unknown, language
structures added to future versions of the Java™ programming
language. Therefore, visitor classes directly implementing this
interface may be source incompatible with future versions of the
platform. To avoid this source incompatibility, visitor
implementations are encouraged to instead extend the appropriate
abstract visitor class that implements this interface. However, an
API should generally use this visitor interface as the type for
parameters, return type, etc. rather than one of the abstract
classes.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

Note that methods to accommodate new language constructs could
be added in a source

compatible

way if they were added as

default methods

. However, default methods are only
available on Java SE 8 and higher releases and the

javax.lang.model.*

packages bundled in Java SE 8 were required to
also be runnable on Java SE 7. Therefore, default methods
were

not

used when extending

javax.lang.model.*

to cover Java SE 8 language features. However, default methods
are used in subsequent revisions of the

javax.lang.model.*

packages that are only required to run on Java SE 8 and higher
platform versions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

TypeMirror

t)

A convenience method equivalent to

visit(t, null)

.

R

visit

​(

TypeMirror

t,

P

p)

Visits a type.

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

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

R

visitWildcard

​(

WildcardType

t,

P

p)

Visits a wildcard type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default

R

visit

​(

TypeMirror

t)

A convenience method equivalent to

visit(t, null)

.

R

visit

​(

TypeMirror

t,

P

p)

Visits a type.

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

visitIntersection

​(

IntersectionType

t,

P

p)

Visits an intersection type.

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

R

visitWildcard

​(

WildcardType

t,

P

p)

Visits a wildcard type.

---

#### Method Summary

A convenience method equivalent to

visit(t, null)

.

Visits a type.

Visits an array type.

Visits a declared type.

Visits an error type.

Visits an executable type.

Visits an intersection type.

Visits a

NoType

instance.

Visits the null type.

Visits a primitive type.

Visits a type variable.

Visits a union type.

Visits an unknown kind of type.

Visits a wildcard type.

============ METHOD DETAIL ==========

- Method Detail

- visit

```java
R
visit​(
TypeMirror
t,

P
p)
```

Visits a type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
TypeMirror
t)
```

A convenience method equivalent to

visit(t, null)

.

**Implementation Requirements:** The default implementation is

visit(t, null)

.
**Parameters:** t

- the element to visit
**Returns:** a visitor-specified result

- visitPrimitive

```java
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitNull

```java
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitArray

```java
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitDeclared

```java
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitError

```java
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitTypeVariable

```java
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitWildcard

```java
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExecutable

```java
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitNoType

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

- visitUnion

```java
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.7

- visitIntersection

```java
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.8

Method Detail

- visit

```java
R
visit​(
TypeMirror
t,

P
p)
```

Visits a type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
TypeMirror
t)
```

A convenience method equivalent to

visit(t, null)

.

**Implementation Requirements:** The default implementation is

visit(t, null)

.
**Parameters:** t

- the element to visit
**Returns:** a visitor-specified result

- visitPrimitive

```java
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitNull

```java
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitArray

```java
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitDeclared

```java
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitError

```java
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitTypeVariable

```java
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitWildcard

```java
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitExecutable

```java
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitNoType

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visitUnknown

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

- visitUnion

```java
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.7

- visitIntersection

```java
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.8

---

#### Method Detail

visit

```java
R
visit​(
TypeMirror
t,

P
p)
```

Visits a type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

R

visit​(

TypeMirror

t,

P

p)

Visits a type.

visit

```java
default
R
visit​(
TypeMirror
t)
```

A convenience method equivalent to

visit(t, null)

.

**Implementation Requirements:** The default implementation is

visit(t, null)

.
**Parameters:** t

- the element to visit
**Returns:** a visitor-specified result

---

#### visit

default

R

visit​(

TypeMirror

t)

A convenience method equivalent to

visit(t, null)

.

visitPrimitive

```java
R
visitPrimitive​(
PrimitiveType
t,

P
p)
```

Visits a primitive type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitPrimitive

R

visitPrimitive​(

PrimitiveType

t,

P

p)

Visits a primitive type.

visitNull

```java
R
visitNull​(
NullType
t,

P
p)
```

Visits the null type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitNull

R

visitNull​(

NullType

t,

P

p)

Visits the null type.

visitArray

```java
R
visitArray​(
ArrayType
t,

P
p)
```

Visits an array type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitArray

R

visitArray​(

ArrayType

t,

P

p)

Visits an array type.

visitDeclared

```java
R
visitDeclared​(
DeclaredType
t,

P
p)
```

Visits a declared type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitDeclared

R

visitDeclared​(

DeclaredType

t,

P

p)

Visits a declared type.

visitError

```java
R
visitError​(
ErrorType
t,

P
p)
```

Visits an error type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitError

R

visitError​(

ErrorType

t,

P

p)

Visits an error type.

visitTypeVariable

```java
R
visitTypeVariable​(
TypeVariable
t,

P
p)
```

Visits a type variable.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitTypeVariable

R

visitTypeVariable​(

TypeVariable

t,

P

p)

Visits a type variable.

visitWildcard

```java
R
visitWildcard​(
WildcardType
t,

P
p)
```

Visits a wildcard type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitWildcard

R

visitWildcard​(

WildcardType

t,

P

p)

Visits a wildcard type.

visitExecutable

```java
R
visitExecutable​(
ExecutableType
t,

P
p)
```

Visits an executable type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitExecutable

R

visitExecutable​(

ExecutableType

t,

P

p)

Visits an executable type.

visitNoType

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visitNoType

R

visitNoType​(

NoType

t,

P

p)

Visits a

NoType

instance.

visitUnknown

```java
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

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Throws:** UnknownTypeException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

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

visitUnion

```java
R
visitUnion​(
UnionType
t,

P
p)
```

Visits a union type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.7

---

#### visitUnion

R

visitUnion​(

UnionType

t,

P

p)

Visits a union type.

visitIntersection

```java
R
visitIntersection​(
IntersectionType
t,

P
p)
```

Visits an intersection type.

**Parameters:** t

- the type to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result
**Since:** 1.8

---

#### visitIntersection

R

visitIntersection​(

IntersectionType

t,

P

p)

Visits an intersection type.

---

