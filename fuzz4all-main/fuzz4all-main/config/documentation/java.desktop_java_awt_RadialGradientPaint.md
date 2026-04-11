# Class RadialGradientPaint

**Source:** `java.desktop\java\awt\RadialGradientPaint.html`

### Class Description

```java
public final class
RadialGradientPaint

extends
MultipleGradientPaint
```

The

RadialGradientPaint

class provides a way to fill a shape with
a circular radial color gradient pattern. The user may specify 2 or more
gradient colors, and this paint will provide an interpolation between
each color.

The user must specify the circle controlling the gradient pattern,
which is described by a center point and a radius. The user can also
specify a separate focus point within that circle, which controls the
location of the first color of the gradient. By default the focus is
set to be the center of the circle.

This paint will map the first color of the gradient to the focus point,
and the last color to the perimeter of the circle, interpolating
smoothly for any in-between colors specified by the user. Any line drawn
from the focus point to the circumference will thus span all the gradient
colors.

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

**All Implemented Interfaces:** Paint

,

Transparency

---

### Field Details

*No entries found.*

### Constructor Details

#### public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:**
- cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- radius

- the radius of the circle defining the extents of the
color gradient
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.

**Throws:**
- NullPointerException

- if

fractions

array is null,
or

colors

array is null
- IllegalArgumentException

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:**
- center

- the center point, in user space, of the circle defining
the gradient
- radius

- the radius of the circle defining the extents of the
color gradient
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.

**Throws:**
- NullPointerException

- if

center

point is null,
or

fractions

array is null,
or

colors

array is null
- IllegalArgumentException

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:**
- cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- radius

- the radius of the circle defining the extents of the
color gradient
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:**
- center

- the center point, in user space, of the circle defining
the gradient
- radius

- the radius of the circle defining the extents of the
color gradient
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

center

point is null,
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

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:**
- cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
- radius

- the radius of the circle defining the extents of the
color gradient
- fx

- the X coordinate of the point in user space to which the
first color is mapped
- fy

- the Y coordinate of the point in user space to which the
first color is mapped
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:**
- center

- the center point, in user space, of the circle defining
the gradient. The last color of the gradient is mapped
to the perimeter of this circle.
- radius

- the radius of the circle defining the extents of the color
gradient
- focus

- the point in user space to which the first color is mapped
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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
({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
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

RadialGradientPaint

.

**Parameters:**
- center

- the center point in user space of the circle defining the
gradient. The last color of the gradient is mapped to
the perimeter of this circle.
- radius

- the radius of the circle defining the extents of the
color gradient
- focus

- the point in user space to which the first color is mapped
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### public RadialGradientPaint​(
Rectangle2D
gradientBounds,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.
The gradient circle of the

RadialGradientPaint

is defined
by the given bounding box.

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

**Parameters:**
- gradientBounds

- the bounding box, in user space, of the circle
defining the outermost extent of the gradient
- fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
- colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

gradientBounds

is null,
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

- if

gradientBounds

is empty,
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
generate a circular radial color gradient pattern.
See the description of the

createContext

method
for information on null parameter handling.

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
getCenterPoint()

Returns a copy of the center point of the radial gradient.

**Returns:**
- a

Point2D

object that is a copy of the center point

---

#### public
Point2D
getFocusPoint()

Returns a copy of the focus point of the radial gradient.
Note that if the focus point specified when the radial gradient
was constructed lies outside of the radius of the circle, this
method will still return the original focus point even though
the rendering may center the rings of color on a different
point that lies inside the radius.

**Returns:**
- a

Point2D

object that is a copy of the focus point

---

#### public float getRadius()

Returns the radius of the circle defining the radial gradient.

**Returns:**
- the radius of the circle defining the radial gradient

---

### Additional Sections

#### Class RadialGradientPaint

java.lang.Object

- java.awt.MultipleGradientPaint
- - java.awt.RadialGradientPaint

java.awt.MultipleGradientPaint

- java.awt.RadialGradientPaint

java.awt.RadialGradientPaint

**All Implemented Interfaces:** Paint

,

Transparency

```java
public final class
RadialGradientPaint

extends
MultipleGradientPaint
```

The

RadialGradientPaint

class provides a way to fill a shape with
a circular radial color gradient pattern. The user may specify 2 or more
gradient colors, and this paint will provide an interpolation between
each color.

The user must specify the circle controlling the gradient pattern,
which is described by a center point and a radius. The user can also
specify a separate focus point within that circle, which controls the
location of the first color of the gradient. By default the focus is
set to be the center of the circle.

This paint will map the first color of the gradient to the focus point,
and the last color to the perimeter of the circle, interpolating
smoothly for any in-between colors specified by the user. Any line drawn
from the focus point to the circumference will thus span all the gradient
colors.

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

**Since:** 1.6
**See Also:** Paint

,

Graphics2D.setPaint(java.awt.Paint)

public final class

RadialGradientPaint

extends

MultipleGradientPaint

The

RadialGradientPaint

class provides a way to fill a shape with
a circular radial color gradient pattern. The user may specify 2 or more
gradient colors, and this paint will provide an interpolation between
each color.

The user must specify the circle controlling the gradient pattern,
which is described by a center point and a radius. The user can also
specify a separate focus point within that circle, which controls the
location of the first color of the gradient. By default the focus is
set to be the center of the circle.

This paint will map the first color of the gradient to the focus point,
and the last color to the perimeter of the circle, interpolating
smoothly for any in-between colors specified by the user. Any line drawn
from the focus point to the circumference will thus span all the gradient
colors.

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

The user must specify the circle controlling the gradient pattern,
which is described by a center point and a radius. The user can also
specify a separate focus point within that circle, which controls the
location of the first color of the gradient. By default the focus is
set to be the center of the circle.

This paint will map the first color of the gradient to the focus point,
and the last color to the perimeter of the circle, interpolating
smoothly for any in-between colors specified by the user. Any line drawn
from the focus point to the circumference will thus span all the gradient
colors.

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

This paint will map the first color of the gradient to the focus point,
and the last color to the perimeter of the circle, interpolating
smoothly for any in-between colors specified by the user. Any line drawn
from the focus point to the circumference will thus span all the gradient
colors.

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

Specifying a focus point outside of the radius of the circle will cause
the rings of the gradient pattern to be centered on the point just inside
the edge of the circle in the direction of the focus point.
The rendering will internally use this modified location as if it were
the specified focus point.

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

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

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

{Color.BLUE, Color.RED}, {.3f, .7f}

{Color.BLUE, Color.BLUE, Color.RED, Color.RED}, {0f, .3f, .7f, 1f}

The user may also select what action the

RadialGradientPaint

object
takes when it is filling the space outside the circle's radius by
setting

CycleMethod

to either

REFLECTION

or

REPEAT

.
The gradient color proportions are equal for any particular line drawn
from the focus point. The following figure shows that the distance AB
is equal to the distance BC, and the distance AD is equal to the distance DE.

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

If the gradient and graphics rendering transforms are uniformly scaled and
the user sets the focus so that it coincides with the center of the circle,
the gradient color proportions are equal for any line drawn from the center.
The following figure shows the distances AB, BC, AD, and DE. They are all equal.

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

Note that some minor variations in distances may occur due to sampling at
the granularity of a pixel.
If no cycle method is specified,

NO_CYCLE

will be chosen by
default, which means the last keyframe color will be used to fill the
remaining area.

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

The colorSpace parameter allows the user to specify in which colorspace
the interpolation should be performed, default sRGB or linearized RGB.

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

The following code demonstrates typical usage of

RadialGradientPaint

, where the center and focus points are
the same:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);
```

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

Point2D center = new Point2D.Float(50, 50);
float radius = 25;
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, dist, colors);

This image demonstrates the example code above, with default
(centered) focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

It is also possible to specify a non-centered focus point, as
in the following code:

```java
Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);
```

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

Point2D center = new Point2D.Float(50, 50);
float radius = 25;
Point2D focus = new Point2D.Float(40, 40);
float[] dist = {0.0f, 0.2f, 1.0f};
Color[] colors = {Color.RED, Color.WHITE, Color.BLUE};
RadialGradientPaint p =
new RadialGradientPaint(center, radius, focus,
dist, colors,
CycleMethod.NO_CYCLE);

This image demonstrates the previous example code, with non-centered
focus for each of the three cycle methods:

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

RadialGradientPaint

​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

​(

Point2D

center,
float radius,

Point2D

focus,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

​(

Point2D

center,
float radius,

Point2D

focus,
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

RadialGradientPaint

.

RadialGradientPaint

​(

Rectangle2D

gradientBounds,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

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
generate a circular radial color gradient pattern.

Point2D

getCenterPoint

()

Returns a copy of the center point of the radial gradient.

Point2D

getFocusPoint

()

Returns a copy of the focus point of the radial gradient.

float

getRadius

()

Returns the radius of the circle defining the radial gradient.

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

RadialGradientPaint

​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

​(

Point2D

center,
float radius,

Point2D

focus,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

​(

Point2D

center,
float radius,

Point2D

focus,
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

RadialGradientPaint

.

RadialGradientPaint

​(

Rectangle2D

gradientBounds,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

---

#### Constructor Summary

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

Constructs a

RadialGradientPaint

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
generate a circular radial color gradient pattern.

Point2D

getCenterPoint

()

Returns a copy of the center point of the radial gradient.

Point2D

getFocusPoint

()

Returns a copy of the focus point of the radial gradient.

float

getRadius

()

Returns the radius of the circle defining the radial gradient.

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
generate a circular radial color gradient pattern.

Returns a copy of the center point of the radial gradient.

Returns a copy of the focus point of the radial gradient.

Returns the radius of the circle defining the radial gradient.

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

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

center

point is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

center

point is null,
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fx

- the X coordinate of the point in user space to which the
first color is mapped
**Parameters:** fy

- the Y coordinate of the point in user space to which the
first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient. The last color of the gradient is mapped
to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the color
gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
@ConstructorProperties
({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
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

RadialGradientPaint

.

**Parameters:** center

- the center point in user space of the circle defining the
gradient. The last color of the gradient is mapped to
the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Rectangle2D
gradientBounds,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.
The gradient circle of the

RadialGradientPaint

is defined
by the given bounding box.

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

**Parameters:** gradientBounds

- the bounding box, in user space, of the circle
defining the outermost extent of the gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

gradientBounds

is null,
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

- if

gradientBounds

is empty,
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
generate a circular radial color gradient pattern.
See the description of the

createContext

method
for information on null parameter handling.

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

- getCenterPoint

```java
public
Point2D
getCenterPoint()
```

Returns a copy of the center point of the radial gradient.

**Returns:** a

Point2D

object that is a copy of the center point

- getFocusPoint

```java
public
Point2D
getFocusPoint()
```

Returns a copy of the focus point of the radial gradient.
Note that if the focus point specified when the radial gradient
was constructed lies outside of the radius of the circle, this
method will still return the original focus point even though
the rendering may center the rings of color on a different
point that lies inside the radius.

**Returns:** a

Point2D

object that is a copy of the focus point

- getRadius

```java
public float getRadius()
```

Returns the radius of the circle defining the radial gradient.

**Returns:** the radius of the circle defining the radial gradient

Constructor Detail

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

center

point is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

center

point is null,
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fx

- the X coordinate of the point in user space to which the
first color is mapped
**Parameters:** fy

- the Y coordinate of the point in user space to which the
first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient. The last color of the gradient is mapped
to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the color
gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
@ConstructorProperties
({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
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

RadialGradientPaint

.

**Parameters:** center

- the center point in user space of the circle defining the
gradient. The last color of the gradient is mapped to
the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

- RadialGradientPaint

```java
public RadialGradientPaint​(
Rectangle2D
gradientBounds,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.
The gradient circle of the

RadialGradientPaint

is defined
by the given bounding box.

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

**Parameters:** gradientBounds

- the bounding box, in user space, of the circle
defining the outermost extent of the gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

gradientBounds

is null,
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

- if

gradientBounds

is empty,
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

RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors)
```

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
**Throws:** NullPointerException

- if

center

point is null,
or

fractions

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors)

Constructs a

RadialGradientPaint

with a default

NO_CYCLE

repeating method and

SRGB

color space,
using the center as the focus point.

RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(float cx,
float cy,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

center

point is null,
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

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(

Point2D

center,
float radius,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space, using the center as the focus point.

RadialGradientPaint

```java
public RadialGradientPaint​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** cx

- the X coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** cy

- the Y coordinate in user space of the center point of the
circle defining the gradient. The last color of the
gradient is mapped to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** fx

- the X coordinate of the point in user space to which the
first color is mapped
**Parameters:** fy

- the Y coordinate of the point in user space to which the
first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(float cx,
float cy,
float radius,
float fx,
float fy,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

```java
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

**Parameters:** center

- the center point, in user space, of the circle defining
the gradient. The last color of the gradient is mapped
to the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the color
gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### RadialGradientPaint

public RadialGradientPaint​(

Point2D

center,
float radius,

Point2D

focus,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.

RadialGradientPaint

```java
@ConstructorProperties
({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public RadialGradientPaint​(
Point2D
center,
float radius,

Point2D
focus,
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

RadialGradientPaint

.

**Parameters:** center

- the center point in user space of the circle defining the
gradient. The last color of the gradient is mapped to
the perimeter of this circle.
**Parameters:** radius

- the radius of the circle defining the extents of the
color gradient
**Parameters:** focus

- the point in user space to which the first color is mapped
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

- if

radius

is non-positive,
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

#### RadialGradientPaint

@ConstructorProperties

({"centerPoint","radius","focusPoint","fractions","colors","cycleMethod","colorSpace","transform"})
public RadialGradientPaint​(

Point2D

center,
float radius,

Point2D

focus,
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

RadialGradientPaint

.

RadialGradientPaint

```java
public RadialGradientPaint​(
Rectangle2D
gradientBounds,
float[] fractions,

Color
[] colors,

MultipleGradientPaint.CycleMethod
cycleMethod)
```

Constructs a

RadialGradientPaint

with a default

SRGB

color space.
The gradient circle of the

RadialGradientPaint

is defined
by the given bounding box.

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

**Parameters:** gradientBounds

- the bounding box, in user space, of the circle
defining the outermost extent of the gradient
**Parameters:** fractions

- numbers ranging from 0.0 to 1.0 specifying the
distribution of colors along the gradient
**Parameters:** colors

- array of colors to use in the gradient. The first color
is used at the focus point, the last color around the
perimeter of the circle.
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

gradientBounds

is null,
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

- if

gradientBounds

is empty,
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

#### RadialGradientPaint

public RadialGradientPaint​(

Rectangle2D

gradientBounds,
float[] fractions,

Color

[] colors,

MultipleGradientPaint.CycleMethod

cycleMethod)

Constructs a

RadialGradientPaint

with a default

SRGB

color space.
The gradient circle of the

RadialGradientPaint

is defined
by the given bounding box.

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

This constructor is a more convenient way to express the
following (equivalent) code:

```java
double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);
```

double gw = gradientBounds.getWidth();
double gh = gradientBounds.getHeight();
double cx = gradientBounds.getCenterX();
double cy = gradientBounds.getCenterY();
Point2D center = new Point2D.Double(cx, cy);

AffineTransform gradientTransform = new AffineTransform();
gradientTransform.translate(cx, cy);
gradientTransform.scale(gw / 2, gh / 2);
gradientTransform.translate(-cx, -cy);

RadialGradientPaint gp =
new RadialGradientPaint(center, 1.0f, center,
fractions, colors,
cycleMethod,
ColorSpaceType.SRGB,
gradientTransform);

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
generate a circular radial color gradient pattern.
See the description of the

createContext

method
for information on null parameter handling.

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

- getCenterPoint

```java
public
Point2D
getCenterPoint()
```

Returns a copy of the center point of the radial gradient.

**Returns:** a

Point2D

object that is a copy of the center point

- getFocusPoint

```java
public
Point2D
getFocusPoint()
```

Returns a copy of the focus point of the radial gradient.
Note that if the focus point specified when the radial gradient
was constructed lies outside of the radius of the circle, this
method will still return the original focus point even though
the rendering may center the rings of color on a different
point that lies inside the radius.

**Returns:** a

Point2D

object that is a copy of the focus point

- getRadius

```java
public float getRadius()
```

Returns the radius of the circle defining the radial gradient.

**Returns:** the radius of the circle defining the radial gradient

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
generate a circular radial color gradient pattern.
See the description of the

createContext

method
for information on null parameter handling.

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
generate a circular radial color gradient pattern.
See the description of the

createContext

method
for information on null parameter handling.

getCenterPoint

```java
public
Point2D
getCenterPoint()
```

Returns a copy of the center point of the radial gradient.

**Returns:** a

Point2D

object that is a copy of the center point

---

#### getCenterPoint

public

Point2D

getCenterPoint()

Returns a copy of the center point of the radial gradient.

getFocusPoint

```java
public
Point2D
getFocusPoint()
```

Returns a copy of the focus point of the radial gradient.
Note that if the focus point specified when the radial gradient
was constructed lies outside of the radius of the circle, this
method will still return the original focus point even though
the rendering may center the rings of color on a different
point that lies inside the radius.

**Returns:** a

Point2D

object that is a copy of the focus point

---

#### getFocusPoint

public

Point2D

getFocusPoint()

Returns a copy of the focus point of the radial gradient.
Note that if the focus point specified when the radial gradient
was constructed lies outside of the radius of the circle, this
method will still return the original focus point even though
the rendering may center the rings of color on a different
point that lies inside the radius.

getRadius

```java
public float getRadius()
```

Returns the radius of the circle defining the radial gradient.

**Returns:** the radius of the circle defining the radial gradient

---

#### getRadius

public float getRadius()

Returns the radius of the circle defining the radial gradient.

---

