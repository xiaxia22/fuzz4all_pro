# Class BevelBorder

**Source:** `java.desktop\javax\swing\border\BevelBorder.html`

### Class Description

```java
public class
BevelBorder

extends
AbstractBorder
```

A class which implements a simple two-line bevel border.

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

#### public static final int RAISED

Raised bevel type.

**See Also:**
- Constant Field Values

---

#### public static final int LOWERED

Lowered bevel type.

**See Also:**
- Constant Field Values

---

#### protected int bevelType

The bevel type.

---

#### protected
Color
highlightOuter

The color to use for the bevel outer highlight.

---

#### protected
Color
highlightInner

The color to use for the bevel inner highlight.

---

#### protected
Color
shadowInner

The color to use for the bevel inner shadow.

---

#### protected
Color
shadowOuter

the color to use for the bevel outer shadow

---

### Constructor Details

#### public BevelBorder​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:**
- bevelType

- the type of bevel for the border

---

#### public BevelBorder​(int bevelType,

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
public BevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)

Creates a bevel border with the specified type, highlight and
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
getHighlightOuterColor​(
Component
c)

Returns the outer highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the highlight may be derived

**Returns:**
- the outer highlight

Color

**Since:**
- 1.3

---

#### public
Color
getHighlightInnerColor​(
Component
c)

Returns the inner highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the highlight may be derived

**Returns:**
- the inner highlight

Color

**Since:**
- 1.3

---

#### public
Color
getShadowInnerColor​(
Component
c)

Returns the inner shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the shadow may be derived

**Returns:**
- the inner shadow

Color

**Since:**
- 1.3

---

#### public
Color
getShadowOuterColor​(
Component
c)

Returns the outer shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:**
- c

- the component for which the shadow may be derived

**Returns:**
- the outer shadow

Color

**Since:**
- 1.3

---

#### public
Color
getHighlightOuterColor()

Returns the outer highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:**
- the outer highlight

Color

or

null

if no highlight
color was specified

**Since:**
- 1.3

---

#### public
Color
getHighlightInnerColor()

Returns the inner highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:**
- the inner highlight

Color

or

null

if no highlight
color was specified

**Since:**
- 1.3

---

#### public
Color
getShadowInnerColor()

Returns the inner shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:**
- the inner shadow

Color

or

null

if no shadow color
was specified

**Since:**
- 1.3

---

#### public
Color
getShadowOuterColor()

Returns the outer shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:**
- the outer shadow

Color

or

null

if no shadow color
was specified

**Since:**
- 1.3

---

#### public int getBevelType()

Returns the type of the bevel border.

**Returns:**
- the bevel border type, either

RAISED

or

LOWERED

---

#### public boolean isBorderOpaque()

Returns whether or not the border is opaque. This implementation
returns

true

.

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

---

#### protected void paintRaisedBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints a raised bevel for the specified component with the specified
position and size.

**Parameters:**
- c

- the component for which the raised bevel is being painted
- g

- the paint graphics
- x

- the x position of the raised bevel
- y

- the y position of the raised bevel
- width

- the width of the raised bevel
- height

- the height of the raised bevel

---

#### protected void paintLoweredBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)

Paints a lowered bevel for the specified component with the specified
position and size.

**Parameters:**
- c

- the component for which the lowered bevel is being painted
- g

- the paint graphics
- x

- the x position of the lowered bevel
- y

- the y position of the lowered bevel
- width

- the width of the lowered bevel
- height

- the height of the lowered bevel

---

### Additional Sections

#### Class BevelBorder

java.lang.Object

- javax.swing.border.AbstractBorder
- - javax.swing.border.BevelBorder

javax.swing.border.AbstractBorder

- javax.swing.border.BevelBorder

javax.swing.border.BevelBorder

**All Implemented Interfaces:** Serializable

,

Border

**Direct Known Subclasses:** BorderUIResource.BevelBorderUIResource

,

SoftBevelBorder

```java
public class
BevelBorder

extends
AbstractBorder
```

A class which implements a simple two-line bevel border.

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

BevelBorder

extends

AbstractBorder

A class which implements a simple two-line bevel border.

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

protected int

bevelType

The bevel type.

protected

Color

highlightInner

The color to use for the bevel inner highlight.

protected

Color

highlightOuter

The color to use for the bevel outer highlight.

static int

LOWERED

Lowered bevel type.

static int

RAISED

Raised bevel type.

protected

Color

shadowInner

The color to use for the bevel inner shadow.

protected

Color

shadowOuter

the color to use for the bevel outer shadow

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BevelBorder

​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

BevelBorder

​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

BevelBorder

​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight and
shadow colors.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBevelType

()

Returns the type of the bevel border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Color

getHighlightInnerColor

()

Returns the inner highlight color of the bevel border.

Color

getHighlightInnerColor

​(

Component

c)

Returns the inner highlight color of the bevel border
when rendered on the specified component.

Color

getHighlightOuterColor

()

Returns the outer highlight color of the bevel border.

Color

getHighlightOuterColor

​(

Component

c)

Returns the outer highlight color of the bevel border
when rendered on the specified component.

Color

getShadowInnerColor

()

Returns the inner shadow color of the bevel border.

Color

getShadowInnerColor

​(

Component

c)

Returns the inner shadow color of the bevel border
when rendered on the specified component.

Color

getShadowOuterColor

()

Returns the outer shadow color of the bevel border.

Color

getShadowOuterColor

​(

Component

c)

Returns the outer shadow color of the bevel border
when rendered on the specified component.

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

protected void

paintLoweredBevel

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a lowered bevel for the specified component with the specified
position and size.

protected void

paintRaisedBevel

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a raised bevel for the specified component with the specified
position and size.

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

protected int

bevelType

The bevel type.

protected

Color

highlightInner

The color to use for the bevel inner highlight.

protected

Color

highlightOuter

The color to use for the bevel outer highlight.

static int

LOWERED

Lowered bevel type.

static int

RAISED

Raised bevel type.

protected

Color

shadowInner

The color to use for the bevel inner shadow.

protected

Color

shadowOuter

the color to use for the bevel outer shadow

---

#### Field Summary

The bevel type.

The color to use for the bevel inner highlight.

The color to use for the bevel outer highlight.

Lowered bevel type.

Raised bevel type.

The color to use for the bevel inner shadow.

the color to use for the bevel outer shadow

Constructor Summary

Constructors

Constructor

Description

BevelBorder

​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

BevelBorder

​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

BevelBorder

​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight and
shadow colors.

---

#### Constructor Summary

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

Creates a bevel border with the specified type, highlight and
shadow colors.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getBevelType

()

Returns the type of the bevel border.

Insets

getBorderInsets

​(

Component

c,

Insets

insets)

Reinitialize the insets parameter with this Border's current Insets.

Color

getHighlightInnerColor

()

Returns the inner highlight color of the bevel border.

Color

getHighlightInnerColor

​(

Component

c)

Returns the inner highlight color of the bevel border
when rendered on the specified component.

Color

getHighlightOuterColor

()

Returns the outer highlight color of the bevel border.

Color

getHighlightOuterColor

​(

Component

c)

Returns the outer highlight color of the bevel border
when rendered on the specified component.

Color

getShadowInnerColor

()

Returns the inner shadow color of the bevel border.

Color

getShadowInnerColor

​(

Component

c)

Returns the inner shadow color of the bevel border
when rendered on the specified component.

Color

getShadowOuterColor

()

Returns the outer shadow color of the bevel border.

Color

getShadowOuterColor

​(

Component

c)

Returns the outer shadow color of the bevel border
when rendered on the specified component.

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

protected void

paintLoweredBevel

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a lowered bevel for the specified component with the specified
position and size.

protected void

paintRaisedBevel

​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a raised bevel for the specified component with the specified
position and size.

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

Returns the type of the bevel border.

Reinitialize the insets parameter with this Border's current Insets.

Returns the inner highlight color of the bevel border.

Returns the inner highlight color of the bevel border
when rendered on the specified component.

Returns the outer highlight color of the bevel border.

Returns the outer highlight color of the bevel border
when rendered on the specified component.

Returns the inner shadow color of the bevel border.

Returns the inner shadow color of the bevel border
when rendered on the specified component.

Returns the outer shadow color of the bevel border.

Returns the outer shadow color of the bevel border
when rendered on the specified component.

Returns whether or not the border is opaque.

Paints the border for the specified component with the specified
position and size.

Paints a lowered bevel for the specified component with the specified
position and size.

Paints a raised bevel for the specified component with the specified
position and size.

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

- RAISED

```java
public static final int RAISED
```

Raised bevel type.

**See Also:** Constant Field Values

- LOWERED

```java
public static final int LOWERED
```

Lowered bevel type.

**See Also:** Constant Field Values

- bevelType

```java
protected int bevelType
```

The bevel type.

- highlightOuter

```java
protected
Color
highlightOuter
```

The color to use for the bevel outer highlight.

- highlightInner

```java
protected
Color
highlightInner
```

The color to use for the bevel inner highlight.

- shadowInner

```java
protected
Color
shadowInner
```

The color to use for the bevel inner shadow.

- shadowOuter

```java
protected
Color
shadowOuter
```

the color to use for the bevel outer shadow

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BevelBorder

```java
public BevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

- BevelBorder

```java
public BevelBorder​(int bevelType,

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

- BevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public BevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight and
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

- getHighlightOuterColor

```java
public
Color
getHighlightOuterColor​(
Component
c)
```

Returns the outer highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the outer highlight

Color
**Since:** 1.3

- getHighlightInnerColor

```java
public
Color
getHighlightInnerColor​(
Component
c)
```

Returns the inner highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the inner highlight

Color
**Since:** 1.3

- getShadowInnerColor

```java
public
Color
getShadowInnerColor​(
Component
c)
```

Returns the inner shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the inner shadow

Color
**Since:** 1.3

- getShadowOuterColor

```java
public
Color
getShadowOuterColor​(
Component
c)
```

Returns the outer shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the outer shadow

Color
**Since:** 1.3

- getHighlightOuterColor

```java
public
Color
getHighlightOuterColor()
```

Returns the outer highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the outer highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

- getHighlightInnerColor

```java
public
Color
getHighlightInnerColor()
```

Returns the inner highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the inner highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

- getShadowInnerColor

```java
public
Color
getShadowInnerColor()
```

Returns the inner shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the inner shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

- getShadowOuterColor

```java
public
Color
getShadowOuterColor()
```

Returns the outer shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the outer shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

- getBevelType

```java
public int getBevelType()
```

Returns the type of the bevel border.

**Returns:** the bevel border type, either

RAISED

or

LOWERED

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque. This implementation
returns

true

.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

- paintRaisedBevel

```java
protected void paintRaisedBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a raised bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the raised bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the raised bevel
**Parameters:** y

- the y position of the raised bevel
**Parameters:** width

- the width of the raised bevel
**Parameters:** height

- the height of the raised bevel

- paintLoweredBevel

```java
protected void paintLoweredBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a lowered bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the lowered bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the lowered bevel
**Parameters:** y

- the y position of the lowered bevel
**Parameters:** width

- the width of the lowered bevel
**Parameters:** height

- the height of the lowered bevel

Field Detail

- RAISED

```java
public static final int RAISED
```

Raised bevel type.

**See Also:** Constant Field Values

- LOWERED

```java
public static final int LOWERED
```

Lowered bevel type.

**See Also:** Constant Field Values

- bevelType

```java
protected int bevelType
```

The bevel type.

- highlightOuter

```java
protected
Color
highlightOuter
```

The color to use for the bevel outer highlight.

- highlightInner

```java
protected
Color
highlightInner
```

The color to use for the bevel inner highlight.

- shadowInner

```java
protected
Color
shadowInner
```

The color to use for the bevel inner shadow.

- shadowOuter

```java
protected
Color
shadowOuter
```

the color to use for the bevel outer shadow

---

#### Field Detail

RAISED

```java
public static final int RAISED
```

Raised bevel type.

**See Also:** Constant Field Values

---

#### RAISED

public static final int RAISED

Raised bevel type.

LOWERED

```java
public static final int LOWERED
```

Lowered bevel type.

**See Also:** Constant Field Values

---

#### LOWERED

public static final int LOWERED

Lowered bevel type.

bevelType

```java
protected int bevelType
```

The bevel type.

---

#### bevelType

protected int bevelType

The bevel type.

highlightOuter

```java
protected
Color
highlightOuter
```

The color to use for the bevel outer highlight.

---

#### highlightOuter

protected

Color

highlightOuter

The color to use for the bevel outer highlight.

highlightInner

```java
protected
Color
highlightInner
```

The color to use for the bevel inner highlight.

---

#### highlightInner

protected

Color

highlightInner

The color to use for the bevel inner highlight.

shadowInner

```java
protected
Color
shadowInner
```

The color to use for the bevel inner shadow.

---

#### shadowInner

protected

Color

shadowInner

The color to use for the bevel inner shadow.

shadowOuter

```java
protected
Color
shadowOuter
```

the color to use for the bevel outer shadow

---

#### shadowOuter

protected

Color

shadowOuter

the color to use for the bevel outer shadow

Constructor Detail

- BevelBorder

```java
public BevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

- BevelBorder

```java
public BevelBorder​(int bevelType,

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

- BevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public BevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight and
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

BevelBorder

```java
public BevelBorder​(int bevelType)
```

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

**Parameters:** bevelType

- the type of bevel for the border

---

#### BevelBorder

public BevelBorder​(int bevelType)

Creates a bevel border with the specified type and whose
colors will be derived from the background color of the
component passed into the paintBorder method.

BevelBorder

```java
public BevelBorder​(int bevelType,

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

#### BevelBorder

public BevelBorder​(int bevelType,

Color

highlight,

Color

shadow)

Creates a bevel border with the specified type, highlight and
shadow colors.

BevelBorder

```java
@ConstructorProperties
({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public BevelBorder​(int bevelType,

Color
highlightOuterColor,

Color
highlightInnerColor,

Color
shadowOuterColor,

Color
shadowInnerColor)
```

Creates a bevel border with the specified type, highlight and
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

#### BevelBorder

@ConstructorProperties

({"bevelType","highlightOuterColor","highlightInnerColor","shadowOuterColor","shadowInnerColor"})
public BevelBorder​(int bevelType,

Color

highlightOuterColor,

Color

highlightInnerColor,

Color

shadowOuterColor,

Color

shadowInnerColor)

Creates a bevel border with the specified type, highlight and
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

- getHighlightOuterColor

```java
public
Color
getHighlightOuterColor​(
Component
c)
```

Returns the outer highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the outer highlight

Color
**Since:** 1.3

- getHighlightInnerColor

```java
public
Color
getHighlightInnerColor​(
Component
c)
```

Returns the inner highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the inner highlight

Color
**Since:** 1.3

- getShadowInnerColor

```java
public
Color
getShadowInnerColor​(
Component
c)
```

Returns the inner shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the inner shadow

Color
**Since:** 1.3

- getShadowOuterColor

```java
public
Color
getShadowOuterColor​(
Component
c)
```

Returns the outer shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the outer shadow

Color
**Since:** 1.3

- getHighlightOuterColor

```java
public
Color
getHighlightOuterColor()
```

Returns the outer highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the outer highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

- getHighlightInnerColor

```java
public
Color
getHighlightInnerColor()
```

Returns the inner highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the inner highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

- getShadowInnerColor

```java
public
Color
getShadowInnerColor()
```

Returns the inner shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the inner shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

- getShadowOuterColor

```java
public
Color
getShadowOuterColor()
```

Returns the outer shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the outer shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

- getBevelType

```java
public int getBevelType()
```

Returns the type of the bevel border.

**Returns:** the bevel border type, either

RAISED

or

LOWERED

- isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque. This implementation
returns

true

.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

- paintRaisedBevel

```java
protected void paintRaisedBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a raised bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the raised bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the raised bevel
**Parameters:** y

- the y position of the raised bevel
**Parameters:** width

- the width of the raised bevel
**Parameters:** height

- the height of the raised bevel

- paintLoweredBevel

```java
protected void paintLoweredBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a lowered bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the lowered bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the lowered bevel
**Parameters:** y

- the y position of the lowered bevel
**Parameters:** width

- the width of the lowered bevel
**Parameters:** height

- the height of the lowered bevel

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

getHighlightOuterColor

```java
public
Color
getHighlightOuterColor​(
Component
c)
```

Returns the outer highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the outer highlight

Color
**Since:** 1.3

---

#### getHighlightOuterColor

public

Color

getHighlightOuterColor​(

Component

c)

Returns the outer highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

getHighlightInnerColor

```java
public
Color
getHighlightInnerColor​(
Component
c)
```

Returns the inner highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the highlight may be derived
**Returns:** the inner highlight

Color
**Since:** 1.3

---

#### getHighlightInnerColor

public

Color

getHighlightInnerColor​(

Component

c)

Returns the inner highlight color of the bevel border
when rendered on the specified component. If no highlight
color was specified at instantiation, the highlight color
is derived from the specified component's background color.

getShadowInnerColor

```java
public
Color
getShadowInnerColor​(
Component
c)
```

Returns the inner shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the inner shadow

Color
**Since:** 1.3

---

#### getShadowInnerColor

public

Color

getShadowInnerColor​(

Component

c)

Returns the inner shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

getShadowOuterColor

```java
public
Color
getShadowOuterColor​(
Component
c)
```

Returns the outer shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

**Parameters:** c

- the component for which the shadow may be derived
**Returns:** the outer shadow

Color
**Since:** 1.3

---

#### getShadowOuterColor

public

Color

getShadowOuterColor​(

Component

c)

Returns the outer shadow color of the bevel border
when rendered on the specified component. If no shadow
color was specified at instantiation, the shadow color
is derived from the specified component's background color.

getHighlightOuterColor

```java
public
Color
getHighlightOuterColor()
```

Returns the outer highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the outer highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

---

#### getHighlightOuterColor

public

Color

getHighlightOuterColor()

Returns the outer highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

getHighlightInnerColor

```java
public
Color
getHighlightInnerColor()
```

Returns the inner highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

**Returns:** the inner highlight

Color

or

null

if no highlight
color was specified
**Since:** 1.3

---

#### getHighlightInnerColor

public

Color

getHighlightInnerColor()

Returns the inner highlight color of the bevel border.
Will return null if no highlight color was specified
at instantiation.

getShadowInnerColor

```java
public
Color
getShadowInnerColor()
```

Returns the inner shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the inner shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

---

#### getShadowInnerColor

public

Color

getShadowInnerColor()

Returns the inner shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

getShadowOuterColor

```java
public
Color
getShadowOuterColor()
```

Returns the outer shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

**Returns:** the outer shadow

Color

or

null

if no shadow color
was specified
**Since:** 1.3

---

#### getShadowOuterColor

public

Color

getShadowOuterColor()

Returns the outer shadow color of the bevel border.
Will return null if no shadow color was specified
at instantiation.

getBevelType

```java
public int getBevelType()
```

Returns the type of the bevel border.

**Returns:** the bevel border type, either

RAISED

or

LOWERED

---

#### getBevelType

public int getBevelType()

Returns the type of the bevel border.

isBorderOpaque

```java
public boolean isBorderOpaque()
```

Returns whether or not the border is opaque. This implementation
returns

true

.

**Specified by:** isBorderOpaque

in interface

Border
**Overrides:** isBorderOpaque

in class

AbstractBorder
**Returns:** true

---

#### isBorderOpaque

public boolean isBorderOpaque()

Returns whether or not the border is opaque. This implementation
returns

true

.

paintRaisedBevel

```java
protected void paintRaisedBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a raised bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the raised bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the raised bevel
**Parameters:** y

- the y position of the raised bevel
**Parameters:** width

- the width of the raised bevel
**Parameters:** height

- the height of the raised bevel

---

#### paintRaisedBevel

protected void paintRaisedBevel​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a raised bevel for the specified component with the specified
position and size.

paintLoweredBevel

```java
protected void paintLoweredBevel​(
Component
c,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints a lowered bevel for the specified component with the specified
position and size.

**Parameters:** c

- the component for which the lowered bevel is being painted
**Parameters:** g

- the paint graphics
**Parameters:** x

- the x position of the lowered bevel
**Parameters:** y

- the y position of the lowered bevel
**Parameters:** width

- the width of the lowered bevel
**Parameters:** height

- the height of the lowered bevel

---

#### paintLoweredBevel

protected void paintLoweredBevel​(

Component

c,

Graphics

g,
int x,
int y,
int width,
int height)

Paints a lowered bevel for the specified component with the specified
position and size.

---

