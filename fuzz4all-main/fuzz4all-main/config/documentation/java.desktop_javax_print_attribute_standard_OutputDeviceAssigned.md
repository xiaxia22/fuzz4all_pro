# Class OutputDeviceAssigned

**Source:** `java.desktop\javax\print\attribute\standard\OutputDeviceAssigned.html`

### Class Description

```java
public final class
OutputDeviceAssigned

extends
TextSyntax

implements
PrintJobAttribute
```

Class

OutputDeviceAssigned

is a printing attribute class, a text
attribute, that identifies the output device to which the service has
assigned this job. If an output device implements an embedded Print Service
instance, the printer need not set this attribute. If a print server
implements a Print Service instance, the value may be empty (zero- length
string) or not returned until the service assigns an output device to the
job. This attribute is particularly useful when a single service supports
multiple devices (so called "fan-out").

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

#### public OutputDeviceAssigned​(
String
deviceName,

Locale
locale)

Constructs a new output device assigned attribute with the given device
name and locale.

**Parameters:**
- deviceName

- device name
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

deviceName

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this output device assigned attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

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

is equivalent to this output
device assigned attribute,

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

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

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

OutputDeviceAssigned

, the category name is

"output-device-assigned"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class OutputDeviceAssigned

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.OutputDeviceAssigned

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.OutputDeviceAssigned

javax.print.attribute.standard.OutputDeviceAssigned

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

```java
public final class
OutputDeviceAssigned

extends
TextSyntax

implements
PrintJobAttribute
```

Class

OutputDeviceAssigned

is a printing attribute class, a text
attribute, that identifies the output device to which the service has
assigned this job. If an output device implements an embedded Print Service
instance, the printer need not set this attribute. If a print server
implements a Print Service instance, the value may be empty (zero- length
string) or not returned until the service assigns an output device to the
job. This attribute is particularly useful when a single service supports
multiple devices (so called "fan-out").

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

OutputDeviceAssigned

extends

TextSyntax

implements

PrintJobAttribute

Class

OutputDeviceAssigned

is a printing attribute class, a text
attribute, that identifies the output device to which the service has
assigned this job. If an output device implements an embedded Print Service
instance, the printer need not set this attribute. If a print server
implements a Print Service instance, the value may be empty (zero- length
string) or not returned until the service assigns an output device to the
job. This attribute is particularly useful when a single service supports
multiple devices (so called "fan-out").

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

OutputDeviceAssigned

​(

String

deviceName,

Locale

locale)

Constructs a new output device assigned attribute with the given device
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

Returns whether this output device assigned attribute is equivalent to
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

OutputDeviceAssigned

​(

String

deviceName,

Locale

locale)

Constructs a new output device assigned attribute with the given device
name and locale.

---

#### Constructor Summary

Constructs a new output device assigned attribute with the given device
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

Returns whether this output device assigned attribute is equivalent to
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

Returns whether this output device assigned attribute is equivalent to
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

- OutputDeviceAssigned

```java
public OutputDeviceAssigned​(
String
deviceName,

Locale
locale)
```

Constructs a new output device assigned attribute with the given device
name and locale.

**Parameters:** deviceName

- device name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

deviceName

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

Returns whether this output device assigned attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

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

is equivalent to this output
device assigned attribute,

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

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

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

OutputDeviceAssigned

, the category name is

"output-device-assigned"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- OutputDeviceAssigned

```java
public OutputDeviceAssigned​(
String
deviceName,

Locale
locale)
```

Constructs a new output device assigned attribute with the given device
name and locale.

**Parameters:** deviceName

- device name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

deviceName

is

null

---

#### Constructor Detail

OutputDeviceAssigned

```java
public OutputDeviceAssigned​(
String
deviceName,

Locale
locale)
```

Constructs a new output device assigned attribute with the given device
name and locale.

**Parameters:** deviceName

- device name
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

deviceName

is

null

---

#### OutputDeviceAssigned

public OutputDeviceAssigned​(

String

deviceName,

Locale

locale)

Constructs a new output device assigned attribute with the given device
name and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this output device assigned attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

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

is equivalent to this output
device assigned attribute,

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

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

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

OutputDeviceAssigned

, the category name is

"output-device-assigned"

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

Returns whether this output device assigned attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

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

is equivalent to this output
device assigned attribute,

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

Returns whether this output device assigned attribute is equivalent to
the passed in object. To be equivalent, all of the following conditions
must be true:

- object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

object

's
locale are equal.

object

is not

null

.

object

is an instance of class

OutputDeviceAssigned

.

This output device assigned attribute's underlying string and

object

's underlying string are equal.

This output device assigned attribute's locale and

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

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

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

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

itself.

For class

OutputDeviceAssigned

, the category is class

OutputDeviceAssigned

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

OutputDeviceAssigned

, the category name is

"output-device-assigned"

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

OutputDeviceAssigned

, the category name is

"output-device-assigned"

.

For class

OutputDeviceAssigned

, the category name is

"output-device-assigned"

.

---

