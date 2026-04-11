# Class Color

**Source:** `java.desktop\java\awt\Color.html`

### Class Description

```java
public class
Color

extends
Object

implements
Paint
,
Serializable
```

The

Color

class is used to encapsulate colors in the default
sRGB color space or colors in arbitrary color spaces identified by a

ColorSpace

. Every color has an implicit alpha value of 1.0 or
an explicit one provided in the constructor. The alpha value
defines the transparency of a color and can be represented by
a float value in the range 0.0 - 1.0 or 0 - 255.
An alpha value of 1.0 or 255 means that the color is completely
opaque and an alpha value of 0 or 0.0 means that the color is
completely transparent.
When constructing a

Color

with an explicit alpha or
getting the color/alpha components of a

Color

, the color
components are never premultiplied by the alpha component.

The default color space for the Java 2D(tm) API is sRGB, a proposed
standard RGB color space. For further information on sRGB,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

---

### Field Details

#### public static final
Color
white

The color white. In the default sRGB space.

---

#### public static final
Color
WHITE

The color white. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
lightGray

The color light gray. In the default sRGB space.

---

#### public static final
Color
LIGHT_GRAY

The color light gray. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
gray

The color gray. In the default sRGB space.

---

#### public static final
Color
GRAY

The color gray. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
darkGray

The color dark gray. In the default sRGB space.

---

#### public static final
Color
DARK_GRAY

The color dark gray. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
black

The color black. In the default sRGB space.

---

#### public static final
Color
BLACK

The color black. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
red

The color red. In the default sRGB space.

---

#### public static final
Color
RED

The color red. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
pink

The color pink. In the default sRGB space.

---

#### public static final
Color
PINK

The color pink. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
orange

The color orange. In the default sRGB space.

---

#### public static final
Color
ORANGE

The color orange. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
yellow

The color yellow. In the default sRGB space.

---

#### public static final
Color
YELLOW

The color yellow. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
green

The color green. In the default sRGB space.

---

#### public static final
Color
GREEN

The color green. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
magenta

The color magenta. In the default sRGB space.

---

#### public static final
Color
MAGENTA

The color magenta. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
cyan

The color cyan. In the default sRGB space.

---

#### public static final
Color
CYAN

The color cyan. In the default sRGB space.

**Since:**
- 1.4

---

#### public static final
Color
blue

The color blue. In the default sRGB space.

---

#### public static final
Color
BLUE

The color blue. In the default sRGB space.

**Since:**
- 1.4

---

### Constructor Details

#### public Color​(int r,
int g,
int b)

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).
The actual color used in rendering depends
on finding the best match given the color space
available for a given output device.
Alpha is defaulted to 255.

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component

**Throws:**
- IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0 to 255, inclusive

**See Also:**
- getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### @ConstructorProperties
({"red","green","blue","alpha"})
public Color​(int r,
int g,
int b,
int a)

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component
- a

- the alpha component

**Throws:**
- IllegalArgumentException

- if

r

,

g

,

b

or

a

are outside of the range
0 to 255, inclusive

**See Also:**
- getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### public Color​(int rgb)

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7. The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device. Alpha is
defaulted to 255.

**Parameters:**
- rgb

- the combined RGB components

**See Also:**
- ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### public Color​(int rgba,
boolean hasalpha)

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.
If the

hasalpha

argument is

false

, alpha
is defaulted to 255.

**Parameters:**
- rgba

- the combined RGBA components
- hasalpha

-

true

if the alpha bits are valid;

false

otherwise

**See Also:**
- ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### public Color​(float r,
float g,
float b)

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0). Alpha is defaulted to 1.0. The
actual color used in rendering depends on finding the best
match given the color space available for a particular output
device.

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component

**Throws:**
- IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0.0 to 1.0, inclusive

**See Also:**
- getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### public Color​(float r,
float g,
float b,
float a)

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0). The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device.

**Parameters:**
- r

- the red component
- g

- the green component
- b

- the blue component
- a

- the alpha component

**Throws:**
- IllegalArgumentException

- if

r

,

g

b

or

a

are outside of the range
0.0 to 1.0, inclusive

**See Also:**
- getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### public Color​(
ColorSpace
cspace,
float[] components,
float alpha)

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha. The number of components is
determined by the type of the

ColorSpace

. For
example, RGB requires 3 components, but CMYK requires 4
components.

**Parameters:**
- cspace

- the

ColorSpace

to be used to
interpret the components
- components

- an arbitrary number of color components
that is compatible with the

ColorSpace
- alpha

- alpha value

**Throws:**
- IllegalArgumentException

- if any of the values in the

components

array or

alpha

is
outside of the range 0.0 to 1.0

**See Also:**
- getComponents(float[])

,

getColorComponents(float[])

---

### Method Details

#### public int getRed()

Returns the red component in the range 0-255 in the default sRGB
space.

**Returns:**
- the red component.

**See Also:**
- getRGB()

---

#### public int getGreen()

Returns the green component in the range 0-255 in the default sRGB
space.

**Returns:**
- the green component.

**See Also:**
- getRGB()

---

#### public int getBlue()

Returns the blue component in the range 0-255 in the default sRGB
space.

**Returns:**
- the blue component.

**See Also:**
- getRGB()

---

#### public int getAlpha()

Returns the alpha component in the range 0-255.

**Returns:**
- the alpha component.

**See Also:**
- getRGB()

---

#### public int getRGB()

Returns the RGB value representing the color in the default sRGB

ColorModel

.
(Bits 24-31 are alpha, 16-23 are red, 8-15 are green, 0-7 are
blue).

**Returns:**
- the RGB value of the color in the default sRGB

ColorModel

.

**See Also:**
- ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

**Since:**
- 1.0

---

#### public
Color
brighter()

Creates a new

Color

that is a brighter version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

**Returns:**
- a new

Color

object that is
a brighter version of this

Color

with the same

alpha

value.

**See Also:**
- darker()

**Since:**
- 1.0

---

#### public
Color
darker()

Creates a new

Color

that is a darker version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

**Returns:**
- a new

Color

object that is
a darker version of this

Color

with the same

alpha

value.

**See Also:**
- brighter()

**Since:**
- 1.0

---

#### public int hashCode()

Computes the hash code for this

Color

.

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

**Since:**
- 1.0

---

#### public boolean equals​(
Object
obj)

Determines whether another object is equal to this

Color

.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the object to test for equality with this

Color

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.0

---

#### public
String
toString()

Returns a string representation of this

Color

. This
method is intended to be used only for debugging purposes. The
content and format of the returned string might vary between
implementations. The returned string might be empty but cannot
be

null

.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this

Color

.

---

#### public static
Color
decode​(
String
nm)
throws
NumberFormatException

Converts a

String

to an integer and returns the
specified opaque

Color

. This method handles string
formats that are used to represent octal and hexadecimal numbers.

**Parameters:**
- nm

- a

String

that represents
an opaque color as a 24-bit integer

**Returns:**
- the new

Color

object.

**Throws:**
- NumberFormatException

- if the specified string cannot
be interpreted as a decimal,
octal, or hexadecimal integer.

**See Also:**
- Integer.decode(java.lang.String)

**Since:**
- 1.1

---

#### public static
Color
getColor​(
String
nm)

Finds a color in the system properties.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

**Parameters:**
- nm

- the name of the color property

**Returns:**
- the

Color

converted from the system
property.

**See Also:**
- System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

**Since:**
- 1.0

---

#### public static
Color
getColor​(
String
nm,

Color
v)

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

**Parameters:**
- nm

- the name of the color property
- v

- the default

Color

**Returns:**
- the

Color

converted from the system
property, or the specified

Color

.

**See Also:**
- System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

**Since:**
- 1.0

---

#### public static
Color
getColor​(
String
nm,
int v)

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

**Parameters:**
- nm

- the name of the color property
- v

- the default color value, as an integer

**Returns:**
- the

Color

converted from the system
property or the

Color

converted from
the specified integer.

**See Also:**
- System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

**Since:**
- 1.0

---

#### public static int HSBtoRGB​(float hue,
float saturation,
float brightness)

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

**Parameters:**
- hue

- the hue component of the color
- saturation

- the saturation of the color
- brightness

- the brightness of the color

**Returns:**
- the RGB value of the color with the indicated hue,
saturation, and brightness.

**See Also:**
- getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

**Since:**
- 1.0

---

#### public static float[] RGBtoHSB​(int r,
int g,
int b,
float[] hsbvals)

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

**Parameters:**
- r

- the red component of the color
- g

- the green component of the color
- b

- the blue component of the color
- hsbvals

- the array used to return the
three HSB values, or

null

**Returns:**
- an array of three elements containing the hue, saturation,
and brightness (in that order), of the color with
the indicated red, green, and blue components.

**See Also:**
- getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

**Since:**
- 1.0

---

#### public static
Color
getHSBColor​(float h,
float s,
float b)

Creates a

Color

object based on the specified values
for the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

**Parameters:**
- h

- the hue component
- s

- the saturation of the color
- b

- the brightness of the color

**Returns:**
- a

Color

object with the specified hue,
saturation, and brightness.

**Since:**
- 1.0

---

#### public float[] getRGBComponents​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.
If

compArray

is

null

, an array of length
4 is created for the return value. Otherwise,

compArray

must have length 4 or greater,
and it is filled in with the components and returned.

**Parameters:**
- compArray

- an array that this method fills with
color and alpha components and returns

**Returns:**
- the RGBA components in a

float

array.

---

#### public float[] getRGBColorComponents​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space. If

compArray

is

null

, an array of
length 3 is created for the return value. Otherwise,

compArray

must have length 3 or greater, and it is
filled in with the components and returned.

**Parameters:**
- compArray

- an array that this method fills with color
components and returns

**Returns:**
- the RGB components in a

float

array.

---

#### public float[] getComponents​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

plus one is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:**
- compArray

- an array that this method fills with the color and
alpha components of this

Color

in its

ColorSpace

and returns

**Returns:**
- the color and alpha components in a

float

array.

---

#### public float[] getColorComponents​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:**
- compArray

- an array that this method fills with the color
components of this

Color

in its

ColorSpace

and returns

**Returns:**
- the color components in a

float

array.

---

#### public float[] getComponents​(
ColorSpace
cspace,
float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an
array with length equal to the number of components in

cspace

plus one is created for the return value.
Otherwise,

compArray

must have at least this
length, and it is filled in with the components and returned.

**Parameters:**
- cspace

- a specified

ColorSpace
- compArray

- an array that this method fills with the
color and alpha components of this

Color

in
the specified

ColorSpace

and returns

**Returns:**
- the color and alpha components in a

float

array.

---

#### public float[] getColorComponents​(
ColorSpace
cspace,
float[] compArray)

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an array
with length equal to the number of components in

cspace

is created for the return value. Otherwise,

compArray

must have at least this length, and it is
filled in with the components and returned.

**Parameters:**
- cspace

- a specified

ColorSpace
- compArray

- an array that this method fills with the color
components of this

Color

in the specified

ColorSpace

**Returns:**
- the color components in a

float

array.

---

#### public
ColorSpace
getColorSpace()

Returns the

ColorSpace

of this

Color

.

**Returns:**
- this

Color

object's

ColorSpace

.

---

#### public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
r,

Rectangle2D
r2d,

AffineTransform
xform,

RenderingHints
hints)

Creates and returns a

PaintContext

used to
generate a solid color field pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:**
- createContext

in interface

Paint

**Parameters:**
- cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
- r

- the device space bounding box
of the graphics primitive being rendered.
- r2d

- the user space bounding box
of the graphics primitive being rendered.
- xform

- the

AffineTransform

from user
space into device space.
- hints

- the set of hints that the context object can use to
choose between rendering alternatives.

**Returns:**
- the

PaintContext

for
generating color patterns.

**See Also:**
- Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

---

#### public int getTransparency()

Returns the transparency mode for this

Color

. This is
required to implement the

Paint

interface.

**Specified by:**
- getTransparency

in interface

Transparency

**Returns:**
- this

Color

object's transparency mode.

**See Also:**
- Paint

,

Transparency

,

createContext(java.awt.image.ColorModel, java.awt.Rectangle, java.awt.geom.Rectangle2D, java.awt.geom.AffineTransform, java.awt.RenderingHints)

---

### Additional Sections

#### Class Color

java.lang.Object

- java.awt.Color

java.awt.Color

**All Implemented Interfaces:** Paint

,

Transparency

,

Serializable

**Direct Known Subclasses:** ColorUIResource

,

SystemColor

```java
public class
Color

extends
Object

implements
Paint
,
Serializable
```

The

Color

class is used to encapsulate colors in the default
sRGB color space or colors in arbitrary color spaces identified by a

ColorSpace

. Every color has an implicit alpha value of 1.0 or
an explicit one provided in the constructor. The alpha value
defines the transparency of a color and can be represented by
a float value in the range 0.0 - 1.0 or 0 - 255.
An alpha value of 1.0 or 255 means that the color is completely
opaque and an alpha value of 0 or 0.0 means that the color is
completely transparent.
When constructing a

Color

with an explicit alpha or
getting the color/alpha components of a

Color

, the color
components are never premultiplied by the alpha component.

The default color space for the Java 2D(tm) API is sRGB, a proposed
standard RGB color space. For further information on sRGB,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

**See Also:** ColorSpace

,

AlphaComposite

,

Serialized Form

public class

Color

extends

Object

implements

Paint

,

Serializable

The

Color

class is used to encapsulate colors in the default
sRGB color space or colors in arbitrary color spaces identified by a

ColorSpace

. Every color has an implicit alpha value of 1.0 or
an explicit one provided in the constructor. The alpha value
defines the transparency of a color and can be represented by
a float value in the range 0.0 - 1.0 or 0 - 255.
An alpha value of 1.0 or 255 means that the color is completely
opaque and an alpha value of 0 or 0.0 means that the color is
completely transparent.
When constructing a

Color

with an explicit alpha or
getting the color/alpha components of a

Color

, the color
components are never premultiplied by the alpha component.

The default color space for the Java 2D(tm) API is sRGB, a proposed
standard RGB color space. For further information on sRGB,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

The default color space for the Java 2D(tm) API is sRGB, a proposed
standard RGB color space. For further information on sRGB,
see

http://www.w3.org/pub/WWW/Graphics/Color/sRGB.html

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Color

black

The color black.

static

Color

BLACK

The color black.

static

Color

blue

The color blue.

static

Color

BLUE

The color blue.

static

Color

cyan

The color cyan.

static

Color

CYAN

The color cyan.

static

Color

DARK_GRAY

The color dark gray.

static

Color

darkGray

The color dark gray.

static

Color

gray

The color gray.

static

Color

GRAY

The color gray.

static

Color

green

The color green.

static

Color

GREEN

The color green.

static

Color

LIGHT_GRAY

The color light gray.

static

Color

lightGray

The color light gray.

static

Color

magenta

The color magenta.

static

Color

MAGENTA

The color magenta.

static

Color

orange

The color orange.

static

Color

ORANGE

The color orange.

static

Color

pink

The color pink.

static

Color

PINK

The color pink.

static

Color

red

The color red.

static

Color

RED

The color red.

static

Color

white

The color white.

static

Color

WHITE

The color white.

static

Color

yellow

The color yellow.

static

Color

YELLOW

The color yellow.

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Color

​(float r,
float g,
float b)

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0).

Color

​(float r,
float g,
float b,
float a)

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0).

Color

​(int rgb)

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7.

Color

​(int rgba,
boolean hasalpha)

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.

Color

​(int r,
int g,
int b)

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).

Color

​(int r,
int g,
int b,
int a)

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

Color

​(

ColorSpace

cspace,
float[] components,
float alpha)

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

brighter

()

Creates a new

Color

that is a brighter version of this

Color

.

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

r,

Rectangle2D

r2d,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a solid color field pattern.

Color

darker

()

Creates a new

Color

that is a darker version of this

Color

.

static

Color

decode

​(

String

nm)

Converts a

String

to an integer and returns the
specified opaque

Color

.

boolean

equals

​(

Object

obj)

Determines whether another object is equal to this

Color

.

int

getAlpha

()

Returns the alpha component in the range 0-255.

int

getBlue

()

Returns the blue component in the range 0-255 in the default sRGB
space.

static

Color

getColor

​(

String

nm)

Finds a color in the system properties.

static

Color

getColor

​(

String

nm,
int v)

Finds a color in the system properties.

static

Color

getColor

​(

String

nm,

Color

v)

Finds a color in the system properties.

float[]

getColorComponents

​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.

float[]

getColorComponents

​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter.

ColorSpace

getColorSpace

()

Returns the

ColorSpace

of this

Color

.

float[]

getComponents

​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.

float[]

getComponents

​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter.

int

getGreen

()

Returns the green component in the range 0-255 in the default sRGB
space.

static

Color

getHSBColor

​(float h,
float s,
float b)

Creates a

Color

object based on the specified values
for the HSB color model.

int

getRed

()

Returns the red component in the range 0-255 in the default sRGB
space.

int

getRGB

()

Returns the RGB value representing the color in the default sRGB

ColorModel

.

float[]

getRGBColorComponents

​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space.

float[]

getRGBComponents

​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.

int

getTransparency

()

Returns the transparency mode for this

Color

.

int

hashCode

()

Computes the hash code for this

Color

.

static int

HSBtoRGB

​(float hue,
float saturation,
float brightness)

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

static float[]

RGBtoHSB

​(int r,
int g,
int b,
float[] hsbvals)

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

String

toString

()

Returns a string representation of this

Color

.

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

static

Color

black

The color black.

static

Color

BLACK

The color black.

static

Color

blue

The color blue.

static

Color

BLUE

The color blue.

static

Color

cyan

The color cyan.

static

Color

CYAN

The color cyan.

static

Color

DARK_GRAY

The color dark gray.

static

Color

darkGray

The color dark gray.

static

Color

gray

The color gray.

static

Color

GRAY

The color gray.

static

Color

green

The color green.

static

Color

GREEN

The color green.

static

Color

LIGHT_GRAY

The color light gray.

static

Color

lightGray

The color light gray.

static

Color

magenta

The color magenta.

static

Color

MAGENTA

The color magenta.

static

Color

orange

The color orange.

static

Color

ORANGE

The color orange.

static

Color

pink

The color pink.

static

Color

PINK

The color pink.

static

Color

red

The color red.

static

Color

RED

The color red.

static

Color

white

The color white.

static

Color

WHITE

The color white.

static

Color

yellow

The color yellow.

static

Color

YELLOW

The color yellow.

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

The color black.

The color blue.

The color cyan.

The color dark gray.

The color gray.

The color green.

The color light gray.

The color magenta.

The color orange.

The color pink.

The color red.

The color white.

The color yellow.

Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Fields declared in interface java.awt. Transparency

Constructor Summary

Constructors

Constructor

Description

Color

​(float r,
float g,
float b)

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0).

Color

​(float r,
float g,
float b,
float a)

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0).

Color

​(int rgb)

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7.

Color

​(int rgba,
boolean hasalpha)

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.

Color

​(int r,
int g,
int b)

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).

Color

​(int r,
int g,
int b,
int a)

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

Color

​(

ColorSpace

cspace,
float[] components,
float alpha)

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha.

---

#### Constructor Summary

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0).

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0).

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7.

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Color

brighter

()

Creates a new

Color

that is a brighter version of this

Color

.

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

r,

Rectangle2D

r2d,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a solid color field pattern.

Color

darker

()

Creates a new

Color

that is a darker version of this

Color

.

static

Color

decode

​(

String

nm)

Converts a

String

to an integer and returns the
specified opaque

Color

.

boolean

equals

​(

Object

obj)

Determines whether another object is equal to this

Color

.

int

getAlpha

()

Returns the alpha component in the range 0-255.

int

getBlue

()

Returns the blue component in the range 0-255 in the default sRGB
space.

static

Color

getColor

​(

String

nm)

Finds a color in the system properties.

static

Color

getColor

​(

String

nm,
int v)

Finds a color in the system properties.

static

Color

getColor

​(

String

nm,

Color

v)

Finds a color in the system properties.

float[]

getColorComponents

​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.

float[]

getColorComponents

​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter.

ColorSpace

getColorSpace

()

Returns the

ColorSpace

of this

Color

.

float[]

getComponents

​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.

float[]

getComponents

​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter.

int

getGreen

()

Returns the green component in the range 0-255 in the default sRGB
space.

static

Color

getHSBColor

​(float h,
float s,
float b)

Creates a

Color

object based on the specified values
for the HSB color model.

int

getRed

()

Returns the red component in the range 0-255 in the default sRGB
space.

int

getRGB

()

Returns the RGB value representing the color in the default sRGB

ColorModel

.

float[]

getRGBColorComponents

​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space.

float[]

getRGBComponents

​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.

int

getTransparency

()

Returns the transparency mode for this

Color

.

int

hashCode

()

Computes the hash code for this

Color

.

static int

HSBtoRGB

​(float hue,
float saturation,
float brightness)

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

static float[]

RGBtoHSB

​(int r,
int g,
int b,
float[] hsbvals)

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

String

toString

()

Returns a string representation of this

Color

.

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

Creates a new

Color

that is a brighter version of this

Color

.

Creates and returns a

PaintContext

used to
generate a solid color field pattern.

Creates a new

Color

that is a darker version of this

Color

.

Converts a

String

to an integer and returns the
specified opaque

Color

.

Determines whether another object is equal to this

Color

.

Returns the alpha component in the range 0-255.

Returns the blue component in the range 0-255 in the default sRGB
space.

Finds a color in the system properties.

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter.

Returns the

ColorSpace

of this

Color

.

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter.

Returns the green component in the range 0-255 in the default sRGB
space.

Creates a

Color

object based on the specified values
for the HSB color model.

Returns the red component in the range 0-255 in the default sRGB
space.

Returns the RGB value representing the color in the default sRGB

ColorModel

.

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space.

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.

Returns the transparency mode for this

Color

.

Computes the hash code for this

Color

.

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

Returns a string representation of this

Color

.

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

- white

```java
public static final
Color
white
```

The color white. In the default sRGB space.

- WHITE

```java
public static final
Color
WHITE
```

The color white. In the default sRGB space.

**Since:** 1.4

- lightGray

```java
public static final
Color
lightGray
```

The color light gray. In the default sRGB space.

- LIGHT_GRAY

```java
public static final
Color
LIGHT_GRAY
```

The color light gray. In the default sRGB space.

**Since:** 1.4

- gray

```java
public static final
Color
gray
```

The color gray. In the default sRGB space.

- GRAY

```java
public static final
Color
GRAY
```

The color gray. In the default sRGB space.

**Since:** 1.4

- darkGray

```java
public static final
Color
darkGray
```

The color dark gray. In the default sRGB space.

- DARK_GRAY

```java
public static final
Color
DARK_GRAY
```

The color dark gray. In the default sRGB space.

**Since:** 1.4

- black

```java
public static final
Color
black
```

The color black. In the default sRGB space.

- BLACK

```java
public static final
Color
BLACK
```

The color black. In the default sRGB space.

**Since:** 1.4

- red

```java
public static final
Color
red
```

The color red. In the default sRGB space.

- RED

```java
public static final
Color
RED
```

The color red. In the default sRGB space.

**Since:** 1.4

- pink

```java
public static final
Color
pink
```

The color pink. In the default sRGB space.

- PINK

```java
public static final
Color
PINK
```

The color pink. In the default sRGB space.

**Since:** 1.4

- orange

```java
public static final
Color
orange
```

The color orange. In the default sRGB space.

- ORANGE

```java
public static final
Color
ORANGE
```

The color orange. In the default sRGB space.

**Since:** 1.4

- yellow

```java
public static final
Color
yellow
```

The color yellow. In the default sRGB space.

- YELLOW

```java
public static final
Color
YELLOW
```

The color yellow. In the default sRGB space.

**Since:** 1.4

- green

```java
public static final
Color
green
```

The color green. In the default sRGB space.

- GREEN

```java
public static final
Color
GREEN
```

The color green. In the default sRGB space.

**Since:** 1.4

- magenta

```java
public static final
Color
magenta
```

The color magenta. In the default sRGB space.

- MAGENTA

```java
public static final
Color
MAGENTA
```

The color magenta. In the default sRGB space.

**Since:** 1.4

- cyan

```java
public static final
Color
cyan
```

The color cyan. In the default sRGB space.

- CYAN

```java
public static final
Color
CYAN
```

The color cyan. In the default sRGB space.

**Since:** 1.4

- blue

```java
public static final
Color
blue
```

The color blue. In the default sRGB space.

- BLUE

```java
public static final
Color
BLUE
```

The color blue. In the default sRGB space.

**Since:** 1.4

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Color

```java
public Color​(int r,
int g,
int b)
```

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).
The actual color used in rendering depends
on finding the best match given the color space
available for a given output device.
Alpha is defaulted to 255.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
@ConstructorProperties
({"red","green","blue","alpha"})
public Color​(int r,
int g,
int b,
int a)
```

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

,

b

or

a

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(int rgb)
```

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7. The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device. Alpha is
defaulted to 255.

**Parameters:** rgb

- the combined RGB components
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
public Color​(int rgba,
boolean hasalpha)
```

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.
If the

hasalpha

argument is

false

, alpha
is defaulted to 255.

**Parameters:** rgba

- the combined RGBA components
**Parameters:** hasalpha

-

true

if the alpha bits are valid;

false

otherwise
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(float r,
float g,
float b)
```

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0). Alpha is defaulted to 1.0. The
actual color used in rendering depends on finding the best
match given the color space available for a particular output
device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
public Color​(float r,
float g,
float b,
float a)
```

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0). The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

b

or

a

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(
ColorSpace
cspace,
float[] components,
float alpha)
```

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha. The number of components is
determined by the type of the

ColorSpace

. For
example, RGB requires 3 components, but CMYK requires 4
components.

**Parameters:** cspace

- the

ColorSpace

to be used to
interpret the components
**Parameters:** components

- an arbitrary number of color components
that is compatible with the

ColorSpace
**Parameters:** alpha

- alpha value
**Throws:** IllegalArgumentException

- if any of the values in the

components

array or

alpha

is
outside of the range 0.0 to 1.0
**See Also:** getComponents(float[])

,

getColorComponents(float[])

============ METHOD DETAIL ==========

- Method Detail

- getRed

```java
public int getRed()
```

Returns the red component in the range 0-255 in the default sRGB
space.

**Returns:** the red component.
**See Also:** getRGB()

- getGreen

```java
public int getGreen()
```

Returns the green component in the range 0-255 in the default sRGB
space.

**Returns:** the green component.
**See Also:** getRGB()

- getBlue

```java
public int getBlue()
```

Returns the blue component in the range 0-255 in the default sRGB
space.

**Returns:** the blue component.
**See Also:** getRGB()

- getAlpha

```java
public int getAlpha()
```

Returns the alpha component in the range 0-255.

**Returns:** the alpha component.
**See Also:** getRGB()

- getRGB

```java
public int getRGB()
```

Returns the RGB value representing the color in the default sRGB

ColorModel

.
(Bits 24-31 are alpha, 16-23 are red, 8-15 are green, 0-7 are
blue).

**Returns:** the RGB value of the color in the default sRGB

ColorModel

.
**Since:** 1.0
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

- brighter

```java
public
Color
brighter()
```

Creates a new

Color

that is a brighter version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

**Returns:** a new

Color

object that is
a brighter version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** darker()

- darker

```java
public
Color
darker()
```

Creates a new

Color

that is a darker version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

**Returns:** a new

Color

object that is
a darker version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** brighter()

- hashCode

```java
public int hashCode()
```

Computes the hash code for this

Color

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.0
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether another object is equal to this

Color

.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this

Color
**Returns:** true

if the objects are the same;

false

otherwise.
**Since:** 1.0
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this

Color

. This
method is intended to be used only for debugging purposes. The
content and format of the returned string might vary between
implementations. The returned string might be empty but cannot
be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Color

.

- decode

```java
public static
Color
decode​(
String
nm)
throws
NumberFormatException
```

Converts a

String

to an integer and returns the
specified opaque

Color

. This method handles string
formats that are used to represent octal and hexadecimal numbers.

**Parameters:** nm

- a

String

that represents
an opaque color as a 24-bit integer
**Returns:** the new

Color

object.
**Throws:** NumberFormatException

- if the specified string cannot
be interpreted as a decimal,
octal, or hexadecimal integer.
**Since:** 1.1
**See Also:** Integer.decode(java.lang.String)

- getColor

```java
public static
Color
getColor​(
String
nm)
```

Finds a color in the system properties.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

**Parameters:** nm

- the name of the color property
**Returns:** the

Color

converted from the system
property.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- getColor

```java
public static
Color
getColor​(
String
nm,

Color
v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default

Color
**Returns:** the

Color

converted from the system
property, or the specified

Color

.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- getColor

```java
public static
Color
getColor​(
String
nm,
int v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default color value, as an integer
**Returns:** the

Color

converted from the system
property or the

Color

converted from
the specified integer.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- HSBtoRGB

```java
public static int HSBtoRGB​(float hue,
float saturation,
float brightness)
```

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

**Parameters:** hue

- the hue component of the color
**Parameters:** saturation

- the saturation of the color
**Parameters:** brightness

- the brightness of the color
**Returns:** the RGB value of the color with the indicated hue,
saturation, and brightness.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

- RGBtoHSB

```java
public static float[] RGBtoHSB​(int r,
int g,
int b,
float[] hsbvals)
```

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

**Parameters:** r

- the red component of the color
**Parameters:** g

- the green component of the color
**Parameters:** b

- the blue component of the color
**Parameters:** hsbvals

- the array used to return the
three HSB values, or

null
**Returns:** an array of three elements containing the hue, saturation,
and brightness (in that order), of the color with
the indicated red, green, and blue components.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

- getHSBColor

```java
public static
Color
getHSBColor​(float h,
float s,
float b)
```

Creates a

Color

object based on the specified values
for the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

**Parameters:** h

- the hue component
**Parameters:** s

- the saturation of the color
**Parameters:** b

- the brightness of the color
**Returns:** a

Color

object with the specified hue,
saturation, and brightness.
**Since:** 1.0

- getRGBComponents

```java
public float[] getRGBComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.
If

compArray

is

null

, an array of length
4 is created for the return value. Otherwise,

compArray

must have length 4 or greater,
and it is filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with
color and alpha components and returns
**Returns:** the RGBA components in a

float

array.

- getRGBColorComponents

```java
public float[] getRGBColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space. If

compArray

is

null

, an array of
length 3 is created for the return value. Otherwise,

compArray

must have length 3 or greater, and it is
filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with color
components and returns
**Returns:** the RGB components in a

float

array.

- getComponents

```java
public float[] getComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

plus one is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color and
alpha components of this

Color

in its

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

- getColorComponents

```java
public float[] getColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in its

ColorSpace

and returns
**Returns:** the color components in a

float

array.

- getComponents

```java
public float[] getComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an
array with length equal to the number of components in

cspace

plus one is created for the return value.
Otherwise,

compArray

must have at least this
length, and it is filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the
color and alpha components of this

Color

in
the specified

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

- getColorComponents

```java
public float[] getColorComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an array
with length equal to the number of components in

cspace

is created for the return value. Otherwise,

compArray

must have at least this length, and it is
filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in the specified

ColorSpace
**Returns:** the color components in a

float

array.

- getColorSpace

```java
public
ColorSpace
getColorSpace()
```

Returns the

ColorSpace

of this

Color

.

**Returns:** this

Color

object's

ColorSpace

.

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
r,

Rectangle2D
r2d,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a solid color field pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** r

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** r2d

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

- getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

Color

. This is
required to implement the

Paint

interface.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** this

Color

object's transparency mode.
**See Also:** Paint

,

Transparency

,

createContext(java.awt.image.ColorModel, java.awt.Rectangle, java.awt.geom.Rectangle2D, java.awt.geom.AffineTransform, java.awt.RenderingHints)

Field Detail

- white

```java
public static final
Color
white
```

The color white. In the default sRGB space.

- WHITE

```java
public static final
Color
WHITE
```

The color white. In the default sRGB space.

**Since:** 1.4

- lightGray

```java
public static final
Color
lightGray
```

The color light gray. In the default sRGB space.

- LIGHT_GRAY

```java
public static final
Color
LIGHT_GRAY
```

The color light gray. In the default sRGB space.

**Since:** 1.4

- gray

```java
public static final
Color
gray
```

The color gray. In the default sRGB space.

- GRAY

```java
public static final
Color
GRAY
```

The color gray. In the default sRGB space.

**Since:** 1.4

- darkGray

```java
public static final
Color
darkGray
```

The color dark gray. In the default sRGB space.

- DARK_GRAY

```java
public static final
Color
DARK_GRAY
```

The color dark gray. In the default sRGB space.

**Since:** 1.4

- black

```java
public static final
Color
black
```

The color black. In the default sRGB space.

- BLACK

```java
public static final
Color
BLACK
```

The color black. In the default sRGB space.

**Since:** 1.4

- red

```java
public static final
Color
red
```

The color red. In the default sRGB space.

- RED

```java
public static final
Color
RED
```

The color red. In the default sRGB space.

**Since:** 1.4

- pink

```java
public static final
Color
pink
```

The color pink. In the default sRGB space.

- PINK

```java
public static final
Color
PINK
```

The color pink. In the default sRGB space.

**Since:** 1.4

- orange

```java
public static final
Color
orange
```

The color orange. In the default sRGB space.

- ORANGE

```java
public static final
Color
ORANGE
```

The color orange. In the default sRGB space.

**Since:** 1.4

- yellow

```java
public static final
Color
yellow
```

The color yellow. In the default sRGB space.

- YELLOW

```java
public static final
Color
YELLOW
```

The color yellow. In the default sRGB space.

**Since:** 1.4

- green

```java
public static final
Color
green
```

The color green. In the default sRGB space.

- GREEN

```java
public static final
Color
GREEN
```

The color green. In the default sRGB space.

**Since:** 1.4

- magenta

```java
public static final
Color
magenta
```

The color magenta. In the default sRGB space.

- MAGENTA

```java
public static final
Color
MAGENTA
```

The color magenta. In the default sRGB space.

**Since:** 1.4

- cyan

```java
public static final
Color
cyan
```

The color cyan. In the default sRGB space.

- CYAN

```java
public static final
Color
CYAN
```

The color cyan. In the default sRGB space.

**Since:** 1.4

- blue

```java
public static final
Color
blue
```

The color blue. In the default sRGB space.

- BLUE

```java
public static final
Color
BLUE
```

The color blue. In the default sRGB space.

**Since:** 1.4

---

#### Field Detail

white

```java
public static final
Color
white
```

The color white. In the default sRGB space.

---

#### white

public static final

Color

white

The color white. In the default sRGB space.

WHITE

```java
public static final
Color
WHITE
```

The color white. In the default sRGB space.

**Since:** 1.4

---

#### WHITE

public static final

Color

WHITE

The color white. In the default sRGB space.

lightGray

```java
public static final
Color
lightGray
```

The color light gray. In the default sRGB space.

---

#### lightGray

public static final

Color

lightGray

The color light gray. In the default sRGB space.

LIGHT_GRAY

```java
public static final
Color
LIGHT_GRAY
```

The color light gray. In the default sRGB space.

**Since:** 1.4

---

#### LIGHT_GRAY

public static final

Color

LIGHT_GRAY

The color light gray. In the default sRGB space.

gray

```java
public static final
Color
gray
```

The color gray. In the default sRGB space.

---

#### gray

public static final

Color

gray

The color gray. In the default sRGB space.

GRAY

```java
public static final
Color
GRAY
```

The color gray. In the default sRGB space.

**Since:** 1.4

---

#### GRAY

public static final

Color

GRAY

The color gray. In the default sRGB space.

darkGray

```java
public static final
Color
darkGray
```

The color dark gray. In the default sRGB space.

---

#### darkGray

public static final

Color

darkGray

The color dark gray. In the default sRGB space.

DARK_GRAY

```java
public static final
Color
DARK_GRAY
```

The color dark gray. In the default sRGB space.

**Since:** 1.4

---

#### DARK_GRAY

public static final

Color

DARK_GRAY

The color dark gray. In the default sRGB space.

black

```java
public static final
Color
black
```

The color black. In the default sRGB space.

---

#### black

public static final

Color

black

The color black. In the default sRGB space.

BLACK

```java
public static final
Color
BLACK
```

The color black. In the default sRGB space.

**Since:** 1.4

---

#### BLACK

public static final

Color

BLACK

The color black. In the default sRGB space.

red

```java
public static final
Color
red
```

The color red. In the default sRGB space.

---

#### red

public static final

Color

red

The color red. In the default sRGB space.

RED

```java
public static final
Color
RED
```

The color red. In the default sRGB space.

**Since:** 1.4

---

#### RED

public static final

Color

RED

The color red. In the default sRGB space.

pink

```java
public static final
Color
pink
```

The color pink. In the default sRGB space.

---

#### pink

public static final

Color

pink

The color pink. In the default sRGB space.

PINK

```java
public static final
Color
PINK
```

The color pink. In the default sRGB space.

**Since:** 1.4

---

#### PINK

public static final

Color

PINK

The color pink. In the default sRGB space.

orange

```java
public static final
Color
orange
```

The color orange. In the default sRGB space.

---

#### orange

public static final

Color

orange

The color orange. In the default sRGB space.

ORANGE

```java
public static final
Color
ORANGE
```

The color orange. In the default sRGB space.

**Since:** 1.4

---

#### ORANGE

public static final

Color

ORANGE

The color orange. In the default sRGB space.

yellow

```java
public static final
Color
yellow
```

The color yellow. In the default sRGB space.

---

#### yellow

public static final

Color

yellow

The color yellow. In the default sRGB space.

YELLOW

```java
public static final
Color
YELLOW
```

The color yellow. In the default sRGB space.

**Since:** 1.4

---

#### YELLOW

public static final

Color

YELLOW

The color yellow. In the default sRGB space.

green

```java
public static final
Color
green
```

The color green. In the default sRGB space.

---

#### green

public static final

Color

green

The color green. In the default sRGB space.

GREEN

```java
public static final
Color
GREEN
```

The color green. In the default sRGB space.

**Since:** 1.4

---

#### GREEN

public static final

Color

GREEN

The color green. In the default sRGB space.

magenta

```java
public static final
Color
magenta
```

The color magenta. In the default sRGB space.

---

#### magenta

public static final

Color

magenta

The color magenta. In the default sRGB space.

MAGENTA

```java
public static final
Color
MAGENTA
```

The color magenta. In the default sRGB space.

**Since:** 1.4

---

#### MAGENTA

public static final

Color

MAGENTA

The color magenta. In the default sRGB space.

cyan

```java
public static final
Color
cyan
```

The color cyan. In the default sRGB space.

---

#### cyan

public static final

Color

cyan

The color cyan. In the default sRGB space.

CYAN

```java
public static final
Color
CYAN
```

The color cyan. In the default sRGB space.

**Since:** 1.4

---

#### CYAN

public static final

Color

CYAN

The color cyan. In the default sRGB space.

blue

```java
public static final
Color
blue
```

The color blue. In the default sRGB space.

---

#### blue

public static final

Color

blue

The color blue. In the default sRGB space.

BLUE

```java
public static final
Color
BLUE
```

The color blue. In the default sRGB space.

**Since:** 1.4

---

#### BLUE

public static final

Color

BLUE

The color blue. In the default sRGB space.

Constructor Detail

- Color

```java
public Color​(int r,
int g,
int b)
```

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).
The actual color used in rendering depends
on finding the best match given the color space
available for a given output device.
Alpha is defaulted to 255.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
@ConstructorProperties
({"red","green","blue","alpha"})
public Color​(int r,
int g,
int b,
int a)
```

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

,

b

or

a

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(int rgb)
```

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7. The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device. Alpha is
defaulted to 255.

**Parameters:** rgb

- the combined RGB components
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
public Color​(int rgba,
boolean hasalpha)
```

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.
If the

hasalpha

argument is

false

, alpha
is defaulted to 255.

**Parameters:** rgba

- the combined RGBA components
**Parameters:** hasalpha

-

true

if the alpha bits are valid;

false

otherwise
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(float r,
float g,
float b)
```

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0). Alpha is defaulted to 1.0. The
actual color used in rendering depends on finding the best
match given the color space available for a particular output
device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

- Color

```java
public Color​(float r,
float g,
float b,
float a)
```

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0). The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

b

or

a

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

- Color

```java
public Color​(
ColorSpace
cspace,
float[] components,
float alpha)
```

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha. The number of components is
determined by the type of the

ColorSpace

. For
example, RGB requires 3 components, but CMYK requires 4
components.

**Parameters:** cspace

- the

ColorSpace

to be used to
interpret the components
**Parameters:** components

- an arbitrary number of color components
that is compatible with the

ColorSpace
**Parameters:** alpha

- alpha value
**Throws:** IllegalArgumentException

- if any of the values in the

components

array or

alpha

is
outside of the range 0.0 to 1.0
**See Also:** getComponents(float[])

,

getColorComponents(float[])

---

#### Constructor Detail

Color

```java
public Color​(int r,
int g,
int b)
```

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).
The actual color used in rendering depends
on finding the best match given the color space
available for a given output device.
Alpha is defaulted to 255.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### Color

public Color​(int r,
int g,
int b)

Creates an opaque sRGB color with the specified red, green,
and blue values in the range (0 - 255).
The actual color used in rendering depends
on finding the best match given the color space
available for a given output device.
Alpha is defaulted to 255.

Color

```java
@ConstructorProperties
({"red","green","blue","alpha"})
public Color​(int r,
int g,
int b,
int a)
```

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

,

b

or

a

are outside of the range
0 to 255, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### Color

@ConstructorProperties

({"red","green","blue","alpha"})
public Color​(int r,
int g,
int b,
int a)

Creates an sRGB color with the specified red, green, blue, and alpha
values in the range (0 - 255).

Color

```java
public Color​(int rgb)
```

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7. The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device. Alpha is
defaulted to 255.

**Parameters:** rgb

- the combined RGB components
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### Color

public Color​(int rgb)

Creates an opaque sRGB color with the specified combined RGB value
consisting of the red component in bits 16-23, the green component
in bits 8-15, and the blue component in bits 0-7. The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device. Alpha is
defaulted to 255.

Color

```java
public Color​(int rgba,
boolean hasalpha)
```

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.
If the

hasalpha

argument is

false

, alpha
is defaulted to 255.

**Parameters:** rgba

- the combined RGBA components
**Parameters:** hasalpha

-

true

if the alpha bits are valid;

false

otherwise
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### Color

public Color​(int rgba,
boolean hasalpha)

Creates an sRGB color with the specified combined RGBA value consisting
of the alpha component in bits 24-31, the red component in bits 16-23,
the green component in bits 8-15, and the blue component in bits 0-7.
If the

hasalpha

argument is

false

, alpha
is defaulted to 255.

Color

```java
public Color​(float r,
float g,
float b)
```

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0). Alpha is defaulted to 1.0. The
actual color used in rendering depends on finding the best
match given the color space available for a particular output
device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Throws:** IllegalArgumentException

- if

r

,

g

or

b

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getRGB()

---

#### Color

public Color​(float r,
float g,
float b)

Creates an opaque sRGB color with the specified red, green, and blue
values in the range (0.0 - 1.0). Alpha is defaulted to 1.0. The
actual color used in rendering depends on finding the best
match given the color space available for a particular output
device.

Color

```java
public Color​(float r,
float g,
float b,
float a)
```

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0). The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device.

**Parameters:** r

- the red component
**Parameters:** g

- the green component
**Parameters:** b

- the blue component
**Parameters:** a

- the alpha component
**Throws:** IllegalArgumentException

- if

r

,

g

b

or

a

are outside of the range
0.0 to 1.0, inclusive
**See Also:** getRed()

,

getGreen()

,

getBlue()

,

getAlpha()

,

getRGB()

---

#### Color

public Color​(float r,
float g,
float b,
float a)

Creates an sRGB color with the specified red, green, blue, and
alpha values in the range (0.0 - 1.0). The actual color
used in rendering depends on finding the best match given the
color space available for a particular output device.

Color

```java
public Color​(
ColorSpace
cspace,
float[] components,
float alpha)
```

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha. The number of components is
determined by the type of the

ColorSpace

. For
example, RGB requires 3 components, but CMYK requires 4
components.

**Parameters:** cspace

- the

ColorSpace

to be used to
interpret the components
**Parameters:** components

- an arbitrary number of color components
that is compatible with the

ColorSpace
**Parameters:** alpha

- alpha value
**Throws:** IllegalArgumentException

- if any of the values in the

components

array or

alpha

is
outside of the range 0.0 to 1.0
**See Also:** getComponents(float[])

,

getColorComponents(float[])

---

#### Color

public Color​(

ColorSpace

cspace,
float[] components,
float alpha)

Creates a color in the specified

ColorSpace

with the color components specified in the

float

array and the specified alpha. The number of components is
determined by the type of the

ColorSpace

. For
example, RGB requires 3 components, but CMYK requires 4
components.

Method Detail

- getRed

```java
public int getRed()
```

Returns the red component in the range 0-255 in the default sRGB
space.

**Returns:** the red component.
**See Also:** getRGB()

- getGreen

```java
public int getGreen()
```

Returns the green component in the range 0-255 in the default sRGB
space.

**Returns:** the green component.
**See Also:** getRGB()

- getBlue

```java
public int getBlue()
```

Returns the blue component in the range 0-255 in the default sRGB
space.

**Returns:** the blue component.
**See Also:** getRGB()

- getAlpha

```java
public int getAlpha()
```

Returns the alpha component in the range 0-255.

**Returns:** the alpha component.
**See Also:** getRGB()

- getRGB

```java
public int getRGB()
```

Returns the RGB value representing the color in the default sRGB

ColorModel

.
(Bits 24-31 are alpha, 16-23 are red, 8-15 are green, 0-7 are
blue).

**Returns:** the RGB value of the color in the default sRGB

ColorModel

.
**Since:** 1.0
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

- brighter

```java
public
Color
brighter()
```

Creates a new

Color

that is a brighter version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

**Returns:** a new

Color

object that is
a brighter version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** darker()

- darker

```java
public
Color
darker()
```

Creates a new

Color

that is a darker version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

**Returns:** a new

Color

object that is
a darker version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** brighter()

- hashCode

```java
public int hashCode()
```

Computes the hash code for this

Color

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.0
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether another object is equal to this

Color

.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this

Color
**Returns:** true

if the objects are the same;

false

otherwise.
**Since:** 1.0
**See Also:** Object.hashCode()

,

HashMap

- toString

```java
public
String
toString()
```

Returns a string representation of this

Color

. This
method is intended to be used only for debugging purposes. The
content and format of the returned string might vary between
implementations. The returned string might be empty but cannot
be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Color

.

- decode

```java
public static
Color
decode​(
String
nm)
throws
NumberFormatException
```

Converts a

String

to an integer and returns the
specified opaque

Color

. This method handles string
formats that are used to represent octal and hexadecimal numbers.

**Parameters:** nm

- a

String

that represents
an opaque color as a 24-bit integer
**Returns:** the new

Color

object.
**Throws:** NumberFormatException

- if the specified string cannot
be interpreted as a decimal,
octal, or hexadecimal integer.
**Since:** 1.1
**See Also:** Integer.decode(java.lang.String)

- getColor

```java
public static
Color
getColor​(
String
nm)
```

Finds a color in the system properties.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

**Parameters:** nm

- the name of the color property
**Returns:** the

Color

converted from the system
property.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- getColor

```java
public static
Color
getColor​(
String
nm,

Color
v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default

Color
**Returns:** the

Color

converted from the system
property, or the specified

Color

.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- getColor

```java
public static
Color
getColor​(
String
nm,
int v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default color value, as an integer
**Returns:** the

Color

converted from the system
property or the

Color

converted from
the specified integer.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

- HSBtoRGB

```java
public static int HSBtoRGB​(float hue,
float saturation,
float brightness)
```

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

**Parameters:** hue

- the hue component of the color
**Parameters:** saturation

- the saturation of the color
**Parameters:** brightness

- the brightness of the color
**Returns:** the RGB value of the color with the indicated hue,
saturation, and brightness.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

- RGBtoHSB

```java
public static float[] RGBtoHSB​(int r,
int g,
int b,
float[] hsbvals)
```

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

**Parameters:** r

- the red component of the color
**Parameters:** g

- the green component of the color
**Parameters:** b

- the blue component of the color
**Parameters:** hsbvals

- the array used to return the
three HSB values, or

null
**Returns:** an array of three elements containing the hue, saturation,
and brightness (in that order), of the color with
the indicated red, green, and blue components.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

- getHSBColor

```java
public static
Color
getHSBColor​(float h,
float s,
float b)
```

Creates a

Color

object based on the specified values
for the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

**Parameters:** h

- the hue component
**Parameters:** s

- the saturation of the color
**Parameters:** b

- the brightness of the color
**Returns:** a

Color

object with the specified hue,
saturation, and brightness.
**Since:** 1.0

- getRGBComponents

```java
public float[] getRGBComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.
If

compArray

is

null

, an array of length
4 is created for the return value. Otherwise,

compArray

must have length 4 or greater,
and it is filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with
color and alpha components and returns
**Returns:** the RGBA components in a

float

array.

- getRGBColorComponents

```java
public float[] getRGBColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space. If

compArray

is

null

, an array of
length 3 is created for the return value. Otherwise,

compArray

must have length 3 or greater, and it is
filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with color
components and returns
**Returns:** the RGB components in a

float

array.

- getComponents

```java
public float[] getComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

plus one is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color and
alpha components of this

Color

in its

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

- getColorComponents

```java
public float[] getColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in its

ColorSpace

and returns
**Returns:** the color components in a

float

array.

- getComponents

```java
public float[] getComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an
array with length equal to the number of components in

cspace

plus one is created for the return value.
Otherwise,

compArray

must have at least this
length, and it is filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the
color and alpha components of this

Color

in
the specified

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

- getColorComponents

```java
public float[] getColorComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an array
with length equal to the number of components in

cspace

is created for the return value. Otherwise,

compArray

must have at least this length, and it is
filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in the specified

ColorSpace
**Returns:** the color components in a

float

array.

- getColorSpace

```java
public
ColorSpace
getColorSpace()
```

Returns the

ColorSpace

of this

Color

.

**Returns:** this

Color

object's

ColorSpace

.

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
r,

Rectangle2D
r2d,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a solid color field pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** r

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** r2d

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

- getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

Color

. This is
required to implement the

Paint

interface.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** this

Color

object's transparency mode.
**See Also:** Paint

,

Transparency

,

createContext(java.awt.image.ColorModel, java.awt.Rectangle, java.awt.geom.Rectangle2D, java.awt.geom.AffineTransform, java.awt.RenderingHints)

---

#### Method Detail

getRed

```java
public int getRed()
```

Returns the red component in the range 0-255 in the default sRGB
space.

**Returns:** the red component.
**See Also:** getRGB()

---

#### getRed

public int getRed()

Returns the red component in the range 0-255 in the default sRGB
space.

getGreen

```java
public int getGreen()
```

Returns the green component in the range 0-255 in the default sRGB
space.

**Returns:** the green component.
**See Also:** getRGB()

---

#### getGreen

public int getGreen()

Returns the green component in the range 0-255 in the default sRGB
space.

getBlue

```java
public int getBlue()
```

Returns the blue component in the range 0-255 in the default sRGB
space.

**Returns:** the blue component.
**See Also:** getRGB()

---

#### getBlue

public int getBlue()

Returns the blue component in the range 0-255 in the default sRGB
space.

getAlpha

```java
public int getAlpha()
```

Returns the alpha component in the range 0-255.

**Returns:** the alpha component.
**See Also:** getRGB()

---

#### getAlpha

public int getAlpha()

Returns the alpha component in the range 0-255.

getRGB

```java
public int getRGB()
```

Returns the RGB value representing the color in the default sRGB

ColorModel

.
(Bits 24-31 are alpha, 16-23 are red, 8-15 are green, 0-7 are
blue).

**Returns:** the RGB value of the color in the default sRGB

ColorModel

.
**Since:** 1.0
**See Also:** ColorModel.getRGBdefault()

,

getRed()

,

getGreen()

,

getBlue()

---

#### getRGB

public int getRGB()

Returns the RGB value representing the color in the default sRGB

ColorModel

.
(Bits 24-31 are alpha, 16-23 are red, 8-15 are green, 0-7 are
blue).

brighter

```java
public
Color
brighter()
```

Creates a new

Color

that is a brighter version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

**Returns:** a new

Color

object that is
a brighter version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** darker()

---

#### brighter

public

Color

brighter()

Creates a new

Color

that is a brighter version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a brighter version
of this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a
series of invocations of these two methods might be inconsistent
because of rounding errors.

darker

```java
public
Color
darker()
```

Creates a new

Color

that is a darker version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

**Returns:** a new

Color

object that is
a darker version of this

Color

with the same

alpha

value.
**Since:** 1.0
**See Also:** brighter()

---

#### darker

public

Color

darker()

Creates a new

Color

that is a darker version of this

Color

.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

This method applies an arbitrary scale factor to each of the three RGB
components of this

Color

to create a darker version of
this

Color

.
The

alpha

value is preserved.
Although

brighter

and

darker

are inverse operations, the results of a series
of invocations of these two methods might be inconsistent because
of rounding errors.

hashCode

```java
public int hashCode()
```

Computes the hash code for this

Color

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code value for this object.
**Since:** 1.0
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes the hash code for this

Color

.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether another object is equal to this

Color

.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the object to test for equality with this

Color
**Returns:** true

if the objects are the same;

false

otherwise.
**Since:** 1.0
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether another object is equal to this

Color

.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

The result is

true

if and only if the argument is not

null

and is a

Color

object that has the same
red, green, blue, and alpha values as this object.

toString

```java
public
String
toString()
```

Returns a string representation of this

Color

. This
method is intended to be used only for debugging purposes. The
content and format of the returned string might vary between
implementations. The returned string might be empty but cannot
be

null

.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this

Color

.

---

#### toString

public

String

toString()

Returns a string representation of this

Color

. This
method is intended to be used only for debugging purposes. The
content and format of the returned string might vary between
implementations. The returned string might be empty but cannot
be

null

.

decode

```java
public static
Color
decode​(
String
nm)
throws
NumberFormatException
```

Converts a

String

to an integer and returns the
specified opaque

Color

. This method handles string
formats that are used to represent octal and hexadecimal numbers.

**Parameters:** nm

- a

String

that represents
an opaque color as a 24-bit integer
**Returns:** the new

Color

object.
**Throws:** NumberFormatException

- if the specified string cannot
be interpreted as a decimal,
octal, or hexadecimal integer.
**Since:** 1.1
**See Also:** Integer.decode(java.lang.String)

---

#### decode

public static

Color

decode​(

String

nm)
throws

NumberFormatException

Converts a

String

to an integer and returns the
specified opaque

Color

. This method handles string
formats that are used to represent octal and hexadecimal numbers.

getColor

```java
public static
Color
getColor​(
String
nm)
```

Finds a color in the system properties.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

**Parameters:** nm

- the name of the color property
**Returns:** the

Color

converted from the system
property.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

---

#### getColor

public static

Color

getColor​(

String

nm)

Finds a color in the system properties.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

The argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

If the specified property is not found or could not be parsed as
an integer then

null

is returned.

getColor

```java
public static
Color
getColor​(
String
nm,

Color
v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default

Color
**Returns:** the

Color

converted from the system
property, or the specified

Color

.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

---

#### getColor

public static

Color

getColor​(

String

nm,

Color

v)

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

If the specified property is not found or cannot be parsed as
an integer then the

Color

specified by the second
argument is returned instead.

getColor

```java
public static
Color
getColor​(
String
nm,
int v)
```

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

**Parameters:** nm

- the name of the color property
**Parameters:** v

- the default color value, as an integer
**Returns:** the

Color

converted from the system
property or the

Color

converted from
the specified integer.
**Since:** 1.0
**See Also:** System.getProperty(java.lang.String)

,

Integer.getInteger(java.lang.String)

,

Color(int)

---

#### getColor

public static

Color

getColor​(

String

nm,
int v)

Finds a color in the system properties.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

The first argument is treated as the name of a system property to
be obtained. The string value of this property is then interpreted
as an integer which is then converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

If the specified property is not found or could not be parsed as
an integer then the integer value

v

is used instead,
and is converted to a

Color

object.

HSBtoRGB

```java
public static int HSBtoRGB​(float hue,
float saturation,
float brightness)
```

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

**Parameters:** hue

- the hue component of the color
**Parameters:** saturation

- the saturation of the color
**Parameters:** brightness

- the brightness of the color
**Returns:** the RGB value of the color with the indicated hue,
saturation, and brightness.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

---

#### HSBtoRGB

public static int HSBtoRGB​(float hue,
float saturation,
float brightness)

Converts the components of a color, as specified by the HSB
model, to an equivalent set of values for the default RGB model.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

The

saturation

and

brightness

components
should be floating-point values between zero and one
(numbers in the range 0.0-1.0). The

hue

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

The integer that is returned by

HSBtoRGB

encodes the
value of a color in bits 0-23 of an integer value that is the same
format used by the method

getRGB

.
This integer can be supplied as an argument to the

Color

constructor that takes a single integer argument.

RGBtoHSB

```java
public static float[] RGBtoHSB​(int r,
int g,
int b,
float[] hsbvals)
```

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

**Parameters:** r

- the red component of the color
**Parameters:** g

- the green component of the color
**Parameters:** b

- the blue component of the color
**Parameters:** hsbvals

- the array used to return the
three HSB values, or

null
**Returns:** an array of three elements containing the hue, saturation,
and brightness (in that order), of the color with
the indicated red, green, and blue components.
**Since:** 1.0
**See Also:** getRGB()

,

Color(int)

,

ColorModel.getRGBdefault()

---

#### RGBtoHSB

public static float[] RGBtoHSB​(int r,
int g,
int b,
float[] hsbvals)

Converts the components of a color, as specified by the default RGB
model, to an equivalent set of values for hue, saturation, and
brightness that are the three components of the HSB model.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

If the

hsbvals

argument is

null

, then a
new array is allocated to return the result. Otherwise, the method
returns the array

hsbvals

, with the values put into
that array.

getHSBColor

```java
public static
Color
getHSBColor​(float h,
float s,
float b)
```

Creates a

Color

object based on the specified values
for the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

**Parameters:** h

- the hue component
**Parameters:** s

- the saturation of the color
**Parameters:** b

- the brightness of the color
**Returns:** a

Color

object with the specified hue,
saturation, and brightness.
**Since:** 1.0

---

#### getHSBColor

public static

Color

getHSBColor​(float h,
float s,
float b)

Creates a

Color

object based on the specified values
for the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

The

s

and

b

components should be
floating-point values between zero and one
(numbers in the range 0.0-1.0). The

h

component
can be any floating-point number. The floor of this number is
subtracted from it to create a fraction between 0 and 1. This
fractional number is then multiplied by 360 to produce the hue
angle in the HSB color model.

getRGBComponents

```java
public float[] getRGBComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.
If

compArray

is

null

, an array of length
4 is created for the return value. Otherwise,

compArray

must have length 4 or greater,
and it is filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with
color and alpha components and returns
**Returns:** the RGBA components in a

float

array.

---

#### getRGBComponents

public float[] getRGBComponents​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, as represented in the default
sRGB color space.
If

compArray

is

null

, an array of length
4 is created for the return value. Otherwise,

compArray

must have length 4 or greater,
and it is filled in with the components and returned.

getRGBColorComponents

```java
public float[] getRGBColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space. If

compArray

is

null

, an array of
length 3 is created for the return value. Otherwise,

compArray

must have length 3 or greater, and it is
filled in with the components and returned.

**Parameters:** compArray

- an array that this method fills with color
components and returns
**Returns:** the RGB components in a

float

array.

---

#### getRGBColorComponents

public float[] getRGBColorComponents​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the default sRGB color
space. If

compArray

is

null

, an array of
length 3 is created for the return value. Otherwise,

compArray

must have length 3 or greater, and it is
filled in with the components and returned.

getComponents

```java
public float[] getComponents​(float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

plus one is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color and
alpha components of this

Color

in its

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

---

#### getComponents

public float[] getComponents​(float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

plus one is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

getColorComponents

```java
public float[] getColorComponents​(float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in its

ColorSpace

and returns
**Returns:** the color components in a

float

array.

---

#### getColorComponents

public float[] getColorComponents​(float[] compArray)

Returns a

float

array containing only the color
components of the

Color

, in the

ColorSpace

of the

Color

.
If

compArray

is

null

, an array with
length equal to the number of components in the associated

ColorSpace

is created for
the return value. Otherwise,

compArray

must have at
least this length and it is filled in with the components and
returned.

getComponents

```java
public float[] getComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an
array with length equal to the number of components in

cspace

plus one is created for the return value.
Otherwise,

compArray

must have at least this
length, and it is filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the
color and alpha components of this

Color

in
the specified

ColorSpace

and returns
**Returns:** the color and alpha components in a

float

array.

---

#### getComponents

public float[] getComponents​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing the color and alpha
components of the

Color

, in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an
array with length equal to the number of components in

cspace

plus one is created for the return value.
Otherwise,

compArray

must have at least this
length, and it is filled in with the components and returned.

getColorComponents

```java
public float[] getColorComponents​(
ColorSpace
cspace,
float[] compArray)
```

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an array
with length equal to the number of components in

cspace

is created for the return value. Otherwise,

compArray

must have at least this length, and it is
filled in with the components and returned.

**Parameters:** cspace

- a specified

ColorSpace
**Parameters:** compArray

- an array that this method fills with the color
components of this

Color

in the specified

ColorSpace
**Returns:** the color components in a

float

array.

---

#### getColorComponents

public float[] getColorComponents​(

ColorSpace

cspace,
float[] compArray)

Returns a

float

array containing only the color
components of the

Color

in the

ColorSpace

specified by the

cspace

parameter. If

compArray

is

null

, an array
with length equal to the number of components in

cspace

is created for the return value. Otherwise,

compArray

must have at least this length, and it is
filled in with the components and returned.

getColorSpace

```java
public
ColorSpace
getColorSpace()
```

Returns the

ColorSpace

of this

Color

.

**Returns:** this

Color

object's

ColorSpace

.

---

#### getColorSpace

public

ColorSpace

getColorSpace()

Returns the

ColorSpace

of this

Color

.

createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
r,

Rectangle2D
r2d,

AffineTransform
xform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a solid color field pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Specified by:** createContext

in interface

Paint
**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** r

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** r2d

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** xform

- the

AffineTransform

from user
space into device space.
**Parameters:** hints

- the set of hints that the context object can use to
choose between rendering alternatives.
**Returns:** the

PaintContext

for
generating color patterns.
**See Also:** Paint

,

PaintContext

,

ColorModel

,

Rectangle

,

Rectangle2D

,

AffineTransform

,

RenderingHints

---

#### createContext

public

PaintContext

createContext​(

ColorModel

cm,

Rectangle

r,

Rectangle2D

r2d,

AffineTransform

xform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a solid color field pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

getTransparency

```java
public int getTransparency()
```

Returns the transparency mode for this

Color

. This is
required to implement the

Paint

interface.

**Specified by:** getTransparency

in interface

Transparency
**Returns:** this

Color

object's transparency mode.
**See Also:** Paint

,

Transparency

,

createContext(java.awt.image.ColorModel, java.awt.Rectangle, java.awt.geom.Rectangle2D, java.awt.geom.AffineTransform, java.awt.RenderingHints)

---

#### getTransparency

public int getTransparency()

Returns the transparency mode for this

Color

. This is
required to implement the

Paint

interface.

---

