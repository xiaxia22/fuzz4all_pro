# Class DocumentName

**Source:** `java.desktop\javax\print\attribute\standard\DocumentName.html`

### Class Description

```java
public final class
DocumentName

extends
TextSyntax

implements
DocAttribute
```

Class

DocumentName

is a printing attribute class, a text attribute,
that specifies the name of a document.

DocumentName

is an attribute
of the print data (the doc), not of the Print Job. A document's name is an
arbitrary string defined by the client. However if a JobName is not
specified, the

DocumentName

should be used instead, which implies
that supporting specification of

DocumentName

requires reporting of
JobName and vice versa. See

JobName

for more information.

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

DocAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocumentName​(
String
documentName,

Locale
locale)

Constructs a new document name attribute with the given document name and
locale.

**Parameters:**
- documentName

- document name
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

documentName

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this document name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

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

is equivalent to this document
name attribute,

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

DocumentName

, the category is class

DocumentName

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

DocumentName

, the category name is

"document-name"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class DocumentName

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.DocumentName

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.DocumentName

javax.print.attribute.standard.DocumentName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

```java
public final class
DocumentName

extends
TextSyntax

implements
DocAttribute
```

Class

DocumentName

is a printing attribute class, a text attribute,
that specifies the name of a document.

DocumentName

is an attribute
of the print data (the doc), not of the Print Job. A document's name is an
arbitrary string defined by the client. However if a JobName is not
specified, the

DocumentName

should be used instead, which implies
that supporting specification of

DocumentName

requires reporting of
JobName and vice versa. See

JobName

for more information.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

DocumentName

extends

TextSyntax

implements

DocAttribute

Class

DocumentName

is a printing attribute class, a text attribute,
that specifies the name of a document.

DocumentName

is an attribute
of the print data (the doc), not of the Print Job. A document's name is an
arbitrary string defined by the client. However if a JobName is not
specified, the

DocumentName

should be used instead, which implies
that supporting specification of

DocumentName

requires reporting of
JobName and vice versa. See

JobName

for more information.

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

DocumentName

​(

String

documentName,

Locale

locale)

Constructs a new document name attribute with the given document name and
locale.

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

Returns whether this document name attribute is equivalent to the passed
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

DocumentName

​(

String

documentName,

Locale

locale)

Constructs a new document name attribute with the given document name and
locale.

---

#### Constructor Summary

Constructs a new document name attribute with the given document name and
locale.

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

Returns whether this document name attribute is equivalent to the passed
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

Returns whether this document name attribute is equivalent to the passed
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

- DocumentName

```java
public DocumentName​(
String
documentName,

Locale
locale)
```

Constructs a new document name attribute with the given document name and
locale.

**Parameters:** documentName

- document name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

documentName

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

Returns whether this document name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

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

is equivalent to this document
name attribute,

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

DocumentName

, the category is class

DocumentName

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

DocumentName

, the category name is

"document-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- DocumentName

```java
public DocumentName​(
String
documentName,

Locale
locale)
```

Constructs a new document name attribute with the given document name and
locale.

**Parameters:** documentName

- document name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

documentName

is

null

---

#### Constructor Detail

DocumentName

```java
public DocumentName​(
String
documentName,

Locale
locale)
```

Constructs a new document name attribute with the given document name and
locale.

**Parameters:** documentName

- document name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

documentName

is

null

---

#### DocumentName

public DocumentName​(

String

documentName,

Locale

locale)

Constructs a new document name attribute with the given document name and
locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this document name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

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

is equivalent to this document
name attribute,

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

DocumentName

, the category is class

DocumentName

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

DocumentName

, the category name is

"document-name"

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

Returns whether this document name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

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

is equivalent to this document
name attribute,

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

Returns whether this document name attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

object

's locale
are equal.

object

is not

null

.

object

is an instance of class

DocumentName

.

This document name attribute's underlying string and

object

's underlying string are equal.

This document name attribute's locale and

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

DocumentName

, the category is class

DocumentName

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

DocumentName

, the category is class

DocumentName

itself.

For class

DocumentName

, the category is class

DocumentName

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

DocumentName

, the category name is

"document-name"

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

DocumentName

, the category name is

"document-name"

.

For class

DocumentName

, the category name is

"document-name"

.

---

