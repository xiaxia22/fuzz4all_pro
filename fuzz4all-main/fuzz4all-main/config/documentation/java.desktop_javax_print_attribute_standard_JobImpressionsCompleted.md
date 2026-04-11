# Class JobImpressionsCompleted

**Source:** `java.desktop\javax\print\attribute\standard\JobImpressionsCompleted.html`

### Class Description

```java
public final class
JobImpressionsCompleted

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

JobImpressionsCompleted

is an integer valued printing attribute
class that specifies the number of impressions completed for the job so far.
For printing devices, the impressions completed includes interpreting,
marking, and stacking the output.

The

JobImpressionsCompleted

attribute describes the progress of the
job. This attribute is intended to be a counter. That is, the

JobImpressionsCompleted

value for a job that has not started
processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobImpressionsCompleted

value is intended to increase as the job is
processed; it indicates the amount of the job that has been processed at the
time the Print Job's attribute set is queried or at the time a print job
event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobImpressionsCompleted

value is the final value for the job.

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

#### public JobImpressionsCompleted​(int value)

Construct a new job impressions completed attribute with the given
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

Returns whether this job impressions completed attribute is equivalent tp
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

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

is equivalent to this job
impressions completed attribute,

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

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

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

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobImpressionsCompleted

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.JobImpressionsCompleted

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.JobImpressionsCompleted

javax.print.attribute.standard.JobImpressionsCompleted

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
JobImpressionsCompleted

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

JobImpressionsCompleted

is an integer valued printing attribute
class that specifies the number of impressions completed for the job so far.
For printing devices, the impressions completed includes interpreting,
marking, and stacking the output.

The

JobImpressionsCompleted

attribute describes the progress of the
job. This attribute is intended to be a counter. That is, the

JobImpressionsCompleted

value for a job that has not started
processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobImpressionsCompleted

value is intended to increase as the job is
processed; it indicates the amount of the job that has been processed at the
time the Print Job's attribute set is queried or at the time a print job
event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobImpressionsCompleted

value is the final value for the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** JobImpressions

,

JobImpressionsSupported

,

JobKOctetsProcessed

,

JobMediaSheetsCompleted

,

Serialized Form

public final class

JobImpressionsCompleted

extends

IntegerSyntax

implements

PrintJobAttribute

Class

JobImpressionsCompleted

is an integer valued printing attribute
class that specifies the number of impressions completed for the job so far.
For printing devices, the impressions completed includes interpreting,
marking, and stacking the output.

The

JobImpressionsCompleted

attribute describes the progress of the
job. This attribute is intended to be a counter. That is, the

JobImpressionsCompleted

value for a job that has not started
processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobImpressionsCompleted

value is intended to increase as the job is
processed; it indicates the amount of the job that has been processed at the
time the Print Job's attribute set is queried or at the time a print job
event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobImpressionsCompleted

value is the final value for the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The

JobImpressionsCompleted

attribute describes the progress of the
job. This attribute is intended to be a counter. That is, the

JobImpressionsCompleted

value for a job that has not started
processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobImpressionsCompleted

value is intended to increase as the job is
processed; it indicates the amount of the job that has been processed at the
time the Print Job's attribute set is queried or at the time a print job
event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobImpressionsCompleted

value is the final value for the job.

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

JobImpressionsCompleted

​(int value)

Construct a new job impressions completed attribute with the given
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

Returns whether this job impressions completed attribute is equivalent tp
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

JobImpressionsCompleted

​(int value)

Construct a new job impressions completed attribute with the given
integer value.

---

#### Constructor Summary

Construct a new job impressions completed attribute with the given
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

Returns whether this job impressions completed attribute is equivalent tp
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

Returns whether this job impressions completed attribute is equivalent tp
the passed in object.

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

- JobImpressionsCompleted

```java
public JobImpressionsCompleted​(int value)
```

Construct a new job impressions completed attribute with the given
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

Returns whether this job impressions completed attribute is equivalent tp
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

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

is equivalent to this job
impressions completed attribute,

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

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

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

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobImpressionsCompleted

```java
public JobImpressionsCompleted​(int value)
```

Construct a new job impressions completed attribute with the given
integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

JobImpressionsCompleted

```java
public JobImpressionsCompleted​(int value)
```

Construct a new job impressions completed attribute with the given
integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### JobImpressionsCompleted

public JobImpressionsCompleted​(int value)

Construct a new job impressions completed attribute with the given
integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job impressions completed attribute is equivalent tp
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

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

is equivalent to this job
impressions completed attribute,

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

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

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

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

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

Returns whether this job impressions completed attribute is equivalent tp
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

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

is equivalent to this job
impressions completed attribute,

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

Returns whether this job impressions completed attribute is equivalent tp
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

object

's value are equal.

object

is not

null

.

object

is an instance of class

JobImpressionsCompleted

.

This job impressions completed attribute's value and

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

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

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

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

itself.

For class

JobImpressionsCompleted

, the category is class

JobImpressionsCompleted

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

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

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

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

.

For class

JobImpressionsCompleted

, the category name is

"job-impressions-completed"

.

---

