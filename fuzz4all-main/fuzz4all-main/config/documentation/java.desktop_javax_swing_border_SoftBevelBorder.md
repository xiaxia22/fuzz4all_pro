# Class SoftBevelBorder

**Source:** `java.desktop\javax\swing\border\SoftBevelBorder.html`

### Class Description

```java
public class
SoftBevelBorder

extends
BevelBorder
```

A class which implements a raised or lowered bevel with
softened corners.

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

*No entries found.*

### Constructor Details

#### public SoftBevelBorder​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:**
- bevelType

- the type of bevel for the border

---

#### public SoftBevelBorder​(int bevelType,

Color
highlight,

Color
shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

**Parameters:**
- bevelType

- the type of bevel for the border
- highlight

- the color to use for the bevel highlight
- shadow

- the color to use for the bevel shadow

---

#### @ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public SoftBevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)

Creates a bevel border with the specified type, highlight
shadow colors.

**Parameters:**
- bevelType

- the type of bevel for the border
- highlightOuterColor

- the color to use for the bevel outer highlight
- highlightInnerColor

- the color to use for the bevel inner highlight
- shadowOuterColor

- the color to use for the bevel outer shadow
- shadowInnerColor

- the color to use for the bevel inner shadow

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

Paints the border for the specified component with the specified
position and size.

**Specified by:**
- paintBorder

in interface

Border

**Overrides:**
- paintBorder

in class

BevelBorder

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

BevelBorder

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

BevelBorder

**Returns:**
- true

---

### Additional Sections

#### Class SoftBevelBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.BevelBorder
- - javax.swing.border.SoftBevelBorder

javax.swing.border.AbstractBorder

- javax.swing.border.BevelBorder
- - javax.swing.border.SoftBevelBorder

javax.swing.border.BevelBorder

- javax.swing.border.SoftBevelBorder

javax.swing.border.SoftBevelBorder

**All Implemented Interfaces:** Serializable

,

Border

```java
public class
SoftBevelBorder

extends
BevelBorder
```

A class which implements a raised or lowered bevel with
softened corners.

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

SoftBevelBorder

extends

BevelBorder

A class which implements a raised or lowered bevel with
softened corners.

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

- Fields declared in class javax.swing.border.

BevelBorder

bevelType

,

highlightInner

,

highlightOuter

,

LOWERED

,

RAISED

,

shadowInner

,

shadowOuter

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SoftBevelBorder

​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

SoftBevelBorder

​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

SoftBevelBorder

​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight
shadow colors.

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

Reinitialize the insets parameter with this Border's current Insets.

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

Paints the border for the specified component with the specified
position and size.

- Methods declared in class javax.swing.border.

BevelBorder

getBevelType

,

getHighlightInnerColor

,

getHighlightInnerColor

,

getHighlightOuterColor

,

getHighlightOuterColor

,

getShadowInnerColor

,

getShadowInnerColor

,

getShadowOuterColor

,

getShadowOuterColor

,

paintLoweredBevel

,

paintRaisedBevel

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

- Fields declared in class javax.swing.border.

BevelBorder

bevelType

,

highlightInner

,

highlightOuter

,

LOWERED

,

RAISED

,

shadowInner

,

shadowOuter

---

#### Field Summary

Fields declared in class javax.swing.border.

BevelBorder

bevelType

,

highlightInner

,

highlightOuter

,

LOWERED

,

RAISED

,

shadowInner

,

shadowOuter

---

#### Fields declared in class javax.swing.border. BevelBorder

Constructor Summary

Constructors

Constructor

Description

SoftBevelBorder

​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

SoftBevelBorder

​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

SoftBevelBorder

​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight
shadow colors.

---

#### Constructor Summary

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

Creates a bevel border with the specified type, highlight and
shadow colors.

Creates a bevel border with the specified type, highlight
shadow colors.

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

Reinitialize the insets parameter with this Border's current Insets.

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

Paints the border for the specified component with the specified
position and size.

- Methods declared in class javax.swing.border.

BevelBorder

getBevelType

,

getHighlightInnerColor

,

getHighlightInnerColor

,

getHighlightOuterColor

,

getHighlightOuterColor

,

getShadowInnerColor

,

getShadowInnerColor

,

getShadowOuterColor

,

getShadowOuterColor

,

paintLoweredBevel

,

paintRaisedBevel

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

Reinitialize the insets parameter with this Border's current Insets.

Returns whether or not the border is opaque.

Paints the border for the specified component with the specified
position and size.

Methods declared in class javax.swing.border.

BevelBorder

getBevelType

,

getHighlightInnerColor

,

getHighlightInnerColor

,

getHighlightOuterColor

,

getHighlightOuterColor

,

getShadowInnerColor

,

getShadowInnerColor

,

getShadowOuterColor

,

getShadowOuterColor

,

paintLoweredBevel

,

paintRaisedBevel

---

#### Methods declared in class javax.swing.border. BevelBorder

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

- SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType,

Color
highlight,

Color
shadow)
```

Creates a bevel border with the specified type, highlight and
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlight

- the color to use for the bevel highlight
**Parameters:** shadow

- the color to use for the bevel shadow

- SoftBevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public SoftBevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlightOuterColor

- the color to use for the bevel outer highlight
**Parameters:** highlightInnerColor

- the color to use for the bevel inner highlight
**Parameters:** shadowOuterColor

- the color to use for the bevel outer shadow
**Parameters:** shadowInnerColor

- the color to use for the bevel inner shadow

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

Paints the border for the specified component with the specified
position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

BevelBorder
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

BevelBorder
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

BevelBorder
**Returns:** true

Constructor Detail

- SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

- SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType,

Color
highlight,

Color
shadow)
```

Creates a bevel border with the specified type, highlight and
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlight

- the color to use for the bevel highlight
**Parameters:** shadow

- the color to use for the bevel shadow

- SoftBevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public SoftBevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlightOuterColor

- the color to use for the bevel outer highlight
**Parameters:** highlightInnerColor

- the color to use for the bevel inner highlight
**Parameters:** shadowOuterColor

- the color to use for the bevel outer shadow
**Parameters:** shadowInnerColor

- the color to use for the bevel inner shadow

---

#### Constructor Detail

SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

---

#### SoftBevelBorder

public SoftBevelBorder​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

SoftBevelBorder

```java
public SoftBevelBorder​(int bevelType,

Color
highlight,

Color
shadow)
```

Creates a bevel border with the specified type, highlight and
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlight

- the color to use for the bevel highlight
**Parameters:** shadow

- the color to use for the bevel shadow

---

#### SoftBevelBorder

public SoftBevelBorder​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

SoftBevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public SoftBevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight
shadow colors.

**Parameters:** bevelType

- the type of bevel for the border
**Parameters:** highlightOuterColor

- the color to use for the bevel outer highlight
**Parameters:** highlightInnerColor

- the color to use for the bevel inner highlight
**Parameters:** shadowOuterColor

- the color to use for the bevel outer shadow
**Parameters:** shadowInnerColor

- the color to use for the bevel inner shadow

---

#### SoftBevelBorder

@ConstructorProperties

({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public SoftBevelBorder​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight
shadow colors.

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

Paints the border for the specified component with the specified
position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

BevelBorder
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

BevelBorder
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

BevelBorder
**Returns:** true

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

Paints the border for the specified component with the specified
position and size.

**Specified by:** paintBorder

in interface

Border
**Overrides:** paintBorder

in class

BevelBorder
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

Paints the border for the specified component with the specified
position and size.

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

BevelBorder
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

BevelBorder
**Returns:** true

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque.

---

