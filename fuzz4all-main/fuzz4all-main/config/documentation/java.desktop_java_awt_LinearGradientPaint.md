# Class LinearGradientPaint

**Source:** `java.desktop\java\awt\LinearGradientPaint.html`

### Class Description

```java
public final class
LinearGradientPaint

extends
MultipleGradientPaint
```

The

LinearGradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern. The user
may specify two or more gradient colors, and this paint will provide an
interpolation between each color. The user also specifies start and end
points which define where in user space the color gradient should begin
and end.

The user must provide an array of floats specifying how to distribute the
colors along the gradient. These values should range from 0.0 to 1.0 and
act like keyframes along the gradient (they mark where the gradient should
be exactly a particular color).

In the event that the user does not set the first keyframe value equal
to 0 and/or the last keyframe value equal to 1, keyframes will be created
at these positions and the first and last colors will be replicated there.
So, if a user specifies the following arrays to construct a gradient:

```java
{Color.BLUE, Color.RED}, {.3f, .7f}
```

this will be converted to a gradient with the following keyframes:

```java
{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}
```

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

**All Implemented Interfaces:** Paint

,

Transparency

---

### Field Details

*No entries found.*

### Constructor Details

#### public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:**
- startX

- the X coordinate of the gradient axis start point
in user space
- startY

- the Y coordinate of the gradient axis start point
in user space
- endX

- the X coordinate of the gradient axis end point
in user space
- endY

- the Y coordinate of the gradient axis end point
in user space
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors corresponding to each fractional value

**Throws:**
- NullPointerException

- if

fractions

array is null,
or

colors

array is null,
- IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:**
- startX

- the X coordinate of the gradient axis start point
in user space
- startY

- the Y coordinate of the gradient axis start point
in user space
- endX

- the X coordinate of the gradient axis end point
in user space
- endY

- the Y coordinate of the gradient axis end point
in user space
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors corresponding to each fractional value
- cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT

**Throws:**
- NullPointerException

- if

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
- IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:**
- start

- the gradient axis start

Point2D

in user space
- end

- the gradient axis end

Point2D

in user space
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors corresponding to each fractional value

**Throws:**
- NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null
- IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:**
- start

- the gradient axis start

Point2D

in user space
- end

- the gradient axis end

Point2D

in user space
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors corresponding to each fractional value
- cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT

**Throws:**
- NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
- IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### @ConstructorProperties
({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod,

MultipleGradientPaint.ColorSpaceType
colorSpace,

AffineTransform
gradientTransform)

Constructs a

LinearGradientPaint

.

**Parameters:**
- start

- the gradient axis start

Point2D

in user space
- end

- the gradient axis end

Point2D

in user space
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors corresponding to each fractional value
- cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
- colorSpace

- which color space to use for interpolation,
either

SRGB

or

LINEAR_RGB
- gradientTransform

- transform to apply to the gradient

**Throws:**
- NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null,
or

colorSpace

is null,
or

gradientTransform

is null
- IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

### Method Details

#### public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
transform,

RenderingHints
hints)

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Parameters:**
- cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
- deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
- userBounds

- the user space bounding box
of the graphics primitive being rendered.
- transform

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

#### public
Point2D
getStartPoint()

Returns a copy of the start point of the gradient axis.

**Returns:**
- a

Point2D

object that is a copy of the point
that anchors the first color of this

LinearGradientPaint

---

#### public
Point2D
getEndPoint()

Returns a copy of the end point of the gradient axis.

**Returns:**
- a

Point2D

object that is a copy of the point
that anchors the last color of this

LinearGradientPaint

---

### Additional Sections

#### Class LinearGradientPaint

java.lang.Object

- java.awt.MultipleGradientPaint
- - java.awt.LinearGradientPaint

java.awt.MultipleGradientPaint

- java.awt.LinearGradientPaint

java.awt.LinearGradientPaint

**All Implemented Interfaces:** Paint

,

Transparency

```java
public final class
LinearGradientPaint

extends
MultipleGradientPaint
```

The

LinearGradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern. The user
may specify two or more gradient colors, and this paint will provide an
interpolation between each color. The user also specifies start and end
points which define where in user space the color gradient should begin
and end.

The user must provide an array of floats specifying how to distribute the
colors along the gradient. These values should range from 0.0 to 1.0 and
act like keyframes along the gradient (they mark where the gradient should
be exactly a particular color).

In the event that the user does not set the first keyframe value equal
to 0 and/or the last keyframe value equal to 1, keyframes will be created
at these positions and the first and last colors will be replicated there.
So, if a user specifies the following arrays to construct a gradient:

```java
{Color.BLUE, Color.RED}, {.3f, .7f}
```

this will be converted to a gradient with the following keyframes:

```java
{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}
```

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

**Since:** 1.6
**See Also:** Paint

,

Graphics2D.setPaint(java.awt.Paint)

public final class

LinearGradientPaint

extends

MultipleGradientPaint

The

LinearGradientPaint

class provides a way to fill
a

Shape

with a linear color gradient pattern. The user
may specify two or more gradient colors, and this paint will provide an
interpolation between each color. The user also specifies start and end
points which define where in user space the color gradient should begin
and end.

The user must provide an array of floats specifying how to distribute the
colors along the gradient. These values should range from 0.0 to 1.0 and
act like keyframes along the gradient (they mark where the gradient should
be exactly a particular color).

In the event that the user does not set the first keyframe value equal
to 0 and/or the last keyframe value equal to 1, keyframes will be created
at these positions and the first and last colors will be replicated there.
So, if a user specifies the following arrays to construct a gradient:

```java
{Color.BLUE, Color.RED}, {.3f, .7f}
```

this will be converted to a gradient with the following keyframes:

```java
{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}
```

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

The user must provide an array of floats specifying how to distribute the
colors along the gradient. These values should range from 0.0 to 1.0 and
act like keyframes along the gradient (they mark where the gradient should
be exactly a particular color).

In the event that the user does not set the first keyframe value equal
to 0 and/or the last keyframe value equal to 1, keyframes will be created
at these positions and the first and last colors will be replicated there.
So, if a user specifies the following arrays to construct a gradient:

```java
{Color.BLUE, Color.RED}, {.3f, .7f}
```

this will be converted to a gradient with the following keyframes:

```java
{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}
```

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

In the event that the user does not set the first keyframe value equal
to 0 and/or the last keyframe value equal to 1, keyframes will be created
at these positions and the first and last colors will be replicated there.
So, if a user specifies the following arrays to construct a gradient:

```java
{Color.BLUE, Color.RED}, {.3f, .7f}
```

this will be converted to a gradient with the following keyframes:

```java
{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}
```

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

{Color.BLUE, Color.RED}, {.3f, .7f}

{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}

The user may also select what action the

LinearGradientPaint

object
takes when it is filling the space outside the start and end points by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The distances between any two colors in any of the reflected or repeated
copies of the gradient are the same as the distance between those same two
colors between the start and end points.
Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the endpoint colors will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

The following code demonstrates typical usage of

LinearGradientPaint

:

```java
Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);
```

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

Point2D start = new Point2D.Float(0, 0);
Point2D end = new Point2D.Float(50, 50);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
LinearGradientPaint p =
new LinearGradientPaint(start, end, dist, colors);

This code will create a

LinearGradientPaint

which interpolates
between red and white for the first 20% of the gradient and between white
and blue for the remaining 80%.

This image demonstrates the example code above for each
of the three cycle methods:

This image demonstrates the example code above for each
of the three cycle methods:

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class java.awt.

MultipleGradientPaint

MultipleGradientPaint.ColorSpaceType

,

MultipleGradientPaint.CycleMethod

=========== FIELD SUMMARY ===========

- Field Summary

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

LinearGradientPaint

​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod,

MultipleGradientPaint.ColorSpaceType

colorSpace,

AffineTransform

gradientTransform)

Constructs a

LinearGradientPaint

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

transform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.

Point2D

getEndPoint

()

Returns a copy of the end point of the gradient axis.

Point2D

getStartPoint

()

Returns a copy of the start point of the gradient axis.

- Methods declared in class java.awt.

MultipleGradientPaint

getColors

,

getColorSpace

,

getCycleMethod

,

getFractions

,

getTransform

,

getTransparency

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

Nested Class Summary

- Nested classes/interfaces declared in class java.awt.

MultipleGradientPaint

MultipleGradientPaint.ColorSpaceType

,

MultipleGradientPaint.CycleMethod

---

#### Nested Class Summary

Nested classes/interfaces declared in class java.awt.

MultipleGradientPaint

MultipleGradientPaint.ColorSpaceType

,

MultipleGradientPaint.CycleMethod

---

#### Nested classes/interfaces declared in class java.awt. MultipleGradientPaint

Field Summary

- Fields declared in interface java.awt.

Transparency

BITMASK

,

OPAQUE

,

TRANSLUCENT

---

#### Field Summary

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

LinearGradientPaint

​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod,

MultipleGradientPaint.ColorSpaceType

colorSpace,

AffineTransform

gradientTransform)

Constructs a

LinearGradientPaint

.

---

#### Constructor Summary

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

Constructs a

LinearGradientPaint

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

PaintContext

createContext

​(

ColorModel

cm,

Rectangle

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

transform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.

Point2D

getEndPoint

()

Returns a copy of the end point of the gradient axis.

Point2D

getStartPoint

()

Returns a copy of the start point of the gradient axis.

- Methods declared in class java.awt.

MultipleGradientPaint

getColors

,

getColorSpace

,

getCycleMethod

,

getFractions

,

getTransform

,

getTransparency

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

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.

Returns a copy of the end point of the gradient axis.

Returns a copy of the start point of the gradient axis.

Methods declared in class java.awt.

MultipleGradientPaint

getColors

,

getColorSpace

,

getCycleMethod

,

getFractions

,

getTransform

,

getTransparency

---

#### Methods declared in class java.awt. MultipleGradientPaint

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
@ConstructorProperties
({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod,

MultipleGradientPaint.ColorSpaceType
colorSpace,

AffineTransform
gradientTransform)
```

Constructs a

LinearGradientPaint

.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Parameters:** colorSpace

- which color space to use for interpolation,
either

SRGB

or

LINEAR_RGB
**Parameters:** gradientTransform

- transform to apply to the gradient
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null,
or

colorSpace

is null,
or

gradientTransform

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

============ METHOD DETAIL ==========

- Method Detail

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
transform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** transform

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

- getStartPoint

```java
public
Point2D
getStartPoint()
```

Returns a copy of the start point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

LinearGradientPaint

- getEndPoint

```java
public
Point2D
getEndPoint()
```

Returns a copy of the end point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the last color of this

LinearGradientPaint

Constructor Detail

- LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

- LinearGradientPaint

```java
@ConstructorProperties
({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod,

MultipleGradientPaint.ColorSpaceType
colorSpace,

AffineTransform
gradientTransform)
```

Constructs a

LinearGradientPaint

.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Parameters:** colorSpace

- which color space to use for interpolation,
either

SRGB

or

LINEAR_RGB
**Parameters:** gradientTransform

- transform to apply to the gradient
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null,
or

colorSpace

is null,
or

gradientTransform

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### Constructor Detail

LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### LinearGradientPaint

public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

```java
public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** startX

- the X coordinate of the gradient axis start point
in user space
**Parameters:** startY

- the Y coordinate of the gradient axis start point
in user space
**Parameters:** endX

- the X coordinate of the gradient axis end point
in user space
**Parameters:** endY

- the Y coordinate of the gradient axis end point
in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### LinearGradientPaint

public LinearGradientPaint​(float startX,
float startY,
float endX,
float endY,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors)
```

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### LinearGradientPaint

public LinearGradientPaint​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors)

Constructs a

LinearGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space.

LinearGradientPaint

```java
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### LinearGradientPaint

public LinearGradientPaint​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

LinearGradientPaint

with a default

SRGB

color space.

LinearGradientPaint

```java
@ConstructorProperties
({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public LinearGradientPaint​(
Point2D
start,

Point2D
end,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod,

MultipleGradientPaint.ColorSpaceType
colorSpace,

AffineTransform
gradientTransform)
```

Constructs a

LinearGradientPaint

.

**Parameters:** start

- the gradient axis start

Point2D

in user space
**Parameters:** end

- the gradient axis end

Point2D

in user space
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors corresponding to each fractional value
**Parameters:** cycleMethod

- either

NO_CYCLE

,

REFLECT

,
or

REPEAT
**Parameters:** colorSpace

- which color space to use for interpolation,
either

SRGB

or

LINEAR_RGB
**Parameters:** gradientTransform

- transform to apply to the gradient
**Throws:** NullPointerException

- if one of the points is null,
or

fractions

array is null,
or

colors

array is null,
or

cycleMethod

is null,
or

colorSpace

is null,
or

gradientTransform

is null
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

fractions.length != colors.length

,
or

colors

is less than 2 in size,
or a

fractions

value is less than 0.0 or greater than 1.0,
or the

fractions

are not provided in strictly increasing order

---

#### LinearGradientPaint

@ConstructorProperties

({"startPoint","endPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public LinearGradientPaint​(

Point2D

start,

Point2D

end,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod,

MultipleGradientPaint.ColorSpaceType

colorSpace,

AffineTransform

gradientTransform)

Constructs a

LinearGradientPaint

.

Method Detail

- createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
transform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** transform

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

- getStartPoint

```java
public
Point2D
getStartPoint()
```

Returns a copy of the start point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

LinearGradientPaint

- getEndPoint

```java
public
Point2D
getEndPoint()
```

Returns a copy of the end point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the last color of this

LinearGradientPaint

---

#### Method Detail

createContext

```java
public
PaintContext
createContext​(
ColorModel
cm,

Rectangle
deviceBounds,

Rectangle2D
userBounds,

AffineTransform
transform,

RenderingHints
hints)
```

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

**Parameters:** cm

- the preferred

ColorModel

which represents the most convenient
format for the caller to receive the pixel data, or

null

if there is no preference.
**Parameters:** deviceBounds

- the device space bounding box
of the graphics primitive being rendered.
**Parameters:** userBounds

- the user space bounding box
of the graphics primitive being rendered.
**Parameters:** transform

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

deviceBounds,

Rectangle2D

userBounds,

AffineTransform

transform,

RenderingHints

hints)

Creates and returns a

PaintContext

used to
generate a linear color gradient pattern.
See the

specification

of the
method in the

Paint

interface for information
on null parameter handling.

getStartPoint

```java
public
Point2D
getStartPoint()
```

Returns a copy of the start point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the first color of this

LinearGradientPaint

---

#### getStartPoint

public

Point2D

getStartPoint()

Returns a copy of the start point of the gradient axis.

getEndPoint

```java
public
Point2D
getEndPoint()
```

Returns a copy of the end point of the gradient axis.

**Returns:** a

Point2D

object that is a copy of the point
that anchors the last color of this

LinearGradientPaint

---

#### getEndPoint

public

Point2D

getEndPoint()

Returns a copy of the end point of the gradient axis.

---

