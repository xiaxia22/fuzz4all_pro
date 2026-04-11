# Class PageAttributes

**Source:** `java.desktop\java\awt\PageAttributes.html`

### Class Description

```java
public final class
PageAttributes

extends
Object

implements
Cloneable
```

A set of attributes which control the output of a printed page.

Instances of this class control the color state, paper size (media type),
orientation, logical origin, print quality, and resolution of every
page which uses the instance. Attribute names are compliant with the
Internet Printing Protocol (IPP) 1.1 where possible. Attribute values
are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the color state to
monochrome, use the following code:

```java
import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

**All Implemented Interfaces:** Cloneable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PageAttributes()

Constructs a PageAttributes instance with default values for every
attribute.

---

#### public PageAttributes​(
PageAttributes
obj)

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

**Parameters:**
- obj

- the PageAttributes to copy.

---

#### public PageAttributes​(
PageAttributes.ColorType
color,

PageAttributes.MediaType
media,

PageAttributes.OrientationRequestedType
orientationRequested,

PageAttributes.OriginType
origin,

PageAttributes.PrintQualityType
printQuality,
int[] printerResolution)

Constructs a PageAttributes instance with the specified values for
every attribute.

**Parameters:**
- color

- ColorType.COLOR or ColorType.MONOCHROME.
- media

- one of the constant fields of the MediaType class.
- orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
- origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
- printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
- printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

### Method Details

#### public
Object
clone()

Creates and returns a copy of this PageAttributes.

**Overrides:**
- clone

in class

Object

**Returns:**
- the newly created copy. It is safe to cast this Object into
a PageAttributes.

**See Also:**
- Cloneable

---

#### public void set​(
PageAttributes
obj)

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

**Parameters:**
- obj

- the PageAttributes to copy.

---

#### public
PageAttributes.ColorType
getColor()

Returns whether pages using these attributes will be rendered in
color or monochrome. This attribute is updated to the value chosen
by the user.

**Returns:**
- ColorType.COLOR or ColorType.MONOCHROME.

---

#### public void setColor​(
PageAttributes.ColorType
color)

Specifies whether pages using these attributes will be rendered in
color or monochrome. Not specifying this attribute is equivalent to
specifying ColorType.MONOCHROME.

**Parameters:**
- color

- ColorType.COLOR or ColorType.MONOCHROME.

**Throws:**
- IllegalArgumentException

- if color is null.

---

#### public
PageAttributes.MediaType
getMedia()

Returns the paper size for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:**
- one of the constant fields of the MediaType class.

---

#### public void setMedia​(
PageAttributes.MediaType
media)

Specifies the desired paper size for pages using these attributes. The
actual paper size will be determined by the limitations of the target
printer. If an exact match cannot be found, an implementation will
choose the closest possible match. Not specifying this attribute is
equivalent to specifying the default size for the default locale. The
default size for locales in the United States and Canada is
MediaType.NA_LETTER. The default size for all other locales is
MediaType.ISO_A4.

**Parameters:**
- media

- one of the constant fields of the MediaType class.

**Throws:**
- IllegalArgumentException

- if media is null.

---

#### public void setMediaToDefault()

Sets the paper size for pages using these attributes to the default
size for the default locale. The default size for locales in the
United States and Canada is MediaType.NA_LETTER. The default size for
all other locales is MediaType.ISO_A4.

---

#### public
PageAttributes.OrientationRequestedType
getOrientationRequested()

Returns the print orientation for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:**
- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.

---

#### public void setOrientationRequested​(
PageAttributes.OrientationRequestedType
orientationRequested)

Specifies the print orientation for pages using these attributes. Not
specifying the property is equivalent to specifying
OrientationRequestedType.PORTRAIT.

**Parameters:**
- orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.

**Throws:**
- IllegalArgumentException

- if orientationRequested is null.

---

#### public void setOrientationRequested​(int orientationRequested)

Specifies the print orientation for pages using these attributes.
Specifying

3

denotes portrait. Specifying

4

denotes landscape. Specifying any other value will generate an
IllegalArgumentException. Not specifying the property is equivalent
to calling setOrientationRequested(OrientationRequestedType.PORTRAIT).

**Parameters:**
- orientationRequested

-

3

or

4

**Throws:**
- IllegalArgumentException

- if orientationRequested is not

3

or

4

---

#### public void setOrientationRequestedToDefault()

Sets the print orientation for pages using these attributes to the
default. The default orientation is portrait.

---

#### public
PageAttributes.OriginType
getOrigin()

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) This attribute cannot be modified by,
and is not subject to any limitations of, the implementation or the
target printer.

**Returns:**
- OriginType.PHYSICAL or OriginType.PRINTABLE

---

#### public void setOrigin​(
PageAttributes.OriginType
origin)

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) Not specifying the property is equivalent to
specifying OriginType.PHYSICAL.

**Parameters:**
- origin

- OriginType.PHYSICAL or OriginType.PRINTABLE

**Throws:**
- IllegalArgumentException

- if origin is null.

---

#### public
PageAttributes.PrintQualityType
getPrintQuality()

Returns the print quality for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:**
- PrintQualityType.DRAFT, PrintQualityType.NORMAL, or
PrintQualityType.HIGH

---

#### public void setPrintQuality​(
PageAttributes.PrintQualityType
printQuality)

Specifies the print quality for pages using these attributes. Not
specifying the property is equivalent to specifying
PrintQualityType.NORMAL.

**Parameters:**
- printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH

**Throws:**
- IllegalArgumentException

- if printQuality is null.

---

#### public void setPrintQuality​(int printQuality)

Specifies the print quality for pages using these attributes.
Specifying

3

denotes draft. Specifying

4

denotes normal. Specifying

5

denotes high. Specifying
any other value will generate an IllegalArgumentException. Not
specifying the property is equivalent to calling
setPrintQuality(PrintQualityType.NORMAL).

**Parameters:**
- printQuality

-

3

,

4

, or

5

**Throws:**
- IllegalArgumentException

- if printQuality is not

3

,

4

, or

5

---

#### public void setPrintQualityToDefault()

Sets the print quality for pages using these attributes to the default.
The default print quality is normal.

---

#### public int[] getPrinterResolution()

Returns the print resolution for pages using these attributes.
Index 0 of the array specifies the cross feed direction resolution
(typically the horizontal resolution). Index 1 of the array specifies
the feed direction resolution (typically the vertical resolution).
Index 2 of the array specifies whether the resolutions are in dots per
inch or dots per centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter.

**Returns:**
- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

---

#### public void setPrinterResolution​(int[] printerResolution)

Specifies the desired print resolution for pages using these attributes.
The actual resolution will be determined by the limitations of the
implementation and the target printer. Index 0 of the array specifies
the cross feed direction resolution (typically the horizontal
resolution). Index 1 of the array specifies the feed direction
resolution (typically the vertical resolution). Index 2 of the array
specifies whether the resolutions are in dots per inch or dots per
centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter. Note that the 1.1 printing implementation
(Toolkit.getPrintJob) requires that the feed and cross feed resolutions
be the same. Not specifying the property is equivalent to calling
setPrinterResolution(72).

**Parameters:**
- printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

**Throws:**
- IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### public void setPrinterResolution​(int printerResolution)

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes. The same value is used for both
resolutions. The actual resolutions will be determined by the
limitations of the implementation and the target printer. Not
specifying the property is equivalent to specifying

72

.

**Parameters:**
- printerResolution

- an integer greater than 0.

**Throws:**
- IllegalArgumentException

- if printerResolution is less than or
equal to 0.

---

#### public void setPrinterResolutionToDefault()

Sets the printer resolution for pages using these attributes to the
default. The default is 72 dpi for both the feed and cross feed
resolutions.

---

#### public boolean equals​(
Object
obj)

Determines whether two PageAttributes are equal to each other.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object whose equality will be checked.

**Returns:**
- whether obj is equal to this PageAttribute according to the
above criteria.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns a hash code value for this PageAttributes.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hash code.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
String
toString()

Returns a string representation of this PageAttributes.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation.

---

### Additional Sections

#### Class PageAttributes

java.lang.Object

- java.awt.PageAttributes

java.awt.PageAttributes

**All Implemented Interfaces:** Cloneable

```java
public final class
PageAttributes

extends
Object

implements
Cloneable
```

A set of attributes which control the output of a printed page.

Instances of this class control the color state, paper size (media type),
orientation, logical origin, print quality, and resolution of every
page which uses the instance. Attribute names are compliant with the
Internet Printing Protocol (IPP) 1.1 where possible. Attribute values
are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the color state to
monochrome, use the following code:

```java
import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

**Since:** 1.3

public final class

PageAttributes

extends

Object

implements

Cloneable

A set of attributes which control the output of a printed page.

Instances of this class control the color state, paper size (media type),
orientation, logical origin, print quality, and resolution of every
page which uses the instance. Attribute names are compliant with the
Internet Printing Protocol (IPP) 1.1 where possible. Attribute values
are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the color state to
monochrome, use the following code:

```java
import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

Instances of this class control the color state, paper size (media type),
orientation, logical origin, print quality, and resolution of every
page which uses the instance. Attribute names are compliant with the
Internet Printing Protocol (IPP) 1.1 where possible. Attribute values
are partially compliant where possible.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the color state to
monochrome, use the following code:

```java
import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

To use a method which takes an inner class type, pass a reference to
one of the constant fields of the inner class. Client code cannot create
new instances of the inner class types because none of those classes
has a public constructor. For example, to set the color state to
monochrome, use the following code:

```java
import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}
```

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

import java.awt.PageAttributes;

public class MonochromeExample {
public void setMonochrome(PageAttributes pageAttributes) {
pageAttributes.setColor(PageAttributes.ColorType.MONOCHROME);
}
}

Every IPP attribute which supports an

attributeName

-default value
has a corresponding

set

attributeName

ToDefault

method.
Default value fields are not provided.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PageAttributes.ColorType

A type-safe enumeration of possible color states.

static class

PageAttributes.MediaType

A type-safe enumeration of possible paper sizes.

static class

PageAttributes.OrientationRequestedType

A type-safe enumeration of possible orientations.

static class

PageAttributes.OriginType

A type-safe enumeration of possible origins.

static class

PageAttributes.PrintQualityType

A type-safe enumeration of possible print qualities.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PageAttributes

()

Constructs a PageAttributes instance with default values for every
attribute.

PageAttributes

​(

PageAttributes

obj)

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

PageAttributes

​(

PageAttributes.ColorType

color,

PageAttributes.MediaType

media,

PageAttributes.OrientationRequestedType

orientationRequested,

PageAttributes.OriginType

origin,

PageAttributes.PrintQualityType

printQuality,
int[] printerResolution)

Constructs a PageAttributes instance with the specified values for
every attribute.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this PageAttributes.

boolean

equals

​(

Object

obj)

Determines whether two PageAttributes are equal to each other.

PageAttributes.ColorType

getColor

()

Returns whether pages using these attributes will be rendered in
color or monochrome.

PageAttributes.MediaType

getMedia

()

Returns the paper size for pages using these attributes.

PageAttributes.OrientationRequestedType

getOrientationRequested

()

Returns the print orientation for pages using these attributes.

PageAttributes.OriginType

getOrigin

()

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

int[]

getPrinterResolution

()

Returns the print resolution for pages using these attributes.

PageAttributes.PrintQualityType

getPrintQuality

()

Returns the print quality for pages using these attributes.

int

hashCode

()

Returns a hash code value for this PageAttributes.

void

set

​(

PageAttributes

obj)

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

void

setColor

​(

PageAttributes.ColorType

color)

Specifies whether pages using these attributes will be rendered in
color or monochrome.

void

setMedia

​(

PageAttributes.MediaType

media)

Specifies the desired paper size for pages using these attributes.

void

setMediaToDefault

()

Sets the paper size for pages using these attributes to the default
size for the default locale.

void

setOrientationRequested

​(int orientationRequested)

Specifies the print orientation for pages using these attributes.

void

setOrientationRequested

​(

PageAttributes.OrientationRequestedType

orientationRequested)

Specifies the print orientation for pages using these attributes.

void

setOrientationRequestedToDefault

()

Sets the print orientation for pages using these attributes to the
default.

void

setOrigin

​(

PageAttributes.OriginType

origin)

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

void

setPrinterResolution

​(int printerResolution)

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes.

void

setPrinterResolution

​(int[] printerResolution)

Specifies the desired print resolution for pages using these attributes.

void

setPrinterResolutionToDefault

()

Sets the printer resolution for pages using these attributes to the
default.

void

setPrintQuality

​(int printQuality)

Specifies the print quality for pages using these attributes.

void

setPrintQuality

​(

PageAttributes.PrintQualityType

printQuality)

Specifies the print quality for pages using these attributes.

void

setPrintQualityToDefault

()

Sets the print quality for pages using these attributes to the default.

String

toString

()

Returns a string representation of this PageAttributes.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

PageAttributes.ColorType

A type-safe enumeration of possible color states.

static class

PageAttributes.MediaType

A type-safe enumeration of possible paper sizes.

static class

PageAttributes.OrientationRequestedType

A type-safe enumeration of possible orientations.

static class

PageAttributes.OriginType

A type-safe enumeration of possible origins.

static class

PageAttributes.PrintQualityType

A type-safe enumeration of possible print qualities.

---

#### Nested Class Summary

A type-safe enumeration of possible color states.

A type-safe enumeration of possible paper sizes.

A type-safe enumeration of possible orientations.

A type-safe enumeration of possible origins.

A type-safe enumeration of possible print qualities.

Constructor Summary

Constructors

Constructor

Description

PageAttributes

()

Constructs a PageAttributes instance with default values for every
attribute.

PageAttributes

​(

PageAttributes

obj)

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

PageAttributes

​(

PageAttributes.ColorType

color,

PageAttributes.MediaType

media,

PageAttributes.OrientationRequestedType

orientationRequested,

PageAttributes.OriginType

origin,

PageAttributes.PrintQualityType

printQuality,
int[] printerResolution)

Constructs a PageAttributes instance with the specified values for
every attribute.

---

#### Constructor Summary

Constructs a PageAttributes instance with default values for every
attribute.

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

Constructs a PageAttributes instance with the specified values for
every attribute.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Object

clone

()

Creates and returns a copy of this PageAttributes.

boolean

equals

​(

Object

obj)

Determines whether two PageAttributes are equal to each other.

PageAttributes.ColorType

getColor

()

Returns whether pages using these attributes will be rendered in
color or monochrome.

PageAttributes.MediaType

getMedia

()

Returns the paper size for pages using these attributes.

PageAttributes.OrientationRequestedType

getOrientationRequested

()

Returns the print orientation for pages using these attributes.

PageAttributes.OriginType

getOrigin

()

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

int[]

getPrinterResolution

()

Returns the print resolution for pages using these attributes.

PageAttributes.PrintQualityType

getPrintQuality

()

Returns the print quality for pages using these attributes.

int

hashCode

()

Returns a hash code value for this PageAttributes.

void

set

​(

PageAttributes

obj)

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

void

setColor

​(

PageAttributes.ColorType

color)

Specifies whether pages using these attributes will be rendered in
color or monochrome.

void

setMedia

​(

PageAttributes.MediaType

media)

Specifies the desired paper size for pages using these attributes.

void

setMediaToDefault

()

Sets the paper size for pages using these attributes to the default
size for the default locale.

void

setOrientationRequested

​(int orientationRequested)

Specifies the print orientation for pages using these attributes.

void

setOrientationRequested

​(

PageAttributes.OrientationRequestedType

orientationRequested)

Specifies the print orientation for pages using these attributes.

void

setOrientationRequestedToDefault

()

Sets the print orientation for pages using these attributes to the
default.

void

setOrigin

​(

PageAttributes.OriginType

origin)

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

void

setPrinterResolution

​(int printerResolution)

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes.

void

setPrinterResolution

​(int[] printerResolution)

Specifies the desired print resolution for pages using these attributes.

void

setPrinterResolutionToDefault

()

Sets the printer resolution for pages using these attributes to the
default.

void

setPrintQuality

​(int printQuality)

Specifies the print quality for pages using these attributes.

void

setPrintQuality

​(

PageAttributes.PrintQualityType

printQuality)

Specifies the print quality for pages using these attributes.

void

setPrintQualityToDefault

()

Sets the print quality for pages using these attributes to the default.

String

toString

()

Returns a string representation of this PageAttributes.

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

Creates and returns a copy of this PageAttributes.

Determines whether two PageAttributes are equal to each other.

Returns whether pages using these attributes will be rendered in
color or monochrome.

Returns the paper size for pages using these attributes.

Returns the print orientation for pages using these attributes.

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

Returns the print resolution for pages using these attributes.

Returns the print quality for pages using these attributes.

Returns a hash code value for this PageAttributes.

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

Specifies whether pages using these attributes will be rendered in
color or monochrome.

Specifies the desired paper size for pages using these attributes.

Sets the paper size for pages using these attributes to the default
size for the default locale.

Specifies the print orientation for pages using these attributes.

Sets the print orientation for pages using these attributes to the
default.

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area.

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes.

Specifies the desired print resolution for pages using these attributes.

Sets the printer resolution for pages using these attributes to the
default.

Specifies the print quality for pages using these attributes.

Sets the print quality for pages using these attributes to the default.

Returns a string representation of this PageAttributes.

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

- PageAttributes

```java
public PageAttributes()
```

Constructs a PageAttributes instance with default values for every
attribute.

- PageAttributes

```java
public PageAttributes​(
PageAttributes
obj)
```

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

**Parameters:** obj

- the PageAttributes to copy.

- PageAttributes

```java
public PageAttributes​(
PageAttributes.ColorType
color,

PageAttributes.MediaType
media,

PageAttributes.OrientationRequestedType
orientationRequested,

PageAttributes.OriginType
origin,

PageAttributes.PrintQualityType
printQuality,
int[] printerResolution)
```

Constructs a PageAttributes instance with the specified values for
every attribute.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Parameters:** media

- one of the constant fields of the MediaType class.
**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this PageAttributes.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy. It is safe to cast this Object into
a PageAttributes.
**See Also:** Cloneable

- set

```java
public void set​(
PageAttributes
obj)
```

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

**Parameters:** obj

- the PageAttributes to copy.

- getColor

```java
public
PageAttributes.ColorType
getColor()
```

Returns whether pages using these attributes will be rendered in
color or monochrome. This attribute is updated to the value chosen
by the user.

**Returns:** ColorType.COLOR or ColorType.MONOCHROME.

- setColor

```java
public void setColor​(
PageAttributes.ColorType
color)
```

Specifies whether pages using these attributes will be rendered in
color or monochrome. Not specifying this attribute is equivalent to
specifying ColorType.MONOCHROME.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Throws:** IllegalArgumentException

- if color is null.

- getMedia

```java
public
PageAttributes.MediaType
getMedia()
```

Returns the paper size for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** one of the constant fields of the MediaType class.

- setMedia

```java
public void setMedia​(
PageAttributes.MediaType
media)
```

Specifies the desired paper size for pages using these attributes. The
actual paper size will be determined by the limitations of the target
printer. If an exact match cannot be found, an implementation will
choose the closest possible match. Not specifying this attribute is
equivalent to specifying the default size for the default locale. The
default size for locales in the United States and Canada is
MediaType.NA_LETTER. The default size for all other locales is
MediaType.ISO_A4.

**Parameters:** media

- one of the constant fields of the MediaType class.
**Throws:** IllegalArgumentException

- if media is null.

- setMediaToDefault

```java
public void setMediaToDefault()
```

Sets the paper size for pages using these attributes to the default
size for the default locale. The default size for locales in the
United States and Canada is MediaType.NA_LETTER. The default size for
all other locales is MediaType.ISO_A4.

- getOrientationRequested

```java
public
PageAttributes.OrientationRequestedType
getOrientationRequested()
```

Returns the print orientation for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.

- setOrientationRequested

```java
public void setOrientationRequested​(
PageAttributes.OrientationRequestedType
orientationRequested)
```

Specifies the print orientation for pages using these attributes. Not
specifying the property is equivalent to specifying
OrientationRequestedType.PORTRAIT.

**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Throws:** IllegalArgumentException

- if orientationRequested is null.

- setOrientationRequested

```java
public void setOrientationRequested​(int orientationRequested)
```

Specifies the print orientation for pages using these attributes.
Specifying

3

denotes portrait. Specifying

4

denotes landscape. Specifying any other value will generate an
IllegalArgumentException. Not specifying the property is equivalent
to calling setOrientationRequested(OrientationRequestedType.PORTRAIT).

**Parameters:** orientationRequested

-

3

or

4
**Throws:** IllegalArgumentException

- if orientationRequested is not

3

or

4

- setOrientationRequestedToDefault

```java
public void setOrientationRequestedToDefault()
```

Sets the print orientation for pages using these attributes to the
default. The default orientation is portrait.

- getOrigin

```java
public
PageAttributes.OriginType
getOrigin()
```

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) This attribute cannot be modified by,
and is not subject to any limitations of, the implementation or the
target printer.

**Returns:** OriginType.PHYSICAL or OriginType.PRINTABLE

- setOrigin

```java
public void setOrigin​(
PageAttributes.OriginType
origin)
```

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) Not specifying the property is equivalent to
specifying OriginType.PHYSICAL.

**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Throws:** IllegalArgumentException

- if origin is null.

- getPrintQuality

```java
public
PageAttributes.PrintQualityType
getPrintQuality()
```

Returns the print quality for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** PrintQualityType.DRAFT, PrintQualityType.NORMAL, or
PrintQualityType.HIGH

- setPrintQuality

```java
public void setPrintQuality​(
PageAttributes.PrintQualityType
printQuality)
```

Specifies the print quality for pages using these attributes. Not
specifying the property is equivalent to specifying
PrintQualityType.NORMAL.

**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Throws:** IllegalArgumentException

- if printQuality is null.

- setPrintQuality

```java
public void setPrintQuality​(int printQuality)
```

Specifies the print quality for pages using these attributes.
Specifying

3

denotes draft. Specifying

4

denotes normal. Specifying

5

denotes high. Specifying
any other value will generate an IllegalArgumentException. Not
specifying the property is equivalent to calling
setPrintQuality(PrintQualityType.NORMAL).

**Parameters:** printQuality

-

3

,

4

, or

5
**Throws:** IllegalArgumentException

- if printQuality is not

3

,

4

, or

5

- setPrintQualityToDefault

```java
public void setPrintQualityToDefault()
```

Sets the print quality for pages using these attributes to the default.
The default print quality is normal.

- getPrinterResolution

```java
public int[] getPrinterResolution()
```

Returns the print resolution for pages using these attributes.
Index 0 of the array specifies the cross feed direction resolution
(typically the horizontal resolution). Index 1 of the array specifies
the feed direction resolution (typically the vertical resolution).
Index 2 of the array specifies whether the resolutions are in dots per
inch or dots per centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter.

**Returns:** an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

- setPrinterResolution

```java
public void setPrinterResolution​(int[] printerResolution)
```

Specifies the desired print resolution for pages using these attributes.
The actual resolution will be determined by the limitations of the
implementation and the target printer. Index 0 of the array specifies
the cross feed direction resolution (typically the horizontal
resolution). Index 1 of the array specifies the feed direction
resolution (typically the vertical resolution). Index 2 of the array
specifies whether the resolutions are in dots per inch or dots per
centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter. Note that the 1.1 printing implementation
(Toolkit.getPrintJob) requires that the feed and cross feed resolutions
be the same. Not specifying the property is equivalent to calling
setPrinterResolution(72).

**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- setPrinterResolution

```java
public void setPrinterResolution​(int printerResolution)
```

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes. The same value is used for both
resolutions. The actual resolutions will be determined by the
limitations of the implementation and the target printer. Not
specifying the property is equivalent to specifying

72

.

**Parameters:** printerResolution

- an integer greater than 0.
**Throws:** IllegalArgumentException

- if printerResolution is less than or
equal to 0.

- setPrinterResolutionToDefault

```java
public void setPrinterResolutionToDefault()
```

Sets the printer resolution for pages using these attributes to the
default. The default is 72 dpi for both the feed and cross feed
resolutions.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two PageAttributes are equal to each other.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this PageAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this PageAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this PageAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

Constructor Detail

- PageAttributes

```java
public PageAttributes()
```

Constructs a PageAttributes instance with default values for every
attribute.

- PageAttributes

```java
public PageAttributes​(
PageAttributes
obj)
```

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

**Parameters:** obj

- the PageAttributes to copy.

- PageAttributes

```java
public PageAttributes​(
PageAttributes.ColorType
color,

PageAttributes.MediaType
media,

PageAttributes.OrientationRequestedType
orientationRequested,

PageAttributes.OriginType
origin,

PageAttributes.PrintQualityType
printQuality,
int[] printerResolution)
```

Constructs a PageAttributes instance with the specified values for
every attribute.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Parameters:** media

- one of the constant fields of the MediaType class.
**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### Constructor Detail

PageAttributes

```java
public PageAttributes()
```

Constructs a PageAttributes instance with default values for every
attribute.

---

#### PageAttributes

public PageAttributes()

Constructs a PageAttributes instance with default values for every
attribute.

PageAttributes

```java
public PageAttributes​(
PageAttributes
obj)
```

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

**Parameters:** obj

- the PageAttributes to copy.

---

#### PageAttributes

public PageAttributes​(

PageAttributes

obj)

Constructs a PageAttributes instance which is a copy of the supplied
PageAttributes.

PageAttributes

```java
public PageAttributes​(
PageAttributes.ColorType
color,

PageAttributes.MediaType
media,

PageAttributes.OrientationRequestedType
orientationRequested,

PageAttributes.OriginType
origin,

PageAttributes.PrintQualityType
printQuality,
int[] printerResolution)
```

Constructs a PageAttributes instance with the specified values for
every attribute.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Parameters:** media

- one of the constant fields of the MediaType class.
**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### PageAttributes

public PageAttributes​(

PageAttributes.ColorType

color,

PageAttributes.MediaType

media,

PageAttributes.OrientationRequestedType

orientationRequested,

PageAttributes.OriginType

origin,

PageAttributes.PrintQualityType

printQuality,
int[] printerResolution)

Constructs a PageAttributes instance with the specified values for
every attribute.

Method Detail

- clone

```java
public
Object
clone()
```

Creates and returns a copy of this PageAttributes.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy. It is safe to cast this Object into
a PageAttributes.
**See Also:** Cloneable

- set

```java
public void set​(
PageAttributes
obj)
```

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

**Parameters:** obj

- the PageAttributes to copy.

- getColor

```java
public
PageAttributes.ColorType
getColor()
```

Returns whether pages using these attributes will be rendered in
color or monochrome. This attribute is updated to the value chosen
by the user.

**Returns:** ColorType.COLOR or ColorType.MONOCHROME.

- setColor

```java
public void setColor​(
PageAttributes.ColorType
color)
```

Specifies whether pages using these attributes will be rendered in
color or monochrome. Not specifying this attribute is equivalent to
specifying ColorType.MONOCHROME.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Throws:** IllegalArgumentException

- if color is null.

- getMedia

```java
public
PageAttributes.MediaType
getMedia()
```

Returns the paper size for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** one of the constant fields of the MediaType class.

- setMedia

```java
public void setMedia​(
PageAttributes.MediaType
media)
```

Specifies the desired paper size for pages using these attributes. The
actual paper size will be determined by the limitations of the target
printer. If an exact match cannot be found, an implementation will
choose the closest possible match. Not specifying this attribute is
equivalent to specifying the default size for the default locale. The
default size for locales in the United States and Canada is
MediaType.NA_LETTER. The default size for all other locales is
MediaType.ISO_A4.

**Parameters:** media

- one of the constant fields of the MediaType class.
**Throws:** IllegalArgumentException

- if media is null.

- setMediaToDefault

```java
public void setMediaToDefault()
```

Sets the paper size for pages using these attributes to the default
size for the default locale. The default size for locales in the
United States and Canada is MediaType.NA_LETTER. The default size for
all other locales is MediaType.ISO_A4.

- getOrientationRequested

```java
public
PageAttributes.OrientationRequestedType
getOrientationRequested()
```

Returns the print orientation for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.

- setOrientationRequested

```java
public void setOrientationRequested​(
PageAttributes.OrientationRequestedType
orientationRequested)
```

Specifies the print orientation for pages using these attributes. Not
specifying the property is equivalent to specifying
OrientationRequestedType.PORTRAIT.

**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Throws:** IllegalArgumentException

- if orientationRequested is null.

- setOrientationRequested

```java
public void setOrientationRequested​(int orientationRequested)
```

Specifies the print orientation for pages using these attributes.
Specifying

3

denotes portrait. Specifying

4

denotes landscape. Specifying any other value will generate an
IllegalArgumentException. Not specifying the property is equivalent
to calling setOrientationRequested(OrientationRequestedType.PORTRAIT).

**Parameters:** orientationRequested

-

3

or

4
**Throws:** IllegalArgumentException

- if orientationRequested is not

3

or

4

- setOrientationRequestedToDefault

```java
public void setOrientationRequestedToDefault()
```

Sets the print orientation for pages using these attributes to the
default. The default orientation is portrait.

- getOrigin

```java
public
PageAttributes.OriginType
getOrigin()
```

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) This attribute cannot be modified by,
and is not subject to any limitations of, the implementation or the
target printer.

**Returns:** OriginType.PHYSICAL or OriginType.PRINTABLE

- setOrigin

```java
public void setOrigin​(
PageAttributes.OriginType
origin)
```

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) Not specifying the property is equivalent to
specifying OriginType.PHYSICAL.

**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Throws:** IllegalArgumentException

- if origin is null.

- getPrintQuality

```java
public
PageAttributes.PrintQualityType
getPrintQuality()
```

Returns the print quality for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** PrintQualityType.DRAFT, PrintQualityType.NORMAL, or
PrintQualityType.HIGH

- setPrintQuality

```java
public void setPrintQuality​(
PageAttributes.PrintQualityType
printQuality)
```

Specifies the print quality for pages using these attributes. Not
specifying the property is equivalent to specifying
PrintQualityType.NORMAL.

**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Throws:** IllegalArgumentException

- if printQuality is null.

- setPrintQuality

```java
public void setPrintQuality​(int printQuality)
```

Specifies the print quality for pages using these attributes.
Specifying

3

denotes draft. Specifying

4

denotes normal. Specifying

5

denotes high. Specifying
any other value will generate an IllegalArgumentException. Not
specifying the property is equivalent to calling
setPrintQuality(PrintQualityType.NORMAL).

**Parameters:** printQuality

-

3

,

4

, or

5
**Throws:** IllegalArgumentException

- if printQuality is not

3

,

4

, or

5

- setPrintQualityToDefault

```java
public void setPrintQualityToDefault()
```

Sets the print quality for pages using these attributes to the default.
The default print quality is normal.

- getPrinterResolution

```java
public int[] getPrinterResolution()
```

Returns the print resolution for pages using these attributes.
Index 0 of the array specifies the cross feed direction resolution
(typically the horizontal resolution). Index 1 of the array specifies
the feed direction resolution (typically the vertical resolution).
Index 2 of the array specifies whether the resolutions are in dots per
inch or dots per centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter.

**Returns:** an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

- setPrinterResolution

```java
public void setPrinterResolution​(int[] printerResolution)
```

Specifies the desired print resolution for pages using these attributes.
The actual resolution will be determined by the limitations of the
implementation and the target printer. Index 0 of the array specifies
the cross feed direction resolution (typically the horizontal
resolution). Index 1 of the array specifies the feed direction
resolution (typically the vertical resolution). Index 2 of the array
specifies whether the resolutions are in dots per inch or dots per
centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter. Note that the 1.1 printing implementation
(Toolkit.getPrintJob) requires that the feed and cross feed resolutions
be the same. Not specifying the property is equivalent to calling
setPrinterResolution(72).

**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

- setPrinterResolution

```java
public void setPrinterResolution​(int printerResolution)
```

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes. The same value is used for both
resolutions. The actual resolutions will be determined by the
limitations of the implementation and the target printer. Not
specifying the property is equivalent to specifying

72

.

**Parameters:** printerResolution

- an integer greater than 0.
**Throws:** IllegalArgumentException

- if printerResolution is less than or
equal to 0.

- setPrinterResolutionToDefault

```java
public void setPrinterResolutionToDefault()
```

Sets the printer resolution for pages using these attributes to the
default. The default is 72 dpi for both the feed and cross feed
resolutions.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two PageAttributes are equal to each other.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this PageAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this PageAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- toString

```java
public
String
toString()
```

Returns a string representation of this PageAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### Method Detail

clone

```java
public
Object
clone()
```

Creates and returns a copy of this PageAttributes.

**Overrides:** clone

in class

Object
**Returns:** the newly created copy. It is safe to cast this Object into
a PageAttributes.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates and returns a copy of this PageAttributes.

set

```java
public void set​(
PageAttributes
obj)
```

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

**Parameters:** obj

- the PageAttributes to copy.

---

#### set

public void set​(

PageAttributes

obj)

Sets all of the attributes of this PageAttributes to the same values as
the attributes of obj.

getColor

```java
public
PageAttributes.ColorType
getColor()
```

Returns whether pages using these attributes will be rendered in
color or monochrome. This attribute is updated to the value chosen
by the user.

**Returns:** ColorType.COLOR or ColorType.MONOCHROME.

---

#### getColor

public

PageAttributes.ColorType

getColor()

Returns whether pages using these attributes will be rendered in
color or monochrome. This attribute is updated to the value chosen
by the user.

setColor

```java
public void setColor​(
PageAttributes.ColorType
color)
```

Specifies whether pages using these attributes will be rendered in
color or monochrome. Not specifying this attribute is equivalent to
specifying ColorType.MONOCHROME.

**Parameters:** color

- ColorType.COLOR or ColorType.MONOCHROME.
**Throws:** IllegalArgumentException

- if color is null.

---

#### setColor

public void setColor​(

PageAttributes.ColorType

color)

Specifies whether pages using these attributes will be rendered in
color or monochrome. Not specifying this attribute is equivalent to
specifying ColorType.MONOCHROME.

getMedia

```java
public
PageAttributes.MediaType
getMedia()
```

Returns the paper size for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** one of the constant fields of the MediaType class.

---

#### getMedia

public

PageAttributes.MediaType

getMedia()

Returns the paper size for pages using these attributes. This
attribute is updated to the value chosen by the user.

setMedia

```java
public void setMedia​(
PageAttributes.MediaType
media)
```

Specifies the desired paper size for pages using these attributes. The
actual paper size will be determined by the limitations of the target
printer. If an exact match cannot be found, an implementation will
choose the closest possible match. Not specifying this attribute is
equivalent to specifying the default size for the default locale. The
default size for locales in the United States and Canada is
MediaType.NA_LETTER. The default size for all other locales is
MediaType.ISO_A4.

**Parameters:** media

- one of the constant fields of the MediaType class.
**Throws:** IllegalArgumentException

- if media is null.

---

#### setMedia

public void setMedia​(

PageAttributes.MediaType

media)

Specifies the desired paper size for pages using these attributes. The
actual paper size will be determined by the limitations of the target
printer. If an exact match cannot be found, an implementation will
choose the closest possible match. Not specifying this attribute is
equivalent to specifying the default size for the default locale. The
default size for locales in the United States and Canada is
MediaType.NA_LETTER. The default size for all other locales is
MediaType.ISO_A4.

setMediaToDefault

```java
public void setMediaToDefault()
```

Sets the paper size for pages using these attributes to the default
size for the default locale. The default size for locales in the
United States and Canada is MediaType.NA_LETTER. The default size for
all other locales is MediaType.ISO_A4.

---

#### setMediaToDefault

public void setMediaToDefault()

Sets the paper size for pages using these attributes to the default
size for the default locale. The default size for locales in the
United States and Canada is MediaType.NA_LETTER. The default size for
all other locales is MediaType.ISO_A4.

getOrientationRequested

```java
public
PageAttributes.OrientationRequestedType
getOrientationRequested()
```

Returns the print orientation for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.

---

#### getOrientationRequested

public

PageAttributes.OrientationRequestedType

getOrientationRequested()

Returns the print orientation for pages using these attributes. This
attribute is updated to the value chosen by the user.

setOrientationRequested

```java
public void setOrientationRequested​(
PageAttributes.OrientationRequestedType
orientationRequested)
```

Specifies the print orientation for pages using these attributes. Not
specifying the property is equivalent to specifying
OrientationRequestedType.PORTRAIT.

**Parameters:** orientationRequested

- OrientationRequestedType.PORTRAIT or
OrientationRequestedType.LANDSCAPE.
**Throws:** IllegalArgumentException

- if orientationRequested is null.

---

#### setOrientationRequested

public void setOrientationRequested​(

PageAttributes.OrientationRequestedType

orientationRequested)

Specifies the print orientation for pages using these attributes. Not
specifying the property is equivalent to specifying
OrientationRequestedType.PORTRAIT.

setOrientationRequested

```java
public void setOrientationRequested​(int orientationRequested)
```

Specifies the print orientation for pages using these attributes.
Specifying

3

denotes portrait. Specifying

4

denotes landscape. Specifying any other value will generate an
IllegalArgumentException. Not specifying the property is equivalent
to calling setOrientationRequested(OrientationRequestedType.PORTRAIT).

**Parameters:** orientationRequested

-

3

or

4
**Throws:** IllegalArgumentException

- if orientationRequested is not

3

or

4

---

#### setOrientationRequested

public void setOrientationRequested​(int orientationRequested)

Specifies the print orientation for pages using these attributes.
Specifying

3

denotes portrait. Specifying

4

denotes landscape. Specifying any other value will generate an
IllegalArgumentException. Not specifying the property is equivalent
to calling setOrientationRequested(OrientationRequestedType.PORTRAIT).

setOrientationRequestedToDefault

```java
public void setOrientationRequestedToDefault()
```

Sets the print orientation for pages using these attributes to the
default. The default orientation is portrait.

---

#### setOrientationRequestedToDefault

public void setOrientationRequestedToDefault()

Sets the print orientation for pages using these attributes to the
default. The default orientation is portrait.

getOrigin

```java
public
PageAttributes.OriginType
getOrigin()
```

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) This attribute cannot be modified by,
and is not subject to any limitations of, the implementation or the
target printer.

**Returns:** OriginType.PHYSICAL or OriginType.PRINTABLE

---

#### getOrigin

public

PageAttributes.OriginType

getOrigin()

Returns whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) This attribute cannot be modified by,
and is not subject to any limitations of, the implementation or the
target printer.

setOrigin

```java
public void setOrigin​(
PageAttributes.OriginType
origin)
```

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) Not specifying the property is equivalent to
specifying OriginType.PHYSICAL.

**Parameters:** origin

- OriginType.PHYSICAL or OriginType.PRINTABLE
**Throws:** IllegalArgumentException

- if origin is null.

---

#### setOrigin

public void setOrigin​(

PageAttributes.OriginType

origin)

Specifies whether drawing at (0, 0) to pages using these attributes
draws at the upper-left corner of the physical page, or at the
upper-left corner of the printable area. (Note that these locations
could be equivalent.) Not specifying the property is equivalent to
specifying OriginType.PHYSICAL.

getPrintQuality

```java
public
PageAttributes.PrintQualityType
getPrintQuality()
```

Returns the print quality for pages using these attributes. This
attribute is updated to the value chosen by the user.

**Returns:** PrintQualityType.DRAFT, PrintQualityType.NORMAL, or
PrintQualityType.HIGH

---

#### getPrintQuality

public

PageAttributes.PrintQualityType

getPrintQuality()

Returns the print quality for pages using these attributes. This
attribute is updated to the value chosen by the user.

setPrintQuality

```java
public void setPrintQuality​(
PageAttributes.PrintQualityType
printQuality)
```

Specifies the print quality for pages using these attributes. Not
specifying the property is equivalent to specifying
PrintQualityType.NORMAL.

**Parameters:** printQuality

- PrintQualityType.DRAFT, PrintQualityType.NORMAL,
or PrintQualityType.HIGH
**Throws:** IllegalArgumentException

- if printQuality is null.

---

#### setPrintQuality

public void setPrintQuality​(

PageAttributes.PrintQualityType

printQuality)

Specifies the print quality for pages using these attributes. Not
specifying the property is equivalent to specifying
PrintQualityType.NORMAL.

setPrintQuality

```java
public void setPrintQuality​(int printQuality)
```

Specifies the print quality for pages using these attributes.
Specifying

3

denotes draft. Specifying

4

denotes normal. Specifying

5

denotes high. Specifying
any other value will generate an IllegalArgumentException. Not
specifying the property is equivalent to calling
setPrintQuality(PrintQualityType.NORMAL).

**Parameters:** printQuality

-

3

,

4

, or

5
**Throws:** IllegalArgumentException

- if printQuality is not

3

,

4

, or

5

---

#### setPrintQuality

public void setPrintQuality​(int printQuality)

Specifies the print quality for pages using these attributes.
Specifying

3

denotes draft. Specifying

4

denotes normal. Specifying

5

denotes high. Specifying
any other value will generate an IllegalArgumentException. Not
specifying the property is equivalent to calling
setPrintQuality(PrintQualityType.NORMAL).

setPrintQualityToDefault

```java
public void setPrintQualityToDefault()
```

Sets the print quality for pages using these attributes to the default.
The default print quality is normal.

---

#### setPrintQualityToDefault

public void setPrintQualityToDefault()

Sets the print quality for pages using these attributes to the default.
The default print quality is normal.

getPrinterResolution

```java
public int[] getPrinterResolution()
```

Returns the print resolution for pages using these attributes.
Index 0 of the array specifies the cross feed direction resolution
(typically the horizontal resolution). Index 1 of the array specifies
the feed direction resolution (typically the vertical resolution).
Index 2 of the array specifies whether the resolutions are in dots per
inch or dots per centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter.

**Returns:** an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.

---

#### getPrinterResolution

public int[] getPrinterResolution()

Returns the print resolution for pages using these attributes.
Index 0 of the array specifies the cross feed direction resolution
(typically the horizontal resolution). Index 1 of the array specifies
the feed direction resolution (typically the vertical resolution).
Index 2 of the array specifies whether the resolutions are in dots per
inch or dots per centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter.

setPrinterResolution

```java
public void setPrinterResolution​(int[] printerResolution)
```

Specifies the desired print resolution for pages using these attributes.
The actual resolution will be determined by the limitations of the
implementation and the target printer. Index 0 of the array specifies
the cross feed direction resolution (typically the horizontal
resolution). Index 1 of the array specifies the feed direction
resolution (typically the vertical resolution). Index 2 of the array
specifies whether the resolutions are in dots per inch or dots per
centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter. Note that the 1.1 printing implementation
(Toolkit.getPrintJob) requires that the feed and cross feed resolutions
be the same. Not specifying the property is equivalent to calling
setPrinterResolution(72).

**Parameters:** printerResolution

- an integer array of 3 elements. The first
element must be greater than 0. The second element must be
must be greater than 0. The third element must be either

3

or

4

.
**Throws:** IllegalArgumentException

- if one or more of the above
conditions is violated.

---

#### setPrinterResolution

public void setPrinterResolution​(int[] printerResolution)

Specifies the desired print resolution for pages using these attributes.
The actual resolution will be determined by the limitations of the
implementation and the target printer. Index 0 of the array specifies
the cross feed direction resolution (typically the horizontal
resolution). Index 1 of the array specifies the feed direction
resolution (typically the vertical resolution). Index 2 of the array
specifies whether the resolutions are in dots per inch or dots per
centimeter.

3

denotes dots per inch.

4

denotes dots per centimeter. Note that the 1.1 printing implementation
(Toolkit.getPrintJob) requires that the feed and cross feed resolutions
be the same. Not specifying the property is equivalent to calling
setPrinterResolution(72).

setPrinterResolution

```java
public void setPrinterResolution​(int printerResolution)
```

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes. The same value is used for both
resolutions. The actual resolutions will be determined by the
limitations of the implementation and the target printer. Not
specifying the property is equivalent to specifying

72

.

**Parameters:** printerResolution

- an integer greater than 0.
**Throws:** IllegalArgumentException

- if printerResolution is less than or
equal to 0.

---

#### setPrinterResolution

public void setPrinterResolution​(int printerResolution)

Specifies the desired cross feed and feed print resolutions in dots per
inch for pages using these attributes. The same value is used for both
resolutions. The actual resolutions will be determined by the
limitations of the implementation and the target printer. Not
specifying the property is equivalent to specifying

72

.

setPrinterResolutionToDefault

```java
public void setPrinterResolutionToDefault()
```

Sets the printer resolution for pages using these attributes to the
default. The default is 72 dpi for both the feed and cross feed
resolutions.

---

#### setPrinterResolutionToDefault

public void setPrinterResolutionToDefault()

Sets the printer resolution for pages using these attributes to the
default. The default is 72 dpi for both the feed and cross feed
resolutions.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether two PageAttributes are equal to each other.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object whose equality will be checked.
**Returns:** whether obj is equal to this PageAttribute according to the
above criteria.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether two PageAttributes are equal to each other.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

Two PageAttributes are equal if and only if each of their attributes are
equal. Attributes of enumeration type are equal if and only if the
fields refer to the same unique enumeration object. This means that
an aliased media is equal to its underlying unique media. Printer
resolutions are equal if and only if the feed resolution, cross feed
resolution, and units are equal.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this PageAttributes.

**Overrides:** hashCode

in class

Object
**Returns:** the hash code.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this PageAttributes.

toString

```java
public
String
toString()
```

Returns a string representation of this PageAttributes.

**Overrides:** toString

in class

Object
**Returns:** the string representation.

---

#### toString

public

String

toString()

Returns a string representation of this PageAttributes.

---

