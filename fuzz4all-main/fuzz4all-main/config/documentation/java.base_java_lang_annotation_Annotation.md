# Interface Annotation

**Source:** `java.base\java\lang\annotation\Annotation.html`

### Class Description

```java
public interface
Annotation
```

The common interface extended by all annotation types. Note that an
interface that manually extends this one does

not

define
an annotation type. Also note that this interface does not itself
define an annotation type.

More information about annotation types can be found in section 9.6 of

The Java™ Language Specification

.

The

AnnotatedElement

interface discusses
compatibility concerns when evolving an annotation type from being
non-repeatable to being repeatable.

**All Known Implementing Classes:** BeanProperty

,

BooleanFlag

,

Category

,

ConstructorParameters

,

ConstructorProperties

,

ContentType

,

DataAmount

,

Deprecated

,

Description

,

DescriptorKey

,

Documented

,

Enabled

,

Experimental

,

Frequency

,

FunctionalInterface

,

Generated

,

Inherited

,

JavaBean

,

Label

,

MemoryAddress

,

MetadataDefinition

,

MXBean

,

Name

,

Native

,

Override

,

Percentage

,

Period

,

Registered

,

Relational

,

Repeatable

,

Retention

,

SafeVarargs

,

SettingDefinition

,

StackTrace

,

SupportedAnnotationTypes

,

SupportedOptions

,

SupportedSourceVersion

,

SuppressWarnings

,

SwingContainer

,

Target

,

Threshold

,

Timespan

,

Timestamp

,

Transient

,

TransitionFrom

,

TransitionTo

,

Unsigned

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean equals​(
Object
obj)

Returns true if the specified object represents an annotation
that is logically equivalent to this one. In other words,
returns true if the specified object is an instance of the same
annotation type as this instance, all of whose members are equal
to the corresponding member of this annotation, as defined below:

- Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the reference object with which to compare.

**Returns:**
- true if the specified object represents an annotation
that is logically equivalent to this one, otherwise false

**See Also:**
- Object.hashCode()

,

HashMap

---

#### int hashCode()

Returns the hash code of this annotation, as defined below:

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code of this annotation

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### String
toString()

Returns a string representation of this annotation. The details
of the representation are implementation-dependent, but the following
may be regarded as typical:

```java
@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)
```

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this annotation

---

#### Class
<? extends
Annotation
> annotationType()

Returns the annotation type of this annotation.

**Returns:**
- the annotation type of this annotation

---

### Additional Sections

#### Interface Annotation

**All Known Implementing Classes:** BeanProperty

,

BooleanFlag

,

Category

,

ConstructorParameters

,

ConstructorProperties

,

ContentType

,

DataAmount

,

Deprecated

,

Description

,

DescriptorKey

,

Documented

,

Enabled

,

Experimental

,

Frequency

,

FunctionalInterface

,

Generated

,

Inherited

,

JavaBean

,

Label

,

MemoryAddress

,

MetadataDefinition

,

MXBean

,

Name

,

Native

,

Override

,

Percentage

,

Period

,

Registered

,

Relational

,

Repeatable

,

Retention

,

SafeVarargs

,

SettingDefinition

,

StackTrace

,

SupportedAnnotationTypes

,

SupportedOptions

,

SupportedSourceVersion

,

SuppressWarnings

,

SwingContainer

,

Target

,

Threshold

,

Timespan

,

Timestamp

,

Transient

,

TransitionFrom

,

TransitionTo

,

Unsigned

```java
public interface
Annotation
```

The common interface extended by all annotation types. Note that an
interface that manually extends this one does

not

define
an annotation type. Also note that this interface does not itself
define an annotation type.

More information about annotation types can be found in section 9.6 of

The Java™ Language Specification

.

The

AnnotatedElement

interface discusses
compatibility concerns when evolving an annotation type from being
non-repeatable to being repeatable.

**Since:** 1.5

public interface

Annotation

The common interface extended by all annotation types. Note that an
interface that manually extends this one does

not

define
an annotation type. Also note that this interface does not itself
define an annotation type.

More information about annotation types can be found in section 9.6 of

The Java™ Language Specification

.

The

AnnotatedElement

interface discusses
compatibility concerns when evolving an annotation type from being
non-repeatable to being repeatable.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<? extends

Annotation

>

annotationType

()

Returns the annotation type of this annotation.

boolean

equals

​(

Object

obj)

Returns true if the specified object represents an annotation
that is logically equivalent to this one.

int

hashCode

()

Returns the hash code of this annotation, as defined below:

String

toString

()

Returns a string representation of this annotation.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Class

<? extends

Annotation

>

annotationType

()

Returns the annotation type of this annotation.

boolean

equals

​(

Object

obj)

Returns true if the specified object represents an annotation
that is logically equivalent to this one.

int

hashCode

()

Returns the hash code of this annotation, as defined below:

String

toString

()

Returns a string representation of this annotation.

---

#### Method Summary

Returns the annotation type of this annotation.

Returns true if the specified object represents an annotation
that is logically equivalent to this one.

Returns the hash code of this annotation, as defined below:

Returns a string representation of this annotation.

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
boolean equals​(
Object
obj)
```

Returns true if the specified object represents an annotation
that is logically equivalent to this one. In other words,
returns true if the specified object is an instance of the same
annotation type as this instance, all of whose members are equal
to the corresponding member of this annotation, as defined below:

- Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the specified object represents an annotation
that is logically equivalent to this one, otherwise false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code of this annotation, as defined below:

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

**Overrides:** hashCode

in class

Object
**Returns:** the hash code of this annotation
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
String
toString()
```

Returns a string representation of this annotation. The details
of the representation are implementation-dependent, but the following
may be regarded as typical:

```java
@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of this annotation

- annotationType

```java
Class
<? extends
Annotation
> annotationType()
```

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation

Method Detail

- equals

```java
boolean equals​(
Object
obj)
```

Returns true if the specified object represents an annotation
that is logically equivalent to this one. In other words,
returns true if the specified object is an instance of the same
annotation type as this instance, all of whose members are equal
to the corresponding member of this annotation, as defined below:

- Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the specified object represents an annotation
that is logically equivalent to this one, otherwise false
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
int hashCode()
```

Returns the hash code of this annotation, as defined below:

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

**Overrides:** hashCode

in class

Object
**Returns:** the hash code of this annotation
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
String
toString()
```

Returns a string representation of this annotation. The details
of the representation are implementation-dependent, but the following
may be regarded as typical:

```java
@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of this annotation

- annotationType

```java
Class
<? extends
Annotation
> annotationType()
```

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation

---

#### Method Detail

equals

```java
boolean equals​(
Object
obj)
```

Returns true if the specified object represents an annotation
that is logically equivalent to this one. In other words,
returns true if the specified object is an instance of the same
annotation type as this instance, all of whose members are equal
to the corresponding member of this annotation, as defined below:

- Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the reference object with which to compare.
**Returns:** true if the specified object represents an annotation
that is logically equivalent to this one, otherwise false
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

boolean equals​(

Object

obj)

Returns true if the specified object represents an annotation
that is logically equivalent to this one. In other words,
returns true if the specified object is an instance of the same
annotation type as this instance, all of whose members are equal
to the corresponding member of this annotation, as defined below:

- Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

Two corresponding primitive typed members whose values are

x

and

y

are considered equal if

x == y

,
unless their type is

float

or

double

.

Two corresponding

float

members whose values
are

x

and

y

are considered equal if

Float.valueOf(x).equals(Float.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0f

unequal to

-0.0f

.)

Two corresponding

double

members whose values
are

x

and

y

are considered equal if

Double.valueOf(x).equals(Double.valueOf(y))

.
(Unlike the

==

operator, NaN is considered equal
to itself, and

0.0

unequal to

-0.0

.)

Two corresponding

String

,

Class

, enum, or
annotation typed members whose values are

x

and

y

are considered equal if

x.equals(y)

. (Note that this
definition is recursive for annotation typed members.)

Two corresponding array typed members

x

and

y

are considered equal if

Arrays.equals(x, y)

, for the
appropriate overloading of

Arrays.equals(long[], long[])

.

hashCode

```java
int hashCode()
```

Returns the hash code of this annotation, as defined below:

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

**Overrides:** hashCode

in class

Object
**Returns:** the hash code of this annotation
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

int hashCode()

Returns the hash code of this annotation, as defined below:

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

The hash code of an annotation is the sum of the hash codes
of its members (including those with default values), as defined
below:

The hash code of an annotation member is (127 times the hash code
of the member-name as computed by

String.hashCode()

) XOR
the hash code of the member-value, as defined below:

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

The hash code of a member-value depends on its type:

- The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

The hash code of a primitive value

v

is equal to

WrapperType

.valueOf(

v

).hashCode()

, where

WrapperType

is the wrapper type corresponding
to the primitive type of

v

(

Byte

,

Character

,

Double

,

Float

,

Integer

,

Long

,

Short

, or

Boolean

).

The hash code of a string, enum, class, or annotation member-value
I

v

is computed as by calling

v

.hashCode()

. (In the case of annotation
member values, this is a recursive definition.)

The hash code of an array member-value is computed by calling
the appropriate overloading of

Arrays.hashCode

on the value. (There is one overloading for each primitive
type, and one for object reference types.)

toString

```java
String
toString()
```

Returns a string representation of this annotation. The details
of the representation are implementation-dependent, but the following
may be regarded as typical:

```java
@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)
```

**Overrides:** toString

in class

Object
**Returns:** a string representation of this annotation

---

#### toString

String

toString()

Returns a string representation of this annotation. The details
of the representation are implementation-dependent, but the following
may be regarded as typical:

```java
@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)
```

@com.acme.util.Name(first=Alfred, middle=E., last=Neuman)

annotationType

```java
Class
<? extends
Annotation
> annotationType()
```

Returns the annotation type of this annotation.

**Returns:** the annotation type of this annotation

---

#### annotationType

Class

<? extends

Annotation

> annotationType()

Returns the annotation type of this annotation.

---

