# Class SynthGraphicsUtils

**Source:** `java.desktop\javax\swing\plaf\synth\SynthGraphicsUtils.html`

### Class Description

```java
public class
SynthGraphicsUtils

extends
Object
```

Wrapper for primitive graphics calls.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthGraphicsUtils()

Creates a

SynthGraphicsUtils

.

---

### Method Details

#### public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2)

Draws a line between the two end points.

**Parameters:**
- context

- Identifies hosting region.
- paintKey

- Identifies the portion of the component being asked
to paint, may be null.
- g

- Graphics object to paint to
- x1

- x origin
- y1

- y origin
- x2

- x destination
- y2

- y destination

---

#### public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2,

Object
styleKey)

Draws a line between the two end points.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

**Parameters:**
- context

- identifies hosting region
- paintKey

- identifies the portion of the component being asked
to paint, may be null
- g

- Graphics object to paint to
- x1

- x origin
- y1

- y origin
- x2

- x destination
- y2

- y destination
- styleKey

- identifies the requested style of the line (e.g. "dashed")

**Since:**
- 1.6

---

#### public
String
layoutText​(
SynthContext
ss,

FontMetrics
fm,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int iconTextGap)

Lays out text and an icon returning, by reference, the location to
place the icon and text.

**Parameters:**
- ss

- SynthContext
- fm

- FontMetrics for the Font to use, this may be ignored
- text

- Text to layout
- icon

- Icon to layout
- hAlign

- horizontal alignment
- vAlign

- vertical alignment
- hTextPosition

- horizontal text position
- vTextPosition

- vertical text position
- viewR

- Rectangle to layout text and icon in.
- iconR

- Rectangle to place icon bounds in
- textR

- Rectangle to place text in
- iconTextGap

- gap between icon and text

**Returns:**
- by reference, the location to
place the icon and text.

---

#### public int computeStringWidth​(
SynthContext
ss,

Font
font,

FontMetrics
metrics,

String
text)

Returns the size of the passed in string.

**Parameters:**
- ss

- SynthContext
- font

- Font to use
- metrics

- FontMetrics, may be ignored
- text

- Text to get size of.

**Returns:**
- the size of the passed in string.

---

#### public
Dimension
getMinimumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the minimum size needed to properly render an icon and text.

**Parameters:**
- ss

- SynthContext
- font

- Font to use
- text

- Text to layout
- icon

- Icon to layout
- hAlign

- horizontal alignment
- vAlign

- vertical alignment
- hTextPosition

- horizontal text position
- vTextPosition

- vertical text position
- iconTextGap

- gap between icon and text
- mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.

**Returns:**
- the minimum size needed to properly render an icon and text.

---

#### public
Dimension
getMaximumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the maximum size needed to properly render an icon and text.

**Parameters:**
- ss

- SynthContext
- font

- Font to use
- text

- Text to layout
- icon

- Icon to layout
- hAlign

- horizontal alignment
- vAlign

- vertical alignment
- hTextPosition

- horizontal text position
- vTextPosition

- vertical text position
- iconTextGap

- gap between icon and text
- mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.

**Returns:**
- the maximum size needed to properly render an icon and text.

---

#### public int getMaximumCharHeight​(
SynthContext
context)

Returns the maximum height of the Font from the passed in
SynthContext.

**Parameters:**
- context

- SynthContext used to determine font.

**Returns:**
- maximum height of the characters for the font from the passed
in context.

---

#### public
Dimension
getPreferredSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the preferred size needed to properly render an icon and text.

**Parameters:**
- ss

- SynthContext
- font

- Font to use
- text

- Text to layout
- icon

- Icon to layout
- hAlign

- horizontal alignment
- vAlign

- vertical alignment
- hTextPosition

- horizontal text position
- vTextPosition

- vertical text position
- iconTextGap

- gap between icon and text
- mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.

**Returns:**
- the preferred size needed to properly render an icon and text.

---

#### public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Rectangle
bounds,
int mnemonicIndex)

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:**
- ss

- SynthContext
- g

- Graphics used to render string in.
- text

- Text to render
- bounds

- Bounds of the text to be drawn.
- mnemonicIndex

- Index to draw string at.

---

#### public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,
int x,
int y,
int mnemonicIndex)

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:**
- ss

- SynthContext
- g

- Graphics used to render string in.
- text

- Text to render
- x

- X location to draw text at.
- y

- Upper left corner to draw text at.
- mnemonicIndex

- Index to draw string at.

---

#### public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)

Paints an icon and text. This will render the text as html, if
necessary, and offset the location by the insets of the component.

**Parameters:**
- ss

- SynthContext
- g

- Graphics to render string and icon into
- text

- Text to layout
- icon

- Icon to layout
- hAlign

- horizontal alignment
- vAlign

- vertical alignment
- hTextPosition

- horizontal text position
- vTextPosition

- vertical text position
- iconTextGap

- gap between icon and text
- mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
- textOffset

- Amount to offset the text when painting

---

#### public static int getIconWidth​(
Icon
icon,

SynthContext
context)

Returns the icon's width.
The

getIconWidth(context)

method is called for

SynthIcon

.

**Parameters:**
- icon

- the icon
- context

-

SynthContext

requesting the icon, may be null.

**Returns:**
- an int specifying the width of the icon.

---

#### public static int getIconHeight​(
Icon
icon,

SynthContext
context)

Returns the icon's height.
The

getIconHeight(context)

method is called for

SynthIcon

.

**Parameters:**
- icon

- the icon
- context

-

SynthContext

requesting the icon, may be null.

**Returns:**
- an int specifying the height of the icon.

---

#### public static void paintIcon​(
Icon
icon,

SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)

Paints the icon. The

paintIcon(context, g, x, y, width, height)

method is called for

SynthIcon

.

**Parameters:**
- icon

- the icon
- context

- identifies hosting region, may be null.
- g

- the graphics context
- x

- the x location to paint to
- y

- the y location to paint to
- width

- the width of the region to paint to, may be 0
- height

- the height of the region to paint to, may be 0

---

### Additional Sections

#### Class SynthGraphicsUtils

java.lang.Object

- javax.swing.plaf.synth.SynthGraphicsUtils

javax.swing.plaf.synth.SynthGraphicsUtils

```java
public class
SynthGraphicsUtils

extends
Object
```

Wrapper for primitive graphics calls.

**Since:** 1.5

public class

SynthGraphicsUtils

extends

Object

Wrapper for primitive graphics calls.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SynthGraphicsUtils

()

Creates a

SynthGraphicsUtils

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

computeStringWidth

​(

SynthContext

ss,

Font

font,

FontMetrics

metrics,

String

text)

Returns the size of the passed in string.

void

drawLine

​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2)

Draws a line between the two end points.

void

drawLine

​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2,

Object

styleKey)

Draws a line between the two end points.

static int

getIconHeight

​(

Icon

icon,

SynthContext

context)

Returns the icon's height.

static int

getIconWidth

​(

Icon

icon,

SynthContext

context)

Returns the icon's width.

int

getMaximumCharHeight

​(

SynthContext

context)

Returns the maximum height of the Font from the passed in
SynthContext.

Dimension

getMaximumSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the maximum size needed to properly render an icon and text.

Dimension

getMinimumSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the minimum size needed to properly render an icon and text.

Dimension

getPreferredSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the preferred size needed to properly render an icon and text.

String

layoutText

​(

SynthContext

ss,

FontMetrics

fm,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int iconTextGap)

Lays out text and an icon returning, by reference, the location to
place the icon and text.

static void

paintIcon

​(

Icon

icon,

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,
int x,
int y,
int mnemonicIndex)

Paints text at the specified location.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,

Rectangle

bounds,
int mnemonicIndex)

Paints text at the specified location.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)

Paints an icon and text.

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

SynthGraphicsUtils

()

Creates a

SynthGraphicsUtils

.

---

#### Constructor Summary

Creates a

SynthGraphicsUtils

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

computeStringWidth

​(

SynthContext

ss,

Font

font,

FontMetrics

metrics,

String

text)

Returns the size of the passed in string.

void

drawLine

​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2)

Draws a line between the two end points.

void

drawLine

​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2,

Object

styleKey)

Draws a line between the two end points.

static int

getIconHeight

​(

Icon

icon,

SynthContext

context)

Returns the icon's height.

static int

getIconWidth

​(

Icon

icon,

SynthContext

context)

Returns the icon's width.

int

getMaximumCharHeight

​(

SynthContext

context)

Returns the maximum height of the Font from the passed in
SynthContext.

Dimension

getMaximumSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the maximum size needed to properly render an icon and text.

Dimension

getMinimumSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the minimum size needed to properly render an icon and text.

Dimension

getPreferredSize

​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the preferred size needed to properly render an icon and text.

String

layoutText

​(

SynthContext

ss,

FontMetrics

fm,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int iconTextGap)

Lays out text and an icon returning, by reference, the location to
place the icon and text.

static void

paintIcon

​(

Icon

icon,

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,
int x,
int y,
int mnemonicIndex)

Paints text at the specified location.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,

Rectangle

bounds,
int mnemonicIndex)

Paints text at the specified location.

void

paintText

​(

SynthContext

ss,

Graphics

g,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)

Paints an icon and text.

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

Returns the size of the passed in string.

Draws a line between the two end points.

Returns the icon's height.

Returns the icon's width.

Returns the maximum height of the Font from the passed in
SynthContext.

Returns the maximum size needed to properly render an icon and text.

Returns the minimum size needed to properly render an icon and text.

Returns the preferred size needed to properly render an icon and text.

Lays out text and an icon returning, by reference, the location to
place the icon and text.

Paints the icon.

Paints text at the specified location.

Paints an icon and text.

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

- SynthGraphicsUtils

```java
public SynthGraphicsUtils()
```

Creates a

SynthGraphicsUtils

.

============ METHOD DETAIL ==========

- Method Detail

- drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2)
```

Draws a line between the two end points.

**Parameters:** context

- Identifies hosting region.
**Parameters:** paintKey

- Identifies the portion of the component being asked
to paint, may be null.
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination

- drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2,

Object
styleKey)
```

Draws a line between the two end points.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

**Parameters:** context

- identifies hosting region
**Parameters:** paintKey

- identifies the portion of the component being asked
to paint, may be null
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination
**Parameters:** styleKey

- identifies the requested style of the line (e.g. "dashed")
**Since:** 1.6

- layoutText

```java
public
String
layoutText​(
SynthContext
ss,

FontMetrics
fm,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int iconTextGap)
```

Lays out text and an icon returning, by reference, the location to
place the icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** fm

- FontMetrics for the Font to use, this may be ignored
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** viewR

- Rectangle to layout text and icon in.
**Parameters:** iconR

- Rectangle to place icon bounds in
**Parameters:** textR

- Rectangle to place text in
**Parameters:** iconTextGap

- gap between icon and text
**Returns:** by reference, the location to
place the icon and text.

- computeStringWidth

```java
public int computeStringWidth​(
SynthContext
ss,

Font
font,

FontMetrics
metrics,

String
text)
```

Returns the size of the passed in string.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** metrics

- FontMetrics, may be ignored
**Parameters:** text

- Text to get size of.
**Returns:** the size of the passed in string.

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the minimum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the minimum size needed to properly render an icon and text.

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the maximum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the maximum size needed to properly render an icon and text.

- getMaximumCharHeight

```java
public int getMaximumCharHeight​(
SynthContext
context)
```

Returns the maximum height of the Font from the passed in
SynthContext.

**Parameters:** context

- SynthContext used to determine font.
**Returns:** maximum height of the characters for the font from the passed
in context.

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the preferred size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the preferred size needed to properly render an icon and text.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Rectangle
bounds,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** bounds

- Bounds of the text to be drawn.
**Parameters:** mnemonicIndex

- Index to draw string at.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,
int x,
int y,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** x

- X location to draw text at.
**Parameters:** y

- Upper left corner to draw text at.
**Parameters:** mnemonicIndex

- Index to draw string at.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)
```

Paints an icon and text. This will render the text as html, if
necessary, and offset the location by the insets of the component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics to render string and icon into
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Parameters:** textOffset

- Amount to offset the text when painting

- getIconWidth

```java
public static int getIconWidth​(
Icon
icon,

SynthContext
context)
```

Returns the icon's width.
The

getIconWidth(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the width of the icon.

- getIconHeight

```java
public static int getIconHeight​(
Icon
icon,

SynthContext
context)
```

Returns the icon's height.
The

getIconHeight(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the height of the icon.

- paintIcon

```java
public static void paintIcon​(
Icon
icon,

SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon. The

paintIcon(context, g, x, y, width, height)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

Constructor Detail

- SynthGraphicsUtils

```java
public SynthGraphicsUtils()
```

Creates a

SynthGraphicsUtils

.

---

#### Constructor Detail

SynthGraphicsUtils

```java
public SynthGraphicsUtils()
```

Creates a

SynthGraphicsUtils

.

---

#### SynthGraphicsUtils

public SynthGraphicsUtils()

Creates a

SynthGraphicsUtils

.

Method Detail

- drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2)
```

Draws a line between the two end points.

**Parameters:** context

- Identifies hosting region.
**Parameters:** paintKey

- Identifies the portion of the component being asked
to paint, may be null.
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination

- drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2,

Object
styleKey)
```

Draws a line between the two end points.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

**Parameters:** context

- identifies hosting region
**Parameters:** paintKey

- identifies the portion of the component being asked
to paint, may be null
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination
**Parameters:** styleKey

- identifies the requested style of the line (e.g. "dashed")
**Since:** 1.6

- layoutText

```java
public
String
layoutText​(
SynthContext
ss,

FontMetrics
fm,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int iconTextGap)
```

Lays out text and an icon returning, by reference, the location to
place the icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** fm

- FontMetrics for the Font to use, this may be ignored
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** viewR

- Rectangle to layout text and icon in.
**Parameters:** iconR

- Rectangle to place icon bounds in
**Parameters:** textR

- Rectangle to place text in
**Parameters:** iconTextGap

- gap between icon and text
**Returns:** by reference, the location to
place the icon and text.

- computeStringWidth

```java
public int computeStringWidth​(
SynthContext
ss,

Font
font,

FontMetrics
metrics,

String
text)
```

Returns the size of the passed in string.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** metrics

- FontMetrics, may be ignored
**Parameters:** text

- Text to get size of.
**Returns:** the size of the passed in string.

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the minimum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the minimum size needed to properly render an icon and text.

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the maximum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the maximum size needed to properly render an icon and text.

- getMaximumCharHeight

```java
public int getMaximumCharHeight​(
SynthContext
context)
```

Returns the maximum height of the Font from the passed in
SynthContext.

**Parameters:** context

- SynthContext used to determine font.
**Returns:** maximum height of the characters for the font from the passed
in context.

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the preferred size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the preferred size needed to properly render an icon and text.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Rectangle
bounds,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** bounds

- Bounds of the text to be drawn.
**Parameters:** mnemonicIndex

- Index to draw string at.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,
int x,
int y,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** x

- X location to draw text at.
**Parameters:** y

- Upper left corner to draw text at.
**Parameters:** mnemonicIndex

- Index to draw string at.

- paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)
```

Paints an icon and text. This will render the text as html, if
necessary, and offset the location by the insets of the component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics to render string and icon into
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Parameters:** textOffset

- Amount to offset the text when painting

- getIconWidth

```java
public static int getIconWidth​(
Icon
icon,

SynthContext
context)
```

Returns the icon's width.
The

getIconWidth(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the width of the icon.

- getIconHeight

```java
public static int getIconHeight​(
Icon
icon,

SynthContext
context)
```

Returns the icon's height.
The

getIconHeight(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the height of the icon.

- paintIcon

```java
public static void paintIcon​(
Icon
icon,

SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon. The

paintIcon(context, g, x, y, width, height)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

---

#### Method Detail

drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2)
```

Draws a line between the two end points.

**Parameters:** context

- Identifies hosting region.
**Parameters:** paintKey

- Identifies the portion of the component being asked
to paint, may be null.
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination

---

#### drawLine

public void drawLine​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2)

Draws a line between the two end points.

drawLine

```java
public void drawLine​(
SynthContext
context,

Object
paintKey,

Graphics
g,
int x1,
int y1,
int x2,
int y2,

Object
styleKey)
```

Draws a line between the two end points.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

**Parameters:** context

- identifies hosting region
**Parameters:** paintKey

- identifies the portion of the component being asked
to paint, may be null
**Parameters:** g

- Graphics object to paint to
**Parameters:** x1

- x origin
**Parameters:** y1

- y origin
**Parameters:** x2

- x destination
**Parameters:** y2

- y destination
**Parameters:** styleKey

- identifies the requested style of the line (e.g. "dashed")
**Since:** 1.6

---

#### drawLine

public void drawLine​(

SynthContext

context,

Object

paintKey,

Graphics

g,
int x1,
int y1,
int x2,
int y2,

Object

styleKey)

Draws a line between the two end points.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

This implementation supports only one line style key,

"dashed"

. The

"dashed"

line style is applied
only to vertical and horizontal lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

Specifying

null

or any key different from

"dashed"

will draw solid lines.

layoutText

```java
public
String
layoutText​(
SynthContext
ss,

FontMetrics
fm,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle
viewR,

Rectangle
iconR,

Rectangle
textR,
int iconTextGap)
```

Lays out text and an icon returning, by reference, the location to
place the icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** fm

- FontMetrics for the Font to use, this may be ignored
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** viewR

- Rectangle to layout text and icon in.
**Parameters:** iconR

- Rectangle to place icon bounds in
**Parameters:** textR

- Rectangle to place text in
**Parameters:** iconTextGap

- gap between icon and text
**Returns:** by reference, the location to
place the icon and text.

---

#### layoutText

public

String

layoutText​(

SynthContext

ss,

FontMetrics

fm,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,

Rectangle

viewR,

Rectangle

iconR,

Rectangle

textR,
int iconTextGap)

Lays out text and an icon returning, by reference, the location to
place the icon and text.

computeStringWidth

```java
public int computeStringWidth​(
SynthContext
ss,

Font
font,

FontMetrics
metrics,

String
text)
```

Returns the size of the passed in string.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** metrics

- FontMetrics, may be ignored
**Parameters:** text

- Text to get size of.
**Returns:** the size of the passed in string.

---

#### computeStringWidth

public int computeStringWidth​(

SynthContext

ss,

Font

font,

FontMetrics

metrics,

String

text)

Returns the size of the passed in string.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the minimum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the minimum size needed to properly render an icon and text.

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the minimum size needed to properly render an icon and text.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the maximum size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the maximum size needed to properly render an icon and text.

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the maximum size needed to properly render an icon and text.

getMaximumCharHeight

```java
public int getMaximumCharHeight​(
SynthContext
context)
```

Returns the maximum height of the Font from the passed in
SynthContext.

**Parameters:** context

- SynthContext used to determine font.
**Returns:** maximum height of the characters for the font from the passed
in context.

---

#### getMaximumCharHeight

public int getMaximumCharHeight​(

SynthContext

context)

Returns the maximum height of the Font from the passed in
SynthContext.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
SynthContext
ss,

Font
font,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)
```

Returns the preferred size needed to properly render an icon and text.

**Parameters:** ss

- SynthContext
**Parameters:** font

- Font to use
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Returns:** the preferred size needed to properly render an icon and text.

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

SynthContext

ss,

Font

font,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex)

Returns the preferred size needed to properly render an icon and text.

paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Rectangle
bounds,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** bounds

- Bounds of the text to be drawn.
**Parameters:** mnemonicIndex

- Index to draw string at.

---

#### paintText

public void paintText​(

SynthContext

ss,

Graphics

g,

String

text,

Rectangle

bounds,
int mnemonicIndex)

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,
int x,
int y,
int mnemonicIndex)
```

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics used to render string in.
**Parameters:** text

- Text to render
**Parameters:** x

- X location to draw text at.
**Parameters:** y

- Upper left corner to draw text at.
**Parameters:** mnemonicIndex

- Index to draw string at.

---

#### paintText

public void paintText​(

SynthContext

ss,

Graphics

g,

String

text,
int x,
int y,
int mnemonicIndex)

Paints text at the specified location. This will not attempt to
render the text as html nor will it offset by the insets of the
component.

paintText

```java
public void paintText​(
SynthContext
ss,

Graphics
g,

String
text,

Icon
icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)
```

Paints an icon and text. This will render the text as html, if
necessary, and offset the location by the insets of the component.

**Parameters:** ss

- SynthContext
**Parameters:** g

- Graphics to render string and icon into
**Parameters:** text

- Text to layout
**Parameters:** icon

- Icon to layout
**Parameters:** hAlign

- horizontal alignment
**Parameters:** vAlign

- vertical alignment
**Parameters:** hTextPosition

- horizontal text position
**Parameters:** vTextPosition

- vertical text position
**Parameters:** iconTextGap

- gap between icon and text
**Parameters:** mnemonicIndex

- Index into text to render the mnemonic at, -1
indicates no mnemonic.
**Parameters:** textOffset

- Amount to offset the text when painting

---

#### paintText

public void paintText​(

SynthContext

ss,

Graphics

g,

String

text,

Icon

icon,
int hAlign,
int vAlign,
int hTextPosition,
int vTextPosition,
int iconTextGap,
int mnemonicIndex,
int textOffset)

Paints an icon and text. This will render the text as html, if
necessary, and offset the location by the insets of the component.

getIconWidth

```java
public static int getIconWidth​(
Icon
icon,

SynthContext
context)
```

Returns the icon's width.
The

getIconWidth(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the width of the icon.

---

#### getIconWidth

public static int getIconWidth​(

Icon

icon,

SynthContext

context)

Returns the icon's width.
The

getIconWidth(context)

method is called for

SynthIcon

.

getIconHeight

```java
public static int getIconHeight​(
Icon
icon,

SynthContext
context)
```

Returns the icon's height.
The

getIconHeight(context)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

-

SynthContext

requesting the icon, may be null.
**Returns:** an int specifying the height of the icon.

---

#### getIconHeight

public static int getIconHeight​(

Icon

icon,

SynthContext

context)

Returns the icon's height.
The

getIconHeight(context)

method is called for

SynthIcon

.

paintIcon

```java
public static void paintIcon​(
Icon
icon,

SynthContext
context,

Graphics
g,
int x,
int y,
int width,
int height)
```

Paints the icon. The

paintIcon(context, g, x, y, width, height)

method is called for

SynthIcon

.

**Parameters:** icon

- the icon
**Parameters:** context

- identifies hosting region, may be null.
**Parameters:** g

- the graphics context
**Parameters:** x

- the x location to paint to
**Parameters:** y

- the y location to paint to
**Parameters:** width

- the width of the region to paint to, may be 0
**Parameters:** height

- the height of the region to paint to, may be 0

---

#### paintIcon

public static void paintIcon​(

Icon

icon,

SynthContext

context,

Graphics

g,
int x,
int y,
int width,
int height)

Paints the icon. The

paintIcon(context, g, x, y, width, height)

method is called for

SynthIcon

.

---

