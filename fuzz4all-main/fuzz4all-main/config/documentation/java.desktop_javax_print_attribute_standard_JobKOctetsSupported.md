# Class JobKOctetsSupported

**Source:** `java.desktop\javax\print\attribute\standard\JobKOctetsSupported.html`

### Class Description

```java
public final class
JobKOctetsSupported

extends
SetOfIntegerSyntax

implements
SupportedValuesAttribute
```

Class

JobKOctetsSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

JobKOctets

attribute. It is restricted to a single contiguous range of integers;
multiple non-overlapping ranges are not allowed. This gives the lower and
upper bounds of the total sizes of print jobs in units of K octets (1024
octets) that the printer will accept.

IPP Compatibility:

The

JobKOctetsSupported

attribute's
canonical array form gives the lower and upper bound for the range of values
to be included in an IPP "job-k-octets-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

SupportedValuesAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobKOctetsSupported​(int lowerBound,
int upperBound)

Construct a new job K octets supported attribute containing a single
range of integers. That is, only those values of JobKOctets in the one
range are supported.

**Parameters:**
- lowerBound

- Lower bound of the range
- upperBound

- Upper bound of the range

**Throws:**
- IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than zero

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this job K octets supported attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

**Overrides:**
- equals

in class

SetOfIntegerSyntax

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
supported attribute,

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

JobKOctetsSupported

, the category is class

JobKOctetsSupported

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

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobKOctetsSupported

java.lang.Object

- javax.print.attribute.SetOfIntegerSyntax
- - javax.print.attribute.standard.JobKOctetsSupported

javax.print.attribute.SetOfIntegerSyntax

- javax.print.attribute.standard.JobKOctetsSupported

javax.print.attribute.standard.JobKOctetsSupported

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

SupportedValuesAttribute

```java
public final class
JobKOctetsSupported

extends
SetOfIntegerSyntax

implements
SupportedValuesAttribute
```

Class

JobKOctetsSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

JobKOctets

attribute. It is restricted to a single contiguous range of integers;
multiple non-overlapping ranges are not allowed. This gives the lower and
upper bounds of the total sizes of print jobs in units of K octets (1024
octets) that the printer will accept.

IPP Compatibility:

The

JobKOctetsSupported

attribute's
canonical array form gives the lower and upper bound for the range of values
to be included in an IPP "job-k-octets-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

**See Also:** Serialized Form

public final class

JobKOctetsSupported

extends

SetOfIntegerSyntax

implements

SupportedValuesAttribute

Class

JobKOctetsSupported

is a printing attribute class, a set of
integers, that gives the supported values for a

JobKOctets

attribute. It is restricted to a single contiguous range of integers;
multiple non-overlapping ranges are not allowed. This gives the lower and
upper bounds of the total sizes of print jobs in units of K octets (1024
octets) that the printer will accept.

IPP Compatibility:

The

JobKOctetsSupported

attribute's
canonical array form gives the lower and upper bound for the range of values
to be included in an IPP "job-k-octets-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

IPP Compatibility:

The

JobKOctetsSupported

attribute's
canonical array form gives the lower and upper bound for the range of values
to be included in an IPP "job-k-octets-supported" attribute. See class

SetOfIntegerSyntax

for an explanation of canonical
array form. The category name returned by

getName()

gives the IPP
attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JobKOctetsSupported

​(int lowerBound,
int upperBound)

Construct a new job K octets supported attribute containing a single
range of integers.

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

Returns whether this job K octets supported attribute is equivalent to
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

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

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

JobKOctetsSupported

​(int lowerBound,
int upperBound)

Construct a new job K octets supported attribute containing a single
range of integers.

---

#### Constructor Summary

Construct a new job K octets supported attribute containing a single
range of integers.

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

Returns whether this job K octets supported attribute is equivalent to
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

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

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

Returns whether this job K octets supported attribute is equivalent to
the passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

SetOfIntegerSyntax

contains

,

contains

,

getMembers

,

hashCode

,

next

,

toString

---

#### Methods declared in class javax.print.attribute. SetOfIntegerSyntax

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

- JobKOctetsSupported

```java
public JobKOctetsSupported​(int lowerBound,
int upperBound)
```

Construct a new job K octets supported attribute containing a single
range of integers. That is, only those values of JobKOctets in the one
range are supported.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than zero

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job K octets supported attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job K octets
supported attribute,

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

JobKOctetsSupported

, the category is class

JobKOctetsSupported

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

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobKOctetsSupported

```java
public JobKOctetsSupported​(int lowerBound,
int upperBound)
```

Construct a new job K octets supported attribute containing a single
range of integers. That is, only those values of JobKOctets in the one
range are supported.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than zero

---

#### Constructor Detail

JobKOctetsSupported

```java
public JobKOctetsSupported​(int lowerBound,
int upperBound)
```

Construct a new job K octets supported attribute containing a single
range of integers. That is, only those values of JobKOctets in the one
range are supported.

**Parameters:** lowerBound

- Lower bound of the range
**Parameters:** upperBound

- Upper bound of the range
**Throws:** IllegalArgumentException

- if a

null

range is specified or
if a

non-null

range is specified with

lowerBound

less than zero

---

#### JobKOctetsSupported

public JobKOctetsSupported​(int lowerBound,
int upperBound)

Construct a new job K octets supported attribute containing a single
range of integers. That is, only those values of JobKOctets in the one
range are supported.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job K octets supported attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job K octets
supported attribute,

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

JobKOctetsSupported

, the category is class

JobKOctetsSupported

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

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

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

Returns whether this job K octets supported attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

**Overrides:** equals

in class

SetOfIntegerSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this job K octets
supported attribute,

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

Returns whether this job K octets supported attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

object

is not

null

.

object

is an instance of class

JobKOctetsSupported

.

This job K octets supported attribute's members and

object

's members are the same.

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

JobKOctetsSupported

, the category is class

JobKOctetsSupported

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

JobKOctetsSupported

, the category is class

JobKOctetsSupported

itself.

For class

JobKOctetsSupported

, the category is class

JobKOctetsSupported

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

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

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

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

.

For class

JobKOctetsSupported

, the category name is

"job-k-octets-supported"

.

---

