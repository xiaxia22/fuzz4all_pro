# Class PrinterURI

**Source:** `java.desktop\javax\print\attribute\standard\PrinterURI.html`

### Class Description

```java
public final class
PrinterURI

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterURI

is a printing attribute class, a

URI

, that
specifies the globally unique name of a printer. If it has such a name, an
administrator determines a printer's

URI

and sets this attribute to
that name.

IPP Compatibility:

This implements the IPP printer-uri attribute. The
string form returned by

toString()

gives the IPP printer-uri value.
The category name returned by

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

#### public PrinterURI​(
URI
uri)

Constructs a new

PrinterURI

attribute with the specified

URI

.

**Parameters:**
- uri

-

URI

of the printer

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

Returns whether this printer name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

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

is equivalent to this

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterURI

java.lang.Object

- javax.print.attribute.URISyntax
- - javax.print.attribute.standard.PrinterURI

javax.print.attribute.URISyntax

- javax.print.attribute.standard.PrinterURI

javax.print.attribute.standard.PrinterURI

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterURI

extends
URISyntax

implements
PrintServiceAttribute
```

Class

PrinterURI

is a printing attribute class, a

URI

, that
specifies the globally unique name of a printer. If it has such a name, an
administrator determines a printer's

URI

and sets this attribute to
that name.

IPP Compatibility:

This implements the IPP printer-uri attribute. The
string form returned by

toString()

gives the IPP printer-uri value.
The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterURI

extends

URISyntax

implements

PrintServiceAttribute

Class

PrinterURI

is a printing attribute class, a

URI

, that
specifies the globally unique name of a printer. If it has such a name, an
administrator determines a printer's

URI

and sets this attribute to
that name.

IPP Compatibility:

This implements the IPP printer-uri attribute. The
string form returned by

toString()

gives the IPP printer-uri value.
The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

This implements the IPP printer-uri attribute. The
string form returned by

toString()

gives the IPP printer-uri value.
The category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterURI

​(

URI

uri)

Constructs a new

PrinterURI

attribute with the specified

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

Returns whether this printer name attribute is equivalent to the passed
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

PrinterURI

​(

URI

uri)

Constructs a new

PrinterURI

attribute with the specified

URI

.

---

#### Constructor Summary

Constructs a new

PrinterURI

attribute with the specified

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

Returns whether this printer name attribute is equivalent to the passed
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

Returns whether this printer name attribute is equivalent to the passed
in object.

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

- PrinterURI

```java
public PrinterURI​(
URI
uri)
```

Constructs a new

PrinterURI

attribute with the specified

URI

.

**Parameters:** uri

-

URI

of the printer
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

Returns whether this printer name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

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

is equivalent to this

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterURI

```java
public PrinterURI​(
URI
uri)
```

Constructs a new

PrinterURI

attribute with the specified

URI

.

**Parameters:** uri

-

URI

of the printer
**Throws:** NullPointerException

- if

uri

is

null

---

#### Constructor Detail

PrinterURI

```java
public PrinterURI​(
URI
uri)
```

Constructs a new

PrinterURI

attribute with the specified

URI

.

**Parameters:** uri

-

URI

of the printer
**Throws:** NullPointerException

- if

uri

is

null

---

#### PrinterURI

public PrinterURI​(

URI

uri)

Constructs a new

PrinterURI

attribute with the specified

URI

.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

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

is equivalent to this

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

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

Returns whether this printer name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

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

is equivalent to this

PrinterURI

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

Returns whether this printer name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

URI

are equal.

object

is not

null

.

object

is an instance of class

PrinterURI

.

This

PrinterURI

attribute's underlying

URI

and

object

's underlying

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

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

itself.

For class

PrinterURI

and any vendor-defined subclasses, the
category is class

PrinterURI

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

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

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

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

.

For class

PrinterURI

and any vendor-defined subclasses, the
category name is

"printer-uri"

.

---

