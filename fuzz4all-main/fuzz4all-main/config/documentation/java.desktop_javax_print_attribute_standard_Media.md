# Class Media

**Source:** `java.desktop\javax\print\attribute\standard\Media.html`

### Class Description

```java
public abstract class
Media

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Media

is a printing attribute class that specifies the medium
on which to print.

Media may be specified in different ways.

- it may be specified by paper source - eg paper tray

it may be specified by a standard size - eg "A4"

it may be specified by a name - eg "letterhead"

Each of these corresponds to the IPP "media" attribute. The current API does
not support describing media by characteristics (eg colour, opacity). This
may be supported in a later revision of the specification.

A

Media

object is constructed with a value which represents one of
the ways in which the Media attribute can be specified.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Media​(int value)

Constructs a new media attribute specified by name.

**Parameters:**
- value

- a value

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this media attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this media
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

Media

and any vendor-defined subclasses, the category
is class

Media

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

Media

and any vendor-defined subclasses, the category
name is

"media"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Media

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Media

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Media

javax.print.attribute.standard.Media

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

**Direct Known Subclasses:** MediaName

,

MediaSizeName

,

MediaTray

```java
public abstract class
Media

extends
EnumSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

Media

is a printing attribute class that specifies the medium
on which to print.

Media may be specified in different ways.

- it may be specified by paper source - eg paper tray

it may be specified by a standard size - eg "A4"

it may be specified by a name - eg "letterhead"

Each of these corresponds to the IPP "media" attribute. The current API does
not support describing media by characteristics (eg colour, opacity). This
may be supported in a later revision of the specification.

A

Media

object is constructed with a value which represents one of
the ways in which the Media attribute can be specified.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public abstract class

Media

extends

EnumSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

Media

is a printing attribute class that specifies the medium
on which to print.

Media may be specified in different ways.

- it may be specified by paper source - eg paper tray

it may be specified by a standard size - eg "A4"

it may be specified by a name - eg "letterhead"

Each of these corresponds to the IPP "media" attribute. The current API does
not support describing media by characteristics (eg colour, opacity). This
may be supported in a later revision of the specification.

A

Media

object is constructed with a value which represents one of
the ways in which the Media attribute can be specified.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

Media may be specified in different ways.

- it may be specified by paper source - eg paper tray

it may be specified by a standard size - eg "A4"

it may be specified by a name - eg "letterhead"

Each of these corresponds to the IPP "media" attribute. The current API does
not support describing media by characteristics (eg colour, opacity). This
may be supported in a later revision of the specification.

A

Media

object is constructed with a value which represents one of
the ways in which the Media attribute can be specified.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

it may be specified by paper source - eg paper tray

it may be specified by a standard size - eg "A4"

it may be specified by a name - eg "letterhead"

A

Media

object is constructed with a value which represents one of
the ways in which the Media attribute can be specified.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Media

​(int value)

Constructs a new media attribute specified by name.

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

Returns whether this media attribute is equivalent to the passed in
object.

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

EnumSyntax

clone

,

getEnumValueTable

,

getOffset

,

getStringTable

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

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

Modifier

Constructor

Description

protected

Media

​(int value)

Constructs a new media attribute specified by name.

---

#### Constructor Summary

Constructs a new media attribute specified by name.

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

Returns whether this media attribute is equivalent to the passed in
object.

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

EnumSyntax

clone

,

getEnumValueTable

,

getOffset

,

getStringTable

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

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

Returns whether this media attribute is equivalent to the passed in
object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getEnumValueTable

,

getOffset

,

getStringTable

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

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

- Media

```java
protected Media​(int value)
```

Constructs a new media attribute specified by name.

**Parameters:** value

- a value

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media
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

Media

and any vendor-defined subclasses, the category
is class

Media

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

Media

and any vendor-defined subclasses, the category
name is

"media"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- Media

```java
protected Media​(int value)
```

Constructs a new media attribute specified by name.

**Parameters:** value

- a value

---

#### Constructor Detail

Media

```java
protected Media​(int value)
```

Constructs a new media attribute specified by name.

**Parameters:** value

- a value

---

#### Media

protected Media​(int value)

Constructs a new media attribute specified by name.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media
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

Media

and any vendor-defined subclasses, the category
is class

Media

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

Media

and any vendor-defined subclasses, the category
name is

"media"

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

Returns whether this media attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

**Overrides:** equals

in class

Object
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media
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

Returns whether this media attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

object

is not

null

.

object

is of the same subclass of

Media

as this
object.

The values are equal.

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

Media

and any vendor-defined subclasses, the category
is class

Media

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

Media

and any vendor-defined subclasses, the category
is class

Media

itself.

For class

Media

and any vendor-defined subclasses, the category
is class

Media

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

Media

and any vendor-defined subclasses, the category
name is

"media"

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

Media

and any vendor-defined subclasses, the category
name is

"media"

.

For class

Media

and any vendor-defined subclasses, the category
name is

"media"

.

---

