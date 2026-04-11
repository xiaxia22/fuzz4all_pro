# Class PrinterName

**Source:** `java.desktop\javax\print\attribute\standard\PrinterName.html`

### Class Description

```java
public final class
PrinterName

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterName

is a printing attribute class, a text attribute,
that specifies the name of a printer. It is a name that is more end-user
friendly than a

URI

. An administrator determines a printer's name and
sets this attribute to that name. This name may be the last part of the
printer's

URI

or it may be unrelated. In non-US-English locales, a
name may contain characters that are not allowed in a

URI

.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

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

#### public PrinterName​(
String
printerName,

Locale
locale)

Constructs a new printer name attribute with the given name and locale.

**Parameters:**
- printerName

- printer name
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

printerName

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

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
are equal.

**Overrides:**
- equals

in class

TextSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this printer name
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

PrinterName

, the category is class

PrinterName

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

PrinterName

, the category name is

"printer-name"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterName

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.PrinterName

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.PrinterName

javax.print.attribute.standard.PrinterName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterName

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterName

is a printing attribute class, a text attribute,
that specifies the name of a printer. It is a name that is more end-user
friendly than a

URI

. An administrator determines a printer's name and
sets this attribute to that name. This name may be the last part of the
printer's

URI

or it may be unrelated. In non-US-English locales, a
name may contain characters that are not allowed in a

URI

.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterName

extends

TextSyntax

implements

PrintServiceAttribute

Class

PrinterName

is a printing attribute class, a text attribute,
that specifies the name of a printer. It is a name that is more end-user
friendly than a

URI

. An administrator determines a printer's name and
sets this attribute to that name. This name may be the last part of the
printer's

URI

or it may be unrelated. In non-US-English locales, a
name may contain characters that are not allowed in a

URI

.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterName

​(

String

printerName,

Locale

locale)

Constructs a new printer name attribute with the given name and locale.

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

TextSyntax

getLocale

,

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

PrinterName

​(

String

printerName,

Locale

locale)

Constructs a new printer name attribute with the given name and locale.

---

#### Constructor Summary

Constructs a new printer name attribute with the given name and locale.

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

TextSyntax

getLocale

,

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

Returns whether this printer name attribute is equivalent to the passed
in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

TextSyntax

getLocale

,

getValue

,

hashCode

,

toString

---

#### Methods declared in class javax.print.attribute. TextSyntax

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

- PrinterName

```java
public PrinterName​(
String
printerName,

Locale
locale)
```

Constructs a new printer name attribute with the given name and locale.

**Parameters:** printerName

- printer name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

printerName

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

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
are equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer name
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

PrinterName

, the category is class

PrinterName

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

PrinterName

, the category name is

"printer-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterName

```java
public PrinterName​(
String
printerName,

Locale
locale)
```

Constructs a new printer name attribute with the given name and locale.

**Parameters:** printerName

- printer name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

printerName

is

null

---

#### Constructor Detail

PrinterName

```java
public PrinterName​(
String
printerName,

Locale
locale)
```

Constructs a new printer name attribute with the given name and locale.

**Parameters:** printerName

- printer name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

printerName

is

null

---

#### PrinterName

public PrinterName​(

String

printerName,

Locale

locale)

Constructs a new printer name attribute with the given name and locale.

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

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
are equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer name
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

PrinterName

, the category is class

PrinterName

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

PrinterName

, the category name is

"printer-name"

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

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
are equal.

**Overrides:** equals

in class

TextSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer name
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

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
are equal.

object

is not

null

.

object

is an instance of class

PrinterName

.

This printer name attribute's underlying string and

object

's underlying string are equal.

This printer name attribute's locale and

object

's locale
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

PrinterName

, the category is class

PrinterName

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

PrinterName

, the category is class

PrinterName

itself.

For class

PrinterName

, the category is class

PrinterName

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

PrinterName

, the category name is

"printer-name"

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

PrinterName

, the category name is

"printer-name"

.

For class

PrinterName

, the category name is

"printer-name"

.

---

