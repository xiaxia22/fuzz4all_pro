# Class DateTimeAtProcessing

**Source:** `java.desktop\javax\print\attribute\standard\DateTimeAtProcessing.html`

### Class Description

```java
public final class
DateTimeAtProcessing

extends
DateTimeSyntax

implements
PrintJobAttribute
```

Class

DateTimeAtProcessing

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job first
began processing.

To construct a

DateTimeAtProcessing

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtProcessing
attribute. To convert a

DateTimeAtProcessing

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtProcessing

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-processing" attribute can be obtained as described above. The
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

#### public DateTimeAtProcessing​(
Date
dateTime)

Construct a new date-time at processing attribute with the given

Date

value.

**Parameters:**
- dateTime

-

Date

value

**Throws:**
- NullPointerException

- if

dateTime

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this date-time at processing attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

**Overrides:**
- equals

in class

DateTimeSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this date-time at
processing attribute,

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

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

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

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class DateTimeAtProcessing

java.lang.Object

- javax.print.attribute.DateTimeSyntax
- - javax.print.attribute.standard.DateTimeAtProcessing

javax.print.attribute.DateTimeSyntax

- javax.print.attribute.standard.DateTimeAtProcessing

javax.print.attribute.standard.DateTimeAtProcessing

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
DateTimeAtProcessing

extends
DateTimeSyntax

implements
PrintJobAttribute
```

Class

DateTimeAtProcessing

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job first
began processing.

To construct a

DateTimeAtProcessing

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtProcessing
attribute. To convert a

DateTimeAtProcessing

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtProcessing

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-processing" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

DateTimeAtProcessing

extends

DateTimeSyntax

implements

PrintJobAttribute

Class

DateTimeAtProcessing

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job first
began processing.

To construct a

DateTimeAtProcessing

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtProcessing
attribute. To convert a

DateTimeAtProcessing

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtProcessing

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-processing" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

To construct a

DateTimeAtProcessing

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtProcessing
attribute. To convert a

DateTimeAtProcessing

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtProcessing

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-processing" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-processing" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DateTimeAtProcessing

​(

Date

dateTime)

Construct a new date-time at processing attribute with the given

Date

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

Returns whether this date-time at processing attribute is equivalent to
the passed in object.

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

DateTimeSyntax

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

DateTimeAtProcessing

​(

Date

dateTime)

Construct a new date-time at processing attribute with the given

Date

value.

---

#### Constructor Summary

Construct a new date-time at processing attribute with the given

Date

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

Returns whether this date-time at processing attribute is equivalent to
the passed in object.

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

DateTimeSyntax

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

Returns whether this date-time at processing attribute is equivalent to
the passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

DateTimeSyntax

getValue

,

hashCode

,

toString

---

#### Methods declared in class javax.print.attribute. DateTimeSyntax

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

- DateTimeAtProcessing

```java
public DateTimeAtProcessing​(
Date
dateTime)
```

Construct a new date-time at processing attribute with the given

Date

value.

**Parameters:** dateTime

-

Date

value
**Throws:** NullPointerException

- if

dateTime

is

null

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time at processing attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

**Overrides:** equals

in class

DateTimeSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this date-time at
processing attribute,

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

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

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

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- DateTimeAtProcessing

```java
public DateTimeAtProcessing​(
Date
dateTime)
```

Construct a new date-time at processing attribute with the given

Date

value.

**Parameters:** dateTime

-

Date

value
**Throws:** NullPointerException

- if

dateTime

is

null

---

#### Constructor Detail

DateTimeAtProcessing

```java
public DateTimeAtProcessing​(
Date
dateTime)
```

Construct a new date-time at processing attribute with the given

Date

value.

**Parameters:** dateTime

-

Date

value
**Throws:** NullPointerException

- if

dateTime

is

null

---

#### DateTimeAtProcessing

public DateTimeAtProcessing​(

Date

dateTime)

Construct a new date-time at processing attribute with the given

Date

value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time at processing attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

**Overrides:** equals

in class

DateTimeSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this date-time at
processing attribute,

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

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

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

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

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

Returns whether this date-time at processing attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

**Overrides:** equals

in class

DateTimeSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this date-time at
processing attribute,

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

Returns whether this date-time at processing attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

object

is not

null

.

object

is an instance of class

DateTimeAtProcessing

.

This date-time at processing attribute's

Date

value and

object

's

Date

value are equal.

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

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

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

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

itself.

For class

DateTimeAtProcessing

, the category is class

DateTimeAtProcessing

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

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

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

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

.

For class

DateTimeAtProcessing

, the category name is

"date-time-at-processing"

.

---

