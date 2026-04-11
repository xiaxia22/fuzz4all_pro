# Class MetalSliderUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalSliderUI.html`

### Class Description

```java
public class
MetalSliderUI

extends
BasicSliderUI
```

A Java L&F implementation of SliderUI.

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

---

### Field Details

#### protected final int TICK_BUFFER

The buffer of a tick.

**See Also:**
- Constant Field Values

---

#### protected boolean filledSlider

The value of the property

JSlider.isFilled

.
By default,

false

if the property is not set,

true

for Ocean theme.

---

#### protected static
Color
thumbColor

The color of a thumb

---

#### protected static
Color
highlightColor

The color of highlighting.

---

#### protected static
Color
darkShadowColor

The color of dark shadow.

---

#### protected static int trackWidth

The width of a track.

---

#### protected static int tickLength

The length of a tick.

---

#### protected static
Icon
horizThumbIcon

A default horizontal thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.horizontalThumbIcon

UIManager property.

---

#### protected static
Icon
vertThumbIcon

A default vertical thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.verticalThumbIcon

UIManager property.

---

#### protected final
String
SLIDER_FILL

Property for

JSlider.isFilled

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MetalSliderUI()

Constructs a

MetalSliderUI

instance.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a

MetalSliderUI

instance.

**Parameters:**
- c

- a component

**Returns:**
- a

MetalSliderUI

instance

---

#### protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)

Constructs

MetalPropertyListener

.

**Overrides:**
- createPropertyChangeListener

in class

BasicSliderUI

**Parameters:**
- slider

- a

JSlider

**Returns:**
- the

MetalPropertyListener

---

#### public int getTickLength()

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders. BasicSliderUI uses the returned value to
determine the tick area rectangle.

**Overrides:**
- getTickLength

in class

BasicSliderUI

**Returns:**
- an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

---

#### protected int getTrackWidth()

Returns the shorter dimension of the track.

**Returns:**
- the shorter dimension of the track

---

#### protected int getTrackLength()

Returns the longer dimension of the slide bar. (The slide bar is only the
part that runs directly under the thumb)

**Returns:**
- the longer dimension of the slide bar

---

#### protected int getThumbOverhang()

Returns the amount that the thumb goes past the slide bar.

**Returns:**
- the amount that the thumb goes past the slide bar

---

### Additional Sections

#### Class MetalSliderUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.metal.MetalSliderUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.SliderUI
- - javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.metal.MetalSliderUI

javax.swing.plaf.SliderUI

- javax.swing.plaf.basic.BasicSliderUI
- - javax.swing.plaf.metal.MetalSliderUI

javax.swing.plaf.basic.BasicSliderUI

- javax.swing.plaf.metal.MetalSliderUI

javax.swing.plaf.metal.MetalSliderUI

```java
public class
MetalSliderUI

extends
BasicSliderUI
```

A Java L&F implementation of SliderUI.

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

public class

MetalSliderUI

extends

BasicSliderUI

A Java L&F implementation of SliderUI.

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

MetalSliderUI.MetalPropertyListener

PropertyListener

for

JSlider.isFilled

.

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

Fields

Modifier and Type

Field

Description

protected static

Color

darkShadowColor

The color of dark shadow.

protected boolean

filledSlider

The value of the property

JSlider.isFilled

.

protected static

Color

highlightColor

The color of highlighting.

protected static

Icon

horizThumbIcon

A default horizontal thumb

Icon

.

protected

String

SLIDER_FILL

Property for

JSlider.isFilled

.

protected static

Color

thumbColor

The color of a thumb

protected int

TICK_BUFFER

The buffer of a tick.

protected static int

tickLength

The length of a tick.

protected static int

trackWidth

The width of a track.

protected static

Icon

vertThumbIcon

A default vertical thumb

Icon

.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalSliderUI

()

Constructs a

MetalSliderUI

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

PropertyChangeListener

createPropertyChangeListener

​(

JSlider

slider)

Constructs

MetalPropertyListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a

MetalSliderUI

instance.

protected int

getThumbOverhang

()

Returns the amount that the thumb goes past the slide bar.

int

getTickLength

()

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders.

protected int

getTrackLength

()

Returns the longer dimension of the slide bar.

protected int

getTrackWidth

()

Returns the shorter dimension of the track.

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

uninstallDefaults

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

protected class

MetalSliderUI.MetalPropertyListener

PropertyListener

for

JSlider.isFilled

.

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

PropertyListener

for

JSlider.isFilled

.

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

Fields

Modifier and Type

Field

Description

protected static

Color

darkShadowColor

The color of dark shadow.

protected boolean

filledSlider

The value of the property

JSlider.isFilled

.

protected static

Color

highlightColor

The color of highlighting.

protected static

Icon

horizThumbIcon

A default horizontal thumb

Icon

.

protected

String

SLIDER_FILL

Property for

JSlider.isFilled

.

protected static

Color

thumbColor

The color of a thumb

protected int

TICK_BUFFER

The buffer of a tick.

protected static int

tickLength

The length of a tick.

protected static int

trackWidth

The width of a track.

protected static

Icon

vertThumbIcon

A default vertical thumb

Icon

.

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

---

#### Field Summary

The color of dark shadow.

The value of the property

JSlider.isFilled

.

The color of highlighting.

A default horizontal thumb

Icon

.

Property for

JSlider.isFilled

.

The color of a thumb

The buffer of a tick.

The length of a tick.

The width of a track.

A default vertical thumb

Icon

.

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

Constructor Summary

Constructors

Constructor

Description

MetalSliderUI

()

Constructs a

MetalSliderUI

instance.

---

#### Constructor Summary

Constructs a

MetalSliderUI

instance.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

PropertyChangeListener

createPropertyChangeListener

​(

JSlider

slider)

Constructs

MetalPropertyListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a

MetalSliderUI

instance.

protected int

getThumbOverhang

()

Returns the amount that the thumb goes past the slide bar.

int

getTickLength

()

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders.

protected int

getTrackLength

()

Returns the longer dimension of the slide bar.

protected int

getTrackWidth

()

Returns the shorter dimension of the track.

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

uninstallDefaults

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

Constructs

MetalPropertyListener

.

Constructs a

MetalSliderUI

instance.

Returns the amount that the thumb goes past the slide bar.

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders.

Returns the longer dimension of the slide bar.

Returns the shorter dimension of the track.

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

uninstallDefaults

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

- TICK_BUFFER

```java
protected final int TICK_BUFFER
```

The buffer of a tick.

**See Also:** Constant Field Values

- filledSlider

```java
protected boolean filledSlider
```

The value of the property

JSlider.isFilled

.
By default,

false

if the property is not set,

true

for Ocean theme.

- thumbColor

```java
protected static
Color
thumbColor
```

The color of a thumb

- highlightColor

```java
protected static
Color
highlightColor
```

The color of highlighting.

- darkShadowColor

```java
protected static
Color
darkShadowColor
```

The color of dark shadow.

- trackWidth

```java
protected static int trackWidth
```

The width of a track.

- tickLength

```java
protected static int tickLength
```

The length of a tick.

- horizThumbIcon

```java
protected static
Icon
horizThumbIcon
```

A default horizontal thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.horizontalThumbIcon

UIManager property.

- vertThumbIcon

```java
protected static
Icon
vertThumbIcon
```

A default vertical thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.verticalThumbIcon

UIManager property.

- SLIDER_FILL

```java
protected final
String
SLIDER_FILL
```

Property for

JSlider.isFilled

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalSliderUI

```java
public MetalSliderUI()
```

Constructs a

MetalSliderUI

instance.

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

Constructs a

MetalSliderUI

instance.

**Parameters:** c

- a component
**Returns:** a

MetalSliderUI

instance

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Constructs

MetalPropertyListener

.

**Overrides:** createPropertyChangeListener

in class

BasicSliderUI
**Parameters:** slider

- a

JSlider
**Returns:** the

MetalPropertyListener

- getTickLength

```java
public int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders. BasicSliderUI uses the returned value to
determine the tick area rectangle.

**Overrides:** getTickLength

in class

BasicSliderUI
**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

- getTrackWidth

```java
protected int getTrackWidth()
```

Returns the shorter dimension of the track.

**Returns:** the shorter dimension of the track

- getTrackLength

```java
protected int getTrackLength()
```

Returns the longer dimension of the slide bar. (The slide bar is only the
part that runs directly under the thumb)

**Returns:** the longer dimension of the slide bar

- getThumbOverhang

```java
protected int getThumbOverhang()
```

Returns the amount that the thumb goes past the slide bar.

**Returns:** the amount that the thumb goes past the slide bar

Field Detail

- TICK_BUFFER

```java
protected final int TICK_BUFFER
```

The buffer of a tick.

**See Also:** Constant Field Values

- filledSlider

```java
protected boolean filledSlider
```

The value of the property

JSlider.isFilled

.
By default,

false

if the property is not set,

true

for Ocean theme.

- thumbColor

```java
protected static
Color
thumbColor
```

The color of a thumb

- highlightColor

```java
protected static
Color
highlightColor
```

The color of highlighting.

- darkShadowColor

```java
protected static
Color
darkShadowColor
```

The color of dark shadow.

- trackWidth

```java
protected static int trackWidth
```

The width of a track.

- tickLength

```java
protected static int tickLength
```

The length of a tick.

- horizThumbIcon

```java
protected static
Icon
horizThumbIcon
```

A default horizontal thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.horizontalThumbIcon

UIManager property.

- vertThumbIcon

```java
protected static
Icon
vertThumbIcon
```

A default vertical thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.verticalThumbIcon

UIManager property.

- SLIDER_FILL

```java
protected final
String
SLIDER_FILL
```

Property for

JSlider.isFilled

.

**See Also:** Constant Field Values

---

#### Field Detail

TICK_BUFFER

```java
protected final int TICK_BUFFER
```

The buffer of a tick.

**See Also:** Constant Field Values

---

#### TICK_BUFFER

protected final int TICK_BUFFER

The buffer of a tick.

filledSlider

```java
protected boolean filledSlider
```

The value of the property

JSlider.isFilled

.
By default,

false

if the property is not set,

true

for Ocean theme.

---

#### filledSlider

protected boolean filledSlider

The value of the property

JSlider.isFilled

.
By default,

false

if the property is not set,

true

for Ocean theme.

thumbColor

```java
protected static
Color
thumbColor
```

The color of a thumb

---

#### thumbColor

protected static

Color

thumbColor

The color of a thumb

highlightColor

```java
protected static
Color
highlightColor
```

The color of highlighting.

---

#### highlightColor

protected static

Color

highlightColor

The color of highlighting.

darkShadowColor

```java
protected static
Color
darkShadowColor
```

The color of dark shadow.

---

#### darkShadowColor

protected static

Color

darkShadowColor

The color of dark shadow.

trackWidth

```java
protected static int trackWidth
```

The width of a track.

---

#### trackWidth

protected static int trackWidth

The width of a track.

tickLength

```java
protected static int tickLength
```

The length of a tick.

---

#### tickLength

protected static int tickLength

The length of a tick.

horizThumbIcon

```java
protected static
Icon
horizThumbIcon
```

A default horizontal thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.horizontalThumbIcon

UIManager property.

---

#### horizThumbIcon

protected static

Icon

horizThumbIcon

A default horizontal thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.horizontalThumbIcon

UIManager property.

vertThumbIcon

```java
protected static
Icon
vertThumbIcon
```

A default vertical thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.verticalThumbIcon

UIManager property.

---

#### vertThumbIcon

protected static

Icon

vertThumbIcon

A default vertical thumb

Icon

. This field might not be
used. To change the

Icon

used by this delegate directly set it
using the

Slider.verticalThumbIcon

UIManager property.

SLIDER_FILL

```java
protected final
String
SLIDER_FILL
```

Property for

JSlider.isFilled

.

**See Also:** Constant Field Values

---

#### SLIDER_FILL

protected final

String

SLIDER_FILL

Property for

JSlider.isFilled

.

Constructor Detail

- MetalSliderUI

```java
public MetalSliderUI()
```

Constructs a

MetalSliderUI

instance.

---

#### Constructor Detail

MetalSliderUI

```java
public MetalSliderUI()
```

Constructs a

MetalSliderUI

instance.

---

#### MetalSliderUI

public MetalSliderUI()

Constructs a

MetalSliderUI

instance.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a

MetalSliderUI

instance.

**Parameters:** c

- a component
**Returns:** a

MetalSliderUI

instance

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Constructs

MetalPropertyListener

.

**Overrides:** createPropertyChangeListener

in class

BasicSliderUI
**Parameters:** slider

- a

JSlider
**Returns:** the

MetalPropertyListener

- getTickLength

```java
public int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders. BasicSliderUI uses the returned value to
determine the tick area rectangle.

**Overrides:** getTickLength

in class

BasicSliderUI
**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

- getTrackWidth

```java
protected int getTrackWidth()
```

Returns the shorter dimension of the track.

**Returns:** the shorter dimension of the track

- getTrackLength

```java
protected int getTrackLength()
```

Returns the longer dimension of the slide bar. (The slide bar is only the
part that runs directly under the thumb)

**Returns:** the longer dimension of the slide bar

- getThumbOverhang

```java
protected int getThumbOverhang()
```

Returns the amount that the thumb goes past the slide bar.

**Returns:** the amount that the thumb goes past the slide bar

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

Constructs a

MetalSliderUI

instance.

**Parameters:** c

- a component
**Returns:** a

MetalSliderUI

instance

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a

MetalSliderUI

instance.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener​(
JSlider
slider)
```

Constructs

MetalPropertyListener

.

**Overrides:** createPropertyChangeListener

in class

BasicSliderUI
**Parameters:** slider

- a

JSlider
**Returns:** the

MetalPropertyListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener​(

JSlider

slider)

Constructs

MetalPropertyListener

.

getTickLength

```java
public int getTickLength()
```

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders. BasicSliderUI uses the returned value to
determine the tick area rectangle.

**Overrides:** getTickLength

in class

BasicSliderUI
**Returns:** an integer representing the height of the tick area for
horizontal sliders, and the width of the tick area for the vertical
sliders

---

#### getTickLength

public int getTickLength()

Gets the height of the tick area for horizontal sliders and the width of the
tick area for vertical sliders. BasicSliderUI uses the returned value to
determine the tick area rectangle.

getTrackWidth

```java
protected int getTrackWidth()
```

Returns the shorter dimension of the track.

**Returns:** the shorter dimension of the track

---

#### getTrackWidth

protected int getTrackWidth()

Returns the shorter dimension of the track.

getTrackLength

```java
protected int getTrackLength()
```

Returns the longer dimension of the slide bar. (The slide bar is only the
part that runs directly under the thumb)

**Returns:** the longer dimension of the slide bar

---

#### getTrackLength

protected int getTrackLength()

Returns the longer dimension of the slide bar. (The slide bar is only the
part that runs directly under the thumb)

getThumbOverhang

```java
protected int getThumbOverhang()
```

Returns the amount that the thumb goes past the slide bar.

**Returns:** the amount that the thumb goes past the slide bar

---

#### getThumbOverhang

protected int getThumbOverhang()

Returns the amount that the thumb goes past the slide bar.

---

