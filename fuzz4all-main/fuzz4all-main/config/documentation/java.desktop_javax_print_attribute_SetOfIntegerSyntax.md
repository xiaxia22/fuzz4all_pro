# Class SetOfIntegerSyntax

**Source:** `java.desktop\javax\print\attribute\SetOfIntegerSyntax.html`

### Class Description

```java
public abstract class
SetOfIntegerSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

SetOfIntegerSyntax

is an abstract base class providing the
common implementation of all attributes whose value is a set of nonnegative
integers. This includes attributes whose value is a single range of integers
and attributes whose value is a set of ranges of integers.

You can construct an instance of

SetOfIntegerSyntax

by giving it in
"string form." The string consists of zero or more comma-separated integer
groups. Each integer group consists of either one integer, two integers
separated by a hyphen (

-

), or two integers separated by a colon
(

:

). Each integer consists of one or more decimal digits (

0

through

9

). Whitespace characters cannot appear within an integer but
are otherwise ignored. For example:

""

,

"1"

,

"5-10"

,

"1:2, 4"

.

You can also construct an instance of

SetOfIntegerSyntax

by giving it
in "array form." Array form consists of an array of zero or more integer
groups where each integer group is a length-1 or length-2 array of

int

s; for example,

int[0][]

,

int[][]{{1}}

,

int[][]{{5,10}}

,

int[][]{{1,2},{4}}

.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

**All Implemented Interfaces:** Serializable

,

Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SetOfIntegerSyntax​(
String
members)

Construct a new set-of-integer attribute with the given members in string
form.

**Parameters:**
- members

- set members in string form. If

null

, an empty set
is constructed.

**Throws:**
- IllegalArgumentException

- if

members

does not obey the
proper syntax

---

#### protected SetOfIntegerSyntax​(int[][] members)

Construct a new set-of-integer attribute with the given members in array
form.

**Parameters:**
- members

- set members in array form. If

null

, an empty set
is constructed.

**Throws:**
- NullPointerException

- if any element of

members

is

null
- IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array or if any

non-null

range
in

members

has a lower bound less than zero

---

#### protected SetOfIntegerSyntax​(int member)

Construct a new set-of-integer attribute containing a single integer.

**Parameters:**
- member

- set member

**Throws:**
- IllegalArgumentException

- if

member

is negative

---

#### protected SetOfIntegerSyntax​(int lowerBound,
int upperBound)

Construct a new set-of-integer attribute containing a single range of
integers. If the lower bound is greater than the upper bound (a null
range), an empty set is constructed.

**Parameters:**
- lowerBound

- Lower bound of the range
- upperBound

- Upper bound of the range

**Throws:**
- IllegalArgumentException

- if the range is

non-null

and

lowerBound

is less than zero

---

### Method Details

#### public int[][] getMembers()

Obtain this set-of-integer attribute's members in canonical array form.
The returned array is "safe;" the client may alter it without affecting
this set-of-integer attribute.

**Returns:**
- this set-of-integer attribute's members in canonical array form

---

#### public boolean contains​(int x)

Determine if this set-of-integer attribute contains the given value.

**Parameters:**
- x

- the Integer value

**Returns:**
- true

if this set-of-integer attribute contains the value

x

,

false

otherwise

---

#### public boolean contains​(
IntegerSyntax
attribute)

Determine if this set-of-integer attribute contains the given integer
attribute's value.

**Parameters:**
- attribute

- the Integer attribute

**Returns:**
- true

if this set-of-integer attribute contains

attribute

's value,

false

otherwise

---

#### public int next​(int x)

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value. If there are no integers in this
set-of-integer attribute greater than the given value,

-1

is
returned. (Since a set-of-integer attribute can only contain nonnegative
values,

-1

will never appear in the set.) You can use the

next()

method to iterate through the integer values in a
set-of-integer attribute in ascending order, like this:

```java
SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}
```

**Parameters:**
- x

- the Integer value

**Returns:**
- the smallest integer in this set-of-integer attribute that is
greater than

x

, or

-1

if no integer in this
set-of-integer attribute is greater than

x

.

---

#### public boolean equals​(
Object
object)

Returns whether this set-of-integer attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

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

is equivalent to this
set-of-integer attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this set-of-integer attribute. The hash
code is the sum of the lower and upper bounds of the ranges in the
canonical array form, or 0 for an empty set.

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

Returns a string value corresponding to this set-of-integer attribute.
The string value is a zero-length string if this set is empty. Otherwise,
the string value is a comma-separated list of the ranges in the canonical
array form, where each range is represented as

"

i

"

if
the lower bound equals the upper bound or

"

i

-

j

"

otherwise.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

### Additional Sections

#### Class SetOfIntegerSyntax

java.lang.Object

- javax.print.attribute.SetOfIntegerSyntax

javax.print.attribute.SetOfIntegerSyntax

**All Implemented Interfaces:** Serializable

,

Cloneable

**Direct Known Subclasses:** CopiesSupported

,

JobImpressionsSupported

,

JobKOctetsSupported

,

JobMediaSheetsSupported

,

NumberUpSupported

,

PageRanges

```java
public abstract class
SetOfIntegerSyntax

extends
Object

implements
Serializable
,
Cloneable
```

Class

SetOfIntegerSyntax

is an abstract base class providing the
common implementation of all attributes whose value is a set of nonnegative
integers. This includes attributes whose value is a single range of integers
and attributes whose value is a set of ranges of integers.

You can construct an instance of

SetOfIntegerSyntax

by giving it in
"string form." The string consists of zero or more comma-separated integer
groups. Each integer group consists of either one integer, two integers
separated by a hyphen (

-

), or two integers separated by a colon
(

:

). Each integer consists of one or more decimal digits (

0

through

9

). Whitespace characters cannot appear within an integer but
are otherwise ignored. For example:

""

,

"1"

,

"5-10"

,

"1:2, 4"

.

You can also construct an instance of

SetOfIntegerSyntax

by giving it
in "array form." Array form consists of an array of zero or more integer
groups where each integer group is a length-1 or length-2 array of

int

s; for example,

int[0][]

,

int[][]{{1}}

,

int[][]{{5,10}}

,

int[][]{{1,2},{4}}

.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

**See Also:** Serialized Form

public abstract class

SetOfIntegerSyntax

extends

Object

implements

Serializable

,

Cloneable

Class

SetOfIntegerSyntax

is an abstract base class providing the
common implementation of all attributes whose value is a set of nonnegative
integers. This includes attributes whose value is a single range of integers
and attributes whose value is a set of ranges of integers.

You can construct an instance of

SetOfIntegerSyntax

by giving it in
"string form." The string consists of zero or more comma-separated integer
groups. Each integer group consists of either one integer, two integers
separated by a hyphen (

-

), or two integers separated by a colon
(

:

). Each integer consists of one or more decimal digits (

0

through

9

). Whitespace characters cannot appear within an integer but
are otherwise ignored. For example:

""

,

"1"

,

"5-10"

,

"1:2, 4"

.

You can also construct an instance of

SetOfIntegerSyntax

by giving it
in "array form." Array form consists of an array of zero or more integer
groups where each integer group is a length-1 or length-2 array of

int

s; for example,

int[0][]

,

int[][]{{1}}

,

int[][]{{5,10}}

,

int[][]{{1,2},{4}}

.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

You can construct an instance of

SetOfIntegerSyntax

by giving it in
"string form." The string consists of zero or more comma-separated integer
groups. Each integer group consists of either one integer, two integers
separated by a hyphen (

-

), or two integers separated by a colon
(

:

). Each integer consists of one or more decimal digits (

0

through

9

). Whitespace characters cannot appear within an integer but
are otherwise ignored. For example:

""

,

"1"

,

"5-10"

,

"1:2, 4"

.

You can also construct an instance of

SetOfIntegerSyntax

by giving it
in "array form." Array form consists of an array of zero or more integer
groups where each integer group is a length-1 or length-2 array of

int

s; for example,

int[0][]

,

int[][]{{1}}

,

int[][]{{5,10}}

,

int[][]{{1,2},{4}}

.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

You can also construct an instance of

SetOfIntegerSyntax

by giving it
in "array form." Array form consists of an array of zero or more integer
groups where each integer group is a length-1 or length-2 array of

int

s; for example,

int[0][]

,

int[][]{{1}}

,

int[][]{{5,10}}

,

int[][]{{1,2},{4}}

.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

In both string form and array form, each successive integer group gives a
range of integers to be included in the set. The first integer in each group
gives the lower bound of the range; the second integer in each group gives
the upper bound of the range; if there is only one integer in the group, the
upper bound is the same as the lower bound. If the upper bound is less than
the lower bound, it denotes a

null

range (no values). If the upper
bound is equal to the lower bound, it denotes a range consisting of a single
value. If the upper bound is greater than the lower bound, it denotes a range
consisting of more than one value. The ranges may appear in any order and are
allowed to overlap. The union of all the ranges gives the set's contents.
Once a

SetOfIntegerSyntax

instance is constructed, its value is
immutable.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

The

SetOfIntegerSyntax

object's value is actually stored in
"

canonical

array form." This is the same as array form, except there
are no

null

ranges; the members of the set are represented in as few
ranges as possible (i.e., overlapping ranges are coalesced); the ranges
appear in ascending order; and each range is always represented as a
length-two array of

int

s in the form {lower bound, upper bound}. An
empty set is represented as a zero-length array.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

Class

SetOfIntegerSyntax

has operations to return the set's members
in canonical array form, to test whether a given integer is a member of the
set, and to iterate through the members of the set.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SetOfIntegerSyntax

​(int member)

Construct a new set-of-integer attribute containing a single integer.

protected

SetOfIntegerSyntax

​(int[][] members)

Construct a new set-of-integer attribute with the given members in array
form.

protected

SetOfIntegerSyntax

​(int lowerBound,
int upperBound)

Construct a new set-of-integer attribute containing a single range of
integers.

protected

SetOfIntegerSyntax

​(

String

members)

Construct a new set-of-integer attribute with the given members in string
form.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(int x)

Determine if this set-of-integer attribute contains the given value.

boolean

contains

​(

IntegerSyntax

attribute)

Determine if this set-of-integer attribute contains the given integer
attribute's value.

boolean

equals

​(

Object

object)

Returns whether this set-of-integer attribute is equivalent to the passed
in object.

int[][]

getMembers

()

Obtain this set-of-integer attribute's members in canonical array form.

int

hashCode

()

Returns a hash code value for this set-of-integer attribute.

int

next

​(int x)

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value.

String

toString

()

Returns a string value corresponding to this set-of-integer attribute.

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

SetOfIntegerSyntax

​(int member)

Construct a new set-of-integer attribute containing a single integer.

protected

SetOfIntegerSyntax

​(int[][] members)

Construct a new set-of-integer attribute with the given members in array
form.

protected

SetOfIntegerSyntax

​(int lowerBound,
int upperBound)

Construct a new set-of-integer attribute containing a single range of
integers.

protected

SetOfIntegerSyntax

​(

String

members)

Construct a new set-of-integer attribute with the given members in string
form.

---

#### Constructor Summary

Construct a new set-of-integer attribute containing a single integer.

Construct a new set-of-integer attribute with the given members in array
form.

Construct a new set-of-integer attribute containing a single range of
integers.

Construct a new set-of-integer attribute with the given members in string
form.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

contains

​(int x)

Determine if this set-of-integer attribute contains the given value.

boolean

contains

​(

IntegerSyntax

attribute)

Determine if this set-of-integer attribute contains the given integer
attribute's value.

boolean

equals

​(

Object

object)

Returns whether this set-of-integer attribute is equivalent to the passed
in object.

int[][]

getMembers

()

Obtain this set-of-integer attribute's members in canonical array form.

int

hashCode

()

Returns a hash code value for this set-of-integer attribute.

int

next

​(int x)

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value.

String

toString

()

Returns a string value corresponding to this set-of-integer attribute.

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

Determine if this set-of-integer attribute contains the given value.

Determine if this set-of-integer attribute contains the given integer
attribute's value.

Returns whether this set-of-integer attribute is equivalent to the passed
in object.

Obtain this set-of-integer attribute's members in canonical array form.

Returns a hash code value for this set-of-integer attribute.

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value.

Returns a string value corresponding to this set-of-integer attribute.

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

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(
String
members)
```

Construct a new set-of-integer attribute with the given members in string
form.

**Parameters:** members

- set members in string form. If

null

, an empty set
is constructed.
**Throws:** IllegalArgumentException

- if

members

does not obey the
proper syntax

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int[][] members)
```

Construct a new set-of-integer attribute with the given members in array
form.

**Parameters:** members

- set members in array form. If

null

, an empty set
is constructed.
**Throws:** NullPointerException

- if any element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array or if any

non-null

range
in

members

has a lower bound less than zero

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int member)
```

Construct a new set-of-integer attribute containing a single integer.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member

is negative

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int lowerBound,
int upperBound)
```

Construct a new set-of-integer attribute containing a single range of
integers. If the lower bound is greater than the upper bound (a null
range), an empty set is constructed.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if the range is

non-null

and

lowerBound

is less than zero

============ METHOD DETAIL ==========

- Method Detail

- getMembers

```java
public int[][] getMembers()
```

Obtain this set-of-integer attribute's members in canonical array form.
The returned array is "safe;" the client may alter it without affecting
this set-of-integer attribute.

**Returns:** this set-of-integer attribute's members in canonical array form

- contains

```java
public boolean contains​(int x)
```

Determine if this set-of-integer attribute contains the given value.

**Parameters:** x

- the Integer value
**Returns:** true

if this set-of-integer attribute contains the value

x

,

false

otherwise

- contains

```java
public boolean contains​(
IntegerSyntax
attribute)
```

Determine if this set-of-integer attribute contains the given integer
attribute's value.

**Parameters:** attribute

- the Integer attribute
**Returns:** true

if this set-of-integer attribute contains

attribute

's value,

false

otherwise

- next

```java
public int next​(int x)
```

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value. If there are no integers in this
set-of-integer attribute greater than the given value,

-1

is
returned. (Since a set-of-integer attribute can only contain nonnegative
values,

-1

will never appear in the set.) You can use the

next()

method to iterate through the integer values in a
set-of-integer attribute in ascending order, like this:

```java
SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}
```

**Parameters:** x

- the Integer value
**Returns:** the smallest integer in this set-of-integer attribute that is
greater than

x

, or

-1

if no integer in this
set-of-integer attribute is greater than

x

.

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this set-of-integer attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

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

is equivalent to this
set-of-integer attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this set-of-integer attribute. The hash
code is the sum of the lower and upper bounds of the ranges in the
canonical array form, or 0 for an empty set.

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

Returns a string value corresponding to this set-of-integer attribute.
The string value is a zero-length string if this set is empty. Otherwise,
the string value is a comma-separated list of the ranges in the canonical
array form, where each range is represented as

"

i

"

if
the lower bound equals the upper bound or

"

i

-

j

"

otherwise.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

Constructor Detail

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(
String
members)
```

Construct a new set-of-integer attribute with the given members in string
form.

**Parameters:** members

- set members in string form. If

null

, an empty set
is constructed.
**Throws:** IllegalArgumentException

- if

members

does not obey the
proper syntax

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int[][] members)
```

Construct a new set-of-integer attribute with the given members in array
form.

**Parameters:** members

- set members in array form. If

null

, an empty set
is constructed.
**Throws:** NullPointerException

- if any element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array or if any

non-null

range
in

members

has a lower bound less than zero

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int member)
```

Construct a new set-of-integer attribute containing a single integer.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member

is negative

- SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int lowerBound,
int upperBound)
```

Construct a new set-of-integer attribute containing a single range of
integers. If the lower bound is greater than the upper bound (a null
range), an empty set is constructed.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if the range is

non-null

and

lowerBound

is less than zero

---

#### Constructor Detail

SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(
String
members)
```

Construct a new set-of-integer attribute with the given members in string
form.

**Parameters:** members

- set members in string form. If

null

, an empty set
is constructed.
**Throws:** IllegalArgumentException

- if

members

does not obey the
proper syntax

---

#### SetOfIntegerSyntax

protected SetOfIntegerSyntax​(

String

members)

Construct a new set-of-integer attribute with the given members in string
form.

SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int[][] members)
```

Construct a new set-of-integer attribute with the given members in array
form.

**Parameters:** members

- set members in array form. If

null

, an empty set
is constructed.
**Throws:** NullPointerException

- if any element of

members

is

null
**Throws:** IllegalArgumentException

- if any element of

members

is not
a length-one or length-two array or if any

non-null

range
in

members

has a lower bound less than zero

---

#### SetOfIntegerSyntax

protected SetOfIntegerSyntax​(int[][] members)

Construct a new set-of-integer attribute with the given members in array
form.

SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int member)
```

Construct a new set-of-integer attribute containing a single integer.

**Parameters:** member

- set member
**Throws:** IllegalArgumentException

- if

member

is negative

---

#### SetOfIntegerSyntax

protected SetOfIntegerSyntax​(int member)

Construct a new set-of-integer attribute containing a single integer.

SetOfIntegerSyntax

```java
protected SetOfIntegerSyntax​(int lowerBound,
int upperBound)
```

Construct a new set-of-integer attribute containing a single range of
integers. If the lower bound is greater than the upper bound (a null
range), an empty set is constructed.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if the range is

non-null

and

lowerBound

is less than zero

---

#### SetOfIntegerSyntax

protected SetOfIntegerSyntax​(int lowerBound,
int upperBound)

Construct a new set-of-integer attribute containing a single range of
integers. If the lower bound is greater than the upper bound (a null
range), an empty set is constructed.

Method Detail

- getMembers

```java
public int[][] getMembers()
```

Obtain this set-of-integer attribute's members in canonical array form.
The returned array is "safe;" the client may alter it without affecting
this set-of-integer attribute.

**Returns:** this set-of-integer attribute's members in canonical array form

- contains

```java
public boolean contains​(int x)
```

Determine if this set-of-integer attribute contains the given value.

**Parameters:** x

- the Integer value
**Returns:** true

if this set-of-integer attribute contains the value

x

,

false

otherwise

- contains

```java
public boolean contains​(
IntegerSyntax
attribute)
```

Determine if this set-of-integer attribute contains the given integer
attribute's value.

**Parameters:** attribute

- the Integer attribute
**Returns:** true

if this set-of-integer attribute contains

attribute

's value,

false

otherwise

- next

```java
public int next​(int x)
```

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value. If there are no integers in this
set-of-integer attribute greater than the given value,

-1

is
returned. (Since a set-of-integer attribute can only contain nonnegative
values,

-1

will never appear in the set.) You can use the

next()

method to iterate through the integer values in a
set-of-integer attribute in ascending order, like this:

```java
SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}
```

**Parameters:** x

- the Integer value
**Returns:** the smallest integer in this set-of-integer attribute that is
greater than

x

, or

-1

if no integer in this
set-of-integer attribute is greater than

x

.

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this set-of-integer attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

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

is equivalent to this
set-of-integer attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this set-of-integer attribute. The hash
code is the sum of the lower and upper bounds of the ranges in the
canonical array form, or 0 for an empty set.

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

Returns a string value corresponding to this set-of-integer attribute.
The string value is a zero-length string if this set is empty. Otherwise,
the string value is a comma-separated list of the ranges in the canonical
array form, where each range is represented as

"

i

"

if
the lower bound equals the upper bound or

"

i

-

j

"

otherwise.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### Method Detail

getMembers

```java
public int[][] getMembers()
```

Obtain this set-of-integer attribute's members in canonical array form.
The returned array is "safe;" the client may alter it without affecting
this set-of-integer attribute.

**Returns:** this set-of-integer attribute's members in canonical array form

---

#### getMembers

public int[][] getMembers()

Obtain this set-of-integer attribute's members in canonical array form.
The returned array is "safe;" the client may alter it without affecting
this set-of-integer attribute.

contains

```java
public boolean contains​(int x)
```

Determine if this set-of-integer attribute contains the given value.

**Parameters:** x

- the Integer value
**Returns:** true

if this set-of-integer attribute contains the value

x

,

false

otherwise

---

#### contains

public boolean contains​(int x)

Determine if this set-of-integer attribute contains the given value.

contains

```java
public boolean contains​(
IntegerSyntax
attribute)
```

Determine if this set-of-integer attribute contains the given integer
attribute's value.

**Parameters:** attribute

- the Integer attribute
**Returns:** true

if this set-of-integer attribute contains

attribute

's value,

false

otherwise

---

#### contains

public boolean contains​(

IntegerSyntax

attribute)

Determine if this set-of-integer attribute contains the given integer
attribute's value.

next

```java
public int next​(int x)
```

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value. If there are no integers in this
set-of-integer attribute greater than the given value,

-1

is
returned. (Since a set-of-integer attribute can only contain nonnegative
values,

-1

will never appear in the set.) You can use the

next()

method to iterate through the integer values in a
set-of-integer attribute in ascending order, like this:

```java
SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}
```

**Parameters:** x

- the Integer value
**Returns:** the smallest integer in this set-of-integer attribute that is
greater than

x

, or

-1

if no integer in this
set-of-integer attribute is greater than

x

.

---

#### next

public int next​(int x)

Determine the smallest integer in this set-of-integer attribute that is
greater than the given value. If there are no integers in this
set-of-integer attribute greater than the given value,

-1

is
returned. (Since a set-of-integer attribute can only contain nonnegative
values,

-1

will never appear in the set.) You can use the

next()

method to iterate through the integer values in a
set-of-integer attribute in ascending order, like this:

```java
SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}
```

SetOfIntegerSyntax attribute = . . .;
int i = -1;
while ((i = attribute.next (i)) != -1)
{
foo (i);
}

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this set-of-integer attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

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

is equivalent to this
set-of-integer attribute,

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

Returns whether this set-of-integer attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

object

is not

null

.

object

is an instance of class

SetOfIntegerSyntax

.

This set-of-integer attribute's members and

object

's
members are the same.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this set-of-integer attribute. The hash
code is the sum of the lower and upper bounds of the ranges in the
canonical array form, or 0 for an empty set.

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

Returns a hash code value for this set-of-integer attribute. The hash
code is the sum of the lower and upper bounds of the ranges in the
canonical array form, or 0 for an empty set.

toString

```java
public
String
toString()
```

Returns a string value corresponding to this set-of-integer attribute.
The string value is a zero-length string if this set is empty. Otherwise,
the string value is a comma-separated list of the ranges in the canonical
array form, where each range is represented as

"

i

"

if
the lower bound equals the upper bound or

"

i

-

j

"

otherwise.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string value corresponding to this set-of-integer attribute.
The string value is a zero-length string if this set is empty. Otherwise,
the string value is a comma-separated list of the ranges in the canonical
array form, where each range is represented as

"

i

"

if
the lower bound equals the upper bound or

"

i

-

j

"

otherwise.

---

