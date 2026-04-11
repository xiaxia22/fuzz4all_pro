# Class SimpleAnnotationValueVisitor6<R,​P>

**Source:** `java.compiler\javax\lang\model\util\SimpleAnnotationValueVisitor6.html`

### Class Description

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleAnnotationValueVisitor6<R,​P>

extends
AbstractAnnotationValueVisitor6
<R,​P>
```

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version. Visit methods call

defaultAction(java.lang.Object, P)

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
protected SimpleAnnotationValueVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### @Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6​(
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
Object
o,

P
p)

The default action for visit methods.

**Parameters:**
- o

- the value of the annotation
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

#### public
R
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
- the result of

defaultAction

**Implementation Requirements:**
- This implementation calls

defaultAction

.

---

### Additional Sections

#### Class SimpleAnnotationValueVisitor6<R,​P>

java.lang.Object

- javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>
- - javax.lang.model.util.SimpleAnnotationValueVisitor6<R,​P>

javax.lang.model.util.AbstractAnnotationValueVisitor6

<R,​P>

- javax.lang.model.util.SimpleAnnotationValueVisitor6<R,​P>

javax.lang.model.util.SimpleAnnotationValueVisitor6<R,​P>

**Type Parameters:** R

- the return type of this visitor's methods
**Type Parameters:** P

- the type of the additional parameter to this visitor's methods.

**All Implemented Interfaces:** AnnotationValueVisitor

<R,​P>

**Direct Known Subclasses:** SimpleAnnotationValueVisitor7

```java
@SupportedSourceVersion
(
RELEASE_6
)
public class
SimpleAnnotationValueVisitor6<R,​P>

extends
AbstractAnnotationValueVisitor6
<R,​P>
```

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version. Visit methods call

defaultAction(java.lang.Object, P)

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

**Since:** 1.6
**See Also:** SimpleAnnotationValueVisitor7

,

SimpleAnnotationValueVisitor8

,

SimpleAnnotationValueVisitor9

@SupportedSourceVersion

(

RELEASE_6

)
public class

SimpleAnnotationValueVisitor6<R,​P>

extends

AbstractAnnotationValueVisitor6

<R,​P>

A simple visitor for annotation values with default behavior
appropriate for the

RELEASE_6

source version. Visit methods call

defaultAction(java.lang.Object, P)

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

SimpleAnnotationValueVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleAnnotationValueVisitor6

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

Object

o,

P

p)

The default action for visit methods.

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

SimpleAnnotationValueVisitor6

()

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

protected

SimpleAnnotationValueVisitor6

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

Object

o,

P

p)

The default action for visit methods.

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

The default action for visit methods.

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

- SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6​(
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
Object
o,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** o

- the value of the annotation
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

- visitBoolean

```java
public
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitByte

```java
public
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitChar

```java
public
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitDouble

```java
public
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitFloat

```java
public
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitInt

```java
public
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitLong

```java
public
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitShort

```java
public
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitString

```java
public
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitType

```java
public
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitEnumConstant

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitAnnotation

```java
public
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitArray

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** vals

- the value being visited
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

- SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

- SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6​(
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

SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6()
```

Deprecated.

Release 6 is obsolete; update to a visitor for a newer
release level.

Constructor for concrete subclasses; uses

null

for the
default value.

---

#### SimpleAnnotationValueVisitor6

@Deprecated

(

since

="9")
protected SimpleAnnotationValueVisitor6()

Constructor for concrete subclasses; uses

null

for the
default value.

SimpleAnnotationValueVisitor6

```java
@Deprecated
(
since
="9")
protected SimpleAnnotationValueVisitor6​(
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

#### SimpleAnnotationValueVisitor6

@Deprecated

(

since

="9")
protected SimpleAnnotationValueVisitor6​(

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
Object
o,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** o

- the value of the annotation
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

- visitBoolean

```java
public
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitByte

```java
public
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitChar

```java
public
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitDouble

```java
public
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitFloat

```java
public
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitInt

```java
public
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitLong

```java
public
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitShort

```java
public
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitString

```java
public
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitType

```java
public
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitEnumConstant

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitAnnotation

```java
public
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

- visitArray

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** vals

- the value being visited
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
Object
o,

P
p)
```

The default action for visit methods.

**Implementation Requirements:** The implementation in this class just returns

DEFAULT_VALUE

; subclasses will commonly override this method.
**Parameters:** o

- the value of the annotation
**Parameters:** p

- a visitor-specified parameter
**Returns:** DEFAULT_VALUE

unless overridden

---

#### defaultAction

protected

R

defaultAction​(

Object

o,

P

p)

The default action for visit methods.

visitBoolean

```java
public
R
visitBoolean​(boolean b,

P
p)
```

Visits a

boolean

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitBoolean

public

R

visitBoolean​(boolean b,

P

p)

Visits a

boolean

value in an annotation.

visitByte

```java
public
R
visitByte​(byte b,

P
p)
```

Visits a

byte

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** b

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitByte

public

R

visitByte​(byte b,

P

p)

Visits a

byte

value in an annotation.

visitChar

```java
public
R
visitChar​(char c,

P
p)
```

Visits a

char

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitChar

public

R

visitChar​(char c,

P

p)

Visits a

char

value in an annotation.

visitDouble

```java
public
R
visitDouble​(double d,

P
p)
```

Visits a

double

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** d

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitDouble

public

R

visitDouble​(double d,

P

p)

Visits a

double

value in an annotation.

visitFloat

```java
public
R
visitFloat​(float f,

P
p)
```

Visits a

float

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** f

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitFloat

public

R

visitFloat​(float f,

P

p)

Visits a

float

value in an annotation.

visitInt

```java
public
R
visitInt​(int i,

P
p)
```

Visits an

int

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitInt

public

R

visitInt​(int i,

P

p)

Visits an

int

value in an annotation.

visitLong

```java
public
R
visitLong​(long i,

P
p)
```

Visits a

long

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** i

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitLong

public

R

visitLong​(long i,

P

p)

Visits a

long

value in an annotation.

visitShort

```java
public
R
visitShort​(short s,

P
p)
```

Visits a

short

value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitShort

public

R

visitShort​(short s,

P

p)

Visits a

short

value in an annotation.

visitString

```java
public
R
visitString​(
String
s,

P
p)
```

Visits a string value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** s

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitString

public

R

visitString​(

String

s,

P

p)

Visits a string value in an annotation.

visitType

```java
public
R
visitType​(
TypeMirror
t,

P
p)
```

Visits a type value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** t

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitType

public

R

visitType​(

TypeMirror

t,

P

p)

Visits a type value in an annotation.

visitEnumConstant

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** c

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitEnumConstant

public

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
public
R
visitAnnotation​(
AnnotationMirror
a,

P
p)
```

Visits an annotation value in an annotation.

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** a

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitAnnotation

public

R

visitAnnotation​(

AnnotationMirror

a,

P

p)

Visits an annotation value in an annotation.

visitArray

```java
public
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

**Implementation Requirements:** This implementation calls

defaultAction

.
**Parameters:** vals

- the value being visited
**Parameters:** p

- a visitor-specified parameter
**Returns:** the result of

defaultAction

---

#### visitArray

public

R

visitArray​(

List

<? extends

AnnotationValue

> vals,

P

p)

Visits an array value in an annotation.

---

