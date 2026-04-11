# Class BasicScrollBarUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicScrollBarUI.html`

### Class Description

```java
public class
BasicScrollBarUI

extends
ScrollBarUI

implements
LayoutManager
,
SwingConstants
```

Implementation of ScrollBarUI for the Basic Look and Feel

**All Implemented Interfaces:** LayoutManager

,

SwingConstants

---

### Field Details

#### protected
Dimension
minimumThumbSize

Minimum thumb size

---

#### protected
Dimension
maximumThumbSize

Maximum thumb size

---

#### protected
Color
thumbHighlightColor

Thumb highlight color

---

#### protected
Color
thumbLightShadowColor

Thumb light shadow color

---

#### protected
Color
thumbDarkShadowColor

Thumb dark shadow color

---

#### protected
Color
thumbColor

Thumb color

---

#### protected
Color
trackColor

Track color

---

#### protected
Color
trackHighlightColor

Track highlight color

---

#### protected
JScrollBar
scrollbar

Scrollbar

---

#### protected
JButton
incrButton

Increment button

---

#### protected
JButton
decrButton

Decrement button

---

#### protected boolean isDragging

Dragging

---

#### protected
BasicScrollBarUI.TrackListener
trackListener

Track listener

---

#### protected
BasicScrollBarUI.ArrowButtonListener
buttonListener

Button listener

---

#### protected
BasicScrollBarUI.ModelListener
modelListener

Model listener

---

#### protected
Rectangle
thumbRect

Thumb rectangle

---

#### protected
Rectangle
trackRect

Track rectangle

---

#### protected int trackHighlight

Track highlight

---

#### protected static final int NO_HIGHLIGHT

No highlight

**See Also:**
- Constant Field Values

---

#### protected static final int DECREASE_HIGHLIGHT

Decrease highlight

**See Also:**
- Constant Field Values

---

#### protected static final int INCREASE_HIGHLIGHT

Increase highlight

**See Also:**
- Constant Field Values

---

#### protected
BasicScrollBarUI.ScrollListener
scrollListener

Scroll listener

---

#### protected
PropertyChangeListener
propertyChangeListener

Property change listener

---

#### protected
Timer
scrollTimer

Scroll timer

---

#### protected int scrollBarWidth

Hint as to what width (when vertical) or height (when horizontal)
should be.

**Since:**
- 1.7

---

#### protected int incrGap

Distance between the increment button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:**
- 1.7

---

#### protected int decrGap

Distance between the decrement button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:**
- 1.7

---

### Constructor Details

#### public BasicScrollBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates the UI.

**Parameters:**
- c

- the component

**Returns:**
- the UI

---

#### protected void configureScrollBarColors()

Configures the scroll bar colors.

---

#### public void installUI​(
JComponent
c)

Installs the UI.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component

**See Also:**
- ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### public void uninstallUI​(
JComponent
c)

Uninstalls the UI.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the component

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### protected void installDefaults()

Installs the defaults.

---

#### protected void installComponents()

Installs the components.

---

#### protected void uninstallComponents()

Uninstalls the components.

---

#### protected void installListeners()

Installs the listeners.

---

#### protected void installKeyboardActions()

Installs the keyboard actions.

---

#### protected void uninstallKeyboardActions()

Uninstalls the keyboard actions.

---

#### protected void uninstallListeners()

Uninstall the listeners.

---

#### protected void uninstallDefaults()

Uninstalls the defaults.

---

#### protected
BasicScrollBarUI.TrackListener
createTrackListener()

Creates a track listener.

**Returns:**
- a track listener

---

#### protected
BasicScrollBarUI.ArrowButtonListener
createArrowButtonListener()

Creates an arrow button listener.

**Returns:**
- an arrow button listener

---

#### protected
BasicScrollBarUI.ModelListener
createModelListener()

Creates a model listener.

**Returns:**
- a model listener

---

#### protected
BasicScrollBarUI.ScrollListener
createScrollListener()

Creates a scroll listener.

**Returns:**
- a scroll listener

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a property change listener.

**Returns:**
- a property change listener

---

#### protected void setThumbRollover​(boolean active)

Sets whether or not the mouse is currently over the thumb.

**Parameters:**
- active

- True indicates the thumb is currently active.

**Since:**
- 1.5

---

#### public boolean isThumbRollover()

Returns true if the mouse is currently over the thumb.

**Returns:**
- true if the thumb is currently active

**Since:**
- 1.5

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb. The preferred height is the
sum of the preferred heights of the same parts. The basis for
the preferred size of a horizontal scrollbar is similar.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- the

JScrollBar

that's delegating this method to us

**Returns:**
- the preferred size of a Basic JScrollBar

**See Also:**
- getMaximumSize(javax.swing.JComponent)

,

ComponentUI.getMinimumSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Description copied from class:

ComponentUI

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- The JScrollBar that's delegating this method to us.

**Returns:**
- new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE);

**See Also:**
- ComponentUI.getMinimumSize(javax.swing.JComponent)

,

getPreferredSize(javax.swing.JComponent)

---

#### protected
JButton
createDecreaseButton​(int orientation)

Creates a decrease button.

**Parameters:**
- orientation

- the orientation

**Returns:**
- a decrease button

---

#### protected
JButton
createIncreaseButton​(int orientation)

Creates an increase button.

**Parameters:**
- orientation

- the orientation

**Returns:**
- an increase button

---

#### protected void paintDecreaseHighlight​(
Graphics
g)

Paints the decrease highlight.

**Parameters:**
- g

- the graphics

---

#### protected void paintIncreaseHighlight​(
Graphics
g)

Paints the increase highlight.

**Parameters:**
- g

- the graphics

---

#### protected void paintTrack​(
Graphics
g,

JComponent
c,

Rectangle
trackBounds)

Paints the track.

**Parameters:**
- g

- the graphics
- c

- the component
- trackBounds

- the track bounds

---

#### protected void paintThumb​(
Graphics
g,

JComponent
c,

Rectangle
thumbBounds)

Paints the thumb.

**Parameters:**
- g

- the graphics
- c

- the component
- thumbBounds

- the thumb bounds

---

#### protected
Dimension
getMinimumThumbSize()

Returns the smallest acceptable size for the thumb. If the scrollbar
becomes so small that this size isn't available, the thumb will be
hidden.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:**
- The smallest acceptable size for the thumb.

**See Also:**
- getMaximumThumbSize()

---

#### protected
Dimension
getMaximumThumbSize()

Returns the largest acceptable size for the thumb. To create a fixed
size thumb one make this method and

getMinimumThumbSize

return the same value.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:**
- The largest acceptable size for the thumb.

**See Also:**
- getMinimumThumbSize()

---

#### protected void layoutVScrollbar​(
JScrollBar
sb)

Laysouts a vertical scroll bar.

**Parameters:**
- sb

- the scroll bar

---

#### protected void layoutHScrollbar​(
JScrollBar
sb)

Laysouts a vertical scroll bar.

**Parameters:**
- sb

- the scroll bar

---

#### protected void setThumbBounds​(int x,
int y,
int width,
int height)

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

**Parameters:**
- x

- set the x location of the thumb
- y

- set the y location of the thumb
- width

- set the width of the thumb
- height

- set the height of the thumb

**See Also:**
- getThumbBounds()

---

#### protected
Rectangle
getThumbBounds()

Return the current size/location of the thumb.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:**
- The current size/location of the thumb.

**See Also:**
- setThumbBounds(int, int, int, int)

---

#### protected
Rectangle
getTrackBounds()

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets. The value
returned by this method is updated each time the scrollbar is
laid out (validated).

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:**
- the current bounds of the scrollbar track

**See Also:**
- LayoutManager.layoutContainer(java.awt.Container)

---

#### protected void scrollByBlock​(int direction)

Scrolls by block.

**Parameters:**
- direction

- the direction to scroll

---

#### protected void scrollByUnit​(int direction)

Scrolls by unit.

**Parameters:**
- direction

- the direction to scroll

---

#### public boolean getSupportsAbsolutePositioning()

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

**Returns:**
- true if a mouse gesture can absolutely position the thumb

**Since:**
- 1.5

---

### Additional Sections

#### Class BasicScrollBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ScrollBarUI
- - javax.swing.plaf.basic.BasicScrollBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ScrollBarUI
- - javax.swing.plaf.basic.BasicScrollBarUI

javax.swing.plaf.ScrollBarUI

- javax.swing.plaf.basic.BasicScrollBarUI

javax.swing.plaf.basic.BasicScrollBarUI

**All Implemented Interfaces:** LayoutManager

,

SwingConstants

**Direct Known Subclasses:** MetalScrollBarUI

,

SynthScrollBarUI

```java
public class
BasicScrollBarUI

extends
ScrollBarUI

implements
LayoutManager
,
SwingConstants
```

Implementation of ScrollBarUI for the Basic Look and Feel

public class

BasicScrollBarUI

extends

ScrollBarUI

implements

LayoutManager

,

SwingConstants

Implementation of ScrollBarUI for the Basic Look and Feel

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicScrollBarUI.ArrowButtonListener

Listener for cursor keys.

protected class

BasicScrollBarUI.ModelListener

A listener to listen for model changes.

class

BasicScrollBarUI.PropertyChangeHandler

Property change handler

protected class

BasicScrollBarUI.ScrollListener

Listener for scrolling events initiated in the

ScrollPane

.

protected class

BasicScrollBarUI.TrackListener

Track mouse drags.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

BasicScrollBarUI.ArrowButtonListener

buttonListener

Button listener

protected

JButton

decrButton

Decrement button

protected static int

DECREASE_HIGHLIGHT

Decrease highlight

protected int

decrGap

Distance between the decrement button and the track.

protected

JButton

incrButton

Increment button

protected static int

INCREASE_HIGHLIGHT

Increase highlight

protected int

incrGap

Distance between the increment button and the track.

protected boolean

isDragging

Dragging

protected

Dimension

maximumThumbSize

Maximum thumb size

protected

Dimension

minimumThumbSize

Minimum thumb size

protected

BasicScrollBarUI.ModelListener

modelListener

Model listener

protected static int

NO_HIGHLIGHT

No highlight

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

JScrollBar

scrollbar

Scrollbar

protected int

scrollBarWidth

Hint as to what width (when vertical) or height (when horizontal)
should be.

protected

BasicScrollBarUI.ScrollListener

scrollListener

Scroll listener

protected

Timer

scrollTimer

Scroll timer

protected

Color

thumbColor

Thumb color

protected

Color

thumbDarkShadowColor

Thumb dark shadow color

protected

Color

thumbHighlightColor

Thumb highlight color

protected

Color

thumbLightShadowColor

Thumb light shadow color

protected

Rectangle

thumbRect

Thumb rectangle

protected

Color

trackColor

Track color

protected int

trackHighlight

Track highlight

protected

Color

trackHighlightColor

Track highlight color

protected

BasicScrollBarUI.TrackListener

trackListener

Track listener

protected

Rectangle

trackRect

Track rectangle

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

BasicScrollBarUI

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

protected void

configureScrollBarColors

()

Configures the scroll bar colors.

protected

BasicScrollBarUI.ArrowButtonListener

createArrowButtonListener

()

Creates an arrow button listener.

protected

JButton

createDecreaseButton

​(int orientation)

Creates a decrease button.

protected

JButton

createIncreaseButton

​(int orientation)

Creates an increase button.

protected

BasicScrollBarUI.ModelListener

createModelListener

()

Creates a model listener.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a property change listener.

protected

BasicScrollBarUI.ScrollListener

createScrollListener

()

Creates a scroll listener.

protected

BasicScrollBarUI.TrackListener

createTrackListener

()

Creates a track listener.

static

ComponentUI

createUI

​(

JComponent

c)

Creates the UI.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

protected

Dimension

getMaximumThumbSize

()

Returns the largest acceptable size for the thumb.

protected

Dimension

getMinimumThumbSize

()

Returns the smallest acceptable size for the thumb.

Dimension

getPreferredSize

​(

JComponent

c)

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb.

boolean

getSupportsAbsolutePositioning

()

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

protected

Rectangle

getThumbBounds

()

Return the current size/location of the thumb.

protected

Rectangle

getTrackBounds

()

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets.

protected void

installComponents

()

Installs the components.

protected void

installDefaults

()

Installs the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Installs the listeners.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isThumbRollover

()

Returns true if the mouse is currently over the thumb.

protected void

layoutHScrollbar

​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

protected void

layoutVScrollbar

​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

protected void

paintDecreaseHighlight

​(

Graphics

g)

Paints the decrease highlight.

protected void

paintIncreaseHighlight

​(

Graphics

g)

Paints the increase highlight.

protected void

paintThumb

​(

Graphics

g,

JComponent

c,

Rectangle

thumbBounds)

Paints the thumb.

protected void

paintTrack

​(

Graphics

g,

JComponent

c,

Rectangle

trackBounds)

Paints the track.

protected void

scrollByBlock

​(int direction)

Scrolls by block.

protected void

scrollByUnit

​(int direction)

Scrolls by unit.

protected void

setThumbBounds

​(int x,
int y,
int width,
int height)

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

protected void

setThumbRollover

​(boolean active)

Sets whether or not the mouse is currently over the thumb.

protected void

uninstallComponents

()

Uninstalls the components.

protected void

uninstallDefaults

()

Uninstalls the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstall the listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

paint

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

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

BasicScrollBarUI.ArrowButtonListener

Listener for cursor keys.

protected class

BasicScrollBarUI.ModelListener

A listener to listen for model changes.

class

BasicScrollBarUI.PropertyChangeHandler

Property change handler

protected class

BasicScrollBarUI.ScrollListener

Listener for scrolling events initiated in the

ScrollPane

.

protected class

BasicScrollBarUI.TrackListener

Track mouse drags.

---

#### Nested Class Summary

Listener for cursor keys.

A listener to listen for model changes.

Property change handler

Listener for scrolling events initiated in the

ScrollPane

.

Track mouse drags.

Field Summary

Fields

Modifier and Type

Field

Description

protected

BasicScrollBarUI.ArrowButtonListener

buttonListener

Button listener

protected

JButton

decrButton

Decrement button

protected static int

DECREASE_HIGHLIGHT

Decrease highlight

protected int

decrGap

Distance between the decrement button and the track.

protected

JButton

incrButton

Increment button

protected static int

INCREASE_HIGHLIGHT

Increase highlight

protected int

incrGap

Distance between the increment button and the track.

protected boolean

isDragging

Dragging

protected

Dimension

maximumThumbSize

Maximum thumb size

protected

Dimension

minimumThumbSize

Minimum thumb size

protected

BasicScrollBarUI.ModelListener

modelListener

Model listener

protected static int

NO_HIGHLIGHT

No highlight

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

JScrollBar

scrollbar

Scrollbar

protected int

scrollBarWidth

Hint as to what width (when vertical) or height (when horizontal)
should be.

protected

BasicScrollBarUI.ScrollListener

scrollListener

Scroll listener

protected

Timer

scrollTimer

Scroll timer

protected

Color

thumbColor

Thumb color

protected

Color

thumbDarkShadowColor

Thumb dark shadow color

protected

Color

thumbHighlightColor

Thumb highlight color

protected

Color

thumbLightShadowColor

Thumb light shadow color

protected

Rectangle

thumbRect

Thumb rectangle

protected

Color

trackColor

Track color

protected int

trackHighlight

Track highlight

protected

Color

trackHighlightColor

Track highlight color

protected

BasicScrollBarUI.TrackListener

trackListener

Track listener

protected

Rectangle

trackRect

Track rectangle

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

Button listener

Decrement button

Decrease highlight

Distance between the decrement button and the track.

Increment button

Increase highlight

Distance between the increment button and the track.

Dragging

Maximum thumb size

Minimum thumb size

Model listener

No highlight

Property change listener

Scrollbar

Hint as to what width (when vertical) or height (when horizontal)
should be.

Scroll listener

Scroll timer

Thumb color

Thumb dark shadow color

Thumb highlight color

Thumb light shadow color

Thumb rectangle

Track color

Track highlight

Track highlight color

Track listener

Track rectangle

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

BasicScrollBarUI

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

protected void

configureScrollBarColors

()

Configures the scroll bar colors.

protected

BasicScrollBarUI.ArrowButtonListener

createArrowButtonListener

()

Creates an arrow button listener.

protected

JButton

createDecreaseButton

​(int orientation)

Creates a decrease button.

protected

JButton

createIncreaseButton

​(int orientation)

Creates an increase button.

protected

BasicScrollBarUI.ModelListener

createModelListener

()

Creates a model listener.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a property change listener.

protected

BasicScrollBarUI.ScrollListener

createScrollListener

()

Creates a scroll listener.

protected

BasicScrollBarUI.TrackListener

createTrackListener

()

Creates a track listener.

static

ComponentUI

createUI

​(

JComponent

c)

Creates the UI.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the specified component's maximum size appropriate for
the look and feel.

protected

Dimension

getMaximumThumbSize

()

Returns the largest acceptable size for the thumb.

protected

Dimension

getMinimumThumbSize

()

Returns the smallest acceptable size for the thumb.

Dimension

getPreferredSize

​(

JComponent

c)

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb.

boolean

getSupportsAbsolutePositioning

()

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

protected

Rectangle

getThumbBounds

()

Return the current size/location of the thumb.

protected

Rectangle

getTrackBounds

()

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets.

protected void

installComponents

()

Installs the components.

protected void

installDefaults

()

Installs the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Installs the listeners.

void

installUI

​(

JComponent

c)

Installs the UI.

boolean

isThumbRollover

()

Returns true if the mouse is currently over the thumb.

protected void

layoutHScrollbar

​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

protected void

layoutVScrollbar

​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

protected void

paintDecreaseHighlight

​(

Graphics

g)

Paints the decrease highlight.

protected void

paintIncreaseHighlight

​(

Graphics

g)

Paints the increase highlight.

protected void

paintThumb

​(

Graphics

g,

JComponent

c,

Rectangle

thumbBounds)

Paints the thumb.

protected void

paintTrack

​(

Graphics

g,

JComponent

c,

Rectangle

trackBounds)

Paints the track.

protected void

scrollByBlock

​(int direction)

Scrolls by block.

protected void

scrollByUnit

​(int direction)

Scrolls by unit.

protected void

setThumbBounds

​(int x,
int y,
int width,
int height)

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

protected void

setThumbRollover

​(boolean active)

Sets whether or not the mouse is currently over the thumb.

protected void

uninstallComponents

()

Uninstalls the components.

protected void

uninstallDefaults

()

Uninstalls the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstall the listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls the UI.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

paint

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

- Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Method Summary

Configures the scroll bar colors.

Creates an arrow button listener.

Creates a decrease button.

Creates an increase button.

Creates a model listener.

Creates a property change listener.

Creates a scroll listener.

Creates a track listener.

Creates the UI.

Returns the specified component's maximum size appropriate for
the look and feel.

Returns the largest acceptable size for the thumb.

Returns the smallest acceptable size for the thumb.

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb.

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

Return the current size/location of the thumb.

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets.

Installs the components.

Installs the defaults.

Installs the keyboard actions.

Installs the listeners.

Installs the UI.

Returns true if the mouse is currently over the thumb.

Laysouts a vertical scroll bar.

Paints the decrease highlight.

Paints the increase highlight.

Paints the thumb.

Paints the track.

Scrolls by block.

Scrolls by unit.

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

Sets whether or not the mouse is currently over the thumb.

Uninstalls the components.

Uninstalls the defaults.

Uninstalls the keyboard actions.

Uninstall the listeners.

Uninstalls the UI.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMinimumSize

,

paint

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

Methods declared in interface java.awt.

LayoutManager

addLayoutComponent

,

layoutContainer

,

minimumLayoutSize

,

preferredLayoutSize

,

removeLayoutComponent

---

#### Methods declared in interface java.awt. LayoutManager

============ FIELD DETAIL ===========

- Field Detail

- minimumThumbSize

```java
protected
Dimension
minimumThumbSize
```

Minimum thumb size

- maximumThumbSize

```java
protected
Dimension
maximumThumbSize
```

Maximum thumb size

- thumbHighlightColor

```java
protected
Color
thumbHighlightColor
```

Thumb highlight color

- thumbLightShadowColor

```java
protected
Color
thumbLightShadowColor
```

Thumb light shadow color

- thumbDarkShadowColor

```java
protected
Color
thumbDarkShadowColor
```

Thumb dark shadow color

- thumbColor

```java
protected
Color
thumbColor
```

Thumb color

- trackColor

```java
protected
Color
trackColor
```

Track color

- trackHighlightColor

```java
protected
Color
trackHighlightColor
```

Track highlight color

- scrollbar

```java
protected
JScrollBar
scrollbar
```

Scrollbar

- incrButton

```java
protected
JButton
incrButton
```

Increment button

- decrButton

```java
protected
JButton
decrButton
```

Decrement button

- isDragging

```java
protected boolean isDragging
```

Dragging

- trackListener

```java
protected
BasicScrollBarUI.TrackListener
trackListener
```

Track listener

- buttonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
buttonListener
```

Button listener

- modelListener

```java
protected
BasicScrollBarUI.ModelListener
modelListener
```

Model listener

- thumbRect

```java
protected
Rectangle
thumbRect
```

Thumb rectangle

- trackRect

```java
protected
Rectangle
trackRect
```

Track rectangle

- trackHighlight

```java
protected int trackHighlight
```

Track highlight

- NO_HIGHLIGHT

```java
protected static final int NO_HIGHLIGHT
```

No highlight

**See Also:** Constant Field Values

- DECREASE_HIGHLIGHT

```java
protected static final int DECREASE_HIGHLIGHT
```

Decrease highlight

**See Also:** Constant Field Values

- INCREASE_HIGHLIGHT

```java
protected static final int INCREASE_HIGHLIGHT
```

Increase highlight

**See Also:** Constant Field Values

- scrollListener

```java
protected
BasicScrollBarUI.ScrollListener
scrollListener
```

Scroll listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- scrollTimer

```java
protected
Timer
scrollTimer
```

Scroll timer

- scrollBarWidth

```java
protected int scrollBarWidth
```

Hint as to what width (when vertical) or height (when horizontal)
should be.

**Since:** 1.7

- incrGap

```java
protected int incrGap
```

Distance between the increment button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

- decrGap

```java
protected int decrGap
```

Distance between the decrement button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicScrollBarUI

```java
public BasicScrollBarUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the UI.

**Parameters:** c

- the component
**Returns:** the UI

- configureScrollBarColors

```java
protected void configureScrollBarColors()
```

Configures the scroll bar colors.

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

- installComponents

```java
protected void installComponents()
```

Installs the components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

- installListeners

```java
protected void installListeners()
```

Installs the listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

- createTrackListener

```java
protected
BasicScrollBarUI.TrackListener
createTrackListener()
```

Creates a track listener.

**Returns:** a track listener

- createArrowButtonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
createArrowButtonListener()
```

Creates an arrow button listener.

**Returns:** an arrow button listener

- createModelListener

```java
protected
BasicScrollBarUI.ModelListener
createModelListener()
```

Creates a model listener.

**Returns:** a model listener

- createScrollListener

```java
protected
BasicScrollBarUI.ScrollListener
createScrollListener()
```

Creates a scroll listener.

**Returns:** a scroll listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a property change listener.

**Returns:** a property change listener

- setThumbRollover

```java
protected void setThumbRollover​(boolean active)
```

Sets whether or not the mouse is currently over the thumb.

**Parameters:** active

- True indicates the thumb is currently active.
**Since:** 1.5

- isThumbRollover

```java
public boolean isThumbRollover()
```

Returns true if the mouse is currently over the thumb.

**Returns:** true if the thumb is currently active
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb. The preferred height is the
sum of the preferred heights of the same parts. The basis for
the preferred size of a horizontal scrollbar is similar.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the

JScrollBar

that's delegating this method to us
**Returns:** the preferred size of a Basic JScrollBar
**See Also:** getMaximumSize(javax.swing.JComponent)

,

ComponentUI.getMinimumSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- The JScrollBar that's delegating this method to us.
**Returns:** new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE);
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

,

getPreferredSize(javax.swing.JComponent)

- createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Creates a decrease button.

**Parameters:** orientation

- the orientation
**Returns:** a decrease button

- createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Creates an increase button.

**Parameters:** orientation

- the orientation
**Returns:** an increase button

- paintDecreaseHighlight

```java
protected void paintDecreaseHighlight​(
Graphics
g)
```

Paints the decrease highlight.

**Parameters:** g

- the graphics

- paintIncreaseHighlight

```java
protected void paintIncreaseHighlight​(
Graphics
g)
```

Paints the increase highlight.

**Parameters:** g

- the graphics

- paintTrack

```java
protected void paintTrack​(
Graphics
g,

JComponent
c,

Rectangle
trackBounds)
```

Paints the track.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** trackBounds

- the track bounds

- paintThumb

```java
protected void paintThumb​(
Graphics
g,

JComponent
c,

Rectangle
thumbBounds)
```

Paints the thumb.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** thumbBounds

- the thumb bounds

- getMinimumThumbSize

```java
protected
Dimension
getMinimumThumbSize()
```

Returns the smallest acceptable size for the thumb. If the scrollbar
becomes so small that this size isn't available, the thumb will be
hidden.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The smallest acceptable size for the thumb.
**See Also:** getMaximumThumbSize()

- getMaximumThumbSize

```java
protected
Dimension
getMaximumThumbSize()
```

Returns the largest acceptable size for the thumb. To create a fixed
size thumb one make this method and

getMinimumThumbSize

return the same value.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The largest acceptable size for the thumb.
**See Also:** getMinimumThumbSize()

- layoutVScrollbar

```java
protected void layoutVScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

- layoutHScrollbar

```java
protected void layoutHScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

- setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** getThumbBounds()

- getThumbBounds

```java
protected
Rectangle
getThumbBounds()
```

Return the current size/location of the thumb.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** The current size/location of the thumb.
**See Also:** setThumbBounds(int, int, int, int)

- getTrackBounds

```java
protected
Rectangle
getTrackBounds()
```

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets. The value
returned by this method is updated each time the scrollbar is
laid out (validated).

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** the current bounds of the scrollbar track
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

- scrollByBlock

```java
protected void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction to scroll

- scrollByUnit

```java
protected void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction to scroll

- getSupportsAbsolutePositioning

```java
public boolean getSupportsAbsolutePositioning()
```

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

**Returns:** true if a mouse gesture can absolutely position the thumb
**Since:** 1.5

Field Detail

- minimumThumbSize

```java
protected
Dimension
minimumThumbSize
```

Minimum thumb size

- maximumThumbSize

```java
protected
Dimension
maximumThumbSize
```

Maximum thumb size

- thumbHighlightColor

```java
protected
Color
thumbHighlightColor
```

Thumb highlight color

- thumbLightShadowColor

```java
protected
Color
thumbLightShadowColor
```

Thumb light shadow color

- thumbDarkShadowColor

```java
protected
Color
thumbDarkShadowColor
```

Thumb dark shadow color

- thumbColor

```java
protected
Color
thumbColor
```

Thumb color

- trackColor

```java
protected
Color
trackColor
```

Track color

- trackHighlightColor

```java
protected
Color
trackHighlightColor
```

Track highlight color

- scrollbar

```java
protected
JScrollBar
scrollbar
```

Scrollbar

- incrButton

```java
protected
JButton
incrButton
```

Increment button

- decrButton

```java
protected
JButton
decrButton
```

Decrement button

- isDragging

```java
protected boolean isDragging
```

Dragging

- trackListener

```java
protected
BasicScrollBarUI.TrackListener
trackListener
```

Track listener

- buttonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
buttonListener
```

Button listener

- modelListener

```java
protected
BasicScrollBarUI.ModelListener
modelListener
```

Model listener

- thumbRect

```java
protected
Rectangle
thumbRect
```

Thumb rectangle

- trackRect

```java
protected
Rectangle
trackRect
```

Track rectangle

- trackHighlight

```java
protected int trackHighlight
```

Track highlight

- NO_HIGHLIGHT

```java
protected static final int NO_HIGHLIGHT
```

No highlight

**See Also:** Constant Field Values

- DECREASE_HIGHLIGHT

```java
protected static final int DECREASE_HIGHLIGHT
```

Decrease highlight

**See Also:** Constant Field Values

- INCREASE_HIGHLIGHT

```java
protected static final int INCREASE_HIGHLIGHT
```

Increase highlight

**See Also:** Constant Field Values

- scrollListener

```java
protected
BasicScrollBarUI.ScrollListener
scrollListener
```

Scroll listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- scrollTimer

```java
protected
Timer
scrollTimer
```

Scroll timer

- scrollBarWidth

```java
protected int scrollBarWidth
```

Hint as to what width (when vertical) or height (when horizontal)
should be.

**Since:** 1.7

- incrGap

```java
protected int incrGap
```

Distance between the increment button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

- decrGap

```java
protected int decrGap
```

Distance between the decrement button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

---

#### Field Detail

minimumThumbSize

```java
protected
Dimension
minimumThumbSize
```

Minimum thumb size

---

#### minimumThumbSize

protected

Dimension

minimumThumbSize

Minimum thumb size

maximumThumbSize

```java
protected
Dimension
maximumThumbSize
```

Maximum thumb size

---

#### maximumThumbSize

protected

Dimension

maximumThumbSize

Maximum thumb size

thumbHighlightColor

```java
protected
Color
thumbHighlightColor
```

Thumb highlight color

---

#### thumbHighlightColor

protected

Color

thumbHighlightColor

Thumb highlight color

thumbLightShadowColor

```java
protected
Color
thumbLightShadowColor
```

Thumb light shadow color

---

#### thumbLightShadowColor

protected

Color

thumbLightShadowColor

Thumb light shadow color

thumbDarkShadowColor

```java
protected
Color
thumbDarkShadowColor
```

Thumb dark shadow color

---

#### thumbDarkShadowColor

protected

Color

thumbDarkShadowColor

Thumb dark shadow color

thumbColor

```java
protected
Color
thumbColor
```

Thumb color

---

#### thumbColor

protected

Color

thumbColor

Thumb color

trackColor

```java
protected
Color
trackColor
```

Track color

---

#### trackColor

protected

Color

trackColor

Track color

trackHighlightColor

```java
protected
Color
trackHighlightColor
```

Track highlight color

---

#### trackHighlightColor

protected

Color

trackHighlightColor

Track highlight color

scrollbar

```java
protected
JScrollBar
scrollbar
```

Scrollbar

---

#### scrollbar

protected

JScrollBar

scrollbar

Scrollbar

incrButton

```java
protected
JButton
incrButton
```

Increment button

---

#### incrButton

protected

JButton

incrButton

Increment button

decrButton

```java
protected
JButton
decrButton
```

Decrement button

---

#### decrButton

protected

JButton

decrButton

Decrement button

isDragging

```java
protected boolean isDragging
```

Dragging

---

#### isDragging

protected boolean isDragging

Dragging

trackListener

```java
protected
BasicScrollBarUI.TrackListener
trackListener
```

Track listener

---

#### trackListener

protected

BasicScrollBarUI.TrackListener

trackListener

Track listener

buttonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
buttonListener
```

Button listener

---

#### buttonListener

protected

BasicScrollBarUI.ArrowButtonListener

buttonListener

Button listener

modelListener

```java
protected
BasicScrollBarUI.ModelListener
modelListener
```

Model listener

---

#### modelListener

protected

BasicScrollBarUI.ModelListener

modelListener

Model listener

thumbRect

```java
protected
Rectangle
thumbRect
```

Thumb rectangle

---

#### thumbRect

protected

Rectangle

thumbRect

Thumb rectangle

trackRect

```java
protected
Rectangle
trackRect
```

Track rectangle

---

#### trackRect

protected

Rectangle

trackRect

Track rectangle

trackHighlight

```java
protected int trackHighlight
```

Track highlight

---

#### trackHighlight

protected int trackHighlight

Track highlight

NO_HIGHLIGHT

```java
protected static final int NO_HIGHLIGHT
```

No highlight

**See Also:** Constant Field Values

---

#### NO_HIGHLIGHT

protected static final int NO_HIGHLIGHT

No highlight

DECREASE_HIGHLIGHT

```java
protected static final int DECREASE_HIGHLIGHT
```

Decrease highlight

**See Also:** Constant Field Values

---

#### DECREASE_HIGHLIGHT

protected static final int DECREASE_HIGHLIGHT

Decrease highlight

INCREASE_HIGHLIGHT

```java
protected static final int INCREASE_HIGHLIGHT
```

Increase highlight

**See Also:** Constant Field Values

---

#### INCREASE_HIGHLIGHT

protected static final int INCREASE_HIGHLIGHT

Increase highlight

scrollListener

```java
protected
BasicScrollBarUI.ScrollListener
scrollListener
```

Scroll listener

---

#### scrollListener

protected

BasicScrollBarUI.ScrollListener

scrollListener

Scroll listener

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

Property change listener

scrollTimer

```java
protected
Timer
scrollTimer
```

Scroll timer

---

#### scrollTimer

protected

Timer

scrollTimer

Scroll timer

scrollBarWidth

```java
protected int scrollBarWidth
```

Hint as to what width (when vertical) or height (when horizontal)
should be.

**Since:** 1.7

---

#### scrollBarWidth

protected int scrollBarWidth

Hint as to what width (when vertical) or height (when horizontal)
should be.

incrGap

```java
protected int incrGap
```

Distance between the increment button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

---

#### incrGap

protected int incrGap

Distance between the increment button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

decrGap

```java
protected int decrGap
```

Distance between the decrement button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

**Since:** 1.7

---

#### decrGap

protected int decrGap

Distance between the decrement button and the track. This may be a negative
number. If negative, then an overlap between the button and track will occur,
which is useful for shaped buttons.

Constructor Detail

- BasicScrollBarUI

```java
public BasicScrollBarUI()
```

---

#### Constructor Detail

BasicScrollBarUI

```java
public BasicScrollBarUI()
```

---

#### BasicScrollBarUI

public BasicScrollBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the UI.

**Parameters:** c

- the component
**Returns:** the UI

- configureScrollBarColors

```java
protected void configureScrollBarColors()
```

Configures the scroll bar colors.

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

- installComponents

```java
protected void installComponents()
```

Installs the components.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

- installListeners

```java
protected void installListeners()
```

Installs the listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

- createTrackListener

```java
protected
BasicScrollBarUI.TrackListener
createTrackListener()
```

Creates a track listener.

**Returns:** a track listener

- createArrowButtonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
createArrowButtonListener()
```

Creates an arrow button listener.

**Returns:** an arrow button listener

- createModelListener

```java
protected
BasicScrollBarUI.ModelListener
createModelListener()
```

Creates a model listener.

**Returns:** a model listener

- createScrollListener

```java
protected
BasicScrollBarUI.ScrollListener
createScrollListener()
```

Creates a scroll listener.

**Returns:** a scroll listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a property change listener.

**Returns:** a property change listener

- setThumbRollover

```java
protected void setThumbRollover​(boolean active)
```

Sets whether or not the mouse is currently over the thumb.

**Parameters:** active

- True indicates the thumb is currently active.
**Since:** 1.5

- isThumbRollover

```java
public boolean isThumbRollover()
```

Returns true if the mouse is currently over the thumb.

**Returns:** true if the thumb is currently active
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb. The preferred height is the
sum of the preferred heights of the same parts. The basis for
the preferred size of a horizontal scrollbar is similar.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the

JScrollBar

that's delegating this method to us
**Returns:** the preferred size of a Basic JScrollBar
**See Also:** getMaximumSize(javax.swing.JComponent)

,

ComponentUI.getMinimumSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- The JScrollBar that's delegating this method to us.
**Returns:** new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE);
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

,

getPreferredSize(javax.swing.JComponent)

- createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Creates a decrease button.

**Parameters:** orientation

- the orientation
**Returns:** a decrease button

- createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Creates an increase button.

**Parameters:** orientation

- the orientation
**Returns:** an increase button

- paintDecreaseHighlight

```java
protected void paintDecreaseHighlight​(
Graphics
g)
```

Paints the decrease highlight.

**Parameters:** g

- the graphics

- paintIncreaseHighlight

```java
protected void paintIncreaseHighlight​(
Graphics
g)
```

Paints the increase highlight.

**Parameters:** g

- the graphics

- paintTrack

```java
protected void paintTrack​(
Graphics
g,

JComponent
c,

Rectangle
trackBounds)
```

Paints the track.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** trackBounds

- the track bounds

- paintThumb

```java
protected void paintThumb​(
Graphics
g,

JComponent
c,

Rectangle
thumbBounds)
```

Paints the thumb.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** thumbBounds

- the thumb bounds

- getMinimumThumbSize

```java
protected
Dimension
getMinimumThumbSize()
```

Returns the smallest acceptable size for the thumb. If the scrollbar
becomes so small that this size isn't available, the thumb will be
hidden.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The smallest acceptable size for the thumb.
**See Also:** getMaximumThumbSize()

- getMaximumThumbSize

```java
protected
Dimension
getMaximumThumbSize()
```

Returns the largest acceptable size for the thumb. To create a fixed
size thumb one make this method and

getMinimumThumbSize

return the same value.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The largest acceptable size for the thumb.
**See Also:** getMinimumThumbSize()

- layoutVScrollbar

```java
protected void layoutVScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

- layoutHScrollbar

```java
protected void layoutHScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

- setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** getThumbBounds()

- getThumbBounds

```java
protected
Rectangle
getThumbBounds()
```

Return the current size/location of the thumb.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** The current size/location of the thumb.
**See Also:** setThumbBounds(int, int, int, int)

- getTrackBounds

```java
protected
Rectangle
getTrackBounds()
```

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets. The value
returned by this method is updated each time the scrollbar is
laid out (validated).

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** the current bounds of the scrollbar track
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

- scrollByBlock

```java
protected void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction to scroll

- scrollByUnit

```java
protected void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction to scroll

- getSupportsAbsolutePositioning

```java
public boolean getSupportsAbsolutePositioning()
```

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

**Returns:** true if a mouse gesture can absolutely position the thumb
**Since:** 1.5

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates the UI.

**Parameters:** c

- the component
**Returns:** the UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates the UI.

configureScrollBarColors

```java
protected void configureScrollBarColors()
```

Configures the scroll bar colors.

---

#### configureScrollBarColors

protected void configureScrollBarColors()

Configures the scroll bar colors.

installUI

```java
public void installUI​(
JComponent
c)
```

Installs the UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.uninstallUI(javax.swing.JComponent)

,

JComponent.setUI(javax.swing.plaf.ComponentUI)

,

JComponent.updateUI()

---

#### installUI

public void installUI​(

JComponent

c)

Installs the UI.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls the UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Uninstalls the UI.

installDefaults

```java
protected void installDefaults()
```

Installs the defaults.

---

#### installDefaults

protected void installDefaults()

Installs the defaults.

installComponents

```java
protected void installComponents()
```

Installs the components.

---

#### installComponents

protected void installComponents()

Installs the components.

uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the components.

---

#### uninstallComponents

protected void uninstallComponents()

Uninstalls the components.

installListeners

```java
protected void installListeners()
```

Installs the listeners.

---

#### installListeners

protected void installListeners()

Installs the listeners.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Installs the keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Installs the keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Uninstalls the keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Uninstalls the keyboard actions.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Uninstall the listeners.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls the defaults.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls the defaults.

createTrackListener

```java
protected
BasicScrollBarUI.TrackListener
createTrackListener()
```

Creates a track listener.

**Returns:** a track listener

---

#### createTrackListener

protected

BasicScrollBarUI.TrackListener

createTrackListener()

Creates a track listener.

createArrowButtonListener

```java
protected
BasicScrollBarUI.ArrowButtonListener
createArrowButtonListener()
```

Creates an arrow button listener.

**Returns:** an arrow button listener

---

#### createArrowButtonListener

protected

BasicScrollBarUI.ArrowButtonListener

createArrowButtonListener()

Creates an arrow button listener.

createModelListener

```java
protected
BasicScrollBarUI.ModelListener
createModelListener()
```

Creates a model listener.

**Returns:** a model listener

---

#### createModelListener

protected

BasicScrollBarUI.ModelListener

createModelListener()

Creates a model listener.

createScrollListener

```java
protected
BasicScrollBarUI.ScrollListener
createScrollListener()
```

Creates a scroll listener.

**Returns:** a scroll listener

---

#### createScrollListener

protected

BasicScrollBarUI.ScrollListener

createScrollListener()

Creates a scroll listener.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a property change listener.

**Returns:** a property change listener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a property change listener.

setThumbRollover

```java
protected void setThumbRollover​(boolean active)
```

Sets whether or not the mouse is currently over the thumb.

**Parameters:** active

- True indicates the thumb is currently active.
**Since:** 1.5

---

#### setThumbRollover

protected void setThumbRollover​(boolean active)

Sets whether or not the mouse is currently over the thumb.

isThumbRollover

```java
public boolean isThumbRollover()
```

Returns true if the mouse is currently over the thumb.

**Returns:** true if the thumb is currently active
**Since:** 1.5

---

#### isThumbRollover

public boolean isThumbRollover()

Returns true if the mouse is currently over the thumb.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb. The preferred height is the
sum of the preferred heights of the same parts. The basis for
the preferred size of a horizontal scrollbar is similar.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- the

JScrollBar

that's delegating this method to us
**Returns:** the preferred size of a Basic JScrollBar
**See Also:** getMaximumSize(javax.swing.JComponent)

,

ComponentUI.getMinimumSize(javax.swing.JComponent)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c)

A vertical scrollbar's preferred width is the maximum of
preferred widths of the (non

null

)
increment/decrement buttons,
and the minimum width of the thumb. The preferred height is the
sum of the preferred heights of the same parts. The basis for
the preferred size of a horizontal scrollbar is similar.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

The

preferredSize

is only computed once, subsequent
calls to this method just return a cached size.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- The JScrollBar that's delegating this method to us.
**Returns:** new Dimension(Integer.MAX_VALUE, Integer.MAX_VALUE);
**See Also:** ComponentUI.getMinimumSize(javax.swing.JComponent)

,

getPreferredSize(javax.swing.JComponent)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Description copied from class:

ComponentUI

Returns the specified component's maximum size appropriate for
the look and feel. If

null

is returned, the maximum
size will be calculated by the component's layout manager instead
(this is the preferred approach for any component with a specific
layout manager installed). The default implementation of this
method invokes

getPreferredSize

and returns that value.

createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Creates a decrease button.

**Parameters:** orientation

- the orientation
**Returns:** a decrease button

---

#### createDecreaseButton

protected

JButton

createDecreaseButton​(int orientation)

Creates a decrease button.

createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Creates an increase button.

**Parameters:** orientation

- the orientation
**Returns:** an increase button

---

#### createIncreaseButton

protected

JButton

createIncreaseButton​(int orientation)

Creates an increase button.

paintDecreaseHighlight

```java
protected void paintDecreaseHighlight​(
Graphics
g)
```

Paints the decrease highlight.

**Parameters:** g

- the graphics

---

#### paintDecreaseHighlight

protected void paintDecreaseHighlight​(

Graphics

g)

Paints the decrease highlight.

paintIncreaseHighlight

```java
protected void paintIncreaseHighlight​(
Graphics
g)
```

Paints the increase highlight.

**Parameters:** g

- the graphics

---

#### paintIncreaseHighlight

protected void paintIncreaseHighlight​(

Graphics

g)

Paints the increase highlight.

paintTrack

```java
protected void paintTrack​(
Graphics
g,

JComponent
c,

Rectangle
trackBounds)
```

Paints the track.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** trackBounds

- the track bounds

---

#### paintTrack

protected void paintTrack​(

Graphics

g,

JComponent

c,

Rectangle

trackBounds)

Paints the track.

paintThumb

```java
protected void paintThumb​(
Graphics
g,

JComponent
c,

Rectangle
thumbBounds)
```

Paints the thumb.

**Parameters:** g

- the graphics
**Parameters:** c

- the component
**Parameters:** thumbBounds

- the thumb bounds

---

#### paintThumb

protected void paintThumb​(

Graphics

g,

JComponent

c,

Rectangle

thumbBounds)

Paints the thumb.

getMinimumThumbSize

```java
protected
Dimension
getMinimumThumbSize()
```

Returns the smallest acceptable size for the thumb. If the scrollbar
becomes so small that this size isn't available, the thumb will be
hidden.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The smallest acceptable size for the thumb.
**See Also:** getMaximumThumbSize()

---

#### getMinimumThumbSize

protected

Dimension

getMinimumThumbSize()

Returns the smallest acceptable size for the thumb. If the scrollbar
becomes so small that this size isn't available, the thumb will be
hidden.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

getMaximumThumbSize

```java
protected
Dimension
getMaximumThumbSize()
```

Returns the largest acceptable size for the thumb. To create a fixed
size thumb one make this method and

getMinimumThumbSize

return the same value.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

**Returns:** The largest acceptable size for the thumb.
**See Also:** getMinimumThumbSize()

---

#### getMaximumThumbSize

protected

Dimension

getMaximumThumbSize()

Returns the largest acceptable size for the thumb. To create a fixed
size thumb one make this method and

getMinimumThumbSize

return the same value.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

Warning

: the value returned by this method should not be
be modified, it's a shared static constant.

layoutVScrollbar

```java
protected void layoutVScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

---

#### layoutVScrollbar

protected void layoutVScrollbar​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

layoutHScrollbar

```java
protected void layoutHScrollbar​(
JScrollBar
sb)
```

Laysouts a vertical scroll bar.

**Parameters:** sb

- the scroll bar

---

#### layoutHScrollbar

protected void layoutHScrollbar​(

JScrollBar

sb)

Laysouts a vertical scroll bar.

setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** getThumbBounds()

---

#### setThumbBounds

protected void setThumbBounds​(int x,
int y,
int width,
int height)

Set the bounds of the thumb and force a repaint that includes
the old thumbBounds and the new one.

getThumbBounds

```java
protected
Rectangle
getThumbBounds()
```

Return the current size/location of the thumb.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** The current size/location of the thumb.
**See Also:** setThumbBounds(int, int, int, int)

---

#### getThumbBounds

protected

Rectangle

getThumbBounds()

Return the current size/location of the thumb.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

getTrackBounds

```java
protected
Rectangle
getTrackBounds()
```

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets. The value
returned by this method is updated each time the scrollbar is
laid out (validated).

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

**Returns:** the current bounds of the scrollbar track
**See Also:** LayoutManager.layoutContainer(java.awt.Container)

---

#### getTrackBounds

protected

Rectangle

getTrackBounds()

Returns the current bounds of the track, i.e. the space in between
the increment and decrement buttons, less the insets. The value
returned by this method is updated each time the scrollbar is
laid out (validated).

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

Warning

: the value returned by this method should not be
be modified, it's a reference to the actual rectangle, not a copy.

scrollByBlock

```java
protected void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction to scroll

---

#### scrollByBlock

protected void scrollByBlock​(int direction)

Scrolls by block.

scrollByUnit

```java
protected void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction to scroll

---

#### scrollByUnit

protected void scrollByUnit​(int direction)

Scrolls by unit.

getSupportsAbsolutePositioning

```java
public boolean getSupportsAbsolutePositioning()
```

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

**Returns:** true if a mouse gesture can absolutely position the thumb
**Since:** 1.5

---

#### getSupportsAbsolutePositioning

public boolean getSupportsAbsolutePositioning()

Indicates whether the user can absolutely position the thumb with
a mouse gesture (usually the middle mouse button).

---

