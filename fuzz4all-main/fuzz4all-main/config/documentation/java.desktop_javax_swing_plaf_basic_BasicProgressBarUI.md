# Class BasicProgressBarUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicProgressBarUI.html`

### Class Description

```java
public class
BasicProgressBarUI

extends
ProgressBarUI
```

A Basic L&F implementation of ProgressBarUI.

**Direct Known Subclasses:** MetalProgressBarUI

,

SynthProgressBarUI

---

### Field Details

#### protected
JProgressBar
progressBar

The instance of

JProgressBar

.

---

#### protected
ChangeListener
changeListener

The instance of

ChangeListener

.

---

#### protected
Rectangle
boxRect

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

**Since:**
- 1.5

---

### Constructor Details

#### public BasicProgressBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Returns a new instance of

BasicProgressBarUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicProgressBarUI

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Unintalls default properties.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void startAnimationTimer()

Starts the animation thread, creating and initializing
it if necessary. This method is invoked when an
indeterminate progress bar should start animating.
Reasons for this may include:

- The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

If you implement your own animation thread,
you must override this method.

**See Also:**
- stopAnimationTimer()

**Since:**
- 1.4

---

#### protected void stopAnimationTimer()

Stops the animation thread.
This method is invoked when the indeterminate
animation should be stopped. Reasons for this may include:

- The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

If you implement your own animation thread,
you must override this method.

**See Also:**
- startAnimationTimer()

**Since:**
- 1.4

---

#### protected void uninstallListeners()

Removes all listeners installed by this object.

---

#### public int getBaseline​(
JComponent
c,
int width,
int height)

Returns the baseline.

**Overrides:**
- getBaseline

in class

ComponentUI

**Parameters:**
- c

-

JComponent

baseline is being requested for
- width

- the width to get the baseline for
- height

- the height to get the baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- NullPointerException

- if

c

is

null
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
JComponent
c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:**
- getBaselineResizeBehavior

in class

ComponentUI

**Parameters:**
- c

-

JComponent

to return baseline resize behavior for

**Returns:**
- an enum indicating how the baseline changes as the component
size changes

**Throws:**
- NullPointerException

- if

c

is

null

**See Also:**
- JComponent.getBaseline(int, int)

**Since:**
- 1.6

---

#### protected
Dimension
getPreferredInnerHorizontal()

Returns preferred size of the horizontal

JProgressBar

.

**Returns:**
- preferred size of the horizontal

JProgressBar

---

#### protected
Dimension
getPreferredInnerVertical()

Returns preferred size of the vertical

JProgressBar

.

**Returns:**
- preferred size of the vertical

JProgressBar

---

#### protected
Color
getSelectionForeground()

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

**Returns:**
- the color of the selected foreground

---

#### protected
Color
getSelectionBackground()

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

**Returns:**
- the color of the selected background

---

#### protected int getCellLength()

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 1 when
the progress string is being rendered.

**Returns:**
- the value representing the spacing between cells

**See Also:**
- setCellLength(int)

,

JProgressBar.isStringPainted()

---

#### protected void setCellLength​(int cellLen)

Sets the cell length.

**Parameters:**
- cellLen

- a new cell length

---

#### protected int getCellSpacing()

Returns the spacing between each of the cells/units in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 0 when
the progress string is being rendered.

**Returns:**
- the value representing the spacing between cells

**See Also:**
- setCellSpacing(int)

,

JProgressBar.isStringPainted()

---

#### protected void setCellSpacing​(int cellSpace)

Sets the cell spacing.

**Parameters:**
- cellSpace

- a new cell spacing

---

#### protected int getAmountFull​(
Insets
b,
int width,
int height)

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model. This is a common
operation so it was abstracted out. It assumes that your progress bar
is linear. That is, if you are making a circular progress indicator,
you will want to override this method.

**Parameters:**
- b

- insets
- width

- a width
- height

- a height

**Returns:**
- the amount of the progress bar that should be filled

---

#### public void paint​(
Graphics
g,

JComponent
c)

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### protected
Rectangle
getBox​(
Rectangle
r)

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.
Subclasses that add to the painting performed
in this class's implementation of

paintIndeterminate

--
to draw an outline around the bouncing box, for example --
can use this method to get the location of the bouncing
box that was just painted.
By overriding this method,
you have complete control over the size and position
of the bouncing box,
without having to reimplement

paintIndeterminate

.

**Parameters:**
- r

- the Rectangle instance to be modified;
may be

null

**Returns:**
- null

if no box should be drawn;
otherwise, returns the passed-in rectangle
(if non-null)
or a new rectangle

**See Also:**
- setAnimationIndex(int)

**Since:**
- 1.4

---

#### protected int getBoxLength​(int availableLength,
int otherDimension)

Returns the length
of the "bouncing box" to be painted.
This method is invoked by the
default implementation of

paintIndeterminate

to get the width (if the progress bar is horizontal)
or height (if vertical) of the box.
For example:

```java
boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);
```

**Parameters:**
- availableLength

- the amount of space available
for the bouncing box to move in;
for a horizontal progress bar,
for example,
this should be
the inside width of the progress bar
(the component width minus borders)
- otherDimension

- for a horizontal progress bar, this should be
the inside height of the progress bar; this
value might be used to constrain or determine
the return value

**Returns:**
- the size of the box dimension being determined;
must be no larger than

availableLength

**See Also:**
- SwingUtilities.calculateInnerArea(javax.swing.JComponent, java.awt.Rectangle)

**Since:**
- 1.5

---

#### protected void paintIndeterminate​(
Graphics
g,

JComponent
c)

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.
Override this if you are making another kind of
progress bar.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component

**See Also:**
- paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.4

---

#### protected void paintDeterminate​(
Graphics
g,

JComponent
c)

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars. By setting a few values in
the defaults
table, things should work just fine to paint your progress bar.
Naturally, override this if you are making a circular or
semi-circular progress bar.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component

**See Also:**
- paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

**Since:**
- 1.4

---

#### protected void paintString​(
Graphics
g,
int x,
int y,
int width,
int height,
int amountFull,

Insets
b)

Paints the progress string.

**Parameters:**
- g

- an instance of

Graphics
- x

- X location of bounding box
- y

- Y location of bounding box
- width

- width of bounding box
- height

- height of bounding box
- amountFull

- size of the fill region, either width or height
depending upon orientation.
- b

- Insets of the progress bar.

---

#### protected
Point
getStringPlacement​(
Graphics
g,

String
progressString,
int x,
int y,
int width,
int height)

Designate the place where the progress string will be painted.
This implementation places it at the center of the progress
bar (in both x and y). Override this if you want to right,
left, top, or bottom align the progress string or if you need
to nudge it around for any reason.

**Parameters:**
- g

- an instance of

Graphics
- progressString

- a text
- x

- an X coordinate
- y

- an Y coordinate
- width

- a width
- height

- a height

**Returns:**
- the place where the progress string will be painted

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

The Minimum size for this component is 10. The rationale here
is that there should be at least one pixel per 10 percent.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### protected int getAnimationIndex()

Gets the index of the current animation frame.

**Returns:**
- the index of the current animation frame

**Since:**
- 1.4

---

#### protected final int getFrameCount()

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar. The progress chunk will go
from one end to the other and back during the entire loop. This
visual behavior may be changed by subclasses in other Look and Feels.

**Returns:**
- the number of frames

**Since:**
- 1.6

---

#### protected void setAnimationIndex​(int newValue)

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.
Subclasses that don't use the default painting code
might need to override this method
to change the way that the

repaint

method
is invoked.

**Parameters:**
- newValue

- the new animation index; no checking
is performed on its value

**See Also:**
- incrementAnimationIndex()

**Since:**
- 1.4

---

#### protected void incrementAnimationIndex()

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.
The next valid value is, by default,
the current animation index plus one.
If the new value would be too large,
this method sets the index to 0.
Subclasses might need to override this method
to ensure that the index does not go over
the number of frames needed for the particular
progress bar instance.
This method is invoked by the default animation thread
every

X

milliseconds,
where

X

is specified by the "ProgressBar.repaintInterval"
UI default.

**See Also:**
- setAnimationIndex(int)

**Since:**
- 1.4

---

### Additional Sections

#### Class BasicProgressBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ProgressBarUI
- - javax.swing.plaf.basic.BasicProgressBarUI

javax.swing.plaf.ProgressBarUI

- javax.swing.plaf.basic.BasicProgressBarUI

javax.swing.plaf.basic.BasicProgressBarUI

**Direct Known Subclasses:** MetalProgressBarUI

,

SynthProgressBarUI

```java
public class
BasicProgressBarUI

extends
ProgressBarUI
```

A Basic L&F implementation of ProgressBarUI.

public class

BasicProgressBarUI

extends

ProgressBarUI

A Basic L&F implementation of ProgressBarUI.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicProgressBarUI.ChangeHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Rectangle

boxRect

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

protected

ChangeListener

changeListener

The instance of

ChangeListener

.

protected

JProgressBar

progressBar

The instance of

JProgressBar

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicProgressBarUI

()

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

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicProgressBarUI

.

protected int

getAmountFull

​(

Insets

b,
int width,
int height)

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model.

protected int

getAnimationIndex

()

Gets the index of the current animation frame.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Rectangle

getBox

​(

Rectangle

r)

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.

protected int

getBoxLength

​(int availableLength,
int otherDimension)

Returns the length
of the "bouncing box" to be painted.

protected int

getCellLength

()

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar.

protected int

getCellSpacing

()

Returns the spacing between each of the cells/units in the
progress bar.

protected int

getFrameCount

()

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar.

Dimension

getMinimumSize

​(

JComponent

c)

The Minimum size for this component is 10.

protected

Dimension

getPreferredInnerHorizontal

()

Returns preferred size of the horizontal

JProgressBar

.

protected

Dimension

getPreferredInnerVertical

()

Returns preferred size of the vertical

JProgressBar

.

protected

Color

getSelectionBackground

()

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

protected

Color

getSelectionForeground

()

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

protected

Point

getStringPlacement

​(

Graphics

g,

String

progressString,
int x,
int y,
int width,
int height)

Designate the place where the progress string will be painted.

protected void

incrementAnimationIndex

()

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

void

paint

​(

Graphics

g,

JComponent

c)

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

protected void

paintDeterminate

​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars.

protected void

paintIndeterminate

​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.

protected void

paintString

​(

Graphics

g,
int x,
int y,
int width,
int height,
int amountFull,

Insets

b)

Paints the progress string.

protected void

setAnimationIndex

​(int newValue)

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.

protected void

setCellLength

​(int cellLen)

Sets the cell length.

protected void

setCellSpacing

​(int cellSpace)

Sets the cell spacing.

protected void

startAnimationTimer

()

Starts the animation thread, creating and initializing
it if necessary.

protected void

stopAnimationTimer

()

Stops the animation thread.

protected void

uninstallDefaults

()

Unintalls default properties.

protected void

uninstallListeners

()

Removes all listeners installed by this object.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

uninstallUI

,

update

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

Nested Classes

Modifier and Type

Class

Description

class

BasicProgressBarUI.ChangeHandler

This class should be treated as a "protected" inner class.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

Field Summary

Fields

Modifier and Type

Field

Description

protected

Rectangle

boxRect

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

protected

ChangeListener

changeListener

The instance of

ChangeListener

.

protected

JProgressBar

progressBar

The instance of

JProgressBar

.

---

#### Field Summary

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

The instance of

ChangeListener

.

The instance of

JProgressBar

.

Constructor Summary

Constructors

Constructor

Description

BasicProgressBarUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

ComponentUI

createUI

​(

JComponent

x)

Returns a new instance of

BasicProgressBarUI

.

protected int

getAmountFull

​(

Insets

b,
int width,
int height)

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model.

protected int

getAnimationIndex

()

Gets the index of the current animation frame.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Rectangle

getBox

​(

Rectangle

r)

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.

protected int

getBoxLength

​(int availableLength,
int otherDimension)

Returns the length
of the "bouncing box" to be painted.

protected int

getCellLength

()

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar.

protected int

getCellSpacing

()

Returns the spacing between each of the cells/units in the
progress bar.

protected int

getFrameCount

()

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar.

Dimension

getMinimumSize

​(

JComponent

c)

The Minimum size for this component is 10.

protected

Dimension

getPreferredInnerHorizontal

()

Returns preferred size of the horizontal

JProgressBar

.

protected

Dimension

getPreferredInnerVertical

()

Returns preferred size of the vertical

JProgressBar

.

protected

Color

getSelectionBackground

()

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

protected

Color

getSelectionForeground

()

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

protected

Point

getStringPlacement

​(

Graphics

g,

String

progressString,
int x,
int y,
int width,
int height)

Designate the place where the progress string will be painted.

protected void

incrementAnimationIndex

()

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

void

paint

​(

Graphics

g,

JComponent

c)

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

protected void

paintDeterminate

​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars.

protected void

paintIndeterminate

​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.

protected void

paintString

​(

Graphics

g,
int x,
int y,
int width,
int height,
int amountFull,

Insets

b)

Paints the progress string.

protected void

setAnimationIndex

​(int newValue)

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.

protected void

setCellLength

​(int cellLen)

Sets the cell length.

protected void

setCellSpacing

​(int cellSpace)

Sets the cell spacing.

protected void

startAnimationTimer

()

Starts the animation thread, creating and initializing
it if necessary.

protected void

stopAnimationTimer

()

Stops the animation thread.

protected void

uninstallDefaults

()

Unintalls default properties.

protected void

uninstallListeners

()

Removes all listeners installed by this object.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

uninstallUI

,

update

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

Returns a new instance of

BasicProgressBarUI

.

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model.

Gets the index of the current animation frame.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.

Returns the length
of the "bouncing box" to be painted.

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar.

Returns the spacing between each of the cells/units in the
progress bar.

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar.

The Minimum size for this component is 10.

Returns preferred size of the horizontal

JProgressBar

.

Returns preferred size of the vertical

JProgressBar

.

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

Designate the place where the progress string will be painted.

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.

Installs default properties.

Registers listeners.

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars.

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.

Paints the progress string.

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.

Sets the cell length.

Sets the cell spacing.

Starts the animation thread, creating and initializing
it if necessary.

Stops the animation thread.

Unintalls default properties.

Removes all listeners installed by this object.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getMaximumSize

,

getPreferredSize

,

installUI

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- progressBar

```java
protected
JProgressBar
progressBar
```

The instance of

JProgressBar

.

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

- boxRect

```java
protected
Rectangle
boxRect
```

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicProgressBarUI

```java
public BasicProgressBarUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicProgressBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicProgressBarUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Unintalls default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- startAnimationTimer

```java
protected void startAnimationTimer()
```

Starts the animation thread, creating and initializing
it if necessary. This method is invoked when an
indeterminate progress bar should start animating.
Reasons for this may include:

- The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** stopAnimationTimer()

- stopAnimationTimer

```java
protected void stopAnimationTimer()
```

Stops the animation thread.
This method is invoked when the indeterminate
animation should be stopped. Reasons for this may include:

- The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** startAnimationTimer()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes all listeners installed by this object.

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getPreferredInnerHorizontal

```java
protected
Dimension
getPreferredInnerHorizontal()
```

Returns preferred size of the horizontal

JProgressBar

.

**Returns:** preferred size of the horizontal

JProgressBar

- getPreferredInnerVertical

```java
protected
Dimension
getPreferredInnerVertical()
```

Returns preferred size of the vertical

JProgressBar

.

**Returns:** preferred size of the vertical

JProgressBar

- getSelectionForeground

```java
protected
Color
getSelectionForeground()
```

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

**Returns:** the color of the selected foreground

- getSelectionBackground

```java
protected
Color
getSelectionBackground()
```

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

**Returns:** the color of the selected background

- getCellLength

```java
protected int getCellLength()
```

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 1 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellLength(int)

,

JProgressBar.isStringPainted()

- setCellLength

```java
protected void setCellLength​(int cellLen)
```

Sets the cell length.

**Parameters:** cellLen

- a new cell length

- getCellSpacing

```java
protected int getCellSpacing()
```

Returns the spacing between each of the cells/units in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 0 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellSpacing(int)

,

JProgressBar.isStringPainted()

- setCellSpacing

```java
protected void setCellSpacing​(int cellSpace)
```

Sets the cell spacing.

**Parameters:** cellSpace

- a new cell spacing

- getAmountFull

```java
protected int getAmountFull​(
Insets
b,
int width,
int height)
```

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model. This is a common
operation so it was abstracted out. It assumes that your progress bar
is linear. That is, if you are making a circular progress indicator,
you will want to override this method.

**Parameters:** b

- insets
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the amount of the progress bar that should be filled

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

- getBox

```java
protected
Rectangle
getBox​(
Rectangle
r)
```

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.
Subclasses that add to the painting performed
in this class's implementation of

paintIndeterminate

--
to draw an outline around the bouncing box, for example --
can use this method to get the location of the bouncing
box that was just painted.
By overriding this method,
you have complete control over the size and position
of the bouncing box,
without having to reimplement

paintIndeterminate

.

**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if no box should be drawn;
otherwise, returns the passed-in rectangle
(if non-null)
or a new rectangle
**Since:** 1.4
**See Also:** setAnimationIndex(int)

- getBoxLength

```java
protected int getBoxLength​(int availableLength,
int otherDimension)
```

Returns the length
of the "bouncing box" to be painted.
This method is invoked by the
default implementation of

paintIndeterminate

to get the width (if the progress bar is horizontal)
or height (if vertical) of the box.
For example:

```java
boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);
```

**Parameters:** availableLength

- the amount of space available
for the bouncing box to move in;
for a horizontal progress bar,
for example,
this should be
the inside width of the progress bar
(the component width minus borders)
**Parameters:** otherDimension

- for a horizontal progress bar, this should be
the inside height of the progress bar; this
value might be used to constrain or determine
the return value
**Returns:** the size of the box dimension being determined;
must be no larger than

availableLength
**Since:** 1.5
**See Also:** SwingUtilities.calculateInnerArea(javax.swing.JComponent, java.awt.Rectangle)

- paintIndeterminate

```java
protected void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.
Override this if you are making another kind of
progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintDeterminate

```java
protected void paintDeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars. By setting a few values in
the defaults
table, things should work just fine to paint your progress bar.
Naturally, override this if you are making a circular or
semi-circular progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintString

```java
protected void paintString​(
Graphics
g,
int x,
int y,
int width,
int height,
int amountFull,

Insets
b)
```

Paints the progress string.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- X location of bounding box
**Parameters:** y

- Y location of bounding box
**Parameters:** width

- width of bounding box
**Parameters:** height

- height of bounding box
**Parameters:** amountFull

- size of the fill region, either width or height
depending upon orientation.
**Parameters:** b

- Insets of the progress bar.

- getStringPlacement

```java
protected
Point
getStringPlacement​(
Graphics
g,

String
progressString,
int x,
int y,
int width,
int height)
```

Designate the place where the progress string will be painted.
This implementation places it at the center of the progress
bar (in both x and y). Override this if you want to right,
left, top, or bottom align the progress string or if you need
to nudge it around for any reason.

**Parameters:** g

- an instance of

Graphics
**Parameters:** progressString

- a text
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the place where the progress string will be painted

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The Minimum size for this component is 10. The rationale here
is that there should be at least one pixel per 10 percent.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getAnimationIndex

```java
protected int getAnimationIndex()
```

Gets the index of the current animation frame.

**Returns:** the index of the current animation frame
**Since:** 1.4

- getFrameCount

```java
protected final int getFrameCount()
```

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar. The progress chunk will go
from one end to the other and back during the entire loop. This
visual behavior may be changed by subclasses in other Look and Feels.

**Returns:** the number of frames
**Since:** 1.6

- setAnimationIndex

```java
protected void setAnimationIndex​(int newValue)
```

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.
Subclasses that don't use the default painting code
might need to override this method
to change the way that the

repaint

method
is invoked.

**Parameters:** newValue

- the new animation index; no checking
is performed on its value
**Since:** 1.4
**See Also:** incrementAnimationIndex()

- incrementAnimationIndex

```java
protected void incrementAnimationIndex()
```

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.
The next valid value is, by default,
the current animation index plus one.
If the new value would be too large,
this method sets the index to 0.
Subclasses might need to override this method
to ensure that the index does not go over
the number of frames needed for the particular
progress bar instance.
This method is invoked by the default animation thread
every

X

milliseconds,
where

X

is specified by the "ProgressBar.repaintInterval"
UI default.

**Since:** 1.4
**See Also:** setAnimationIndex(int)

Field Detail

- progressBar

```java
protected
JProgressBar
progressBar
```

The instance of

JProgressBar

.

- changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

- boxRect

```java
protected
Rectangle
boxRect
```

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

**Since:** 1.5

---

#### Field Detail

progressBar

```java
protected
JProgressBar
progressBar
```

The instance of

JProgressBar

.

---

#### progressBar

protected

JProgressBar

progressBar

The instance of

JProgressBar

.

changeListener

```java
protected
ChangeListener
changeListener
```

The instance of

ChangeListener

.

---

#### changeListener

protected

ChangeListener

changeListener

The instance of

ChangeListener

.

boxRect

```java
protected
Rectangle
boxRect
```

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

**Since:** 1.5

---

#### boxRect

protected

Rectangle

boxRect

Used to hold the location and size of the bouncing box (returned
by getBox) to be painted.

Constructor Detail

- BasicProgressBarUI

```java
public BasicProgressBarUI()
```

---

#### Constructor Detail

BasicProgressBarUI

```java
public BasicProgressBarUI()
```

---

#### BasicProgressBarUI

public BasicProgressBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicProgressBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicProgressBarUI

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Unintalls default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- startAnimationTimer

```java
protected void startAnimationTimer()
```

Starts the animation thread, creating and initializing
it if necessary. This method is invoked when an
indeterminate progress bar should start animating.
Reasons for this may include:

- The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** stopAnimationTimer()

- stopAnimationTimer

```java
protected void stopAnimationTimer()
```

Stops the animation thread.
This method is invoked when the indeterminate
animation should be stopped. Reasons for this may include:

- The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** startAnimationTimer()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes all listeners installed by this object.

- getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

- getPreferredInnerHorizontal

```java
protected
Dimension
getPreferredInnerHorizontal()
```

Returns preferred size of the horizontal

JProgressBar

.

**Returns:** preferred size of the horizontal

JProgressBar

- getPreferredInnerVertical

```java
protected
Dimension
getPreferredInnerVertical()
```

Returns preferred size of the vertical

JProgressBar

.

**Returns:** preferred size of the vertical

JProgressBar

- getSelectionForeground

```java
protected
Color
getSelectionForeground()
```

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

**Returns:** the color of the selected foreground

- getSelectionBackground

```java
protected
Color
getSelectionBackground()
```

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

**Returns:** the color of the selected background

- getCellLength

```java
protected int getCellLength()
```

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 1 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellLength(int)

,

JProgressBar.isStringPainted()

- setCellLength

```java
protected void setCellLength​(int cellLen)
```

Sets the cell length.

**Parameters:** cellLen

- a new cell length

- getCellSpacing

```java
protected int getCellSpacing()
```

Returns the spacing between each of the cells/units in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 0 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellSpacing(int)

,

JProgressBar.isStringPainted()

- setCellSpacing

```java
protected void setCellSpacing​(int cellSpace)
```

Sets the cell spacing.

**Parameters:** cellSpace

- a new cell spacing

- getAmountFull

```java
protected int getAmountFull​(
Insets
b,
int width,
int height)
```

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model. This is a common
operation so it was abstracted out. It assumes that your progress bar
is linear. That is, if you are making a circular progress indicator,
you will want to override this method.

**Parameters:** b

- insets
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the amount of the progress bar that should be filled

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

- getBox

```java
protected
Rectangle
getBox​(
Rectangle
r)
```

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.
Subclasses that add to the painting performed
in this class's implementation of

paintIndeterminate

--
to draw an outline around the bouncing box, for example --
can use this method to get the location of the bouncing
box that was just painted.
By overriding this method,
you have complete control over the size and position
of the bouncing box,
without having to reimplement

paintIndeterminate

.

**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if no box should be drawn;
otherwise, returns the passed-in rectangle
(if non-null)
or a new rectangle
**Since:** 1.4
**See Also:** setAnimationIndex(int)

- getBoxLength

```java
protected int getBoxLength​(int availableLength,
int otherDimension)
```

Returns the length
of the "bouncing box" to be painted.
This method is invoked by the
default implementation of

paintIndeterminate

to get the width (if the progress bar is horizontal)
or height (if vertical) of the box.
For example:

```java
boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);
```

**Parameters:** availableLength

- the amount of space available
for the bouncing box to move in;
for a horizontal progress bar,
for example,
this should be
the inside width of the progress bar
(the component width minus borders)
**Parameters:** otherDimension

- for a horizontal progress bar, this should be
the inside height of the progress bar; this
value might be used to constrain or determine
the return value
**Returns:** the size of the box dimension being determined;
must be no larger than

availableLength
**Since:** 1.5
**See Also:** SwingUtilities.calculateInnerArea(javax.swing.JComponent, java.awt.Rectangle)

- paintIndeterminate

```java
protected void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.
Override this if you are making another kind of
progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintDeterminate

```java
protected void paintDeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars. By setting a few values in
the defaults
table, things should work just fine to paint your progress bar.
Naturally, override this if you are making a circular or
semi-circular progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

- paintString

```java
protected void paintString​(
Graphics
g,
int x,
int y,
int width,
int height,
int amountFull,

Insets
b)
```

Paints the progress string.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- X location of bounding box
**Parameters:** y

- Y location of bounding box
**Parameters:** width

- width of bounding box
**Parameters:** height

- height of bounding box
**Parameters:** amountFull

- size of the fill region, either width or height
depending upon orientation.
**Parameters:** b

- Insets of the progress bar.

- getStringPlacement

```java
protected
Point
getStringPlacement​(
Graphics
g,

String
progressString,
int x,
int y,
int width,
int height)
```

Designate the place where the progress string will be painted.
This implementation places it at the center of the progress
bar (in both x and y). Override this if you want to right,
left, top, or bottom align the progress string or if you need
to nudge it around for any reason.

**Parameters:** g

- an instance of

Graphics
**Parameters:** progressString

- a text
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the place where the progress string will be painted

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The Minimum size for this component is 10. The rationale here
is that there should be at least one pixel per 10 percent.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getAnimationIndex

```java
protected int getAnimationIndex()
```

Gets the index of the current animation frame.

**Returns:** the index of the current animation frame
**Since:** 1.4

- getFrameCount

```java
protected final int getFrameCount()
```

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar. The progress chunk will go
from one end to the other and back during the entire loop. This
visual behavior may be changed by subclasses in other Look and Feels.

**Returns:** the number of frames
**Since:** 1.6

- setAnimationIndex

```java
protected void setAnimationIndex​(int newValue)
```

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.
Subclasses that don't use the default painting code
might need to override this method
to change the way that the

repaint

method
is invoked.

**Parameters:** newValue

- the new animation index; no checking
is performed on its value
**Since:** 1.4
**See Also:** incrementAnimationIndex()

- incrementAnimationIndex

```java
protected void incrementAnimationIndex()
```

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.
The next valid value is, by default,
the current animation index plus one.
If the new value would be too large,
this method sets the index to 0.
Subclasses might need to override this method
to ensure that the index does not go over
the number of frames needed for the particular
progress bar instance.
This method is invoked by the default animation thread
every

X

milliseconds,
where

X

is specified by the "ProgressBar.repaintInterval"
UI default.

**Since:** 1.4
**See Also:** setAnimationIndex(int)

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Returns a new instance of

BasicProgressBarUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicProgressBarUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Returns a new instance of

BasicProgressBarUI

.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Unintalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Unintalls default properties.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

startAnimationTimer

```java
protected void startAnimationTimer()
```

Starts the animation thread, creating and initializing
it if necessary. This method is invoked when an
indeterminate progress bar should start animating.
Reasons for this may include:

- The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** stopAnimationTimer()

---

#### startAnimationTimer

protected void startAnimationTimer()

Starts the animation thread, creating and initializing
it if necessary. This method is invoked when an
indeterminate progress bar should start animating.
Reasons for this may include:

- The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

If you implement your own animation thread,
you must override this method.

The progress bar is determinate and becomes displayable

The progress bar is displayable and becomes determinate

The progress bar is displayable and determinate and this
UI is installed

stopAnimationTimer

```java
protected void stopAnimationTimer()
```

Stops the animation thread.
This method is invoked when the indeterminate
animation should be stopped. Reasons for this may include:

- The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

If you implement your own animation thread,
you must override this method.

**Since:** 1.4
**See Also:** startAnimationTimer()

---

#### stopAnimationTimer

protected void stopAnimationTimer()

Stops the animation thread.
This method is invoked when the indeterminate
animation should be stopped. Reasons for this may include:

- The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

If you implement your own animation thread,
you must override this method.

The progress bar changes to determinate

The progress bar is no longer part of a displayable hierarchy

This UI in uninstalled

uninstallListeners

```java
protected void uninstallListeners()
```

Removes all listeners installed by this object.

---

#### uninstallListeners

protected void uninstallListeners()

Removes all listeners installed by this object.

getBaseline

```java
public int getBaseline​(
JComponent
c,
int width,
int height)
```

Returns the baseline.

**Overrides:** getBaseline

in class

ComponentUI
**Parameters:** c

-

JComponent

baseline is being requested for
**Parameters:** width

- the width to get the baseline for
**Parameters:** height

- the height to get the baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** NullPointerException

- if

c

is

null
**Throws:** IllegalArgumentException

- if width or height is < 0
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaseline

public int getBaseline​(

JComponent

c,
int width,
int height)

Returns the baseline.

getBaselineResizeBehavior

```java
public
Component.BaselineResizeBehavior
getBaselineResizeBehavior​(
JComponent
c)
```

Returns an enum indicating how the baseline of the component
changes as the size changes.

**Overrides:** getBaselineResizeBehavior

in class

ComponentUI
**Parameters:** c

-

JComponent

to return baseline resize behavior for
**Returns:** an enum indicating how the baseline changes as the component
size changes
**Throws:** NullPointerException

- if

c

is

null
**Since:** 1.6
**See Also:** JComponent.getBaseline(int, int)

---

#### getBaselineResizeBehavior

public

Component.BaselineResizeBehavior

getBaselineResizeBehavior​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

getPreferredInnerHorizontal

```java
protected
Dimension
getPreferredInnerHorizontal()
```

Returns preferred size of the horizontal

JProgressBar

.

**Returns:** preferred size of the horizontal

JProgressBar

---

#### getPreferredInnerHorizontal

protected

Dimension

getPreferredInnerHorizontal()

Returns preferred size of the horizontal

JProgressBar

.

getPreferredInnerVertical

```java
protected
Dimension
getPreferredInnerVertical()
```

Returns preferred size of the vertical

JProgressBar

.

**Returns:** preferred size of the vertical

JProgressBar

---

#### getPreferredInnerVertical

protected

Dimension

getPreferredInnerVertical()

Returns preferred size of the vertical

JProgressBar

.

getSelectionForeground

```java
protected
Color
getSelectionForeground()
```

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

**Returns:** the color of the selected foreground

---

#### getSelectionForeground

protected

Color

getSelectionForeground()

The "selectionForeground" is the color of the text when it is painted
over a filled area of the progress bar.

getSelectionBackground

```java
protected
Color
getSelectionBackground()
```

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

**Returns:** the color of the selected background

---

#### getSelectionBackground

protected

Color

getSelectionBackground()

The "selectionBackground" is the color of the text when it is painted
over an unfilled area of the progress bar.

getCellLength

```java
protected int getCellLength()
```

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 1 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellLength(int)

,

JProgressBar.isStringPainted()

---

#### getCellLength

protected int getCellLength()

Returns the width (if HORIZONTAL) or height (if VERTICAL)
of each of the individual cells/units to be rendered in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 1 when
the progress string is being rendered.

setCellLength

```java
protected void setCellLength​(int cellLen)
```

Sets the cell length.

**Parameters:** cellLen

- a new cell length

---

#### setCellLength

protected void setCellLength​(int cellLen)

Sets the cell length.

getCellSpacing

```java
protected int getCellSpacing()
```

Returns the spacing between each of the cells/units in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 0 when
the progress string is being rendered.

**Returns:** the value representing the spacing between cells
**See Also:** setCellSpacing(int)

,

JProgressBar.isStringPainted()

---

#### getCellSpacing

protected int getCellSpacing()

Returns the spacing between each of the cells/units in the
progress bar. However, for text rendering simplification and
aesthetic considerations, this function will return 0 when
the progress string is being rendered.

setCellSpacing

```java
protected void setCellSpacing​(int cellSpace)
```

Sets the cell spacing.

**Parameters:** cellSpace

- a new cell spacing

---

#### setCellSpacing

protected void setCellSpacing​(int cellSpace)

Sets the cell spacing.

getAmountFull

```java
protected int getAmountFull​(
Insets
b,
int width,
int height)
```

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model. This is a common
operation so it was abstracted out. It assumes that your progress bar
is linear. That is, if you are making a circular progress indicator,
you will want to override this method.

**Parameters:** b

- insets
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the amount of the progress bar that should be filled

---

#### getAmountFull

protected int getAmountFull​(

Insets

b,
int width,
int height)

This determines the amount of the progress bar that should be filled
based on the percent done gathered from the model. This is a common
operation so it was abstracted out. It assumes that your progress bar
is linear. That is, if you are making a circular progress indicator,
you will want to override this method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** ComponentUI.update(java.awt.Graphics, javax.swing.JComponent)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Delegates painting to one of two methods:
paintDeterminate or paintIndeterminate.

getBox

```java
protected
Rectangle
getBox​(
Rectangle
r)
```

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.
Subclasses that add to the painting performed
in this class's implementation of

paintIndeterminate

--
to draw an outline around the bouncing box, for example --
can use this method to get the location of the bouncing
box that was just painted.
By overriding this method,
you have complete control over the size and position
of the bouncing box,
without having to reimplement

paintIndeterminate

.

**Parameters:** r

- the Rectangle instance to be modified;
may be

null
**Returns:** null

if no box should be drawn;
otherwise, returns the passed-in rectangle
(if non-null)
or a new rectangle
**Since:** 1.4
**See Also:** setAnimationIndex(int)

---

#### getBox

protected

Rectangle

getBox​(

Rectangle

r)

Stores the position and size of
the bouncing box that would be painted for the current animation index
in

r

and returns

r

.
Subclasses that add to the painting performed
in this class's implementation of

paintIndeterminate

--
to draw an outline around the bouncing box, for example --
can use this method to get the location of the bouncing
box that was just painted.
By overriding this method,
you have complete control over the size and position
of the bouncing box,
without having to reimplement

paintIndeterminate

.

getBoxLength

```java
protected int getBoxLength​(int availableLength,
int otherDimension)
```

Returns the length
of the "bouncing box" to be painted.
This method is invoked by the
default implementation of

paintIndeterminate

to get the width (if the progress bar is horizontal)
or height (if vertical) of the box.
For example:

```java
boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);
```

**Parameters:** availableLength

- the amount of space available
for the bouncing box to move in;
for a horizontal progress bar,
for example,
this should be
the inside width of the progress bar
(the component width minus borders)
**Parameters:** otherDimension

- for a horizontal progress bar, this should be
the inside height of the progress bar; this
value might be used to constrain or determine
the return value
**Returns:** the size of the box dimension being determined;
must be no larger than

availableLength
**Since:** 1.5
**See Also:** SwingUtilities.calculateInnerArea(javax.swing.JComponent, java.awt.Rectangle)

---

#### getBoxLength

protected int getBoxLength​(int availableLength,
int otherDimension)

Returns the length
of the "bouncing box" to be painted.
This method is invoked by the
default implementation of

paintIndeterminate

to get the width (if the progress bar is horizontal)
or height (if vertical) of the box.
For example:

```java
boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);
```

boxRect.width = getBoxLength(componentInnards.width,
componentInnards.height);

paintIndeterminate

```java
protected void paintIndeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.
Override this if you are making another kind of
progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintDeterminate(java.awt.Graphics, javax.swing.JComponent)

---

#### paintIndeterminate

protected void paintIndeterminate​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for all
linear bouncing-box progress bars.
Override this if you are making another kind of
progress bar.

paintDeterminate

```java
protected void paintDeterminate​(
Graphics
g,

JComponent
c)
```

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars. By setting a few values in
the defaults
table, things should work just fine to paint your progress bar.
Naturally, override this if you are making a circular or
semi-circular progress bar.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component
**Since:** 1.4
**See Also:** paintIndeterminate(java.awt.Graphics, javax.swing.JComponent)

---

#### paintDeterminate

protected void paintDeterminate​(

Graphics

g,

JComponent

c)

All purpose paint method that should do the right thing for almost
all linear, determinate progress bars. By setting a few values in
the defaults
table, things should work just fine to paint your progress bar.
Naturally, override this if you are making a circular or
semi-circular progress bar.

paintString

```java
protected void paintString​(
Graphics
g,
int x,
int y,
int width,
int height,
int amountFull,

Insets
b)
```

Paints the progress string.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- X location of bounding box
**Parameters:** y

- Y location of bounding box
**Parameters:** width

- width of bounding box
**Parameters:** height

- height of bounding box
**Parameters:** amountFull

- size of the fill region, either width or height
depending upon orientation.
**Parameters:** b

- Insets of the progress bar.

---

#### paintString

protected void paintString​(

Graphics

g,
int x,
int y,
int width,
int height,
int amountFull,

Insets

b)

Paints the progress string.

getStringPlacement

```java
protected
Point
getStringPlacement​(
Graphics
g,

String
progressString,
int x,
int y,
int width,
int height)
```

Designate the place where the progress string will be painted.
This implementation places it at the center of the progress
bar (in both x and y). Override this if you want to right,
left, top, or bottom align the progress string or if you need
to nudge it around for any reason.

**Parameters:** g

- an instance of

Graphics
**Parameters:** progressString

- a text
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** width

- a width
**Parameters:** height

- a height
**Returns:** the place where the progress string will be painted

---

#### getStringPlacement

protected

Point

getStringPlacement​(

Graphics

g,

String

progressString,
int x,
int y,
int width,
int height)

Designate the place where the progress string will be painted.
This implementation places it at the center of the progress
bar (in both x and y). Override this if you want to right,
left, top, or bottom align the progress string or if you need
to nudge it around for any reason.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

The Minimum size for this component is 10. The rationale here
is that there should be at least one pixel per 10 percent.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### getMinimumSize

public

Dimension

getMinimumSize​(

JComponent

c)

The Minimum size for this component is 10. The rationale here
is that there should be at least one pixel per 10 percent.

getAnimationIndex

```java
protected int getAnimationIndex()
```

Gets the index of the current animation frame.

**Returns:** the index of the current animation frame
**Since:** 1.4

---

#### getAnimationIndex

protected int getAnimationIndex()

Gets the index of the current animation frame.

getFrameCount

```java
protected final int getFrameCount()
```

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar. The progress chunk will go
from one end to the other and back during the entire loop. This
visual behavior may be changed by subclasses in other Look and Feels.

**Returns:** the number of frames
**Since:** 1.6

---

#### getFrameCount

protected final int getFrameCount()

Returns the number of frames for the complete animation loop
used by an indeterminate JProgessBar. The progress chunk will go
from one end to the other and back during the entire loop. This
visual behavior may be changed by subclasses in other Look and Feels.

setAnimationIndex

```java
protected void setAnimationIndex​(int newValue)
```

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.
Subclasses that don't use the default painting code
might need to override this method
to change the way that the

repaint

method
is invoked.

**Parameters:** newValue

- the new animation index; no checking
is performed on its value
**Since:** 1.4
**See Also:** incrementAnimationIndex()

---

#### setAnimationIndex

protected void setAnimationIndex​(int newValue)

Sets the index of the current animation frame
to the specified value and requests that the
progress bar be repainted.
Subclasses that don't use the default painting code
might need to override this method
to change the way that the

repaint

method
is invoked.

incrementAnimationIndex

```java
protected void incrementAnimationIndex()
```

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.
The next valid value is, by default,
the current animation index plus one.
If the new value would be too large,
this method sets the index to 0.
Subclasses might need to override this method
to ensure that the index does not go over
the number of frames needed for the particular
progress bar instance.
This method is invoked by the default animation thread
every

X

milliseconds,
where

X

is specified by the "ProgressBar.repaintInterval"
UI default.

**Since:** 1.4
**See Also:** setAnimationIndex(int)

---

#### incrementAnimationIndex

protected void incrementAnimationIndex()

Sets the index of the current animation frame,
to the next valid value,
which results in the progress bar being repainted.
The next valid value is, by default,
the current animation index plus one.
If the new value would be too large,
this method sets the index to 0.
Subclasses might need to override this method
to ensure that the index does not go over
the number of frames needed for the particular
progress bar instance.
This method is invoked by the default animation thread
every

X

milliseconds,
where

X

is specified by the "ProgressBar.repaintInterval"
UI default.

---

