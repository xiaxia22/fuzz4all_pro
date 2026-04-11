# Class JobPriority

**Source:** `java.desktop\javax\print\attribute\standard\JobPriority.html`

### Class Description

```java
public final class
JobPriority

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobPriority

is an integer valued printing attribute class that
specifies a print job's priority.

If a

JobPriority

attribute is specified for a Print Job, it specifies
a priority for scheduling the job. A higher value specifies a higher
priority. The value 1 indicates the lowest possible priority. The value 100
indicates the highest possible priority. Among those jobs that are ready to
print, a printer must print all jobs with a priority value of

n

before
printing those with a priority value of

n

-1 for all

n.

If the client does not specify a

JobPriority

attribute for a Print
Job and the printer does support the JobPriority attribute, the printer must
use an implementation-defined default JobPriority value.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

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

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobPriority​(int value)

Construct a new job priority attribute with the given integer value.

**Parameters:**
- value

- Integer value

**Throws:**
- IllegalArgumentException

- if

value

is less than 1 or
greater than 100

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this job priority attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

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

is equivalent to this job priority
attribute,

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

JobPriority

, the category is class

JobPriority

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

JobPriority

, the category name is

"job-priority"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobPriority

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.JobPriority

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.JobPriority

javax.print.attribute.standard.JobPriority

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
JobPriority

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobPriority

is an integer valued printing attribute class that
specifies a print job's priority.

If a

JobPriority

attribute is specified for a Print Job, it specifies
a priority for scheduling the job. A higher value specifies a higher
priority. The value 1 indicates the lowest possible priority. The value 100
indicates the highest possible priority. Among those jobs that are ready to
print, a printer must print all jobs with a priority value of

n

before
printing those with a priority value of

n

-1 for all

n.

If the client does not specify a

JobPriority

attribute for a Print
Job and the printer does support the JobPriority attribute, the printer must
use an implementation-defined default JobPriority value.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

JobPriority

extends

IntegerSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobPriority

is an integer valued printing attribute class that
specifies a print job's priority.

If a

JobPriority

attribute is specified for a Print Job, it specifies
a priority for scheduling the job. A higher value specifies a higher
priority. The value 1 indicates the lowest possible priority. The value 100
indicates the highest possible priority. Among those jobs that are ready to
print, a printer must print all jobs with a priority value of

n

before
printing those with a priority value of

n

-1 for all

n.

If the client does not specify a

JobPriority

attribute for a Print
Job and the printer does support the JobPriority attribute, the printer must
use an implementation-defined default JobPriority value.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

If a

JobPriority

attribute is specified for a Print Job, it specifies
a priority for scheduling the job. A higher value specifies a higher
priority. The value 1 indicates the lowest possible priority. The value 100
indicates the highest possible priority. Among those jobs that are ready to
print, a printer must print all jobs with a priority value of

n

before
printing those with a priority value of

n

-1 for all

n.

If the client does not specify a

JobPriority

attribute for a Print
Job and the printer does support the JobPriority attribute, the printer must
use an implementation-defined default JobPriority value.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

If the client does not specify a

JobPriority

attribute for a Print
Job and the printer does support the JobPriority attribute, the printer must
use an implementation-defined default JobPriority value.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The client can always specify any job priority value from 1 to 100 for a job.
However, a Print Service instance may support fewer than 100 different job
priority levels. If this is the case, the Print Service instance
automatically maps the client-specified job priority value to one of the
supported job priority levels, dividing the 100 job priority values equally
among the available job priority levels.

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

JobPriority

​(int value)

Construct a new job priority attribute with the given integer value.

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

Returns whether this job priority attribute is equivalent to the passed
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

JobPriority

​(int value)

Construct a new job priority attribute with the given integer value.

---

#### Constructor Summary

Construct a new job priority attribute with the given integer value.

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

Returns whether this job priority attribute is equivalent to the passed
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

Returns whether this job priority attribute is equivalent to the passed
in object.

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

- JobPriority

```java
public JobPriority​(int value)
```

Construct a new job priority attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is less than 1 or
greater than 100

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job priority attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

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

is equivalent to this job priority
attribute,

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

JobPriority

, the category is class

JobPriority

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

JobPriority

, the category name is

"job-priority"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobPriority

```java
public JobPriority​(int value)
```

Construct a new job priority attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is less than 1 or
greater than 100

---

#### Constructor Detail

JobPriority

```java
public JobPriority​(int value)
```

Construct a new job priority attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is less than 1 or
greater than 100

---

#### JobPriority

public JobPriority​(int value)

Construct a new job priority attribute with the given integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job priority attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

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

is equivalent to this job priority
attribute,

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

JobPriority

, the category is class

JobPriority

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

JobPriority

, the category name is

"job-priority"

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

Returns whether this job priority attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

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

is equivalent to this job priority
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

Returns whether this job priority attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

object

is not

null

.

object

is an instance of class

JobPriority

.

This job priority attribute's value and

object

's value are
equal.

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

JobPriority

, the category is class

JobPriority

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

JobPriority

, the category is class

JobPriority

itself.

For class

JobPriority

, the category is class

JobPriority

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

JobPriority

, the category name is

"job-priority"

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

JobPriority

, the category name is

"job-priority"

.

For class

JobPriority

, the category name is

"job-priority"

.

---

