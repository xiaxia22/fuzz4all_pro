# Class PrinterMessageFromOperator

**Source:** `java.desktop\javax\print\attribute\standard\PrinterMessageFromOperator.html`

### Class Description

```java
public final class
PrinterMessageFromOperator

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterMessageFromOperator

is a printing attribute class, a
text attribute, that provides a message from an operator, system
administrator, or "intelligent" process to indicate to the end user
information about or status of the printer, such as why it is unavailable or
when it is expected to be available.

A Print Service's attribute set includes zero instances or one instance of a

PrinterMessageFromOperator

attribute, not more than one instance. A
new

PrinterMessageFromOperator

attribute replaces an existing

PrinterMessageFromOperator

attribute, if any. In other words,

PrinterMessageFromOperator

is not intended to be a history log. If it
wishes, the client can detect changes to a Print Service's

PrinterMessageFromOperator

attribute and maintain the client's own
history log of the

PrinterMessageFromOperator

attribute values.

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

#### public PrinterMessageFromOperator​(
String
message,

Locale
locale)

Constructs a new printer message from operator attribute with the given
message and locale.

**Parameters:**
- message

- the message
- locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()

**Throws:**
- NullPointerException

- if

message

is

null

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this printer message from operator attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

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

is equivalent to this printer
message from operator attribute,

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

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

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

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterMessageFromOperator

java.lang.Object

- javax.print.attribute.TextSyntax
- - javax.print.attribute.standard.PrinterMessageFromOperator

javax.print.attribute.TextSyntax

- javax.print.attribute.standard.PrinterMessageFromOperator

javax.print.attribute.standard.PrinterMessageFromOperator

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterMessageFromOperator

extends
TextSyntax

implements
PrintServiceAttribute
```

Class

PrinterMessageFromOperator

is a printing attribute class, a
text attribute, that provides a message from an operator, system
administrator, or "intelligent" process to indicate to the end user
information about or status of the printer, such as why it is unavailable or
when it is expected to be available.

A Print Service's attribute set includes zero instances or one instance of a

PrinterMessageFromOperator

attribute, not more than one instance. A
new

PrinterMessageFromOperator

attribute replaces an existing

PrinterMessageFromOperator

attribute, if any. In other words,

PrinterMessageFromOperator

is not intended to be a history log. If it
wishes, the client can detect changes to a Print Service's

PrinterMessageFromOperator

attribute and maintain the client's own
history log of the

PrinterMessageFromOperator

attribute values.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterMessageFromOperator

extends

TextSyntax

implements

PrintServiceAttribute

Class

PrinterMessageFromOperator

is a printing attribute class, a
text attribute, that provides a message from an operator, system
administrator, or "intelligent" process to indicate to the end user
information about or status of the printer, such as why it is unavailable or
when it is expected to be available.

A Print Service's attribute set includes zero instances or one instance of a

PrinterMessageFromOperator

attribute, not more than one instance. A
new

PrinterMessageFromOperator

attribute replaces an existing

PrinterMessageFromOperator

attribute, if any. In other words,

PrinterMessageFromOperator

is not intended to be a history log. If it
wishes, the client can detect changes to a Print Service's

PrinterMessageFromOperator

attribute and maintain the client's own
history log of the

PrinterMessageFromOperator

attribute values.

IPP Compatibility:

The string value gives the IPP name value. The
locale gives the IPP natural language. The category name returned by

getName()

gives the IPP attribute name.

A Print Service's attribute set includes zero instances or one instance of a

PrinterMessageFromOperator

attribute, not more than one instance. A
new

PrinterMessageFromOperator

attribute replaces an existing

PrinterMessageFromOperator

attribute, if any. In other words,

PrinterMessageFromOperator

is not intended to be a history log. If it
wishes, the client can detect changes to a Print Service's

PrinterMessageFromOperator

attribute and maintain the client's own
history log of the

PrinterMessageFromOperator

attribute values.

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

PrinterMessageFromOperator

​(

String

message,

Locale

locale)

Constructs a new printer message from operator attribute with the given
message and locale.

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

Returns whether this printer message from operator attribute is
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

PrinterMessageFromOperator

​(

String

message,

Locale

locale)

Constructs a new printer message from operator attribute with the given
message and locale.

---

#### Constructor Summary

Constructs a new printer message from operator attribute with the given
message and locale.

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

Returns whether this printer message from operator attribute is
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

Returns whether this printer message from operator attribute is
equivalent to the passed in object.

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

- PrinterMessageFromOperator

```java
public PrinterMessageFromOperator​(
String
message,

Locale
locale)
```

Constructs a new printer message from operator attribute with the given
message and locale.

**Parameters:** message

- the message
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

message

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

Returns whether this printer message from operator attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

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

is equivalent to this printer
message from operator attribute,

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

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

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

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterMessageFromOperator

```java
public PrinterMessageFromOperator​(
String
message,

Locale
locale)
```

Constructs a new printer message from operator attribute with the given
message and locale.

**Parameters:** message

- the message
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

message

is

null

---

#### Constructor Detail

PrinterMessageFromOperator

```java
public PrinterMessageFromOperator​(
String
message,

Locale
locale)
```

Constructs a new printer message from operator attribute with the given
message and locale.

**Parameters:** message

- the message
**Parameters:** locale

- natural language of the text string.

null

is
interpreted to mean the default locale as returned by

Locale.getDefault()
**Throws:** NullPointerException

- if

message

is

null

---

#### PrinterMessageFromOperator

public PrinterMessageFromOperator​(

String

message,

Locale

locale)

Constructs a new printer message from operator attribute with the given
message and locale.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer message from operator attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

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

is equivalent to this printer
message from operator attribute,

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

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

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

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

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

Returns whether this printer message from operator attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

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

is equivalent to this printer
message from operator attribute,

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

Returns whether this printer message from operator attribute is
equivalent to the passed in object. To be equivalent, all of the
following conditions must be true:

- object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

object

's locale are equal.

object

is not

null

.

object

is an instance of class

PrinterMessageFromOperator

.

This printer message from operator attribute's underlying string
and

object

's underlying string are equal.

This printer message from operator attribute's locale and

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

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

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

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

itself.

For class

PrinterMessageFromOperator

, the category is class

PrinterMessageFromOperator

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

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

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

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

.

For class

PrinterMessageFromOperator

, the category name is

"printer-message-from-operator"

.

---

