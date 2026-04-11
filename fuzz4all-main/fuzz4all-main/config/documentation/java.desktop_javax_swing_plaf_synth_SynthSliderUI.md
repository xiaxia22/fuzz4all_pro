# Class SynthSliderUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthSliderUI.html`

### Class Description

```java
public class
SynthSliderUI

extends
BasicSliderUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSlider

.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SynthSliderUI​(
JSlider
c)

Constructs a

SynthSliderUI

.

**Parameters:**
- c

- a slider

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Creates a new UI object for the given component.

**Parameters:**
- c

- component to create UI object for

**Returns:**
- the UI object

---

#### protected void uninstallDefaults​(
JSlider
slider)

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Overrides:**
- uninstallDefaults

in class

BasicSliderUI

**Parameters:**
- slider

- a slider

---

#### protected void layout()

Lays out the slider.

---

#### public void update​(
Graphics
g,

JComponent
c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:**
- update

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

object used for painting
- c

- the component being painted

**See Also:**
- paint(SynthContext,Graphics)

---

#### protected void paint​(
SynthContext
context,

Graphics
g)

Paints the specified component.

**Parameters:**
- context

- context for the component being painted
- g

- the

Graphics

object used for painting

**See Also:**
- update(Graphics,JComponent)

---

#### protected void paintThumb​(
SynthContext
context,

Graphics
g,

Rectangle
thumbBounds)

Paints the slider thumb.

**Parameters:**
- context

- context for the component being painted
- g

-

Graphics

object used for painting
- thumbBounds

- bounding box for the thumb

---

#### protected void paintTrack​(
SynthContext
context,

Graphics
g,

Rectangle
trackBounds)

Paints the slider track.

**Parameters:**
- context

- context for the component being painted
- g

-

Graphics

object used for painting
- trackBounds

- bounding box for the track

---

### Additional Sections

#### Class SynthSliderUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.synth.SynthSliderUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.synth.SynthSliderUI

javax.swing.plaf.SliderUI

- javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.synth.SynthSliderUI

javax.swing.plaf.basic.BasicSliderUI

- javax.swing.plaf.synth.SynthSliderUI

javax.swing.plaf.synth.SynthSliderUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthSliderUI

extends
BasicSliderUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JSlider

.

**Since:** 1.7

public class

SynthSliderUI

extends

BasicSliderUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JSlider

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicSliderUI

BasicSliderUI.ActionScroller

,

BasicSliderUI.ChangeHandler

,

BasicSliderUI.ComponentHandler

,

BasicSliderUI.FocusHandler

,

BasicSliderUI.PropertyChangeHandler

,

BasicSliderUI.ScrollListener

,

BasicSliderUI.TrackListener

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSliderUI

changeListener

,

componentListener

,

contentRect

,

focusInsets

,

focusListener

,

focusRect

,

insetCache

,

labelRect

,

leftToRightCache

,

MAX_SCROLL

,

MIN_SCROLL

,

NEGATIVE_SCROLL

,

POSITIVE_SCROLL

,

propertyChangeListener

,

scrollListener

,

scrollTimer

,

slider

,

thumbRect

,

tickRect

,

trackBuffer

,

trackListener

,

trackRect

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SynthSliderUI

​(

JSlider

c)

Constructs a

SynthSliderUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

protected void

layout

()

Lays out the slider.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintThumb

​(

SynthContext

context,

Graphics

g,

Rectangle

thumbBounds)

Paints the slider thumb.

protected void

paintTrack

​(

SynthContext

context,

Graphics

g,

Rectangle

trackBounds)

Paints the slider track.

protected void

uninstallDefaults

​(

JSlider

slider)

Uninstalls default setting.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSliderUI

calculateContentRect

,

calculateFocusRect

,

calculateGeometry

,

calculateLabelRect

,

calculateThumbLocation

,

calculateThumbSize

,

calculateTickRect

,

calculateTrackBuffer

,

calculateTrackRect

,

createChangeListener

,

createComponentListener

,

createFocusListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

drawInverted

,

getBaseline

,

getBaselineResizeBehavior

,

getFocusColor

,

getHeightOfHighValueLabel

,

getHeightOfLowValueLabel

,

getHeightOfTallestLabel

,

getHighestValue

,

getHighestValueLabel

,

getHighlightColor

,

getLowestValue

,

getLowestValueLabel

,

getMaximumSize

,

getMinimumHorizontalSize

,

getMinimumSize

,

getMinimumVerticalSize

,

getPreferredHorizontalSize

,

getPreferredSize

,

getPreferredVerticalSize

,

getShadowColor

,

getThumbSize

,

getTickLength

,

getWidthOfHighValueLabel

,

getWidthOfLowValueLabel

,

getWidthOfWidestLabel

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isDragging

,

labelsHaveSameBaselines

,

paintFocus

,

paintHorizontalLabel

,

paintLabels

,

paintMajorTickForHorizSlider

,

paintMajorTickForVertSlider

,

paintMinorTickForHorizSlider

,

paintMinorTickForVertSlider

,

paintThumb

,

paintTicks

,

paintTrack

,

paintVerticalLabel

,

recalculateIfInsetsChanged

,

recalculateIfOrientationChanged

,

scrollByBlock

,

scrollByUnit

,

scrollDueToClickInTrack

,

setThumbLocation

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

valueForXPosition

,

valueForYPosition

,

xPositionForValue

,

yPositionForValue

,

yPositionForValue

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicSliderUI

BasicSliderUI.ActionScroller

,

BasicSliderUI.ChangeHandler

,

BasicSliderUI.ComponentHandler

,

BasicSliderUI.FocusHandler

,

BasicSliderUI.PropertyChangeHandler

,

BasicSliderUI.ScrollListener

,

BasicSliderUI.TrackListener

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicSliderUI

BasicSliderUI.ActionScroller

,

BasicSliderUI.ChangeHandler

,

BasicSliderUI.ComponentHandler

,

BasicSliderUI.FocusHandler

,

BasicSliderUI.PropertyChangeHandler

,

BasicSliderUI.ScrollListener

,

BasicSliderUI.TrackListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicSliderUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicSliderUI

changeListener

,

componentListener

,

contentRect

,

focusInsets

,

focusListener

,

focusRect

,

insetCache

,

labelRect

,

leftToRightCache

,

MAX_SCROLL

,

MIN_SCROLL

,

NEGATIVE_SCROLL

,

POSITIVE_SCROLL

,

propertyChangeListener

,

scrollListener

,

scrollTimer

,

slider

,

thumbRect

,

tickRect

,

trackBuffer

,

trackListener

,

trackRect

- Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Field Summary

Fields declared in class javax.swing.plaf.basic.

BasicSliderUI

changeListener

,

componentListener

,

contentRect

,

focusInsets

,

focusListener

,

focusRect

,

insetCache

,

labelRect

,

leftToRightCache

,

MAX_SCROLL

,

MIN_SCROLL

,

NEGATIVE_SCROLL

,

POSITIVE_SCROLL

,

propertyChangeListener

,

scrollListener

,

scrollTimer

,

slider

,

thumbRect

,

tickRect

,

trackBuffer

,

trackListener

,

trackRect

---

#### Fields declared in class javax.swing.plaf.basic. BasicSliderUI

Fields declared in interface javax.swing.plaf.synth.

SynthConstants

DEFAULT

,

DISABLED

,

ENABLED

,

FOCUSED

,

MOUSE_OVER

,

PRESSED

,

SELECTED

---

#### Fields declared in interface javax.swing.plaf.synth. SynthConstants

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SynthSliderUI

​(

JSlider

c)

Constructs a

SynthSliderUI

.

---

#### Constructor Summary

Constructs a

SynthSliderUI

.

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

c)

Creates a new UI object for the given component.

protected void

layout

()

Lays out the slider.

void

paint

​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

protected void

paint

​(

SynthContext

context,

Graphics

g)

Paints the specified component.

protected void

paintThumb

​(

SynthContext

context,

Graphics

g,

Rectangle

thumbBounds)

Paints the slider thumb.

protected void

paintTrack

​(

SynthContext

context,

Graphics

g,

Rectangle

trackBounds)

Paints the slider track.

protected void

uninstallDefaults

​(

JSlider

slider)

Uninstalls default setting.

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

- Methods declared in class javax.swing.plaf.basic.

BasicSliderUI

calculateContentRect

,

calculateFocusRect

,

calculateGeometry

,

calculateLabelRect

,

calculateThumbLocation

,

calculateThumbSize

,

calculateTickRect

,

calculateTrackBuffer

,

calculateTrackRect

,

createChangeListener

,

createComponentListener

,

createFocusListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

drawInverted

,

getBaseline

,

getBaselineResizeBehavior

,

getFocusColor

,

getHeightOfHighValueLabel

,

getHeightOfLowValueLabel

,

getHeightOfTallestLabel

,

getHighestValue

,

getHighestValueLabel

,

getHighlightColor

,

getLowestValue

,

getLowestValueLabel

,

getMaximumSize

,

getMinimumHorizontalSize

,

getMinimumSize

,

getMinimumVerticalSize

,

getPreferredHorizontalSize

,

getPreferredSize

,

getPreferredVerticalSize

,

getShadowColor

,

getThumbSize

,

getTickLength

,

getWidthOfHighValueLabel

,

getWidthOfLowValueLabel

,

getWidthOfWidestLabel

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isDragging

,

labelsHaveSameBaselines

,

paintFocus

,

paintHorizontalLabel

,

paintLabels

,

paintMajorTickForHorizSlider

,

paintMajorTickForVertSlider

,

paintMinorTickForHorizSlider

,

paintMinorTickForVertSlider

,

paintThumb

,

paintTicks

,

paintTrack

,

paintVerticalLabel

,

recalculateIfInsetsChanged

,

recalculateIfOrientationChanged

,

scrollByBlock

,

scrollByUnit

,

scrollDueToClickInTrack

,

setThumbLocation

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

valueForXPosition

,

valueForYPosition

,

xPositionForValue

,

yPositionForValue

,

yPositionForValue

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

- Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Method Summary

Creates a new UI object for the given component.

Lays out the slider.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Paints the slider thumb.

Paints the slider track.

Uninstalls default setting.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicSliderUI

calculateContentRect

,

calculateFocusRect

,

calculateGeometry

,

calculateLabelRect

,

calculateThumbLocation

,

calculateThumbSize

,

calculateTickRect

,

calculateTrackBuffer

,

calculateTrackRect

,

createChangeListener

,

createComponentListener

,

createFocusListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

drawInverted

,

getBaseline

,

getBaselineResizeBehavior

,

getFocusColor

,

getHeightOfHighValueLabel

,

getHeightOfLowValueLabel

,

getHeightOfTallestLabel

,

getHighestValue

,

getHighestValueLabel

,

getHighlightColor

,

getLowestValue

,

getLowestValueLabel

,

getMaximumSize

,

getMinimumHorizontalSize

,

getMinimumSize

,

getMinimumVerticalSize

,

getPreferredHorizontalSize

,

getPreferredSize

,

getPreferredVerticalSize

,

getShadowColor

,

getThumbSize

,

getTickLength

,

getWidthOfHighValueLabel

,

getWidthOfLowValueLabel

,

getWidthOfWidestLabel

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isDragging

,

labelsHaveSameBaselines

,

paintFocus

,

paintHorizontalLabel

,

paintLabels

,

paintMajorTickForHorizSlider

,

paintMajorTickForVertSlider

,

paintMinorTickForHorizSlider

,

paintMinorTickForVertSlider

,

paintThumb

,

paintTicks

,

paintTrack

,

paintVerticalLabel

,

recalculateIfInsetsChanged

,

recalculateIfOrientationChanged

,

scrollByBlock

,

scrollByUnit

,

scrollDueToClickInTrack

,

setThumbLocation

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

,

valueForXPosition

,

valueForYPosition

,

xPositionForValue

,

yPositionForValue

,

yPositionForValue

---

#### Methods declared in class javax.swing.plaf.basic. BasicSliderUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

Methods declared in interface javax.swing.plaf.synth.

SynthUI

getContext

,

paintBorder

---

#### Methods declared in interface javax.swing.plaf.synth. SynthUI

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SynthSliderUI

```java
protected SynthSliderUI​(
JSlider
c)
```

Constructs a

SynthSliderUI

.

**Parameters:** c

- a slider

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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Overrides:** uninstallDefaults

in class

BasicSliderUI
**Parameters:** slider

- a slider

- layout

```java
protected void layout()
```

Lays out the slider.

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintThumb

```java
protected void paintThumb​(
SynthContext
context,

Graphics
g,

Rectangle
thumbBounds)
```

Paints the slider thumb.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** thumbBounds

- bounding box for the thumb

- paintTrack

```java
protected void paintTrack​(
SynthContext
context,

Graphics
g,

Rectangle
trackBounds)
```

Paints the slider track.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** trackBounds

- bounding box for the track

Constructor Detail

- SynthSliderUI

```java
protected SynthSliderUI​(
JSlider
c)
```

Constructs a

SynthSliderUI

.

**Parameters:** c

- a slider

---

#### Constructor Detail

SynthSliderUI

```java
protected SynthSliderUI​(
JSlider
c)
```

Constructs a

SynthSliderUI

.

**Parameters:** c

- a slider

---

#### SynthSliderUI

protected SynthSliderUI​(

JSlider

c)

Constructs a

SynthSliderUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Overrides:** uninstallDefaults

in class

BasicSliderUI
**Parameters:** slider

- a slider

- layout

```java
protected void layout()
```

Lays out the slider.

- update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

- paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

- paintThumb

```java
protected void paintThumb​(
SynthContext
context,

Graphics
g,

Rectangle
thumbBounds)
```

Paints the slider thumb.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** thumbBounds

- bounding box for the thumb

- paintTrack

```java
protected void paintTrack​(
SynthContext
context,

Graphics
g,

Rectangle
trackBounds)
```

Paints the slider track.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** trackBounds

- bounding box for the track

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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Creates a new UI object for the given component.

uninstallDefaults

```java
protected void uninstallDefaults​(
JSlider
slider)
```

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

**Overrides:** uninstallDefaults

in class

BasicSliderUI
**Parameters:** slider

- a slider

---

#### uninstallDefaults

protected void uninstallDefaults​(

JSlider

slider)

Uninstalls default setting. This method is called when a

LookAndFeel

is uninstalled.

layout

```java
protected void layout()
```

Lays out the slider.

---

#### layout

protected void layout()

Lays out the slider.

update

```java
public void update​(
Graphics
g,

JComponent
c)
```

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

**Overrides:** update

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### update

public void update​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.
This method paints the component background, then calls
the

paint(SynthContext,Graphics)

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

In general, this method does not need to be overridden by subclasses.
All Look and Feel rendering code should reside in the

paint

method.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

object used for painting
**Parameters:** c

- the component being painted
**See Also:** paint(SynthContext,Graphics)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paints the specified component according to the Look and Feel.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

This method is not used by Synth Look and Feel.
Painting is handled by the

paint(SynthContext,Graphics)

method.

paint

```java
protected void paint​(
SynthContext
context,

Graphics
g)
```

Paints the specified component.

**Parameters:** context

- context for the component being painted
**Parameters:** g

- the

Graphics

object used for painting
**See Also:** update(Graphics,JComponent)

---

#### paint

protected void paint​(

SynthContext

context,

Graphics

g)

Paints the specified component.

paintThumb

```java
protected void paintThumb​(
SynthContext
context,

Graphics
g,

Rectangle
thumbBounds)
```

Paints the slider thumb.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** thumbBounds

- bounding box for the thumb

---

#### paintThumb

protected void paintThumb​(

SynthContext

context,

Graphics

g,

Rectangle

thumbBounds)

Paints the slider thumb.

paintTrack

```java
protected void paintTrack​(
SynthContext
context,

Graphics
g,

Rectangle
trackBounds)
```

Paints the slider track.

**Parameters:** context

- context for the component being painted
**Parameters:** g

-

Graphics

object used for painting
**Parameters:** trackBounds

- bounding box for the track

---

#### paintTrack

protected void paintTrack​(

SynthContext

context,

Graphics

g,

Rectangle

trackBounds)

Paints the slider track.

---

