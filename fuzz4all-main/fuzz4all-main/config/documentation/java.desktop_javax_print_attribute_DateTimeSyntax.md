# Class DateTimeSyntax

**Source:** `java.desktop\javax\print\attribute\DateTimeSyntax.html`

### Class Description

```java
public abstract class
DateTimeSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

DateTimeSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a date and time.

Under the hood, a date-time attribute is stored as a value of class

java.util.Date

. You can get a date-time attribute's

Date

value by calling

getValue()

. A date-time attribute's

Date

value is established when it is constructed (see

DateTimeSyntax(Date)

). Once constructed, a
date-time attribute's value is immutable.

To construct a date-time attribute from separate values of the year, month,
day, hour, minute, and so on, use a

java.util.Calendar

object to
construct a

java.util.Date

object, then use the

java.util.Date

object to construct the date-time attribute. To
convert a date-time attribute to separate values of the year, month, day,
hour, minute, and so on, create a

java.util.Calendar

object and set
it to the

java.util.Date

from the date-time attribute. Class

DateTimeSyntax

stores its value in the form of a

java.util.Date

rather than a

java.util.Calendar

because it
typically takes less memory to store and less time to compare a

java.util.Date

than a

java.util.Calendar

.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected DateTimeSyntax​(
Date
value)

Construct a new date-time attribute with the given

java.util.Date

value.

**Parameters:**
- value

-

java.util.Date

value

**Throws:**
- NullPointerException

- if

value

is

null

---

### Method Details

#### public
Date
getValue()

Returns this date-time attribute's

java.util.Date

value.

**Returns:**
- the

Date

---

#### public boolean equals​(
Object
object)

Returns whether this date-time attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

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

is equivalent to this date-time
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this date-time attribute. The hashcode is
that of this attribute's

java.util.Date

value.

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

Returns a string value corresponding to this date-time attribute. The
string value is just this attribute's

java.util.Date

value
converted to a string.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class DateTimeSyntax

java.lang.Object

- javax.print.attribute.DateTimeSyntax

javax.print.attribute.DateTimeSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** DateTimeAtCompleted

,

DateTimeAtCreation

,

DateTimeAtProcessing

,

JobHoldUntil

```java
public abstract class
DateTimeSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

DateTimeSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a date and time.

Under the hood, a date-time attribute is stored as a value of class

java.util.Date

. You can get a date-time attribute's

Date

value by calling

getValue()

. A date-time attribute's

Date

value is established when it is constructed (see

DateTimeSyntax(Date)

). Once constructed, a
date-time attribute's value is immutable.

To construct a date-time attribute from separate values of the year, month,
day, hour, minute, and so on, use a

java.util.Calendar

object to
construct a

java.util.Date

object, then use the

java.util.Date

object to construct the date-time attribute. To
convert a date-time attribute to separate values of the year, month, day,
hour, minute, and so on, create a

java.util.Calendar

object and set
it to the

java.util.Date

from the date-time attribute. Class

DateTimeSyntax

stores its value in the form of a

java.util.Date

rather than a

java.util.Calendar

because it
typically takes less memory to store and less time to compare a

java.util.Date

than a

java.util.Calendar

.

**See Also:** Serialized Form

public abstract class

DateTimeSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

DateTimeSyntax

is an abstract base class providing the common
implementation of all attributes whose value is a date and time.

Under the hood, a date-time attribute is stored as a value of class

java.util.Date

. You can get a date-time attribute's

Date

value by calling

getValue()

. A date-time attribute's

Date

value is established when it is constructed (see

DateTimeSyntax(Date)

). Once constructed, a
date-time attribute's value is immutable.

To construct a date-time attribute from separate values of the year, month,
day, hour, minute, and so on, use a

java.util.Calendar

object to
construct a

java.util.Date

object, then use the

java.util.Date

object to construct the date-time attribute. To
convert a date-time attribute to separate values of the year, month, day,
hour, minute, and so on, create a

java.util.Calendar

object and set
it to the

java.util.Date

from the date-time attribute. Class

DateTimeSyntax

stores its value in the form of a

java.util.Date

rather than a

java.util.Calendar

because it
typically takes less memory to store and less time to compare a

java.util.Date

than a

java.util.Calendar

.

Under the hood, a date-time attribute is stored as a value of class

java.util.Date

. You can get a date-time attribute's

Date

value by calling

getValue()

. A date-time attribute's

Date

value is established when it is constructed (see

DateTimeSyntax(Date)

). Once constructed, a
date-time attribute's value is immutable.

To construct a date-time attribute from separate values of the year, month,
day, hour, minute, and so on, use a

java.util.Calendar

object to
construct a

java.util.Date

object, then use the

java.util.Date

object to construct the date-time attribute. To
convert a date-time attribute to separate values of the year, month, day,
hour, minute, and so on, create a

java.util.Calendar

object and set
it to the

java.util.Date

from the date-time attribute. Class

DateTimeSyntax

stores its value in the form of a

java.util.Date

rather than a

java.util.Calendar

because it
typically takes less memory to store and less time to compare a

java.util.Date

than a

java.util.Calendar

.

To construct a date-time attribute from separate values of the year, month,
day, hour, minute, and so on, use a

java.util.Calendar

object to
construct a

java.util.Date

object, then use the

java.util.Date

object to construct the date-time attribute. To
convert a date-time attribute to separate values of the year, month, day,
hour, minute, and so on, create a

java.util.Calendar

object and set
it to the

java.util.Date

from the date-time attribute. Class

DateTimeSyntax

stores its value in the form of a

java.util.Date

rather than a

java.util.Calendar

because it
typically takes less memory to store and less time to compare a

java.util.Date

than a

java.util.Calendar

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

DateTimeSyntax

​(

Date

value)

Construct a new date-time attribute with the given

java.util.Date

value.

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

Returns whether this date-time attribute is equivalent to the passed in
object.

Date

getValue

()

Returns this date-time attribute's

java.util.Date

value.

int

hashCode

()

Returns a hash code value for this date-time attribute.

String

toString

()

Returns a string value corresponding to this date-time attribute.

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

DateTimeSyntax

​(

Date

value)

Construct a new date-time attribute with the given

java.util.Date

value.

---

#### Constructor Summary

Construct a new date-time attribute with the given

java.util.Date

value.

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

Returns whether this date-time attribute is equivalent to the passed in
object.

Date

getValue

()

Returns this date-time attribute's

java.util.Date

value.

int

hashCode

()

Returns a hash code value for this date-time attribute.

String

toString

()

Returns a string value corresponding to this date-time attribute.

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

Returns whether this date-time attribute is equivalent to the passed in
object.

Returns this date-time attribute's

java.util.Date

value.

Returns a hash code value for this date-time attribute.

Returns a string value corresponding to this date-time attribute.

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

- DateTimeSyntax

```java
protected DateTimeSyntax​(
Date
value)
```

Construct a new date-time attribute with the given

java.util.Date

value.

**Parameters:** value

-

java.util.Date

value
**Throws:** NullPointerException

- if

value

is

null

============ METHOD DETAIL ==========

- Method Detail

- getValue

```java
public
Date
getValue()
```

Returns this date-time attribute's

java.util.Date

value.

**Returns:** the

Date

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

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

is equivalent to this date-time
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

Returns a hash code value for this date-time attribute. The hashcode is
that of this attribute's

java.util.Date

value.

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

Returns a string value corresponding to this date-time attribute. The
string value is just this attribute's

java.util.Date

value
converted to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- DateTimeSyntax

```java
protected DateTimeSyntax​(
Date
value)
```

Construct a new date-time attribute with the given

java.util.Date

value.

**Parameters:** value

-

java.util.Date

value
**Throws:** NullPointerException

- if

value

is

null

---

#### Constructor Detail

DateTimeSyntax

```java
protected DateTimeSyntax​(
Date
value)
```

Construct a new date-time attribute with the given

java.util.Date

value.

**Parameters:** value

-

java.util.Date

value
**Throws:** NullPointerException

- if

value

is

null

---

#### DateTimeSyntax

protected DateTimeSyntax​(

Date

value)

Construct a new date-time attribute with the given

java.util.Date

value.

Method Detail

- getValue

```java
public
Date
getValue()
```

Returns this date-time attribute's

java.util.Date

value.

**Returns:** the

Date

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

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

is equivalent to this date-time
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

Returns a hash code value for this date-time attribute. The hashcode is
that of this attribute's

java.util.Date

value.

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

Returns a string value corresponding to this date-time attribute. The
string value is just this attribute's

java.util.Date

value
converted to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getValue

```java
public
Date
getValue()
```

Returns this date-time attribute's

java.util.Date

value.

**Returns:** the

Date

---

#### getValue

public

Date

getValue()

Returns this date-time attribute's

java.util.Date

value.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

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

is equivalent to this date-time
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

Returns whether this date-time attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

object

is not

null

.

object

is an instance of class

DateTimeSyntax

.

This date-time attribute's

java.util.Date

value and

object

's

java.util.Date

value are equal.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this date-time attribute. The hashcode is
that of this attribute's

java.util.Date

value.

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

Returns a hash code value for this date-time attribute. The hashcode is
that of this attribute's

java.util.Date

value.

toString

```java
public
String
toString()
```

Returns a string value corresponding to this date-time attribute. The
string value is just this attribute's

java.util.Date

value
converted to a string.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string value corresponding to this date-time attribute. The
string value is just this attribute's

java.util.Date

value
converted to a string.

---

