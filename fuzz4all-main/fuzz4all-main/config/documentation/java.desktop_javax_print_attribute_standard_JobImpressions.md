# Class JobImpressions

**Source:** `java.desktop\javax\print\attribute\standard\JobImpressions.html`

### Class Description

```java
public final class
JobImpressions

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobImpressions

is an integer valued printing attribute class
that specifies the total size in number of impressions of the document(s)
being submitted. An "impression" is the image (possibly many print-stream
pages in different configurations) imposed onto a single media page.

The

JobImpressions

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobImpressions

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobImpressions

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobImpressions

attribute either right at
job submission time or at any later point in time.

As with

JobKOctets

, the

JobImpressions

value must
not include the multiplicative factors contributed by the number of copies
specified by the

Copies

attribute, independent of whether the
device can process multiple copies without making multiple passes over the
job or document data and independent of whether the output is collated or
not. Thus the value is independent of the implementation and reflects the
size of the document(s) measured in impressions independent of the number of
copies.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

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

#### public JobImpressions​(int value)

Construct a new job impressions attribute with the given integer value.

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

Returns whether this job impressions attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

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
impressions attribute,

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

JobImpressions

, the category is class

JobImpressions

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

JobImpressions

, the category name is

"job-impressions"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobImpressions

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.JobImpressions

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.JobImpressions

javax.print.attribute.standard.JobImpressions

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
JobImpressions

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobImpressions

is an integer valued printing attribute class
that specifies the total size in number of impressions of the document(s)
being submitted. An "impression" is the image (possibly many print-stream
pages in different configurations) imposed onto a single media page.

The

JobImpressions

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobImpressions

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobImpressions

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobImpressions

attribute either right at
job submission time or at any later point in time.

As with

JobKOctets

, the

JobImpressions

value must
not include the multiplicative factors contributed by the number of copies
specified by the

Copies

attribute, independent of whether the
device can process multiple copies without making multiple passes over the
job or document data and independent of whether the output is collated or
not. Thus the value is independent of the implementation and reflects the
size of the document(s) measured in impressions independent of the number of
copies.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** JobImpressionsSupported

,

JobImpressionsCompleted

,

JobKOctets

,

JobMediaSheets

,

Serialized Form

public final class

JobImpressions

extends

IntegerSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobImpressions

is an integer valued printing attribute class
that specifies the total size in number of impressions of the document(s)
being submitted. An "impression" is the image (possibly many print-stream
pages in different configurations) imposed onto a single media page.

The

JobImpressions

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobImpressions

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobImpressions

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobImpressions

attribute either right at
job submission time or at any later point in time.

As with

JobKOctets

, the

JobImpressions

value must
not include the multiplicative factors contributed by the number of copies
specified by the

Copies

attribute, independent of whether the
device can process multiple copies without making multiple passes over the
job or document data and independent of whether the output is collated or
not. Thus the value is independent of the implementation and reflects the
size of the document(s) measured in impressions independent of the number of
copies.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The

JobImpressions

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobImpressions

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobImpressions

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobImpressions

attribute either right at
job submission time or at any later point in time.

As with

JobKOctets

, the

JobImpressions

value must
not include the multiplicative factors contributed by the number of copies
specified by the

Copies

attribute, independent of whether the
device can process multiple copies without making multiple passes over the
job or document data and independent of whether the output is collated or
not. Thus the value is independent of the implementation and reflects the
size of the document(s) measured in impressions independent of the number of
copies.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

As with

JobKOctets

, the

JobImpressions

value must
not include the multiplicative factors contributed by the number of copies
specified by the

Copies

attribute, independent of whether the
device can process multiple copies without making multiple passes over the
job or document data and independent of whether the output is collated or
not. Thus the value is independent of the implementation and reflects the
size of the document(s) measured in impressions independent of the number of
copies.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

As with

JobKOctets

, the

JobImpressions

value must
also not include the multiplicative factor due to a copies instruction
embedded in the document data. If the document data actually includes
replications of the document data, this value will include such replication.
In other words, this value is always the number of impressions in the source
document data, rather than a measure of the number of impressions to be
produced by the job.

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

JobImpressions

​(int value)

Construct a new job impressions attribute with the given integer value.

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

Returns whether this job impressions attribute is equivalent to the
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

JobImpressions

​(int value)

Construct a new job impressions attribute with the given integer value.

---

#### Constructor Summary

Construct a new job impressions attribute with the given integer value.

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

Returns whether this job impressions attribute is equivalent to the
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

Returns whether this job impressions attribute is equivalent to the
passed in object.

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

- JobImpressions

```java
public JobImpressions​(int value)
```

Construct a new job impressions attribute with the given integer value.

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

Returns whether this job impressions attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

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
impressions attribute,

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

JobImpressions

, the category is class

JobImpressions

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

JobImpressions

, the category name is

"job-impressions"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobImpressions

```java
public JobImpressions​(int value)
```

Construct a new job impressions attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

JobImpressions

```java
public JobImpressions​(int value)
```

Construct a new job impressions attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### JobImpressions

public JobImpressions​(int value)

Construct a new job impressions attribute with the given integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job impressions attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

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
impressions attribute,

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

JobImpressions

, the category is class

JobImpressions

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

JobImpressions

, the category name is

"job-impressions"

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

Returns whether this job impressions attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

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
impressions attribute,

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

Returns whether this job impressions attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

object

is not

null

.

object

is an instance of class

JobImpressions

.

This job impressions attribute's value and

object

's value
are equal.

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

JobImpressions

, the category is class

JobImpressions

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

JobImpressions

, the category is class

JobImpressions

itself.

For class

JobImpressions

, the category is class

JobImpressions

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

JobImpressions

, the category name is

"job-impressions"

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

JobImpressions

, the category name is

"job-impressions"

.

For class

JobImpressions

, the category name is

"job-impressions"

.

---

