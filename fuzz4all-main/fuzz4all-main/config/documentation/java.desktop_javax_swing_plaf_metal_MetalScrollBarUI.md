# Class MetalScrollBarUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalScrollBarUI.html`

### Class Description

```java
public class
MetalScrollBarUI

extends
BasicScrollBarUI
```

Implementation of ScrollBarUI for the Metal Look and Feel

**All Implemented Interfaces:** LayoutManager

,

SwingConstants

---

### Field Details

#### protected
MetalScrollButton
increaseButton

The increase button.

---

#### protected
MetalScrollButton
decreaseButton

The decrease button.

---

#### protected int scrollBarWidth

The width of the scroll bar.

---

#### public static final
String
FREE_STANDING_PROP

The property

JScrollBar.isFreeStanding

.

**See Also:**
- Constant Field Values

---

#### protected boolean isFreeStanding

The value of the property

JScrollBar.isFreeStanding

.

---

### Constructor Details

#### public MetalScrollBarUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Constructs a new

MetalScrollBarUI

instance.

**Parameters:**
- c

- a component

**Returns:**
- a new

MetalScrollBarUI

instance

---

#### protected
JButton
createDecreaseButton​(int orientation)

Returns the view that represents the decrease view.

**Overrides:**
- createDecreaseButton

in class

BasicScrollBarUI

**Parameters:**
- orientation

- the orientation

**Returns:**
- a decrease button

---

#### protected
JButton
createIncreaseButton​(int orientation)

Returns the view that represents the increase view.

**Overrides:**
- createIncreaseButton

in class

BasicScrollBarUI

**Parameters:**
- orientation

- the orientation

**Returns:**
- an increase button

---

#### protected void setThumbBounds​(int x,
int y,
int width,
int height)

This is overridden only to increase the invalid area. This
ensures that the "Shadow" below the thumb is invalidated

**Overrides:**
- setThumbBounds

in class

BasicScrollBarUI

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
- BasicScrollBarUI.getThumbBounds()

---

### Additional Sections

#### Class MetalScrollBarUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ScrollBarUI
- - javax.swing.plaf.basic.BasicScrollBarUI
- - javax.swing.plaf.metal.MetalScrollBarUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ScrollBarUI
- - javax.swing.plaf.basic.BasicScrollBarUI
- - javax.swing.plaf.metal.MetalScrollBarUI

javax.swing.plaf.ScrollBarUI

- javax.swing.plaf.basic.BasicScrollBarUI
- - javax.swing.plaf.metal.MetalScrollBarUI

javax.swing.plaf.basic.BasicScrollBarUI

- javax.swing.plaf.metal.MetalScrollBarUI

javax.swing.plaf.metal.MetalScrollBarUI

**All Implemented Interfaces:** LayoutManager

,

SwingConstants

```java
public class
MetalScrollBarUI

extends
BasicScrollBarUI
```

Implementation of ScrollBarUI for the Metal Look and Feel

public class

MetalScrollBarUI

extends

BasicScrollBarUI

Implementation of ScrollBarUI for the Metal Look and Feel

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicScrollBarUI

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.ModelListener

,

BasicScrollBarUI.PropertyChangeHandler

,

BasicScrollBarUI.ScrollListener

,

BasicScrollBarUI.TrackListener

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

MetalScrollButton

decreaseButton

The decrease button.

static

String

FREE_STANDING_PROP

The property

JScrollBar.isFreeStanding

.

protected

MetalScrollButton

increaseButton

The increase button.

protected boolean

isFreeStanding

The value of the property

JScrollBar.isFreeStanding

.

protected int

scrollBarWidth

The width of the scroll bar.

- Fields declared in class javax.swing.plaf.basic.

BasicScrollBarUI

buttonListener

,

decrButton

,

DECREASE_HIGHLIGHT

,

decrGap

,

incrButton

,

INCREASE_HIGHLIGHT

,

incrGap

,

isDragging

,

maximumThumbSize

,

minimumThumbSize

,

modelListener

,

NO_HIGHLIGHT

,

propertyChangeListener

,

scrollbar

,

scrollListener

,

scrollTimer

,

thumbDarkShadowColor

,

thumbLightShadowColor

,

thumbRect

,

trackColor

,

trackHighlight

,

trackHighlightColor

,

trackListener

,

trackRect

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

MetalScrollBarUI

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

protected

JButton

createDecreaseButton

​(int orientation)

Returns the view that represents the decrease view.

protected

JButton

createIncreaseButton

​(int orientation)

Returns the view that represents the increase view.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new

MetalScrollBarUI

instance.

protected void

setThumbBounds

​(int x,
int y,
int width,
int height)

This is overridden only to increase the invalid area.

- Methods declared in class javax.swing.plaf.basic.

BasicScrollBarUI

configureScrollBarColors

,

createArrowButtonListener

,

createModelListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

getMaximumSize

,

getMaximumThumbSize

,

getMinimumThumbSize

,

getPreferredSize

,

getSupportsAbsolutePositioning

,

getThumbBounds

,

getTrackBounds

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isThumbRollover

,

layoutHScrollbar

,

layoutVScrollbar

,

paintDecreaseHighlight

,

paintIncreaseHighlight

,

paintThumb

,

paintTrack

,

scrollByBlock

,

scrollByUnit

,

setThumbRollover

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicScrollBarUI

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.ModelListener

,

BasicScrollBarUI.PropertyChangeHandler

,

BasicScrollBarUI.ScrollListener

,

BasicScrollBarUI.TrackListener

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicScrollBarUI

BasicScrollBarUI.ArrowButtonListener

,

BasicScrollBarUI.ModelListener

,

BasicScrollBarUI.PropertyChangeHandler

,

BasicScrollBarUI.ScrollListener

,

BasicScrollBarUI.TrackListener

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicScrollBarUI

Field Summary

Fields

Modifier and Type

Field

Description

protected

MetalScrollButton

decreaseButton

The decrease button.

static

String

FREE_STANDING_PROP

The property

JScrollBar.isFreeStanding

.

protected

MetalScrollButton

increaseButton

The increase button.

protected boolean

isFreeStanding

The value of the property

JScrollBar.isFreeStanding

.

protected int

scrollBarWidth

The width of the scroll bar.

- Fields declared in class javax.swing.plaf.basic.

BasicScrollBarUI

buttonListener

,

decrButton

,

DECREASE_HIGHLIGHT

,

decrGap

,

incrButton

,

INCREASE_HIGHLIGHT

,

incrGap

,

isDragging

,

maximumThumbSize

,

minimumThumbSize

,

modelListener

,

NO_HIGHLIGHT

,

propertyChangeListener

,

scrollbar

,

scrollListener

,

scrollTimer

,

thumbDarkShadowColor

,

thumbLightShadowColor

,

thumbRect

,

trackColor

,

trackHighlight

,

trackHighlightColor

,

trackListener

,

trackRect

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

The decrease button.

The property

JScrollBar.isFreeStanding

.

The increase button.

The value of the property

JScrollBar.isFreeStanding

.

The width of the scroll bar.

Fields declared in class javax.swing.plaf.basic.

BasicScrollBarUI

buttonListener

,

decrButton

,

DECREASE_HIGHLIGHT

,

decrGap

,

incrButton

,

INCREASE_HIGHLIGHT

,

incrGap

,

isDragging

,

maximumThumbSize

,

minimumThumbSize

,

modelListener

,

NO_HIGHLIGHT

,

propertyChangeListener

,

scrollbar

,

scrollListener

,

scrollTimer

,

thumbDarkShadowColor

,

thumbLightShadowColor

,

thumbRect

,

trackColor

,

trackHighlight

,

trackHighlightColor

,

trackListener

,

trackRect

---

#### Fields declared in class javax.swing.plaf.basic. BasicScrollBarUI

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

MetalScrollBarUI

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

protected

JButton

createDecreaseButton

​(int orientation)

Returns the view that represents the decrease view.

protected

JButton

createIncreaseButton

​(int orientation)

Returns the view that represents the increase view.

static

ComponentUI

createUI

​(

JComponent

c)

Constructs a new

MetalScrollBarUI

instance.

protected void

setThumbBounds

​(int x,
int y,
int width,
int height)

This is overridden only to increase the invalid area.

- Methods declared in class javax.swing.plaf.basic.

BasicScrollBarUI

configureScrollBarColors

,

createArrowButtonListener

,

createModelListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

getMaximumSize

,

getMaximumThumbSize

,

getMinimumThumbSize

,

getPreferredSize

,

getSupportsAbsolutePositioning

,

getThumbBounds

,

getTrackBounds

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isThumbRollover

,

layoutHScrollbar

,

layoutVScrollbar

,

paintDecreaseHighlight

,

paintIncreaseHighlight

,

paintThumb

,

paintTrack

,

scrollByBlock

,

scrollByUnit

,

setThumbRollover

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

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

Returns the view that represents the decrease view.

Returns the view that represents the increase view.

Constructs a new

MetalScrollBarUI

instance.

This is overridden only to increase the invalid area.

Methods declared in class javax.swing.plaf.basic.

BasicScrollBarUI

configureScrollBarColors

,

createArrowButtonListener

,

createModelListener

,

createPropertyChangeListener

,

createScrollListener

,

createTrackListener

,

getMaximumSize

,

getMaximumThumbSize

,

getMinimumThumbSize

,

getPreferredSize

,

getSupportsAbsolutePositioning

,

getThumbBounds

,

getTrackBounds

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

installUI

,

isThumbRollover

,

layoutHScrollbar

,

layoutVScrollbar

,

paintDecreaseHighlight

,

paintIncreaseHighlight

,

paintThumb

,

paintTrack

,

scrollByBlock

,

scrollByUnit

,

setThumbRollover

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

uninstallUI

---

#### Methods declared in class javax.swing.plaf.basic. BasicScrollBarUI

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

- increaseButton

```java
protected
MetalScrollButton
increaseButton
```

The increase button.

- decreaseButton

```java
protected
MetalScrollButton
decreaseButton
```

The decrease button.

- scrollBarWidth

```java
protected int scrollBarWidth
```

The width of the scroll bar.

- FREE_STANDING_PROP

```java
public static final
String
FREE_STANDING_PROP
```

The property

JScrollBar.isFreeStanding

.

**See Also:** Constant Field Values

- isFreeStanding

```java
protected boolean isFreeStanding
```

The value of the property

JScrollBar.isFreeStanding

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalScrollBarUI

```java
public MetalScrollBarUI()
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

Constructs a new

MetalScrollBarUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalScrollBarUI

instance

- createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Returns the view that represents the decrease view.

**Overrides:** createDecreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** a decrease button

- createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Returns the view that represents the increase view.

**Overrides:** createIncreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** an increase button

- setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

This is overridden only to increase the invalid area. This
ensures that the "Shadow" below the thumb is invalidated

**Overrides:** setThumbBounds

in class

BasicScrollBarUI
**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** BasicScrollBarUI.getThumbBounds()

Field Detail

- increaseButton

```java
protected
MetalScrollButton
increaseButton
```

The increase button.

- decreaseButton

```java
protected
MetalScrollButton
decreaseButton
```

The decrease button.

- scrollBarWidth

```java
protected int scrollBarWidth
```

The width of the scroll bar.

- FREE_STANDING_PROP

```java
public static final
String
FREE_STANDING_PROP
```

The property

JScrollBar.isFreeStanding

.

**See Also:** Constant Field Values

- isFreeStanding

```java
protected boolean isFreeStanding
```

The value of the property

JScrollBar.isFreeStanding

.

---

#### Field Detail

increaseButton

```java
protected
MetalScrollButton
increaseButton
```

The increase button.

---

#### increaseButton

protected

MetalScrollButton

increaseButton

The increase button.

decreaseButton

```java
protected
MetalScrollButton
decreaseButton
```

The decrease button.

---

#### decreaseButton

protected

MetalScrollButton

decreaseButton

The decrease button.

scrollBarWidth

```java
protected int scrollBarWidth
```

The width of the scroll bar.

---

#### scrollBarWidth

protected int scrollBarWidth

The width of the scroll bar.

FREE_STANDING_PROP

```java
public static final
String
FREE_STANDING_PROP
```

The property

JScrollBar.isFreeStanding

.

**See Also:** Constant Field Values

---

#### FREE_STANDING_PROP

public static final

String

FREE_STANDING_PROP

The property

JScrollBar.isFreeStanding

.

isFreeStanding

```java
protected boolean isFreeStanding
```

The value of the property

JScrollBar.isFreeStanding

.

---

#### isFreeStanding

protected boolean isFreeStanding

The value of the property

JScrollBar.isFreeStanding

.

Constructor Detail

- MetalScrollBarUI

```java
public MetalScrollBarUI()
```

---

#### Constructor Detail

MetalScrollBarUI

```java
public MetalScrollBarUI()
```

---

#### MetalScrollBarUI

public MetalScrollBarUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Constructs a new

MetalScrollBarUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalScrollBarUI

instance

- createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Returns the view that represents the decrease view.

**Overrides:** createDecreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** a decrease button

- createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Returns the view that represents the increase view.

**Overrides:** createIncreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** an increase button

- setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

This is overridden only to increase the invalid area. This
ensures that the "Shadow" below the thumb is invalidated

**Overrides:** setThumbBounds

in class

BasicScrollBarUI
**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** BasicScrollBarUI.getThumbBounds()

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

Constructs a new

MetalScrollBarUI

instance.

**Parameters:** c

- a component
**Returns:** a new

MetalScrollBarUI

instance

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Constructs a new

MetalScrollBarUI

instance.

createDecreaseButton

```java
protected
JButton
createDecreaseButton​(int orientation)
```

Returns the view that represents the decrease view.

**Overrides:** createDecreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** a decrease button

---

#### createDecreaseButton

protected

JButton

createDecreaseButton​(int orientation)

Returns the view that represents the decrease view.

createIncreaseButton

```java
protected
JButton
createIncreaseButton​(int orientation)
```

Returns the view that represents the increase view.

**Overrides:** createIncreaseButton

in class

BasicScrollBarUI
**Parameters:** orientation

- the orientation
**Returns:** an increase button

---

#### createIncreaseButton

protected

JButton

createIncreaseButton​(int orientation)

Returns the view that represents the increase view.

setThumbBounds

```java
protected void setThumbBounds​(int x,
int y,
int width,
int height)
```

This is overridden only to increase the invalid area. This
ensures that the "Shadow" below the thumb is invalidated

**Overrides:** setThumbBounds

in class

BasicScrollBarUI
**Parameters:** x

- set the x location of the thumb
**Parameters:** y

- set the y location of the thumb
**Parameters:** width

- set the width of the thumb
**Parameters:** height

- set the height of the thumb
**See Also:** BasicScrollBarUI.getThumbBounds()

---

#### setThumbBounds

protected void setThumbBounds​(int x,
int y,
int width,
int height)

This is overridden only to increase the invalid area. This
ensures that the "Shadow" below the thumb is invalidated

---

