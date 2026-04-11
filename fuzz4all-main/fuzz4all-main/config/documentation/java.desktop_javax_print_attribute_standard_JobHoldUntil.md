# Class JobHoldUntil

**Source:** `java.desktop\javax\print\attribute\standard\JobHoldUntil.html`

### Class Description

```java
public final class
JobHoldUntil

extends
DateTimeSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobHoldUntil

is a printing attribute class, a date-time
attribute, that specifies the exact date and time at which the job must
become a candidate for printing.

If the value of this attribute specifies a date-time that is in the future,
the printer should add the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

to the job's

JobStateReasons

attribute, must move the job to the

PENDING_HELD

state, and must not schedule the job for printing until
the specified date-time arrives.

When the specified date-time arrives, the printer must remove the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

from the job's

JobStateReasons

attribute, if present. If there are
no other job state reasons that keep the job in the

PENDING_HELD

state, the printer must consider the job as a candidate for processing by
moving the job to the PENDING state.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobHoldUntil​(
Date
dateTime)

Construct a new job hold until date-time attribute with the given

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

Returns whether this job hold until attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobHoldUntil

.

This job hold until attribute's

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

is equivalent to this job hold
until attribute,

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

JobHoldUntil

, the category is class

JobHoldUntil

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

JobHoldUntil

, the category name is

"job-hold-until"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobHoldUntil

java.lang.Object

- javax.print.attribute.DateTimeSyntax
- - javax.print.attribute.standard.JobHoldUntil

javax.print.attribute.DateTimeSyntax

- javax.print.attribute.standard.JobHoldUntil

javax.print.attribute.standard.JobHoldUntil

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
JobHoldUntil

extends
DateTimeSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobHoldUntil

is a printing attribute class, a date-time
attribute, that specifies the exact date and time at which the job must
become a candidate for printing.

If the value of this attribute specifies a date-time that is in the future,
the printer should add the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

to the job's

JobStateReasons

attribute, must move the job to the

PENDING_HELD

state, and must not schedule the job for printing until
the specified date-time arrives.

When the specified date-time arrives, the printer must remove the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

from the job's

JobStateReasons

attribute, if present. If there are
no other job state reasons that keep the job in the

PENDING_HELD

state, the printer must consider the job as a candidate for processing by
moving the job to the PENDING state.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

JobHoldUntil

extends

DateTimeSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobHoldUntil

is a printing attribute class, a date-time
attribute, that specifies the exact date and time at which the job must
become a candidate for printing.

If the value of this attribute specifies a date-time that is in the future,
the printer should add the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

to the job's

JobStateReasons

attribute, must move the job to the

PENDING_HELD

state, and must not schedule the job for printing until
the specified date-time arrives.

When the specified date-time arrives, the printer must remove the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

from the job's

JobStateReasons

attribute, if present. If there are
no other job state reasons that keep the job in the

PENDING_HELD

state, the printer must consider the job as a candidate for processing by
moving the job to the PENDING state.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

If the value of this attribute specifies a date-time that is in the future,
the printer should add the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

to the job's

JobStateReasons

attribute, must move the job to the

PENDING_HELD

state, and must not schedule the job for printing until
the specified date-time arrives.

When the specified date-time arrives, the printer must remove the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

from the job's

JobStateReasons

attribute, if present. If there are
no other job state reasons that keep the job in the

PENDING_HELD

state, the printer must consider the job as a candidate for processing by
moving the job to the PENDING state.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

When the specified date-time arrives, the printer must remove the

JobStateReason

value of

JOB_HOLD_UNTIL_SPECIFIED

from the job's

JobStateReasons

attribute, if present. If there are
no other job state reasons that keep the job in the

PENDING_HELD

state, the printer must consider the job as a candidate for processing by
moving the job to the PENDING state.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

If the specified date-time has already passed, the job must be a candidate
for processing immediately. Thus, one way to make the job immediately become
a candidate for processing is to specify a

JobHoldUntil

attribute
constructed like this
(denoting a date-time of January 1, 1970, 00:00:00 GMT):

```java
JobHoldUntil immediately = new JobHoldUntil (new Date (0L));
```

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

JobHoldUntil immediately = new JobHoldUntil (new Date (0L));

If the client does not supply this attribute in a Print Request and the
printer supports this attribute, the printer must use its
(implementation-dependent) default

JobHoldUntil

value at job
submission time (unlike most job template attributes that are used if
necessary at job processing time).

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

To construct a

JobHoldUntil

attribute from separate values of the
year, month, day, hour, minute, and so on, use a

Calendar

object to construct a

Date

object, then use the

Date

object to construct the

JobHoldUntil

attribute. To
convert a

JobHoldUntil

attribute to separate values of the year,
month, day, hour, minute, and so on, create a

Calendar

object and set it to the

Date

from the

JobHoldUntil

attribute.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

Although IPP supports a "job-hold-until" attribute
specified as a keyword, IPP does not at this time support a "job-hold-until"
attribute specified as a date and time. However, the date and time can be
converted to one of the standard IPP keywords with some loss of precision;
for example, a

JobHoldUntil

value with today's date and 9:00pm local
time might be converted to the standard IPP keyword "night". The category
name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JobHoldUntil

​(

Date

dateTime)

Construct a new job hold until date-time attribute with the given

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

Returns whether this job hold until attribute is equivalent to the passed
in object.

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

JobHoldUntil

​(

Date

dateTime)

Construct a new job hold until date-time attribute with the given

Date

value.

---

#### Constructor Summary

Construct a new job hold until date-time attribute with the given

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

Returns whether this job hold until attribute is equivalent to the passed
in object.

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

Returns whether this job hold until attribute is equivalent to the passed
in object.

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

- JobHoldUntil

```java
public JobHoldUntil​(
Date
dateTime)
```

Construct a new job hold until date-time attribute with the given

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

Returns whether this job hold until attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobHoldUntil

.

This job hold until attribute's

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

is equivalent to this job hold
until attribute,

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

JobHoldUntil

, the category is class

JobHoldUntil

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

JobHoldUntil

, the category name is

"job-hold-until"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobHoldUntil

```java
public JobHoldUntil​(
Date
dateTime)
```

Construct a new job hold until date-time attribute with the given

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

JobHoldUntil

```java
public JobHoldUntil​(
Date
dateTime)
```

Construct a new job hold until date-time attribute with the given

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

#### JobHoldUntil

public JobHoldUntil​(

Date

dateTime)

Construct a new job hold until date-time attribute with the given

Date

value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job hold until attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobHoldUntil

.

This job hold until attribute's

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

is equivalent to this job hold
until attribute,

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

JobHoldUntil

, the category is class

JobHoldUntil

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

JobHoldUntil

, the category name is

"job-hold-until"

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

Returns whether this job hold until attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobHoldUntil

.

This job hold until attribute's

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

is equivalent to this job hold
until attribute,

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

Returns whether this job hold until attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobHoldUntil

.

This job hold until attribute's

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

JobHoldUntil

.

This job hold until attribute's

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

JobHoldUntil

, the category is class

JobHoldUntil

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

JobHoldUntil

, the category is class

JobHoldUntil

itself.

For class

JobHoldUntil

, the category is class

JobHoldUntil

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

JobHoldUntil

, the category name is

"job-hold-until"

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

JobHoldUntil

, the category name is

"job-hold-until"

.

For class

JobHoldUntil

, the category name is

"job-hold-until"

.

---

