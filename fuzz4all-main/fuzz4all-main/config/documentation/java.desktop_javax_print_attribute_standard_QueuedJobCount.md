# Class QueuedJobCount

**Source:** `java.desktop\javax\print\attribute\standard\QueuedJobCount.html`

### Class Description

```java
public final class
QueuedJobCount

extends
IntegerSyntax

implements
PrintServiceAttribute
```

Class

QueuedJobCount

is an integer valued printing attribute that
indicates the number of jobs in the printer whose

JobState

is either

PENDING

,

PENDING_HELD

,

PROCESSING

, or

PROCESSING_STOPPED

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

PrintServiceAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public QueuedJobCount​(int value)

Construct a new queued job count attribute with the given integer value.

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

Returns whether this queued job count attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions mus
be true:

- object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

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

is equivalent to this queued job
count attribute,

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

QueuedJobCount

, the category is class

QueuedJobCount

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

QueuedJobCount

, the category name is

"queued-job-count"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class QueuedJobCount

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.QueuedJobCount

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.QueuedJobCount

javax.print.attribute.standard.QueuedJobCount

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
QueuedJobCount

extends
IntegerSyntax

implements
PrintServiceAttribute
```

Class

QueuedJobCount

is an integer valued printing attribute that
indicates the number of jobs in the printer whose

JobState

is either

PENDING

,

PENDING_HELD

,

PROCESSING

, or

PROCESSING_STOPPED

.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

QueuedJobCount

extends

IntegerSyntax

implements

PrintServiceAttribute

Class

QueuedJobCount

is an integer valued printing attribute that
indicates the number of jobs in the printer whose

JobState

is either

PENDING

,

PENDING_HELD

,

PROCESSING

, or

PROCESSING_STOPPED

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

QueuedJobCount

​(int value)

Construct a new queued job count attribute with the given integer value.

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

Returns whether this queued job count attribute is equivalent to the
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

QueuedJobCount

​(int value)

Construct a new queued job count attribute with the given integer value.

---

#### Constructor Summary

Construct a new queued job count attribute with the given integer value.

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

Returns whether this queued job count attribute is equivalent to the
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

Returns whether this queued job count attribute is equivalent to the
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

- QueuedJobCount

```java
public QueuedJobCount​(int value)
```

Construct a new queued job count attribute with the given integer value.

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

Returns whether this queued job count attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions mus
be true:

- object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

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

is equivalent to this queued job
count attribute,

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

QueuedJobCount

, the category is class

QueuedJobCount

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

QueuedJobCount

, the category name is

"queued-job-count"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- QueuedJobCount

```java
public QueuedJobCount​(int value)
```

Construct a new queued job count attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### Constructor Detail

QueuedJobCount

```java
public QueuedJobCount​(int value)
```

Construct a new queued job count attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value

is negative

---

#### QueuedJobCount

public QueuedJobCount​(int value)

Construct a new queued job count attribute with the given integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this queued job count attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions mus
be true:

- object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

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

is equivalent to this queued job
count attribute,

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

QueuedJobCount

, the category is class

QueuedJobCount

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

QueuedJobCount

, the category name is

"queued-job-count"

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

Returns whether this queued job count attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions mus
be true:

- object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

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

is equivalent to this queued job
count attribute,

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

Returns whether this queued job count attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions mus
be true:

- object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

object

's value
are equal.

object

is not

null

.

object

is an instance of class

QueuedJobCount

.

This queued job count attribute's value and

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

QueuedJobCount

, the category is class

QueuedJobCount

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

QueuedJobCount

, the category is class

QueuedJobCount

itself.

For class

QueuedJobCount

, the category is class

QueuedJobCount

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

QueuedJobCount

, the category name is

"queued-job-count"

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

QueuedJobCount

, the category name is

"queued-job-count"

.

For class

QueuedJobCount

, the category name is

"queued-job-count"

.

---

