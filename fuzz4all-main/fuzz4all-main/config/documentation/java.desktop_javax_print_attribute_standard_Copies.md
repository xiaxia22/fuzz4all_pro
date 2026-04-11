# Class Copies

**Source:** `java.desktop\javax\print\attribute\standard\Copies.html`

### Class Description

```java
public final class
Copies

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Copies

is an integer valued printing attribute class that
specifies the number of copies to be printed.

On many devices the supported number of collated copies will be limited by
the number of physical output bins on the device, and may be different from
the number of uncollated copies which can be supported.

The effect of a

Copies

attribute with a value of

n

on a
multidoc print job (a job with multiple documents) depends on the (perhaps
defaulted) value of the

MultipleDocumentHandling

attribute:

- SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

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

#### public Copies​(int value)

Construct a new copies attribute with the given integer value.

**Parameters:**
- value

- Integer value

**Throws:**
- IllegalArgumentException

- if

value < 1

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this copies attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

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

is equivalent to this copies
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

Copies

, the category is class

Copies

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

Copies

, the category name is

"copies"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Copies

java.lang.Object

- javax.print.attribute.IntegerSyntax
- - javax.print.attribute.standard.Copies

javax.print.attribute.IntegerSyntax

- javax.print.attribute.standard.Copies

javax.print.attribute.standard.Copies

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
Copies

extends
IntegerSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Copies

is an integer valued printing attribute class that
specifies the number of copies to be printed.

On many devices the supported number of collated copies will be limited by
the number of physical output bins on the device, and may be different from
the number of uncollated copies which can be supported.

The effect of a

Copies

attribute with a value of

n

on a
multidoc print job (a job with multiple documents) depends on the (perhaps
defaulted) value of the

MultipleDocumentHandling

attribute:

- SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

Copies

extends

IntegerSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

Copies

is an integer valued printing attribute class that
specifies the number of copies to be printed.

On many devices the supported number of collated copies will be limited by
the number of physical output bins on the device, and may be different from
the number of uncollated copies which can be supported.

The effect of a

Copies

attribute with a value of

n

on a
multidoc print job (a job with multiple documents) depends on the (perhaps
defaulted) value of the

MultipleDocumentHandling

attribute:

- SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

On many devices the supported number of collated copies will be limited by
the number of physical output bins on the device, and may be different from
the number of uncollated copies which can be supported.

The effect of a

Copies

attribute with a value of

n

on a
multidoc print job (a job with multiple documents) depends on the (perhaps
defaulted) value of the

MultipleDocumentHandling

attribute:

- SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

The effect of a

Copies

attribute with a value of

n

on a
multidoc print job (a job with multiple documents) depends on the (perhaps
defaulted) value of the

MultipleDocumentHandling

attribute:

- SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

IPP Compatibility:

The integer value gives the IPP integer value. The
category name returned by

getName()

gives the IPP attribute name.

SINGLE_DOCUMENT

-- The result will be

n

copies of a
single output document comprising all the input docs.

SINGLE_DOCUMENT_NEW_SHEET

-- The result will be

n

copies
of a single output document comprising all the input docs, and the first
impression of each input doc will always start on a new media sheet.

SEPARATE_DOCUMENTS_UNCOLLATED_COPIES

-- The result will be

n

copies of the first input document, followed by

n

copies of
the second input document, . . . followed by

n

copies of the last
input document.

SEPARATE_DOCUMENTS_COLLATED_COPIES

-- The result will be the
first input document, the second input document, . . . the last input
document, the group of documents being repeated

n

times.

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

Copies

​(int value)

Construct a new copies attribute with the given integer value.

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

Returns whether this copies attribute is equivalent to the passed in
object.

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

Copies

​(int value)

Construct a new copies attribute with the given integer value.

---

#### Constructor Summary

Construct a new copies attribute with the given integer value.

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

Returns whether this copies attribute is equivalent to the passed in
object.

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

Returns whether this copies attribute is equivalent to the passed in
object.

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

- Copies

```java
public Copies​(int value)
```

Construct a new copies attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value < 1

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this copies attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

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

is equivalent to this copies
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

Copies

, the category is class

Copies

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

Copies

, the category name is

"copies"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- Copies

```java
public Copies​(int value)
```

Construct a new copies attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value < 1

---

#### Constructor Detail

Copies

```java
public Copies​(int value)
```

Construct a new copies attribute with the given integer value.

**Parameters:** value

- Integer value
**Throws:** IllegalArgumentException

- if

value < 1

---

#### Copies

public Copies​(int value)

Construct a new copies attribute with the given integer value.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this copies attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

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

is equivalent to this copies
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

Copies

, the category is class

Copies

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

Copies

, the category name is

"copies"

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

Returns whether this copies attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

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

is equivalent to this copies
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

Returns whether this copies attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

object

's value are equal.

object

is not

null

.

object

is an instance of class

Copies

.

This copies attribute's value and

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

Copies

, the category is class

Copies

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

Copies

, the category is class

Copies

itself.

For class

Copies

, the category is class

Copies

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

Copies

, the category name is

"copies"

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

Copies

, the category name is

"copies"

.

For class

Copies

, the category name is

"copies"

.

---

