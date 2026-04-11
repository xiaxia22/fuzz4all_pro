# Class Destination

**Source:** `java.desktop\javax\print\attribute\standard\Destination.html`

### Class Description

```java
public final class
Destination

extends
URISyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

Destination

is a printing attribute class, a

URI

, that
is used to indicate an alternate destination for the spooled printer
formatted data. Many

PrintServices

will not support the notion of a
destination other than the printer device, and so will not support this
attribute.

A common use for this attribute will be applications which want to redirect
output to a local disk file : eg."file:out.prn". Note that proper
construction of "file:" scheme

URI

instances should be performed
using the

toURI()

method of class

File

. See the
documentation on that class for more information.

If a destination

URI

is specified in a PrintRequest and it is not
accessible for output by the

PrintService

, a

PrintException

will be thrown. The

PrintException

may implement

URIException

to provide a more specific cause.

IPP Compatibility:

Destination is not an IPP attribute.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public Destination​(
URI
uri)

Constructs a new destination attribute with the specified

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

Returns whether this destination attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Destination

.

This destination attribute's

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

is equivalent to this destination
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

Destination

, the category is class

Destination

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

Destination

, the category name is

"spool-data-destination"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Destination

java.lang.Object

- javax.print.attribute.URISyntax
- - javax.print.attribute.standard.Destination

javax.print.attribute.URISyntax

- javax.print.attribute.standard.Destination

javax.print.attribute.standard.Destination

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
Destination

extends
URISyntax

implements
PrintJobAttribute
,
PrintRequestAttribute
```

Class

Destination

is a printing attribute class, a

URI

, that
is used to indicate an alternate destination for the spooled printer
formatted data. Many

PrintServices

will not support the notion of a
destination other than the printer device, and so will not support this
attribute.

A common use for this attribute will be applications which want to redirect
output to a local disk file : eg."file:out.prn". Note that proper
construction of "file:" scheme

URI

instances should be performed
using the

toURI()

method of class

File

. See the
documentation on that class for more information.

If a destination

URI

is specified in a PrintRequest and it is not
accessible for output by the

PrintService

, a

PrintException

will be thrown. The

PrintException

may implement

URIException

to provide a more specific cause.

IPP Compatibility:

Destination is not an IPP attribute.

**See Also:** Serialized Form

public final class

Destination

extends

URISyntax

implements

PrintJobAttribute

,

PrintRequestAttribute

Class

Destination

is a printing attribute class, a

URI

, that
is used to indicate an alternate destination for the spooled printer
formatted data. Many

PrintServices

will not support the notion of a
destination other than the printer device, and so will not support this
attribute.

A common use for this attribute will be applications which want to redirect
output to a local disk file : eg."file:out.prn". Note that proper
construction of "file:" scheme

URI

instances should be performed
using the

toURI()

method of class

File

. See the
documentation on that class for more information.

If a destination

URI

is specified in a PrintRequest and it is not
accessible for output by the

PrintService

, a

PrintException

will be thrown. The

PrintException

may implement

URIException

to provide a more specific cause.

IPP Compatibility:

Destination is not an IPP attribute.

A common use for this attribute will be applications which want to redirect
output to a local disk file : eg."file:out.prn". Note that proper
construction of "file:" scheme

URI

instances should be performed
using the

toURI()

method of class

File

. See the
documentation on that class for more information.

If a destination

URI

is specified in a PrintRequest and it is not
accessible for output by the

PrintService

, a

PrintException

will be thrown. The

PrintException

may implement

URIException

to provide a more specific cause.

IPP Compatibility:

Destination is not an IPP attribute.

If a destination

URI

is specified in a PrintRequest and it is not
accessible for output by the

PrintService

, a

PrintException

will be thrown. The

PrintException

may implement

URIException

to provide a more specific cause.

IPP Compatibility:

Destination is not an IPP attribute.

IPP Compatibility:

Destination is not an IPP attribute.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Destination

​(

URI

uri)

Constructs a new destination attribute with the specified

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

Returns whether this destination attribute is equivalent to the passed in
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

Destination

​(

URI

uri)

Constructs a new destination attribute with the specified

URI

.

---

#### Constructor Summary

Constructs a new destination attribute with the specified

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

Returns whether this destination attribute is equivalent to the passed in
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

Returns whether this destination attribute is equivalent to the passed in
object.

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

- Destination

```java
public Destination​(
URI
uri)
```

Constructs a new destination attribute with the specified

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

Returns whether this destination attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Destination

.

This destination attribute's

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

is equivalent to this destination
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

Destination

, the category is class

Destination

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

Destination

, the category name is

"spool-data-destination"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- Destination

```java
public Destination​(
URI
uri)
```

Constructs a new destination attribute with the specified

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

Destination

```java
public Destination​(
URI
uri)
```

Constructs a new destination attribute with the specified

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

#### Destination

public Destination​(

URI

uri)

Constructs a new destination attribute with the specified

URI

.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this destination attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Destination

.

This destination attribute's

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

is equivalent to this destination
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

Destination

, the category is class

Destination

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

Destination

, the category name is

"spool-data-destination"

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

Returns whether this destination attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Destination

.

This destination attribute's

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

is equivalent to this destination
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

Returns whether this destination attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

Destination

.

This destination attribute's

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

Destination

.

This destination attribute's

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

Destination

, the category is class

Destination

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

Destination

, the category is class

Destination

itself.

For class

Destination

, the category is class

Destination

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

Destination

, the category name is

"spool-data-destination"

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

Destination

, the category name is

"spool-data-destination"

.

For class

Destination

, the category name is

"spool-data-destination"

.

---

