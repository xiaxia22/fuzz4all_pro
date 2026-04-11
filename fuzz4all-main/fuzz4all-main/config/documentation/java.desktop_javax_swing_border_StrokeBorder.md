# Class StrokeBorder

**Source:** `java.desktop\javax\swing\border\StrokeBorder.html`

### Class Description

```java
public class
StrokeBorder

extends
AbstractBorder
```

A class which implements a border of an arbitrary stroke.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI
between applications running the same version of Swing.
As of 1.4, support for long term storage of all JavaBeans™
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

*No entries found.*

### Constructor Details

#### public StrokeBorder​(
BasicStroke
stroke)

Creates a border of the specified

stroke

.
The component's foreground color will be used to render the border.

**Parameters:**
- stroke

- the

BasicStroke

object used to stroke a shape

**Throws:**
- NullPointerException

- if the specified

stroke

is

null

---

#### @ConstructorProperties
({"stroke","paint"})
public StrokeBorder​(
BasicStroke
stroke,

Paint
paint)

Creates a border of the specified

stroke

and

paint

.
If the specified

paint

is

null

,
the component's foreground color will be used to render the border.

**Parameters:**
- stroke

- the

BasicStroke

object used to stroke a shape
- paint

- the

Paint

object used to generate a color

**Throws:**
- NullPointerException

- if the specified

stroke

is

null

---

### Method Details

#### public void paintBorder​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the border for the specified component
with the specified position and size.
If the border was not specified with a

Paint

object,
the component's foreground color will be used to render the border.
If the component's foreground color is not available,
the default color of the

Graphics

object will be used.

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

**Throws:**
- NullPointerException

- if the specified

g

is

null

---

#### public
Insets
getBorderInsets​(
Component
c,

Insets
insets)

Reinitializes the

insets

parameter
with this border's current insets.
Every inset is the smallest (closest to negative infinity) integer value
that is greater than or equal to the line width of the stroke
that is used to paint the border.

**Overrides:**
- getBorderInsets

in class

AbstractBorder

**Parameters:**
- c

- the component for which this border insets value applies
- insets

- the

Insets

object to be reinitialized

**Returns:**
- the reinitialized

insets

parameter

**Throws:**
- NullPointerException

- if the specified

insets

is

null

**See Also:**
- Math.ceil(double)

---

#### public
BasicStroke
getStroke()

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

**Returns:**
- the

BasicStroke

object

---

#### public
Paint
getPaint()

Returns the

Paint

object used to generate a color
during the border rendering.

**Returns:**
- the

Paint

object or

null

if the

paint

parameter is not set

---

### Additional Sections

#### Class StrokeBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.StrokeBorder

javax.swing.border.AbstractBorder

- javax.swing.border.StrokeBorder

javax.swing.border.StrokeBorder

**All Implemented Interfaces:** Serializable

,

Border

```java
public class
StrokeBorder

extends
AbstractBorder
```

A class which implements a border of an arbitrary stroke.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI
between applications running the same version of Swing.
As of 1.4, support for long term storage of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**Since:** 1.7
**See Also:** Serialized Form

public class

StrokeBorder

extends

AbstractBorder

A class which implements a border of an arbitrary stroke.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI
between applications running the same version of Swing.
As of 1.4, support for long term storage of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI
between applications running the same version of Swing.
As of 1.4, support for long term storage of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StrokeBorder

​(

BasicStroke

stroke)

Creates a border of the specified

stroke

.

StrokeBorder

​(

BasicStroke

stroke,

Paint

paint)

Creates a border of the specified

stroke

and

paint

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitializes the

insets

parameter
with this border's current insets.

Paint

getPaint

()

Returns the

Paint

object used to generate a color
during the border rendering.

BasicStroke

getStroke

()

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

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

Paints the border for the specified component
with the specified position and size.

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

,

isBorderOpaque

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

Constructor Summary

Constructors

Constructor

Description

StrokeBorder

​(

BasicStroke

stroke)

Creates a border of the specified

stroke

.

StrokeBorder

​(

BasicStroke

stroke,

Paint

paint)

Creates a border of the specified

stroke

and

paint

.

---

#### Constructor Summary

Creates a border of the specified

stroke

.

Creates a border of the specified

stroke

and

paint

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitializes the

insets

parameter
with this border's current insets.

Paint

getPaint

()

Returns the

Paint

object used to generate a color
during the border rendering.

BasicStroke

getStroke

()

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

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

Paints the border for the specified component
with the specified position and size.

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

,

isBorderOpaque

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

Reinitializes the

insets

parameter
with this border's current insets.

Returns the

Paint

object used to generate a color
during the border rendering.

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

Paints the border for the specified component
with the specified position and size.

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

,

isBorderOpaque

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StrokeBorder

```java
public StrokeBorder​(
BasicStroke
stroke)
```

Creates a border of the specified

stroke

.
The component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Throws:** NullPointerException

- if the specified

stroke

is

null

- StrokeBorder

```java
@ConstructorProperties
({"stroke","paint"})
public StrokeBorder​(
BasicStroke
stroke,

Paint
paint)
```

Creates a border of the specified

stroke

and

paint

.
If the specified

paint

is

null

,
the component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Parameters:** paint

- the

Paint

object used to generate a color
**Throws:** NullPointerException

- if the specified

stroke

is

null

============ METHOD DETAIL ==========

- Method Detail

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

Paints the border for the specified component
with the specified position and size.
If the border was not specified with a

Paint

object,
the component's foreground color will be used to render the border.
If the component's foreground color is not available,
the default color of the

Graphics

object will be used.

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
**Throws:** NullPointerException

- if the specified

g

is

null

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

Reinitializes the

insets

parameter
with this border's current insets.
Every inset is the smallest (closest to negative infinity) integer value
that is greater than or equal to the line width of the stroke
that is used to paint the border.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the

Insets

object to be reinitialized
**Returns:** the reinitialized

insets

parameter
**Throws:** NullPointerException

- if the specified

insets

is

null
**See Also:** Math.ceil(double)

- getStroke

```java
public
BasicStroke
getStroke()
```

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

**Returns:** the

BasicStroke

object

- getPaint

```java
public
Paint
getPaint()
```

Returns the

Paint

object used to generate a color
during the border rendering.

**Returns:** the

Paint

object or

null

if the

paint

parameter is not set

Constructor Detail

- StrokeBorder

```java
public StrokeBorder​(
BasicStroke
stroke)
```

Creates a border of the specified

stroke

.
The component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Throws:** NullPointerException

- if the specified

stroke

is

null

- StrokeBorder

```java
@ConstructorProperties
({"stroke","paint"})
public StrokeBorder​(
BasicStroke
stroke,

Paint
paint)
```

Creates a border of the specified

stroke

and

paint

.
If the specified

paint

is

null

,
the component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Parameters:** paint

- the

Paint

object used to generate a color
**Throws:** NullPointerException

- if the specified

stroke

is

null

---

#### Constructor Detail

StrokeBorder

```java
public StrokeBorder​(
BasicStroke
stroke)
```

Creates a border of the specified

stroke

.
The component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Throws:** NullPointerException

- if the specified

stroke

is

null

---

#### StrokeBorder

public StrokeBorder​(

BasicStroke

stroke)

Creates a border of the specified

stroke

.
The component's foreground color will be used to render the border.

StrokeBorder

```java
@ConstructorProperties
({"stroke","paint"})
public StrokeBorder​(
BasicStroke
stroke,

Paint
paint)
```

Creates a border of the specified

stroke

and

paint

.
If the specified

paint

is

null

,
the component's foreground color will be used to render the border.

**Parameters:** stroke

- the

BasicStroke

object used to stroke a shape
**Parameters:** paint

- the

Paint

object used to generate a color
**Throws:** NullPointerException

- if the specified

stroke

is

null

---

#### StrokeBorder

@ConstructorProperties

({"stroke","paint"})
public StrokeBorder​(

BasicStroke

stroke,

Paint

paint)

Creates a border of the specified

stroke

and

paint

.
If the specified

paint

is

null

,
the component's foreground color will be used to render the border.

Method Detail

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

Paints the border for the specified component
with the specified position and size.
If the border was not specified with a

Paint

object,
the component's foreground color will be used to render the border.
If the component's foreground color is not available,
the default color of the

Graphics

object will be used.

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
**Throws:** NullPointerException

- if the specified

g

is

null

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

Reinitializes the

insets

parameter
with this border's current insets.
Every inset is the smallest (closest to negative infinity) integer value
that is greater than or equal to the line width of the stroke
that is used to paint the border.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the

Insets

object to be reinitialized
**Returns:** the reinitialized

insets

parameter
**Throws:** NullPointerException

- if the specified

insets

is

null
**See Also:** Math.ceil(double)

- getStroke

```java
public
BasicStroke
getStroke()
```

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

**Returns:** the

BasicStroke

object

- getPaint

```java
public
Paint
getPaint()
```

Returns the

Paint

object used to generate a color
during the border rendering.

**Returns:** the

Paint

object or

null

if the

paint

parameter is not set

---

#### Method Detail

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

Paints the border for the specified component
with the specified position and size.
If the border was not specified with a

Paint

object,
the component's foreground color will be used to render the border.
If the component's foreground color is not available,
the default color of the

Graphics

object will be used.

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
**Throws:** NullPointerException

- if the specified

g

is

null

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

Paints the border for the specified component
with the specified position and size.
If the border was not specified with a

Paint

object,
the component's foreground color will be used to render the border.
If the component's foreground color is not available,
the default color of the

Graphics

object will be used.

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

Reinitializes the

insets

parameter
with this border's current insets.
Every inset is the smallest (closest to negative infinity) integer value
that is greater than or equal to the line width of the stroke
that is used to paint the border.

**Overrides:** getBorderInsets

in class

AbstractBorder
**Parameters:** c

- the component for which this border insets value applies
**Parameters:** insets

- the

Insets

object to be reinitialized
**Returns:** the reinitialized

insets

parameter
**Throws:** NullPointerException

- if the specified

insets

is

null
**See Also:** Math.ceil(double)

---

#### getBorderInsets

public

Insets

getBorderInsets​(

Component

c,

Insets

insets)

Reinitializes the

insets

parameter
with this border's current insets.
Every inset is the smallest (closest to negative infinity) integer value
that is greater than or equal to the line width of the stroke
that is used to paint the border.

getStroke

```java
public
BasicStroke
getStroke()
```

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

**Returns:** the

BasicStroke

object

---

#### getStroke

public

BasicStroke

getStroke()

Returns the

BasicStroke

object used to stroke a shape
during the border rendering.

getPaint

```java
public
Paint
getPaint()
```

Returns the

Paint

object used to generate a color
during the border rendering.

**Returns:** the

Paint

object or

null

if the

paint

parameter is not set

---

#### getPaint

public

Paint

getPaint()

Returns the

Paint

object used to generate a color
during the border rendering.

---

