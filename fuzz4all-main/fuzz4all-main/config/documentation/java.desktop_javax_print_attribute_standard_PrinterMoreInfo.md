# Class PrinterMoreInfo

**Source:** `java.desktop\javax\print\attribute\standard\PrinterMoreInfo.html`

### Class Description

```java
public final class
PrinterMoreInfo

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterMoreInfo

is a printing attribute class, a

URI

,
that is used to obtain more information about this specific printer. For
example, this could be an HTTP type

URI

referencing an HTML page
accessible to a web browser. The information obtained from this

URI

is intended for end user consumption. Features outside the scope of the Print
Service API can be accessed from this

URI

. The information is
intended to be specific to this printer instance and site specific services
(e.g. job pricing, services offered, end user assistance).

In contrast, the

PrinterMoreInfoManufacturer

attribute is
used to find out more information about this general kind of printer rather
than this specific printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

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

#### public PrinterMoreInfo​(
URI
uri)

Constructs a new printer more info attribute with the specified

URI

.

**Parameters:**
- uri

-

URI

**Throws:**
- NullPointerException

- if

uri

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this printer more info attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

are equal.

**Overrides:**
- equals

in class

URISyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this printer more
info attribute,

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

PrinterMoreInfo

, the category is class

PrinterMoreInfo

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

PrinterMoreInfo

, the category name is

"printer-more-info"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterMoreInfo

java.lang.Object

- javax.print.attribute.URISyntax
- - javax.print.attribute.standard.PrinterMoreInfo

javax.print.attribute.URISyntax

- javax.print.attribute.standard.PrinterMoreInfo

javax.print.attribute.standard.PrinterMoreInfo

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterMoreInfo

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterMoreInfo

is a printing attribute class, a

URI

,
that is used to obtain more information about this specific printer. For
example, this could be an HTTP type

URI

referencing an HTML page
accessible to a web browser. The information obtained from this

URI

is intended for end user consumption. Features outside the scope of the Print
Service API can be accessed from this

URI

. The information is
intended to be specific to this printer instance and site specific services
(e.g. job pricing, services offered, end user assistance).

In contrast, the

PrinterMoreInfoManufacturer

attribute is
used to find out more information about this general kind of printer rather
than this specific printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterMoreInfo

extends

URISyntax

implements

PrintServiceAttribute

Class

PrinterMoreInfo

is a printing attribute class, a

URI

,
that is used to obtain more information about this specific printer. For
example, this could be an HTTP type

URI

referencing an HTML page
accessible to a web browser. The information obtained from this

URI

is intended for end user consumption. Features outside the scope of the Print
Service API can be accessed from this

URI

. The information is
intended to be specific to this printer instance and site specific services
(e.g. job pricing, services offered, end user assistance).

In contrast, the

PrinterMoreInfoManufacturer

attribute is
used to find out more information about this general kind of printer rather
than this specific printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

In contrast, the

PrinterMoreInfoManufacturer

attribute is
used to find out more information about this general kind of printer rather
than this specific printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterMoreInfo

​(

URI

uri)

Constructs a new printer more info attribute with the specified

URI

.

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

Returns whether this printer more info attribute is equivalent to the
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

URISyntax

getURI

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

PrinterMoreInfo

​(

URI

uri)

Constructs a new printer more info attribute with the specified

URI

.

---

#### Constructor Summary

Constructs a new printer more info attribute with the specified

URI

.

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

Returns whether this printer more info attribute is equivalent to the
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

URISyntax

getURI

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

Returns whether this printer more info attribute is equivalent to the
passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

URISyntax

getURI

,

hashCode

,

toString

---

#### Methods declared in class javax.print.attribute. URISyntax

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

- PrinterMoreInfo

```java
public PrinterMoreInfo​(
URI
uri)
```

Constructs a new printer more info attribute with the specified

URI

.

**Parameters:** uri

-

URI
**Throws:** NullPointerException

- if

uri

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

Returns whether this printer more info attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

are equal.

**Overrides:** equals

in class

URISyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer more
info attribute,

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

PrinterMoreInfo

, the category is class

PrinterMoreInfo

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

PrinterMoreInfo

, the category name is

"printer-more-info"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterMoreInfo

```java
public PrinterMoreInfo​(
URI
uri)
```

Constructs a new printer more info attribute with the specified

URI

.

**Parameters:** uri

-

URI
**Throws:** NullPointerException

- if

uri

is

null

---

#### Constructor Detail

PrinterMoreInfo

```java
public PrinterMoreInfo​(
URI
uri)
```

Constructs a new printer more info attribute with the specified

URI

.

**Parameters:** uri

-

URI
**Throws:** NullPointerException

- if

uri

is

null

---

#### PrinterMoreInfo

public PrinterMoreInfo​(

URI

uri)

Constructs a new printer more info attribute with the specified

URI

.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer more info attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

are equal.

**Overrides:** equals

in class

URISyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer more
info attribute,

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

PrinterMoreInfo

, the category is class

PrinterMoreInfo

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

PrinterMoreInfo

, the category name is

"printer-more-info"

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

Returns whether this printer more info attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

are equal.

**Overrides:** equals

in class

URISyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer more
info attribute,

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

Returns whether this printer more info attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

are equal.

object

is not

null

.

object

is an instance of class

PrinterMoreInfo

.

This printer more info attribute's

URI

and

object

's

URI

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

PrinterMoreInfo

, the category is class

PrinterMoreInfo

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

PrinterMoreInfo

, the category is class

PrinterMoreInfo

itself.

For class

PrinterMoreInfo

, the category is class

PrinterMoreInfo

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

PrinterMoreInfo

, the category name is

"printer-more-info"

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

PrinterMoreInfo

, the category name is

"printer-more-info"

.

For class

PrinterMoreInfo

, the category name is

"printer-more-info"

.

---

