# Class BasicSliderUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicSliderUI.html`

### Class Description

```java
public class
BasicSliderUI

extends
SliderUI
```

A Basic L&F implementation of SliderUI.

**Direct Known Subclasses:** MetalSliderUI

,

SynthSliderUI

---

### Field Details

#### public static final int POSITIVE_SCROLL

Positive scroll

**See Also:**
- Constant Field Values

---

#### public static final int NEGATIVE_SCROLL

Negative scroll

**See Also:**
- Constant Field Values

---

#### public static final int MIN_SCROLL

Minimum scroll

**See Also:**
- Constant Field Values

---

#### public static final int MAX_SCROLL

Maximum scroll

**See Also:**
- Constant Field Values

---

#### protected
Timer
scrollTimer

Scroll timer

---

#### protected
JSlider
slider

Slider

---

#### protected
Insets
focusInsets

Focus insets

---

#### protected
Insets
insetCache

Inset cache

---

#### protected boolean leftToRightCache

Left-to-right cache

---

#### protected
Rectangle
focusRect

Focus rectangle

---

#### protected
Rectangle
contentRect

Content rectangle

---

#### protected
Rectangle
labelRect

Label rectangle

---

#### protected
Rectangle
tickRect

Tick rectangle

---

#### protected
Rectangle
trackRect

Track rectangle

---

#### protected
Rectangle
thumbRect

Thumb rectangle

---

#### protected int trackBuffer

The distance that the track is from the side of the control

---

#### protected
BasicSliderUI.TrackListener
trackListener

Track listener

---

#### protected
ChangeListener
changeListener

Change listener

---

#### protected
ComponentListener
componentListener

Component listener

---

#### protected
FocusListener
focusListener

Focus listener

---

#### protected
BasicSliderUI.ScrollListener
scrollListener

Scroll listener

---

#### protected
PropertyChangeListener
propertyChangeListener

Property chane listener

---

### Constructor Details

#### public BasicSliderUI​(
JSlider
b)

Constructs a

BasicSliderUI

.

**Parameters:**
- b

- a slider

---

### Method Details

#### protected
Color
getShadowColor()

Returns the shadow color.

**Returns:**
- the shadow color

---

#### protected
Color
getHighlightColor()

Returns the highlight color.

**Returns:**
- the highlight color

---

#### protected
Color
getFocusColor()

Returns the focus color.

**Returns:**
- the focus color

---

#### protected boolean isDragging()

Returns true if the user is dragging the slider.

**Returns:**
- true if the user is dragging the slider

**Since:**
- 1.5

---

#### public static
ComponentUI
createUI​(
JComponent
b)

Creates a UI.

**Parameters:**
- b

- a component

**Returns:**
- a UI

---

#### public void installUI​(
JComponent
c)

Installs a UI.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- a component

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

Uninstalls a UI.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- a component

**See Also:**
- ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### protected void installDefaults​(
JSlider
slider)

Installs the defaults.

**Parameters:**
- slider

- a slider

---

#### protected void uninstallDefaults​(
JSlider
slider)

Uninstalls the defaults.

**Parameters:**
- slider

- a slider

---

#### protected
BasicSliderUI.TrackListener
createTrackListener​(
JSlider
slider)

Creates a track listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a track listener

---

#### protected
ChangeListener
createChangeListener​(
JSlider
slider)

Creates a change listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a change listener

---

#### protected
ComponentListener
createComponentListener​(
JSlider
slider)

Creates a composite listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a composite listener

---

#### protected
FocusListener
createFocusListener​(
JSlider
slider)

Creates a focus listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a focus listener

---

#### protected
BasicSliderUI.ScrollListener
createScrollListener​(
JSlider
slider)

Creates a scroll listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a scroll listener

---

#### protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)

Creates a property change listener.

**Parameters:**
- slider

- a slider

**Returns:**
- a property change listener

---

#### protected void installListeners​(
JSlider
slider)

Installs listeners.

**Parameters:**
- slider

- a slider

---

#### protected void uninstallListeners​(
JSlider
slider)

Uninstalls listeners.

**Parameters:**
- slider

- a slider

---

#### protected void installKeyboardActions​(
JSlider
slider)

Installs keyboard actions.

**Parameters:**
- slider

- a slider

---

#### protected void uninstallKeyboardActions​(
JSlider
slider)

Uninstalls keyboard actions.

**Parameters:**
- slider

- a slider

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

#### protected boolean labelsHaveSameBaselines()

Returns true if all the labels from the label table have the same
baseline.

**Returns:**
- true if all the labels from the label table have the
same baseline

**Since:**
- 1.6

---

#### public
Dimension
getPreferredHorizontalSize()

Returns the preferred horizontal size.

**Returns:**
- the preferred horizontal size

---

#### public
Dimension
getPreferredVerticalSize()

Returns the preferred vertical size.

**Returns:**
- the preferred vertical size

---

#### public
Dimension
getMinimumHorizontalSize()

Returns the minimum horizontal size.

**Returns:**
- the minimum horizontal size

---

#### public
Dimension
getMinimumVerticalSize()

Returns the minimum vertical size.

**Returns:**
- the minimum vertical size

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

Returns the preferred size.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- a component

**Returns:**
- the preferred size

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

Returns the minimum size.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- a component

**Returns:**
- the minimum size

**See Also:**
- JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

---

#### public
Dimension
getMaximumSize​(
JComponent
c)

Returns the maximum size.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- a component

**Returns:**
- the maximum size

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### protected void calculateGeometry()

Calculates the geometry.

---

#### protected void calculateFocusRect()

Calculates the focus rectangle.

---

#### protected void calculateThumbSize()

Calculates the thumb size rectangle.

---

#### protected void calculateContentRect()

Calculates the content rectangle.

---

#### protected void calculateThumbLocation()

Calculates the thumb location.

---

#### protected void calculateTrackBuffer()

Calculates the track buffer.

---

#### protected void calculateTrackRect()

Calculates the track rectangle.

---

#### protected int getTickLength()

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders. BasicSliderUI uses the returned value
to determine the tick area rectangle. If you want to give your ticks some
room, make this larger than you need and paint your ticks away from the
sides in paintTicks().

**Returns:**
- an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

---

#### protected void calculateTickRect()

Calculates the tick rectangle.

---

#### protected void calculateLabelRect()

Calculates the label rectangle.

---

#### protected
Dimension
getThumbSize()

Returns the thumb size.

**Returns:**
- the thumb size

---

#### protected int getWidthOfWidestLabel()

Returns the width of the widest label.

**Returns:**
- the width of the widest label

---

#### protected int getHeightOfTallestLabel()

Returns the height of the tallest label.

**Returns:**
- the height of the tallest label

---

#### protected int getWidthOfHighValueLabel()

Returns the width of the highest value label.

**Returns:**
- the width of the highest value label

---

#### protected int getWidthOfLowValueLabel()

Returns the width of the lowest value label.

**Returns:**
- the width of the lowest value label

---

#### protected int getHeightOfHighValueLabel()

Returns the height of the highest value label.

**Returns:**
- the height of the highest value label

---

#### protected int getHeightOfLowValueLabel()

Returns the height of the lowest value label.

**Returns:**
- the height of the lowest value label

---

#### protected boolean drawInverted()

Draws inverted.

**Returns:**
- the inverted-ness

---

#### protected
Integer
getHighestValue()

Returns the biggest value that has an entry in the label table.

**Returns:**
- biggest value that has an entry in the label table, or
null.

**Since:**
- 1.6

---

#### protected
Integer
getLowestValue()

Returns the smallest value that has an entry in the label table.

**Returns:**
- smallest value that has an entry in the label table, or
null.

**Since:**
- 1.6

---

#### protected
Component
getLowestValueLabel()

Returns the label that corresponds to the highest slider value in the
label table.

**Returns:**
- the label that corresponds to the highest slider value in the
label table

**See Also:**
- JSlider.setLabelTable(java.util.Dictionary)

---

#### protected
Component
getHighestValueLabel()

Returns the label that corresponds to the lowest slider value in the
label table.

**Returns:**
- the label that corresponds to the lowest slider value in the
label table

**See Also:**
- JSlider.setLabelTable(java.util.Dictionary)

---

#### protected void recalculateIfInsetsChanged()

Recalculates if the insets have changed.

---

#### protected void recalculateIfOrientationChanged()

Recalculates if the orientation has changed.

---

#### public void paintFocus​(
Graphics
g)

Paints focus.

**Parameters:**
- g

- the graphics

---

#### public void paintTrack​(
Graphics
g)

Paints track.

**Parameters:**
- g

- the graphics

---

#### public void paintTicks​(
Graphics
g)

Paints ticks.

**Parameters:**
- g

- the graphics

---

#### protected void paintMinorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)

Paints minor tick for horizontal slider.

**Parameters:**
- g

- the graphics
- tickBounds

- the tick bounds
- x

- the x coordinate

---

#### protected void paintMajorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)

Paints major tick for horizontal slider.

**Parameters:**
- g

- the graphics
- tickBounds

- the tick bounds
- x

- the x coordinate

---

#### protected void paintMinorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)

Paints minor tick for vertical slider.

**Parameters:**
- g

- the graphics
- tickBounds

- the tick bounds
- y

- the y coordinate

---

#### protected void paintMajorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)

Paints major tick for vertical slider.

**Parameters:**
- g

- the graphics
- tickBounds

- the tick bounds
- y

- the y coordinate

---

#### public void paintLabels​(
Graphics
g)

Paints the labels.

**Parameters:**
- g

- the graphics

---

#### protected void paintHorizontalLabel​(
Graphics
g,
int value,

Component
label)

Called for every label in the label table. Used to draw the labels for
horizontal sliders. The graphics have been translated to labelRect.y
already.

**Parameters:**
- g

- the graphics context in which to paint
- value

- the value of the slider
- label

- the component label in the label table that needs to be
painted

**See Also:**
- JSlider.setLabelTable(java.util.Dictionary)

---

#### protected void paintVerticalLabel​(
Graphics
g,
int value,

Component
label)

Called for every label in the label table. Used to draw the labels for
vertical sliders. The graphics have been translated to labelRect.x
already.

**Parameters:**
- g

- the graphics context in which to paint
- value

- the value of the slider
- label

- the component label in the label table that needs to be
painted

**See Also:**
- JSlider.setLabelTable(java.util.Dictionary)

---

#### public void paintThumb​(
Graphics
g)

Paints the thumb.

**Parameters:**
- g

- the graphics

---

#### public void setThumbLocation​(int x,
int y)

Sets the thumb location.

**Parameters:**
- x

- the x coordinate
- y

- the y coordinate

---

#### public void scrollByBlock​(int direction)

Scrolls by block.

**Parameters:**
- direction

- the direction

---

#### public void scrollByUnit​(int direction)

Scrolls by unit.

**Parameters:**
- direction

- the direction

---

#### protected void scrollDueToClickInTrack​(int dir)

This function is called when a mousePressed was detected in the track,
not in the thumb. The default behavior is to scroll by block. You can
override this method to stop it from scrolling or to add additional
behavior.

**Parameters:**
- dir

- the direction and number of blocks to scroll

---

#### protected int xPositionForValue​(int value)

Returns the x position for a value.

**Parameters:**
- value

- the value

**Returns:**
- the x position for a value

---

#### protected int yPositionForValue​(int value)

Returns the y position for a value.

**Parameters:**
- value

- the value

**Returns:**
- the y position for a value

---

#### protected int yPositionForValue​(int value,
int trackY,
int trackHeight)

Returns the y location for the specified value. No checking is
done on the arguments. In particular if

trackHeight

is
negative undefined results may occur.

**Parameters:**
- value

- the slider value to get the location for
- trackY

- y-origin of the track
- trackHeight

- the height of the track

**Returns:**
- the y location for the specified value of the slider

**Since:**
- 1.6

---

#### public int valueForYPosition​(int yPos)

Returns the value at the y position. If

yPos

is beyond the
track at the bottom or the top, this method sets the value to either
the minimum or maximum value of the slider, depending on if the slider
is inverted or not.

**Parameters:**
- yPos

- the location of the slider along the y axis

**Returns:**
- the value at the y position

---

#### public int valueForXPosition​(int xPos)

Returns the value at the x position. If

xPos

is beyond the
track at the left or the right, this method sets the value to either the
minimum or maximum value of the slider, depending on if the slider is
inverted or not.

**Parameters:**
- xPos

- the location of the slider along the x axis

**Returns:**
- the value of the x position

---

### Additional Sections

#### Class BasicSliderUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI

javax.swing.plaf.SliderUI

- javax.swing.plaf.basic.BasicSliderUI

javax.swing.plaf.basic.BasicSliderUI

**Direct Known Subclasses:** MetalSliderUI

,

SynthSliderUI

```java
public class
BasicSliderUI

extends
SliderUI
```

A Basic L&F implementation of SliderUI.

public class

BasicSliderUI

extends

SliderUI

A Basic L&F implementation of SliderUI.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicSliderUI.ActionScroller

As of Java 2 platform v1.3 this undocumented class is no longer used.

class

BasicSliderUI.ChangeHandler

Data model listener.

class

BasicSliderUI.ComponentHandler

Listener for resizing events.

class

BasicSliderUI.FocusHandler

Focus-change listener.

class

BasicSliderUI.PropertyChangeHandler

A property change handler.

class

BasicSliderUI.ScrollListener

Scroll-event listener.

class

BasicSliderUI.TrackListener

Track mouse movements.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeListener

changeListener

Change listener

protected

ComponentListener

componentListener

Component listener

protected

Rectangle

contentRect

Content rectangle

protected

Insets

focusInsets

Focus insets

protected

FocusListener

focusListener

Focus listener

protected

Rectangle

focusRect

Focus rectangle

protected

Insets

insetCache

Inset cache

protected

Rectangle

labelRect

Label rectangle

protected boolean

leftToRightCache

Left-to-right cache

static int

MAX_SCROLL

Maximum scroll

static int

MIN_SCROLL

Minimum scroll

static int

NEGATIVE_SCROLL

Negative scroll

static int

POSITIVE_SCROLL

Positive scroll

protected

PropertyChangeListener

propertyChangeListener

Property chane listener

protected

BasicSliderUI.ScrollListener

scrollListener

Scroll listener

protected

Timer

scrollTimer

Scroll timer

protected

JSlider

slider

Slider

protected

Rectangle

thumbRect

Thumb rectangle

protected

Rectangle

tickRect

Tick rectangle

protected int

trackBuffer

The distance that the track is from the side of the control

protected

BasicSliderUI.TrackListener

trackListener

Track listener

protected

Rectangle

trackRect

Track rectangle

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicSliderUI

​(

JSlider

b)

Constructs a

BasicSliderUI

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

protected void

calculateContentRect

()

Calculates the content rectangle.

protected void

calculateFocusRect

()

Calculates the focus rectangle.

protected void

calculateGeometry

()

Calculates the geometry.

protected void

calculateLabelRect

()

Calculates the label rectangle.

protected void

calculateThumbLocation

()

Calculates the thumb location.

protected void

calculateThumbSize

()

Calculates the thumb size rectangle.

protected void

calculateTickRect

()

Calculates the tick rectangle.

protected void

calculateTrackBuffer

()

Calculates the track buffer.

protected void

calculateTrackRect

()

Calculates the track rectangle.

protected

ChangeListener

createChangeListener

​(

JSlider

slider)

Creates a change listener.

protected

ComponentListener

createComponentListener

​(

JSlider

slider)

Creates a composite listener.

protected

FocusListener

createFocusListener

​(

JSlider

slider)

Creates a focus listener.

protected

PropertyChangeListener

createPropertyChangeListener

​(

JSlider

slider)

Creates a property change listener.

protected

BasicSliderUI.ScrollListener

createScrollListener

​(

JSlider

slider)

Creates a scroll listener.

protected

BasicSliderUI.TrackListener

createTrackListener

​(

JSlider

slider)

Creates a track listener.

static

ComponentUI

createUI

​(

JComponent

b)

Creates a UI.

protected boolean

drawInverted

()

Draws inverted.

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

Color

getFocusColor

()

Returns the focus color.

protected int

getHeightOfHighValueLabel

()

Returns the height of the highest value label.

protected int

getHeightOfLowValueLabel

()

Returns the height of the lowest value label.

protected int

getHeightOfTallestLabel

()

Returns the height of the tallest label.

protected

Integer

getHighestValue

()

Returns the biggest value that has an entry in the label table.

protected

Component

getHighestValueLabel

()

Returns the label that corresponds to the lowest slider value in the
label table.

protected

Color

getHighlightColor

()

Returns the highlight color.

protected

Integer

getLowestValue

()

Returns the smallest value that has an entry in the label table.

protected

Component

getLowestValueLabel

()

Returns the label that corresponds to the highest slider value in the
label table.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size.

Dimension

getMinimumHorizontalSize

()

Returns the minimum horizontal size.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size.

Dimension

getMinimumVerticalSize

()

Returns the minimum vertical size.

Dimension

getPreferredHorizontalSize

()

Returns the preferred horizontal size.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size.

Dimension

getPreferredVerticalSize

()

Returns the preferred vertical size.

protected

Color

getShadowColor

()

Returns the shadow color.

protected

Dimension

getThumbSize

()

Returns the thumb size.

protected int

getTickLength

()

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders.

protected int

getWidthOfHighValueLabel

()

Returns the width of the highest value label.

protected int

getWidthOfLowValueLabel

()

Returns the width of the lowest value label.

protected int

getWidthOfWidestLabel

()

Returns the width of the widest label.

protected void

installDefaults

​(

JSlider

slider)

Installs the defaults.

protected void

installKeyboardActions

​(

JSlider

slider)

Installs keyboard actions.

protected void

installListeners

​(

JSlider

slider)

Installs listeners.

void

installUI

​(

JComponent

c)

Installs a UI.

protected boolean

isDragging

()

Returns true if the user is dragging the slider.

protected boolean

labelsHaveSameBaselines

()

Returns true if all the labels from the label table have the same
baseline.

void

paintFocus

​(

Graphics

g)

Paints focus.

protected void

paintHorizontalLabel

​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table.

void

paintLabels

​(

Graphics

g)

Paints the labels.

protected void

paintMajorTickForHorizSlider

​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints major tick for horizontal slider.

protected void

paintMajorTickForVertSlider

​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints major tick for vertical slider.

protected void

paintMinorTickForHorizSlider

​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints minor tick for horizontal slider.

protected void

paintMinorTickForVertSlider

​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints minor tick for vertical slider.

void

paintThumb

​(

Graphics

g)

Paints the thumb.

void

paintTicks

​(

Graphics

g)

Paints ticks.

void

paintTrack

​(

Graphics

g)

Paints track.

protected void

paintVerticalLabel

​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table.

protected void

recalculateIfInsetsChanged

()

Recalculates if the insets have changed.

protected void

recalculateIfOrientationChanged

()

Recalculates if the orientation has changed.

void

scrollByBlock

​(int direction)

Scrolls by block.

void

scrollByUnit

​(int direction)

Scrolls by unit.

protected void

scrollDueToClickInTrack

​(int dir)

This function is called when a mousePressed was detected in the track,
not in the thumb.

void

setThumbLocation

​(int x,
int y)

Sets the thumb location.

protected void

uninstallDefaults

​(

JSlider

slider)

Uninstalls the defaults.

protected void

uninstallKeyboardActions

​(

JSlider

slider)

Uninstalls keyboard actions.

protected void

uninstallListeners

​(

JSlider

slider)

Uninstalls listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls a UI.

int

valueForXPosition

​(int xPos)

Returns the value at the x position.

int

valueForYPosition

​(int yPos)

Returns the value at the y position.

protected int

xPositionForValue

​(int value)

Returns the x position for a value.

protected int

yPositionForValue

​(int value)

Returns the y position for a value.

protected int

yPositionForValue

​(int value,
int trackY,
int trackHeight)

Returns the y location for the specified value.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicSliderUI.ActionScroller

As of Java 2 platform v1.3 this undocumented class is no longer used.

class

BasicSliderUI.ChangeHandler

Data model listener.

class

BasicSliderUI.ComponentHandler

Listener for resizing events.

class

BasicSliderUI.FocusHandler

Focus-change listener.

class

BasicSliderUI.PropertyChangeHandler

A property change handler.

class

BasicSliderUI.ScrollListener

Scroll-event listener.

class

BasicSliderUI.TrackListener

Track mouse movements.

---

#### Nested Class Summary

As of Java 2 platform v1.3 this undocumented class is no longer used.

Data model listener.

Listener for resizing events.

Focus-change listener.

A property change handler.

Scroll-event listener.

Track mouse movements.

Field Summary

Fields

Modifier and Type

Field

Description

protected

ChangeListener

changeListener

Change listener

protected

ComponentListener

componentListener

Component listener

protected

Rectangle

contentRect

Content rectangle

protected

Insets

focusInsets

Focus insets

protected

FocusListener

focusListener

Focus listener

protected

Rectangle

focusRect

Focus rectangle

protected

Insets

insetCache

Inset cache

protected

Rectangle

labelRect

Label rectangle

protected boolean

leftToRightCache

Left-to-right cache

static int

MAX_SCROLL

Maximum scroll

static int

MIN_SCROLL

Minimum scroll

static int

NEGATIVE_SCROLL

Negative scroll

static int

POSITIVE_SCROLL

Positive scroll

protected

PropertyChangeListener

propertyChangeListener

Property chane listener

protected

BasicSliderUI.ScrollListener

scrollListener

Scroll listener

protected

Timer

scrollTimer

Scroll timer

protected

JSlider

slider

Slider

protected

Rectangle

thumbRect

Thumb rectangle

protected

Rectangle

tickRect

Tick rectangle

protected int

trackBuffer

The distance that the track is from the side of the control

protected

BasicSliderUI.TrackListener

trackListener

Track listener

protected

Rectangle

trackRect

Track rectangle

---

#### Field Summary

Change listener

Component listener

Content rectangle

Focus insets

Focus listener

Focus rectangle

Inset cache

Label rectangle

Left-to-right cache

Maximum scroll

Minimum scroll

Negative scroll

Positive scroll

Property chane listener

Scroll listener

Scroll timer

Slider

Thumb rectangle

Tick rectangle

The distance that the track is from the side of the control

Track listener

Track rectangle

Constructor Summary

Constructors

Constructor

Description

BasicSliderUI

​(

JSlider

b)

Constructs a

BasicSliderUI

.

---

#### Constructor Summary

Constructs a

BasicSliderUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

calculateContentRect

()

Calculates the content rectangle.

protected void

calculateFocusRect

()

Calculates the focus rectangle.

protected void

calculateGeometry

()

Calculates the geometry.

protected void

calculateLabelRect

()

Calculates the label rectangle.

protected void

calculateThumbLocation

()

Calculates the thumb location.

protected void

calculateThumbSize

()

Calculates the thumb size rectangle.

protected void

calculateTickRect

()

Calculates the tick rectangle.

protected void

calculateTrackBuffer

()

Calculates the track buffer.

protected void

calculateTrackRect

()

Calculates the track rectangle.

protected

ChangeListener

createChangeListener

​(

JSlider

slider)

Creates a change listener.

protected

ComponentListener

createComponentListener

​(

JSlider

slider)

Creates a composite listener.

protected

FocusListener

createFocusListener

​(

JSlider

slider)

Creates a focus listener.

protected

PropertyChangeListener

createPropertyChangeListener

​(

JSlider

slider)

Creates a property change listener.

protected

BasicSliderUI.ScrollListener

createScrollListener

​(

JSlider

slider)

Creates a scroll listener.

protected

BasicSliderUI.TrackListener

createTrackListener

​(

JSlider

slider)

Creates a track listener.

static

ComponentUI

createUI

​(

JComponent

b)

Creates a UI.

protected boolean

drawInverted

()

Draws inverted.

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

Color

getFocusColor

()

Returns the focus color.

protected int

getHeightOfHighValueLabel

()

Returns the height of the highest value label.

protected int

getHeightOfLowValueLabel

()

Returns the height of the lowest value label.

protected int

getHeightOfTallestLabel

()

Returns the height of the tallest label.

protected

Integer

getHighestValue

()

Returns the biggest value that has an entry in the label table.

protected

Component

getHighestValueLabel

()

Returns the label that corresponds to the lowest slider value in the
label table.

protected

Color

getHighlightColor

()

Returns the highlight color.

protected

Integer

getLowestValue

()

Returns the smallest value that has an entry in the label table.

protected

Component

getLowestValueLabel

()

Returns the label that corresponds to the highest slider value in the
label table.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size.

Dimension

getMinimumHorizontalSize

()

Returns the minimum horizontal size.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size.

Dimension

getMinimumVerticalSize

()

Returns the minimum vertical size.

Dimension

getPreferredHorizontalSize

()

Returns the preferred horizontal size.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size.

Dimension

getPreferredVerticalSize

()

Returns the preferred vertical size.

protected

Color

getShadowColor

()

Returns the shadow color.

protected

Dimension

getThumbSize

()

Returns the thumb size.

protected int

getTickLength

()

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders.

protected int

getWidthOfHighValueLabel

()

Returns the width of the highest value label.

protected int

getWidthOfLowValueLabel

()

Returns the width of the lowest value label.

protected int

getWidthOfWidestLabel

()

Returns the width of the widest label.

protected void

installDefaults

​(

JSlider

slider)

Installs the defaults.

protected void

installKeyboardActions

​(

JSlider

slider)

Installs keyboard actions.

protected void

installListeners

​(

JSlider

slider)

Installs listeners.

void

installUI

​(

JComponent

c)

Installs a UI.

protected boolean

isDragging

()

Returns true if the user is dragging the slider.

protected boolean

labelsHaveSameBaselines

()

Returns true if all the labels from the label table have the same
baseline.

void

paintFocus

​(

Graphics

g)

Paints focus.

protected void

paintHorizontalLabel

​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table.

void

paintLabels

​(

Graphics

g)

Paints the labels.

protected void

paintMajorTickForHorizSlider

​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints major tick for horizontal slider.

protected void

paintMajorTickForVertSlider

​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints major tick for vertical slider.

protected void

paintMinorTickForHorizSlider

​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints minor tick for horizontal slider.

protected void

paintMinorTickForVertSlider

​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints minor tick for vertical slider.

void

paintThumb

​(

Graphics

g)

Paints the thumb.

void

paintTicks

​(

Graphics

g)

Paints ticks.

void

paintTrack

​(

Graphics

g)

Paints track.

protected void

paintVerticalLabel

​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table.

protected void

recalculateIfInsetsChanged

()

Recalculates if the insets have changed.

protected void

recalculateIfOrientationChanged

()

Recalculates if the orientation has changed.

void

scrollByBlock

​(int direction)

Scrolls by block.

void

scrollByUnit

​(int direction)

Scrolls by unit.

protected void

scrollDueToClickInTrack

​(int dir)

This function is called when a mousePressed was detected in the track,
not in the thumb.

void

setThumbLocation

​(int x,
int y)

Sets the thumb location.

protected void

uninstallDefaults

​(

JSlider

slider)

Uninstalls the defaults.

protected void

uninstallKeyboardActions

​(

JSlider

slider)

Uninstalls keyboard actions.

protected void

uninstallListeners

​(

JSlider

slider)

Uninstalls listeners.

void

uninstallUI

​(

JComponent

c)

Uninstalls a UI.

int

valueForXPosition

​(int xPos)

Returns the value at the x position.

int

valueForYPosition

​(int yPos)

Returns the value at the y position.

protected int

xPositionForValue

​(int value)

Returns the x position for a value.

protected int

yPositionForValue

​(int value)

Returns the y position for a value.

protected int

yPositionForValue

​(int value,
int trackY,
int trackHeight)

Returns the y location for the specified value.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

---

#### Method Summary

Calculates the content rectangle.

Calculates the focus rectangle.

Calculates the geometry.

Calculates the label rectangle.

Calculates the thumb location.

Calculates the thumb size rectangle.

Calculates the tick rectangle.

Calculates the track buffer.

Calculates the track rectangle.

Creates a change listener.

Creates a composite listener.

Creates a focus listener.

Creates a property change listener.

Creates a scroll listener.

Creates a track listener.

Creates a UI.

Draws inverted.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the focus color.

Returns the height of the highest value label.

Returns the height of the lowest value label.

Returns the height of the tallest label.

Returns the biggest value that has an entry in the label table.

Returns the label that corresponds to the lowest slider value in the
label table.

Returns the highlight color.

Returns the smallest value that has an entry in the label table.

Returns the label that corresponds to the highest slider value in the
label table.

Returns the maximum size.

Returns the minimum horizontal size.

Returns the minimum size.

Returns the minimum vertical size.

Returns the preferred horizontal size.

Returns the preferred size.

Returns the preferred vertical size.

Returns the shadow color.

Returns the thumb size.

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders.

Returns the width of the highest value label.

Returns the width of the lowest value label.

Returns the width of the widest label.

Installs the defaults.

Installs keyboard actions.

Installs listeners.

Installs a UI.

Returns true if the user is dragging the slider.

Returns true if all the labels from the label table have the same
baseline.

Paints focus.

Called for every label in the label table.

Paints the labels.

Paints major tick for horizontal slider.

Paints major tick for vertical slider.

Paints minor tick for horizontal slider.

Paints minor tick for vertical slider.

Paints the thumb.

Paints ticks.

Paints track.

Recalculates if the insets have changed.

Recalculates if the orientation has changed.

Scrolls by block.

Scrolls by unit.

This function is called when a mousePressed was detected in the track,
not in the thumb.

Sets the thumb location.

Uninstalls the defaults.

Uninstalls keyboard actions.

Uninstalls listeners.

Uninstalls a UI.

Returns the value at the x position.

Returns the value at the y position.

Returns the x position for a value.

Returns the y position for a value.

Returns the y location for the specified value.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

============ FIELD DETAIL ===========

- Field Detail

- POSITIVE_SCROLL

```java
public static final int POSITIVE_SCROLL
```

Positive scroll

**See Also:** Constant Field Values

- NEGATIVE_SCROLL

```java
public static final int NEGATIVE_SCROLL
```

Negative scroll

**See Also:** Constant Field Values

- MIN_SCROLL

```java
public static final int MIN_SCROLL
```

Minimum scroll

**See Also:** Constant Field Values

- MAX_SCROLL

```java
public static final int MAX_SCROLL
```

Maximum scroll

**See Also:** Constant Field Values

- scrollTimer

```java
protected
Timer
scrollTimer
```

Scroll timer

- slider

```java
protected
JSlider
slider
```

Slider

- focusInsets

```java
protected
Insets
focusInsets
```

Focus insets

- insetCache

```java
protected
Insets
insetCache
```

Inset cache

- leftToRightCache

```java
protected boolean leftToRightCache
```

Left-to-right cache

- focusRect

```java
protected
Rectangle
focusRect
```

Focus rectangle

- contentRect

```java
protected
Rectangle
contentRect
```

Content rectangle

- labelRect

```java
protected
Rectangle
labelRect
```

Label rectangle

- tickRect

```java
protected
Rectangle
tickRect
```

Tick rectangle

- trackRect

```java
protected
Rectangle
trackRect
```

Track rectangle

- thumbRect

```java
protected
Rectangle
thumbRect
```

Thumb rectangle

- trackBuffer

```java
protected int trackBuffer
```

The distance that the track is from the side of the control

- trackListener

```java
protected
BasicSliderUI.TrackListener
trackListener
```

Track listener

- changeListener

```java
protected
ChangeListener
changeListener
```

Change listener

- componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

- focusListener

```java
protected
FocusListener
focusListener
```

Focus listener

- scrollListener

```java
protected
BasicSliderUI.ScrollListener
scrollListener
```

Scroll listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property chane listener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicSliderUI

```java
public BasicSliderUI​(
JSlider
b)
```

Constructs a

BasicSliderUI

.

**Parameters:** b

- a slider

============ METHOD DETAIL ==========

- Method Detail

- getShadowColor

```java
protected
Color
getShadowColor()
```

Returns the shadow color.

**Returns:** the shadow color

- getHighlightColor

```java
protected
Color
getHighlightColor()
```

Returns the highlight color.

**Returns:** the highlight color

- getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the focus color.

**Returns:** the focus color

- isDragging

```java
protected boolean isDragging()
```

Returns true if the user is dragging the slider.

**Returns:** true if the user is dragging the slider
**Since:** 1.5

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a UI.

**Parameters:** b

- a component
**Returns:** a UI

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs a UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- a component
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

Uninstalls a UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- a component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults​(
JSlider
slider)
```

Installs the defaults.

**Parameters:** slider

- a slider

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls the defaults.

**Parameters:** slider

- a slider

- createTrackListener

```java
protected
BasicSliderUI.TrackListener
createTrackListener​(
JSlider
slider)
```

Creates a track listener.

**Parameters:** slider

- a slider
**Returns:** a track listener

- createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JSlider
slider)
```

Creates a change listener.

**Parameters:** slider

- a slider
**Returns:** a change listener

- createComponentListener

```java
protected
ComponentListener
createComponentListener​(
JSlider
slider)
```

Creates a composite listener.

**Parameters:** slider

- a slider
**Returns:** a composite listener

- createFocusListener

```java
protected
FocusListener
createFocusListener​(
JSlider
slider)
```

Creates a focus listener.

**Parameters:** slider

- a slider
**Returns:** a focus listener

- createScrollListener

```java
protected
BasicSliderUI.ScrollListener
createScrollListener​(
JSlider
slider)
```

Creates a scroll listener.

**Parameters:** slider

- a slider
**Returns:** a scroll listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Creates a property change listener.

**Parameters:** slider

- a slider
**Returns:** a property change listener

- installListeners

```java
protected void installListeners​(
JSlider
slider)
```

Installs listeners.

**Parameters:** slider

- a slider

- uninstallListeners

```java
protected void uninstallListeners​(
JSlider
slider)
```

Uninstalls listeners.

**Parameters:** slider

- a slider

- installKeyboardActions

```java
protected void installKeyboardActions​(
JSlider
slider)
```

Installs keyboard actions.

**Parameters:** slider

- a slider

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JSlider
slider)
```

Uninstalls keyboard actions.

**Parameters:** slider

- a slider

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

- labelsHaveSameBaselines

```java
protected boolean labelsHaveSameBaselines()
```

Returns true if all the labels from the label table have the same
baseline.

**Returns:** true if all the labels from the label table have the
same baseline
**Since:** 1.6

- getPreferredHorizontalSize

```java
public
Dimension
getPreferredHorizontalSize()
```

Returns the preferred horizontal size.

**Returns:** the preferred horizontal size

- getPreferredVerticalSize

```java
public
Dimension
getPreferredVerticalSize()
```

Returns the preferred vertical size.

**Returns:** the preferred vertical size

- getMinimumHorizontalSize

```java
public
Dimension
getMinimumHorizontalSize()
```

Returns the minimum horizontal size.

**Returns:** the minimum horizontal size

- getMinimumVerticalSize

```java
public
Dimension
getMinimumVerticalSize()
```

Returns the minimum vertical size.

**Returns:** the minimum vertical size

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the minimum size
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- calculateGeometry

```java
protected void calculateGeometry()
```

Calculates the geometry.

- calculateFocusRect

```java
protected void calculateFocusRect()
```

Calculates the focus rectangle.

- calculateThumbSize

```java
protected void calculateThumbSize()
```

Calculates the thumb size rectangle.

- calculateContentRect

```java
protected void calculateContentRect()
```

Calculates the content rectangle.

- calculateThumbLocation

```java
protected void calculateThumbLocation()
```

Calculates the thumb location.

- calculateTrackBuffer

```java
protected void calculateTrackBuffer()
```

Calculates the track buffer.

- calculateTrackRect

```java
protected void calculateTrackRect()
```

Calculates the track rectangle.

- getTickLength

```java
protected int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders. BasicSliderUI uses the returned value
to determine the tick area rectangle. If you want to give your ticks some
room, make this larger than you need and paint your ticks away from the
sides in paintTicks().

**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

- calculateTickRect

```java
protected void calculateTickRect()
```

Calculates the tick rectangle.

- calculateLabelRect

```java
protected void calculateLabelRect()
```

Calculates the label rectangle.

- getThumbSize

```java
protected
Dimension
getThumbSize()
```

Returns the thumb size.

**Returns:** the thumb size

- getWidthOfWidestLabel

```java
protected int getWidthOfWidestLabel()
```

Returns the width of the widest label.

**Returns:** the width of the widest label

- getHeightOfTallestLabel

```java
protected int getHeightOfTallestLabel()
```

Returns the height of the tallest label.

**Returns:** the height of the tallest label

- getWidthOfHighValueLabel

```java
protected int getWidthOfHighValueLabel()
```

Returns the width of the highest value label.

**Returns:** the width of the highest value label

- getWidthOfLowValueLabel

```java
protected int getWidthOfLowValueLabel()
```

Returns the width of the lowest value label.

**Returns:** the width of the lowest value label

- getHeightOfHighValueLabel

```java
protected int getHeightOfHighValueLabel()
```

Returns the height of the highest value label.

**Returns:** the height of the highest value label

- getHeightOfLowValueLabel

```java
protected int getHeightOfLowValueLabel()
```

Returns the height of the lowest value label.

**Returns:** the height of the lowest value label

- drawInverted

```java
protected boolean drawInverted()
```

Draws inverted.

**Returns:** the inverted-ness

- getHighestValue

```java
protected
Integer
getHighestValue()
```

Returns the biggest value that has an entry in the label table.

**Returns:** biggest value that has an entry in the label table, or
null.
**Since:** 1.6

- getLowestValue

```java
protected
Integer
getLowestValue()
```

Returns the smallest value that has an entry in the label table.

**Returns:** smallest value that has an entry in the label table, or
null.
**Since:** 1.6

- getLowestValueLabel

```java
protected
Component
getLowestValueLabel()
```

Returns the label that corresponds to the highest slider value in the
label table.

**Returns:** the label that corresponds to the highest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- getHighestValueLabel

```java
protected
Component
getHighestValueLabel()
```

Returns the label that corresponds to the lowest slider value in the
label table.

**Returns:** the label that corresponds to the lowest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- recalculateIfInsetsChanged

```java
protected void recalculateIfInsetsChanged()
```

Recalculates if the insets have changed.

- recalculateIfOrientationChanged

```java
protected void recalculateIfOrientationChanged()
```

Recalculates if the orientation has changed.

- paintFocus

```java
public void paintFocus​(
Graphics
g)
```

Paints focus.

**Parameters:** g

- the graphics

- paintTrack

```java
public void paintTrack​(
Graphics
g)
```

Paints track.

**Parameters:** g

- the graphics

- paintTicks

```java
public void paintTicks​(
Graphics
g)
```

Paints ticks.

**Parameters:** g

- the graphics

- paintMinorTickForHorizSlider

```java
protected void paintMinorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints minor tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

- paintMajorTickForHorizSlider

```java
protected void paintMajorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints major tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

- paintMinorTickForVertSlider

```java
protected void paintMinorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints minor tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

- paintMajorTickForVertSlider

```java
protected void paintMajorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints major tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

- paintLabels

```java
public void paintLabels​(
Graphics
g)
```

Paints the labels.

**Parameters:** g

- the graphics

- paintHorizontalLabel

```java
protected void paintHorizontalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
horizontal sliders. The graphics have been translated to labelRect.y
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- paintVerticalLabel

```java
protected void paintVerticalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
vertical sliders. The graphics have been translated to labelRect.x
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- paintThumb

```java
public void paintThumb​(
Graphics
g)
```

Paints the thumb.

**Parameters:** g

- the graphics

- setThumbLocation

```java
public void setThumbLocation​(int x,
int y)
```

Sets the thumb location.

**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate

- scrollByBlock

```java
public void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction

- scrollByUnit

```java
public void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction

- scrollDueToClickInTrack

```java
protected void scrollDueToClickInTrack​(int dir)
```

This function is called when a mousePressed was detected in the track,
not in the thumb. The default behavior is to scroll by block. You can
override this method to stop it from scrolling or to add additional
behavior.

**Parameters:** dir

- the direction and number of blocks to scroll

- xPositionForValue

```java
protected int xPositionForValue​(int value)
```

Returns the x position for a value.

**Parameters:** value

- the value
**Returns:** the x position for a value

- yPositionForValue

```java
protected int yPositionForValue​(int value)
```

Returns the y position for a value.

**Parameters:** value

- the value
**Returns:** the y position for a value

- yPositionForValue

```java
protected int yPositionForValue​(int value,
int trackY,
int trackHeight)
```

Returns the y location for the specified value. No checking is
done on the arguments. In particular if

trackHeight

is
negative undefined results may occur.

**Parameters:** value

- the slider value to get the location for
**Parameters:** trackY

- y-origin of the track
**Parameters:** trackHeight

- the height of the track
**Returns:** the y location for the specified value of the slider
**Since:** 1.6

- valueForYPosition

```java
public int valueForYPosition​(int yPos)
```

Returns the value at the y position. If

yPos

is beyond the
track at the bottom or the top, this method sets the value to either
the minimum or maximum value of the slider, depending on if the slider
is inverted or not.

**Parameters:** yPos

- the location of the slider along the y axis
**Returns:** the value at the y position

- valueForXPosition

```java
public int valueForXPosition​(int xPos)
```

Returns the value at the x position. If

xPos

is beyond the
track at the left or the right, this method sets the value to either the
minimum or maximum value of the slider, depending on if the slider is
inverted or not.

**Parameters:** xPos

- the location of the slider along the x axis
**Returns:** the value of the x position

Field Detail

- POSITIVE_SCROLL

```java
public static final int POSITIVE_SCROLL
```

Positive scroll

**See Also:** Constant Field Values

- NEGATIVE_SCROLL

```java
public static final int NEGATIVE_SCROLL
```

Negative scroll

**See Also:** Constant Field Values

- MIN_SCROLL

```java
public static final int MIN_SCROLL
```

Minimum scroll

**See Also:** Constant Field Values

- MAX_SCROLL

```java
public static final int MAX_SCROLL
```

Maximum scroll

**See Also:** Constant Field Values

- scrollTimer

```java
protected
Timer
scrollTimer
```

Scroll timer

- slider

```java
protected
JSlider
slider
```

Slider

- focusInsets

```java
protected
Insets
focusInsets
```

Focus insets

- insetCache

```java
protected
Insets
insetCache
```

Inset cache

- leftToRightCache

```java
protected boolean leftToRightCache
```

Left-to-right cache

- focusRect

```java
protected
Rectangle
focusRect
```

Focus rectangle

- contentRect

```java
protected
Rectangle
contentRect
```

Content rectangle

- labelRect

```java
protected
Rectangle
labelRect
```

Label rectangle

- tickRect

```java
protected
Rectangle
tickRect
```

Tick rectangle

- trackRect

```java
protected
Rectangle
trackRect
```

Track rectangle

- thumbRect

```java
protected
Rectangle
thumbRect
```

Thumb rectangle

- trackBuffer

```java
protected int trackBuffer
```

The distance that the track is from the side of the control

- trackListener

```java
protected
BasicSliderUI.TrackListener
trackListener
```

Track listener

- changeListener

```java
protected
ChangeListener
changeListener
```

Change listener

- componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

- focusListener

```java
protected
FocusListener
focusListener
```

Focus listener

- scrollListener

```java
protected
BasicSliderUI.ScrollListener
scrollListener
```

Scroll listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property chane listener

---

#### Field Detail

POSITIVE_SCROLL

```java
public static final int POSITIVE_SCROLL
```

Positive scroll

**See Also:** Constant Field Values

---

#### POSITIVE_SCROLL

public static final int POSITIVE_SCROLL

Positive scroll

NEGATIVE_SCROLL

```java
public static final int NEGATIVE_SCROLL
```

Negative scroll

**See Also:** Constant Field Values

---

#### NEGATIVE_SCROLL

public static final int NEGATIVE_SCROLL

Negative scroll

MIN_SCROLL

```java
public static final int MIN_SCROLL
```

Minimum scroll

**See Also:** Constant Field Values

---

#### MIN_SCROLL

public static final int MIN_SCROLL

Minimum scroll

MAX_SCROLL

```java
public static final int MAX_SCROLL
```

Maximum scroll

**See Also:** Constant Field Values

---

#### MAX_SCROLL

public static final int MAX_SCROLL

Maximum scroll

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

slider

```java
protected
JSlider
slider
```

Slider

---

#### slider

protected

JSlider

slider

Slider

focusInsets

```java
protected
Insets
focusInsets
```

Focus insets

---

#### focusInsets

protected

Insets

focusInsets

Focus insets

insetCache

```java
protected
Insets
insetCache
```

Inset cache

---

#### insetCache

protected

Insets

insetCache

Inset cache

leftToRightCache

```java
protected boolean leftToRightCache
```

Left-to-right cache

---

#### leftToRightCache

protected boolean leftToRightCache

Left-to-right cache

focusRect

```java
protected
Rectangle
focusRect
```

Focus rectangle

---

#### focusRect

protected

Rectangle

focusRect

Focus rectangle

contentRect

```java
protected
Rectangle
contentRect
```

Content rectangle

---

#### contentRect

protected

Rectangle

contentRect

Content rectangle

labelRect

```java
protected
Rectangle
labelRect
```

Label rectangle

---

#### labelRect

protected

Rectangle

labelRect

Label rectangle

tickRect

```java
protected
Rectangle
tickRect
```

Tick rectangle

---

#### tickRect

protected

Rectangle

tickRect

Tick rectangle

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

trackBuffer

```java
protected int trackBuffer
```

The distance that the track is from the side of the control

---

#### trackBuffer

protected int trackBuffer

The distance that the track is from the side of the control

trackListener

```java
protected
BasicSliderUI.TrackListener
trackListener
```

Track listener

---

#### trackListener

protected

BasicSliderUI.TrackListener

trackListener

Track listener

changeListener

```java
protected
ChangeListener
changeListener
```

Change listener

---

#### changeListener

protected

ChangeListener

changeListener

Change listener

componentListener

```java
protected
ComponentListener
componentListener
```

Component listener

---

#### componentListener

protected

ComponentListener

componentListener

Component listener

focusListener

```java
protected
FocusListener
focusListener
```

Focus listener

---

#### focusListener

protected

FocusListener

focusListener

Focus listener

scrollListener

```java
protected
BasicSliderUI.ScrollListener
scrollListener
```

Scroll listener

---

#### scrollListener

protected

BasicSliderUI.ScrollListener

scrollListener

Scroll listener

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property chane listener

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

Property chane listener

Constructor Detail

- BasicSliderUI

```java
public BasicSliderUI​(
JSlider
b)
```

Constructs a

BasicSliderUI

.

**Parameters:** b

- a slider

---

#### Constructor Detail

BasicSliderUI

```java
public BasicSliderUI​(
JSlider
b)
```

Constructs a

BasicSliderUI

.

**Parameters:** b

- a slider

---

#### BasicSliderUI

public BasicSliderUI​(

JSlider

b)

Constructs a

BasicSliderUI

.

Method Detail

- getShadowColor

```java
protected
Color
getShadowColor()
```

Returns the shadow color.

**Returns:** the shadow color

- getHighlightColor

```java
protected
Color
getHighlightColor()
```

Returns the highlight color.

**Returns:** the highlight color

- getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the focus color.

**Returns:** the focus color

- isDragging

```java
protected boolean isDragging()
```

Returns true if the user is dragging the slider.

**Returns:** true if the user is dragging the slider
**Since:** 1.5

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a UI.

**Parameters:** b

- a component
**Returns:** a UI

- installUI

```java
public void installUI​(
JComponent
c)
```

Installs a UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- a component
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

Uninstalls a UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- a component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

- installDefaults

```java
protected void installDefaults​(
JSlider
slider)
```

Installs the defaults.

**Parameters:** slider

- a slider

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls the defaults.

**Parameters:** slider

- a slider

- createTrackListener

```java
protected
BasicSliderUI.TrackListener
createTrackListener​(
JSlider
slider)
```

Creates a track listener.

**Parameters:** slider

- a slider
**Returns:** a track listener

- createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JSlider
slider)
```

Creates a change listener.

**Parameters:** slider

- a slider
**Returns:** a change listener

- createComponentListener

```java
protected
ComponentListener
createComponentListener​(
JSlider
slider)
```

Creates a composite listener.

**Parameters:** slider

- a slider
**Returns:** a composite listener

- createFocusListener

```java
protected
FocusListener
createFocusListener​(
JSlider
slider)
```

Creates a focus listener.

**Parameters:** slider

- a slider
**Returns:** a focus listener

- createScrollListener

```java
protected
BasicSliderUI.ScrollListener
createScrollListener​(
JSlider
slider)
```

Creates a scroll listener.

**Parameters:** slider

- a slider
**Returns:** a scroll listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Creates a property change listener.

**Parameters:** slider

- a slider
**Returns:** a property change listener

- installListeners

```java
protected void installListeners​(
JSlider
slider)
```

Installs listeners.

**Parameters:** slider

- a slider

- uninstallListeners

```java
protected void uninstallListeners​(
JSlider
slider)
```

Uninstalls listeners.

**Parameters:** slider

- a slider

- installKeyboardActions

```java
protected void installKeyboardActions​(
JSlider
slider)
```

Installs keyboard actions.

**Parameters:** slider

- a slider

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JSlider
slider)
```

Uninstalls keyboard actions.

**Parameters:** slider

- a slider

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

- labelsHaveSameBaselines

```java
protected boolean labelsHaveSameBaselines()
```

Returns true if all the labels from the label table have the same
baseline.

**Returns:** true if all the labels from the label table have the
same baseline
**Since:** 1.6

- getPreferredHorizontalSize

```java
public
Dimension
getPreferredHorizontalSize()
```

Returns the preferred horizontal size.

**Returns:** the preferred horizontal size

- getPreferredVerticalSize

```java
public
Dimension
getPreferredVerticalSize()
```

Returns the preferred vertical size.

**Returns:** the preferred vertical size

- getMinimumHorizontalSize

```java
public
Dimension
getMinimumHorizontalSize()
```

Returns the minimum horizontal size.

**Returns:** the minimum horizontal size

- getMinimumVerticalSize

```java
public
Dimension
getMinimumVerticalSize()
```

Returns the minimum vertical size.

**Returns:** the minimum vertical size

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the minimum size
**See Also:** JComponent.getMinimumSize()

,

LayoutManager.minimumLayoutSize(java.awt.Container)

,

ComponentUI.getPreferredSize(javax.swing.JComponent)

- getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- calculateGeometry

```java
protected void calculateGeometry()
```

Calculates the geometry.

- calculateFocusRect

```java
protected void calculateFocusRect()
```

Calculates the focus rectangle.

- calculateThumbSize

```java
protected void calculateThumbSize()
```

Calculates the thumb size rectangle.

- calculateContentRect

```java
protected void calculateContentRect()
```

Calculates the content rectangle.

- calculateThumbLocation

```java
protected void calculateThumbLocation()
```

Calculates the thumb location.

- calculateTrackBuffer

```java
protected void calculateTrackBuffer()
```

Calculates the track buffer.

- calculateTrackRect

```java
protected void calculateTrackRect()
```

Calculates the track rectangle.

- getTickLength

```java
protected int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders. BasicSliderUI uses the returned value
to determine the tick area rectangle. If you want to give your ticks some
room, make this larger than you need and paint your ticks away from the
sides in paintTicks().

**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

- calculateTickRect

```java
protected void calculateTickRect()
```

Calculates the tick rectangle.

- calculateLabelRect

```java
protected void calculateLabelRect()
```

Calculates the label rectangle.

- getThumbSize

```java
protected
Dimension
getThumbSize()
```

Returns the thumb size.

**Returns:** the thumb size

- getWidthOfWidestLabel

```java
protected int getWidthOfWidestLabel()
```

Returns the width of the widest label.

**Returns:** the width of the widest label

- getHeightOfTallestLabel

```java
protected int getHeightOfTallestLabel()
```

Returns the height of the tallest label.

**Returns:** the height of the tallest label

- getWidthOfHighValueLabel

```java
protected int getWidthOfHighValueLabel()
```

Returns the width of the highest value label.

**Returns:** the width of the highest value label

- getWidthOfLowValueLabel

```java
protected int getWidthOfLowValueLabel()
```

Returns the width of the lowest value label.

**Returns:** the width of the lowest value label

- getHeightOfHighValueLabel

```java
protected int getHeightOfHighValueLabel()
```

Returns the height of the highest value label.

**Returns:** the height of the highest value label

- getHeightOfLowValueLabel

```java
protected int getHeightOfLowValueLabel()
```

Returns the height of the lowest value label.

**Returns:** the height of the lowest value label

- drawInverted

```java
protected boolean drawInverted()
```

Draws inverted.

**Returns:** the inverted-ness

- getHighestValue

```java
protected
Integer
getHighestValue()
```

Returns the biggest value that has an entry in the label table.

**Returns:** biggest value that has an entry in the label table, or
null.
**Since:** 1.6

- getLowestValue

```java
protected
Integer
getLowestValue()
```

Returns the smallest value that has an entry in the label table.

**Returns:** smallest value that has an entry in the label table, or
null.
**Since:** 1.6

- getLowestValueLabel

```java
protected
Component
getLowestValueLabel()
```

Returns the label that corresponds to the highest slider value in the
label table.

**Returns:** the label that corresponds to the highest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- getHighestValueLabel

```java
protected
Component
getHighestValueLabel()
```

Returns the label that corresponds to the lowest slider value in the
label table.

**Returns:** the label that corresponds to the lowest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- recalculateIfInsetsChanged

```java
protected void recalculateIfInsetsChanged()
```

Recalculates if the insets have changed.

- recalculateIfOrientationChanged

```java
protected void recalculateIfOrientationChanged()
```

Recalculates if the orientation has changed.

- paintFocus

```java
public void paintFocus​(
Graphics
g)
```

Paints focus.

**Parameters:** g

- the graphics

- paintTrack

```java
public void paintTrack​(
Graphics
g)
```

Paints track.

**Parameters:** g

- the graphics

- paintTicks

```java
public void paintTicks​(
Graphics
g)
```

Paints ticks.

**Parameters:** g

- the graphics

- paintMinorTickForHorizSlider

```java
protected void paintMinorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints minor tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

- paintMajorTickForHorizSlider

```java
protected void paintMajorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints major tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

- paintMinorTickForVertSlider

```java
protected void paintMinorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints minor tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

- paintMajorTickForVertSlider

```java
protected void paintMajorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints major tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

- paintLabels

```java
public void paintLabels​(
Graphics
g)
```

Paints the labels.

**Parameters:** g

- the graphics

- paintHorizontalLabel

```java
protected void paintHorizontalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
horizontal sliders. The graphics have been translated to labelRect.y
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- paintVerticalLabel

```java
protected void paintVerticalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
vertical sliders. The graphics have been translated to labelRect.x
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

- paintThumb

```java
public void paintThumb​(
Graphics
g)
```

Paints the thumb.

**Parameters:** g

- the graphics

- setThumbLocation

```java
public void setThumbLocation​(int x,
int y)
```

Sets the thumb location.

**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate

- scrollByBlock

```java
public void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction

- scrollByUnit

```java
public void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction

- scrollDueToClickInTrack

```java
protected void scrollDueToClickInTrack​(int dir)
```

This function is called when a mousePressed was detected in the track,
not in the thumb. The default behavior is to scroll by block. You can
override this method to stop it from scrolling or to add additional
behavior.

**Parameters:** dir

- the direction and number of blocks to scroll

- xPositionForValue

```java
protected int xPositionForValue​(int value)
```

Returns the x position for a value.

**Parameters:** value

- the value
**Returns:** the x position for a value

- yPositionForValue

```java
protected int yPositionForValue​(int value)
```

Returns the y position for a value.

**Parameters:** value

- the value
**Returns:** the y position for a value

- yPositionForValue

```java
protected int yPositionForValue​(int value,
int trackY,
int trackHeight)
```

Returns the y location for the specified value. No checking is
done on the arguments. In particular if

trackHeight

is
negative undefined results may occur.

**Parameters:** value

- the slider value to get the location for
**Parameters:** trackY

- y-origin of the track
**Parameters:** trackHeight

- the height of the track
**Returns:** the y location for the specified value of the slider
**Since:** 1.6

- valueForYPosition

```java
public int valueForYPosition​(int yPos)
```

Returns the value at the y position. If

yPos

is beyond the
track at the bottom or the top, this method sets the value to either
the minimum or maximum value of the slider, depending on if the slider
is inverted or not.

**Parameters:** yPos

- the location of the slider along the y axis
**Returns:** the value at the y position

- valueForXPosition

```java
public int valueForXPosition​(int xPos)
```

Returns the value at the x position. If

xPos

is beyond the
track at the left or the right, this method sets the value to either the
minimum or maximum value of the slider, depending on if the slider is
inverted or not.

**Parameters:** xPos

- the location of the slider along the x axis
**Returns:** the value of the x position

---

#### Method Detail

getShadowColor

```java
protected
Color
getShadowColor()
```

Returns the shadow color.

**Returns:** the shadow color

---

#### getShadowColor

protected

Color

getShadowColor()

Returns the shadow color.

getHighlightColor

```java
protected
Color
getHighlightColor()
```

Returns the highlight color.

**Returns:** the highlight color

---

#### getHighlightColor

protected

Color

getHighlightColor()

Returns the highlight color.

getFocusColor

```java
protected
Color
getFocusColor()
```

Returns the focus color.

**Returns:** the focus color

---

#### getFocusColor

protected

Color

getFocusColor()

Returns the focus color.

isDragging

```java
protected boolean isDragging()
```

Returns true if the user is dragging the slider.

**Returns:** true if the user is dragging the slider
**Since:** 1.5

---

#### isDragging

protected boolean isDragging()

Returns true if the user is dragging the slider.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
b)
```

Creates a UI.

**Parameters:** b

- a component
**Returns:** a UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

b)

Creates a UI.

installUI

```java
public void installUI​(
JComponent
c)
```

Installs a UI.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- a component
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

Installs a UI.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninstalls a UI.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- a component
**See Also:** ComponentUI.installUI(javax.swing.JComponent)

,

JComponent.updateUI()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Uninstalls a UI.

installDefaults

```java
protected void installDefaults​(
JSlider
slider)
```

Installs the defaults.

**Parameters:** slider

- a slider

---

#### installDefaults

protected void installDefaults​(

JSlider

slider)

Installs the defaults.

uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls the defaults.

**Parameters:** slider

- a slider

---

#### uninstallDefaults

protected void uninstallDefaults​(

JSlider

slider)

Uninstalls the defaults.

createTrackListener

```java
protected
BasicSliderUI.TrackListener
createTrackListener​(
JSlider
slider)
```

Creates a track listener.

**Parameters:** slider

- a slider
**Returns:** a track listener

---

#### createTrackListener

protected

BasicSliderUI.TrackListener

createTrackListener​(

JSlider

slider)

Creates a track listener.

createChangeListener

```java
protected
ChangeListener
createChangeListener​(
JSlider
slider)
```

Creates a change listener.

**Parameters:** slider

- a slider
**Returns:** a change listener

---

#### createChangeListener

protected

ChangeListener

createChangeListener​(

JSlider

slider)

Creates a change listener.

createComponentListener

```java
protected
ComponentListener
createComponentListener​(
JSlider
slider)
```

Creates a composite listener.

**Parameters:** slider

- a slider
**Returns:** a composite listener

---

#### createComponentListener

protected

ComponentListener

createComponentListener​(

JSlider

slider)

Creates a composite listener.

createFocusListener

```java
protected
FocusListener
createFocusListener​(
JSlider
slider)
```

Creates a focus listener.

**Parameters:** slider

- a slider
**Returns:** a focus listener

---

#### createFocusListener

protected

FocusListener

createFocusListener​(

JSlider

slider)

Creates a focus listener.

createScrollListener

```java
protected
BasicSliderUI.ScrollListener
createScrollListener​(
JSlider
slider)
```

Creates a scroll listener.

**Parameters:** slider

- a slider
**Returns:** a scroll listener

---

#### createScrollListener

protected

BasicSliderUI.ScrollListener

createScrollListener​(

JSlider

slider)

Creates a scroll listener.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Creates a property change listener.

**Parameters:** slider

- a slider
**Returns:** a property change listener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener​(

JSlider

slider)

Creates a property change listener.

installListeners

```java
protected void installListeners​(
JSlider
slider)
```

Installs listeners.

**Parameters:** slider

- a slider

---

#### installListeners

protected void installListeners​(

JSlider

slider)

Installs listeners.

uninstallListeners

```java
protected void uninstallListeners​(
JSlider
slider)
```

Uninstalls listeners.

**Parameters:** slider

- a slider

---

#### uninstallListeners

protected void uninstallListeners​(

JSlider

slider)

Uninstalls listeners.

installKeyboardActions

```java
protected void installKeyboardActions​(
JSlider
slider)
```

Installs keyboard actions.

**Parameters:** slider

- a slider

---

#### installKeyboardActions

protected void installKeyboardActions​(

JSlider

slider)

Installs keyboard actions.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions​(
JSlider
slider)
```

Uninstalls keyboard actions.

**Parameters:** slider

- a slider

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions​(

JSlider

slider)

Uninstalls keyboard actions.

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

labelsHaveSameBaselines

```java
protected boolean labelsHaveSameBaselines()
```

Returns true if all the labels from the label table have the same
baseline.

**Returns:** true if all the labels from the label table have the
same baseline
**Since:** 1.6

---

#### labelsHaveSameBaselines

protected boolean labelsHaveSameBaselines()

Returns true if all the labels from the label table have the same
baseline.

getPreferredHorizontalSize

```java
public
Dimension
getPreferredHorizontalSize()
```

Returns the preferred horizontal size.

**Returns:** the preferred horizontal size

---

#### getPreferredHorizontalSize

public

Dimension

getPreferredHorizontalSize()

Returns the preferred horizontal size.

getPreferredVerticalSize

```java
public
Dimension
getPreferredVerticalSize()
```

Returns the preferred vertical size.

**Returns:** the preferred vertical size

---

#### getPreferredVerticalSize

public

Dimension

getPreferredVerticalSize()

Returns the preferred vertical size.

getMinimumHorizontalSize

```java
public
Dimension
getMinimumHorizontalSize()
```

Returns the minimum horizontal size.

**Returns:** the minimum horizontal size

---

#### getMinimumHorizontalSize

public

Dimension

getMinimumHorizontalSize()

Returns the minimum horizontal size.

getMinimumVerticalSize

```java
public
Dimension
getMinimumVerticalSize()
```

Returns the minimum vertical size.

**Returns:** the minimum vertical size

---

#### getMinimumVerticalSize

public

Dimension

getMinimumVerticalSize()

Returns the minimum vertical size.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c)

Returns the preferred size.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the minimum size
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

Returns the minimum size.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the maximum size
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### getMaximumSize

public

Dimension

getMaximumSize​(

JComponent

c)

Returns the maximum size.

calculateGeometry

```java
protected void calculateGeometry()
```

Calculates the geometry.

---

#### calculateGeometry

protected void calculateGeometry()

Calculates the geometry.

calculateFocusRect

```java
protected void calculateFocusRect()
```

Calculates the focus rectangle.

---

#### calculateFocusRect

protected void calculateFocusRect()

Calculates the focus rectangle.

calculateThumbSize

```java
protected void calculateThumbSize()
```

Calculates the thumb size rectangle.

---

#### calculateThumbSize

protected void calculateThumbSize()

Calculates the thumb size rectangle.

calculateContentRect

```java
protected void calculateContentRect()
```

Calculates the content rectangle.

---

#### calculateContentRect

protected void calculateContentRect()

Calculates the content rectangle.

calculateThumbLocation

```java
protected void calculateThumbLocation()
```

Calculates the thumb location.

---

#### calculateThumbLocation

protected void calculateThumbLocation()

Calculates the thumb location.

calculateTrackBuffer

```java
protected void calculateTrackBuffer()
```

Calculates the track buffer.

---

#### calculateTrackBuffer

protected void calculateTrackBuffer()

Calculates the track buffer.

calculateTrackRect

```java
protected void calculateTrackRect()
```

Calculates the track rectangle.

---

#### calculateTrackRect

protected void calculateTrackRect()

Calculates the track rectangle.

getTickLength

```java
protected int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders. BasicSliderUI uses the returned value
to determine the tick area rectangle. If you want to give your ticks some
room, make this larger than you need and paint your ticks away from the
sides in paintTicks().

**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

---

#### getTickLength

protected int getTickLength()

Gets the height of the tick area for horizontal sliders and the width of
the tick area for vertical sliders. BasicSliderUI uses the returned value
to determine the tick area rectangle. If you want to give your ticks some
room, make this larger than you need and paint your ticks away from the
sides in paintTicks().

calculateTickRect

```java
protected void calculateTickRect()
```

Calculates the tick rectangle.

---

#### calculateTickRect

protected void calculateTickRect()

Calculates the tick rectangle.

calculateLabelRect

```java
protected void calculateLabelRect()
```

Calculates the label rectangle.

---

#### calculateLabelRect

protected void calculateLabelRect()

Calculates the label rectangle.

getThumbSize

```java
protected
Dimension
getThumbSize()
```

Returns the thumb size.

**Returns:** the thumb size

---

#### getThumbSize

protected

Dimension

getThumbSize()

Returns the thumb size.

getWidthOfWidestLabel

```java
protected int getWidthOfWidestLabel()
```

Returns the width of the widest label.

**Returns:** the width of the widest label

---

#### getWidthOfWidestLabel

protected int getWidthOfWidestLabel()

Returns the width of the widest label.

getHeightOfTallestLabel

```java
protected int getHeightOfTallestLabel()
```

Returns the height of the tallest label.

**Returns:** the height of the tallest label

---

#### getHeightOfTallestLabel

protected int getHeightOfTallestLabel()

Returns the height of the tallest label.

getWidthOfHighValueLabel

```java
protected int getWidthOfHighValueLabel()
```

Returns the width of the highest value label.

**Returns:** the width of the highest value label

---

#### getWidthOfHighValueLabel

protected int getWidthOfHighValueLabel()

Returns the width of the highest value label.

getWidthOfLowValueLabel

```java
protected int getWidthOfLowValueLabel()
```

Returns the width of the lowest value label.

**Returns:** the width of the lowest value label

---

#### getWidthOfLowValueLabel

protected int getWidthOfLowValueLabel()

Returns the width of the lowest value label.

getHeightOfHighValueLabel

```java
protected int getHeightOfHighValueLabel()
```

Returns the height of the highest value label.

**Returns:** the height of the highest value label

---

#### getHeightOfHighValueLabel

protected int getHeightOfHighValueLabel()

Returns the height of the highest value label.

getHeightOfLowValueLabel

```java
protected int getHeightOfLowValueLabel()
```

Returns the height of the lowest value label.

**Returns:** the height of the lowest value label

---

#### getHeightOfLowValueLabel

protected int getHeightOfLowValueLabel()

Returns the height of the lowest value label.

drawInverted

```java
protected boolean drawInverted()
```

Draws inverted.

**Returns:** the inverted-ness

---

#### drawInverted

protected boolean drawInverted()

Draws inverted.

getHighestValue

```java
protected
Integer
getHighestValue()
```

Returns the biggest value that has an entry in the label table.

**Returns:** biggest value that has an entry in the label table, or
null.
**Since:** 1.6

---

#### getHighestValue

protected

Integer

getHighestValue()

Returns the biggest value that has an entry in the label table.

getLowestValue

```java
protected
Integer
getLowestValue()
```

Returns the smallest value that has an entry in the label table.

**Returns:** smallest value that has an entry in the label table, or
null.
**Since:** 1.6

---

#### getLowestValue

protected

Integer

getLowestValue()

Returns the smallest value that has an entry in the label table.

getLowestValueLabel

```java
protected
Component
getLowestValueLabel()
```

Returns the label that corresponds to the highest slider value in the
label table.

**Returns:** the label that corresponds to the highest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

---

#### getLowestValueLabel

protected

Component

getLowestValueLabel()

Returns the label that corresponds to the highest slider value in the
label table.

getHighestValueLabel

```java
protected
Component
getHighestValueLabel()
```

Returns the label that corresponds to the lowest slider value in the
label table.

**Returns:** the label that corresponds to the lowest slider value in the
label table
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

---

#### getHighestValueLabel

protected

Component

getHighestValueLabel()

Returns the label that corresponds to the lowest slider value in the
label table.

recalculateIfInsetsChanged

```java
protected void recalculateIfInsetsChanged()
```

Recalculates if the insets have changed.

---

#### recalculateIfInsetsChanged

protected void recalculateIfInsetsChanged()

Recalculates if the insets have changed.

recalculateIfOrientationChanged

```java
protected void recalculateIfOrientationChanged()
```

Recalculates if the orientation has changed.

---

#### recalculateIfOrientationChanged

protected void recalculateIfOrientationChanged()

Recalculates if the orientation has changed.

paintFocus

```java
public void paintFocus​(
Graphics
g)
```

Paints focus.

**Parameters:** g

- the graphics

---

#### paintFocus

public void paintFocus​(

Graphics

g)

Paints focus.

paintTrack

```java
public void paintTrack​(
Graphics
g)
```

Paints track.

**Parameters:** g

- the graphics

---

#### paintTrack

public void paintTrack​(

Graphics

g)

Paints track.

paintTicks

```java
public void paintTicks​(
Graphics
g)
```

Paints ticks.

**Parameters:** g

- the graphics

---

#### paintTicks

public void paintTicks​(

Graphics

g)

Paints ticks.

paintMinorTickForHorizSlider

```java
protected void paintMinorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints minor tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

---

#### paintMinorTickForHorizSlider

protected void paintMinorTickForHorizSlider​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints minor tick for horizontal slider.

paintMajorTickForHorizSlider

```java
protected void paintMajorTickForHorizSlider​(
Graphics
g,

Rectangle
tickBounds,
int x)
```

Paints major tick for horizontal slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** x

- the x coordinate

---

#### paintMajorTickForHorizSlider

protected void paintMajorTickForHorizSlider​(

Graphics

g,

Rectangle

tickBounds,
int x)

Paints major tick for horizontal slider.

paintMinorTickForVertSlider

```java
protected void paintMinorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints minor tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

---

#### paintMinorTickForVertSlider

protected void paintMinorTickForVertSlider​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints minor tick for vertical slider.

paintMajorTickForVertSlider

```java
protected void paintMajorTickForVertSlider​(
Graphics
g,

Rectangle
tickBounds,
int y)
```

Paints major tick for vertical slider.

**Parameters:** g

- the graphics
**Parameters:** tickBounds

- the tick bounds
**Parameters:** y

- the y coordinate

---

#### paintMajorTickForVertSlider

protected void paintMajorTickForVertSlider​(

Graphics

g,

Rectangle

tickBounds,
int y)

Paints major tick for vertical slider.

paintLabels

```java
public void paintLabels​(
Graphics
g)
```

Paints the labels.

**Parameters:** g

- the graphics

---

#### paintLabels

public void paintLabels​(

Graphics

g)

Paints the labels.

paintHorizontalLabel

```java
protected void paintHorizontalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
horizontal sliders. The graphics have been translated to labelRect.y
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

---

#### paintHorizontalLabel

protected void paintHorizontalLabel​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table. Used to draw the labels for
horizontal sliders. The graphics have been translated to labelRect.y
already.

paintVerticalLabel

```java
protected void paintVerticalLabel​(
Graphics
g,
int value,

Component
label)
```

Called for every label in the label table. Used to draw the labels for
vertical sliders. The graphics have been translated to labelRect.x
already.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** value

- the value of the slider
**Parameters:** label

- the component label in the label table that needs to be
painted
**See Also:** JSlider.setLabelTable(java.util.Dictionary)

---

#### paintVerticalLabel

protected void paintVerticalLabel​(

Graphics

g,
int value,

Component

label)

Called for every label in the label table. Used to draw the labels for
vertical sliders. The graphics have been translated to labelRect.x
already.

paintThumb

```java
public void paintThumb​(
Graphics
g)
```

Paints the thumb.

**Parameters:** g

- the graphics

---

#### paintThumb

public void paintThumb​(

Graphics

g)

Paints the thumb.

setThumbLocation

```java
public void setThumbLocation​(int x,
int y)
```

Sets the thumb location.

**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate

---

#### setThumbLocation

public void setThumbLocation​(int x,
int y)

Sets the thumb location.

scrollByBlock

```java
public void scrollByBlock​(int direction)
```

Scrolls by block.

**Parameters:** direction

- the direction

---

#### scrollByBlock

public void scrollByBlock​(int direction)

Scrolls by block.

scrollByUnit

```java
public void scrollByUnit​(int direction)
```

Scrolls by unit.

**Parameters:** direction

- the direction

---

#### scrollByUnit

public void scrollByUnit​(int direction)

Scrolls by unit.

scrollDueToClickInTrack

```java
protected void scrollDueToClickInTrack​(int dir)
```

This function is called when a mousePressed was detected in the track,
not in the thumb. The default behavior is to scroll by block. You can
override this method to stop it from scrolling or to add additional
behavior.

**Parameters:** dir

- the direction and number of blocks to scroll

---

#### scrollDueToClickInTrack

protected void scrollDueToClickInTrack​(int dir)

This function is called when a mousePressed was detected in the track,
not in the thumb. The default behavior is to scroll by block. You can
override this method to stop it from scrolling or to add additional
behavior.

xPositionForValue

```java
protected int xPositionForValue​(int value)
```

Returns the x position for a value.

**Parameters:** value

- the value
**Returns:** the x position for a value

---

#### xPositionForValue

protected int xPositionForValue​(int value)

Returns the x position for a value.

yPositionForValue

```java
protected int yPositionForValue​(int value)
```

Returns the y position for a value.

**Parameters:** value

- the value
**Returns:** the y position for a value

---

#### yPositionForValue

protected int yPositionForValue​(int value)

Returns the y position for a value.

yPositionForValue

```java
protected int yPositionForValue​(int value,
int trackY,
int trackHeight)
```

Returns the y location for the specified value. No checking is
done on the arguments. In particular if

trackHeight

is
negative undefined results may occur.

**Parameters:** value

- the slider value to get the location for
**Parameters:** trackY

- y-origin of the track
**Parameters:** trackHeight

- the height of the track
**Returns:** the y location for the specified value of the slider
**Since:** 1.6

---

#### yPositionForValue

protected int yPositionForValue​(int value,
int trackY,
int trackHeight)

Returns the y location for the specified value. No checking is
done on the arguments. In particular if

trackHeight

is
negative undefined results may occur.

valueForYPosition

```java
public int valueForYPosition​(int yPos)
```

Returns the value at the y position. If

yPos

is beyond the
track at the bottom or the top, this method sets the value to either
the minimum or maximum value of the slider, depending on if the slider
is inverted or not.

**Parameters:** yPos

- the location of the slider along the y axis
**Returns:** the value at the y position

---

#### valueForYPosition

public int valueForYPosition​(int yPos)

Returns the value at the y position. If

yPos

is beyond the
track at the bottom or the top, this method sets the value to either
the minimum or maximum value of the slider, depending on if the slider
is inverted or not.

valueForXPosition

```java
public int valueForXPosition​(int xPos)
```

Returns the value at the x position. If

xPos

is beyond the
track at the left or the right, this method sets the value to either the
minimum or maximum value of the slider, depending on if the slider is
inverted or not.

**Parameters:** xPos

- the location of the slider along the x axis
**Returns:** the value of the x position

---

#### valueForXPosition

public int valueForXPosition​(int xPos)

Returns the value at the x position. If

xPos

is beyond the
track at the left or the right, this method sets the value to either the
minimum or maximum value of the slider, depending on if the slider is
inverted or not.

---

