# Class IntegerSyntax

**Source:** `java.desktop\javax\print\attribute\IntegerSyntax.html`

### Class Description

```java
public abstract class
IntegerSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

IntegerSyntax

is an abstract base class providing the common
implementation of all attributes with integer values.

Under the hood, an integer attribute is just an integer. You can get an
integer attribute's integer value by calling

getValue()

.
An integer attribute's integer value is established when it is constructed
(see

IntegerSyntax(int)

). Once constructed, an
integer attribute's value is immutable.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected IntegerSyntax​(int value)

Construct a new integer attribute with the given integer value.

**Parameters:**
- value

- Integer value

---

#### protected IntegerSyntax​(int value,
int lowerBound,
int upperBound)

Construct a new integer attribute with the given integer value, which
must lie within the given range.

**Parameters:**
- value

- Integer value
- lowerBound

- Lower bound
- upperBound

- Upper bound

**Throws:**
- IllegalArgumentException

- if

value

is less than

lowerBound

or greater than

upperBound

---

### Method Details

#### public int getValue()

Returns this integer attribute's integer value.

**Returns:**
- the integer value

---

#### public boolean equals​(
Object
object)

Returns whether this integer attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this integer
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this integer attribute. The hash code is
just this integer attribute's integer value.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string value corresponding to this integer attribute. The
string value is just this integer attribute's integer value converted to
a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class IntegerSyntax

java.lang.Object

- javax.print.attribute.IntegerSyntax

javax.print.attribute.IntegerSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** Copies

,

JobImpressions

,

JobImpressionsCompleted

,

JobKOctets

,

JobKOctetsProcessed

,

JobMediaSheets

,

JobMediaSheetsCompleted

,

JobPriority

,

JobPrioritySupported

,

NumberOfDocuments

,

NumberOfInterveningJobs

,

NumberUp

,

PagesPerMinute

,

PagesPerMinuteColor

,

QueuedJobCount

```java
public abstract class
IntegerSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

IntegerSyntax

is an abstract base class providing the common
implementation of all attributes with integer values.

Under the hood, an integer attribute is just an integer. You can get an
integer attribute's integer value by calling

getValue()

.
An integer attribute's integer value is established when it is constructed
(see

IntegerSyntax(int)

). Once constructed, an
integer attribute's value is immutable.

**See Also:** Serialized Form

public abstract class

IntegerSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

IntegerSyntax

is an abstract base class providing the common
implementation of all attributes with integer values.

Under the hood, an integer attribute is just an integer. You can get an
integer attribute's integer value by calling

getValue()

.
An integer attribute's integer value is established when it is constructed
(see

IntegerSyntax(int)

). Once constructed, an
integer attribute's value is immutable.

Under the hood, an integer attribute is just an integer. You can get an
integer attribute's integer value by calling

getValue()

.
An integer attribute's integer value is established when it is constructed
(see

IntegerSyntax(int)

). Once constructed, an
integer attribute's value is immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

IntegerSyntax

​(int value)

Construct a new integer attribute with the given integer value.

protected

IntegerSyntax

​(int value,
int lowerBound,
int upperBound)

Construct a new integer attribute with the given integer value, which
must lie within the given range.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this integer attribute is equivalent to the passed in
object.

int

getValue

()

Returns this integer attribute's integer value.

int

hashCode

()

Returns a hash code value for this integer attribute.

String

toString

()

Returns a string value corresponding to this integer attribute.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

IntegerSyntax

​(int value)

Construct a new integer attribute with the given integer value.

protected

IntegerSyntax

​(int value,
int lowerBound,
int upperBound)

Construct a new integer attribute with the given integer value, which
must lie within the given range.

---

#### Constructor Summary

Construct a new integer attribute with the given integer value.

Construct a new integer attribute with the given integer value, which
must lie within the given range.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this integer attribute is equivalent to the passed in
object.

int

getValue

()

Returns this integer attribute's integer value.

int

hashCode

()

Returns a hash code value for this integer attribute.

String

toString

()

Returns a string value corresponding to this integer attribute.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns whether this integer attribute is equivalent to the passed in
object.

Returns this integer attribute's integer value.

Returns a hash code value for this integer attribute.

Returns a string value corresponding to this integer attribute.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- IntegerSyntax

```java
protected IntegerSyntax​(int value)
```

Construct a new integer attribute with the given integer value.

**Parameters:** value

- Integer value

- IntegerSyntax

```java
protected IntegerSyntax​(int value,
int lowerBound,
int upperBound)
```

Construct a new integer attribute with the given integer value, which
must lie within the given range.

**Parameters:** value

- Integer value
**Parameters:** lowerBound

- Lower bound
**Parameters:** upperBound

- Upper bound
**Throws:** IllegalArgumentException

- if

value

is less than

lowerBound

or greater than

upperBound

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public int getValue()
```

Returns this integer attribute's integer value.

**Returns:** the integer value

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this integer attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this integer
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this integer attribute. The hash code is
just this integer attribute's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string value corresponding to this integer attribute. The
string value is just this integer attribute's integer value converted to
a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- IntegerSyntax

```java
protected IntegerSyntax​(int value)
```

Construct a new integer attribute with the given integer value.

**Parameters:** value

- Integer value

- IntegerSyntax

```java
protected IntegerSyntax​(int value,
int lowerBound,
int upperBound)
```

Construct a new integer attribute with the given integer value, which
must lie within the given range.

**Parameters:** value

- Integer value
**Parameters:** lowerBound

- Lower bound
**Parameters:** upperBound

- Upper bound
**Throws:** IllegalArgumentException

- if

value

is less than

lowerBound

or greater than

upperBound

---

#### Constructor Detail

IntegerSyntax

```java
protected IntegerSyntax​(int value)
```

Construct a new integer attribute with the given integer value.

**Parameters:** value

- Integer value

---

#### IntegerSyntax

protected IntegerSyntax​(int value)

Construct a new integer attribute with the given integer value.

IntegerSyntax

```java
protected IntegerSyntax​(int value,
int lowerBound,
int upperBound)
```

Construct a new integer attribute with the given integer value, which
must lie within the given range.

**Parameters:** value

- Integer value
**Parameters:** lowerBound

- Lower bound
**Parameters:** upperBound

- Upper bound
**Throws:** IllegalArgumentException

- if

value

is less than

lowerBound

or greater than

upperBound

---

#### IntegerSyntax

protected IntegerSyntax​(int value,
int lowerBound,
int upperBound)

Construct a new integer attribute with the given integer value, which
must lie within the given range.

Method Detail

- getValue

```java
public int getValue()
```

Returns this integer attribute's integer value.

**Returns:** the integer value

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this integer attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this integer
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this integer attribute. The hash code is
just this integer attribute's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string value corresponding to this integer attribute. The
string value is just this integer attribute's integer value converted to
a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getValue

```java
public int getValue()
```

Returns this integer attribute's integer value.

**Returns:** the integer value

---

#### getValue

public int getValue()

Returns this integer attribute's integer value.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this integer attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this integer
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this integer attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

object

is not

null

.

object

is an instance of class

IntegerSyntax

.

This integer attribute's value and

object

's value are
equal.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this integer attribute. The hash code is
just this integer attribute's integer value.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this integer attribute. The hash code is
just this integer attribute's integer value.

toString

```java
public
String
toString()
```

Returns a string value corresponding to this integer attribute. The
string value is just this integer attribute's integer value converted to
a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string value corresponding to this integer attribute. The
string value is just this integer attribute's integer value converted to
a string.

---

