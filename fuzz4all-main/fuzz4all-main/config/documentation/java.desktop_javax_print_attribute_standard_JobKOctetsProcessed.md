# Class JobKOctetsProcessed

**Source:** `java.desktop\javax\print\attribute\standard\JobKOctetsProcessed.html`

### Class Description

```java
public final class
JobKOctetsProcessed

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

JobKOctetsProcessed

is an integer valued printing attribute
class that specifies the total number of print data octets processed so far
in K octets, i.e., in units of 1024 octets. The value must be rounded up, so
that a job between 1 and 1024 octets inclusive must be indicated as being 1K
octets, 1025 to 2048 inclusive must be 2K, etc. For a multidoc print job (a
job with multiple documents), the JobKOctetsProcessed value is computed by
adding up the individual documents' number of octets processed so far, then
rounding up to the next K octets value.

The

JobKOctetsProcessed

attribute describes the progress of the job.
This attribute is intended to be a counter. That is, the JobKOctetsProcessed
value for a job that has not started processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobKOctetsProcessed

value is intended
to increase as the job is processed; it indicates the amount of the job that
has been processed at the time the Print Job's attribute set is queried or at
the time a print job event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobKOctetsProcessed

value is the final value for the job.

For implementations where multiple copies are produced by the interpreter
with only a single pass over the data, the final value of the
JobKOctetsProcessed attribute must be equal to the value of the

JobKOctets

attribute. For implementations where multiple
copies are produced by the interpreter by processing the data for each copy,
the final value must be a multiple of the value of the

JobKOctets

attribute.

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

#### public JobKOctetsProcessed​(int value)

Construct a new job K octets processed attribute with the given integer
value.

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

Returns whether this job K octets processed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
value are equal.

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

is equivalent to this job K octets
processed attribute,

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

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

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

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobKOctetsProcessed

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.JobKOctetsProcessed

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.JobKOctetsProcessed

javax.print.attribute.standard.JobKOctetsProcessed

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
JobKOctetsProcessed

extends
IntegerSyntax

implements
PrintJobAttribute
```

Class

JobKOctetsProcessed

is an integer valued printing attribute
class that specifies the total number of print data octets processed so far
in K octets, i.e., in units of 1024 octets. The value must be rounded up, so
that a job between 1 and 1024 octets inclusive must be indicated as being 1K
octets, 1025 to 2048 inclusive must be 2K, etc. For a multidoc print job (a
job with multiple documents), the JobKOctetsProcessed value is computed by
adding up the individual documents' number of octets processed so far, then
rounding up to the next K octets value.

The

JobKOctetsProcessed

attribute describes the progress of the job.
This attribute is intended to be a counter. That is, the JobKOctetsProcessed
value for a job that has not started processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobKOctetsProcessed

value is intended
to increase as the job is processed; it indicates the amount of the job that
has been processed at the time the Print Job's attribute set is queried or at
the time a print job event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobKOctetsProcessed

value is the final value for the job.

For implementations where multiple copies are produced by the interpreter
with only a single pass over the data, the final value of the
JobKOctetsProcessed attribute must be equal to the value of the

JobKOctets

attribute. For implementations where multiple
copies are produced by the interpreter by processing the data for each copy,
the final value must be a multiple of the value of the

JobKOctets

attribute.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** JobKOctets

,

JobKOctetsSupported

,

JobImpressionsCompleted

,

JobMediaSheetsCompleted

,

Serialized Form

public final class

JobKOctetsProcessed

extends

IntegerSyntax

implements

PrintJobAttribute

Class

JobKOctetsProcessed

is an integer valued printing attribute
class that specifies the total number of print data octets processed so far
in K octets, i.e., in units of 1024 octets. The value must be rounded up, so
that a job between 1 and 1024 octets inclusive must be indicated as being 1K
octets, 1025 to 2048 inclusive must be 2K, etc. For a multidoc print job (a
job with multiple documents), the JobKOctetsProcessed value is computed by
adding up the individual documents' number of octets processed so far, then
rounding up to the next K octets value.

The

JobKOctetsProcessed

attribute describes the progress of the job.
This attribute is intended to be a counter. That is, the JobKOctetsProcessed
value for a job that has not started processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobKOctetsProcessed

value is intended
to increase as the job is processed; it indicates the amount of the job that
has been processed at the time the Print Job's attribute set is queried or at
the time a print job event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobKOctetsProcessed

value is the final value for the job.

For implementations where multiple copies are produced by the interpreter
with only a single pass over the data, the final value of the
JobKOctetsProcessed attribute must be equal to the value of the

JobKOctets

attribute. For implementations where multiple
copies are produced by the interpreter by processing the data for each copy,
the final value must be a multiple of the value of the

JobKOctets

attribute.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The

JobKOctetsProcessed

attribute describes the progress of the job.
This attribute is intended to be a counter. That is, the JobKOctetsProcessed
value for a job that has not started processing must be 0. When the job's

JobState

is

PROCESSING

or

PROCESSING_STOPPED

, the

JobKOctetsProcessed

value is intended
to increase as the job is processed; it indicates the amount of the job that
has been processed at the time the Print Job's attribute set is queried or at
the time a print job event is reported. When the job enters the

COMPLETED

,

CANCELED

, or

ABORTED

states, the

JobKOctetsProcessed

value is the final value for the job.

For implementations where multiple copies are produced by the interpreter
with only a single pass over the data, the final value of the
JobKOctetsProcessed attribute must be equal to the value of the

JobKOctets

attribute. For implementations where multiple
copies are produced by the interpreter by processing the data for each copy,
the final value must be a multiple of the value of the

JobKOctets

attribute.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

For implementations where multiple copies are produced by the interpreter
with only a single pass over the data, the final value of the
JobKOctetsProcessed attribute must be equal to the value of the

JobKOctets

attribute. For implementations where multiple
copies are produced by the interpreter by processing the data for each copy,
the final value must be a multiple of the value of the

JobKOctets

attribute.

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

JobKOctetsProcessed

​(int value)

Construct a new job K octets processed attribute with the given integer
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

Returns whether this job K octets processed attribute is equivalent to
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

JobKOctetsProcessed

​(int value)

Construct a new job K octets processed attribute with the given integer
value.

---

#### Constructor Summary

Construct a new job K octets processed attribute with the given integer
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

Returns whether this job K octets processed attribute is equivalent to
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

Returns whether this job K octets processed attribute is equivalent to
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

- JobKOctetsProcessed

```java
public JobKOctetsProcessed​(int value)
```

Construct a new job K octets processed attribute with the given integer
value.

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

Returns whether this job K octets processed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
value are equal.

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

is equivalent to this job K octets
processed attribute,

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

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

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

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobKOctetsProcessed

```java
public JobKOctetsProcessed​(int value)
```

Construct a new job K octets processed attribute with the given integer
value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

JobKOctetsProcessed

```java
public JobKOctetsProcessed​(int value)
```

Construct a new job K octets processed attribute with the given integer
value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### JobKOctetsProcessed

public JobKOctetsProcessed​(int value)

Construct a new job K octets processed attribute with the given integer
value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job K octets processed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
value are equal.

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

is equivalent to this job K octets
processed attribute,

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

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

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

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

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

Returns whether this job K octets processed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
value are equal.

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

is equivalent to this job K octets
processed attribute,

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

Returns whether this job K octets processed attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
value are equal.

object

is not

null

.

object

is an instance of class

JobKOctetsProcessed

.

This job K octets processed attribute's value and

object

's
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

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

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

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

itself.

For class

JobKOctetsProcessed

, the category is class

JobKOctetsProcessed

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

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

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

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

.

For class

JobKOctetsProcessed

, the category name is

"job-k-octets-processed"

.

---

