# Class DateTimeAtCompleted

**Source:** `java.desktop\javax\print\attribute\standard\DateTimeAtCompleted.html`

### Class Description

```java
public final class
DateTimeAtCompleted

extends
DateTimeSyntax

implements
PrintJobAttribute
```

Class

DateTimeAtCompleted

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job completed
(or was canceled or aborted).

To construct a

DateTimeAtCompleted

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtCompleted
attribute. To convert a

DateTimeAtCompleted

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtCompleted

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-completed" attribute can be obtained as described above. The
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

#### public DateTimeAtCompleted​(
Date
dateTime)

Construct a new date-time at completed attribute with the given

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

Returns whether this date-time at completed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtCompleted

.

This date-time at completed attribute's

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
completed attribute,

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

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

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

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class DateTimeAtCompleted

java.lang.Object

- javax.print.attribute.DateTimeSyntax
- - javax.print.attribute.standard.DateTimeAtCompleted

javax.print.attribute.DateTimeSyntax

- javax.print.attribute.standard.DateTimeAtCompleted

javax.print.attribute.standard.DateTimeAtCompleted

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
DateTimeAtCompleted

extends
DateTimeSyntax

implements
PrintJobAttribute
```

Class

DateTimeAtCompleted

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job completed
(or was canceled or aborted).

To construct a

DateTimeAtCompleted

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtCompleted
attribute. To convert a

DateTimeAtCompleted

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtCompleted

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-completed" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

DateTimeAtCompleted

extends

DateTimeSyntax

implements

PrintJobAttribute

Class

DateTimeAtCompleted

is a printing attribute class, a date-time
attribute, that indicates the date and time at which the Print Job completed
(or was canceled or aborted).

To construct a

DateTimeAtCompleted

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtCompleted
attribute. To convert a

DateTimeAtCompleted

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtCompleted

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-completed" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

To construct a

DateTimeAtCompleted

attribute from separate values of
the year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object,
then use the

Date

object to construct the DateTimeAtCompleted
attribute. To convert a

DateTimeAtCompleted

attribute to separate
values of the year, month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

DateTimeAtCompleted

attribute.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-completed" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The information needed to construct an IPP
"date-time-at-completed" attribute can be obtained as described above. The
category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DateTimeAtCompleted

​(

Date

dateTime)

Construct a new date-time at completed attribute with the given

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

Returns whether this date-time at completed attribute is equivalent to
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

DateTimeAtCompleted

​(

Date

dateTime)

Construct a new date-time at completed attribute with the given

Date

value.

---

#### Constructor Summary

Construct a new date-time at completed attribute with the given

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

Returns whether this date-time at completed attribute is equivalent to
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

Returns whether this date-time at completed attribute is equivalent to
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

- DateTimeAtCompleted

```java
public DateTimeAtCompleted​(
Date
dateTime)
```

Construct a new date-time at completed attribute with the given

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

Returns whether this date-time at completed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtCompleted

.

This date-time at completed attribute's

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
completed attribute,

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

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

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

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- DateTimeAtCompleted

```java
public DateTimeAtCompleted​(
Date
dateTime)
```

Construct a new date-time at completed attribute with the given

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

DateTimeAtCompleted

```java
public DateTimeAtCompleted​(
Date
dateTime)
```

Construct a new date-time at completed attribute with the given

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

#### DateTimeAtCompleted

public DateTimeAtCompleted​(

Date

dateTime)

Construct a new date-time at completed attribute with the given

Date

value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this date-time at completed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtCompleted

.

This date-time at completed attribute's

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
completed attribute,

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

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

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

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

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

Returns whether this date-time at completed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtCompleted

.

This date-time at completed attribute's

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
completed attribute,

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

Returns whether this date-time at completed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

DateTimeAtCompleted

.

This date-time at completed attribute's

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

DateTimeAtCompleted

.

This date-time at completed attribute's

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

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

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

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

itself.

For class

DateTimeAtCompleted

, the category is class

DateTimeAtCompleted

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

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

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

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

.

For class

DateTimeAtCompleted

, the category name is

"date-time-at-completed"

.

---

