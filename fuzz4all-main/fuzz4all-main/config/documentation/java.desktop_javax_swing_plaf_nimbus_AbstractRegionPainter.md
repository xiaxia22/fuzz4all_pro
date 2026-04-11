# Class AbstractRegionPainter

**Source:** `java.desktop\javax\swing\plaf\nimbus\AbstractRegionPainter.html`

### Class Description

```java
public abstract class
AbstractRegionPainter

extends
Object

implements
Painter
<
JComponent
>
```

Convenient base class for defining Painter instances for rendering a
region or component in Nimbus.

**All Implemented Interfaces:** Painter

<

JComponent

>

---

### Field Details

*No entries found.*

### Constructor Details

#### protected AbstractRegionPainter()

Create a new AbstractRegionPainter

---

### Method Details

#### protected
Object
[] getExtendedCacheKeys​(
JComponent
c)

Get any extra attributes which the painter implementation would like
to include in the image cache lookups. This is checked for every call
of the paint(g, c, w, h) method.

**Parameters:**
- c

- The component on the current paint call

**Returns:**
- Array of extra objects to be included in the cache key

---

#### protected abstract
AbstractRegionPainter.PaintContext
getPaintContext()

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

**Returns:**
- a PaintContext associated with this paint operation.

---

#### protected void configureGraphics​(
Graphics2D
g)

Configures the given Graphics2D. Often, rendering hints or compositing rules are
applied to a Graphics2D object prior to painting, which should affect all of the
subsequent painting operations. This method provides a convenient hook for configuring
the Graphics object prior to rendering, regardless of whether the render operation is
performed to an intermediate buffer or directly to the display.

**Parameters:**
- g

- The Graphics2D object to configure. Will not be null.

---

#### protected abstract void doPaint​(
Graphics2D
g,

JComponent
c,
int width,
int height,

Object
[] extendedCacheKeys)

Actually performs the painting operation. Subclasses must implement this method.
The graphics object passed may represent the actual surface being rendered to,
or it may be an intermediate buffer. It has also been pre-translated. Simply render
the component as if it were located at 0, 0 and had a width of

width

and a height of

height

. For performance reasons, you may want to read
the clip from the Graphics2D object and only render within that space.

**Parameters:**
- g

- The Graphics2D surface to paint to
- c

- The JComponent related to the drawing event. For example, if the
region being rendered is Button, then

c

will be a
JButton. If the region being drawn is ScrollBarSlider, then the
component will be JScrollBar. This value may be null.
- width

- The width of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getWidth().
- height

- The height of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getHeight().
- extendedCacheKeys

- The result of the call to getExtendedCacheKeys()

---

#### protected final float decodeX​(float x)

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

**Parameters:**
- x

- an encoded x value (0...1, or 1...2, or 2...3)

**Returns:**
- the decoded x value

**Throws:**
- IllegalArgumentException

- if

x < 0

or

x > 3

---

#### protected final float decodeY​(float y)

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

**Parameters:**
- y

- an encoded y value (0...1, or 1...2, or 2...3)

**Returns:**
- the decoded y value

**Throws:**
- IllegalArgumentException

- if

y < 0

or

y > 3

---

#### protected final float decodeAnchorX​(float x,
float dx)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:**
- x

- an encoded x value of the bezier control point (0...1, or 1...2, or 2...3)
- dx

- the offset distance to the anchor from the control point x

**Returns:**
- the decoded x location of the control point

**Throws:**
- IllegalArgumentException

- if

x < 0

or

x > 3

---

#### protected final float decodeAnchorY​(float y,
float dy)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:**
- y

- an encoded y value of the bezier control point (0...1, or 1...2, or 2...3)
- dy

- the offset distance to the anchor from the control point y

**Returns:**
- the decoded y position of the control point

**Throws:**
- IllegalArgumentException

- if

y < 0

or

y > 3

---

#### protected final
Color
decodeColor​(
String
key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)

Decodes and returns a color, which is derived from a base color in UI
defaults.

**Parameters:**
- key

- A key corresponding to the value in the UI Defaults table
of UIManager where the base color is defined
- hOffset

- The hue offset used for derivation.
- sOffset

- The saturation offset used for derivation.
- bOffset

- The brightness offset used for derivation.
- aOffset

- The alpha offset used for derivation. Between 0...255

**Returns:**
- The derived color, whose color value will change if the parent
uiDefault color changes.

---

#### protected final
Color
decodeColor​(
Color
color1,

Color
color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:**
- color1

- The first color
- color2

- The second color
- midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;

**Returns:**
- The derived color

---

#### protected final
LinearGradientPaint
decodeGradient​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color
[] colors)

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint. One primary purpose for this
method is to avoid creating a LinearGradientPaint where the start and
end points are equal. In such a case, the end y point is slightly
increased to avoid the overlap.

**Parameters:**
- x1

- x1
- y1

- y1
- x2

- x2
- y2

- y2
- midpoints

- the midpoints
- colors

- the colors

**Returns:**
- a valid LinearGradientPaint. This method never returns null.

**Throws:**
- NullPointerException

- if

midpoints

array is null,
or

colors

array is null,
- IllegalArgumentException

- if start and end points are the same points,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

---

#### protected final
RadialGradientPaint
decodeRadialGradient​(float x,
float y,
float r,
float[] midpoints,

Color
[] colors)

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint. One primary purpose for this
method is to avoid creating a RadialGradientPaint where the radius
is non-positive. In such a case, the radius is just slightly
increased to avoid 0.

**Parameters:**
- x

- x-coordinate
- y

- y-coordinate
- r

- radius
- midpoints

- the midpoints
- colors

- the colors

**Returns:**
- a valid RadialGradientPaint. This method never returns null.

**Throws:**
- NullPointerException

- if

midpoints

array is null,
or

colors

array is null
- IllegalArgumentException

- if

r

is non-positive,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

---

#### protected final
Color
getComponentColor​(
JComponent
c,

String
property,

Color
defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)

Get a color property from the given JComponent. First checks for a

getXXX()

method and if that fails checks for a client
property with key

property

. If that still fails to return
a Color then

defaultColor

is returned.

**Parameters:**
- c

- The component to get the color property from
- property

- The name of a bean style property or client property
- defaultColor

- The color to return if no color was obtained from
the component.
- saturationOffset

- additively modifies the HSB saturation component
of the color returned (ignored if default color is returned).
- brightnessOffset

- additively modifies the HSB brightness component
of the color returned (ignored if default color is returned).
- alphaOffset

- additively modifies the ARGB alpha component of the
color returned (ignored if default color is returned).

**Returns:**
- The color that was obtained from the component or defaultColor

---

### Additional Sections

#### Class AbstractRegionPainter

java.lang.Object

- javax.swing.plaf.nimbus.AbstractRegionPainter

javax.swing.plaf.nimbus.AbstractRegionPainter

**All Implemented Interfaces:** Painter

<

JComponent

>

```java
public abstract class
AbstractRegionPainter

extends
Object

implements
Painter
<
JComponent
>
```

Convenient base class for defining Painter instances for rendering a
region or component in Nimbus.

public abstract class

AbstractRegionPainter

extends

Object

implements

Painter

<

JComponent

>

Convenient base class for defining Painter instances for rendering a
region or component in Nimbus.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

AbstractRegionPainter.PaintContext

A class encapsulating state useful when painting.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractRegionPainter

()

Create a new AbstractRegionPainter

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

configureGraphics

​(

Graphics2D

g)

Configures the given Graphics2D.

protected float

decodeAnchorX

​(float x,
float dx)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

protected float

decodeAnchorY

​(float y,
float dy)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

protected

Color

decodeColor

​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

protected

Color

decodeColor

​(

String

key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)

Decodes and returns a color, which is derived from a base color in UI
defaults.

protected

LinearGradientPaint

decodeGradient

​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color

[] colors)

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint.

protected

RadialGradientPaint

decodeRadialGradient

​(float x,
float y,
float r,
float[] midpoints,

Color

[] colors)

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint.

protected float

decodeX

​(float x)

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

protected float

decodeY

​(float y)

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

protected abstract void

doPaint

​(

Graphics2D

g,

JComponent

c,
int width,
int height,

Object

[] extendedCacheKeys)

Actually performs the painting operation.

protected

Color

getComponentColor

​(

JComponent

c,

String

property,

Color

defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)

Get a color property from the given JComponent.

protected

Object

[]

getExtendedCacheKeys

​(

JComponent

c)

Get any extra attributes which the painter implementation would like
to include in the image cache lookups.

protected abstract

AbstractRegionPainter.PaintContext

getPaintContext

()

Gets the PaintContext for this painting operation.

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

- Methods declared in interface javax.swing.

Painter

paint

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected static class

AbstractRegionPainter.PaintContext

A class encapsulating state useful when painting.

---

#### Nested Class Summary

A class encapsulating state useful when painting.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

AbstractRegionPainter

()

Create a new AbstractRegionPainter

---

#### Constructor Summary

Create a new AbstractRegionPainter

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

configureGraphics

​(

Graphics2D

g)

Configures the given Graphics2D.

protected float

decodeAnchorX

​(float x,
float dx)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

protected float

decodeAnchorY

​(float y,
float dy)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

protected

Color

decodeColor

​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

protected

Color

decodeColor

​(

String

key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)

Decodes and returns a color, which is derived from a base color in UI
defaults.

protected

LinearGradientPaint

decodeGradient

​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color

[] colors)

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint.

protected

RadialGradientPaint

decodeRadialGradient

​(float x,
float y,
float r,
float[] midpoints,

Color

[] colors)

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint.

protected float

decodeX

​(float x)

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

protected float

decodeY

​(float y)

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

protected abstract void

doPaint

​(

Graphics2D

g,

JComponent

c,
int width,
int height,

Object

[] extendedCacheKeys)

Actually performs the painting operation.

protected

Color

getComponentColor

​(

JComponent

c,

String

property,

Color

defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)

Get a color property from the given JComponent.

protected

Object

[]

getExtendedCacheKeys

​(

JComponent

c)

Get any extra attributes which the painter implementation would like
to include in the image cache lookups.

protected abstract

AbstractRegionPainter.PaintContext

getPaintContext

()

Gets the PaintContext for this painting operation.

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

- Methods declared in interface javax.swing.

Painter

paint

---

#### Method Summary

Configures the given Graphics2D.

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

Decodes and returns a color, which is derived from a offset between two
other colors.

Decodes and returns a color, which is derived from a base color in UI
defaults.

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint.

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint.

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

Actually performs the painting operation.

Get a color property from the given JComponent.

Get any extra attributes which the painter implementation would like
to include in the image cache lookups.

Gets the PaintContext for this painting operation.

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

Methods declared in interface javax.swing.

Painter

paint

---

#### Methods declared in interface javax.swing. Painter

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractRegionPainter

```java
protected AbstractRegionPainter()
```

Create a new AbstractRegionPainter

============ METHOD DETAIL ==========

- Method Detail

- getExtendedCacheKeys

```java
protected
Object
[] getExtendedCacheKeys​(
JComponent
c)
```

Get any extra attributes which the painter implementation would like
to include in the image cache lookups. This is checked for every call
of the paint(g, c, w, h) method.

**Parameters:** c

- The component on the current paint call
**Returns:** Array of extra objects to be included in the cache key

- getPaintContext

```java
protected abstract
AbstractRegionPainter.PaintContext
getPaintContext()
```

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

**Returns:** a PaintContext associated with this paint operation.

- configureGraphics

```java
protected void configureGraphics​(
Graphics2D
g)
```

Configures the given Graphics2D. Often, rendering hints or compositing rules are
applied to a Graphics2D object prior to painting, which should affect all of the
subsequent painting operations. This method provides a convenient hook for configuring
the Graphics object prior to rendering, regardless of whether the render operation is
performed to an intermediate buffer or directly to the display.

**Parameters:** g

- The Graphics2D object to configure. Will not be null.

- doPaint

```java
protected abstract void doPaint​(
Graphics2D
g,

JComponent
c,
int width,
int height,

Object
[] extendedCacheKeys)
```

Actually performs the painting operation. Subclasses must implement this method.
The graphics object passed may represent the actual surface being rendered to,
or it may be an intermediate buffer. It has also been pre-translated. Simply render
the component as if it were located at 0, 0 and had a width of

width

and a height of

height

. For performance reasons, you may want to read
the clip from the Graphics2D object and only render within that space.

**Parameters:** g

- The Graphics2D surface to paint to
**Parameters:** c

- The JComponent related to the drawing event. For example, if the
region being rendered is Button, then

c

will be a
JButton. If the region being drawn is ScrollBarSlider, then the
component will be JScrollBar. This value may be null.
**Parameters:** width

- The width of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getWidth().
**Parameters:** height

- The height of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getHeight().
**Parameters:** extendedCacheKeys

- The result of the call to getExtendedCacheKeys()

- decodeX

```java
protected final float decodeX​(float x)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

**Parameters:** x

- an encoded x value (0...1, or 1...2, or 2...3)
**Returns:** the decoded x value
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

- decodeY

```java
protected final float decodeY​(float y)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

**Parameters:** y

- an encoded y value (0...1, or 1...2, or 2...3)
**Returns:** the decoded y value
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

- decodeAnchorX

```java
protected final float decodeAnchorX​(float x,
float dx)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** x

- an encoded x value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dx

- the offset distance to the anchor from the control point x
**Returns:** the decoded x location of the control point
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

- decodeAnchorY

```java
protected final float decodeAnchorY​(float y,
float dy)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** y

- an encoded y value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dy

- the offset distance to the anchor from the control point y
**Returns:** the decoded y position of the control point
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

- decodeColor

```java
protected final
Color
decodeColor​(
String
key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)
```

Decodes and returns a color, which is derived from a base color in UI
defaults.

**Parameters:** key

- A key corresponding to the value in the UI Defaults table
of UIManager where the base color is defined
**Parameters:** hOffset

- The hue offset used for derivation.
**Parameters:** sOffset

- The saturation offset used for derivation.
**Parameters:** bOffset

- The brightness offset used for derivation.
**Parameters:** aOffset

- The alpha offset used for derivation. Between 0...255
**Returns:** The derived color, whose color value will change if the parent
uiDefault color changes.

- decodeColor

```java
protected final
Color
decodeColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color

- decodeGradient

```java
protected final
LinearGradientPaint
decodeGradient​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint. One primary purpose for this
method is to avoid creating a LinearGradientPaint where the start and
end points are equal. In such a case, the end y point is slightly
increased to avoid the overlap.

**Parameters:** x1

- x1
**Parameters:** y1

- y1
**Parameters:** x2

- x2
**Parameters:** y2

- y2
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid LinearGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

- decodeRadialGradient

```java
protected final
RadialGradientPaint
decodeRadialGradient​(float x,
float y,
float r,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint. One primary purpose for this
method is to avoid creating a RadialGradientPaint where the radius
is non-positive. In such a case, the radius is just slightly
increased to avoid 0.

**Parameters:** x

- x-coordinate
**Parameters:** y

- y-coordinate
**Parameters:** r

- radius
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid RadialGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

r

is non-positive,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

- getComponentColor

```java
protected final
Color
getComponentColor​(
JComponent
c,

String
property,

Color
defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)
```

Get a color property from the given JComponent. First checks for a

getXXX()

method and if that fails checks for a client
property with key

property

. If that still fails to return
a Color then

defaultColor

is returned.

**Parameters:** c

- The component to get the color property from
**Parameters:** property

- The name of a bean style property or client property
**Parameters:** defaultColor

- The color to return if no color was obtained from
the component.
**Parameters:** saturationOffset

- additively modifies the HSB saturation component
of the color returned (ignored if default color is returned).
**Parameters:** brightnessOffset

- additively modifies the HSB brightness component
of the color returned (ignored if default color is returned).
**Parameters:** alphaOffset

- additively modifies the ARGB alpha component of the
color returned (ignored if default color is returned).
**Returns:** The color that was obtained from the component or defaultColor

Constructor Detail

- AbstractRegionPainter

```java
protected AbstractRegionPainter()
```

Create a new AbstractRegionPainter

---

#### Constructor Detail

AbstractRegionPainter

```java
protected AbstractRegionPainter()
```

Create a new AbstractRegionPainter

---

#### AbstractRegionPainter

protected AbstractRegionPainter()

Create a new AbstractRegionPainter

Method Detail

- getExtendedCacheKeys

```java
protected
Object
[] getExtendedCacheKeys​(
JComponent
c)
```

Get any extra attributes which the painter implementation would like
to include in the image cache lookups. This is checked for every call
of the paint(g, c, w, h) method.

**Parameters:** c

- The component on the current paint call
**Returns:** Array of extra objects to be included in the cache key

- getPaintContext

```java
protected abstract
AbstractRegionPainter.PaintContext
getPaintContext()
```

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

**Returns:** a PaintContext associated with this paint operation.

- configureGraphics

```java
protected void configureGraphics​(
Graphics2D
g)
```

Configures the given Graphics2D. Often, rendering hints or compositing rules are
applied to a Graphics2D object prior to painting, which should affect all of the
subsequent painting operations. This method provides a convenient hook for configuring
the Graphics object prior to rendering, regardless of whether the render operation is
performed to an intermediate buffer or directly to the display.

**Parameters:** g

- The Graphics2D object to configure. Will not be null.

- doPaint

```java
protected abstract void doPaint​(
Graphics2D
g,

JComponent
c,
int width,
int height,

Object
[] extendedCacheKeys)
```

Actually performs the painting operation. Subclasses must implement this method.
The graphics object passed may represent the actual surface being rendered to,
or it may be an intermediate buffer. It has also been pre-translated. Simply render
the component as if it were located at 0, 0 and had a width of

width

and a height of

height

. For performance reasons, you may want to read
the clip from the Graphics2D object and only render within that space.

**Parameters:** g

- The Graphics2D surface to paint to
**Parameters:** c

- The JComponent related to the drawing event. For example, if the
region being rendered is Button, then

c

will be a
JButton. If the region being drawn is ScrollBarSlider, then the
component will be JScrollBar. This value may be null.
**Parameters:** width

- The width of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getWidth().
**Parameters:** height

- The height of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getHeight().
**Parameters:** extendedCacheKeys

- The result of the call to getExtendedCacheKeys()

- decodeX

```java
protected final float decodeX​(float x)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

**Parameters:** x

- an encoded x value (0...1, or 1...2, or 2...3)
**Returns:** the decoded x value
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

- decodeY

```java
protected final float decodeY​(float y)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

**Parameters:** y

- an encoded y value (0...1, or 1...2, or 2...3)
**Returns:** the decoded y value
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

- decodeAnchorX

```java
protected final float decodeAnchorX​(float x,
float dx)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** x

- an encoded x value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dx

- the offset distance to the anchor from the control point x
**Returns:** the decoded x location of the control point
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

- decodeAnchorY

```java
protected final float decodeAnchorY​(float y,
float dy)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** y

- an encoded y value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dy

- the offset distance to the anchor from the control point y
**Returns:** the decoded y position of the control point
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

- decodeColor

```java
protected final
Color
decodeColor​(
String
key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)
```

Decodes and returns a color, which is derived from a base color in UI
defaults.

**Parameters:** key

- A key corresponding to the value in the UI Defaults table
of UIManager where the base color is defined
**Parameters:** hOffset

- The hue offset used for derivation.
**Parameters:** sOffset

- The saturation offset used for derivation.
**Parameters:** bOffset

- The brightness offset used for derivation.
**Parameters:** aOffset

- The alpha offset used for derivation. Between 0...255
**Returns:** The derived color, whose color value will change if the parent
uiDefault color changes.

- decodeColor

```java
protected final
Color
decodeColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color

- decodeGradient

```java
protected final
LinearGradientPaint
decodeGradient​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint. One primary purpose for this
method is to avoid creating a LinearGradientPaint where the start and
end points are equal. In such a case, the end y point is slightly
increased to avoid the overlap.

**Parameters:** x1

- x1
**Parameters:** y1

- y1
**Parameters:** x2

- x2
**Parameters:** y2

- y2
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid LinearGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

- decodeRadialGradient

```java
protected final
RadialGradientPaint
decodeRadialGradient​(float x,
float y,
float r,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint. One primary purpose for this
method is to avoid creating a RadialGradientPaint where the radius
is non-positive. In such a case, the radius is just slightly
increased to avoid 0.

**Parameters:** x

- x-coordinate
**Parameters:** y

- y-coordinate
**Parameters:** r

- radius
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid RadialGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

r

is non-positive,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

- getComponentColor

```java
protected final
Color
getComponentColor​(
JComponent
c,

String
property,

Color
defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)
```

Get a color property from the given JComponent. First checks for a

getXXX()

method and if that fails checks for a client
property with key

property

. If that still fails to return
a Color then

defaultColor

is returned.

**Parameters:** c

- The component to get the color property from
**Parameters:** property

- The name of a bean style property or client property
**Parameters:** defaultColor

- The color to return if no color was obtained from
the component.
**Parameters:** saturationOffset

- additively modifies the HSB saturation component
of the color returned (ignored if default color is returned).
**Parameters:** brightnessOffset

- additively modifies the HSB brightness component
of the color returned (ignored if default color is returned).
**Parameters:** alphaOffset

- additively modifies the ARGB alpha component of the
color returned (ignored if default color is returned).
**Returns:** The color that was obtained from the component or defaultColor

---

#### Method Detail

getExtendedCacheKeys

```java
protected
Object
[] getExtendedCacheKeys​(
JComponent
c)
```

Get any extra attributes which the painter implementation would like
to include in the image cache lookups. This is checked for every call
of the paint(g, c, w, h) method.

**Parameters:** c

- The component on the current paint call
**Returns:** Array of extra objects to be included in the cache key

---

#### getExtendedCacheKeys

protected

Object

[] getExtendedCacheKeys​(

JComponent

c)

Get any extra attributes which the painter implementation would like
to include in the image cache lookups. This is checked for every call
of the paint(g, c, w, h) method.

getPaintContext

```java
protected abstract
AbstractRegionPainter.PaintContext
getPaintContext()
```

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

**Returns:** a PaintContext associated with this paint operation.

---

#### getPaintContext

protected abstract

AbstractRegionPainter.PaintContext

getPaintContext()

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

Gets the PaintContext for this painting operation. This method is called on every
paint, and so should be fast and produce no garbage. The PaintContext contains
information such as cache hints. It also contains data necessary for decoding
points at runtime, such as the stretching insets, the canvas size at which the
encoded points were defined, and whether the stretching insets are inverted.

This method allows for subclasses to package the painting of different states
with possibly different canvas sizes, etc, into one AbstractRegionPainter implementation.

configureGraphics

```java
protected void configureGraphics​(
Graphics2D
g)
```

Configures the given Graphics2D. Often, rendering hints or compositing rules are
applied to a Graphics2D object prior to painting, which should affect all of the
subsequent painting operations. This method provides a convenient hook for configuring
the Graphics object prior to rendering, regardless of whether the render operation is
performed to an intermediate buffer or directly to the display.

**Parameters:** g

- The Graphics2D object to configure. Will not be null.

---

#### configureGraphics

protected void configureGraphics​(

Graphics2D

g)

Configures the given Graphics2D. Often, rendering hints or compositing rules are
applied to a Graphics2D object prior to painting, which should affect all of the
subsequent painting operations. This method provides a convenient hook for configuring
the Graphics object prior to rendering, regardless of whether the render operation is
performed to an intermediate buffer or directly to the display.

doPaint

```java
protected abstract void doPaint​(
Graphics2D
g,

JComponent
c,
int width,
int height,

Object
[] extendedCacheKeys)
```

Actually performs the painting operation. Subclasses must implement this method.
The graphics object passed may represent the actual surface being rendered to,
or it may be an intermediate buffer. It has also been pre-translated. Simply render
the component as if it were located at 0, 0 and had a width of

width

and a height of

height

. For performance reasons, you may want to read
the clip from the Graphics2D object and only render within that space.

**Parameters:** g

- The Graphics2D surface to paint to
**Parameters:** c

- The JComponent related to the drawing event. For example, if the
region being rendered is Button, then

c

will be a
JButton. If the region being drawn is ScrollBarSlider, then the
component will be JScrollBar. This value may be null.
**Parameters:** width

- The width of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getWidth().
**Parameters:** height

- The height of the region to paint. Note that in the case of
painting the foreground, this value may differ from c.getHeight().
**Parameters:** extendedCacheKeys

- The result of the call to getExtendedCacheKeys()

---

#### doPaint

protected abstract void doPaint​(

Graphics2D

g,

JComponent

c,
int width,
int height,

Object

[] extendedCacheKeys)

Actually performs the painting operation. Subclasses must implement this method.
The graphics object passed may represent the actual surface being rendered to,
or it may be an intermediate buffer. It has also been pre-translated. Simply render
the component as if it were located at 0, 0 and had a width of

width

and a height of

height

. For performance reasons, you may want to read
the clip from the Graphics2D object and only render within that space.

decodeX

```java
protected final float decodeX​(float x)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

**Parameters:** x

- an encoded x value (0...1, or 1...2, or 2...3)
**Returns:** the decoded x value
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

---

#### decodeX

protected final float decodeX​(float x)

Decodes and returns a float value representing the actual pixel location for
the given encoded X value.

decodeY

```java
protected final float decodeY​(float y)
```

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

**Parameters:** y

- an encoded y value (0...1, or 1...2, or 2...3)
**Returns:** the decoded y value
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

---

#### decodeY

protected final float decodeY​(float y)

Decodes and returns a float value representing the actual pixel location for
the given encoded y value.

decodeAnchorX

```java
protected final float decodeAnchorX​(float x,
float dx)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** x

- an encoded x value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dx

- the offset distance to the anchor from the control point x
**Returns:** the decoded x location of the control point
**Throws:** IllegalArgumentException

- if

x < 0

or

x > 3

---

#### decodeAnchorX

protected final float decodeAnchorX​(float x,
float dx)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded X value of the control point, and the offset
distance to the anchor from that control point.

decodeAnchorY

```java
protected final float decodeAnchorY​(float y,
float dy)
```

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

**Parameters:** y

- an encoded y value of the bezier control point (0...1, or 1...2, or 2...3)
**Parameters:** dy

- the offset distance to the anchor from the control point y
**Returns:** the decoded y position of the control point
**Throws:** IllegalArgumentException

- if

y < 0

or

y > 3

---

#### decodeAnchorY

protected final float decodeAnchorY​(float y,
float dy)

Decodes and returns a float value representing the actual pixel location for
the anchor point given the encoded Y value of the control point, and the offset
distance to the anchor from that control point.

decodeColor

```java
protected final
Color
decodeColor​(
String
key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)
```

Decodes and returns a color, which is derived from a base color in UI
defaults.

**Parameters:** key

- A key corresponding to the value in the UI Defaults table
of UIManager where the base color is defined
**Parameters:** hOffset

- The hue offset used for derivation.
**Parameters:** sOffset

- The saturation offset used for derivation.
**Parameters:** bOffset

- The brightness offset used for derivation.
**Parameters:** aOffset

- The alpha offset used for derivation. Between 0...255
**Returns:** The derived color, whose color value will change if the parent
uiDefault color changes.

---

#### decodeColor

protected final

Color

decodeColor​(

String

key,
float hOffset,
float sOffset,
float bOffset,
int aOffset)

Decodes and returns a color, which is derived from a base color in UI
defaults.

decodeColor

```java
protected final
Color
decodeColor​(
Color
color1,

Color
color2,
float midPoint)
```

Decodes and returns a color, which is derived from a offset between two
other colors.

**Parameters:** color1

- The first color
**Parameters:** color2

- The second color
**Parameters:** midPoint

- The offset between color 1 and color 2, a value of 0.0 is
color 1 and 1.0 is color 2;
**Returns:** The derived color

---

#### decodeColor

protected final

Color

decodeColor​(

Color

color1,

Color

color2,
float midPoint)

Decodes and returns a color, which is derived from a offset between two
other colors.

decodeGradient

```java
protected final
LinearGradientPaint
decodeGradient​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint. One primary purpose for this
method is to avoid creating a LinearGradientPaint where the start and
end points are equal. In such a case, the end y point is slightly
increased to avoid the overlap.

**Parameters:** x1

- x1
**Parameters:** y1

- y1
**Parameters:** x2

- x2
**Parameters:** y2

- y2
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid LinearGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null,
**Throws:** IllegalArgumentException

- if start and end points are the same points,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

---

#### decodeGradient

protected final

LinearGradientPaint

decodeGradient​(float x1,
float y1,
float x2,
float y2,
float[] midpoints,

Color

[] colors)

Given parameters for creating a LinearGradientPaint, this method will
create and return a linear gradient paint. One primary purpose for this
method is to avoid creating a LinearGradientPaint where the start and
end points are equal. In such a case, the end y point is slightly
increased to avoid the overlap.

decodeRadialGradient

```java
protected final
RadialGradientPaint
decodeRadialGradient​(float x,
float y,
float r,
float[] midpoints,

Color
[] colors)
```

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint. One primary purpose for this
method is to avoid creating a RadialGradientPaint where the radius
is non-positive. In such a case, the radius is just slightly
increased to avoid 0.

**Parameters:** x

- x-coordinate
**Parameters:** y

- y-coordinate
**Parameters:** r

- radius
**Parameters:** midpoints

- the midpoints
**Parameters:** colors

- the colors
**Returns:** a valid RadialGradientPaint. This method never returns null.
**Throws:** NullPointerException

- if

midpoints

array is null,
or

colors

array is null
**Throws:** IllegalArgumentException

- if

r

is non-positive,
or

midpoints.length != colors.length

,
or

colors

is less than 2 in size,
or a

midpoints

value is less than 0.0 or greater than 1.0,
or the

midpoints

are not provided in strictly increasing order

---

#### decodeRadialGradient

protected final

RadialGradientPaint

decodeRadialGradient​(float x,
float y,
float r,
float[] midpoints,

Color

[] colors)

Given parameters for creating a RadialGradientPaint, this method will
create and return a radial gradient paint. One primary purpose for this
method is to avoid creating a RadialGradientPaint where the radius
is non-positive. In such a case, the radius is just slightly
increased to avoid 0.

getComponentColor

```java
protected final
Color
getComponentColor​(
JComponent
c,

String
property,

Color
defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)
```

Get a color property from the given JComponent. First checks for a

getXXX()

method and if that fails checks for a client
property with key

property

. If that still fails to return
a Color then

defaultColor

is returned.

**Parameters:** c

- The component to get the color property from
**Parameters:** property

- The name of a bean style property or client property
**Parameters:** defaultColor

- The color to return if no color was obtained from
the component.
**Parameters:** saturationOffset

- additively modifies the HSB saturation component
of the color returned (ignored if default color is returned).
**Parameters:** brightnessOffset

- additively modifies the HSB brightness component
of the color returned (ignored if default color is returned).
**Parameters:** alphaOffset

- additively modifies the ARGB alpha component of the
color returned (ignored if default color is returned).
**Returns:** The color that was obtained from the component or defaultColor

---

#### getComponentColor

protected final

Color

getComponentColor​(

JComponent

c,

String

property,

Color

defaultColor,
float saturationOffset,
float brightnessOffset,
int alphaOffset)

Get a color property from the given JComponent. First checks for a

getXXX()

method and if that fails checks for a client
property with key

property

. If that still fails to return
a Color then

defaultColor

is returned.

---

