# Class LineBorder

**Source:** `java.desktop\javax\swing\border\LineBorder.html`

### Class Description

```java
public class
LineBorder

extends
AbstractBorder
```

A class which implements a line border of arbitrary thickness
and of a single color.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Implemented Interfaces:** Serializable

,

Border

---

### Field Details

#### protected int thickness

Thickness of the border.

---

#### protected
Color
lineColor

Color of the border.

---

#### protected boolean roundedCorners

Whether or not the border has rounded corners.

---

### Constructor Details

#### public LineBorder​(
Color
color)

Creates a line border with the specified color and a
thickness = 1.

**Parameters:**
- color

- the color for the border

---

#### public LineBorder​(
Color
color,
int thickness)

Creates a line border with the specified color and thickness.

**Parameters:**
- color

- the color of the border
- thickness

- the thickness of the border

---

#### @ConstructorProperties
({"lineColor","thickness","roundedCorners"})
public LineBorder​(
Color
color,
int thickness,
boolean roundedCorners)

Creates a line border with the specified color, thickness,
and corner shape.

**Parameters:**
- color

- the color of the border
- thickness

- the thickness of the border
- roundedCorners

- whether or not border corners should be round

**Since:**
- 1.3

---

### Method Details

#### public static
Border
createBlackLineBorder()

Convenience method for getting the Color.black LineBorder of thickness 1.

**Returns:**
- a

LineBorder

with

Color.black

and thickness of 1

---

#### public static
Border
createGrayLineBorder()

Convenience method for getting the Color.gray LineBorder of thickness 1.

**Returns:**
- a

LineBorder

with

Color.gray

and thickness of 1

---

#### public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

**Specified by:**
- paintBorder

in interface

Border

**Overrides:**
- paintBorder

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border is being painted
- g

- the paint graphics
- x

- the x position of the painted border
- y

- the y position of the painted border
- width

- the width of the painted border
- height

- the height of the painted border

---

#### public
Insets
getBorderInsets​(
Component
c,

Insets
insets)

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:**
- getBorderInsets

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border insets value applies
- insets

- the object to be reinitialized

**Returns:**
- the

insets

object

---

#### public
Color
getLineColor()

Returns the color of the border.

**Returns:**
- a

Color

object representing the color of this object

---

#### public int getThickness()

Returns the thickness of the border.

**Returns:**
- the thickness of this border

---

#### public boolean getRoundedCorners()

Returns whether this border will be drawn with rounded corners.

**Returns:**
- true

if this border should have rounded corners

**Since:**
- 1.3

---

#### public boolean isBorderOpaque()

Returns whether or not the border is opaque.

**Specified by:**
- isBorderOpaque

in interface

Border

**Overrides:**
- isBorderOpaque

in class

AbstractBorder

**Returns:**
- true

if the border is opaque,

false

otherwise

---

### Additional Sections

#### Class LineBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.LineBorder

javax.swing.border.AbstractBorder

- javax.swing.border.LineBorder

javax.swing.border.LineBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.LineBorderUIResource

```java
public class
LineBorder

extends
AbstractBorder
```

A class which implements a line border of arbitrary thickness
and of a single color.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**See Also:** Serialized Form

public class

LineBorder

extends

AbstractBorder

A class which implements a line border of arbitrary thickness
and of a single color.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Color

lineColor

Color of the border.

protected boolean

roundedCorners

Whether or not the border has rounded corners.

protected int

thickness

Thickness of the border.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LineBorder

​(

Color

color)

Creates a line border with the specified color and a
thickness = 1.

LineBorder

​(

Color

color,
int thickness)

Creates a line border with the specified color and thickness.

LineBorder

​(

Color

color,
int thickness,
boolean roundedCorners)

Creates a line border with the specified color, thickness,
and corner shape.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Border

createBlackLineBorder

()

Convenience method for getting the Color.black LineBorder of thickness 1.

static

Border

createGrayLineBorder

()

Convenience method for getting the Color.gray LineBorder of thickness 1.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Color

getLineColor

()

Returns the color of the border.

boolean

getRoundedCorners

()

Returns whether this border will be drawn with rounded corners.

int

getThickness

()

Returns the thickness of the border.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

protected

Color

lineColor

Color of the border.

protected boolean

roundedCorners

Whether or not the border has rounded corners.

protected int

thickness

Thickness of the border.

---

#### Field Summary

Color of the border.

Whether or not the border has rounded corners.

Thickness of the border.

Constructor Summary

Constructors

Constructor

Description

LineBorder

​(

Color

color)

Creates a line border with the specified color and a
thickness = 1.

LineBorder

​(

Color

color,
int thickness)

Creates a line border with the specified color and thickness.

LineBorder

​(

Color

color,
int thickness,
boolean roundedCorners)

Creates a line border with the specified color, thickness,
and corner shape.

---

#### Constructor Summary

Creates a line border with the specified color and a
thickness = 1.

Creates a line border with the specified color and thickness.

Creates a line border with the specified color, thickness,
and corner shape.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Border

createBlackLineBorder

()

Convenience method for getting the Color.black LineBorder of thickness 1.

static

Border

createGrayLineBorder

()

Convenience method for getting the Color.gray LineBorder of thickness 1.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Color

getLineColor

()

Returns the color of the border.

boolean

getRoundedCorners

()

Returns whether this border will be drawn with rounded corners.

int

getThickness

()

Returns the thickness of the border.

boolean

isBorderOpaque

()

Returns whether or not the border is opaque.

void

paintBorder

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

- Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

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

Convenience method for getting the Color.black LineBorder of thickness 1.

Convenience method for getting the Color.gray LineBorder of thickness 1.

Reinitialize the insets parameter with this Border's current Insets.

Returns the color of the border.

Returns whether this border will be drawn with rounded corners.

Returns the thickness of the border.

Returns whether or not the border is opaque.

Paints the border for the specified component with the
specified position and size.

Methods declared in class javax.swing.border.

AbstractBorder

getBaseline

,

getBaselineResizeBehavior

,

getBorderInsets

,

getInteriorRectangle

,

getInteriorRectangle

---

#### Methods declared in class javax.swing.border. AbstractBorder

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

- thickness

```java
protected int thickness
```

Thickness of the border.

- lineColor

```java
protected
Color
lineColor
```

Color of the border.

- roundedCorners

```java
protected boolean roundedCorners
```

Whether or not the border has rounded corners.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LineBorder

```java
public LineBorder​(
Color
color)
```

Creates a line border with the specified color and a
thickness = 1.

**Parameters:** color

- the color for the border

- LineBorder

```java
public LineBorder​(
Color
color,
int thickness)
```

Creates a line border with the specified color and thickness.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border

- LineBorder

```java
@ConstructorProperties
({"lineColor","thickness","roundedCorners"})
public LineBorder​(
Color
color,
int thickness,
boolean roundedCorners)
```

Creates a line border with the specified color, thickness,
and corner shape.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border
**Parameters:** roundedCorners

- whether or not border corners should be round
**Since:** 1.3

============ METHOD DETAIL ==========

- Method Detail

- createBlackLineBorder

```java
public static
Border
createBlackLineBorder()
```

Convenience method for getting the Color.black LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.black

and thickness of 1

- createGrayLineBorder

```java
public static
Border
createGrayLineBorder()
```

Convenience method for getting the Color.gray LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.gray

and thickness of 1

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- getLineColor

```java
public
Color
getLineColor()
```

Returns the color of the border.

**Returns:** a

Color

object representing the color of this object

- getThickness

```java
public int getThickness()
```

Returns the thickness of the border.

**Returns:** the thickness of this border

- getRoundedCorners

```java
public boolean getRoundedCorners()
```

Returns whether this border will be drawn with rounded corners.

**Returns:** true

if this border should have rounded corners
**Since:** 1.3

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the border is opaque,

false

otherwise

Field Detail

- thickness

```java
protected int thickness
```

Thickness of the border.

- lineColor

```java
protected
Color
lineColor
```

Color of the border.

- roundedCorners

```java
protected boolean roundedCorners
```

Whether or not the border has rounded corners.

---

#### Field Detail

thickness

```java
protected int thickness
```

Thickness of the border.

---

#### thickness

protected int thickness

Thickness of the border.

lineColor

```java
protected
Color
lineColor
```

Color of the border.

---

#### lineColor

protected

Color

lineColor

Color of the border.

roundedCorners

```java
protected boolean roundedCorners
```

Whether or not the border has rounded corners.

---

#### roundedCorners

protected boolean roundedCorners

Whether or not the border has rounded corners.

Constructor Detail

- LineBorder

```java
public LineBorder​(
Color
color)
```

Creates a line border with the specified color and a
thickness = 1.

**Parameters:** color

- the color for the border

- LineBorder

```java
public LineBorder​(
Color
color,
int thickness)
```

Creates a line border with the specified color and thickness.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border

- LineBorder

```java
@ConstructorProperties
({"lineColor","thickness","roundedCorners"})
public LineBorder​(
Color
color,
int thickness,
boolean roundedCorners)
```

Creates a line border with the specified color, thickness,
and corner shape.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border
**Parameters:** roundedCorners

- whether or not border corners should be round
**Since:** 1.3

---

#### Constructor Detail

LineBorder

```java
public LineBorder​(
Color
color)
```

Creates a line border with the specified color and a
thickness = 1.

**Parameters:** color

- the color for the border

---

#### LineBorder

public LineBorder​(

Color

color)

Creates a line border with the specified color and a
thickness = 1.

LineBorder

```java
public LineBorder​(
Color
color,
int thickness)
```

Creates a line border with the specified color and thickness.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border

---

#### LineBorder

public LineBorder​(

Color

color,
int thickness)

Creates a line border with the specified color and thickness.

LineBorder

```java
@ConstructorProperties
({"lineColor","thickness","roundedCorners"})
public LineBorder​(
Color
color,
int thickness,
boolean roundedCorners)
```

Creates a line border with the specified color, thickness,
and corner shape.

**Parameters:** color

- the color of the border
**Parameters:** thickness

- the thickness of the border
**Parameters:** roundedCorners

- whether or not border corners should be round
**Since:** 1.3

---

#### LineBorder

@ConstructorProperties

({"lineColor","thickness","roundedCorners"})
public LineBorder​(

Color

color,
int thickness,
boolean roundedCorners)

Creates a line border with the specified color, thickness,
and corner shape.

Method Detail

- createBlackLineBorder

```java
public static
Border
createBlackLineBorder()
```

Convenience method for getting the Color.black LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.black

and thickness of 1

- createGrayLineBorder

```java
public static
Border
createGrayLineBorder()
```

Convenience method for getting the Color.gray LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.gray

and thickness of 1

- paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

- getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

- getLineColor

```java
public
Color
getLineColor()
```

Returns the color of the border.

**Returns:** a

Color

object representing the color of this object

- getThickness

```java
public int getThickness()
```

Returns the thickness of the border.

**Returns:** the thickness of this border

- getRoundedCorners

```java
public boolean getRoundedCorners()
```

Returns whether this border will be drawn with rounded corners.

**Returns:** true

if this border should have rounded corners
**Since:** 1.3

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the border is opaque,

false

otherwise

---

#### Method Detail

createBlackLineBorder

```java
public static
Border
createBlackLineBorder()
```

Convenience method for getting the Color.black LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.black

and thickness of 1

---

#### createBlackLineBorder

public static

Border

createBlackLineBorder()

Convenience method for getting the Color.black LineBorder of thickness 1.

createGrayLineBorder

```java
public static
Border
createGrayLineBorder()
```

Convenience method for getting the Color.gray LineBorder of thickness 1.

**Returns:** a

LineBorder

with

Color.gray

and thickness of 1

---

#### createGrayLineBorder

public static

Border

createGrayLineBorder()

Convenience method for getting the Color.gray LineBorder of thickness 1.

paintBorder

```java
public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the border for the specified component with the
specified position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

AbstractBorder
**Parameters:** c

- the component for which this border is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the painted border
**Parameters:** y

- the y position of the painted border
**Parameters:** width

- the width of the painted border
**Parameters:** height

- the height of the painted border

---

#### paintBorder

public void paintBorder​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the border for the specified component with the
specified position and size.

getBorderInsets

```java
public
Insets
getBorderInsets​(
Component
c,

Insets
insets)
```

Reinitialize the insets parameter with this Border's current Insets.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the object to be reinitialized
**Returns:** the

insets

object

---

#### getBorderInsets

public

Insets

getBorderInsets​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

getLineColor

```java
public
Color
getLineColor()
```

Returns the color of the border.

**Returns:** a

Color

object representing the color of this object

---

#### getLineColor

public

Color

getLineColor()

Returns the color of the border.

getThickness

```java
public int getThickness()
```

Returns the thickness of the border.

**Returns:** the thickness of this border

---

#### getThickness

public int getThickness()

Returns the thickness of the border.

getRoundedCorners

```java
public boolean getRoundedCorners()
```

Returns whether this border will be drawn with rounded corners.

**Returns:** true

if this border should have rounded corners
**Since:** 1.3

---

#### getRoundedCorners

public boolean getRoundedCorners()

Returns whether this border will be drawn with rounded corners.

isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

if the border is opaque,

false

otherwise

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque.

---

