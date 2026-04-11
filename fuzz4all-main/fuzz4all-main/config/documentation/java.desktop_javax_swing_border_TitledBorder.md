# Class TitledBorder

**Source:** `java.desktop\javax\swing\border\TitledBorder.html`

### Class Description

```java
public class
TitledBorder

extends
AbstractBorder
```

A class which implements an arbitrary border
with the addition of a String title in a
specified position and justification.

If the border, font, or color property values are not
specified in the constructor or by invoking the appropriate
set methods, the property values will be defined by the current
look and feel, using the following property names in the
Defaults Table:

- "TitledBorder.border"

"TitledBorder.font"

"TitledBorder.titleColor"

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

#### protected
String
title

The title the border should display.

---

#### protected
Border
border

The border.

---

#### protected int titlePosition

The position for the title.

---

#### protected int titleJustification

The justification for the title.

---

#### protected
Font
titleFont

The font for rendering the title.

---

#### protected
Color
titleColor

The color of the title.

---

#### public static final int DEFAULT_POSITION

Use the default vertical orientation for the title text.

**See Also:**
- Constant Field Values

---

#### public static final int ABOVE_TOP

Position the title above the border's top line.

**See Also:**
- Constant Field Values

---

#### public static final int TOP

Position the title in the middle of the border's top line.

**See Also:**
- Constant Field Values

---

#### public static final int BELOW_TOP

Position the title below the border's top line.

**See Also:**
- Constant Field Values

---

#### public static final int ABOVE_BOTTOM

Position the title above the border's bottom line.

**See Also:**
- Constant Field Values

---

#### public static final int BOTTOM

Position the title in the middle of the border's bottom line.

**See Also:**
- Constant Field Values

---

#### public static final int BELOW_BOTTOM

Position the title below the border's bottom line.

**See Also:**
- Constant Field Values

---

#### public static final int DEFAULT_JUSTIFICATION

Use the default justification for the title text.

**See Also:**
- Constant Field Values

---

#### public static final int LEFT

Position title text at the left side of the border line.

**See Also:**
- Constant Field Values

---

#### public static final int CENTER

Position title text in the center of the border line.

**See Also:**
- Constant Field Values

---

#### public static final int RIGHT

Position title text at the right side of the border line.

**See Also:**
- Constant Field Values

---

#### public static final int LEADING

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

**See Also:**
- Constant Field Values

---

#### public static final int TRAILING

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

**See Also:**
- Constant Field Values

---

#### protected static final int EDGE_SPACING

Space between the border and the component's edge

**See Also:**
- Constant Field Values

---

#### protected static final int TEXT_SPACING

Space between the border and text

**See Also:**
- Constant Field Values

---

#### protected static final int TEXT_INSET_H

Horizontal inset of text that is left or right justified

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public TitledBorder​(
String
title)

Creates a TitledBorder instance.

**Parameters:**
- title

- the title the border should display

---

#### public TitledBorder​(
Border
border)

Creates a TitledBorder instance with the specified border
and an empty title.

**Parameters:**
- border

- the border

---

#### public TitledBorder​(
Border
border,

String
title)

Creates a TitledBorder instance with the specified border
and title.

**Parameters:**
- border

- the border
- title

- the title the border should display

---

#### public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition)

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

**Parameters:**
- border

- the border
- title

- the title the border should display
- titleJustification

- the justification for the title
- titlePosition

- the position for the title

---

#### public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

**Parameters:**
- border

- the border
- title

- the title the border should display
- titleJustification

- the justification for the title
- titlePosition

- the position for the title
- titleFont

- the font for rendering the title

---

#### @ConstructorProperties
({"border","title","titleJustification","titlePosition","titleFont","titleColor"})
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont,

Color
titleColor)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

**Parameters:**
- border

- the border
- title

- the title the border should display
- titleJustification

- the justification for the title
- titlePosition

- the position for the title
- titleFont

- the font of the title
- titleColor

- the color of the title

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
- false

---

#### public
String
getTitle()

Returns the title of the titled border.

**Returns:**
- the title of the titled border

---

#### public
Border
getBorder()

Returns the border of the titled border.

**Returns:**
- the border of the titled border

---

#### public int getTitlePosition()

Returns the title-position of the titled border.

**Returns:**
- the title-position of the titled border

---

#### public int getTitleJustification()

Returns the title-justification of the titled border.

**Returns:**
- the title-justification of the titled border

---

#### public
Font
getTitleFont()

Returns the title-font of the titled border.

**Returns:**
- the title-font of the titled border

---

#### public
Color
getTitleColor()

Returns the title-color of the titled border.

**Returns:**
- the title-color of the titled border

---

#### public void setTitle​(
String
title)

Sets the title of the titled border.

**Parameters:**
- title

- the title for the border

---

#### public void setBorder​(
Border
border)

Sets the border of the titled border.

**Parameters:**
- border

- the border

---

#### public void setTitlePosition​(int titlePosition)

Sets the title-position of the titled border.

**Parameters:**
- titlePosition

- the position for the border

---

#### public void setTitleJustification​(int titleJustification)

Sets the title-justification of the titled border.

**Parameters:**
- titleJustification

- the justification for the border

---

#### public void setTitleFont​(
Font
titleFont)

Sets the title-font of the titled border.

**Parameters:**
- titleFont

- the font for the border title

---

#### public void setTitleColor​(
Color
titleColor)

Sets the title-color of the titled border.

**Parameters:**
- titleColor

- the color for the border title

---

#### public
Dimension
getMinimumSize​(
Component
c)

Returns the minimum dimensions this border requires
in order to fully display the border and title.

**Parameters:**
- c

- the component where this border will be drawn

**Returns:**
- the

Dimension

object

---

#### public int getBaseline​(
Component
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

AbstractBorder

**Parameters:**
- c

-

Component

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- the baseline or < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException
- IllegalArgumentException

- if width or height is < 0

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)

Returns an enum indicating how the baseline of the border
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

AbstractBorder

**Parameters:**
- c

-

Component

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the border is
resized

**Throws:**
- NullPointerException

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### protected
Font
getFont​(
Component
c)

Returns default font of the titled border.

**Parameters:**
- c

- the component

**Returns:**
- default font of the titled border

---

### Additional Sections

#### Class TitledBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.TitledBorder

javax.swing.border.AbstractBorder

- javax.swing.border.TitledBorder

javax.swing.border.TitledBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.TitledBorderUIResource

```java
public class
TitledBorder

extends
AbstractBorder
```

A class which implements an arbitrary border
with the addition of a String title in a
specified position and justification.

If the border, font, or color property values are not
specified in the constructor or by invoking the appropriate
set methods, the property values will be defined by the current
look and feel, using the following property names in the
Defaults Table:

- "TitledBorder.border"

"TitledBorder.font"

"TitledBorder.titleColor"

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

TitledBorder

extends

AbstractBorder

A class which implements an arbitrary border
with the addition of a String title in a
specified position and justification.

If the border, font, or color property values are not
specified in the constructor or by invoking the appropriate
set methods, the property values will be defined by the current
look and feel, using the following property names in the
Defaults Table:

- "TitledBorder.border"

"TitledBorder.font"

"TitledBorder.titleColor"

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

If the border, font, or color property values are not
specified in the constructor or by invoking the appropriate
set methods, the property values will be defined by the current
look and feel, using the following property names in the
Defaults Table:

- "TitledBorder.border"

"TitledBorder.font"

"TitledBorder.titleColor"

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

"TitledBorder.border"

"TitledBorder.font"

"TitledBorder.titleColor"

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

static int

ABOVE_BOTTOM

Position the title above the border's bottom line.

static int

ABOVE_TOP

Position the title above the border's top line.

static int

BELOW_BOTTOM

Position the title below the border's bottom line.

static int

BELOW_TOP

Position the title below the border's top line.

protected

Border

border

The border.

static int

BOTTOM

Position the title in the middle of the border's bottom line.

static int

CENTER

Position title text in the center of the border line.

static int

DEFAULT_JUSTIFICATION

Use the default justification for the title text.

static int

DEFAULT_POSITION

Use the default vertical orientation for the title text.

protected static int

EDGE_SPACING

Space between the border and the component's edge

static int

LEADING

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

static int

LEFT

Position title text at the left side of the border line.

static int

RIGHT

Position title text at the right side of the border line.

protected static int

TEXT_INSET_H

Horizontal inset of text that is left or right justified

protected static int

TEXT_SPACING

Space between the border and text

protected

String

title

The title the border should display.

protected

Color

titleColor

The color of the title.

protected

Font

titleFont

The font for rendering the title.

protected int

titleJustification

The justification for the title.

protected int

titlePosition

The position for the title.

static int

TOP

Position the title in the middle of the border's top line.

static int

TRAILING

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TitledBorder

​(

String

title)

Creates a TitledBorder instance.

TitledBorder

​(

Border

border)

Creates a TitledBorder instance with the specified border
and an empty title.

TitledBorder

​(

Border

border,

String

title)

Creates a TitledBorder instance with the specified border
and title.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition)

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont,

Color

titleColor)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBaseline

​(

Component

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

Component

c)

Returns an enum indicating how the baseline of the border
changes as the size changes.

Border

getBorder

()

Returns the border of the titled border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

protected

Font

getFont

​(

Component

c)

Returns default font of the titled border.

Dimension

getMinimumSize

​(

Component

c)

Returns the minimum dimensions this border requires
in order to fully display the border and title.

String

getTitle

()

Returns the title of the titled border.

Color

getTitleColor

()

Returns the title-color of the titled border.

Font

getTitleFont

()

Returns the title-font of the titled border.

int

getTitleJustification

()

Returns the title-justification of the titled border.

int

getTitlePosition

()

Returns the title-position of the titled border.

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

void

setBorder

​(

Border

border)

Sets the border of the titled border.

void

setTitle

​(

String

title)

Sets the title of the titled border.

void

setTitleColor

​(

Color

titleColor)

Sets the title-color of the titled border.

void

setTitleFont

​(

Font

titleFont)

Sets the title-font of the titled border.

void

setTitleJustification

​(int titleJustification)

Sets the title-justification of the titled border.

void

setTitlePosition

​(int titlePosition)

Sets the title-position of the titled border.

- Methods declared in class javax.swing.border.

AbstractBorder

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

static int

ABOVE_BOTTOM

Position the title above the border's bottom line.

static int

ABOVE_TOP

Position the title above the border's top line.

static int

BELOW_BOTTOM

Position the title below the border's bottom line.

static int

BELOW_TOP

Position the title below the border's top line.

protected

Border

border

The border.

static int

BOTTOM

Position the title in the middle of the border's bottom line.

static int

CENTER

Position title text in the center of the border line.

static int

DEFAULT_JUSTIFICATION

Use the default justification for the title text.

static int

DEFAULT_POSITION

Use the default vertical orientation for the title text.

protected static int

EDGE_SPACING

Space between the border and the component's edge

static int

LEADING

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

static int

LEFT

Position title text at the left side of the border line.

static int

RIGHT

Position title text at the right side of the border line.

protected static int

TEXT_INSET_H

Horizontal inset of text that is left or right justified

protected static int

TEXT_SPACING

Space between the border and text

protected

String

title

The title the border should display.

protected

Color

titleColor

The color of the title.

protected

Font

titleFont

The font for rendering the title.

protected int

titleJustification

The justification for the title.

protected int

titlePosition

The position for the title.

static int

TOP

Position the title in the middle of the border's top line.

static int

TRAILING

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

---

#### Field Summary

Position the title above the border's bottom line.

Position the title above the border's top line.

Position the title below the border's bottom line.

Position the title below the border's top line.

The border.

Position the title in the middle of the border's bottom line.

Position title text in the center of the border line.

Use the default justification for the title text.

Use the default vertical orientation for the title text.

Space between the border and the component's edge

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

Position title text at the left side of the border line.

Position title text at the right side of the border line.

Horizontal inset of text that is left or right justified

Space between the border and text

The title the border should display.

The color of the title.

The font for rendering the title.

The justification for the title.

The position for the title.

Position the title in the middle of the border's top line.

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

Constructor Summary

Constructors

Constructor

Description

TitledBorder

​(

String

title)

Creates a TitledBorder instance.

TitledBorder

​(

Border

border)

Creates a TitledBorder instance with the specified border
and an empty title.

TitledBorder

​(

Border

border,

String

title)

Creates a TitledBorder instance with the specified border
and title.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition)

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

TitledBorder

​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont,

Color

titleColor)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

---

#### Constructor Summary

Creates a TitledBorder instance.

Creates a TitledBorder instance with the specified border
and an empty title.

Creates a TitledBorder instance with the specified border
and title.

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBaseline

​(

Component

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

Component

c)

Returns an enum indicating how the baseline of the border
changes as the size changes.

Border

getBorder

()

Returns the border of the titled border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

protected

Font

getFont

​(

Component

c)

Returns default font of the titled border.

Dimension

getMinimumSize

​(

Component

c)

Returns the minimum dimensions this border requires
in order to fully display the border and title.

String

getTitle

()

Returns the title of the titled border.

Color

getTitleColor

()

Returns the title-color of the titled border.

Font

getTitleFont

()

Returns the title-font of the titled border.

int

getTitleJustification

()

Returns the title-justification of the titled border.

int

getTitlePosition

()

Returns the title-position of the titled border.

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

void

setBorder

​(

Border

border)

Sets the border of the titled border.

void

setTitle

​(

String

title)

Sets the title of the titled border.

void

setTitleColor

​(

Color

titleColor)

Sets the title-color of the titled border.

void

setTitleFont

​(

Font

titleFont)

Sets the title-font of the titled border.

void

setTitleJustification

​(int titleJustification)

Sets the title-justification of the titled border.

void

setTitlePosition

​(int titlePosition)

Sets the title-position of the titled border.

- Methods declared in class javax.swing.border.

AbstractBorder

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

Returns the baseline.

Returns an enum indicating how the baseline of the border
changes as the size changes.

Returns the border of the titled border.

Reinitialize the insets parameter with this Border's current Insets.

Returns default font of the titled border.

Returns the minimum dimensions this border requires
in order to fully display the border and title.

Returns the title of the titled border.

Returns the title-color of the titled border.

Returns the title-font of the titled border.

Returns the title-justification of the titled border.

Returns the title-position of the titled border.

Returns whether or not the border is opaque.

Paints the border for the specified component with the
specified position and size.

Sets the border of the titled border.

Sets the title of the titled border.

Sets the title-color of the titled border.

Sets the title-font of the titled border.

Sets the title-justification of the titled border.

Sets the title-position of the titled border.

Methods declared in class javax.swing.border.

AbstractBorder

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

- title

```java
protected
String
title
```

The title the border should display.

- border

```java
protected
Border
border
```

The border.

- titlePosition

```java
protected int titlePosition
```

The position for the title.

- titleJustification

```java
protected int titleJustification
```

The justification for the title.

- titleFont

```java
protected
Font
titleFont
```

The font for rendering the title.

- titleColor

```java
protected
Color
titleColor
```

The color of the title.

- DEFAULT_POSITION

```java
public static final int DEFAULT_POSITION
```

Use the default vertical orientation for the title text.

**See Also:** Constant Field Values

- ABOVE_TOP

```java
public static final int ABOVE_TOP
```

Position the title above the border's top line.

**See Also:** Constant Field Values

- TOP

```java
public static final int TOP
```

Position the title in the middle of the border's top line.

**See Also:** Constant Field Values

- BELOW_TOP

```java
public static final int BELOW_TOP
```

Position the title below the border's top line.

**See Also:** Constant Field Values

- ABOVE_BOTTOM

```java
public static final int ABOVE_BOTTOM
```

Position the title above the border's bottom line.

**See Also:** Constant Field Values

- BOTTOM

```java
public static final int BOTTOM
```

Position the title in the middle of the border's bottom line.

**See Also:** Constant Field Values

- BELOW_BOTTOM

```java
public static final int BELOW_BOTTOM
```

Position the title below the border's bottom line.

**See Also:** Constant Field Values

- DEFAULT_JUSTIFICATION

```java
public static final int DEFAULT_JUSTIFICATION
```

Use the default justification for the title text.

**See Also:** Constant Field Values

- LEFT

```java
public static final int LEFT
```

Position title text at the left side of the border line.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

Position title text in the center of the border line.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

Position title text at the right side of the border line.

**See Also:** Constant Field Values

- LEADING

```java
public static final int LEADING
```

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

**See Also:** Constant Field Values

- TRAILING

```java
public static final int TRAILING
```

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

**See Also:** Constant Field Values

- EDGE_SPACING

```java
protected static final int EDGE_SPACING
```

Space between the border and the component's edge

**See Also:** Constant Field Values

- TEXT_SPACING

```java
protected static final int TEXT_SPACING
```

Space between the border and text

**See Also:** Constant Field Values

- TEXT_INSET_H

```java
protected static final int TEXT_INSET_H
```

Horizontal inset of text that is left or right justified

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TitledBorder

```java
public TitledBorder​(
String
title)
```

Creates a TitledBorder instance.

**Parameters:** title

- the title the border should display

- TitledBorder

```java
public TitledBorder​(
Border
border)
```

Creates a TitledBorder instance with the specified border
and an empty title.

**Parameters:** border

- the border

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title)
```

Creates a TitledBorder instance with the specified border
and title.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font for rendering the title

- TitledBorder

```java
@ConstructorProperties
({"border","title","titleJustification","titlePosition","titleFont","titleColor"})
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont,

Color
titleColor)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font of the title
**Parameters:** titleColor

- the color of the title

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
**Returns:** false

- getTitle

```java
public
String
getTitle()
```

Returns the title of the titled border.

**Returns:** the title of the titled border

- getBorder

```java
public
Border
getBorder()
```

Returns the border of the titled border.

**Returns:** the border of the titled border

- getTitlePosition

```java
public int getTitlePosition()
```

Returns the title-position of the titled border.

**Returns:** the title-position of the titled border

- getTitleJustification

```java
public int getTitleJustification()
```

Returns the title-justification of the titled border.

**Returns:** the title-justification of the titled border

- getTitleFont

```java
public
Font
getTitleFont()
```

Returns the title-font of the titled border.

**Returns:** the title-font of the titled border

- getTitleColor

```java
public
Color
getTitleColor()
```

Returns the title-color of the titled border.

**Returns:** the title-color of the titled border

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the titled border.

**Parameters:** title

- the title for the border

- setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of the titled border.

**Parameters:** border

- the border

- setTitlePosition

```java
public void setTitlePosition​(int titlePosition)
```

Sets the title-position of the titled border.

**Parameters:** titlePosition

- the position for the border

- setTitleJustification

```java
public void setTitleJustification​(int titleJustification)
```

Sets the title-justification of the titled border.

**Parameters:** titleJustification

- the justification for the border

- setTitleFont

```java
public void setTitleFont​(
Font
titleFont)
```

Sets the title-font of the titled border.

**Parameters:** titleFont

- the font for the border title

- setTitleColor

```java
public void setTitleColor​(
Color
titleColor)
```

Sets the title-color of the titled border.

**Parameters:** titleColor

- the color for the border title

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
Component
c)
```

Returns the minimum dimensions this border requires
in order to fully display the border and title.

**Parameters:** c

- the component where this border will be drawn
**Returns:** the

Dimension

object

- getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

AbstractBorder
**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of the border
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

AbstractBorder
**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Throws:** NullPointerException
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getFont

```java
protected
Font
getFont​(
Component
c)
```

Returns default font of the titled border.

**Parameters:** c

- the component
**Returns:** default font of the titled border

Field Detail

- title

```java
protected
String
title
```

The title the border should display.

- border

```java
protected
Border
border
```

The border.

- titlePosition

```java
protected int titlePosition
```

The position for the title.

- titleJustification

```java
protected int titleJustification
```

The justification for the title.

- titleFont

```java
protected
Font
titleFont
```

The font for rendering the title.

- titleColor

```java
protected
Color
titleColor
```

The color of the title.

- DEFAULT_POSITION

```java
public static final int DEFAULT_POSITION
```

Use the default vertical orientation for the title text.

**See Also:** Constant Field Values

- ABOVE_TOP

```java
public static final int ABOVE_TOP
```

Position the title above the border's top line.

**See Also:** Constant Field Values

- TOP

```java
public static final int TOP
```

Position the title in the middle of the border's top line.

**See Also:** Constant Field Values

- BELOW_TOP

```java
public static final int BELOW_TOP
```

Position the title below the border's top line.

**See Also:** Constant Field Values

- ABOVE_BOTTOM

```java
public static final int ABOVE_BOTTOM
```

Position the title above the border's bottom line.

**See Also:** Constant Field Values

- BOTTOM

```java
public static final int BOTTOM
```

Position the title in the middle of the border's bottom line.

**See Also:** Constant Field Values

- BELOW_BOTTOM

```java
public static final int BELOW_BOTTOM
```

Position the title below the border's bottom line.

**See Also:** Constant Field Values

- DEFAULT_JUSTIFICATION

```java
public static final int DEFAULT_JUSTIFICATION
```

Use the default justification for the title text.

**See Also:** Constant Field Values

- LEFT

```java
public static final int LEFT
```

Position title text at the left side of the border line.

**See Also:** Constant Field Values

- CENTER

```java
public static final int CENTER
```

Position title text in the center of the border line.

**See Also:** Constant Field Values

- RIGHT

```java
public static final int RIGHT
```

Position title text at the right side of the border line.

**See Also:** Constant Field Values

- LEADING

```java
public static final int LEADING
```

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

**See Also:** Constant Field Values

- TRAILING

```java
public static final int TRAILING
```

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

**See Also:** Constant Field Values

- EDGE_SPACING

```java
protected static final int EDGE_SPACING
```

Space between the border and the component's edge

**See Also:** Constant Field Values

- TEXT_SPACING

```java
protected static final int TEXT_SPACING
```

Space between the border and text

**See Also:** Constant Field Values

- TEXT_INSET_H

```java
protected static final int TEXT_INSET_H
```

Horizontal inset of text that is left or right justified

**See Also:** Constant Field Values

---

#### Field Detail

title

```java
protected
String
title
```

The title the border should display.

---

#### title

protected

String

title

The title the border should display.

border

```java
protected
Border
border
```

The border.

---

#### border

protected

Border

border

The border.

titlePosition

```java
protected int titlePosition
```

The position for the title.

---

#### titlePosition

protected int titlePosition

The position for the title.

titleJustification

```java
protected int titleJustification
```

The justification for the title.

---

#### titleJustification

protected int titleJustification

The justification for the title.

titleFont

```java
protected
Font
titleFont
```

The font for rendering the title.

---

#### titleFont

protected

Font

titleFont

The font for rendering the title.

titleColor

```java
protected
Color
titleColor
```

The color of the title.

---

#### titleColor

protected

Color

titleColor

The color of the title.

DEFAULT_POSITION

```java
public static final int DEFAULT_POSITION
```

Use the default vertical orientation for the title text.

**See Also:** Constant Field Values

---

#### DEFAULT_POSITION

public static final int DEFAULT_POSITION

Use the default vertical orientation for the title text.

ABOVE_TOP

```java
public static final int ABOVE_TOP
```

Position the title above the border's top line.

**See Also:** Constant Field Values

---

#### ABOVE_TOP

public static final int ABOVE_TOP

Position the title above the border's top line.

TOP

```java
public static final int TOP
```

Position the title in the middle of the border's top line.

**See Also:** Constant Field Values

---

#### TOP

public static final int TOP

Position the title in the middle of the border's top line.

BELOW_TOP

```java
public static final int BELOW_TOP
```

Position the title below the border's top line.

**See Also:** Constant Field Values

---

#### BELOW_TOP

public static final int BELOW_TOP

Position the title below the border's top line.

ABOVE_BOTTOM

```java
public static final int ABOVE_BOTTOM
```

Position the title above the border's bottom line.

**See Also:** Constant Field Values

---

#### ABOVE_BOTTOM

public static final int ABOVE_BOTTOM

Position the title above the border's bottom line.

BOTTOM

```java
public static final int BOTTOM
```

Position the title in the middle of the border's bottom line.

**See Also:** Constant Field Values

---

#### BOTTOM

public static final int BOTTOM

Position the title in the middle of the border's bottom line.

BELOW_BOTTOM

```java
public static final int BELOW_BOTTOM
```

Position the title below the border's bottom line.

**See Also:** Constant Field Values

---

#### BELOW_BOTTOM

public static final int BELOW_BOTTOM

Position the title below the border's bottom line.

DEFAULT_JUSTIFICATION

```java
public static final int DEFAULT_JUSTIFICATION
```

Use the default justification for the title text.

**See Also:** Constant Field Values

---

#### DEFAULT_JUSTIFICATION

public static final int DEFAULT_JUSTIFICATION

Use the default justification for the title text.

LEFT

```java
public static final int LEFT
```

Position title text at the left side of the border line.

**See Also:** Constant Field Values

---

#### LEFT

public static final int LEFT

Position title text at the left side of the border line.

CENTER

```java
public static final int CENTER
```

Position title text in the center of the border line.

**See Also:** Constant Field Values

---

#### CENTER

public static final int CENTER

Position title text in the center of the border line.

RIGHT

```java
public static final int RIGHT
```

Position title text at the right side of the border line.

**See Also:** Constant Field Values

---

#### RIGHT

public static final int RIGHT

Position title text at the right side of the border line.

LEADING

```java
public static final int LEADING
```

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

**See Also:** Constant Field Values

---

#### LEADING

public static final int LEADING

Position title text at the left side of the border line
for left to right orientation, at the right side of the
border line for right to left orientation.

TRAILING

```java
public static final int TRAILING
```

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

**See Also:** Constant Field Values

---

#### TRAILING

public static final int TRAILING

Position title text at the right side of the border line
for left to right orientation, at the left side of the
border line for right to left orientation.

EDGE_SPACING

```java
protected static final int EDGE_SPACING
```

Space between the border and the component's edge

**See Also:** Constant Field Values

---

#### EDGE_SPACING

protected static final int EDGE_SPACING

Space between the border and the component's edge

TEXT_SPACING

```java
protected static final int TEXT_SPACING
```

Space between the border and text

**See Also:** Constant Field Values

---

#### TEXT_SPACING

protected static final int TEXT_SPACING

Space between the border and text

TEXT_INSET_H

```java
protected static final int TEXT_INSET_H
```

Horizontal inset of text that is left or right justified

**See Also:** Constant Field Values

---

#### TEXT_INSET_H

protected static final int TEXT_INSET_H

Horizontal inset of text that is left or right justified

Constructor Detail

- TitledBorder

```java
public TitledBorder​(
String
title)
```

Creates a TitledBorder instance.

**Parameters:** title

- the title the border should display

- TitledBorder

```java
public TitledBorder​(
Border
border)
```

Creates a TitledBorder instance with the specified border
and an empty title.

**Parameters:** border

- the border

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title)
```

Creates a TitledBorder instance with the specified border
and title.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title

- TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font for rendering the title

- TitledBorder

```java
@ConstructorProperties
({"border","title","titleJustification","titlePosition","titleFont","titleColor"})
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont,

Color
titleColor)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font of the title
**Parameters:** titleColor

- the color of the title

---

#### Constructor Detail

TitledBorder

```java
public TitledBorder​(
String
title)
```

Creates a TitledBorder instance.

**Parameters:** title

- the title the border should display

---

#### TitledBorder

public TitledBorder​(

String

title)

Creates a TitledBorder instance.

TitledBorder

```java
public TitledBorder​(
Border
border)
```

Creates a TitledBorder instance with the specified border
and an empty title.

**Parameters:** border

- the border

---

#### TitledBorder

public TitledBorder​(

Border

border)

Creates a TitledBorder instance with the specified border
and an empty title.

TitledBorder

```java
public TitledBorder​(
Border
border,

String
title)
```

Creates a TitledBorder instance with the specified border
and title.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display

---

#### TitledBorder

public TitledBorder​(

Border

border,

String

title)

Creates a TitledBorder instance with the specified border
and title.

TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title

---

#### TitledBorder

public TitledBorder​(

Border

border,

String

title,
int titleJustification,
int titlePosition)

Creates a TitledBorder instance with the specified border,
title, title-justification, and title-position.

TitledBorder

```java
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font for rendering the title

---

#### TitledBorder

public TitledBorder​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, and title-font.

TitledBorder

```java
@ConstructorProperties
({"border","title","titleJustification","titlePosition","titleFont","titleColor"})
public TitledBorder​(
Border
border,

String
title,
int titleJustification,
int titlePosition,

Font
titleFont,

Color
titleColor)
```

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

**Parameters:** border

- the border
**Parameters:** title

- the title the border should display
**Parameters:** titleJustification

- the justification for the title
**Parameters:** titlePosition

- the position for the title
**Parameters:** titleFont

- the font of the title
**Parameters:** titleColor

- the color of the title

---

#### TitledBorder

@ConstructorProperties

({"border","title","titleJustification","titlePosition","titleFont","titleColor"})
public TitledBorder​(

Border

border,

String

title,
int titleJustification,
int titlePosition,

Font

titleFont,

Color

titleColor)

Creates a TitledBorder instance with the specified border,
title, title-justification, title-position, title-font, and
title-color.

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
**Returns:** false

- getTitle

```java
public
String
getTitle()
```

Returns the title of the titled border.

**Returns:** the title of the titled border

- getBorder

```java
public
Border
getBorder()
```

Returns the border of the titled border.

**Returns:** the border of the titled border

- getTitlePosition

```java
public int getTitlePosition()
```

Returns the title-position of the titled border.

**Returns:** the title-position of the titled border

- getTitleJustification

```java
public int getTitleJustification()
```

Returns the title-justification of the titled border.

**Returns:** the title-justification of the titled border

- getTitleFont

```java
public
Font
getTitleFont()
```

Returns the title-font of the titled border.

**Returns:** the title-font of the titled border

- getTitleColor

```java
public
Color
getTitleColor()
```

Returns the title-color of the titled border.

**Returns:** the title-color of the titled border

- setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the titled border.

**Parameters:** title

- the title for the border

- setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of the titled border.

**Parameters:** border

- the border

- setTitlePosition

```java
public void setTitlePosition​(int titlePosition)
```

Sets the title-position of the titled border.

**Parameters:** titlePosition

- the position for the border

- setTitleJustification

```java
public void setTitleJustification​(int titleJustification)
```

Sets the title-justification of the titled border.

**Parameters:** titleJustification

- the justification for the border

- setTitleFont

```java
public void setTitleFont​(
Font
titleFont)
```

Sets the title-font of the titled border.

**Parameters:** titleFont

- the font for the border title

- setTitleColor

```java
public void setTitleColor​(
Color
titleColor)
```

Sets the title-color of the titled border.

**Parameters:** titleColor

- the color for the border title

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
Component
c)
```

Returns the minimum dimensions this border requires
in order to fully display the border and title.

**Parameters:** c

- the component where this border will be drawn
**Returns:** the

Dimension

object

- getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

AbstractBorder
**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of the border
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

AbstractBorder
**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Throws:** NullPointerException
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getFont

```java
protected
Font
getFont​(
Component
c)
```

Returns default font of the titled border.

**Parameters:** c

- the component
**Returns:** default font of the titled border

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
**Returns:** false

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque.

getTitle

```java
public
String
getTitle()
```

Returns the title of the titled border.

**Returns:** the title of the titled border

---

#### getTitle

public

String

getTitle()

Returns the title of the titled border.

getBorder

```java
public
Border
getBorder()
```

Returns the border of the titled border.

**Returns:** the border of the titled border

---

#### getBorder

public

Border

getBorder()

Returns the border of the titled border.

getTitlePosition

```java
public int getTitlePosition()
```

Returns the title-position of the titled border.

**Returns:** the title-position of the titled border

---

#### getTitlePosition

public int getTitlePosition()

Returns the title-position of the titled border.

getTitleJustification

```java
public int getTitleJustification()
```

Returns the title-justification of the titled border.

**Returns:** the title-justification of the titled border

---

#### getTitleJustification

public int getTitleJustification()

Returns the title-justification of the titled border.

getTitleFont

```java
public
Font
getTitleFont()
```

Returns the title-font of the titled border.

**Returns:** the title-font of the titled border

---

#### getTitleFont

public

Font

getTitleFont()

Returns the title-font of the titled border.

getTitleColor

```java
public
Color
getTitleColor()
```

Returns the title-color of the titled border.

**Returns:** the title-color of the titled border

---

#### getTitleColor

public

Color

getTitleColor()

Returns the title-color of the titled border.

setTitle

```java
public void setTitle​(
String
title)
```

Sets the title of the titled border.

**Parameters:** title

- the title for the border

---

#### setTitle

public void setTitle​(

String

title)

Sets the title of the titled border.

setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of the titled border.

**Parameters:** border

- the border

---

#### setBorder

public void setBorder​(

Border

border)

Sets the border of the titled border.

setTitlePosition

```java
public void setTitlePosition​(int titlePosition)
```

Sets the title-position of the titled border.

**Parameters:** titlePosition

- the position for the border

---

#### setTitlePosition

public void setTitlePosition​(int titlePosition)

Sets the title-position of the titled border.

setTitleJustification

```java
public void setTitleJustification​(int titleJustification)
```

Sets the title-justification of the titled border.

**Parameters:** titleJustification

- the justification for the border

---

#### setTitleJustification

public void setTitleJustification​(int titleJustification)

Sets the title-justification of the titled border.

setTitleFont

```java
public void setTitleFont​(
Font
titleFont)
```

Sets the title-font of the titled border.

**Parameters:** titleFont

- the font for the border title

---

#### setTitleFont

public void setTitleFont​(

Font

titleFont)

Sets the title-font of the titled border.

setTitleColor

```java
public void setTitleColor​(
Color
titleColor)
```

Sets the title-color of the titled border.

**Parameters:** titleColor

- the color for the border title

---

#### setTitleColor

public void setTitleColor​(

Color

titleColor)

Sets the title-color of the titled border.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
Component
c)
```

Returns the minimum dimensions this border requires
in order to fully display the border and title.

**Parameters:** c

- the component where this border will be drawn
**Returns:** the

Dimension

object

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

Component

c)

Returns the minimum dimensions this border requires
in order to fully display the border and title.

getBaseline

```java
public int getBaseline​(
Component
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

AbstractBorder
**Parameters:** c

-

Component

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** the baseline or < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

Component

c,
int width,
int height)

Returns the baseline.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
Component
c)
```

Returns an enum indicating how the baseline of the border
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

AbstractBorder
**Parameters:** c

-

Component

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the border is
resized
**Throws:** NullPointerException
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

Component

c)

Returns an enum indicating how the baseline of the border
changes as the size changes.

getFont

```java
protected
Font
getFont​(
Component
c)
```

Returns default font of the titled border.

**Parameters:** c

- the component
**Returns:** default font of the titled border

---

#### getFont

protected

Font

getFont​(

Component

c)

Returns default font of the titled border.

---

