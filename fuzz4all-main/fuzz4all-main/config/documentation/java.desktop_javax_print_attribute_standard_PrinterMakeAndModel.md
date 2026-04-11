# Class PrinterMakeAndModel

**Source:** `java.desktop\javax\print\attribute\standard\PrinterMakeAndModel.html`

### Class Description

```java
public final class
PrinterMakeAndModel

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterMakeAndModel

is a printing attribute class, a text
attribute, that the make and model of the printer.

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

#### public PrinterMakeAndModel​(
String
makeAndModel,

Locale
locale)

Constructs a new printer make and model attribute with the given make and
model string and locale.

**Parameters:**
- makeAndModel

- printer make and model string
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

makeAndModel

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this printer make and model attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

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

is equivalent to this printer make
and model attribute,

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

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

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

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterMakeAndModel

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.PrinterMakeAndModel

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.PrinterMakeAndModel

javax.print.attribute.standard.PrinterMakeAndModel

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterMakeAndModel

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterMakeAndModel

is a printing attribute class, a text
attribute, that the make and model of the printer.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterMakeAndModel

extends

TextSyntax

implements

PrintServiceAttribute

Class

PrinterMakeAndModel

is a printing attribute class, a text
attribute, that the make and model of the printer.

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

PrinterMakeAndModel

​(

String

makeAndModel,

Locale

locale)

Constructs a new printer make and model attribute with the given make and
model string and locale.

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

Returns whether this printer make and model attribute is equivalent to
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

PrinterMakeAndModel

​(

String

makeAndModel,

Locale

locale)

Constructs a new printer make and model attribute with the given make and
model string and locale.

---

#### Constructor Summary

Constructs a new printer make and model attribute with the given make and
model string and locale.

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

Returns whether this printer make and model attribute is equivalent to
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

Returns whether this printer make and model attribute is equivalent to
the passed in object.

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

- PrinterMakeAndModel

```java
public PrinterMakeAndModel​(
String
makeAndModel,

Locale
locale)
```

Constructs a new printer make and model attribute with the given make and
model string and locale.

**Parameters:** makeAndModel

- printer make and model string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

makeAndModel

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

Returns whether this printer make and model attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

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

is equivalent to this printer make
and model attribute,

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

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

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

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterMakeAndModel

```java
public PrinterMakeAndModel​(
String
makeAndModel,

Locale
locale)
```

Constructs a new printer make and model attribute with the given make and
model string and locale.

**Parameters:** makeAndModel

- printer make and model string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

makeAndModel

is

null

---

#### Constructor Detail

PrinterMakeAndModel

```java
public PrinterMakeAndModel​(
String
makeAndModel,

Locale
locale)
```

Constructs a new printer make and model attribute with the given make and
model string and locale.

**Parameters:** makeAndModel

- printer make and model string
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

makeAndModel

is

null

---

#### PrinterMakeAndModel

public PrinterMakeAndModel​(

String

makeAndModel,

Locale

locale)

Constructs a new printer make and model attribute with the given make and
model string and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer make and model attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

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

is equivalent to this printer make
and model attribute,

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

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

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

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

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

Returns whether this printer make and model attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

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

is equivalent to this printer make
and model attribute,

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

Returns whether this printer make and model attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

object

is not

null

.

object

is an instance of class

PrinterMakeAndModel

.

This printer make and model attribute's underlying string and

object

's underlying string are equal.

This printer make and model attribute's locale and

object

's
locale are equal.

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

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

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

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

itself.

For class

PrinterMakeAndModel

, the category is class

PrinterMakeAndModel

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

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

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

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

.

For class

PrinterMakeAndModel

, the category name is

"printer-make-and-model"

.

---

