# Class RequestingUserName

**Source:** `java.desktop\javax\print\attribute\standard\RequestingUserName.html`

### Class Description

```java
public final class
RequestingUserName

extends
TextSyntax

implements
PrintRequestAttribute
```

Class

RequestingUserName

is a printing attribute class, a text
attribute, that specifies the name of the end user that submitted the print
job. A requesting user name is an arbitrary string defined by the client. The
printer does not put the client-specified

RequestingUserName

attribute into the Print Job's attribute set; rather, the printer puts in a

JobOriginatingUserName

attribute. This means
that services which support specifying a username with this attribute should
also report a

JobOriginatingUserName

in the job's attribute set. Note
that many print services may have a way to independently authenticate the
user name, and so may state support for a requesting user name, but in
practice will then report the user name authenticated by the service rather
than that specified via this attribute.

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

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public RequestingUserName​(
String
userName,

Locale
locale)

Constructs a new requesting user name attribute with the given user name
and locale.

**Parameters:**
- userName

- user name
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

userName

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this requesting user name attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

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

is equivalent to this requesting
user name attribute,

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

RequestingUserName

, the category is class

RequestingUserName

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

RequestingUserName

, the category name is

"requesting-user-name"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class RequestingUserName

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.RequestingUserName

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.RequestingUserName

javax.print.attribute.standard.RequestingUserName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintRequestAttribute

```java
public final class
RequestingUserName

extends
TextSyntax

implements
PrintRequestAttribute
```

Class

RequestingUserName

is a printing attribute class, a text
attribute, that specifies the name of the end user that submitted the print
job. A requesting user name is an arbitrary string defined by the client. The
printer does not put the client-specified

RequestingUserName

attribute into the Print Job's attribute set; rather, the printer puts in a

JobOriginatingUserName

attribute. This means
that services which support specifying a username with this attribute should
also report a

JobOriginatingUserName

in the job's attribute set. Note
that many print services may have a way to independently authenticate the
user name, and so may state support for a requesting user name, but in
practice will then report the user name authenticated by the service rather
than that specified via this attribute.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

RequestingUserName

extends

TextSyntax

implements

PrintRequestAttribute

Class

RequestingUserName

is a printing attribute class, a text
attribute, that specifies the name of the end user that submitted the print
job. A requesting user name is an arbitrary string defined by the client. The
printer does not put the client-specified

RequestingUserName

attribute into the Print Job's attribute set; rather, the printer puts in a

JobOriginatingUserName

attribute. This means
that services which support specifying a username with this attribute should
also report a

JobOriginatingUserName

in the job's attribute set. Note
that many print services may have a way to independently authenticate the
user name, and so may state support for a requesting user name, but in
practice will then report the user name authenticated by the service rather
than that specified via this attribute.

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

RequestingUserName

​(

String

userName,

Locale

locale)

Constructs a new requesting user name attribute with the given user name
and locale.

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

Returns whether this requesting user name attribute is equivalent to the
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

RequestingUserName

​(

String

userName,

Locale

locale)

Constructs a new requesting user name attribute with the given user name
and locale.

---

#### Constructor Summary

Constructs a new requesting user name attribute with the given user name
and locale.

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

Returns whether this requesting user name attribute is equivalent to the
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

Returns whether this requesting user name attribute is equivalent to the
passed in object.

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

- RequestingUserName

```java
public RequestingUserName​(
String
userName,

Locale
locale)
```

Constructs a new requesting user name attribute with the given user name
and locale.

**Parameters:** userName

- user name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

userName

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

Returns whether this requesting user name attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

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

is equivalent to this requesting
user name attribute,

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

RequestingUserName

, the category is class

RequestingUserName

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

RequestingUserName

, the category name is

"requesting-user-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- RequestingUserName

```java
public RequestingUserName​(
String
userName,

Locale
locale)
```

Constructs a new requesting user name attribute with the given user name
and locale.

**Parameters:** userName

- user name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

userName

is

null

---

#### Constructor Detail

RequestingUserName

```java
public RequestingUserName​(
String
userName,

Locale
locale)
```

Constructs a new requesting user name attribute with the given user name
and locale.

**Parameters:** userName

- user name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

userName

is

null

---

#### RequestingUserName

public RequestingUserName​(

String

userName,

Locale

locale)

Constructs a new requesting user name attribute with the given user name
and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this requesting user name attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

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

is equivalent to this requesting
user name attribute,

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

RequestingUserName

, the category is class

RequestingUserName

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

RequestingUserName

, the category name is

"requesting-user-name"

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

Returns whether this requesting user name attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

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

is equivalent to this requesting
user name attribute,

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

Returns whether this requesting user name attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

object

's
locale are equal.

object

is not

null

.

object

is an instance of class

RequestingUserName

.

This requesting user name attribute's underlying string and

object

's underlying string are equal.

This requesting user name attribute's locale and

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

RequestingUserName

, the category is class

RequestingUserName

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

RequestingUserName

, the category is class

RequestingUserName

itself.

For class

RequestingUserName

, the category is class

RequestingUserName

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

RequestingUserName

, the category name is

"requesting-user-name"

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

RequestingUserName

, the category name is

"requesting-user-name"

.

For class

RequestingUserName

, the category name is

"requesting-user-name"

.

---

