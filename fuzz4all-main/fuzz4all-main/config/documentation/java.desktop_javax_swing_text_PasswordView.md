# Class PasswordView

**Source:** `java.desktop\javax\swing\text\PasswordView.html`

### Class Description

```java
public class
PasswordView

extends
FieldView
```

Implements a View suitable for use in JPasswordField
UI implementations. This is basically a field ui that
renders its contents as the echo character specified
in the associated component (if it can narrow the
component to a JPasswordField).

**All Implemented Interfaces:** SwingConstants

,

TabExpander

---

### Field Details

*No entries found.*

### Constructor Details

#### public PasswordView​(
Element
elem)

Constructs a new view wrapped on an element.

**Parameters:**
- elem

- the element

---

### Method Details

#### @Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as normal unselected
text. This sets the foreground color and echos the characters
using the value returned by getEchoChar().

**Overrides:**
- drawUnselectedText

in class

PlainView

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- p0

- the starting offset in the model >= 0
- p1

- the ending offset in the model >= p0

**Returns:**
- the X location of the end of the range >= 0

**Throws:**
- BadLocationException

- if p0 or p1 are out of range

---

#### @Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background. Uses the result of getEchoChar() to
display the characters.

**Overrides:**
- drawSelectedText

in class

PlainView

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- p0

- the starting offset in the model >= 0
- p1

- the ending offset in the model >= p0

**Returns:**
- the X location of the end of the range >= 0

**Throws:**
- BadLocationException

- if p0 or p1 are out of range

---

#### @Deprecated
(
since
="9")
protected int drawEchoCharacter​(
Graphics
g,
int x,
int y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate >= 0
- y

- the starting Y coordinate >= 0
- c

- the echo character

**Returns:**
- the updated X position >= 0

---

#### protected float drawEchoCharacter​(
Graphics2D
g,
float x,
float y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:**
- g

- the graphics context
- x

- the starting X coordinate

>= 0
- y

- the starting Y coordinate

>= 0
- c

- the echo character

**Returns:**
- the updated X position

>= 0

**Since:**
- 9

---

#### public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:**
- modelToView

in class

FieldView

**Parameters:**
- pos

- the position to convert >= 0
- a

- the allocated region to render into
- b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward

**Returns:**
- the bounding box of the given position

**Throws:**
- BadLocationException

- if the given position does not
represent a valid location in the associated document

**See Also:**
- View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:**
- viewToModel

in class

FieldView

**Parameters:**
- fx

- the X coordinate >= 0.0f
- fy

- the Y coordinate >= 0.0f
- a

- the allocated region to render into
- bias

- the returned bias

**Returns:**
- the location within the model that best represents the
given point in the view

**See Also:**
- View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

**Overrides:**
- getPreferredSpan

in class

FieldView

**Parameters:**
- axis

- may be either View.X_AXIS or View.Y_AXIS

**Returns:**
- the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.

**See Also:**
- View.getPreferredSpan(int)

---

### Additional Sections

#### Class PasswordView

java.lang.Object

- javax.swing.text.View
- - javax.swing.text.PlainView
- - javax.swing.text.FieldView
- - javax.swing.text.PasswordView

javax.swing.text.View

- javax.swing.text.PlainView
- - javax.swing.text.FieldView
- - javax.swing.text.PasswordView

javax.swing.text.PlainView

- javax.swing.text.FieldView
- - javax.swing.text.PasswordView

javax.swing.text.FieldView

- javax.swing.text.PasswordView

javax.swing.text.PasswordView

**All Implemented Interfaces:** SwingConstants

,

TabExpander

```java
public class
PasswordView

extends
FieldView
```

Implements a View suitable for use in JPasswordField
UI implementations. This is basically a field ui that
renders its contents as the echo character specified
in the associated component (if it can narrow the
component to a JPasswordField).

**See Also:** View

public class

PasswordView

extends

FieldView

Implements a View suitable for use in JPasswordField
UI implementations. This is basically a field ui that
renders its contents as the echo character specified
in the associated component (if it can narrow the
component to a JPasswordField).

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.text.

PlainView

metrics

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PasswordView

​(

Element

elem)

Constructs a new view wrapped on an element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected float

drawEchoCharacter

​(

Graphics2D

g,
float x,
float y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters.

protected int

drawEchoCharacter

​(

Graphics

g,
int x,
int y,
char c)

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

protected int

drawSelectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

protected int

drawUnselectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

int

viewToModel

​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

FieldView

adjustAllocation

,

getFontMetrics

,

getResizeWeight

,

insertUpdate

,

paint

,

removeUpdate

- Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

replace

,

setParent

,

updateChildren

,

updateLayout

,

viewToModel

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

- Fields declared in class javax.swing.text.

PlainView

metrics

- Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

- Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Field Summary

Fields declared in class javax.swing.text.

PlainView

metrics

---

#### Fields declared in class javax.swing.text. PlainView

Fields declared in class javax.swing.text.

View

BadBreakWeight

,

ExcellentBreakWeight

,

ForcedBreakWeight

,

GoodBreakWeight

,

X_AXIS

,

Y_AXIS

---

#### Fields declared in class javax.swing.text. View

Fields declared in interface javax.swing.

SwingConstants

BOTTOM

,

CENTER

,

EAST

,

HORIZONTAL

,

LEADING

,

LEFT

,

NEXT

,

NORTH

,

NORTH_EAST

,

NORTH_WEST

,

PREVIOUS

,

RIGHT

,

SOUTH

,

SOUTH_EAST

,

SOUTH_WEST

,

TOP

,

TRAILING

,

VERTICAL

,

WEST

---

#### Fields declared in interface javax.swing. SwingConstants

Constructor Summary

Constructors

Constructor

Description

PasswordView

​(

Element

elem)

Constructs a new view wrapped on an element.

---

#### Constructor Summary

Constructs a new view wrapped on an element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected float

drawEchoCharacter

​(

Graphics2D

g,
float x,
float y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters.

protected int

drawEchoCharacter

​(

Graphics

g,
int x,
int y,
char c)

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

protected int

drawSelectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

protected int

drawUnselectedText

​(

Graphics

g,
int x,
int y,
int p0,
int p1)

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

float

getPreferredSpan

​(int axis)

Determines the preferred span for this view along an
axis.

Shape

modelToView

​(int pos,

Shape

a,

Position.Bias

b)

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

int

viewToModel

​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

- Methods declared in class javax.swing.text.

FieldView

adjustAllocation

,

getFontMetrics

,

getResizeWeight

,

insertUpdate

,

paint

,

removeUpdate

- Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

- Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

replace

,

setParent

,

updateChildren

,

updateLayout

,

viewToModel

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

Renders the echo character, or whatever graphic should be used
to display the password characters.

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

Determines the preferred span for this view along an
axis.

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

Methods declared in class javax.swing.text.

FieldView

adjustAllocation

,

getFontMetrics

,

getResizeWeight

,

insertUpdate

,

paint

,

removeUpdate

---

#### Methods declared in class javax.swing.text. FieldView

Methods declared in class javax.swing.text.

PlainView

changedUpdate

,

damageLineRange

,

drawLine

,

drawLine

,

drawSelectedText

,

drawUnselectedText

,

getLineBuffer

,

getTabSize

,

lineToRect

,

nextTabStop

,

setSize

,

updateDamage

,

updateMetrics

---

#### Methods declared in class javax.swing.text. PlainView

Methods declared in class javax.swing.text.

View

append

,

breakView

,

createFragment

,

forwardUpdate

,

forwardUpdateToView

,

getAlignment

,

getAttributes

,

getBreakWeight

,

getChildAllocation

,

getContainer

,

getDocument

,

getElement

,

getEndOffset

,

getGraphics

,

getMaximumSpan

,

getMinimumSpan

,

getNextVisualPositionFrom

,

getParent

,

getStartOffset

,

getToolTipText

,

getView

,

getViewCount

,

getViewFactory

,

getViewIndex

,

getViewIndex

,

insert

,

isVisible

,

modelToView

,

modelToView

,

preferenceChanged

,

remove

,

removeAll

,

replace

,

setParent

,

updateChildren

,

updateLayout

,

viewToModel

---

#### Methods declared in class javax.swing.text. View

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

- PasswordView

```java
public PasswordView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

============ METHOD DETAIL ==========

- Method Detail

- drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. This sets the foreground color and echos the characters
using the value returned by getEchoChar().

**Overrides:** drawUnselectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

- drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background. Uses the result of getEchoChar() to
display the characters.

**Overrides:** drawSelectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

- drawEchoCharacter

```java
@Deprecated
(
since
="9")
protected int drawEchoCharacter​(
Graphics
g,
int x,
int y,
char c)
```

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position >= 0

- drawEchoCharacter

```java
protected float drawEchoCharacter​(
Graphics2D
g,
float x,
float y,
char c)
```

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position

>= 0
**Since:** 9

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

FieldView
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

FieldView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

FieldView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

Constructor Detail

- PasswordView

```java
public PasswordView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### Constructor Detail

PasswordView

```java
public PasswordView​(
Element
elem)
```

Constructs a new view wrapped on an element.

**Parameters:** elem

- the element

---

#### PasswordView

public PasswordView​(

Element

elem)

Constructs a new view wrapped on an element.

Method Detail

- drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. This sets the foreground color and echos the characters
using the value returned by getEchoChar().

**Overrides:** drawUnselectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

- drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background. Uses the result of getEchoChar() to
display the characters.

**Overrides:** drawSelectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

- drawEchoCharacter

```java
@Deprecated
(
since
="9")
protected int drawEchoCharacter​(
Graphics
g,
int x,
int y,
char c)
```

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position >= 0

- drawEchoCharacter

```java
protected float drawEchoCharacter​(
Graphics2D
g,
float x,
float y,
char c)
```

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position

>= 0
**Since:** 9

- modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

FieldView
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

- viewToModel

```java
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

FieldView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

- getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

FieldView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

---

#### Method Detail

drawUnselectedText

```java
@Deprecated
(
since
="9")
protected int drawUnselectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawUnselectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as normal unselected
text. This sets the foreground color and echos the characters
using the value returned by getEchoChar().

**Overrides:** drawUnselectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

---

#### drawUnselectedText

@Deprecated

(

since

="9")
protected int drawUnselectedText​(

Graphics

g,
int x,
int y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as normal unselected
text. This sets the foreground color and echos the characters
using the value returned by getEchoChar().

drawSelectedText

```java
@Deprecated
(
since
="9")
protected int drawSelectedText​(
Graphics
g,
int x,
int y,
int p0,
int p1)
throws
BadLocationException
```

Deprecated.

replaced by

PlainView.drawSelectedText(Graphics2D, float, float, int, int)

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background. Uses the result of getEchoChar() to
display the characters.

**Overrides:** drawSelectedText

in class

PlainView
**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** p0

- the starting offset in the model >= 0
**Parameters:** p1

- the ending offset in the model >= p0
**Returns:** the X location of the end of the range >= 0
**Throws:** BadLocationException

- if p0 or p1 are out of range

---

#### drawSelectedText

@Deprecated

(

since

="9")
protected int drawSelectedText​(

Graphics

g,
int x,
int y,
int p0,
int p1)
throws

BadLocationException

Renders the given range in the model as selected text. This
is implemented to render the text in the color specified in
the hosting component. It assumes the highlighter will render
the selected background. Uses the result of getEchoChar() to
display the characters.

drawEchoCharacter

```java
@Deprecated
(
since
="9")
protected int drawEchoCharacter​(
Graphics
g,
int x,
int y,
char c)
```

Deprecated.

replaced by

drawEchoCharacter(Graphics2D, float, float, char)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate >= 0
**Parameters:** y

- the starting Y coordinate >= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position >= 0

---

#### drawEchoCharacter

@Deprecated

(

since

="9")
protected int drawEchoCharacter​(

Graphics

g,
int x,
int y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

drawEchoCharacter

```java
protected float drawEchoCharacter​(
Graphics2D
g,
float x,
float y,
char c)
```

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

**Parameters:** g

- the graphics context
**Parameters:** x

- the starting X coordinate

>= 0
**Parameters:** y

- the starting Y coordinate

>= 0
**Parameters:** c

- the echo character
**Returns:** the updated X position

>= 0
**Since:** 9

---

#### drawEchoCharacter

protected float drawEchoCharacter​(

Graphics2D

g,
float x,
float y,
char c)

Renders the echo character, or whatever graphic should be used
to display the password characters. The color in the Graphics
object is set to the appropriate foreground color for selected
or unselected text.

modelToView

```java
public
Shape
modelToView​(int pos,

Shape
a,

Position.Bias
b)
throws
BadLocationException
```

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

**Overrides:** modelToView

in class

FieldView
**Parameters:** pos

- the position to convert >= 0
**Parameters:** a

- the allocated region to render into
**Parameters:** b

- the bias toward the previous character or the
next character represented by the offset, in case the
position is a boundary of two views;

b

will have one
of these values:

- Position.Bias.Forward

Position.Bias.Backward
**Returns:** the bounding box of the given position
**Throws:** BadLocationException

- if the given position does not
represent a valid location in the associated document
**See Also:** View.modelToView(int, java.awt.Shape, javax.swing.text.Position.Bias)

---

#### modelToView

public

Shape

modelToView​(int pos,

Shape

a,

Position.Bias

b)
throws

BadLocationException

Provides a mapping from the document model coordinate space
to the coordinate space of the view mapped to it.

Position.Bias.Forward

Position.Bias.Backward

viewToModel

```java
public int viewToModel​(float fx,
float fy,

Shape
a,

Position.Bias
[] bias)
```

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

**Overrides:** viewToModel

in class

FieldView
**Parameters:** fx

- the X coordinate >= 0.0f
**Parameters:** fy

- the Y coordinate >= 0.0f
**Parameters:** a

- the allocated region to render into
**Parameters:** bias

- the returned bias
**Returns:** the location within the model that best represents the
given point in the view
**See Also:** View.viewToModel(float, float, java.awt.Shape, javax.swing.text.Position.Bias[])

---

#### viewToModel

public int viewToModel​(float fx,
float fy,

Shape

a,

Position.Bias

[] bias)

Provides a mapping from the view coordinate space to the logical
coordinate space of the model.

getPreferredSpan

```java
public float getPreferredSpan​(int axis)
```

Determines the preferred span for this view along an
axis.

**Overrides:** getPreferredSpan

in class

FieldView
**Parameters:** axis

- may be either View.X_AXIS or View.Y_AXIS
**Returns:** the span the view would like to be rendered into >= 0.
Typically the view is told to render into the span
that is returned, although there is no guarantee.
The parent may choose to resize or break the view.
**See Also:** View.getPreferredSpan(int)

---

#### getPreferredSpan

public float getPreferredSpan​(int axis)

Determines the preferred span for this view along an
axis.

---

