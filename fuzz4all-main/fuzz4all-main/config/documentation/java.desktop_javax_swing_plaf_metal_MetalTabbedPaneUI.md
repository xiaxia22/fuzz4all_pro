# Class MetalTabbedPaneUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalTabbedPaneUI.html`

### Class Description

```java
public class
MetalTabbedPaneUI

extends
BasicTabbedPaneUI
```

The Metal subclass of BasicTabbedPaneUI.

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

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected int minTabWidth

The minimum width of a pane.

---

#### protected
Color
tabAreaBackground

The color of tab's background.

---

#### protected
Color
selectColor

The color of the selected pane.

---

#### protected
Color
selectHighlight

The color of the highlight.

---

### Constructor Details

#### public MetalTabbedPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs

MetalTabbedPaneUI

.

**Parameters:**
- x

- a component

**Returns:**
- an instance of

MetalTabbedPaneUI

---

#### protected void paintTopTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the top tab border.

**Parameters:**
- tabIndex

- a tab index
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- btm

- bottom
- rght

- right
- isSelected

- a selection

---

#### protected boolean shouldFillGap​(int currentRun,
int tabIndex,
int x,
int y)

Returns

true

if the gap should be filled.

**Parameters:**
- currentRun

- the current run
- tabIndex

- the tab index
- x

- an X coordinate
- y

- an Y coordinate

**Returns:**
- true

if the gap should be filled

---

#### protected
Color
getColorForGap​(int currentRun,
int x,
int y)

Returns the color of the gap.

**Parameters:**
- currentRun

- the current run
- x

- an X coordinate
- y

- an Y coordinate

**Returns:**
- the color of the gap

---

#### protected void paintLeftTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the left tab border.

**Parameters:**
- tabIndex

- a tab index
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- btm

- bottom
- rght

- right
- isSelected

- a selection

---

#### protected void paintBottomTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the bottom tab border.

**Parameters:**
- tabIndex

- a tab index
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- btm

- bottom
- rght

- right
- isSelected

- a selection

---

#### protected void paintRightTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the right tab border.

**Parameters:**
- tabIndex

- a tab index
- g

- an instance of

Graphics
- x

- an X coordinate
- y

- an Y coordinate
- w

- a width
- h

- a height
- btm

- bottom
- rght

- right
- isSelected

- a selection

---

#### protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

**Overrides:**
- getTabLabelShiftX

in class

BasicTabbedPaneUI

**Parameters:**
- tabPlacement

- the tab placement
- tabIndex

- the tab index
- isSelected

- selection status

**Returns:**
- the tab label shift x

---

#### protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

**Overrides:**
- getTabLabelShiftY

in class

BasicTabbedPaneUI

**Parameters:**
- tabPlacement

- the tab placement
- tabIndex

- the tab index
- isSelected

- selection status

**Returns:**
- the tab label shift y

---

#### protected int getBaselineOffset()

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Overrides:**
- getBaselineOffset

in class

BasicTabbedPaneUI

**Returns:**
- amount to offset the baseline by

**Since:**
- 1.6

---

#### protected void paintHighlightBelowTab()

Paints highlights below tab.

---

#### protected boolean shouldRotateTabRuns​(int tabPlacement,
int selectedRun)

Returns

true

if tab runs should be rotated.

**Parameters:**
- tabPlacement

- a tab placement
- selectedRun

- a selected run

**Returns:**
- true

if tab runs should be rotated.

---

### Additional Sections

#### Class MetalTabbedPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.metal.MetalTabbedPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.metal.MetalTabbedPaneUI

javax.swing.plaf.TabbedPaneUI

- javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.metal.MetalTabbedPaneUI

javax.swing.plaf.basic.BasicTabbedPaneUI

- javax.swing.plaf.metal.MetalTabbedPaneUI

javax.swing.plaf.metal.MetalTabbedPaneUI

**All Implemented Interfaces:** SwingConstants

```java
public class
MetalTabbedPaneUI

extends
BasicTabbedPaneUI
```

The Metal subclass of BasicTabbedPaneUI.

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

MetalTabbedPaneUI

extends

BasicTabbedPaneUI

The Metal subclass of BasicTabbedPaneUI.

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

class

MetalTabbedPaneUI.TabbedPaneLayout

This class should be treated as a "protected" inner class.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabSelectionHandler

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

minTabWidth

The minimum width of a pane.

protected

Color

selectColor

The color of the selected pane.

protected

Color

selectHighlight

The color of the highlight.

protected

Color

tabAreaBackground

The color of tab's background.

- Fields declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

calcRect

,

contentBorderInsets

,

darkShadow

,

downKey

,

focus

,

focusListener

,

highlight

,

leftKey

,

lightHighlight

,

maxTabHeight

,

maxTabWidth

,

mouseListener

,

propertyChangeListener

,

rects

,

rightKey

,

runCount

,

selectedRun

,

selectedTabPadInsets

,

shadow

,

tabAreaInsets

,

tabChangeListener

,

tabInsets

,

tabPane

,

tabRunOverlay

,

tabRuns

,

textIconGap

,

upKey

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

MetalTabbedPaneUI

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

Constructs

MetalTabbedPaneUI

.

protected int

getBaselineOffset

()

Returns the amount the baseline is offset by.

protected

Color

getColorForGap

​(int currentRun,
int x,
int y)

Returns the color of the gap.

protected int

getTabLabelShiftX

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

protected int

getTabLabelShiftY

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

protected void

paintBottomTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the bottom tab border.

protected void

paintHighlightBelowTab

()

Paints highlights below tab.

protected void

paintLeftTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the left tab border.

protected void

paintRightTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the right tab border.

protected void

paintTopTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the top tab border.

protected boolean

shouldFillGap

​(int currentRun,
int tabIndex,
int x,
int y)

Returns

true

if the gap should be filled.

protected boolean

shouldRotateTabRuns

​(int tabPlacement,
int selectedRun)

Returns

true

if tab runs should be rotated.

- Methods declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

assureRectsCreated

,

calculateMaxTabHeight

,

calculateMaxTabWidth

,

calculateTabAreaHeight

,

calculateTabAreaWidth

,

calculateTabHeight

,

calculateTabWidth

,

createChangeListener

,

createFocusListener

,

createLayoutManager

,

createMouseListener

,

createPropertyChangeListener

,

createScrollButton

,

expandTabRunsArray

,

getBaseline

,

getBaseline

,

getBaselineResizeBehavior

,

getContentBorderInsets

,

getFocusIndex

,

getFontMetrics

,

getIconForTab

,

getNextTabIndex

,

getNextTabIndexInRun

,

getNextTabRun

,

getPreviousTabIndex

,

getPreviousTabIndexInRun

,

getPreviousTabRun

,

getRolloverTab

,

getRunForTab

,

getSelectedTabPadInsets

,

getTabAreaInsets

,

getTabBounds

,

getTabBounds

,

getTabInsets

,

getTabRunIndent

,

getTabRunOffset

,

getTabRunOverlay

,

getTextViewForTab

,

getVisibleComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

lastTabInRun

,

layoutLabel

,

navigateSelectedTab

,

paintContentBorder

,

paintContentBorderBottomEdge

,

paintContentBorderLeftEdge

,

paintContentBorderRightEdge

,

paintContentBorderTopEdge

,

paintFocusIndicator

,

paintIcon

,

paintTab

,

paintTabArea

,

paintTabBackground

,

paintTabBorder

,

paintText

,

rotateInsets

,

selectAdjacentRunTab

,

selectNextTab

,

selectNextTabInRun

,

selectPreviousTab

,

selectPreviousTabInRun

,

setRolloverTab

,

setVisibleComponent

,

shouldPadTabRun

,

shouldRotateTabRuns

,

tabForCoordinate

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

TabbedPaneUI

getTabRunCount

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

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

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

MetalTabbedPaneUI.TabbedPaneLayout

This class should be treated as a "protected" inner class.

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabSelectionHandler

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabSelectionHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicTabbedPaneUI

Field Summary

Fields

Modifier and Type

Field

Description

protected int

minTabWidth

The minimum width of a pane.

protected

Color

selectColor

The color of the selected pane.

protected

Color

selectHighlight

The color of the highlight.

protected

Color

tabAreaBackground

The color of tab's background.

- Fields declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

calcRect

,

contentBorderInsets

,

darkShadow

,

downKey

,

focus

,

focusListener

,

highlight

,

leftKey

,

lightHighlight

,

maxTabHeight

,

maxTabWidth

,

mouseListener

,

propertyChangeListener

,

rects

,

rightKey

,

runCount

,

selectedRun

,

selectedTabPadInsets

,

shadow

,

tabAreaInsets

,

tabChangeListener

,

tabInsets

,

tabPane

,

tabRunOverlay

,

tabRuns

,

textIconGap

,

upKey

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

The minimum width of a pane.

The color of the selected pane.

The color of the highlight.

The color of tab's background.

Fields declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

calcRect

,

contentBorderInsets

,

darkShadow

,

downKey

,

focus

,

focusListener

,

highlight

,

leftKey

,

lightHighlight

,

maxTabHeight

,

maxTabWidth

,

mouseListener

,

propertyChangeListener

,

rects

,

rightKey

,

runCount

,

selectedRun

,

selectedTabPadInsets

,

shadow

,

tabAreaInsets

,

tabChangeListener

,

tabInsets

,

tabPane

,

tabRunOverlay

,

tabRuns

,

textIconGap

,

upKey

---

#### Fields declared in class javax.swing.plaf.basic. BasicTabbedPaneUI

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

MetalTabbedPaneUI

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

Constructs

MetalTabbedPaneUI

.

protected int

getBaselineOffset

()

Returns the amount the baseline is offset by.

protected

Color

getColorForGap

​(int currentRun,
int x,
int y)

Returns the color of the gap.

protected int

getTabLabelShiftX

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

protected int

getTabLabelShiftY

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

protected void

paintBottomTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the bottom tab border.

protected void

paintHighlightBelowTab

()

Paints highlights below tab.

protected void

paintLeftTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the left tab border.

protected void

paintRightTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the right tab border.

protected void

paintTopTabBorder

​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the top tab border.

protected boolean

shouldFillGap

​(int currentRun,
int tabIndex,
int x,
int y)

Returns

true

if the gap should be filled.

protected boolean

shouldRotateTabRuns

​(int tabPlacement,
int selectedRun)

Returns

true

if tab runs should be rotated.

- Methods declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

assureRectsCreated

,

calculateMaxTabHeight

,

calculateMaxTabWidth

,

calculateTabAreaHeight

,

calculateTabAreaWidth

,

calculateTabHeight

,

calculateTabWidth

,

createChangeListener

,

createFocusListener

,

createLayoutManager

,

createMouseListener

,

createPropertyChangeListener

,

createScrollButton

,

expandTabRunsArray

,

getBaseline

,

getBaseline

,

getBaselineResizeBehavior

,

getContentBorderInsets

,

getFocusIndex

,

getFontMetrics

,

getIconForTab

,

getNextTabIndex

,

getNextTabIndexInRun

,

getNextTabRun

,

getPreviousTabIndex

,

getPreviousTabIndexInRun

,

getPreviousTabRun

,

getRolloverTab

,

getRunForTab

,

getSelectedTabPadInsets

,

getTabAreaInsets

,

getTabBounds

,

getTabBounds

,

getTabInsets

,

getTabRunIndent

,

getTabRunOffset

,

getTabRunOverlay

,

getTextViewForTab

,

getVisibleComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

lastTabInRun

,

layoutLabel

,

navigateSelectedTab

,

paintContentBorder

,

paintContentBorderBottomEdge

,

paintContentBorderLeftEdge

,

paintContentBorderRightEdge

,

paintContentBorderTopEdge

,

paintFocusIndicator

,

paintIcon

,

paintTab

,

paintTabArea

,

paintTabBackground

,

paintTabBorder

,

paintText

,

rotateInsets

,

selectAdjacentRunTab

,

selectNextTab

,

selectNextTabInRun

,

selectPreviousTab

,

selectPreviousTabInRun

,

setRolloverTab

,

setVisibleComponent

,

shouldPadTabRun

,

shouldRotateTabRuns

,

tabForCoordinate

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

- Methods declared in class javax.swing.plaf.

TabbedPaneUI

getTabRunCount

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

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

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

Constructs

MetalTabbedPaneUI

.

Returns the amount the baseline is offset by.

Returns the color of the gap.

Overridden to do nothing for the Java L&F.

Paints the bottom tab border.

Paints highlights below tab.

Paints the left tab border.

Paints the right tab border.

Paints the top tab border.

Returns

true

if the gap should be filled.

Returns

true

if tab runs should be rotated.

Methods declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

assureRectsCreated

,

calculateMaxTabHeight

,

calculateMaxTabWidth

,

calculateTabAreaHeight

,

calculateTabAreaWidth

,

calculateTabHeight

,

calculateTabWidth

,

createChangeListener

,

createFocusListener

,

createLayoutManager

,

createMouseListener

,

createPropertyChangeListener

,

createScrollButton

,

expandTabRunsArray

,

getBaseline

,

getBaseline

,

getBaselineResizeBehavior

,

getContentBorderInsets

,

getFocusIndex

,

getFontMetrics

,

getIconForTab

,

getNextTabIndex

,

getNextTabIndexInRun

,

getNextTabRun

,

getPreviousTabIndex

,

getPreviousTabIndexInRun

,

getPreviousTabRun

,

getRolloverTab

,

getRunForTab

,

getSelectedTabPadInsets

,

getTabAreaInsets

,

getTabBounds

,

getTabBounds

,

getTabInsets

,

getTabRunIndent

,

getTabRunOffset

,

getTabRunOverlay

,

getTextViewForTab

,

getVisibleComponent

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

lastTabInRun

,

layoutLabel

,

navigateSelectedTab

,

paintContentBorder

,

paintContentBorderBottomEdge

,

paintContentBorderLeftEdge

,

paintContentBorderRightEdge

,

paintContentBorderTopEdge

,

paintFocusIndicator

,

paintIcon

,

paintTab

,

paintTabArea

,

paintTabBackground

,

paintTabBorder

,

paintText

,

rotateInsets

,

selectAdjacentRunTab

,

selectNextTab

,

selectNextTabInRun

,

selectPreviousTab

,

selectPreviousTabInRun

,

setRolloverTab

,

setVisibleComponent

,

shouldPadTabRun

,

shouldRotateTabRuns

,

tabForCoordinate

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicTabbedPaneUI

Methods declared in class javax.swing.plaf.

TabbedPaneUI

getTabRunCount

---

#### Methods declared in class javax.swing.plaf. TabbedPaneUI

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

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

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

- minTabWidth

```java
protected int minTabWidth
```

The minimum width of a pane.

- tabAreaBackground

```java
protected
Color
tabAreaBackground
```

The color of tab's background.

- selectColor

```java
protected
Color
selectColor
```

The color of the selected pane.

- selectHighlight

```java
protected
Color
selectHighlight
```

The color of the highlight.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalTabbedPaneUI

```java
public MetalTabbedPaneUI()
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

Constructs

MetalTabbedPaneUI

.

**Parameters:** x

- a component
**Returns:** an instance of

MetalTabbedPaneUI

- paintTopTabBorder

```java
protected void paintTopTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the top tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- shouldFillGap

```java
protected boolean shouldFillGap​(int currentRun,
int tabIndex,
int x,
int y)
```

Returns

true

if the gap should be filled.

**Parameters:** currentRun

- the current run
**Parameters:** tabIndex

- the tab index
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** true

if the gap should be filled

- getColorForGap

```java
protected
Color
getColorForGap​(int currentRun,
int x,
int y)
```

Returns the color of the gap.

**Parameters:** currentRun

- the current run
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** the color of the gap

- paintLeftTabBorder

```java
protected void paintLeftTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the left tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- paintBottomTabBorder

```java
protected void paintBottomTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the bottom tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- paintRightTabBorder

```java
protected void paintRightTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the right tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftX

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift x

- getTabLabelShiftY

```java
protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftY

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift y

- getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Overrides:** getBaselineOffset

in class

BasicTabbedPaneUI
**Returns:** amount to offset the baseline by
**Since:** 1.6

- paintHighlightBelowTab

```java
protected void paintHighlightBelowTab()
```

Paints highlights below tab.

- shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement,
int selectedRun)
```

Returns

true

if tab runs should be rotated.

**Parameters:** tabPlacement

- a tab placement
**Parameters:** selectedRun

- a selected run
**Returns:** true

if tab runs should be rotated.

Field Detail

- minTabWidth

```java
protected int minTabWidth
```

The minimum width of a pane.

- tabAreaBackground

```java
protected
Color
tabAreaBackground
```

The color of tab's background.

- selectColor

```java
protected
Color
selectColor
```

The color of the selected pane.

- selectHighlight

```java
protected
Color
selectHighlight
```

The color of the highlight.

---

#### Field Detail

minTabWidth

```java
protected int minTabWidth
```

The minimum width of a pane.

---

#### minTabWidth

protected int minTabWidth

The minimum width of a pane.

tabAreaBackground

```java
protected
Color
tabAreaBackground
```

The color of tab's background.

---

#### tabAreaBackground

protected

Color

tabAreaBackground

The color of tab's background.

selectColor

```java
protected
Color
selectColor
```

The color of the selected pane.

---

#### selectColor

protected

Color

selectColor

The color of the selected pane.

selectHighlight

```java
protected
Color
selectHighlight
```

The color of the highlight.

---

#### selectHighlight

protected

Color

selectHighlight

The color of the highlight.

Constructor Detail

- MetalTabbedPaneUI

```java
public MetalTabbedPaneUI()
```

---

#### Constructor Detail

MetalTabbedPaneUI

```java
public MetalTabbedPaneUI()
```

---

#### MetalTabbedPaneUI

public MetalTabbedPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Constructs

MetalTabbedPaneUI

.

**Parameters:** x

- a component
**Returns:** an instance of

MetalTabbedPaneUI

- paintTopTabBorder

```java
protected void paintTopTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the top tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- shouldFillGap

```java
protected boolean shouldFillGap​(int currentRun,
int tabIndex,
int x,
int y)
```

Returns

true

if the gap should be filled.

**Parameters:** currentRun

- the current run
**Parameters:** tabIndex

- the tab index
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** true

if the gap should be filled

- getColorForGap

```java
protected
Color
getColorForGap​(int currentRun,
int x,
int y)
```

Returns the color of the gap.

**Parameters:** currentRun

- the current run
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** the color of the gap

- paintLeftTabBorder

```java
protected void paintLeftTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the left tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- paintBottomTabBorder

```java
protected void paintBottomTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the bottom tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- paintRightTabBorder

```java
protected void paintRightTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the right tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

- getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftX

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift x

- getTabLabelShiftY

```java
protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftY

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift y

- getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Overrides:** getBaselineOffset

in class

BasicTabbedPaneUI
**Returns:** amount to offset the baseline by
**Since:** 1.6

- paintHighlightBelowTab

```java
protected void paintHighlightBelowTab()
```

Paints highlights below tab.

- shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement,
int selectedRun)
```

Returns

true

if tab runs should be rotated.

**Parameters:** tabPlacement

- a tab placement
**Parameters:** selectedRun

- a selected run
**Returns:** true

if tab runs should be rotated.

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

Constructs

MetalTabbedPaneUI

.

**Parameters:** x

- a component
**Returns:** an instance of

MetalTabbedPaneUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs

MetalTabbedPaneUI

.

paintTopTabBorder

```java
protected void paintTopTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the top tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

---

#### paintTopTabBorder

protected void paintTopTabBorder​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the top tab border.

shouldFillGap

```java
protected boolean shouldFillGap​(int currentRun,
int tabIndex,
int x,
int y)
```

Returns

true

if the gap should be filled.

**Parameters:** currentRun

- the current run
**Parameters:** tabIndex

- the tab index
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** true

if the gap should be filled

---

#### shouldFillGap

protected boolean shouldFillGap​(int currentRun,
int tabIndex,
int x,
int y)

Returns

true

if the gap should be filled.

getColorForGap

```java
protected
Color
getColorForGap​(int currentRun,
int x,
int y)
```

Returns the color of the gap.

**Parameters:** currentRun

- the current run
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Returns:** the color of the gap

---

#### getColorForGap

protected

Color

getColorForGap​(int currentRun,
int x,
int y)

Returns the color of the gap.

paintLeftTabBorder

```java
protected void paintLeftTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the left tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

---

#### paintLeftTabBorder

protected void paintLeftTabBorder​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the left tab border.

paintBottomTabBorder

```java
protected void paintBottomTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the bottom tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

---

#### paintBottomTabBorder

protected void paintBottomTabBorder​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the bottom tab border.

paintRightTabBorder

```java
protected void paintRightTabBorder​(int tabIndex,

Graphics
g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)
```

Paints the right tab border.

**Parameters:** tabIndex

- a tab index
**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate
**Parameters:** w

- a width
**Parameters:** h

- a height
**Parameters:** btm

- bottom
**Parameters:** rght

- right
**Parameters:** isSelected

- a selection

---

#### paintRightTabBorder

protected void paintRightTabBorder​(int tabIndex,

Graphics

g,
int x,
int y,
int w,
int h,
int btm,
int rght,
boolean isSelected)

Paints the right tab border.

getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftX

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift x

---

#### getTabLabelShiftX

protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

getTabLabelShiftY

```java
protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Overridden to do nothing for the Java L&F.

**Overrides:** getTabLabelShiftY

in class

BasicTabbedPaneUI
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift y

---

#### getTabLabelShiftY

protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)

Overridden to do nothing for the Java L&F.

getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Overrides:** getBaselineOffset

in class

BasicTabbedPaneUI
**Returns:** amount to offset the baseline by
**Since:** 1.6

---

#### getBaselineOffset

protected int getBaselineOffset()

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

paintHighlightBelowTab

```java
protected void paintHighlightBelowTab()
```

Paints highlights below tab.

---

#### paintHighlightBelowTab

protected void paintHighlightBelowTab()

Paints highlights below tab.

shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement,
int selectedRun)
```

Returns

true

if tab runs should be rotated.

**Parameters:** tabPlacement

- a tab placement
**Parameters:** selectedRun

- a selected run
**Returns:** true

if tab runs should be rotated.

---

#### shouldRotateTabRuns

protected boolean shouldRotateTabRuns​(int tabPlacement,
int selectedRun)

Returns

true

if tab runs should be rotated.

---

