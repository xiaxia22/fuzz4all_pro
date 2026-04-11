# Class JobMediaSheets

**Source:** `java.desktop\javax\print\attribute\standard\JobMediaSheets.html`

### Class Description

```java
public class
JobMediaSheets

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobMediaSheets

is an integer valued printing attribute class
that specifies the total number of media sheets to be produced for this job.

The

JobMediaSheets

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobMediaSheets

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobMediaSheets

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobMediaSheets

attribute either right at
job submission time or at any later point in time.

Unlike the

JobKOctets

and

JobImpressions

attributes, the

JobMediaSheets

value must include the multiplicative factors contributed by the number of
copies specified by the

Copies

attribute and a "number of
copies" instruction embedded in the document data, if any. This difference
allows the system administrator to control the lower and upper bounds of both
(1) the size of the document(s) with

JobKOctetsSupported

and

JobImpressionsSupported

and (2) the size of
the job with

JobMediaSheetsSupported

.

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

#### public JobMediaSheets​(int value)

Construct a new job media sheets attribute with the given integer value.

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

Returns whether this job media sheets attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

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

is equivalent to this job media
sheets attribute,

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

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

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

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobMediaSheets

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.JobMediaSheets

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.JobMediaSheets

javax.print.attribute.standard.JobMediaSheets

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
public class
JobMediaSheets

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobMediaSheets

is an integer valued printing attribute class
that specifies the total number of media sheets to be produced for this job.

The

JobMediaSheets

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobMediaSheets

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobMediaSheets

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobMediaSheets

attribute either right at
job submission time or at any later point in time.

Unlike the

JobKOctets

and

JobImpressions

attributes, the

JobMediaSheets

value must include the multiplicative factors contributed by the number of
copies specified by the

Copies

attribute and a "number of
copies" instruction embedded in the document data, if any. This difference
allows the system administrator to control the lower and upper bounds of both
(1) the size of the document(s) with

JobKOctetsSupported

and

JobImpressionsSupported

and (2) the size of
the job with

JobMediaSheetsSupported

.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** JobMediaSheetsSupported

,

JobMediaSheetsCompleted

,

JobKOctets

,

JobImpressions

,

Serialized Form

public class

JobMediaSheets

extends

IntegerSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobMediaSheets

is an integer valued printing attribute class
that specifies the total number of media sheets to be produced for this job.

The

JobMediaSheets

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobMediaSheets

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobMediaSheets

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobMediaSheets

attribute either right at
job submission time or at any later point in time.

Unlike the

JobKOctets

and

JobImpressions

attributes, the

JobMediaSheets

value must include the multiplicative factors contributed by the number of
copies specified by the

Copies

attribute and a "number of
copies" instruction embedded in the document data, if any. This difference
allows the system administrator to control the lower and upper bounds of both
(1) the size of the document(s) with

JobKOctetsSupported

and

JobImpressionsSupported

and (2) the size of
the job with

JobMediaSheetsSupported

.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The

JobMediaSheets

attribute describes the size of the job. This
attribute is not intended to be a counter; it is intended to be useful
routing and scheduling information if known. The printer may try to compute
the

JobMediaSheets

attribute's value if it is not supplied in the
Print Request. Even if the client does supply a value for the

JobMediaSheets

attribute in the Print Request, the printer may choose
to change the value if the printer is able to compute a value which is more
accurate than the client supplied value. The printer may be able to determine
the correct value for the

JobMediaSheets

attribute either right at
job submission time or at any later point in time.

Unlike the

JobKOctets

and

JobImpressions

attributes, the

JobMediaSheets

value must include the multiplicative factors contributed by the number of
copies specified by the

Copies

attribute and a "number of
copies" instruction embedded in the document data, if any. This difference
allows the system administrator to control the lower and upper bounds of both
(1) the size of the document(s) with

JobKOctetsSupported

and

JobImpressionsSupported

and (2) the size of
the job with

JobMediaSheetsSupported

.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

Unlike the

JobKOctets

and

JobImpressions

attributes, the

JobMediaSheets

value must include the multiplicative factors contributed by the number of
copies specified by the

Copies

attribute and a "number of
copies" instruction embedded in the document data, if any. This difference
allows the system administrator to control the lower and upper bounds of both
(1) the size of the document(s) with

JobKOctetsSupported

and

JobImpressionsSupported

and (2) the size of
the job with

JobMediaSheetsSupported

.

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

JobMediaSheets

​(int value)

Construct a new job media sheets attribute with the given integer value.

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

Returns whether this job media sheets attribute is equivalent to the
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

JobMediaSheets

​(int value)

Construct a new job media sheets attribute with the given integer value.

---

#### Constructor Summary

Construct a new job media sheets attribute with the given integer value.

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

Returns whether this job media sheets attribute is equivalent to the
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

Returns whether this job media sheets attribute is equivalent to the
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

- JobMediaSheets

```java
public JobMediaSheets​(int value)
```

Construct a new job media sheets attribute with the given integer value.

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

Returns whether this job media sheets attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

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

is equivalent to this job media
sheets attribute,

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

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

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

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobMediaSheets

```java
public JobMediaSheets​(int value)
```

Construct a new job media sheets attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

JobMediaSheets

```java
public JobMediaSheets​(int value)
```

Construct a new job media sheets attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### JobMediaSheets

public JobMediaSheets​(int value)

Construct a new job media sheets attribute with the given integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job media sheets attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

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

is equivalent to this job media
sheets attribute,

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

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

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

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

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

Returns whether this job media sheets attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

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

is equivalent to this job media
sheets attribute,

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

Returns whether this job media sheets attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

object

's value
are equal.

object

is not

null

.

object

is an instance of class

JobMediaSheets

.

This job media sheets attribute's value and

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

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

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

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

itself.

For class

JobMediaSheets

and any vendor-defined subclasses, the
category is class

JobMediaSheets

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

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

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

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

.

For class

JobMediaSheets

and any vendor-defined subclasses, the
category name is

"job-media-sheets"

.

---

