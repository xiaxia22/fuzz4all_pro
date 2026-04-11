# Class NumberOfInterveningJobs

**Source:** `java.desktop\javax\print\attribute\standard\NumberOfInterveningJobs.html`

### Class Description

```java
public final class
NumberOfInterveningJobs

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

NumberOfInterveningJobs

is an integer valued printing attribute
that indicates the number of jobs that are ahead of this job in the relative
chronological order of expected time to complete (i.e., the current scheduled
order).

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public NumberOfInterveningJobs​(int value)

Construct a new number of intervening jobs attribute with the given
integer value.

**Parameters:**
- value

- Integer value

**Throws:**
- IllegalArgumentException

- if

value

is negative

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object. To be equivalent, all of the following
conditions must be true:

- object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

**Overrides:**
- equals

in class

IntegerSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this number of
intervening jobs attribute,

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

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

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

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class NumberOfInterveningJobs

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.NumberOfInterveningJobs

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.NumberOfInterveningJobs

javax.print.attribute.standard.NumberOfInterveningJobs

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
NumberOfInterveningJobs

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

NumberOfInterveningJobs

is an integer valued printing attribute
that indicates the number of jobs that are ahead of this job in the relative
chronological order of expected time to complete (i.e., the current scheduled
order).

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

NumberOfInterveningJobs

extends

IntegerSyntax

implements

PrintJobAttribute

Class

NumberOfInterveningJobs

is an integer valued printing attribute
that indicates the number of jobs that are ahead of this job in the relative
chronological order of expected time to complete (i.e., the current scheduled
order).

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NumberOfInterveningJobs

​(int value)

Construct a new number of intervening jobs attribute with the given
integer value.

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

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object.

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

IntegerSyntax

getValue

,

hashCode

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

NumberOfInterveningJobs

​(int value)

Construct a new number of intervening jobs attribute with the given
integer value.

---

#### Constructor Summary

Construct a new number of intervening jobs attribute with the given
integer value.

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

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object.

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

IntegerSyntax

getValue

,

hashCode

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

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

IntegerSyntax

getValue

,

hashCode

,

toString

---

#### Methods declared in class javax.print.attribute. IntegerSyntax

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

- NumberOfInterveningJobs

```java
public NumberOfInterveningJobs​(int value)
```

Construct a new number of intervening jobs attribute with the given
integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object. To be equivalent, all of the following
conditions must be true:

- object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

**Overrides:** equals

in class

IntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number of
intervening jobs attribute,

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

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

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

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- NumberOfInterveningJobs

```java
public NumberOfInterveningJobs​(int value)
```

Construct a new number of intervening jobs attribute with the given
integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

NumberOfInterveningJobs

```java
public NumberOfInterveningJobs​(int value)
```

Construct a new number of intervening jobs attribute with the given
integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### NumberOfInterveningJobs

public NumberOfInterveningJobs​(int value)

Construct a new number of intervening jobs attribute with the given
integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object. To be equivalent, all of the following
conditions must be true:

- object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

**Overrides:** equals

in class

IntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number of
intervening jobs attribute,

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

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

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

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

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

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object. To be equivalent, all of the following
conditions must be true:

- object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

**Overrides:** equals

in class

IntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this number of
intervening jobs attribute,

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

Returns whether this number of intervening jobs attribute is equivalent
to the passed in object. To be equivalent, all of the following
conditions must be true:

- object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

object

is not

null

.

object

is an instance of class

NumberOfInterveningJobs

.

This number of intervening jobs attribute's value and

object

's value are equal.

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

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

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

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

itself.

For class

NumberOfInterveningJobs

, the category is class

NumberOfInterveningJobs

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

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

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

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

.

For class

NumberOfInterveningJobs

, the category name is

"number-of-intervening-jobs"

.

---

