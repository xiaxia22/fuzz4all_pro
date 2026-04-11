# Class DebugGraphics

**Source:** `java.desktop\javax\swing\DebugGraphics.html`

### Class Description

```java
public class
DebugGraphics

extends
Graphics
```

Graphics subclass supporting graphics debugging. Overrides most methods
from Graphics. DebugGraphics objects are rarely created by hand. They
are most frequently created automatically when a JComponent's
debugGraphicsOptions are changed using the setDebugGraphicsOptions()
method.

NOTE: You must turn off double buffering to use DebugGraphics:
RepaintManager repaintManager = RepaintManager.currentManager(component);
repaintManager.setDoubleBufferingEnabled(false);

**Since:** 1.2
**See Also:** JComponent.setDebugGraphicsOptions(int)

,

RepaintManager.currentManager(java.awt.Component)

,

RepaintManager.setDoubleBufferingEnabled(boolean)

---

### Field Details

#### public static final int LOG_OPTION

Log graphics operations.

**See Also:**
- Constant Field Values

---

#### public static final int FLASH_OPTION

Flash graphics operations.

**See Also:**
- Constant Field Values

---

#### public static final int BUFFERED_OPTION

Show buffered operations in a separate

Frame

.

**See Also:**
- Constant Field Values

---

#### public static final int NONE_OPTION

Don't debug graphics operations.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public DebugGraphics()

Constructs a new debug graphics context that supports slowed
down drawing.

---

#### public DebugGraphics​(
Graphics
graphics,

JComponent
component)

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

**Parameters:**
- graphics

- the Graphics context to slow down
- component

- the JComponent to draw slowly

---

#### public DebugGraphics​(
Graphics
graphics)

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

**Parameters:**
- graphics

- the Graphics context to slow down

---

### Method Details

#### public
Graphics
create()

Overrides

Graphics.create

to return a DebugGraphics object.

**Specified by:**
- create

in class

Graphics

**Returns:**
- a new graphics context that is a copy of
this graphics context.

---

#### public
Graphics
create​(int x,
int y,
int width,
int height)

Overrides

Graphics.create

to return a DebugGraphics object.

**Overrides:**
- create

in class

Graphics

**Parameters:**
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- width

- the width of the clipping rectangle.
- height

- the height of the clipping rectangle.

**Returns:**
- a new graphics context.

**See Also:**
- Graphics.translate(int, int)

,

Graphics.clipRect(int, int, int, int)

---

#### public static void setFlashColor​(
Color
flashColor)

Sets the Color used to flash drawing operations.

**Parameters:**
- flashColor

- the Color used to flash drawing operations

---

#### public static
Color
flashColor()

Returns the Color used to flash drawing operations.

**Returns:**
- the Color used to flash drawing operations

**See Also:**
- setFlashColor(java.awt.Color)

---

#### public static void setFlashTime​(int flashTime)

Sets the time delay of drawing operation flashing.

**Parameters:**
- flashTime

- the time delay of drawing operation flashing

---

#### public static int flashTime()

Returns the time delay of drawing operation flashing.

**Returns:**
- the time delay of drawing operation flashing

**See Also:**
- setFlashTime(int)

---

#### public static void setFlashCount​(int flashCount)

Sets the number of times that drawing operations will flash.

**Parameters:**
- flashCount

- number of times that drawing operations will flash

---

#### public static int flashCount()

Returns the number of times that drawing operations will flash.

**Returns:**
- the number of times that drawing operations will flash

**See Also:**
- setFlashCount(int)

---

#### public static void setLogStream​(
PrintStream
stream)

Sets the stream to which the DebugGraphics logs drawing operations.

**Parameters:**
- stream

- the stream to which the DebugGraphics logs drawing operations

---

#### public static
PrintStream
logStream()

Returns the stream to which the DebugGraphics logs drawing operations.

**Returns:**
- the stream to which the DebugGraphics logs drawing operations

**See Also:**
- setLogStream(java.io.PrintStream)

---

#### public void setFont​(
Font
aFont)

Sets the Font used for text drawing operations.

**Specified by:**
- setFont

in class

Graphics

**Parameters:**
- aFont

- the font.

**See Also:**
- Graphics.getFont()

,

Graphics.drawString(java.lang.String, int, int)

,

Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### public
Font
getFont()

Returns the Font used for text drawing operations.

**Specified by:**
- getFont

in class

Graphics

**Returns:**
- this graphics context's current font.

**See Also:**
- setFont(java.awt.Font)

---

#### public void setColor​(
Color
aColor)

Sets the color to be used for drawing and filling lines and shapes.

**Specified by:**
- setColor

in class

Graphics

**Parameters:**
- aColor

- the new rendering color.

**See Also:**
- Color

,

Graphics.getColor()

---

#### public
Color
getColor()

Returns the Color used for text drawing operations.

**Specified by:**
- getColor

in class

Graphics

**Returns:**
- this graphics context's current color.

**See Also:**
- setColor(java.awt.Color)

---

#### public
FontMetrics
getFontMetrics()

Overrides

Graphics.getFontMetrics

.

**Overrides:**
- getFontMetrics

in class

Graphics

**Returns:**
- the font metrics of this graphics
context's current font.

**See Also:**
- Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics(Font)

---

#### public
FontMetrics
getFontMetrics​(
Font
f)

Overrides

Graphics.getFontMetrics

.

**Specified by:**
- getFontMetrics

in class

Graphics

**Parameters:**
- f

- the specified font

**Returns:**
- the font metrics for the specified font.

**See Also:**
- Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics()

---

#### public void translate​(int x,
int y)

Overrides

Graphics.translate

.

**Specified by:**
- translate

in class

Graphics

**Parameters:**
- x

- the

x

coordinate.
- y

- the

y

coordinate.

---

#### public void setPaintMode()

Overrides

Graphics.setPaintMode

.

**Specified by:**
- setPaintMode

in class

Graphics

---

#### public void setXORMode​(
Color
aColor)

Overrides

Graphics.setXORMode

.

**Specified by:**
- setXORMode

in class

Graphics

**Parameters:**
- aColor

- the XOR alternation color

---

#### public
Rectangle
getClipBounds()

Overrides

Graphics.getClipBounds

.

**Specified by:**
- getClipBounds

in class

Graphics

**Returns:**
- the bounding rectangle of the current clipping area,
or

null

if no clip is set.

**See Also:**
- Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### public void clipRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.clipRect

.

**Specified by:**
- clipRect

in class

Graphics

**Parameters:**
- x

- the x coordinate of the rectangle to intersect the clip with
- y

- the y coordinate of the rectangle to intersect the clip with
- width

- the width of the rectangle to intersect the clip with
- height

- the height of the rectangle to intersect the clip with

**See Also:**
- Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### public void setClip​(int x,
int y,
int width,
int height)

Overrides

Graphics.setClip

.

**Specified by:**
- setClip

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the new clip rectangle.
- y

- the

y

coordinate of the new clip rectangle.
- width

- the width of the new clip rectangle.
- height

- the height of the new clip rectangle.

**See Also:**
- Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(Shape)

,

Graphics.getClip()

---

#### public
Shape
getClip()

Overrides

Graphics.getClip

.

**Specified by:**
- getClip

in class

Graphics

**Returns:**
- a

Shape

object representing the
current clipping area, or

null

if
no clip is set.

**See Also:**
- Graphics.getClipBounds()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### public void setClip​(
Shape
clip)

Overrides

Graphics.setClip

.

**Specified by:**
- setClip

in class

Graphics

**Parameters:**
- clip

- the

Shape

to use to set the clip

**See Also:**
- Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

---

#### public void drawRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawRect

.

**Overrides:**
- drawRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate
of the rectangle to be drawn.
- y

- the

y

coordinate
of the rectangle to be drawn.
- width

- the width of the rectangle to be drawn.
- height

- the height of the rectangle to be drawn.

**See Also:**
- Graphics.fillRect(int, int, int, int)

,

Graphics.clearRect(int, int, int, int)

---

#### public void fillRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillRect

.

**Specified by:**
- fillRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate
of the rectangle to be filled.
- y

- the

y

coordinate
of the rectangle to be filled.
- width

- the width of the rectangle to be filled.
- height

- the height of the rectangle to be filled.

**See Also:**
- Graphics.clearRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

---

#### public void clearRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.clearRect

.

**Specified by:**
- clearRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the rectangle to clear.
- y

- the

y

coordinate of the rectangle to clear.
- width

- the width of the rectangle to clear.
- height

- the height of the rectangle to clear.

**See Also:**
- Graphics.fillRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

,

Graphics.setColor(java.awt.Color)

,

Graphics.setPaintMode()

,

Graphics.setXORMode(java.awt.Color)

---

#### public void drawRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.drawRoundRect

.

**Specified by:**
- drawRoundRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the rectangle to be drawn.
- y

- the

y

coordinate of the rectangle to be drawn.
- width

- the width of the rectangle to be drawn.
- height

- the height of the rectangle to be drawn.
- arcWidth

- the horizontal diameter of the arc
at the four corners.
- arcHeight

- the vertical diameter of the arc
at the four corners.

**See Also:**
- Graphics.fillRoundRect(int, int, int, int, int, int)

---

#### public void fillRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.fillRoundRect

.

**Specified by:**
- fillRoundRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the rectangle to be filled.
- y

- the

y

coordinate of the rectangle to be filled.
- width

- the width of the rectangle to be filled.
- height

- the height of the rectangle to be filled.
- arcWidth

- the horizontal diameter
of the arc at the four corners.
- arcHeight

- the vertical diameter
of the arc at the four corners.

**See Also:**
- Graphics.drawRoundRect(int, int, int, int, int, int)

---

#### public void drawLine​(int x1,
int y1,
int x2,
int y2)

Overrides

Graphics.drawLine

.

**Specified by:**
- drawLine

in class

Graphics

**Parameters:**
- x1

- the first point's

x

coordinate.
- y1

- the first point's

y

coordinate.
- x2

- the second point's

x

coordinate.
- y2

- the second point's

y

coordinate.

---

#### public void draw3DRect​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.draw3DRect

.

**Overrides:**
- draw3DRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the rectangle to be drawn.
- y

- the

y

coordinate of the rectangle to be drawn.
- width

- the width of the rectangle to be drawn.
- height

- the height of the rectangle to be drawn.
- raised

- a boolean that determines whether the rectangle
appears to be raised above the surface
or sunk into the surface.

**See Also:**
- Graphics.fill3DRect(int, int, int, int, boolean)

---

#### public void fill3DRect​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.fill3DRect

.

**Overrides:**
- fill3DRect

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the rectangle to be filled.
- y

- the

y

coordinate of the rectangle to be filled.
- width

- the width of the rectangle to be filled.
- height

- the height of the rectangle to be filled.
- raised

- a boolean value that determines whether the
rectangle appears to be raised above the surface
or etched into the surface.

**See Also:**
- Graphics.draw3DRect(int, int, int, int, boolean)

---

#### public void drawOval​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawOval

.

**Specified by:**
- drawOval

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the upper left
corner of the oval to be drawn.
- y

- the

y

coordinate of the upper left
corner of the oval to be drawn.
- width

- the width of the oval to be drawn.
- height

- the height of the oval to be drawn.

**See Also:**
- Graphics.fillOval(int, int, int, int)

---

#### public void fillOval​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillOval

.

**Specified by:**
- fillOval

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the upper left corner
of the oval to be filled.
- y

- the

y

coordinate of the upper left corner
of the oval to be filled.
- width

- the width of the oval to be filled.
- height

- the height of the oval to be filled.

**See Also:**
- Graphics.drawOval(int, int, int, int)

---

#### public void drawArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.drawArc

.

**Specified by:**
- drawArc

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the
upper-left corner of the arc to be drawn.
- y

- the

y

coordinate of the
upper-left corner of the arc to be drawn.
- width

- the width of the arc to be drawn.
- height

- the height of the arc to be drawn.
- startAngle

- the beginning angle.
- arcAngle

- the angular extent of the arc,
relative to the start angle.

**See Also:**
- Graphics.fillArc(int, int, int, int, int, int)

---

#### public void fillArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.fillArc

.

**Specified by:**
- fillArc

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the
upper-left corner of the arc to be filled.
- y

- the

y

coordinate of the
upper-left corner of the arc to be filled.
- width

- the width of the arc to be filled.
- height

- the height of the arc to be filled.
- startAngle

- the beginning angle.
- arcAngle

- the angular extent of the arc,
relative to the start angle.

**See Also:**
- Graphics.drawArc(int, int, int, int, int, int)

---

#### public void drawPolyline​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolyline

.

**Specified by:**
- drawPolyline

in class

Graphics

**Parameters:**
- xPoints

- an array of

x

points
- yPoints

- an array of

y

points
- nPoints

- the total number of points

**See Also:**
- Graphics.drawPolygon(int[], int[], int)

---

#### public void drawPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolygon

.

**Specified by:**
- drawPolygon

in class

Graphics

**Parameters:**
- xPoints

- a an array of

x

coordinates.
- yPoints

- a an array of

y

coordinates.
- nPoints

- a the total number of points.

**See Also:**
- Graphics.fillPolygon(int[], int[], int)

,

Graphics.drawPolyline(int[], int[], int)

---

#### public void fillPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.fillPolygon

.

**Specified by:**
- fillPolygon

in class

Graphics

**Parameters:**
- xPoints

- a an array of

x

coordinates.
- yPoints

- a an array of

y

coordinates.
- nPoints

- a the total number of points.

**See Also:**
- Graphics.drawPolygon(int[], int[], int)

---

#### public void drawString​(
String
aString,
int x,
int y)

Overrides

Graphics.drawString

.

**Specified by:**
- drawString

in class

Graphics

**Parameters:**
- aString

- the string to be drawn.
- x

- the

x

coordinate.
- y

- the

y

coordinate.

**See Also:**
- Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### public void drawString​(
AttributedCharacterIterator
iterator,
int x,
int y)

Overrides

Graphics.drawString

.

**Specified by:**
- drawString

in class

Graphics

**Parameters:**
- iterator

- the iterator whose text is to be drawn
- x

- the

x

coordinate.
- y

- the

y

coordinate.

**See Also:**
- Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### public void drawBytes​(byte[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawBytes

.

**Overrides:**
- drawBytes

in class

Graphics

**Parameters:**
- data

- the data to be drawn
- offset

- the start offset in the data
- length

- the number of bytes that are drawn
- x

- the

x

coordinate of the baseline of the text
- y

- the

y

coordinate of the baseline of the text

**See Also:**
- Graphics.drawChars(char[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

---

#### public void drawChars​(char[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawChars

.

**Overrides:**
- drawChars

in class

Graphics

**Parameters:**
- data

- the array of characters to be drawn
- offset

- the start offset in the data
- length

- the number of characters to be drawn
- x

- the

x

coordinate of the baseline of the text
- y

- the

y

coordinate of the baseline of the text

**See Also:**
- Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

---

#### public boolean drawImage​(
Image
img,
int x,
int y,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- observer

- object to be notified as more of
the image is converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- width

- the width of the rectangle.
- height

- the height of the rectangle.
- observer

- object to be notified as more of
the image is converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public boolean drawImage​(
Image
img,
int x,
int y,

Color
bgcolor,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- bgcolor

- the background color to paint under the
non-opaque portions of the image.
- observer

- object to be notified as more of
the image is converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

Color
bgcolor,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- x

- the

x

coordinate.
- y

- the

y

coordinate.
- width

- the width of the rectangle.
- height

- the height of the rectangle.
- bgcolor

- the background color to paint under the
non-opaque portions of the image.
- observer

- object to be notified as more of
the image is converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- dx1

- the

x

coordinate of the first corner of the
destination rectangle.
- dy1

- the

y

coordinate of the first corner of the
destination rectangle.
- dx2

- the

x

coordinate of the second corner of the
destination rectangle.
- dy2

- the

y

coordinate of the second corner of the
destination rectangle.
- sx1

- the

x

coordinate of the first corner of the
source rectangle.
- sy1

- the

y

coordinate of the first corner of the
source rectangle.
- sx2

- the

x

coordinate of the second corner of the
source rectangle.
- sy2

- the

y

coordinate of the second corner of the
source rectangle.
- observer

- object to be notified as more of the image is
scaled and converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color
bgcolor,

ImageObserver
observer)

Overrides

Graphics.drawImage

.

**Specified by:**
- drawImage

in class

Graphics

**Parameters:**
- img

- the specified image to be drawn. This method does
nothing if

img

is null.
- dx1

- the

x

coordinate of the first corner of the
destination rectangle.
- dy1

- the

y

coordinate of the first corner of the
destination rectangle.
- dx2

- the

x

coordinate of the second corner of the
destination rectangle.
- dy2

- the

y

coordinate of the second corner of the
destination rectangle.
- sx1

- the

x

coordinate of the first corner of the
source rectangle.
- sy1

- the

y

coordinate of the first corner of the
source rectangle.
- sx2

- the

x

coordinate of the second corner of the
source rectangle.
- sy2

- the

y

coordinate of the second corner of the
source rectangle.
- bgcolor

- the background color to paint under the
non-opaque portions of the image.
- observer

- object to be notified as more of the image is
scaled and converted.

**Returns:**
- false

if the image pixels are still changing;

true

otherwise.

**See Also:**
- Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### public void copyArea​(int x,
int y,
int width,
int height,
int destX,
int destY)

Overrides

Graphics.copyArea

.

**Specified by:**
- copyArea

in class

Graphics

**Parameters:**
- x

- the

x

coordinate of the source rectangle.
- y

- the

y

coordinate of the source rectangle.
- width

- the width of the source rectangle.
- height

- the height of the source rectangle.
- destX

- the horizontal distance to copy the pixels.
- destY

- the vertical distance to copy the pixels.

---

#### public void dispose()

Overrides

Graphics.dispose

.

**Specified by:**
- dispose

in class

Graphics

**See Also:**
- Graphics.finalize()

,

Component.paint(java.awt.Graphics)

,

Component.update(java.awt.Graphics)

,

Component.getGraphics()

,

Graphics.create()

---

#### public boolean isDrawingBuffer()

Returns the drawingBuffer value.

**Returns:**
- true if this object is drawing from a Buffer

---

#### public void setDebugOptions​(int options)

Enables/disables diagnostic information about every graphics
operation. The value of

options

indicates how this information
should be displayed. LOG_OPTION causes a text message to be printed.
FLASH_OPTION causes the drawing to flash several times. BUFFERED_OPTION
creates a new Frame that shows each operation on an
offscreen buffer. The value of

options

is bitwise OR'd into
the current value. To disable debugging use NONE_OPTION.

**Parameters:**
- options

- indicates how diagnostic information should be displayed

---

#### public int getDebugOptions()

Returns the current debugging options for this DebugGraphics.

**Returns:**
- the current debugging options for this DebugGraphics

**See Also:**
- setDebugOptions(int)

---

### Additional Sections

#### Class DebugGraphics

java.lang.Object

- java.awt.Graphics
- - javax.swing.DebugGraphics

java.awt.Graphics

- javax.swing.DebugGraphics

javax.swing.DebugGraphics

```java
public class
DebugGraphics

extends
Graphics
```

Graphics subclass supporting graphics debugging. Overrides most methods
from Graphics. DebugGraphics objects are rarely created by hand. They
are most frequently created automatically when a JComponent's
debugGraphicsOptions are changed using the setDebugGraphicsOptions()
method.

NOTE: You must turn off double buffering to use DebugGraphics:
RepaintManager repaintManager = RepaintManager.currentManager(component);
repaintManager.setDoubleBufferingEnabled(false);

**Since:** 1.2
**See Also:** JComponent.setDebugGraphicsOptions(int)

,

RepaintManager.currentManager(java.awt.Component)

,

RepaintManager.setDoubleBufferingEnabled(boolean)

public class

DebugGraphics

extends

Graphics

Graphics subclass supporting graphics debugging. Overrides most methods
from Graphics. DebugGraphics objects are rarely created by hand. They
are most frequently created automatically when a JComponent's
debugGraphicsOptions are changed using the setDebugGraphicsOptions()
method.

NOTE: You must turn off double buffering to use DebugGraphics:
RepaintManager repaintManager = RepaintManager.currentManager(component);
repaintManager.setDoubleBufferingEnabled(false);

NOTE: You must turn off double buffering to use DebugGraphics:
RepaintManager repaintManager = RepaintManager.currentManager(component);
repaintManager.setDoubleBufferingEnabled(false);

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

BUFFERED_OPTION

Show buffered operations in a separate

Frame

.

static int

FLASH_OPTION

Flash graphics operations.

static int

LOG_OPTION

Log graphics operations.

static int

NONE_OPTION

Don't debug graphics operations.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DebugGraphics

()

Constructs a new debug graphics context that supports slowed
down drawing.

DebugGraphics

​(

Graphics

graphics)

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

DebugGraphics

​(

Graphics

graphics,

JComponent

component)

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.clearRect

.

void

clipRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.clipRect

.

void

copyArea

​(int x,
int y,
int width,
int height,
int destX,
int destY)

Overrides

Graphics.copyArea

.

Graphics

create

()

Overrides

Graphics.create

to return a DebugGraphics object.

Graphics

create

​(int x,
int y,
int width,
int height)

Overrides

Graphics.create

to return a DebugGraphics object.

void

dispose

()

Overrides

Graphics.dispose

.

void

draw3DRect

​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.draw3DRect

.

void

drawArc

​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.drawArc

.

void

drawBytes

​(byte[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawBytes

.

void

drawChars

​(char[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawChars

.

boolean

drawImage

​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,
int width,
int height,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,
int width,
int height,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

void

drawLine

​(int x1,
int y1,
int x2,
int y2)

Overrides

Graphics.drawLine

.

void

drawOval

​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawOval

.

void

drawPolygon

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolygon

.

void

drawPolyline

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolyline

.

void

drawRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawRect

.

void

drawRoundRect

​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.drawRoundRect

.

void

drawString

​(

String

aString,
int x,
int y)

Overrides

Graphics.drawString

.

void

drawString

​(

AttributedCharacterIterator

iterator,
int x,
int y)

Overrides

Graphics.drawString

.

void

fill3DRect

​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.fill3DRect

.

void

fillArc

​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.fillArc

.

void

fillOval

​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillOval

.

void

fillPolygon

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.fillPolygon

.

void

fillRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillRect

.

void

fillRoundRect

​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.fillRoundRect

.

static

Color

flashColor

()

Returns the Color used to flash drawing operations.

static int

flashCount

()

Returns the number of times that drawing operations will flash.

static int

flashTime

()

Returns the time delay of drawing operation flashing.

Shape

getClip

()

Overrides

Graphics.getClip

.

Rectangle

getClipBounds

()

Overrides

Graphics.getClipBounds

.

Color

getColor

()

Returns the Color used for text drawing operations.

int

getDebugOptions

()

Returns the current debugging options for this DebugGraphics.

Font

getFont

()

Returns the Font used for text drawing operations.

FontMetrics

getFontMetrics

()

Overrides

Graphics.getFontMetrics

.

FontMetrics

getFontMetrics

​(

Font

f)

Overrides

Graphics.getFontMetrics

.

boolean

isDrawingBuffer

()

Returns the drawingBuffer value.

static

PrintStream

logStream

()

Returns the stream to which the DebugGraphics logs drawing operations.

void

setClip

​(int x,
int y,
int width,
int height)

Overrides

Graphics.setClip

.

void

setClip

​(

Shape

clip)

Overrides

Graphics.setClip

.

void

setColor

​(

Color

aColor)

Sets the color to be used for drawing and filling lines and shapes.

void

setDebugOptions

​(int options)

Enables/disables diagnostic information about every graphics
operation.

static void

setFlashColor

​(

Color

flashColor)

Sets the Color used to flash drawing operations.

static void

setFlashCount

​(int flashCount)

Sets the number of times that drawing operations will flash.

static void

setFlashTime

​(int flashTime)

Sets the time delay of drawing operation flashing.

void

setFont

​(

Font

aFont)

Sets the Font used for text drawing operations.

static void

setLogStream

​(

PrintStream

stream)

Sets the stream to which the DebugGraphics logs drawing operations.

void

setPaintMode

()

Overrides

Graphics.setPaintMode

.

void

setXORMode

​(

Color

aColor)

Overrides

Graphics.setXORMode

.

void

translate

​(int x,
int y)

Overrides

Graphics.translate

.

- Methods declared in class java.awt.

Graphics

drawPolygon

,

fillPolygon

,

finalize

,

getClipBounds

,

getClipRect

,

hitClip

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

getClass

,

hashCode

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

static int

BUFFERED_OPTION

Show buffered operations in a separate

Frame

.

static int

FLASH_OPTION

Flash graphics operations.

static int

LOG_OPTION

Log graphics operations.

static int

NONE_OPTION

Don't debug graphics operations.

---

#### Field Summary

Show buffered operations in a separate

Frame

.

Flash graphics operations.

Log graphics operations.

Don't debug graphics operations.

Constructor Summary

Constructors

Constructor

Description

DebugGraphics

()

Constructs a new debug graphics context that supports slowed
down drawing.

DebugGraphics

​(

Graphics

graphics)

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

DebugGraphics

​(

Graphics

graphics,

JComponent

component)

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

---

#### Constructor Summary

Constructs a new debug graphics context that supports slowed
down drawing.

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

clearRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.clearRect

.

void

clipRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.clipRect

.

void

copyArea

​(int x,
int y,
int width,
int height,
int destX,
int destY)

Overrides

Graphics.copyArea

.

Graphics

create

()

Overrides

Graphics.create

to return a DebugGraphics object.

Graphics

create

​(int x,
int y,
int width,
int height)

Overrides

Graphics.create

to return a DebugGraphics object.

void

dispose

()

Overrides

Graphics.dispose

.

void

draw3DRect

​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.draw3DRect

.

void

drawArc

​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.drawArc

.

void

drawBytes

​(byte[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawBytes

.

void

drawChars

​(char[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawChars

.

boolean

drawImage

​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,
int width,
int height,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,
int width,
int height,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

boolean

drawImage

​(

Image

img,
int x,
int y,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

void

drawLine

​(int x1,
int y1,
int x2,
int y2)

Overrides

Graphics.drawLine

.

void

drawOval

​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawOval

.

void

drawPolygon

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolygon

.

void

drawPolyline

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolyline

.

void

drawRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawRect

.

void

drawRoundRect

​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.drawRoundRect

.

void

drawString

​(

String

aString,
int x,
int y)

Overrides

Graphics.drawString

.

void

drawString

​(

AttributedCharacterIterator

iterator,
int x,
int y)

Overrides

Graphics.drawString

.

void

fill3DRect

​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.fill3DRect

.

void

fillArc

​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.fillArc

.

void

fillOval

​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillOval

.

void

fillPolygon

​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.fillPolygon

.

void

fillRect

​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillRect

.

void

fillRoundRect

​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.fillRoundRect

.

static

Color

flashColor

()

Returns the Color used to flash drawing operations.

static int

flashCount

()

Returns the number of times that drawing operations will flash.

static int

flashTime

()

Returns the time delay of drawing operation flashing.

Shape

getClip

()

Overrides

Graphics.getClip

.

Rectangle

getClipBounds

()

Overrides

Graphics.getClipBounds

.

Color

getColor

()

Returns the Color used for text drawing operations.

int

getDebugOptions

()

Returns the current debugging options for this DebugGraphics.

Font

getFont

()

Returns the Font used for text drawing operations.

FontMetrics

getFontMetrics

()

Overrides

Graphics.getFontMetrics

.

FontMetrics

getFontMetrics

​(

Font

f)

Overrides

Graphics.getFontMetrics

.

boolean

isDrawingBuffer

()

Returns the drawingBuffer value.

static

PrintStream

logStream

()

Returns the stream to which the DebugGraphics logs drawing operations.

void

setClip

​(int x,
int y,
int width,
int height)

Overrides

Graphics.setClip

.

void

setClip

​(

Shape

clip)

Overrides

Graphics.setClip

.

void

setColor

​(

Color

aColor)

Sets the color to be used for drawing and filling lines and shapes.

void

setDebugOptions

​(int options)

Enables/disables diagnostic information about every graphics
operation.

static void

setFlashColor

​(

Color

flashColor)

Sets the Color used to flash drawing operations.

static void

setFlashCount

​(int flashCount)

Sets the number of times that drawing operations will flash.

static void

setFlashTime

​(int flashTime)

Sets the time delay of drawing operation flashing.

void

setFont

​(

Font

aFont)

Sets the Font used for text drawing operations.

static void

setLogStream

​(

PrintStream

stream)

Sets the stream to which the DebugGraphics logs drawing operations.

void

setPaintMode

()

Overrides

Graphics.setPaintMode

.

void

setXORMode

​(

Color

aColor)

Overrides

Graphics.setXORMode

.

void

translate

​(int x,
int y)

Overrides

Graphics.translate

.

- Methods declared in class java.awt.

Graphics

drawPolygon

,

fillPolygon

,

finalize

,

getClipBounds

,

getClipRect

,

hitClip

,

toString

- Methods declared in class java.lang.

Object

clone

,

equals

,

getClass

,

hashCode

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

Overrides

Graphics.clearRect

.

Overrides

Graphics.clipRect

.

Overrides

Graphics.copyArea

.

Overrides

Graphics.create

to return a DebugGraphics object.

Overrides

Graphics.dispose

.

Overrides

Graphics.draw3DRect

.

Overrides

Graphics.drawArc

.

Overrides

Graphics.drawBytes

.

Overrides

Graphics.drawChars

.

Overrides

Graphics.drawImage

.

Overrides

Graphics.drawLine

.

Overrides

Graphics.drawOval

.

Overrides

Graphics.drawPolygon

.

Overrides

Graphics.drawPolyline

.

Overrides

Graphics.drawRect

.

Overrides

Graphics.drawRoundRect

.

Overrides

Graphics.drawString

.

Overrides

Graphics.fill3DRect

.

Overrides

Graphics.fillArc

.

Overrides

Graphics.fillOval

.

Overrides

Graphics.fillPolygon

.

Overrides

Graphics.fillRect

.

Overrides

Graphics.fillRoundRect

.

Returns the Color used to flash drawing operations.

Returns the number of times that drawing operations will flash.

Returns the time delay of drawing operation flashing.

Overrides

Graphics.getClip

.

Overrides

Graphics.getClipBounds

.

Returns the Color used for text drawing operations.

Returns the current debugging options for this DebugGraphics.

Returns the Font used for text drawing operations.

Overrides

Graphics.getFontMetrics

.

Returns the drawingBuffer value.

Returns the stream to which the DebugGraphics logs drawing operations.

Overrides

Graphics.setClip

.

Sets the color to be used for drawing and filling lines and shapes.

Enables/disables diagnostic information about every graphics
operation.

Sets the Color used to flash drawing operations.

Sets the number of times that drawing operations will flash.

Sets the time delay of drawing operation flashing.

Sets the Font used for text drawing operations.

Sets the stream to which the DebugGraphics logs drawing operations.

Overrides

Graphics.setPaintMode

.

Overrides

Graphics.setXORMode

.

Overrides

Graphics.translate

.

Methods declared in class java.awt.

Graphics

drawPolygon

,

fillPolygon

,

finalize

,

getClipBounds

,

getClipRect

,

hitClip

,

toString

---

#### Methods declared in class java.awt. Graphics

Methods declared in class java.lang.

Object

clone

,

equals

,

getClass

,

hashCode

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

- LOG_OPTION

```java
public static final int LOG_OPTION
```

Log graphics operations.

**See Also:** Constant Field Values

- FLASH_OPTION

```java
public static final int FLASH_OPTION
```

Flash graphics operations.

**See Also:** Constant Field Values

- BUFFERED_OPTION

```java
public static final int BUFFERED_OPTION
```

Show buffered operations in a separate

Frame

.

**See Also:** Constant Field Values

- NONE_OPTION

```java
public static final int NONE_OPTION
```

Don't debug graphics operations.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DebugGraphics

```java
public DebugGraphics()
```

Constructs a new debug graphics context that supports slowed
down drawing.

- DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics,

JComponent
component)
```

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

**Parameters:** graphics

- the Graphics context to slow down
**Parameters:** component

- the JComponent to draw slowly

- DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics)
```

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

**Parameters:** graphics

- the Graphics context to slow down

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public
Graphics
create()
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Specified by:** create

in class

Graphics
**Returns:** a new graphics context that is a copy of
this graphics context.

- create

```java
public
Graphics
create​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Overrides:** create

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the clipping rectangle.
**Parameters:** height

- the height of the clipping rectangle.
**Returns:** a new graphics context.
**See Also:** Graphics.translate(int, int)

,

Graphics.clipRect(int, int, int, int)

- setFlashColor

```java
public static void setFlashColor​(
Color
flashColor)
```

Sets the Color used to flash drawing operations.

**Parameters:** flashColor

- the Color used to flash drawing operations

- flashColor

```java
public static
Color
flashColor()
```

Returns the Color used to flash drawing operations.

**Returns:** the Color used to flash drawing operations
**See Also:** setFlashColor(java.awt.Color)

- setFlashTime

```java
public static void setFlashTime​(int flashTime)
```

Sets the time delay of drawing operation flashing.

**Parameters:** flashTime

- the time delay of drawing operation flashing

- flashTime

```java
public static int flashTime()
```

Returns the time delay of drawing operation flashing.

**Returns:** the time delay of drawing operation flashing
**See Also:** setFlashTime(int)

- setFlashCount

```java
public static void setFlashCount​(int flashCount)
```

Sets the number of times that drawing operations will flash.

**Parameters:** flashCount

- number of times that drawing operations will flash

- flashCount

```java
public static int flashCount()
```

Returns the number of times that drawing operations will flash.

**Returns:** the number of times that drawing operations will flash
**See Also:** setFlashCount(int)

- setLogStream

```java
public static void setLogStream​(
PrintStream
stream)
```

Sets the stream to which the DebugGraphics logs drawing operations.

**Parameters:** stream

- the stream to which the DebugGraphics logs drawing operations

- logStream

```java
public static
PrintStream
logStream()
```

Returns the stream to which the DebugGraphics logs drawing operations.

**Returns:** the stream to which the DebugGraphics logs drawing operations
**See Also:** setLogStream(java.io.PrintStream)

- setFont

```java
public void setFont​(
Font
aFont)
```

Sets the Font used for text drawing operations.

**Specified by:** setFont

in class

Graphics
**Parameters:** aFont

- the font.
**See Also:** Graphics.getFont()

,

Graphics.drawString(java.lang.String, int, int)

,

Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- getFont

```java
public
Font
getFont()
```

Returns the Font used for text drawing operations.

**Specified by:** getFont

in class

Graphics
**Returns:** this graphics context's current font.
**See Also:** setFont(java.awt.Font)

- setColor

```java
public void setColor​(
Color
aColor)
```

Sets the color to be used for drawing and filling lines and shapes.

**Specified by:** setColor

in class

Graphics
**Parameters:** aColor

- the new rendering color.
**See Also:** Color

,

Graphics.getColor()

- getColor

```java
public
Color
getColor()
```

Returns the Color used for text drawing operations.

**Specified by:** getColor

in class

Graphics
**Returns:** this graphics context's current color.
**See Also:** setColor(java.awt.Color)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics()
```

Overrides

Graphics.getFontMetrics

.

**Overrides:** getFontMetrics

in class

Graphics
**Returns:** the font metrics of this graphics
context's current font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics(Font)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Overrides

Graphics.getFontMetrics

.

**Specified by:** getFontMetrics

in class

Graphics
**Parameters:** f

- the specified font
**Returns:** the font metrics for the specified font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics()

- translate

```java
public void translate​(int x,
int y)
```

Overrides

Graphics.translate

.

**Specified by:** translate

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.

- setPaintMode

```java
public void setPaintMode()
```

Overrides

Graphics.setPaintMode

.

**Specified by:** setPaintMode

in class

Graphics

- setXORMode

```java
public void setXORMode​(
Color
aColor)
```

Overrides

Graphics.setXORMode

.

**Specified by:** setXORMode

in class

Graphics
**Parameters:** aColor

- the XOR alternation color

- getClipBounds

```java
public
Rectangle
getClipBounds()
```

Overrides

Graphics.getClipBounds

.

**Specified by:** getClipBounds

in class

Graphics
**Returns:** the bounding rectangle of the current clipping area,
or

null

if no clip is set.
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- clipRect

```java
public void clipRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clipRect

.

**Specified by:** clipRect

in class

Graphics
**Parameters:** x

- the x coordinate of the rectangle to intersect the clip with
**Parameters:** y

- the y coordinate of the rectangle to intersect the clip with
**Parameters:** width

- the width of the rectangle to intersect the clip with
**Parameters:** height

- the height of the rectangle to intersect the clip with
**See Also:** Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- setClip

```java
public void setClip​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** x

- the

x

coordinate of the new clip rectangle.
**Parameters:** y

- the

y

coordinate of the new clip rectangle.
**Parameters:** width

- the width of the new clip rectangle.
**Parameters:** height

- the height of the new clip rectangle.
**See Also:** Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(Shape)

,

Graphics.getClip()

- getClip

```java
public
Shape
getClip()
```

Overrides

Graphics.getClip

.

**Specified by:** getClip

in class

Graphics
**Returns:** a

Shape

object representing the
current clipping area, or

null

if
no clip is set.
**See Also:** Graphics.getClipBounds()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- setClip

```java
public void setClip​(
Shape
clip)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** clip

- the

Shape

to use to set the clip
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

- drawRect

```java
public void drawRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawRect

.

**Overrides:** drawRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate
of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.clearRect(int, int, int, int)

- fillRect

```java
public void fillRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillRect

.

**Specified by:** fillRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate
of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**See Also:** Graphics.clearRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

- clearRect

```java
public void clearRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clearRect

.

**Specified by:** clearRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to clear.
**Parameters:** y

- the

y

coordinate of the rectangle to clear.
**Parameters:** width

- the width of the rectangle to clear.
**Parameters:** height

- the height of the rectangle to clear.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

,

Graphics.setColor(java.awt.Color)

,

Graphics.setPaintMode()

,

Graphics.setXORMode(java.awt.Color)

- drawRoundRect

```java
public void drawRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.drawRoundRect

.

**Specified by:** drawRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** arcWidth

- the horizontal diameter of the arc
at the four corners.
**Parameters:** arcHeight

- the vertical diameter of the arc
at the four corners.
**See Also:** Graphics.fillRoundRect(int, int, int, int, int, int)

- fillRoundRect

```java
public void fillRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.fillRoundRect

.

**Specified by:** fillRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** arcWidth

- the horizontal diameter
of the arc at the four corners.
**Parameters:** arcHeight

- the vertical diameter
of the arc at the four corners.
**See Also:** Graphics.drawRoundRect(int, int, int, int, int, int)

- drawLine

```java
public void drawLine​(int x1,
int y1,
int x2,
int y2)
```

Overrides

Graphics.drawLine

.

**Specified by:** drawLine

in class

Graphics
**Parameters:** x1

- the first point's

x

coordinate.
**Parameters:** y1

- the first point's

y

coordinate.
**Parameters:** x2

- the second point's

x

coordinate.
**Parameters:** y2

- the second point's

y

coordinate.

- draw3DRect

```java
public void draw3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.draw3DRect

.

**Overrides:** draw3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** raised

- a boolean that determines whether the rectangle
appears to be raised above the surface
or sunk into the surface.
**See Also:** Graphics.fill3DRect(int, int, int, int, boolean)

- fill3DRect

```java
public void fill3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.fill3DRect

.

**Overrides:** fill3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** raised

- a boolean value that determines whether the
rectangle appears to be raised above the surface
or etched into the surface.
**See Also:** Graphics.draw3DRect(int, int, int, int, boolean)

- drawOval

```java
public void drawOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawOval

.

**Specified by:** drawOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** y

- the

y

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** width

- the width of the oval to be drawn.
**Parameters:** height

- the height of the oval to be drawn.
**See Also:** Graphics.fillOval(int, int, int, int)

- fillOval

```java
public void fillOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillOval

.

**Specified by:** fillOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** y

- the

y

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** width

- the width of the oval to be filled.
**Parameters:** height

- the height of the oval to be filled.
**See Also:** Graphics.drawOval(int, int, int, int)

- drawArc

```java
public void drawArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.drawArc

.

**Specified by:** drawArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** width

- the width of the arc to be drawn.
**Parameters:** height

- the height of the arc to be drawn.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.fillArc(int, int, int, int, int, int)

- fillArc

```java
public void fillArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.fillArc

.

**Specified by:** fillArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** width

- the width of the arc to be filled.
**Parameters:** height

- the height of the arc to be filled.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.drawArc(int, int, int, int, int, int)

- drawPolyline

```java
public void drawPolyline​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolyline

.

**Specified by:** drawPolyline

in class

Graphics
**Parameters:** xPoints

- an array of

x

points
**Parameters:** yPoints

- an array of

y

points
**Parameters:** nPoints

- the total number of points
**See Also:** Graphics.drawPolygon(int[], int[], int)

- drawPolygon

```java
public void drawPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolygon

.

**Specified by:** drawPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.fillPolygon(int[], int[], int)

,

Graphics.drawPolyline(int[], int[], int)

- fillPolygon

```java
public void fillPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.fillPolygon

.

**Specified by:** fillPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.drawPolygon(int[], int[], int)

- drawString

```java
public void drawString​(
String
aString,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** aString

- the string to be drawn.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- drawString

```java
public void drawString​(
AttributedCharacterIterator
iterator,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** iterator

- the iterator whose text is to be drawn
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- drawBytes

```java
public void drawBytes​(byte[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawBytes

.

**Overrides:** drawBytes

in class

Graphics
**Parameters:** data

- the data to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of bytes that are drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawChars(char[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

- drawChars

```java
public void drawChars​(char[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawChars

.

**Overrides:** drawChars

in class

Graphics
**Parameters:** data

- the array of characters to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of characters to be drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- copyArea

```java
public void copyArea​(int x,
int y,
int width,
int height,
int destX,
int destY)
```

Overrides

Graphics.copyArea

.

**Specified by:** copyArea

in class

Graphics
**Parameters:** x

- the

x

coordinate of the source rectangle.
**Parameters:** y

- the

y

coordinate of the source rectangle.
**Parameters:** width

- the width of the source rectangle.
**Parameters:** height

- the height of the source rectangle.
**Parameters:** destX

- the horizontal distance to copy the pixels.
**Parameters:** destY

- the vertical distance to copy the pixels.

- dispose

```java
public void dispose()
```

Overrides

Graphics.dispose

.

**Specified by:** dispose

in class

Graphics
**See Also:** Graphics.finalize()

,

Component.paint(java.awt.Graphics)

,

Component.update(java.awt.Graphics)

,

Component.getGraphics()

,

Graphics.create()

- isDrawingBuffer

```java
public boolean isDrawingBuffer()
```

Returns the drawingBuffer value.

**Returns:** true if this object is drawing from a Buffer

- setDebugOptions

```java
public void setDebugOptions​(int options)
```

Enables/disables diagnostic information about every graphics
operation. The value of

options

indicates how this information
should be displayed. LOG_OPTION causes a text message to be printed.
FLASH_OPTION causes the drawing to flash several times. BUFFERED_OPTION
creates a new Frame that shows each operation on an
offscreen buffer. The value of

options

is bitwise OR'd into
the current value. To disable debugging use NONE_OPTION.

**Parameters:** options

- indicates how diagnostic information should be displayed

- getDebugOptions

```java
public int getDebugOptions()
```

Returns the current debugging options for this DebugGraphics.

**Returns:** the current debugging options for this DebugGraphics
**See Also:** setDebugOptions(int)

Field Detail

- LOG_OPTION

```java
public static final int LOG_OPTION
```

Log graphics operations.

**See Also:** Constant Field Values

- FLASH_OPTION

```java
public static final int FLASH_OPTION
```

Flash graphics operations.

**See Also:** Constant Field Values

- BUFFERED_OPTION

```java
public static final int BUFFERED_OPTION
```

Show buffered operations in a separate

Frame

.

**See Also:** Constant Field Values

- NONE_OPTION

```java
public static final int NONE_OPTION
```

Don't debug graphics operations.

**See Also:** Constant Field Values

---

#### Field Detail

LOG_OPTION

```java
public static final int LOG_OPTION
```

Log graphics operations.

**See Also:** Constant Field Values

---

#### LOG_OPTION

public static final int LOG_OPTION

Log graphics operations.

FLASH_OPTION

```java
public static final int FLASH_OPTION
```

Flash graphics operations.

**See Also:** Constant Field Values

---

#### FLASH_OPTION

public static final int FLASH_OPTION

Flash graphics operations.

BUFFERED_OPTION

```java
public static final int BUFFERED_OPTION
```

Show buffered operations in a separate

Frame

.

**See Also:** Constant Field Values

---

#### BUFFERED_OPTION

public static final int BUFFERED_OPTION

Show buffered operations in a separate

Frame

.

NONE_OPTION

```java
public static final int NONE_OPTION
```

Don't debug graphics operations.

**See Also:** Constant Field Values

---

#### NONE_OPTION

public static final int NONE_OPTION

Don't debug graphics operations.

Constructor Detail

- DebugGraphics

```java
public DebugGraphics()
```

Constructs a new debug graphics context that supports slowed
down drawing.

- DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics,

JComponent
component)
```

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

**Parameters:** graphics

- the Graphics context to slow down
**Parameters:** component

- the JComponent to draw slowly

- DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics)
```

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

**Parameters:** graphics

- the Graphics context to slow down

---

#### Constructor Detail

DebugGraphics

```java
public DebugGraphics()
```

Constructs a new debug graphics context that supports slowed
down drawing.

---

#### DebugGraphics

public DebugGraphics()

Constructs a new debug graphics context that supports slowed
down drawing.

DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics,

JComponent
component)
```

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

**Parameters:** graphics

- the Graphics context to slow down
**Parameters:** component

- the JComponent to draw slowly

---

#### DebugGraphics

public DebugGraphics​(

Graphics

graphics,

JComponent

component)

Constructs a debug graphics context from an existing graphics
context that slows down drawing for the specified component.

DebugGraphics

```java
public DebugGraphics​(
Graphics
graphics)
```

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

**Parameters:** graphics

- the Graphics context to slow down

---

#### DebugGraphics

public DebugGraphics​(

Graphics

graphics)

Constructs a debug graphics context from an existing graphics
context that supports slowed down drawing.

Method Detail

- create

```java
public
Graphics
create()
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Specified by:** create

in class

Graphics
**Returns:** a new graphics context that is a copy of
this graphics context.

- create

```java
public
Graphics
create​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Overrides:** create

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the clipping rectangle.
**Parameters:** height

- the height of the clipping rectangle.
**Returns:** a new graphics context.
**See Also:** Graphics.translate(int, int)

,

Graphics.clipRect(int, int, int, int)

- setFlashColor

```java
public static void setFlashColor​(
Color
flashColor)
```

Sets the Color used to flash drawing operations.

**Parameters:** flashColor

- the Color used to flash drawing operations

- flashColor

```java
public static
Color
flashColor()
```

Returns the Color used to flash drawing operations.

**Returns:** the Color used to flash drawing operations
**See Also:** setFlashColor(java.awt.Color)

- setFlashTime

```java
public static void setFlashTime​(int flashTime)
```

Sets the time delay of drawing operation flashing.

**Parameters:** flashTime

- the time delay of drawing operation flashing

- flashTime

```java
public static int flashTime()
```

Returns the time delay of drawing operation flashing.

**Returns:** the time delay of drawing operation flashing
**See Also:** setFlashTime(int)

- setFlashCount

```java
public static void setFlashCount​(int flashCount)
```

Sets the number of times that drawing operations will flash.

**Parameters:** flashCount

- number of times that drawing operations will flash

- flashCount

```java
public static int flashCount()
```

Returns the number of times that drawing operations will flash.

**Returns:** the number of times that drawing operations will flash
**See Also:** setFlashCount(int)

- setLogStream

```java
public static void setLogStream​(
PrintStream
stream)
```

Sets the stream to which the DebugGraphics logs drawing operations.

**Parameters:** stream

- the stream to which the DebugGraphics logs drawing operations

- logStream

```java
public static
PrintStream
logStream()
```

Returns the stream to which the DebugGraphics logs drawing operations.

**Returns:** the stream to which the DebugGraphics logs drawing operations
**See Also:** setLogStream(java.io.PrintStream)

- setFont

```java
public void setFont​(
Font
aFont)
```

Sets the Font used for text drawing operations.

**Specified by:** setFont

in class

Graphics
**Parameters:** aFont

- the font.
**See Also:** Graphics.getFont()

,

Graphics.drawString(java.lang.String, int, int)

,

Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- getFont

```java
public
Font
getFont()
```

Returns the Font used for text drawing operations.

**Specified by:** getFont

in class

Graphics
**Returns:** this graphics context's current font.
**See Also:** setFont(java.awt.Font)

- setColor

```java
public void setColor​(
Color
aColor)
```

Sets the color to be used for drawing and filling lines and shapes.

**Specified by:** setColor

in class

Graphics
**Parameters:** aColor

- the new rendering color.
**See Also:** Color

,

Graphics.getColor()

- getColor

```java
public
Color
getColor()
```

Returns the Color used for text drawing operations.

**Specified by:** getColor

in class

Graphics
**Returns:** this graphics context's current color.
**See Also:** setColor(java.awt.Color)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics()
```

Overrides

Graphics.getFontMetrics

.

**Overrides:** getFontMetrics

in class

Graphics
**Returns:** the font metrics of this graphics
context's current font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics(Font)

- getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Overrides

Graphics.getFontMetrics

.

**Specified by:** getFontMetrics

in class

Graphics
**Parameters:** f

- the specified font
**Returns:** the font metrics for the specified font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics()

- translate

```java
public void translate​(int x,
int y)
```

Overrides

Graphics.translate

.

**Specified by:** translate

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.

- setPaintMode

```java
public void setPaintMode()
```

Overrides

Graphics.setPaintMode

.

**Specified by:** setPaintMode

in class

Graphics

- setXORMode

```java
public void setXORMode​(
Color
aColor)
```

Overrides

Graphics.setXORMode

.

**Specified by:** setXORMode

in class

Graphics
**Parameters:** aColor

- the XOR alternation color

- getClipBounds

```java
public
Rectangle
getClipBounds()
```

Overrides

Graphics.getClipBounds

.

**Specified by:** getClipBounds

in class

Graphics
**Returns:** the bounding rectangle of the current clipping area,
or

null

if no clip is set.
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- clipRect

```java
public void clipRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clipRect

.

**Specified by:** clipRect

in class

Graphics
**Parameters:** x

- the x coordinate of the rectangle to intersect the clip with
**Parameters:** y

- the y coordinate of the rectangle to intersect the clip with
**Parameters:** width

- the width of the rectangle to intersect the clip with
**Parameters:** height

- the height of the rectangle to intersect the clip with
**See Also:** Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- setClip

```java
public void setClip​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** x

- the

x

coordinate of the new clip rectangle.
**Parameters:** y

- the

y

coordinate of the new clip rectangle.
**Parameters:** width

- the width of the new clip rectangle.
**Parameters:** height

- the height of the new clip rectangle.
**See Also:** Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(Shape)

,

Graphics.getClip()

- getClip

```java
public
Shape
getClip()
```

Overrides

Graphics.getClip

.

**Specified by:** getClip

in class

Graphics
**Returns:** a

Shape

object representing the
current clipping area, or

null

if
no clip is set.
**See Also:** Graphics.getClipBounds()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

- setClip

```java
public void setClip​(
Shape
clip)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** clip

- the

Shape

to use to set the clip
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

- drawRect

```java
public void drawRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawRect

.

**Overrides:** drawRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate
of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.clearRect(int, int, int, int)

- fillRect

```java
public void fillRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillRect

.

**Specified by:** fillRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate
of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**See Also:** Graphics.clearRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

- clearRect

```java
public void clearRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clearRect

.

**Specified by:** clearRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to clear.
**Parameters:** y

- the

y

coordinate of the rectangle to clear.
**Parameters:** width

- the width of the rectangle to clear.
**Parameters:** height

- the height of the rectangle to clear.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

,

Graphics.setColor(java.awt.Color)

,

Graphics.setPaintMode()

,

Graphics.setXORMode(java.awt.Color)

- drawRoundRect

```java
public void drawRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.drawRoundRect

.

**Specified by:** drawRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** arcWidth

- the horizontal diameter of the arc
at the four corners.
**Parameters:** arcHeight

- the vertical diameter of the arc
at the four corners.
**See Also:** Graphics.fillRoundRect(int, int, int, int, int, int)

- fillRoundRect

```java
public void fillRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.fillRoundRect

.

**Specified by:** fillRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** arcWidth

- the horizontal diameter
of the arc at the four corners.
**Parameters:** arcHeight

- the vertical diameter
of the arc at the four corners.
**See Also:** Graphics.drawRoundRect(int, int, int, int, int, int)

- drawLine

```java
public void drawLine​(int x1,
int y1,
int x2,
int y2)
```

Overrides

Graphics.drawLine

.

**Specified by:** drawLine

in class

Graphics
**Parameters:** x1

- the first point's

x

coordinate.
**Parameters:** y1

- the first point's

y

coordinate.
**Parameters:** x2

- the second point's

x

coordinate.
**Parameters:** y2

- the second point's

y

coordinate.

- draw3DRect

```java
public void draw3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.draw3DRect

.

**Overrides:** draw3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** raised

- a boolean that determines whether the rectangle
appears to be raised above the surface
or sunk into the surface.
**See Also:** Graphics.fill3DRect(int, int, int, int, boolean)

- fill3DRect

```java
public void fill3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.fill3DRect

.

**Overrides:** fill3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** raised

- a boolean value that determines whether the
rectangle appears to be raised above the surface
or etched into the surface.
**See Also:** Graphics.draw3DRect(int, int, int, int, boolean)

- drawOval

```java
public void drawOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawOval

.

**Specified by:** drawOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** y

- the

y

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** width

- the width of the oval to be drawn.
**Parameters:** height

- the height of the oval to be drawn.
**See Also:** Graphics.fillOval(int, int, int, int)

- fillOval

```java
public void fillOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillOval

.

**Specified by:** fillOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** y

- the

y

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** width

- the width of the oval to be filled.
**Parameters:** height

- the height of the oval to be filled.
**See Also:** Graphics.drawOval(int, int, int, int)

- drawArc

```java
public void drawArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.drawArc

.

**Specified by:** drawArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** width

- the width of the arc to be drawn.
**Parameters:** height

- the height of the arc to be drawn.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.fillArc(int, int, int, int, int, int)

- fillArc

```java
public void fillArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.fillArc

.

**Specified by:** fillArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** width

- the width of the arc to be filled.
**Parameters:** height

- the height of the arc to be filled.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.drawArc(int, int, int, int, int, int)

- drawPolyline

```java
public void drawPolyline​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolyline

.

**Specified by:** drawPolyline

in class

Graphics
**Parameters:** xPoints

- an array of

x

points
**Parameters:** yPoints

- an array of

y

points
**Parameters:** nPoints

- the total number of points
**See Also:** Graphics.drawPolygon(int[], int[], int)

- drawPolygon

```java
public void drawPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolygon

.

**Specified by:** drawPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.fillPolygon(int[], int[], int)

,

Graphics.drawPolyline(int[], int[], int)

- fillPolygon

```java
public void fillPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.fillPolygon

.

**Specified by:** fillPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.drawPolygon(int[], int[], int)

- drawString

```java
public void drawString​(
String
aString,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** aString

- the string to be drawn.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- drawString

```java
public void drawString​(
AttributedCharacterIterator
iterator,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** iterator

- the iterator whose text is to be drawn
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

- drawBytes

```java
public void drawBytes​(byte[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawBytes

.

**Overrides:** drawBytes

in class

Graphics
**Parameters:** data

- the data to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of bytes that are drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawChars(char[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

- drawChars

```java
public void drawChars​(char[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawChars

.

**Overrides:** drawChars

in class

Graphics
**Parameters:** data

- the array of characters to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of characters to be drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

- copyArea

```java
public void copyArea​(int x,
int y,
int width,
int height,
int destX,
int destY)
```

Overrides

Graphics.copyArea

.

**Specified by:** copyArea

in class

Graphics
**Parameters:** x

- the

x

coordinate of the source rectangle.
**Parameters:** y

- the

y

coordinate of the source rectangle.
**Parameters:** width

- the width of the source rectangle.
**Parameters:** height

- the height of the source rectangle.
**Parameters:** destX

- the horizontal distance to copy the pixels.
**Parameters:** destY

- the vertical distance to copy the pixels.

- dispose

```java
public void dispose()
```

Overrides

Graphics.dispose

.

**Specified by:** dispose

in class

Graphics
**See Also:** Graphics.finalize()

,

Component.paint(java.awt.Graphics)

,

Component.update(java.awt.Graphics)

,

Component.getGraphics()

,

Graphics.create()

- isDrawingBuffer

```java
public boolean isDrawingBuffer()
```

Returns the drawingBuffer value.

**Returns:** true if this object is drawing from a Buffer

- setDebugOptions

```java
public void setDebugOptions​(int options)
```

Enables/disables diagnostic information about every graphics
operation. The value of

options

indicates how this information
should be displayed. LOG_OPTION causes a text message to be printed.
FLASH_OPTION causes the drawing to flash several times. BUFFERED_OPTION
creates a new Frame that shows each operation on an
offscreen buffer. The value of

options

is bitwise OR'd into
the current value. To disable debugging use NONE_OPTION.

**Parameters:** options

- indicates how diagnostic information should be displayed

- getDebugOptions

```java
public int getDebugOptions()
```

Returns the current debugging options for this DebugGraphics.

**Returns:** the current debugging options for this DebugGraphics
**See Also:** setDebugOptions(int)

---

#### Method Detail

create

```java
public
Graphics
create()
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Specified by:** create

in class

Graphics
**Returns:** a new graphics context that is a copy of
this graphics context.

---

#### create

public

Graphics

create()

Overrides

Graphics.create

to return a DebugGraphics object.

create

```java
public
Graphics
create​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.create

to return a DebugGraphics object.

**Overrides:** create

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the clipping rectangle.
**Parameters:** height

- the height of the clipping rectangle.
**Returns:** a new graphics context.
**See Also:** Graphics.translate(int, int)

,

Graphics.clipRect(int, int, int, int)

---

#### create

public

Graphics

create​(int x,
int y,
int width,
int height)

Overrides

Graphics.create

to return a DebugGraphics object.

setFlashColor

```java
public static void setFlashColor​(
Color
flashColor)
```

Sets the Color used to flash drawing operations.

**Parameters:** flashColor

- the Color used to flash drawing operations

---

#### setFlashColor

public static void setFlashColor​(

Color

flashColor)

Sets the Color used to flash drawing operations.

flashColor

```java
public static
Color
flashColor()
```

Returns the Color used to flash drawing operations.

**Returns:** the Color used to flash drawing operations
**See Also:** setFlashColor(java.awt.Color)

---

#### flashColor

public static

Color

flashColor()

Returns the Color used to flash drawing operations.

setFlashTime

```java
public static void setFlashTime​(int flashTime)
```

Sets the time delay of drawing operation flashing.

**Parameters:** flashTime

- the time delay of drawing operation flashing

---

#### setFlashTime

public static void setFlashTime​(int flashTime)

Sets the time delay of drawing operation flashing.

flashTime

```java
public static int flashTime()
```

Returns the time delay of drawing operation flashing.

**Returns:** the time delay of drawing operation flashing
**See Also:** setFlashTime(int)

---

#### flashTime

public static int flashTime()

Returns the time delay of drawing operation flashing.

setFlashCount

```java
public static void setFlashCount​(int flashCount)
```

Sets the number of times that drawing operations will flash.

**Parameters:** flashCount

- number of times that drawing operations will flash

---

#### setFlashCount

public static void setFlashCount​(int flashCount)

Sets the number of times that drawing operations will flash.

flashCount

```java
public static int flashCount()
```

Returns the number of times that drawing operations will flash.

**Returns:** the number of times that drawing operations will flash
**See Also:** setFlashCount(int)

---

#### flashCount

public static int flashCount()

Returns the number of times that drawing operations will flash.

setLogStream

```java
public static void setLogStream​(
PrintStream
stream)
```

Sets the stream to which the DebugGraphics logs drawing operations.

**Parameters:** stream

- the stream to which the DebugGraphics logs drawing operations

---

#### setLogStream

public static void setLogStream​(

PrintStream

stream)

Sets the stream to which the DebugGraphics logs drawing operations.

logStream

```java
public static
PrintStream
logStream()
```

Returns the stream to which the DebugGraphics logs drawing operations.

**Returns:** the stream to which the DebugGraphics logs drawing operations
**See Also:** setLogStream(java.io.PrintStream)

---

#### logStream

public static

PrintStream

logStream()

Returns the stream to which the DebugGraphics logs drawing operations.

setFont

```java
public void setFont​(
Font
aFont)
```

Sets the Font used for text drawing operations.

**Specified by:** setFont

in class

Graphics
**Parameters:** aFont

- the font.
**See Also:** Graphics.getFont()

,

Graphics.drawString(java.lang.String, int, int)

,

Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### setFont

public void setFont​(

Font

aFont)

Sets the Font used for text drawing operations.

getFont

```java
public
Font
getFont()
```

Returns the Font used for text drawing operations.

**Specified by:** getFont

in class

Graphics
**Returns:** this graphics context's current font.
**See Also:** setFont(java.awt.Font)

---

#### getFont

public

Font

getFont()

Returns the Font used for text drawing operations.

setColor

```java
public void setColor​(
Color
aColor)
```

Sets the color to be used for drawing and filling lines and shapes.

**Specified by:** setColor

in class

Graphics
**Parameters:** aColor

- the new rendering color.
**See Also:** Color

,

Graphics.getColor()

---

#### setColor

public void setColor​(

Color

aColor)

Sets the color to be used for drawing and filling lines and shapes.

getColor

```java
public
Color
getColor()
```

Returns the Color used for text drawing operations.

**Specified by:** getColor

in class

Graphics
**Returns:** this graphics context's current color.
**See Also:** setColor(java.awt.Color)

---

#### getColor

public

Color

getColor()

Returns the Color used for text drawing operations.

getFontMetrics

```java
public
FontMetrics
getFontMetrics()
```

Overrides

Graphics.getFontMetrics

.

**Overrides:** getFontMetrics

in class

Graphics
**Returns:** the font metrics of this graphics
context's current font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics(Font)

---

#### getFontMetrics

public

FontMetrics

getFontMetrics()

Overrides

Graphics.getFontMetrics

.

getFontMetrics

```java
public
FontMetrics
getFontMetrics​(
Font
f)
```

Overrides

Graphics.getFontMetrics

.

**Specified by:** getFontMetrics

in class

Graphics
**Parameters:** f

- the specified font
**Returns:** the font metrics for the specified font.
**See Also:** Graphics.getFont()

,

FontMetrics

,

Graphics.getFontMetrics()

---

#### getFontMetrics

public

FontMetrics

getFontMetrics​(

Font

f)

Overrides

Graphics.getFontMetrics

.

translate

```java
public void translate​(int x,
int y)
```

Overrides

Graphics.translate

.

**Specified by:** translate

in class

Graphics
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.

---

#### translate

public void translate​(int x,
int y)

Overrides

Graphics.translate

.

setPaintMode

```java
public void setPaintMode()
```

Overrides

Graphics.setPaintMode

.

**Specified by:** setPaintMode

in class

Graphics

---

#### setPaintMode

public void setPaintMode()

Overrides

Graphics.setPaintMode

.

setXORMode

```java
public void setXORMode​(
Color
aColor)
```

Overrides

Graphics.setXORMode

.

**Specified by:** setXORMode

in class

Graphics
**Parameters:** aColor

- the XOR alternation color

---

#### setXORMode

public void setXORMode​(

Color

aColor)

Overrides

Graphics.setXORMode

.

getClipBounds

```java
public
Rectangle
getClipBounds()
```

Overrides

Graphics.getClipBounds

.

**Specified by:** getClipBounds

in class

Graphics
**Returns:** the bounding rectangle of the current clipping area,
or

null

if no clip is set.
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### getClipBounds

public

Rectangle

getClipBounds()

Overrides

Graphics.getClipBounds

.

clipRect

```java
public void clipRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clipRect

.

**Specified by:** clipRect

in class

Graphics
**Parameters:** x

- the x coordinate of the rectangle to intersect the clip with
**Parameters:** y

- the y coordinate of the rectangle to intersect the clip with
**Parameters:** width

- the width of the rectangle to intersect the clip with
**Parameters:** height

- the height of the rectangle to intersect the clip with
**See Also:** Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### clipRect

public void clipRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.clipRect

.

setClip

```java
public void setClip​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** x

- the

x

coordinate of the new clip rectangle.
**Parameters:** y

- the

y

coordinate of the new clip rectangle.
**Parameters:** width

- the width of the new clip rectangle.
**Parameters:** height

- the height of the new clip rectangle.
**See Also:** Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(Shape)

,

Graphics.getClip()

---

#### setClip

public void setClip​(int x,
int y,
int width,
int height)

Overrides

Graphics.setClip

.

getClip

```java
public
Shape
getClip()
```

Overrides

Graphics.getClip

.

**Specified by:** getClip

in class

Graphics
**Returns:** a

Shape

object representing the
current clipping area, or

null

if
no clip is set.
**See Also:** Graphics.getClipBounds()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

,

Graphics.setClip(Shape)

---

#### getClip

public

Shape

getClip()

Overrides

Graphics.getClip

.

setClip

```java
public void setClip​(
Shape
clip)
```

Overrides

Graphics.setClip

.

**Specified by:** setClip

in class

Graphics
**Parameters:** clip

- the

Shape

to use to set the clip
**See Also:** Graphics.getClip()

,

Graphics.clipRect(int, int, int, int)

,

Graphics.setClip(int, int, int, int)

---

#### setClip

public void setClip​(

Shape

clip)

Overrides

Graphics.setClip

.

drawRect

```java
public void drawRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawRect

.

**Overrides:** drawRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate
of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.clearRect(int, int, int, int)

---

#### drawRect

public void drawRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawRect

.

fillRect

```java
public void fillRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillRect

.

**Specified by:** fillRect

in class

Graphics
**Parameters:** x

- the

x

coordinate
of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate
of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**See Also:** Graphics.clearRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

---

#### fillRect

public void fillRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillRect

.

clearRect

```java
public void clearRect​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.clearRect

.

**Specified by:** clearRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to clear.
**Parameters:** y

- the

y

coordinate of the rectangle to clear.
**Parameters:** width

- the width of the rectangle to clear.
**Parameters:** height

- the height of the rectangle to clear.
**See Also:** Graphics.fillRect(int, int, int, int)

,

Graphics.drawRect(int, int, int, int)

,

Graphics.setColor(java.awt.Color)

,

Graphics.setPaintMode()

,

Graphics.setXORMode(java.awt.Color)

---

#### clearRect

public void clearRect​(int x,
int y,
int width,
int height)

Overrides

Graphics.clearRect

.

drawRoundRect

```java
public void drawRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.drawRoundRect

.

**Specified by:** drawRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** arcWidth

- the horizontal diameter of the arc
at the four corners.
**Parameters:** arcHeight

- the vertical diameter of the arc
at the four corners.
**See Also:** Graphics.fillRoundRect(int, int, int, int, int, int)

---

#### drawRoundRect

public void drawRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.drawRoundRect

.

fillRoundRect

```java
public void fillRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)
```

Overrides

Graphics.fillRoundRect

.

**Specified by:** fillRoundRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** arcWidth

- the horizontal diameter
of the arc at the four corners.
**Parameters:** arcHeight

- the vertical diameter
of the arc at the four corners.
**See Also:** Graphics.drawRoundRect(int, int, int, int, int, int)

---

#### fillRoundRect

public void fillRoundRect​(int x,
int y,
int width,
int height,
int arcWidth,
int arcHeight)

Overrides

Graphics.fillRoundRect

.

drawLine

```java
public void drawLine​(int x1,
int y1,
int x2,
int y2)
```

Overrides

Graphics.drawLine

.

**Specified by:** drawLine

in class

Graphics
**Parameters:** x1

- the first point's

x

coordinate.
**Parameters:** y1

- the first point's

y

coordinate.
**Parameters:** x2

- the second point's

x

coordinate.
**Parameters:** y2

- the second point's

y

coordinate.

---

#### drawLine

public void drawLine​(int x1,
int y1,
int x2,
int y2)

Overrides

Graphics.drawLine

.

draw3DRect

```java
public void draw3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.draw3DRect

.

**Overrides:** draw3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be drawn.
**Parameters:** y

- the

y

coordinate of the rectangle to be drawn.
**Parameters:** width

- the width of the rectangle to be drawn.
**Parameters:** height

- the height of the rectangle to be drawn.
**Parameters:** raised

- a boolean that determines whether the rectangle
appears to be raised above the surface
or sunk into the surface.
**See Also:** Graphics.fill3DRect(int, int, int, int, boolean)

---

#### draw3DRect

public void draw3DRect​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.draw3DRect

.

fill3DRect

```java
public void fill3DRect​(int x,
int y,
int width,
int height,
boolean raised)
```

Overrides

Graphics.fill3DRect

.

**Overrides:** fill3DRect

in class

Graphics
**Parameters:** x

- the

x

coordinate of the rectangle to be filled.
**Parameters:** y

- the

y

coordinate of the rectangle to be filled.
**Parameters:** width

- the width of the rectangle to be filled.
**Parameters:** height

- the height of the rectangle to be filled.
**Parameters:** raised

- a boolean value that determines whether the
rectangle appears to be raised above the surface
or etched into the surface.
**See Also:** Graphics.draw3DRect(int, int, int, int, boolean)

---

#### fill3DRect

public void fill3DRect​(int x,
int y,
int width,
int height,
boolean raised)

Overrides

Graphics.fill3DRect

.

drawOval

```java
public void drawOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.drawOval

.

**Specified by:** drawOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** y

- the

y

coordinate of the upper left
corner of the oval to be drawn.
**Parameters:** width

- the width of the oval to be drawn.
**Parameters:** height

- the height of the oval to be drawn.
**See Also:** Graphics.fillOval(int, int, int, int)

---

#### drawOval

public void drawOval​(int x,
int y,
int width,
int height)

Overrides

Graphics.drawOval

.

fillOval

```java
public void fillOval​(int x,
int y,
int width,
int height)
```

Overrides

Graphics.fillOval

.

**Specified by:** fillOval

in class

Graphics
**Parameters:** x

- the

x

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** y

- the

y

coordinate of the upper left corner
of the oval to be filled.
**Parameters:** width

- the width of the oval to be filled.
**Parameters:** height

- the height of the oval to be filled.
**See Also:** Graphics.drawOval(int, int, int, int)

---

#### fillOval

public void fillOval​(int x,
int y,
int width,
int height)

Overrides

Graphics.fillOval

.

drawArc

```java
public void drawArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.drawArc

.

**Specified by:** drawArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be drawn.
**Parameters:** width

- the width of the arc to be drawn.
**Parameters:** height

- the height of the arc to be drawn.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.fillArc(int, int, int, int, int, int)

---

#### drawArc

public void drawArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.drawArc

.

fillArc

```java
public void fillArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)
```

Overrides

Graphics.fillArc

.

**Specified by:** fillArc

in class

Graphics
**Parameters:** x

- the

x

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** y

- the

y

coordinate of the
upper-left corner of the arc to be filled.
**Parameters:** width

- the width of the arc to be filled.
**Parameters:** height

- the height of the arc to be filled.
**Parameters:** startAngle

- the beginning angle.
**Parameters:** arcAngle

- the angular extent of the arc,
relative to the start angle.
**See Also:** Graphics.drawArc(int, int, int, int, int, int)

---

#### fillArc

public void fillArc​(int x,
int y,
int width,
int height,
int startAngle,
int arcAngle)

Overrides

Graphics.fillArc

.

drawPolyline

```java
public void drawPolyline​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolyline

.

**Specified by:** drawPolyline

in class

Graphics
**Parameters:** xPoints

- an array of

x

points
**Parameters:** yPoints

- an array of

y

points
**Parameters:** nPoints

- the total number of points
**See Also:** Graphics.drawPolygon(int[], int[], int)

---

#### drawPolyline

public void drawPolyline​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolyline

.

drawPolygon

```java
public void drawPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.drawPolygon

.

**Specified by:** drawPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.fillPolygon(int[], int[], int)

,

Graphics.drawPolyline(int[], int[], int)

---

#### drawPolygon

public void drawPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.drawPolygon

.

fillPolygon

```java
public void fillPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)
```

Overrides

Graphics.fillPolygon

.

**Specified by:** fillPolygon

in class

Graphics
**Parameters:** xPoints

- a an array of

x

coordinates.
**Parameters:** yPoints

- a an array of

y

coordinates.
**Parameters:** nPoints

- a the total number of points.
**See Also:** Graphics.drawPolygon(int[], int[], int)

---

#### fillPolygon

public void fillPolygon​(int[] xPoints,
int[] yPoints,
int nPoints)

Overrides

Graphics.fillPolygon

.

drawString

```java
public void drawString​(
String
aString,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** aString

- the string to be drawn.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### drawString

public void drawString​(

String

aString,
int x,
int y)

Overrides

Graphics.drawString

.

drawString

```java
public void drawString​(
AttributedCharacterIterator
iterator,
int x,
int y)
```

Overrides

Graphics.drawString

.

**Specified by:** drawString

in class

Graphics
**Parameters:** iterator

- the iterator whose text is to be drawn
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawChars(char[], int, int, int, int)

---

#### drawString

public void drawString​(

AttributedCharacterIterator

iterator,
int x,
int y)

Overrides

Graphics.drawString

.

drawBytes

```java
public void drawBytes​(byte[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawBytes

.

**Overrides:** drawBytes

in class

Graphics
**Parameters:** data

- the data to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of bytes that are drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawChars(char[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

---

#### drawBytes

public void drawBytes​(byte[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawBytes

.

drawChars

```java
public void drawChars​(char[] data,
int offset,
int length,
int x,
int y)
```

Overrides

Graphics.drawChars

.

**Overrides:** drawChars

in class

Graphics
**Parameters:** data

- the array of characters to be drawn
**Parameters:** offset

- the start offset in the data
**Parameters:** length

- the number of characters to be drawn
**Parameters:** x

- the

x

coordinate of the baseline of the text
**Parameters:** y

- the

y

coordinate of the baseline of the text
**See Also:** Graphics.drawBytes(byte[], int, int, int, int)

,

Graphics.drawString(java.lang.String, int, int)

---

#### drawChars

public void drawChars​(char[] data,
int offset,
int length,
int x,
int y)

Overrides

Graphics.drawChars

.

drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int x,
int y,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int x,
int y,
int width,
int height,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int x,
int y,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

drawImage

```java
public boolean drawImage​(
Image
img,
int x,
int y,
int width,
int height,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** x

- the

x

coordinate.
**Parameters:** y

- the

y

coordinate.
**Parameters:** width

- the width of the rectangle.
**Parameters:** height

- the height of the rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of
the image is converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int x,
int y,
int width,
int height,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

drawImage

```java
public boolean drawImage​(
Image
img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color
bgcolor,

ImageObserver
observer)
```

Overrides

Graphics.drawImage

.

**Specified by:** drawImage

in class

Graphics
**Parameters:** img

- the specified image to be drawn. This method does
nothing if

img

is null.
**Parameters:** dx1

- the

x

coordinate of the first corner of the
destination rectangle.
**Parameters:** dy1

- the

y

coordinate of the first corner of the
destination rectangle.
**Parameters:** dx2

- the

x

coordinate of the second corner of the
destination rectangle.
**Parameters:** dy2

- the

y

coordinate of the second corner of the
destination rectangle.
**Parameters:** sx1

- the

x

coordinate of the first corner of the
source rectangle.
**Parameters:** sy1

- the

y

coordinate of the first corner of the
source rectangle.
**Parameters:** sx2

- the

x

coordinate of the second corner of the
source rectangle.
**Parameters:** sy2

- the

y

coordinate of the second corner of the
source rectangle.
**Parameters:** bgcolor

- the background color to paint under the
non-opaque portions of the image.
**Parameters:** observer

- object to be notified as more of the image is
scaled and converted.
**Returns:** false

if the image pixels are still changing;

true

otherwise.
**See Also:** Image

,

ImageObserver

,

ImageObserver.imageUpdate(java.awt.Image, int, int, int, int, int)

---

#### drawImage

public boolean drawImage​(

Image

img,
int dx1,
int dy1,
int dx2,
int dy2,
int sx1,
int sy1,
int sx2,
int sy2,

Color

bgcolor,

ImageObserver

observer)

Overrides

Graphics.drawImage

.

copyArea

```java
public void copyArea​(int x,
int y,
int width,
int height,
int destX,
int destY)
```

Overrides

Graphics.copyArea

.

**Specified by:** copyArea

in class

Graphics
**Parameters:** x

- the

x

coordinate of the source rectangle.
**Parameters:** y

- the

y

coordinate of the source rectangle.
**Parameters:** width

- the width of the source rectangle.
**Parameters:** height

- the height of the source rectangle.
**Parameters:** destX

- the horizontal distance to copy the pixels.
**Parameters:** destY

- the vertical distance to copy the pixels.

---

#### copyArea

public void copyArea​(int x,
int y,
int width,
int height,
int destX,
int destY)

Overrides

Graphics.copyArea

.

dispose

```java
public void dispose()
```

Overrides

Graphics.dispose

.

**Specified by:** dispose

in class

Graphics
**See Also:** Graphics.finalize()

,

Component.paint(java.awt.Graphics)

,

Component.update(java.awt.Graphics)

,

Component.getGraphics()

,

Graphics.create()

---

#### dispose

public void dispose()

Overrides

Graphics.dispose

.

isDrawingBuffer

```java
public boolean isDrawingBuffer()
```

Returns the drawingBuffer value.

**Returns:** true if this object is drawing from a Buffer

---

#### isDrawingBuffer

public boolean isDrawingBuffer()

Returns the drawingBuffer value.

setDebugOptions

```java
public void setDebugOptions​(int options)
```

Enables/disables diagnostic information about every graphics
operation. The value of

options

indicates how this information
should be displayed. LOG_OPTION causes a text message to be printed.
FLASH_OPTION causes the drawing to flash several times. BUFFERED_OPTION
creates a new Frame that shows each operation on an
offscreen buffer. The value of

options

is bitwise OR'd into
the current value. To disable debugging use NONE_OPTION.

**Parameters:** options

- indicates how diagnostic information should be displayed

---

#### setDebugOptions

public void setDebugOptions​(int options)

Enables/disables diagnostic information about every graphics
operation. The value of

options

indicates how this information
should be displayed. LOG_OPTION causes a text message to be printed.
FLASH_OPTION causes the drawing to flash several times. BUFFERED_OPTION
creates a new Frame that shows each operation on an
offscreen buffer. The value of

options

is bitwise OR'd into
the current value. To disable debugging use NONE_OPTION.

getDebugOptions

```java
public int getDebugOptions()
```

Returns the current debugging options for this DebugGraphics.

**Returns:** the current debugging options for this DebugGraphics
**See Also:** setDebugOptions(int)

---

#### getDebugOptions

public int getDebugOptions()

Returns the current debugging options for this DebugGraphics.

---

