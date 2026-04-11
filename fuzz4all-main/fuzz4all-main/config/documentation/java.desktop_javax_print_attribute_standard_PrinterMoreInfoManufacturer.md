# Class PrinterMoreInfoManufacturer

**Source:** `java.desktop\javax\print\attribute\standard\PrinterMoreInfoManufacturer.html`

### Class Description

```java
public final class
PrinterMoreInfoManufacturer

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterMoreInfoManufacturer

is a printing attribute class, a

URI

, that is used to obtain more information about this type of
device. The information obtained from this

URI

is intended for end
user consumption. Features outside the scope of the Print Service API can be
accessed from this

URI

(e.g., latest firmware, upgrades, service
proxies, optional features available, details on color support). The
information is intended to be germane to this kind of printer without regard
to site specific modifications or services.

In contrast, the

PrinterMoreInfo

attribute is used to
find out more information about this specific printer rather than this
general kind of printer.

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

#### public PrinterMoreInfoManufacturer​(
URI
uri)

Constructs a new printer more info manufacturer attribute with the
specified

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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
info manufacturer attribute,

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

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

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

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterMoreInfoManufacturer

java.lang.Object

- javax.print.attribute.URISyntax
- - javax.print.attribute.standard.PrinterMoreInfoManufacturer

javax.print.attribute.URISyntax

- javax.print.attribute.standard.PrinterMoreInfoManufacturer

javax.print.attribute.standard.PrinterMoreInfoManufacturer

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterMoreInfoManufacturer

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterMoreInfoManufacturer

is a printing attribute class, a

URI

, that is used to obtain more information about this type of
device. The information obtained from this

URI

is intended for end
user consumption. Features outside the scope of the Print Service API can be
accessed from this

URI

(e.g., latest firmware, upgrades, service
proxies, optional features available, details on color support). The
information is intended to be germane to this kind of printer without regard
to site specific modifications or services.

In contrast, the

PrinterMoreInfo

attribute is used to
find out more information about this specific printer rather than this
general kind of printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterMoreInfoManufacturer

extends

URISyntax

implements

PrintServiceAttribute

Class

PrinterMoreInfoManufacturer

is a printing attribute class, a

URI

, that is used to obtain more information about this type of
device. The information obtained from this

URI

is intended for end
user consumption. Features outside the scope of the Print Service API can be
accessed from this

URI

(e.g., latest firmware, upgrades, service
proxies, optional features available, details on color support). The
information is intended to be germane to this kind of printer without regard
to site specific modifications or services.

In contrast, the

PrinterMoreInfo

attribute is used to
find out more information about this specific printer rather than this
general kind of printer.

IPP Compatibility:

The string form returned by

toString()

gives the IPP uri value. The category name returned by

getName()

gives the IPP attribute name.

In contrast, the

PrinterMoreInfo

attribute is used to
find out more information about this specific printer rather than this
general kind of printer.

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

PrinterMoreInfoManufacturer

​(

URI

uri)

Constructs a new printer more info manufacturer attribute with the
specified

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object.

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

PrinterMoreInfoManufacturer

​(

URI

uri)

Constructs a new printer more info manufacturer attribute with the
specified

URI

.

---

#### Constructor Summary

Constructs a new printer more info manufacturer attribute with the
specified

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object.

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object.

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

- PrinterMoreInfoManufacturer

```java
public PrinterMoreInfoManufacturer​(
URI
uri)
```

Constructs a new printer more info manufacturer attribute with the
specified

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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
info manufacturer attribute,

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

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

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

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterMoreInfoManufacturer

```java
public PrinterMoreInfoManufacturer​(
URI
uri)
```

Constructs a new printer more info manufacturer attribute with the
specified

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

PrinterMoreInfoManufacturer

```java
public PrinterMoreInfoManufacturer​(
URI
uri)
```

Constructs a new printer more info manufacturer attribute with the
specified

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

#### PrinterMoreInfoManufacturer

public PrinterMoreInfoManufacturer​(

URI

uri)

Constructs a new printer more info manufacturer attribute with the
specified

URI

.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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
info manufacturer attribute,

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

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

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

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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
info manufacturer attribute,

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

Returns whether this printer more info manufacturer attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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

PrinterMoreInfoManufacturer

.

This printer more info manufacturer attribute's

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

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

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

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

itself.

For class

PrinterMoreInfoManufacturer

, the category is class

PrinterMoreInfoManufacturer

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

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

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

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

.

For class

PrinterMoreInfoManufacturer

, the category name is

"printer-more-info-manufacturer"

.

---

