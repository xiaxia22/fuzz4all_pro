# Class NumberUpSupported

**Source:** `java.desktop\javax\print\attribute\standard\NumberUpSupported.html`

### Class Description

```java
public final class
NumberUpSupported

extends
SetOfIntegerSyntax

implements
SupportedValuesAttribute
```

Class

NumberUpSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

NumberUp

attribute.

IPP Compatibility:

The NumberUpSupported attribute's canonical array
form gives the lower and upper bound for each range of number-up to be
included in an IPP "number-up-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

SupportedValuesAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public NumberUpSupported​(int[][] members)

Construct a new number up supported attribute with the given members. The
supported values for NumberUp are specified in "array form;" see class

SetOfIntegerSyntax

for
an explanation of array form.

**Parameters:**
- members

- set members in array form

**Throws:**
- NullPointerException

- if

members

is

null

or any
element of

members

is

null
- IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array. Also if

members

is a
zero-length array or if any member of the set is less than 1.

---

#### public NumberUpSupported​(int member)

Construct a new number up supported attribute containing a single
integer. That is, only the one value of

NumberUp

is supported.

**Parameters:**
- member

- set member

**Throws:**
- IllegalArgumentException

- if

member < 1

---

#### public NumberUpSupported​(int lowerBound,
int upperBound)

Construct a new number up supported attribute containing a single range
of integers. That is, only those values of

NumberUp

in the one
range are supported.

**Parameters:**
- lowerBound

- lower bound of the range
- upperBound

- upper bound of the range

**Throws:**
- IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than 1

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this number up supported attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

**Overrides:**
- equals

in class

SetOfIntegerSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this number up
supported attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class NumberUpSupported

java.lang.Object

- javax.print.attribute.SetOfIntegerSyntax
- - javax.print.attribute.standard.NumberUpSupported

javax.print.attribute.SetOfIntegerSyntax

- javax.print.attribute.standard.NumberUpSupported

javax.print.attribute.standard.NumberUpSupported

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

SupportedValuesAttribute

```java
public final class
NumberUpSupported

extends
SetOfIntegerSyntax

implements
SupportedValuesAttribute
```

Class

NumberUpSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

NumberUp

attribute.

IPP Compatibility:

The NumberUpSupported attribute's canonical array
form gives the lower and upper bound for each range of number-up to be
included in an IPP "number-up-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

**See Also:** Serialized Form

public final class

NumberUpSupported

extends

SetOfIntegerSyntax

implements

SupportedValuesAttribute

Class

NumberUpSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

NumberUp

attribute.

IPP Compatibility:

The NumberUpSupported attribute's canonical array
form gives the lower and upper bound for each range of number-up to be
included in an IPP "number-up-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

IPP Compatibility:

The NumberUpSupported attribute's canonical array
form gives the lower and upper bound for each range of number-up to be
included in an IPP "number-up-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NumberUpSupported

​(int member)

Construct a new number up supported attribute containing a single
integer.

NumberUpSupported

​(int[][] members)

Construct a new number up supported attribute with the given members.

NumberUpSupported

​(int lowerBound,
int upperBound)

Construct a new number up supported attribute containing a single range
of integers.

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

Returns whether this number up supported attribute is equivalent to the
passed in object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

,

toString

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

Constructor

Description

NumberUpSupported

​(int member)

Construct a new number up supported attribute containing a single
integer.

NumberUpSupported

​(int[][] members)

Construct a new number up supported attribute with the given members.

NumberUpSupported

​(int lowerBound,
int upperBound)

Construct a new number up supported attribute containing a single range
of integers.

---

#### Constructor Summary

Construct a new number up supported attribute containing a single
integer.

Construct a new number up supported attribute with the given members.

Construct a new number up supported attribute containing a single range
of integers.

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

Returns whether this number up supported attribute is equivalent to the
passed in object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

,

toString

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

Returns whether this number up supported attribute is equivalent to the
passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

,

toString

---

#### Methods declared in class javax.print.attribute. SetOfIntegerSyntax

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

- NumberUpSupported

```java
public NumberUpSupported​(int[][] members)
```

Construct a new number up supported attribute with the given members. The
supported values for NumberUp are specified in "array form;" see class

SetOfIntegerSyntax

for
an explanation of array form.

**Parameters:** members

- set members in array form
**Throws:** NullPointerException

- if

members

is

null

or any
element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array. Also if

members

is a
zero-length array or if any member of the set is less than 1.

- NumberUpSupported

```java
public NumberUpSupported​(int member)
```

Construct a new number up supported attribute containing a single
integer. That is, only the one value of

NumberUp

is supported.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member < 1

- NumberUpSupported

```java
public NumberUpSupported​(int lowerBound,
int upperBound)
```

Construct a new number up supported attribute containing a single range
of integers. That is, only those values of

NumberUp

in the one
range are supported.

**Parameters:** lowerBound

- lower bound of the range
**Parameters:** upperBound

- upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than 1

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this number up supported attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number up
supported attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- NumberUpSupported

```java
public NumberUpSupported​(int[][] members)
```

Construct a new number up supported attribute with the given members. The
supported values for NumberUp are specified in "array form;" see class

SetOfIntegerSyntax

for
an explanation of array form.

**Parameters:** members

- set members in array form
**Throws:** NullPointerException

- if

members

is

null

or any
element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array. Also if

members

is a
zero-length array or if any member of the set is less than 1.

- NumberUpSupported

```java
public NumberUpSupported​(int member)
```

Construct a new number up supported attribute containing a single
integer. That is, only the one value of

NumberUp

is supported.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member < 1

- NumberUpSupported

```java
public NumberUpSupported​(int lowerBound,
int upperBound)
```

Construct a new number up supported attribute containing a single range
of integers. That is, only those values of

NumberUp

in the one
range are supported.

**Parameters:** lowerBound

- lower bound of the range
**Parameters:** upperBound

- upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than 1

---

#### Constructor Detail

NumberUpSupported

```java
public NumberUpSupported​(int[][] members)
```

Construct a new number up supported attribute with the given members. The
supported values for NumberUp are specified in "array form;" see class

SetOfIntegerSyntax

for
an explanation of array form.

**Parameters:** members

- set members in array form
**Throws:** NullPointerException

- if

members

is

null

or any
element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array. Also if

members

is a
zero-length array or if any member of the set is less than 1.

---

#### NumberUpSupported

public NumberUpSupported​(int[][] members)

Construct a new number up supported attribute with the given members. The
supported values for NumberUp are specified in "array form;" see class

SetOfIntegerSyntax

for
an explanation of array form.

NumberUpSupported

```java
public NumberUpSupported​(int member)
```

Construct a new number up supported attribute containing a single
integer. That is, only the one value of

NumberUp

is supported.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member < 1

---

#### NumberUpSupported

public NumberUpSupported​(int member)

Construct a new number up supported attribute containing a single
integer. That is, only the one value of

NumberUp

is supported.

NumberUpSupported

```java
public NumberUpSupported​(int lowerBound,
int upperBound)
```

Construct a new number up supported attribute containing a single range
of integers. That is, only those values of

NumberUp

in the one
range are supported.

**Parameters:** lowerBound

- lower bound of the range
**Parameters:** upperBound

- upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than 1

---

#### NumberUpSupported

public NumberUpSupported​(int lowerBound,
int upperBound)

Construct a new number up supported attribute containing a single range
of integers. That is, only those values of

NumberUp

in the one
range are supported.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this number up supported attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number up
supported attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this number up supported attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number up
supported attribute,

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

Returns whether this number up supported attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

object

is not

null

.

object

is an instance of class

NumberUpSupported

.

This number up supported attribute's members and

object

's
members are the same.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

For class

NumberUpSupported

, the category is class

NumberUpSupported

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

For class

NumberUpSupported

, the category name is

"number-up-supported"

.

---

