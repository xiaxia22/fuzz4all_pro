# Interface AnnotationValueVisitor<R,​P>

**Source:** `java.compiler\javax\lang\model\element\AnnotationValueVisitor.html`

### Class Description

```java
public interface
AnnotationValueVisitor<R,​P>
```

A visitor of the values of annotation type elements, using a
variant of the visitor design pattern. Unlike a standard visitor
which dispatches based on the concrete type of a member of a type
hierarchy, this visitor dispatches based on the type of data
stored; there are no distinct subclasses for storing, for example,

boolean

values versus

int

values. Classes
implementing this interface are used to operate on a value when the
type of that value is unknown at compile time. When a visitor is
passed to a value's

accept

method,
the

visit

Xyz

method applicable to that value is
invoked.

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

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### R
visit​(
AnnotationValue
av,

P
p)

Visits an annotation value.

**Parameters:**
- av

- the value to visit
- p

- a visitor-specified parameter

**Returns:**
- a visitor-specified result

---

#### default
R
visit​(
AnnotationValue
av)

A convenience method equivalent to

visit(av, null)

.

**Parameters:**
- av

- the value to visit

**Returns:**
- a visitor-specified result

**Implementation Requirements:**
- The default implementation is

visit(av, null)

.

---

#### R
visitBoolean​(boolean b,

P
p)

Visits a

boolean

value in an annotation.

**Parameters:**
- b

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitByte​(byte b,

P
p)

Visits a

byte

value in an annotation.

**Parameters:**
- b

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitChar​(char c,

P
p)

Visits a

char

value in an annotation.

**Parameters:**
- c

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitDouble​(double d,

P
p)

Visits a

double

value in an annotation.

**Parameters:**
- d

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitFloat​(float f,

P
p)

Visits a

float

value in an annotation.

**Parameters:**
- f

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitInt​(int i,

P
p)

Visits an

int

value in an annotation.

**Parameters:**
- i

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitLong​(long i,

P
p)

Visits a

long

value in an annotation.

**Parameters:**
- i

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitShort​(short s,

P
p)

Visits a

short

value in an annotation.

**Parameters:**
- s

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitString​(
String
s,

P
p)

Visits a string value in an annotation.

**Parameters:**
- s

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitType​(
TypeMirror
t,

P
p)

Visits a type value in an annotation.

**Parameters:**
- t

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitEnumConstant​(
VariableElement
c,

P
p)

Visits an

enum

value in an annotation.

**Parameters:**
- c

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitAnnotation​(
AnnotationMirror
a,

P
p)

Visits an annotation value in an annotation.

**Parameters:**
- a

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitArray​(
List
<? extends
AnnotationValue
> vals,

P
p)

Visits an array value in an annotation.

**Parameters:**
- vals

- the value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

---

#### R
visitUnknown​(
AnnotationValue
av,

P
p)

Visits an unknown kind of annotation value.
This can occur if the language evolves and new kinds
of value can be stored in an annotation.

**Parameters:**
- av

- the unknown value being visited
- p

- a visitor-specified parameter

**Returns:**
- the result of the visit

**Throws:**
- UnknownAnnotationValueException

- a visitor implementation may optionally throw this exception

---

### Additional Sections

#### Interface AnnotationValueVisitor<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

**All Known Implementing Classes:** AbstractAnnotationValueVisitor6

,

AbstractAnnotationValueVisitor7

,

AbstractAnnotationValueVisitor8

,

AbstractAnnotationValueVisitor9

,

SimpleAnnotationValueVisitor6

,

SimpleAnnotationValueVisitor7

,

SimpleAnnotationValueVisitor8

,

SimpleAnnotationValueVisitor9

```java
public interface
AnnotationValueVisitor<R,​P>
```

A visitor of the values of annotation type elements, using a
variant of the visitor design pattern. Unlike a standard visitor
which dispatches based on the concrete type of a member of a type
hierarchy, this visitor dispatches based on the type of data
stored; there are no distinct subclasses for storing, for example,

boolean

values versus

int

values. Classes
implementing this interface are used to operate on a value when the
type of that value is unknown at compile time. When a visitor is
passed to a value's

accept

method,
the

visit

Xyz

method applicable to that value is
invoked.

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

AnnotationValueVisitor<R,​P>

A visitor of the values of annotation type elements, using a
variant of the visitor design pattern. Unlike a standard visitor
which dispatches based on the concrete type of a member of a type
hierarchy, this visitor dispatches based on the type of data
stored; there are no distinct subclasses for storing, for example,

boolean

values versus

int

values. Classes
implementing this interface are used to operate on a value when the
type of that value is unknown at compile time. When a visitor is
passed to a value's

accept

method,
the

visit

Xyz

method applicable to that value is
invoked.

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

AnnotationValue

av)

A convenience method equivalent to

visit(av, null)

.

R

visit

​(

AnnotationValue

av,

P

p)

Visits an annotation value.

R

visitAnnotation

​(

AnnotationMirror

a,

P

p)

Visits an annotation value in an annotation.

R

visitArray

​(

List

<? extends

AnnotationValue

> vals,

P

p)

Visits an array value in an annotation.

R

visitBoolean

​(boolean b,

P

p)

Visits a

boolean

value in an annotation.

R

visitByte

​(byte b,

P

p)

Visits a

byte

value in an annotation.

R

visitChar

​(char c,

P

p)

Visits a

char

value in an annotation.

R

visitDouble

​(double d,

P

p)

Visits a

double

value in an annotation.

R

visitEnumConstant

​(

VariableElement

c,

P

p)

Visits an

enum

value in an annotation.

R

visitFloat

​(float f,

P

p)

Visits a

float

value in an annotation.

R

visitInt

​(int i,

P

p)

Visits an

int

value in an annotation.

R

visitLong

​(long i,

P

p)

Visits a

long

value in an annotation.

R

visitShort

​(short s,

P

p)

Visits a

short

value in an annotation.

R

visitString

​(

String

s,

P

p)

Visits a string value in an annotation.

R

visitType

​(

TypeMirror

t,

P

p)

Visits a type value in an annotation.

R

visitUnknown

​(

AnnotationValue

av,

P

p)

Visits an unknown kind of annotation value.

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

AnnotationValue

av)

A convenience method equivalent to

visit(av, null)

.

R

visit

​(

AnnotationValue

av,

P

p)

Visits an annotation value.

R

visitAnnotation

​(

AnnotationMirror

a,

P

p)

Visits an annotation value in an annotation.

R

visitArray

​(

List

<? extends

AnnotationValue

> vals,

P

p)

Visits an array value in an annotation.

R

visitBoolean

​(boolean b,

P

p)

Visits a

boolean

value in an annotation.

R

visitByte

​(byte b,

P

p)

Visits a

byte

value in an annotation.

R

visitChar

​(char c,

P

p)

Visits a

char

value in an annotation.

R

visitDouble

​(double d,

P

p)

Visits a

double

value in an annotation.

R

visitEnumConstant

​(

VariableElement

c,

P

p)

Visits an

enum

value in an annotation.

R

visitFloat

​(float f,

P

p)

Visits a

float

value in an annotation.

R

visitInt

​(int i,

P

p)

Visits an

int

value in an annotation.

R

visitLong

​(long i,

P

p)

Visits a

long

value in an annotation.

R

visitShort

​(short s,

P

p)

Visits a

short

value in an annotation.

R

visitString

​(

String

s,

P

p)

Visits a string value in an annotation.

R

visitType

​(

TypeMirror

t,

P

p)

Visits a type value in an annotation.

R

visitUnknown

​(

AnnotationValue

av,

P

p)

Visits an unknown kind of annotation value.

---

#### Method Summary

A convenience method equivalent to

visit(av, null)

.

Visits an annotation value.

Visits an annotation value in an annotation.

Visits an array value in an annotation.

Visits a

boolean

value in an annotation.

Visits a

byte

value in an annotation.

Visits a

char

value in an annotation.

Visits a

double

value in an annotation.

Visits an

enum

value in an annotation.

Visits a

float

value in an annotation.

Visits an

int

value in an annotation.

Visits a

long

value in an annotation.

Visits a

short

value in an annotation.

Visits a string value in an annotation.

Visits a type value in an annotation.

Visits an unknown kind of annotation value.

============ METHOD DETAIL ==========

- Method Detail

- visit

```java
R
visit​(
AnnotationValue
av,

P
p)
```

Visits an annotation value.

**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
AnnotationValue
av)
```

A convenience method equivalent to

visit(av, null)

.

**Implementation Requirements:** The default implementation is

visit(av, null)

.
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

- visitBoolean

```java
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitByte

```java
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitChar

```java
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitDouble

```java
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitFloat

```java
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitInt

```java
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitLong

```java
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitShort

```java
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitString

```java
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitType

```java
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitEnumConstant

```java
R
visitEnumConstant​(
VariableElement
c,

P
p)
```

Visits an

enum

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitAnnotation

```java
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitArray

```java
R
visitArray​(
List
<? extends
AnnotationValue
> vals,

P
p)
```

Visits an array value in an annotation.

**Parameters:** vals

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitUnknown

```java
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

**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit
**Throws:** UnknownAnnotationValueException

- a visitor implementation may optionally throw this exception

Method Detail

- visit

```java
R
visit​(
AnnotationValue
av,

P
p)
```

Visits an annotation value.

**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

- visit

```java
default
R
visit​(
AnnotationValue
av)
```

A convenience method equivalent to

visit(av, null)

.

**Implementation Requirements:** The default implementation is

visit(av, null)

.
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

- visitBoolean

```java
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitByte

```java
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitChar

```java
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitDouble

```java
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitFloat

```java
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitInt

```java
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitLong

```java
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitShort

```java
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitString

```java
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitType

```java
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitEnumConstant

```java
R
visitEnumConstant​(
VariableElement
c,

P
p)
```

Visits an

enum

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitAnnotation

```java
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitArray

```java
R
visitArray​(
List
<? extends
AnnotationValue
> vals,

P
p)
```

Visits an array value in an annotation.

**Parameters:** vals

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

- visitUnknown

```java
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

**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit
**Throws:** UnknownAnnotationValueException

- a visitor implementation may optionally throw this exception

---

#### Method Detail

visit

```java
R
visit​(
AnnotationValue
av,

P
p)
```

Visits an annotation value.

**Parameters:** av

- the value to visit
**Parameters:** p

- a visitor-specified parameter
**Returns:** a visitor-specified result

---

#### visit

R

visit​(

AnnotationValue

av,

P

p)

Visits an annotation value.

visit

```java
default
R
visit​(
AnnotationValue
av)
```

A convenience method equivalent to

visit(av, null)

.

**Implementation Requirements:** The default implementation is

visit(av, null)

.
**Parameters:** av

- the value to visit
**Returns:** a visitor-specified result

---

#### visit

default

R

visit​(

AnnotationValue

av)

A convenience method equivalent to

visit(av, null)

.

visitBoolean

```java
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitBoolean

R

visitBoolean​(boolean b,

P

p)

Visits a

boolean

value in an annotation.

visitByte

```java
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitByte

R

visitByte​(byte b,

P

p)

Visits a

byte

value in an annotation.

visitChar

```java
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitChar

R

visitChar​(char c,

P

p)

Visits a

char

value in an annotation.

visitDouble

```java
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitDouble

R

visitDouble​(double d,

P

p)

Visits a

double

value in an annotation.

visitFloat

```java
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitFloat

R

visitFloat​(float f,

P

p)

Visits a

float

value in an annotation.

visitInt

```java
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitInt

R

visitInt​(int i,

P

p)

Visits an

int

value in an annotation.

visitLong

```java
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitLong

R

visitLong​(long i,

P

p)

Visits a

long

value in an annotation.

visitShort

```java
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitShort

R

visitShort​(short s,

P

p)

Visits a

short

value in an annotation.

visitString

```java
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitString

R

visitString​(

String

s,

P

p)

Visits a string value in an annotation.

visitType

```java
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitType

R

visitType​(

TypeMirror

t,

P

p)

Visits a type value in an annotation.

visitEnumConstant

```java
R
visitEnumConstant​(
VariableElement
c,

P
p)
```

Visits an

enum

value in an annotation.

**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitEnumConstant

R

visitEnumConstant​(

VariableElement

c,

P

p)

Visits an

enum

value in an annotation.

visitAnnotation

```java
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitAnnotation

R

visitAnnotation​(

AnnotationMirror

a,

P

p)

Visits an annotation value in an annotation.

visitArray

```java
R
visitArray​(
List
<? extends
AnnotationValue
> vals,

P
p)
```

Visits an array value in an annotation.

**Parameters:** vals

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit

---

#### visitArray

R

visitArray​(

List

<? extends

AnnotationValue

> vals,

P

p)

Visits an array value in an annotation.

visitUnknown

```java
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

**Parameters:** av

- the unknown value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of the visit
**Throws:** UnknownAnnotationValueException

- a visitor implementation may optionally throw this exception

---

#### visitUnknown

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

