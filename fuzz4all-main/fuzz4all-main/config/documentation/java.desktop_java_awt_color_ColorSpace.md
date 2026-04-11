# Class ColorSpace

**Source:** `java.desktop\java\awt\color\ColorSpace.html`

### Class Description

```java
public abstract class
ColorSpace

extends
Object

implements
Serializable
```

This abstract class is used to serve as a color space tag to identify the
specific color space of a Color object or, via a ColorModel object,
of an Image, a BufferedImage, or a GraphicsDevice. It contains
methods that transform colors in a specific color space to/from sRGB
and to/from a well-defined CIEXYZ color space.

For purposes of the methods in this class, colors are represented as
arrays of color components represented as floats in a normalized range
defined by each ColorSpace. For many ColorSpaces (e.g. sRGB), this
range is 0.0 to 1.0. However, some ColorSpaces have components whose
values have a different range. Methods are provided to inquire per
component minimum and maximum normalized values.

Several variables are defined for purposes of referring to color
space types (e.g. TYPE_RGB, TYPE_XYZ, etc.) and to refer to specific
color spaces (e.g. CS_sRGB and CS_CIEXYZ).
sRGB is a proposed standard RGB color space. For more information,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

**All Implemented Interfaces:** Serializable

---

### Field Details

#### @Native

public static final int TYPE_XYZ

Any of the family of XYZ color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_Lab

Any of the family of Lab color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_Luv

Any of the family of Luv color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_YCbCr

Any of the family of YCbCr color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_Yxy

Any of the family of Yxy color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_RGB

Any of the family of RGB color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_GRAY

Any of the family of GRAY color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_HSV

Any of the family of HSV color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_HLS

Any of the family of HLS color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_CMYK

Any of the family of CMYK color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_CMY

Any of the family of CMY color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_2CLR

Generic 2 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_3CLR

Generic 3 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_4CLR

Generic 4 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_5CLR

Generic 5 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_6CLR

Generic 6 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_7CLR

Generic 7 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_8CLR

Generic 8 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_9CLR

Generic 9 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_ACLR

Generic 10 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_BCLR

Generic 11 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_CCLR

Generic 12 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_DCLR

Generic 13 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_ECLR

Generic 14 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TYPE_FCLR

Generic 15 component color spaces.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CS_sRGB

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CS_LINEAR_RGB

A built-in linear RGB color space. This space is based on the
same RGB primaries as CS_sRGB, but has a linear tone reproduction curve.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CS_CIEXYZ

The CIEXYZ conversion color space defined above.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CS_PYCC

The Photo YCC conversion color space.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int CS_GRAY

The built-in linear gray scale color space.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected ColorSpace​(int type,
int numcomponents)

Constructs a ColorSpace object given a color space type
and the number of components.

**Parameters:**
- type

- one of the

ColorSpace

type constants
- numcomponents

- the number of components in the color space

---

### Method Details

#### public static
ColorSpace
getInstance​(int colorspace)

Returns a ColorSpace representing one of the specific
predefined color spaces.

**Parameters:**
- colorspace

- a specific color space identified by one of
the predefined class constants (e.g. CS_sRGB, CS_LINEAR_RGB,
CS_CIEXYZ, CS_GRAY, or CS_PYCC)

**Returns:**
- the requested

ColorSpace

object

---

#### public boolean isCS_sRGB()

Returns true if the ColorSpace is CS_sRGB.

**Returns:**
- true

if this is a

CS_sRGB

color
space,

false

if it is not

---

#### public abstract float[] toRGB​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:**
- colorvalue

- a float array with length of at least the number
of components in this ColorSpace

**Returns:**
- a float array of length 3

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace

---

#### public abstract float[] fromRGB​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:**
- rgbvalue

- a float array with length of at least 3

**Returns:**
- a float array with length equal to the number of
components in this ColorSpace

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least 3

---

#### public abstract float[] toCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:**
- colorvalue

- a float array with length of at least the number
of components in this ColorSpace

**Returns:**
- a float array of length 3

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### public abstract float[] fromCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:**
- colorvalue

- a float array with length of at least 3

**Returns:**
- a float array with length equal to the number of
components in this ColorSpace

**Throws:**
- ArrayIndexOutOfBoundsException

- if array length is not
at least 3

---

#### public int getType()

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...). The type defines the
number of components of the color space and the interpretation,
e.g. TYPE_RGB identifies a color space with three components - red,
green, and blue. It does not define the particular color
characteristics of the space, e.g. the chromaticities of the
primaries.

**Returns:**
- the type constant that represents the type of this

ColorSpace

---

#### public int getNumComponents()

Returns the number of components of this ColorSpace.

**Returns:**
- The number of components in this

ColorSpace

.

---

#### public
String
getName​(int idx)

Returns the name of the component given the component index.

**Parameters:**
- idx

- the component index

**Returns:**
- the name of the component at the specified index

**Throws:**
- IllegalArgumentException

- if

idx

is
less than 0 or greater than numComponents - 1

---

#### public float getMinValue​(int component)

Returns the minimum normalized color component value for the
specified component. The default implementation in this abstract
class returns 0.0 for all components. Subclasses should override
this method if necessary.

**Parameters:**
- component

- the component index

**Returns:**
- the minimum normalized component value

**Throws:**
- IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1

**Since:**
- 1.4

---

#### public float getMaxValue​(int component)

Returns the maximum normalized color component value for the
specified component. The default implementation in this abstract
class returns 1.0 for all components. Subclasses should override
this method if necessary.

**Parameters:**
- component

- the component index

**Returns:**
- the maximum normalized component value

**Throws:**
- IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1

**Since:**
- 1.4

---

### Additional Sections

#### Class ColorSpace

java.lang.Object

- java.awt.color.ColorSpace

java.awt.color.ColorSpace

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** ICC_ColorSpace

```java
public abstract class
ColorSpace

extends
Object

implements
Serializable
```

This abstract class is used to serve as a color space tag to identify the
specific color space of a Color object or, via a ColorModel object,
of an Image, a BufferedImage, or a GraphicsDevice. It contains
methods that transform colors in a specific color space to/from sRGB
and to/from a well-defined CIEXYZ color space.

For purposes of the methods in this class, colors are represented as
arrays of color components represented as floats in a normalized range
defined by each ColorSpace. For many ColorSpaces (e.g. sRGB), this
range is 0.0 to 1.0. However, some ColorSpaces have components whose
values have a different range. Methods are provided to inquire per
component minimum and maximum normalized values.

Several variables are defined for purposes of referring to color
space types (e.g. TYPE_RGB, TYPE_XYZ, etc.) and to refer to specific
color spaces (e.g. CS_sRGB and CS_CIEXYZ).
sRGB is a proposed standard RGB color space. For more information,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

**See Also:** ICC_ColorSpace

,

Serialized Form

public abstract class

ColorSpace

extends

Object

implements

Serializable

This abstract class is used to serve as a color space tag to identify the
specific color space of a Color object or, via a ColorModel object,
of an Image, a BufferedImage, or a GraphicsDevice. It contains
methods that transform colors in a specific color space to/from sRGB
and to/from a well-defined CIEXYZ color space.

For purposes of the methods in this class, colors are represented as
arrays of color components represented as floats in a normalized range
defined by each ColorSpace. For many ColorSpaces (e.g. sRGB), this
range is 0.0 to 1.0. However, some ColorSpaces have components whose
values have a different range. Methods are provided to inquire per
component minimum and maximum normalized values.

Several variables are defined for purposes of referring to color
space types (e.g. TYPE_RGB, TYPE_XYZ, etc.) and to refer to specific
color spaces (e.g. CS_sRGB and CS_CIEXYZ).
sRGB is a proposed standard RGB color space. For more information,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

For purposes of the methods in this class, colors are represented as
arrays of color components represented as floats in a normalized range
defined by each ColorSpace. For many ColorSpaces (e.g. sRGB), this
range is 0.0 to 1.0. However, some ColorSpaces have components whose
values have a different range. Methods are provided to inquire per
component minimum and maximum normalized values.

Several variables are defined for purposes of referring to color
space types (e.g. TYPE_RGB, TYPE_XYZ, etc.) and to refer to specific
color spaces (e.g. CS_sRGB and CS_CIEXYZ).
sRGB is a proposed standard RGB color space. For more information,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

Several variables are defined for purposes of referring to color
space types (e.g. TYPE_RGB, TYPE_XYZ, etc.) and to refer to specific
color spaces (e.g. CS_sRGB and CS_CIEXYZ).
sRGB is a proposed standard RGB color space. For more information,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

The purpose of the methods to transform to/from the well-defined
CIEXYZ color space is to support conversions between any two color
spaces at a reasonably high degree of accuracy. It is expected that
particular implementations of subclasses of ColorSpace (e.g.
ICC_ColorSpace) will support high performance conversion based on
underlying platform color management systems.

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

The CS_CIEXYZ space used by the toCIEXYZ/fromCIEXYZ methods can be
described as follows:

```java
CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).
```

CIEXYZ
viewing illuminance: 200 lux
viewing white point: CIE D50
media white point: "that of a perfectly reflecting diffuser" -- D50
media black point: 0 lux or 0 Reflectance
flare: 1 percent
surround: 20percent of the media white point
media description: reflection print (i.e., RLAB, Hunt viewing media)
note: For developers creating an ICC profile for this conversion
space, the following is applicable. Use a simple Von Kries
white point adaptation folded into the 3X3 matrix parameters
and fold the flare and surround effects into the three
one-dimensional lookup tables (assuming one uses the minimal
model for monitors).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CS_CIEXYZ

The CIEXYZ conversion color space defined above.

static int

CS_GRAY

The built-in linear gray scale color space.

static int

CS_LINEAR_RGB

A built-in linear RGB color space.

static int

CS_PYCC

The Photo YCC conversion color space.

static int

CS_sRGB

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

static int

TYPE_2CLR

Generic 2 component color spaces.

static int

TYPE_3CLR

Generic 3 component color spaces.

static int

TYPE_4CLR

Generic 4 component color spaces.

static int

TYPE_5CLR

Generic 5 component color spaces.

static int

TYPE_6CLR

Generic 6 component color spaces.

static int

TYPE_7CLR

Generic 7 component color spaces.

static int

TYPE_8CLR

Generic 8 component color spaces.

static int

TYPE_9CLR

Generic 9 component color spaces.

static int

TYPE_ACLR

Generic 10 component color spaces.

static int

TYPE_BCLR

Generic 11 component color spaces.

static int

TYPE_CCLR

Generic 12 component color spaces.

static int

TYPE_CMY

Any of the family of CMY color spaces.

static int

TYPE_CMYK

Any of the family of CMYK color spaces.

static int

TYPE_DCLR

Generic 13 component color spaces.

static int

TYPE_ECLR

Generic 14 component color spaces.

static int

TYPE_FCLR

Generic 15 component color spaces.

static int

TYPE_GRAY

Any of the family of GRAY color spaces.

static int

TYPE_HLS

Any of the family of HLS color spaces.

static int

TYPE_HSV

Any of the family of HSV color spaces.

static int

TYPE_Lab

Any of the family of Lab color spaces.

static int

TYPE_Luv

Any of the family of Luv color spaces.

static int

TYPE_RGB

Any of the family of RGB color spaces.

static int

TYPE_XYZ

Any of the family of XYZ color spaces.

static int

TYPE_YCbCr

Any of the family of YCbCr color spaces.

static int

TYPE_Yxy

Any of the family of Yxy color spaces.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorSpace

​(int type,
int numcomponents)

Constructs a ColorSpace object given a color space type
and the number of components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract float[]

fromCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

abstract float[]

fromRGB

​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

static

ColorSpace

getInstance

​(int colorspace)

Returns a ColorSpace representing one of the specific
predefined color spaces.

float

getMaxValue

​(int component)

Returns the maximum normalized color component value for the
specified component.

float

getMinValue

​(int component)

Returns the minimum normalized color component value for the
specified component.

String

getName

​(int idx)

Returns the name of the component given the component index.

int

getNumComponents

()

Returns the number of components of this ColorSpace.

int

getType

()

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...).

boolean

isCS_sRGB

()

Returns true if the ColorSpace is CS_sRGB.

abstract float[]

toCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

abstract float[]

toRGB

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

CS_CIEXYZ

The CIEXYZ conversion color space defined above.

static int

CS_GRAY

The built-in linear gray scale color space.

static int

CS_LINEAR_RGB

A built-in linear RGB color space.

static int

CS_PYCC

The Photo YCC conversion color space.

static int

CS_sRGB

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

static int

TYPE_2CLR

Generic 2 component color spaces.

static int

TYPE_3CLR

Generic 3 component color spaces.

static int

TYPE_4CLR

Generic 4 component color spaces.

static int

TYPE_5CLR

Generic 5 component color spaces.

static int

TYPE_6CLR

Generic 6 component color spaces.

static int

TYPE_7CLR

Generic 7 component color spaces.

static int

TYPE_8CLR

Generic 8 component color spaces.

static int

TYPE_9CLR

Generic 9 component color spaces.

static int

TYPE_ACLR

Generic 10 component color spaces.

static int

TYPE_BCLR

Generic 11 component color spaces.

static int

TYPE_CCLR

Generic 12 component color spaces.

static int

TYPE_CMY

Any of the family of CMY color spaces.

static int

TYPE_CMYK

Any of the family of CMYK color spaces.

static int

TYPE_DCLR

Generic 13 component color spaces.

static int

TYPE_ECLR

Generic 14 component color spaces.

static int

TYPE_FCLR

Generic 15 component color spaces.

static int

TYPE_GRAY

Any of the family of GRAY color spaces.

static int

TYPE_HLS

Any of the family of HLS color spaces.

static int

TYPE_HSV

Any of the family of HSV color spaces.

static int

TYPE_Lab

Any of the family of Lab color spaces.

static int

TYPE_Luv

Any of the family of Luv color spaces.

static int

TYPE_RGB

Any of the family of RGB color spaces.

static int

TYPE_XYZ

Any of the family of XYZ color spaces.

static int

TYPE_YCbCr

Any of the family of YCbCr color spaces.

static int

TYPE_Yxy

Any of the family of Yxy color spaces.

---

#### Field Summary

The CIEXYZ conversion color space defined above.

The built-in linear gray scale color space.

A built-in linear RGB color space.

The Photo YCC conversion color space.

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

Generic 2 component color spaces.

Generic 3 component color spaces.

Generic 4 component color spaces.

Generic 5 component color spaces.

Generic 6 component color spaces.

Generic 7 component color spaces.

Generic 8 component color spaces.

Generic 9 component color spaces.

Generic 10 component color spaces.

Generic 11 component color spaces.

Generic 12 component color spaces.

Any of the family of CMY color spaces.

Any of the family of CMYK color spaces.

Generic 13 component color spaces.

Generic 14 component color spaces.

Generic 15 component color spaces.

Any of the family of GRAY color spaces.

Any of the family of HLS color spaces.

Any of the family of HSV color spaces.

Any of the family of Lab color spaces.

Any of the family of Luv color spaces.

Any of the family of RGB color spaces.

Any of the family of XYZ color spaces.

Any of the family of YCbCr color spaces.

Any of the family of Yxy color spaces.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

ColorSpace

​(int type,
int numcomponents)

Constructs a ColorSpace object given a color space type
and the number of components.

---

#### Constructor Summary

Constructs a ColorSpace object given a color space type
and the number of components.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract float[]

fromCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

abstract float[]

fromRGB

​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

static

ColorSpace

getInstance

​(int colorspace)

Returns a ColorSpace representing one of the specific
predefined color spaces.

float

getMaxValue

​(int component)

Returns the maximum normalized color component value for the
specified component.

float

getMinValue

​(int component)

Returns the minimum normalized color component value for the
specified component.

String

getName

​(int idx)

Returns the name of the component given the component index.

int

getNumComponents

()

Returns the number of components of this ColorSpace.

int

getType

()

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...).

boolean

isCS_sRGB

()

Returns true if the ColorSpace is CS_sRGB.

abstract float[]

toCIEXYZ

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

abstract float[]

toRGB

​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

Returns a ColorSpace representing one of the specific
predefined color spaces.

Returns the maximum normalized color component value for the
specified component.

Returns the minimum normalized color component value for the
specified component.

Returns the name of the component given the component index.

Returns the number of components of this ColorSpace.

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...).

Returns true if the ColorSpace is CS_sRGB.

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

- TYPE_XYZ

```java
@Native

public static final int TYPE_XYZ
```

Any of the family of XYZ color spaces.

**See Also:** Constant Field Values

- TYPE_Lab

```java
@Native

public static final int TYPE_Lab
```

Any of the family of Lab color spaces.

**See Also:** Constant Field Values

- TYPE_Luv

```java
@Native

public static final int TYPE_Luv
```

Any of the family of Luv color spaces.

**See Also:** Constant Field Values

- TYPE_YCbCr

```java
@Native

public static final int TYPE_YCbCr
```

Any of the family of YCbCr color spaces.

**See Also:** Constant Field Values

- TYPE_Yxy

```java
@Native

public static final int TYPE_Yxy
```

Any of the family of Yxy color spaces.

**See Also:** Constant Field Values

- TYPE_RGB

```java
@Native

public static final int TYPE_RGB
```

Any of the family of RGB color spaces.

**See Also:** Constant Field Values

- TYPE_GRAY

```java
@Native

public static final int TYPE_GRAY
```

Any of the family of GRAY color spaces.

**See Also:** Constant Field Values

- TYPE_HSV

```java
@Native

public static final int TYPE_HSV
```

Any of the family of HSV color spaces.

**See Also:** Constant Field Values

- TYPE_HLS

```java
@Native

public static final int TYPE_HLS
```

Any of the family of HLS color spaces.

**See Also:** Constant Field Values

- TYPE_CMYK

```java
@Native

public static final int TYPE_CMYK
```

Any of the family of CMYK color spaces.

**See Also:** Constant Field Values

- TYPE_CMY

```java
@Native

public static final int TYPE_CMY
```

Any of the family of CMY color spaces.

**See Also:** Constant Field Values

- TYPE_2CLR

```java
@Native

public static final int TYPE_2CLR
```

Generic 2 component color spaces.

**See Also:** Constant Field Values

- TYPE_3CLR

```java
@Native

public static final int TYPE_3CLR
```

Generic 3 component color spaces.

**See Also:** Constant Field Values

- TYPE_4CLR

```java
@Native

public static final int TYPE_4CLR
```

Generic 4 component color spaces.

**See Also:** Constant Field Values

- TYPE_5CLR

```java
@Native

public static final int TYPE_5CLR
```

Generic 5 component color spaces.

**See Also:** Constant Field Values

- TYPE_6CLR

```java
@Native

public static final int TYPE_6CLR
```

Generic 6 component color spaces.

**See Also:** Constant Field Values

- TYPE_7CLR

```java
@Native

public static final int TYPE_7CLR
```

Generic 7 component color spaces.

**See Also:** Constant Field Values

- TYPE_8CLR

```java
@Native

public static final int TYPE_8CLR
```

Generic 8 component color spaces.

**See Also:** Constant Field Values

- TYPE_9CLR

```java
@Native

public static final int TYPE_9CLR
```

Generic 9 component color spaces.

**See Also:** Constant Field Values

- TYPE_ACLR

```java
@Native

public static final int TYPE_ACLR
```

Generic 10 component color spaces.

**See Also:** Constant Field Values

- TYPE_BCLR

```java
@Native

public static final int TYPE_BCLR
```

Generic 11 component color spaces.

**See Also:** Constant Field Values

- TYPE_CCLR

```java
@Native

public static final int TYPE_CCLR
```

Generic 12 component color spaces.

**See Also:** Constant Field Values

- TYPE_DCLR

```java
@Native

public static final int TYPE_DCLR
```

Generic 13 component color spaces.

**See Also:** Constant Field Values

- TYPE_ECLR

```java
@Native

public static final int TYPE_ECLR
```

Generic 14 component color spaces.

**See Also:** Constant Field Values

- TYPE_FCLR

```java
@Native

public static final int TYPE_FCLR
```

Generic 15 component color spaces.

**See Also:** Constant Field Values

- CS_sRGB

```java
@Native

public static final int CS_sRGB
```

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**See Also:** Constant Field Values

- CS_LINEAR_RGB

```java
@Native

public static final int CS_LINEAR_RGB
```

A built-in linear RGB color space. This space is based on the
same RGB primaries as CS_sRGB, but has a linear tone reproduction curve.

**See Also:** Constant Field Values

- CS_CIEXYZ

```java
@Native

public static final int CS_CIEXYZ
```

The CIEXYZ conversion color space defined above.

**See Also:** Constant Field Values

- CS_PYCC

```java
@Native

public static final int CS_PYCC
```

The Photo YCC conversion color space.

**See Also:** Constant Field Values

- CS_GRAY

```java
@Native

public static final int CS_GRAY
```

The built-in linear gray scale color space.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ColorSpace

```java
protected ColorSpace​(int type,
int numcomponents)
```

Constructs a ColorSpace object given a color space type
and the number of components.

**Parameters:** type

- one of the

ColorSpace

type constants
**Parameters:** numcomponents

- the number of components in the color space

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
ColorSpace
getInstance​(int colorspace)
```

Returns a ColorSpace representing one of the specific
predefined color spaces.

**Parameters:** colorspace

- a specific color space identified by one of
the predefined class constants (e.g. CS_sRGB, CS_LINEAR_RGB,
CS_CIEXYZ, CS_GRAY, or CS_PYCC)
**Returns:** the requested

ColorSpace

object

- isCS_sRGB

```java
public boolean isCS_sRGB()
```

Returns true if the ColorSpace is CS_sRGB.

**Returns:** true

if this is a

CS_sRGB

color
space,

false

if it is not

- toRGB

```java
public abstract float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace

- fromRGB

```java
public abstract float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** rgbvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

- toCIEXYZ

```java
public abstract float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromCIEXYZ

```java
public abstract float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

- getType

```java
public int getType()
```

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...). The type defines the
number of components of the color space and the interpretation,
e.g. TYPE_RGB identifies a color space with three components - red,
green, and blue. It does not define the particular color
characteristics of the space, e.g. the chromaticities of the
primaries.

**Returns:** the type constant that represents the type of this

ColorSpace

- getNumComponents

```java
public int getNumComponents()
```

Returns the number of components of this ColorSpace.

**Returns:** The number of components in this

ColorSpace

.

- getName

```java
public
String
getName​(int idx)
```

Returns the name of the component given the component index.

**Parameters:** idx

- the component index
**Returns:** the name of the component at the specified index
**Throws:** IllegalArgumentException

- if

idx

is
less than 0 or greater than numComponents - 1

- getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. The default implementation in this abstract
class returns 0.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the minimum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

- getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. The default implementation in this abstract
class returns 1.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the maximum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

Field Detail

- TYPE_XYZ

```java
@Native

public static final int TYPE_XYZ
```

Any of the family of XYZ color spaces.

**See Also:** Constant Field Values

- TYPE_Lab

```java
@Native

public static final int TYPE_Lab
```

Any of the family of Lab color spaces.

**See Also:** Constant Field Values

- TYPE_Luv

```java
@Native

public static final int TYPE_Luv
```

Any of the family of Luv color spaces.

**See Also:** Constant Field Values

- TYPE_YCbCr

```java
@Native

public static final int TYPE_YCbCr
```

Any of the family of YCbCr color spaces.

**See Also:** Constant Field Values

- TYPE_Yxy

```java
@Native

public static final int TYPE_Yxy
```

Any of the family of Yxy color spaces.

**See Also:** Constant Field Values

- TYPE_RGB

```java
@Native

public static final int TYPE_RGB
```

Any of the family of RGB color spaces.

**See Also:** Constant Field Values

- TYPE_GRAY

```java
@Native

public static final int TYPE_GRAY
```

Any of the family of GRAY color spaces.

**See Also:** Constant Field Values

- TYPE_HSV

```java
@Native

public static final int TYPE_HSV
```

Any of the family of HSV color spaces.

**See Also:** Constant Field Values

- TYPE_HLS

```java
@Native

public static final int TYPE_HLS
```

Any of the family of HLS color spaces.

**See Also:** Constant Field Values

- TYPE_CMYK

```java
@Native

public static final int TYPE_CMYK
```

Any of the family of CMYK color spaces.

**See Also:** Constant Field Values

- TYPE_CMY

```java
@Native

public static final int TYPE_CMY
```

Any of the family of CMY color spaces.

**See Also:** Constant Field Values

- TYPE_2CLR

```java
@Native

public static final int TYPE_2CLR
```

Generic 2 component color spaces.

**See Also:** Constant Field Values

- TYPE_3CLR

```java
@Native

public static final int TYPE_3CLR
```

Generic 3 component color spaces.

**See Also:** Constant Field Values

- TYPE_4CLR

```java
@Native

public static final int TYPE_4CLR
```

Generic 4 component color spaces.

**See Also:** Constant Field Values

- TYPE_5CLR

```java
@Native

public static final int TYPE_5CLR
```

Generic 5 component color spaces.

**See Also:** Constant Field Values

- TYPE_6CLR

```java
@Native

public static final int TYPE_6CLR
```

Generic 6 component color spaces.

**See Also:** Constant Field Values

- TYPE_7CLR

```java
@Native

public static final int TYPE_7CLR
```

Generic 7 component color spaces.

**See Also:** Constant Field Values

- TYPE_8CLR

```java
@Native

public static final int TYPE_8CLR
```

Generic 8 component color spaces.

**See Also:** Constant Field Values

- TYPE_9CLR

```java
@Native

public static final int TYPE_9CLR
```

Generic 9 component color spaces.

**See Also:** Constant Field Values

- TYPE_ACLR

```java
@Native

public static final int TYPE_ACLR
```

Generic 10 component color spaces.

**See Also:** Constant Field Values

- TYPE_BCLR

```java
@Native

public static final int TYPE_BCLR
```

Generic 11 component color spaces.

**See Also:** Constant Field Values

- TYPE_CCLR

```java
@Native

public static final int TYPE_CCLR
```

Generic 12 component color spaces.

**See Also:** Constant Field Values

- TYPE_DCLR

```java
@Native

public static final int TYPE_DCLR
```

Generic 13 component color spaces.

**See Also:** Constant Field Values

- TYPE_ECLR

```java
@Native

public static final int TYPE_ECLR
```

Generic 14 component color spaces.

**See Also:** Constant Field Values

- TYPE_FCLR

```java
@Native

public static final int TYPE_FCLR
```

Generic 15 component color spaces.

**See Also:** Constant Field Values

- CS_sRGB

```java
@Native

public static final int CS_sRGB
```

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**See Also:** Constant Field Values

- CS_LINEAR_RGB

```java
@Native

public static final int CS_LINEAR_RGB
```

A built-in linear RGB color space. This space is based on the
same RGB primaries as CS_sRGB, but has a linear tone reproduction curve.

**See Also:** Constant Field Values

- CS_CIEXYZ

```java
@Native

public static final int CS_CIEXYZ
```

The CIEXYZ conversion color space defined above.

**See Also:** Constant Field Values

- CS_PYCC

```java
@Native

public static final int CS_PYCC
```

The Photo YCC conversion color space.

**See Also:** Constant Field Values

- CS_GRAY

```java
@Native

public static final int CS_GRAY
```

The built-in linear gray scale color space.

**See Also:** Constant Field Values

---

#### Field Detail

TYPE_XYZ

```java
@Native

public static final int TYPE_XYZ
```

Any of the family of XYZ color spaces.

**See Also:** Constant Field Values

---

#### TYPE_XYZ

@Native

public static final int TYPE_XYZ

Any of the family of XYZ color spaces.

TYPE_Lab

```java
@Native

public static final int TYPE_Lab
```

Any of the family of Lab color spaces.

**See Also:** Constant Field Values

---

#### TYPE_Lab

@Native

public static final int TYPE_Lab

Any of the family of Lab color spaces.

TYPE_Luv

```java
@Native

public static final int TYPE_Luv
```

Any of the family of Luv color spaces.

**See Also:** Constant Field Values

---

#### TYPE_Luv

@Native

public static final int TYPE_Luv

Any of the family of Luv color spaces.

TYPE_YCbCr

```java
@Native

public static final int TYPE_YCbCr
```

Any of the family of YCbCr color spaces.

**See Also:** Constant Field Values

---

#### TYPE_YCbCr

@Native

public static final int TYPE_YCbCr

Any of the family of YCbCr color spaces.

TYPE_Yxy

```java
@Native

public static final int TYPE_Yxy
```

Any of the family of Yxy color spaces.

**See Also:** Constant Field Values

---

#### TYPE_Yxy

@Native

public static final int TYPE_Yxy

Any of the family of Yxy color spaces.

TYPE_RGB

```java
@Native

public static final int TYPE_RGB
```

Any of the family of RGB color spaces.

**See Also:** Constant Field Values

---

#### TYPE_RGB

@Native

public static final int TYPE_RGB

Any of the family of RGB color spaces.

TYPE_GRAY

```java
@Native

public static final int TYPE_GRAY
```

Any of the family of GRAY color spaces.

**See Also:** Constant Field Values

---

#### TYPE_GRAY

@Native

public static final int TYPE_GRAY

Any of the family of GRAY color spaces.

TYPE_HSV

```java
@Native

public static final int TYPE_HSV
```

Any of the family of HSV color spaces.

**See Also:** Constant Field Values

---

#### TYPE_HSV

@Native

public static final int TYPE_HSV

Any of the family of HSV color spaces.

TYPE_HLS

```java
@Native

public static final int TYPE_HLS
```

Any of the family of HLS color spaces.

**See Also:** Constant Field Values

---

#### TYPE_HLS

@Native

public static final int TYPE_HLS

Any of the family of HLS color spaces.

TYPE_CMYK

```java
@Native

public static final int TYPE_CMYK
```

Any of the family of CMYK color spaces.

**See Also:** Constant Field Values

---

#### TYPE_CMYK

@Native

public static final int TYPE_CMYK

Any of the family of CMYK color spaces.

TYPE_CMY

```java
@Native

public static final int TYPE_CMY
```

Any of the family of CMY color spaces.

**See Also:** Constant Field Values

---

#### TYPE_CMY

@Native

public static final int TYPE_CMY

Any of the family of CMY color spaces.

TYPE_2CLR

```java
@Native

public static final int TYPE_2CLR
```

Generic 2 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_2CLR

@Native

public static final int TYPE_2CLR

Generic 2 component color spaces.

TYPE_3CLR

```java
@Native

public static final int TYPE_3CLR
```

Generic 3 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_3CLR

@Native

public static final int TYPE_3CLR

Generic 3 component color spaces.

TYPE_4CLR

```java
@Native

public static final int TYPE_4CLR
```

Generic 4 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_4CLR

@Native

public static final int TYPE_4CLR

Generic 4 component color spaces.

TYPE_5CLR

```java
@Native

public static final int TYPE_5CLR
```

Generic 5 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_5CLR

@Native

public static final int TYPE_5CLR

Generic 5 component color spaces.

TYPE_6CLR

```java
@Native

public static final int TYPE_6CLR
```

Generic 6 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_6CLR

@Native

public static final int TYPE_6CLR

Generic 6 component color spaces.

TYPE_7CLR

```java
@Native

public static final int TYPE_7CLR
```

Generic 7 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_7CLR

@Native

public static final int TYPE_7CLR

Generic 7 component color spaces.

TYPE_8CLR

```java
@Native

public static final int TYPE_8CLR
```

Generic 8 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_8CLR

@Native

public static final int TYPE_8CLR

Generic 8 component color spaces.

TYPE_9CLR

```java
@Native

public static final int TYPE_9CLR
```

Generic 9 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_9CLR

@Native

public static final int TYPE_9CLR

Generic 9 component color spaces.

TYPE_ACLR

```java
@Native

public static final int TYPE_ACLR
```

Generic 10 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_ACLR

@Native

public static final int TYPE_ACLR

Generic 10 component color spaces.

TYPE_BCLR

```java
@Native

public static final int TYPE_BCLR
```

Generic 11 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_BCLR

@Native

public static final int TYPE_BCLR

Generic 11 component color spaces.

TYPE_CCLR

```java
@Native

public static final int TYPE_CCLR
```

Generic 12 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_CCLR

@Native

public static final int TYPE_CCLR

Generic 12 component color spaces.

TYPE_DCLR

```java
@Native

public static final int TYPE_DCLR
```

Generic 13 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_DCLR

@Native

public static final int TYPE_DCLR

Generic 13 component color spaces.

TYPE_ECLR

```java
@Native

public static final int TYPE_ECLR
```

Generic 14 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_ECLR

@Native

public static final int TYPE_ECLR

Generic 14 component color spaces.

TYPE_FCLR

```java
@Native

public static final int TYPE_FCLR
```

Generic 15 component color spaces.

**See Also:** Constant Field Values

---

#### TYPE_FCLR

@Native

public static final int TYPE_FCLR

Generic 15 component color spaces.

CS_sRGB

```java
@Native

public static final int CS_sRGB
```

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**See Also:** Constant Field Values

---

#### CS_sRGB

@Native

public static final int CS_sRGB

The sRGB color space defined at

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

CS_LINEAR_RGB

```java
@Native

public static final int CS_LINEAR_RGB
```

A built-in linear RGB color space. This space is based on the
same RGB primaries as CS_sRGB, but has a linear tone reproduction curve.

**See Also:** Constant Field Values

---

#### CS_LINEAR_RGB

@Native

public static final int CS_LINEAR_RGB

A built-in linear RGB color space. This space is based on the
same RGB primaries as CS_sRGB, but has a linear tone reproduction curve.

CS_CIEXYZ

```java
@Native

public static final int CS_CIEXYZ
```

The CIEXYZ conversion color space defined above.

**See Also:** Constant Field Values

---

#### CS_CIEXYZ

@Native

public static final int CS_CIEXYZ

The CIEXYZ conversion color space defined above.

CS_PYCC

```java
@Native

public static final int CS_PYCC
```

The Photo YCC conversion color space.

**See Also:** Constant Field Values

---

#### CS_PYCC

@Native

public static final int CS_PYCC

The Photo YCC conversion color space.

CS_GRAY

```java
@Native

public static final int CS_GRAY
```

The built-in linear gray scale color space.

**See Also:** Constant Field Values

---

#### CS_GRAY

@Native

public static final int CS_GRAY

The built-in linear gray scale color space.

Constructor Detail

- ColorSpace

```java
protected ColorSpace​(int type,
int numcomponents)
```

Constructs a ColorSpace object given a color space type
and the number of components.

**Parameters:** type

- one of the

ColorSpace

type constants
**Parameters:** numcomponents

- the number of components in the color space

---

#### Constructor Detail

ColorSpace

```java
protected ColorSpace​(int type,
int numcomponents)
```

Constructs a ColorSpace object given a color space type
and the number of components.

**Parameters:** type

- one of the

ColorSpace

type constants
**Parameters:** numcomponents

- the number of components in the color space

---

#### ColorSpace

protected ColorSpace​(int type,
int numcomponents)

Constructs a ColorSpace object given a color space type
and the number of components.

Method Detail

- getInstance

```java
public static
ColorSpace
getInstance​(int colorspace)
```

Returns a ColorSpace representing one of the specific
predefined color spaces.

**Parameters:** colorspace

- a specific color space identified by one of
the predefined class constants (e.g. CS_sRGB, CS_LINEAR_RGB,
CS_CIEXYZ, CS_GRAY, or CS_PYCC)
**Returns:** the requested

ColorSpace

object

- isCS_sRGB

```java
public boolean isCS_sRGB()
```

Returns true if the ColorSpace is CS_sRGB.

**Returns:** true

if this is a

CS_sRGB

color
space,

false

if it is not

- toRGB

```java
public abstract float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace

- fromRGB

```java
public abstract float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** rgbvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

- toCIEXYZ

```java
public abstract float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

- fromCIEXYZ

```java
public abstract float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

- getType

```java
public int getType()
```

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...). The type defines the
number of components of the color space and the interpretation,
e.g. TYPE_RGB identifies a color space with three components - red,
green, and blue. It does not define the particular color
characteristics of the space, e.g. the chromaticities of the
primaries.

**Returns:** the type constant that represents the type of this

ColorSpace

- getNumComponents

```java
public int getNumComponents()
```

Returns the number of components of this ColorSpace.

**Returns:** The number of components in this

ColorSpace

.

- getName

```java
public
String
getName​(int idx)
```

Returns the name of the component given the component index.

**Parameters:** idx

- the component index
**Returns:** the name of the component at the specified index
**Throws:** IllegalArgumentException

- if

idx

is
less than 0 or greater than numComponents - 1

- getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. The default implementation in this abstract
class returns 0.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the minimum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

- getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. The default implementation in this abstract
class returns 1.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the maximum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

---

#### Method Detail

getInstance

```java
public static
ColorSpace
getInstance​(int colorspace)
```

Returns a ColorSpace representing one of the specific
predefined color spaces.

**Parameters:** colorspace

- a specific color space identified by one of
the predefined class constants (e.g. CS_sRGB, CS_LINEAR_RGB,
CS_CIEXYZ, CS_GRAY, or CS_PYCC)
**Returns:** the requested

ColorSpace

object

---

#### getInstance

public static

ColorSpace

getInstance​(int colorspace)

Returns a ColorSpace representing one of the specific
predefined color spaces.

isCS_sRGB

```java
public boolean isCS_sRGB()
```

Returns true if the ColorSpace is CS_sRGB.

**Returns:** true

if this is a

CS_sRGB

color
space,

false

if it is not

---

#### isCS_sRGB

public boolean isCS_sRGB()

Returns true if the ColorSpace is CS_sRGB.

toRGB

```java
public abstract float[] toRGB​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace

---

#### toRGB

public abstract float[] toRGB​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into a value in the default CS_sRGB color space.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of this color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of the CS_sRGB color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

fromRGB

```java
public abstract float[] fromRGB​(float[] rgbvalue)
```

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

**Parameters:** rgbvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

---

#### fromRGB

public abstract float[] fromRGB​(float[] rgbvalue)

Transforms a color value assumed to be in the default CS_sRGB
color space into this ColorSpace.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

This method transforms color values using algorithms designed
to produce the best perceptual match between input and output
colors. In order to do colorimetric conversion of color values,
you should use the

toCIEXYZ

method of the CS_sRGB color space to first convert from the input
color space to the CS_CIEXYZ color space, and then use the

fromCIEXYZ

method of this color space to
convert from CS_CIEXYZ to the output color space.
See

toCIEXYZ

and

fromCIEXYZ

for further information.

toCIEXYZ

```java
public abstract float[] toCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least the number
of components in this ColorSpace
**Returns:** a float array of length 3
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least the number of components in this ColorSpace.

---

#### toCIEXYZ

public abstract float[] toCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in this ColorSpace
into the CS_CIEXYZ conversion color space.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ values returned by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. This
representation is not the same as the XYZ values that would
be measured from the given color value by a colorimeter.
A further transformation is necessary to compute the XYZ values
that would be measured using current CIE recommended practices.
See the

toCIEXYZ

method of

ICC_ColorSpace

for further information.

fromCIEXYZ

```java
public abstract float[] fromCIEXYZ​(float[] colorvalue)
```

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

**Parameters:** colorvalue

- a float array with length of at least 3
**Returns:** a float array with length equal to the number of
components in this ColorSpace
**Throws:** ArrayIndexOutOfBoundsException

- if array length is not
at least 3

---

#### fromCIEXYZ

public abstract float[] fromCIEXYZ​(float[] colorvalue)

Transforms a color value assumed to be in the CS_CIEXYZ conversion
color space into this ColorSpace.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

This method transforms color values using relative colorimetry,
as defined by the International Color Consortium standard. This
means that the XYZ argument values taken by this method are represented
relative to the D50 white point of the CS_CIEXYZ color space.
This representation is useful in a two-step color conversion
process in which colors are transformed from an input color
space to CS_CIEXYZ and then to an output color space. The color
values returned by this method are not those that would produce
the XYZ value passed to the method when measured by a colorimeter.
If you have XYZ values corresponding to measurements made using
current CIE recommended practices, they must be converted to D50
relative values before being passed to this method.
See the

fromCIEXYZ

method of

ICC_ColorSpace

for further information.

getType

```java
public int getType()
```

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...). The type defines the
number of components of the color space and the interpretation,
e.g. TYPE_RGB identifies a color space with three components - red,
green, and blue. It does not define the particular color
characteristics of the space, e.g. the chromaticities of the
primaries.

**Returns:** the type constant that represents the type of this

ColorSpace

---

#### getType

public int getType()

Returns the color space type of this ColorSpace (for example
TYPE_RGB, TYPE_XYZ, ...). The type defines the
number of components of the color space and the interpretation,
e.g. TYPE_RGB identifies a color space with three components - red,
green, and blue. It does not define the particular color
characteristics of the space, e.g. the chromaticities of the
primaries.

getNumComponents

```java
public int getNumComponents()
```

Returns the number of components of this ColorSpace.

**Returns:** The number of components in this

ColorSpace

.

---

#### getNumComponents

public int getNumComponents()

Returns the number of components of this ColorSpace.

getName

```java
public
String
getName​(int idx)
```

Returns the name of the component given the component index.

**Parameters:** idx

- the component index
**Returns:** the name of the component at the specified index
**Throws:** IllegalArgumentException

- if

idx

is
less than 0 or greater than numComponents - 1

---

#### getName

public

String

getName​(int idx)

Returns the name of the component given the component index.

getMinValue

```java
public float getMinValue​(int component)
```

Returns the minimum normalized color component value for the
specified component. The default implementation in this abstract
class returns 0.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the minimum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

---

#### getMinValue

public float getMinValue​(int component)

Returns the minimum normalized color component value for the
specified component. The default implementation in this abstract
class returns 0.0 for all components. Subclasses should override
this method if necessary.

getMaxValue

```java
public float getMaxValue​(int component)
```

Returns the maximum normalized color component value for the
specified component. The default implementation in this abstract
class returns 1.0 for all components. Subclasses should override
this method if necessary.

**Parameters:** component

- the component index
**Returns:** the maximum normalized component value
**Throws:** IllegalArgumentException

- if component is less than 0 or
greater than numComponents - 1
**Since:** 1.4

---

#### getMaxValue

public float getMaxValue​(int component)

Returns the maximum normalized color component value for the
specified component. The default implementation in this abstract
class returns 1.0 for all components. Subclasses should override
this method if necessary.

---

