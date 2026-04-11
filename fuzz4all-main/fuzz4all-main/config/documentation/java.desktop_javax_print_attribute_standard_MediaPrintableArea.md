# Class MediaPrintableArea

**Source:** `java.desktop\javax\print\attribute\standard\MediaPrintableArea.html`

### Class Description

```java
public final class
MediaPrintableArea

extends
Object

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

MediaPrintableArea

is a printing attribute used to distinguish
the printable and non-printable areas of media.

The printable area is specified to be a rectangle, within the overall
dimensions of a media.

Most printers cannot print on the entire surface of the media, due to printer
hardware limitations. This class can be used to query the acceptable values
for a supposed print job, and to request an area within the constraints of
the printable area to be used in a print job.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

**All Implemented Interfaces:** Serializable

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

#### public static final int INCH

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:**
- Constant Field Values

---

#### public static final int MM

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MediaPrintableArea​(float x,
float y,
float w,
float h,
int units)

Constructs a

MediaPrintableArea

object from floating point
values.

**Parameters:**
- x

- printable x
- y

- printable y
- w

- printable width
- h

- printable height
- units

- in which the values are expressed

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

---

#### public MediaPrintableArea​(int x,
int y,
int w,
int h,
int units)

Constructs a

MediaPrintableArea

object from integer values.

**Parameters:**
- x

- printable x
- y

- printable y
- w

- printable width
- h

- printable height
- units

- in which the values are expressed

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

---

### Method Details

#### public float[] getPrintableArea​(int units)

Get the printable area as an array of 4 values in the order

x, y, w, h

. The values returned are in the given units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- printable area as array of

x, y, w, h

in the specified
units

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getX​(int units)

Get the

x

location of the origin of the printable area in the
specified units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- x

location of the origin of the printable area in the
specified units

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getY​(int units)

Get the

y

location of the origin of the printable area in the
specified units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- y

location of the origin of the printable area in the
specified units

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getWidth​(int units)

Get the

width

of the printable area in the specified units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- width

of the printable area in the specified units

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public float getHeight​(int units)

Get the

height

of the printable area in the specified units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM

**Returns:**
- height

of the printable area in the specified units

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public boolean equals​(
Object
object)

Returns whether this media margins attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

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
margins attribute,

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

MediaPrintableArea

, the category is class

MediaPrintableArea

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

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

#### public
String
toString​(int units,

String
unitsName)

Returns a string version of this rectangular size attribute in the given
units.

**Parameters:**
- units

- unit conversion factor, e.g.

INCH

or

MM
- unitsName

- units name string, e.g.

"in"

or

"mm"

.
If

null

, no units name is appended to the result

**Returns:**
- string version of this two-dimensional size attribute

**Throws:**
- IllegalArgumentException

- if

units < 1

---

#### public
String
toString()

Returns a string version of this rectangular size attribute in mm.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of the object.

---

#### public int hashCode()

Returns a hash code value for this attribute.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code value for this object.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class MediaPrintableArea

java.lang.Object

- javax.print.attribute.standard.MediaPrintableArea

javax.print.attribute.standard.MediaPrintableArea

**All Implemented Interfaces:** Serializable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
MediaPrintableArea

extends
Object

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

MediaPrintableArea

is a printing attribute used to distinguish
the printable and non-printable areas of media.

The printable area is specified to be a rectangle, within the overall
dimensions of a media.

Most printers cannot print on the entire surface of the media, due to printer
hardware limitations. This class can be used to query the acceptable values
for a supposed print job, and to request an area within the constraints of
the printable area to be used in a print job.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

**See Also:** Serialized Form

public final class

MediaPrintableArea

extends

Object

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

MediaPrintableArea

is a printing attribute used to distinguish
the printable and non-printable areas of media.

The printable area is specified to be a rectangle, within the overall
dimensions of a media.

Most printers cannot print on the entire surface of the media, due to printer
hardware limitations. This class can be used to query the acceptable values
for a supposed print job, and to request an area within the constraints of
the printable area to be used in a print job.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

The printable area is specified to be a rectangle, within the overall
dimensions of a media.

Most printers cannot print on the entire surface of the media, due to printer
hardware limitations. This class can be used to query the acceptable values
for a supposed print job, and to request an area within the constraints of
the printable area to be used in a print job.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

Most printers cannot print on the entire surface of the media, due to printer
hardware limitations. This class can be used to query the acceptable values
for a supposed print job, and to request an area within the constraints of
the printable area to be used in a print job.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

To query for the printable area, a client must supply a suitable context.
Without specifying at the very least the size of the media being used no
meaningful value for printable area can be obtained.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

The attribute is not described in terms of the distance from the edge of the
paper, in part to emphasise that this attribute is not independent of a
particular media, but must be described within the context of a choice of
other attributes. Additionally it is usually more convenient for a client to
use the printable area.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

The hardware's minimum margins is not just a property of the printer, but may
be a function of the media size, orientation, media type, and any specified
finishings.

PrintService

provides the method to query the supported
values of an attribute in a suitable context : See

PrintService.getSupportedAttributeValues()

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

The rectangular printable area is defined thus: The (x,y) origin is
positioned at the top-left of the paper in portrait mode regardless of the
orientation specified in the requesting context. For example a printable area
for A4 paper in portrait or landscape orientation will have height
> width.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

A printable area attribute's values are stored internally as integers in
units of micrometers (µm), where 1 micrometer = 10

-6

meter =
1/1000 millimeter = 1/25400 inch. This permits dimensions to be represented
exactly to a precision of 1/1000 mm (= 1 µm) or 1/100 inch (= 254
µm). If fractional inches are expressed in negative powers of two, this
permits dimensions to be represented exactly to a precision of 1/8 inch
(= 3175 µm) but not 1/16 inch (because 1/16 inch does not equal an
integral number of µm).

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

IPP Compatibility:

MediaPrintableArea is not an IPP attribute.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

INCH

Value to indicate units of inches (in).

static int

MM

Value to indicate units of millimeters (mm).

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MediaPrintableArea

​(float x,
float y,
float w,
float h,
int units)

Constructs a

MediaPrintableArea

object from floating point
values.

MediaPrintableArea

​(int x,
int y,
int w,
int h,
int units)

Constructs a

MediaPrintableArea

object from integer values.

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

Returns whether this media margins attribute is equivalent to the passed
in object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

float

getHeight

​(int units)

Get the

height

of the printable area in the specified units.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

float[]

getPrintableArea

​(int units)

Get the printable area as an array of 4 values in the order

x, y, w, h

.

float

getWidth

​(int units)

Get the

width

of the printable area in the specified units.

float

getX

​(int units)

Get the

x

location of the origin of the printable area in the
specified units.

float

getY

​(int units)

Get the

y

location of the origin of the printable area in the
specified units.

int

hashCode

()

Returns a hash code value for this attribute.

String

toString

()

Returns a string version of this rectangular size attribute in mm.

String

toString

​(int units,

String

unitsName)

Returns a string version of this rectangular size attribute in the given
units.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

INCH

Value to indicate units of inches (in).

static int

MM

Value to indicate units of millimeters (mm).

---

#### Field Summary

Value to indicate units of inches (in).

Value to indicate units of millimeters (mm).

Constructor Summary

Constructors

Constructor

Description

MediaPrintableArea

​(float x,
float y,
float w,
float h,
int units)

Constructs a

MediaPrintableArea

object from floating point
values.

MediaPrintableArea

​(int x,
int y,
int w,
int h,
int units)

Constructs a

MediaPrintableArea

object from integer values.

---

#### Constructor Summary

Constructs a

MediaPrintableArea

object from floating point
values.

Constructs a

MediaPrintableArea

object from integer values.

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

Returns whether this media margins attribute is equivalent to the passed
in object.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

float

getHeight

​(int units)

Get the

height

of the printable area in the specified units.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

float[]

getPrintableArea

​(int units)

Get the printable area as an array of 4 values in the order

x, y, w, h

.

float

getWidth

​(int units)

Get the

width

of the printable area in the specified units.

float

getX

​(int units)

Get the

x

location of the origin of the printable area in the
specified units.

float

getY

​(int units)

Get the

y

location of the origin of the printable area in the
specified units.

int

hashCode

()

Returns a hash code value for this attribute.

String

toString

()

Returns a string version of this rectangular size attribute in mm.

String

toString

​(int units,

String

unitsName)

Returns a string version of this rectangular size attribute in the given
units.

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

Returns whether this media margins attribute is equivalent to the passed
in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the

height

of the printable area in the specified units.

Get the name of the category of which this attribute value is an
instance.

Get the printable area as an array of 4 values in the order

x, y, w, h

.

Get the

width

of the printable area in the specified units.

Get the

x

location of the origin of the printable area in the
specified units.

Get the

y

location of the origin of the printable area in the
specified units.

Returns a hash code value for this attribute.

Returns a string version of this rectangular size attribute in mm.

Returns a string version of this rectangular size attribute in the given
units.

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

============ FIELD DETAIL ===========

- Field Detail

- INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

- MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaPrintableArea

```java
public MediaPrintableArea​(float x,
float y,
float w,
float h,
int units)
```

Constructs a

MediaPrintableArea

object from floating point
values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

- MediaPrintableArea

```java
public MediaPrintableArea​(int x,
int y,
int w,
int h,
int units)
```

Constructs a

MediaPrintableArea

object from integer values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

============ METHOD DETAIL ==========

- Method Detail

- getPrintableArea

```java
public float[] getPrintableArea​(int units)
```

Get the printable area as an array of 4 values in the order

x, y, w, h

. The values returned are in the given units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** printable area as array of

x, y, w, h

in the specified
units
**Throws:** IllegalArgumentException

- if

units < 1

- getX

```java
public float getX​(int units)
```

Get the

x

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** x

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getY

```java
public float getY​(int units)
```

Get the

y

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** y

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getWidth

```java
public float getWidth​(int units)
```

Get the

width

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** width

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getHeight

```java
public float getHeight​(int units)
```

Get the

height

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** height

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media margins attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

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
margins attribute,

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

MediaPrintableArea

, the category is class

MediaPrintableArea

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

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

- toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this rectangular size attribute in the given
units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

"in"

or

"mm"

.
If

null

, no units name is appended to the result
**Returns:** string version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

- toString

```java
public
String
toString()
```

Returns a string version of this rectangular size attribute in mm.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Field Detail

- INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

- MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

---

#### Field Detail

INCH

```java
public static final int INCH
```

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

**See Also:** Constant Field Values

---

#### INCH

public static final int INCH

Value to indicate units of inches (in). It is actually the conversion
factor by which to multiply inches to yield µm (25400).

MM

```java
public static final int MM
```

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

**See Also:** Constant Field Values

---

#### MM

public static final int MM

Value to indicate units of millimeters (mm). It is actually the
conversion factor by which to multiply mm to yield µm (1000).

Constructor Detail

- MediaPrintableArea

```java
public MediaPrintableArea​(float x,
float y,
float w,
float h,
int units)
```

Constructs a

MediaPrintableArea

object from floating point
values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

- MediaPrintableArea

```java
public MediaPrintableArea​(int x,
int y,
int w,
int h,
int units)
```

Constructs a

MediaPrintableArea

object from integer values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

---

#### Constructor Detail

MediaPrintableArea

```java
public MediaPrintableArea​(float x,
float y,
float w,
float h,
int units)
```

Constructs a

MediaPrintableArea

object from floating point
values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

---

#### MediaPrintableArea

public MediaPrintableArea​(float x,
float y,
float w,
float h,
int units)

Constructs a

MediaPrintableArea

object from floating point
values.

MediaPrintableArea

```java
public MediaPrintableArea​(int x,
int y,
int w,
int h,
int units)
```

Constructs a

MediaPrintableArea

object from integer values.

**Parameters:** x

- printable x
**Parameters:** y

- printable y
**Parameters:** w

- printable width
**Parameters:** h

- printable height
**Parameters:** units

- in which the values are expressed
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

w <= 0

or

h <= 0

or

units < 1

---

#### MediaPrintableArea

public MediaPrintableArea​(int x,
int y,
int w,
int h,
int units)

Constructs a

MediaPrintableArea

object from integer values.

Method Detail

- getPrintableArea

```java
public float[] getPrintableArea​(int units)
```

Get the printable area as an array of 4 values in the order

x, y, w, h

. The values returned are in the given units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** printable area as array of

x, y, w, h

in the specified
units
**Throws:** IllegalArgumentException

- if

units < 1

- getX

```java
public float getX​(int units)
```

Get the

x

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** x

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getY

```java
public float getY​(int units)
```

Get the

y

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** y

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getWidth

```java
public float getWidth​(int units)
```

Get the

width

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** width

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

- getHeight

```java
public float getHeight​(int units)
```

Get the

height

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** height

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media margins attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

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
margins attribute,

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

MediaPrintableArea

, the category is class

MediaPrintableArea

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

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

- toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this rectangular size attribute in the given
units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

"in"

or

"mm"

.
If

null

, no units name is appended to the result
**Returns:** string version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

- toString

```java
public
String
toString()
```

Returns a string version of this rectangular size attribute in mm.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

- hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

getPrintableArea

```java
public float[] getPrintableArea​(int units)
```

Get the printable area as an array of 4 values in the order

x, y, w, h

. The values returned are in the given units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** printable area as array of

x, y, w, h

in the specified
units
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getPrintableArea

public float[] getPrintableArea​(int units)

Get the printable area as an array of 4 values in the order

x, y, w, h

. The values returned are in the given units.

getX

```java
public float getX​(int units)
```

Get the

x

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** x

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getX

public float getX​(int units)

Get the

x

location of the origin of the printable area in the
specified units.

getY

```java
public float getY​(int units)
```

Get the

y

location of the origin of the printable area in the
specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** y

location of the origin of the printable area in the
specified units
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getY

public float getY​(int units)

Get the

y

location of the origin of the printable area in the
specified units.

getWidth

```java
public float getWidth​(int units)
```

Get the

width

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** width

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getWidth

public float getWidth​(int units)

Get the

width

of the printable area in the specified units.

getHeight

```java
public float getHeight​(int units)
```

Get the

height

of the printable area in the specified units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Returns:** height

of the printable area in the specified units
**Throws:** IllegalArgumentException

- if

units < 1

---

#### getHeight

public float getHeight​(int units)

Get the

height

of the printable area in the specified units.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media margins attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

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
margins attribute,

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

Returns whether this media margins attribute is equivalent to the passed
in object. To be equivalent, all of the following conditions must be
true:

- object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

object

is not

null

.

object

is an instance of class

MediaPrintableArea

.

The origin and dimensions are the same.

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

MediaPrintableArea

, the category is class

MediaPrintableArea

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

MediaPrintableArea

, the category is class

MediaPrintableArea

itself.

For class

MediaPrintableArea

, the category is class

MediaPrintableArea

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

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

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

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

For class

MediaPrintableArea

, the category name is

"media-printable-area"

.

This is not an IPP V1.1 attribute.

This is not an IPP V1.1 attribute.

toString

```java
public
String
toString​(int units,

String
unitsName)
```

Returns a string version of this rectangular size attribute in the given
units.

**Parameters:** units

- unit conversion factor, e.g.

INCH

or

MM
**Parameters:** unitsName

- units name string, e.g.

"in"

or

"mm"

.
If

null

, no units name is appended to the result
**Returns:** string version of this two-dimensional size attribute
**Throws:** IllegalArgumentException

- if

units < 1

---

#### toString

public

String

toString​(int units,

String

unitsName)

Returns a string version of this rectangular size attribute in the given
units.

toString

```java
public
String
toString()
```

Returns a string version of this rectangular size attribute in mm.

**Overrides:** toString

in class

Object
**Returns:** a string representation of the object.

---

#### toString

public

String

toString()

Returns a string version of this rectangular size attribute in mm.

hashCode

```java
public int hashCode()
```

Returns a hash code value for this attribute.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code value for this attribute.

---

