# Class JobOriginatingUserName

**Source:** `java.desktop\javax\print\attribute\standard\JobOriginatingUserName.html`

### Class Description

```java
public final class
JobOriginatingUserName

extends
TextSyntax

implements
PrintJobAttribute
```

Class

JobOriginatingUserName

is a printing attribute class, a text
attribute, that contains the name of the end user that submitted the print
job. If possible, the printer sets this attribute to the most authenticated
printable user name that it can obtain from the authentication service that
authenticated the submitted Print Request. If such is not available, the
printer uses the value of the

RequestingUserName

attribute supplied by the client in the Print Request's attribute set. If no
authentication service is available, and the client did not supply a

RequestingUserName

attribute, the printer sets the
JobOriginatingUserName attribute to an empty (zero-length) string.

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

PrintJobAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public JobOriginatingUserName​(
String
userName,

Locale
locale)

Constructs a new job originating user name attribute with the given user
name and locale.

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

Returns whether this job originating user name attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

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

is equivalent to this job
originating user name attribute,

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

JobOriginatingUserName

, the category is class

JobOriginatingUserName

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

JobOriginatingUserName

, the category name is

"job-originating-user-name"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobOriginatingUserName

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.JobOriginatingUserName

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.JobOriginatingUserName

javax.print.attribute.standard.JobOriginatingUserName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
JobOriginatingUserName

extends
TextSyntax

implements
PrintJobAttribute
```

Class

JobOriginatingUserName

is a printing attribute class, a text
attribute, that contains the name of the end user that submitted the print
job. If possible, the printer sets this attribute to the most authenticated
printable user name that it can obtain from the authentication service that
authenticated the submitted Print Request. If such is not available, the
printer uses the value of the

RequestingUserName

attribute supplied by the client in the Print Request's attribute set. If no
authentication service is available, and the client did not supply a

RequestingUserName

attribute, the printer sets the
JobOriginatingUserName attribute to an empty (zero-length) string.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

JobOriginatingUserName

extends

TextSyntax

implements

PrintJobAttribute

Class

JobOriginatingUserName

is a printing attribute class, a text
attribute, that contains the name of the end user that submitted the print
job. If possible, the printer sets this attribute to the most authenticated
printable user name that it can obtain from the authentication service that
authenticated the submitted Print Request. If such is not available, the
printer uses the value of the

RequestingUserName

attribute supplied by the client in the Print Request's attribute set. If no
authentication service is available, and the client did not supply a

RequestingUserName

attribute, the printer sets the
JobOriginatingUserName attribute to an empty (zero-length) string.

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

JobOriginatingUserName

​(

String

userName,

Locale

locale)

Constructs a new job originating user name attribute with the given user
name and locale.

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

Returns whether this job originating user name attribute is equivalent to
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

JobOriginatingUserName

​(

String

userName,

Locale

locale)

Constructs a new job originating user name attribute with the given user
name and locale.

---

#### Constructor Summary

Constructs a new job originating user name attribute with the given user
name and locale.

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

Returns whether this job originating user name attribute is equivalent to
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

Returns whether this job originating user name attribute is equivalent to
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

- JobOriginatingUserName

```java
public JobOriginatingUserName​(
String
userName,

Locale
locale)
```

Constructs a new job originating user name attribute with the given user
name and locale.

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

Returns whether this job originating user name attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

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

is equivalent to this job
originating user name attribute,

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

JobOriginatingUserName

, the category is class

JobOriginatingUserName

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

JobOriginatingUserName

, the category name is

"job-originating-user-name"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- JobOriginatingUserName

```java
public JobOriginatingUserName​(
String
userName,

Locale
locale)
```

Constructs a new job originating user name attribute with the given user
name and locale.

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

JobOriginatingUserName

```java
public JobOriginatingUserName​(
String
userName,

Locale
locale)
```

Constructs a new job originating user name attribute with the given user
name and locale.

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

#### JobOriginatingUserName

public JobOriginatingUserName​(

String

userName,

Locale

locale)

Constructs a new job originating user name attribute with the given user
name and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this job originating user name attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

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

is equivalent to this job
originating user name attribute,

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

JobOriginatingUserName

, the category is class

JobOriginatingUserName

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

JobOriginatingUserName

, the category name is

"job-originating-user-name"

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

Returns whether this job originating user name attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

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

is equivalent to this job
originating user name attribute,

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

Returns whether this job originating user name attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

object

is not

null

.

object

is an instance of class

JobOriginatingUserName

.

This job originating user name attribute's underlying string and

object

's underlying string are equal.

This job originating user name attribute's locale and

object

's locale are equal.

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

JobOriginatingUserName

, the category is class

JobOriginatingUserName

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

JobOriginatingUserName

, the category is class

JobOriginatingUserName

itself.

For class

JobOriginatingUserName

, the category is class

JobOriginatingUserName

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

JobOriginatingUserName

, the category name is

"job-originating-user-name"

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

JobOriginatingUserName

, the category name is

"job-originating-user-name"

.

For class

JobOriginatingUserName

, the category name is

"job-originating-user-name"

.

---

