# Class BasicTabbedPaneUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTabbedPaneUI.html`

### Class Description

```java
public class
BasicTabbedPaneUI

extends
TabbedPaneUI

implements
SwingConstants
```

A Basic L&F implementation of TabbedPaneUI.

**All Implemented Interfaces:** SwingConstants

---

### Field Details

#### protected
JTabbedPane
tabPane

The tab pane

---

#### protected
Color
highlight

Highlight color

---

#### protected
Color
lightHighlight

Light highlight color

---

#### protected
Color
shadow

Shadow color

---

#### protected
Color
darkShadow

Dark shadow color

---

#### protected
Color
focus

Focus color

---

#### protected int textIconGap

Text icon gap

---

#### protected int tabRunOverlay

Tab run overlay

---

#### protected
Insets
tabInsets

Tab insets

---

#### protected
Insets
selectedTabPadInsets

Selected tab insets

---

#### protected
Insets
tabAreaInsets

Tab area insets

---

#### protected
Insets
contentBorderInsets

Content border insets

---

#### @Deprecated

protected
KeyStroke
upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### @Deprecated

protected
KeyStroke
rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### protected int[] tabRuns

Tab runs

---

#### protected int runCount

Run count

---

#### protected int selectedRun

Selected run

---

#### protected
Rectangle
[] rects

Tab rects

---

#### protected int maxTabHeight

Maximum tab height

---

#### protected int maxTabWidth

Maximum tab width

---

#### protected
ChangeListener
tabChangeListener

Tab change listener

---

#### protected
PropertyChangeListener
propertyChangeListener

Property change listener

---

#### protected
MouseListener
mouseListener

Mouse change listener

---

#### protected
FocusListener
focusListener

Focus change listener

---

#### protected transient
Rectangle
calcRect

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

---

### Constructor Details

#### public BasicTabbedPaneUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Create a UI.

**Parameters:**
- c

- a component

**Returns:**
- a UI

---

#### protected
LayoutManager
createLayoutManager()

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

**Returns:**
- a layout manager object

**See Also:**
- BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

---

#### protected void installComponents()

Creates and installs any required subcomponents for the JTabbedPane.
Invoked by installUI.

**Since:**
- 1.4

---

#### protected
JButton
createScrollButton​(int direction)

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction. The
returned JButton must be instance of UIResource.

**Parameters:**
- direction

- One of the SwingConstants constants:
SOUTH, NORTH, EAST or WEST

**Returns:**
- Widget for user to

**Throws:**
- IllegalArgumentException

- if direction is not one of
NORTH, SOUTH, EAST or WEST

**See Also:**
- JTabbedPane.setTabPlacement(int)

,

SwingConstants

**Since:**
- 1.5

---

#### protected void uninstallComponents()

Removes any installed subcomponents from the JTabbedPane.
Invoked by uninstallUI.

**Since:**
- 1.4

---

#### protected void installDefaults()

Install the defaults.

---

#### protected void uninstallDefaults()

Uninstall the defaults.

---

#### protected void installListeners()

Install the listeners.

---

#### protected void uninstallListeners()

Uninstall the listeners.

---

#### protected
MouseListener
createMouseListener()

Creates a mouse listener.

**Returns:**
- a mouse listener

---

#### protected
FocusListener
createFocusListener()

Creates a focus listener.

**Returns:**
- a focus listener

---

#### protected
ChangeListener
createChangeListener()

Creates a change listener.

**Returns:**
- a change listener

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a property change listener.

**Returns:**
- a property change listener

---

#### protected void installKeyboardActions()

Installs the keyboard actions.

---

#### protected void uninstallKeyboardActions()

Uninstalls the keyboard actions.

---

#### protected void setRolloverTab​(int index)

Sets the tab the mouse is currently over to

index

.

index

will be -1 if the mouse is no longer over any
tab. No checking is done to ensure the passed in index identifies a
valid tab.

**Parameters:**
- index

- Index of the tab the mouse is over.

**Since:**
- 1.5

---

#### protected int getRolloverTab()

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

**Returns:**
- the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab

**Since:**
- 1.5

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

#### protected int getBaseline​(int tab)

Returns the baseline for the specified tab.

**Parameters:**
- tab

- index of tab to get baseline for

**Returns:**
- baseline or a value < 0 indicating there is no reasonable
baseline

**Throws:**
- IndexOutOfBoundsException

- if index is out of range
(index < 0 || index >= tab count)

**Since:**
- 1.6

---

#### protected int getBaselineOffset()

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Returns:**
- amount to offset the baseline by

**Since:**
- 1.6

---

#### protected void paintTabArea​(
Graphics
g,
int tabPlacement,
int selectedIndex)

Paints the tabs in the tab area.
Invoked by paint().
The graphics parameter must be a valid

Graphics

object. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
The selected index must be a valid tabbed pane tab index (0 to
tab count - 1, inclusive) or -1 if no tab is currently selected.
The handling of invalid parameters is unspecified.

**Parameters:**
- g

- the graphics object to use for rendering
- tabPlacement

- the placement for the tabs within the JTabbedPane
- selectedIndex

- the tab index of the selected component

**Since:**
- 1.4

---

#### protected void paintTab​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect)

Paints a tab.

**Parameters:**
- g

- the graphics
- tabPlacement

- the tab placement
- rects

- rectangles
- tabIndex

- the tab index
- iconRect

- the icon rectangle
- textRect

- the text rectangle

---

#### protected void layoutLabel​(int tabPlacement,

FontMetrics
metrics,
int tabIndex,

String
title,

Icon
icon,

Rectangle
tabRect,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)

Laysout a label.

**Parameters:**
- tabPlacement

- the tab placement
- metrics

- the font metric
- tabIndex

- the tab index
- title

- the title
- icon

- the icon
- tabRect

- the tab rectangle
- iconRect

- the icon rectangle
- textRect

- the text rectangle
- isSelected

- selection status

---

#### protected void paintIcon​(
Graphics
g,
int tabPlacement,
int tabIndex,

Icon
icon,

Rectangle
iconRect,
boolean isSelected)

Paints an icon.

**Parameters:**
- g

- the graphics
- tabPlacement

- the tab placement
- tabIndex

- the tab index
- icon

- the icon
- iconRect

- the icon rectangle
- isSelected

- selection status

---

#### protected void paintText​(
Graphics
g,
int tabPlacement,

Font
font,

FontMetrics
metrics,
int tabIndex,

String
title,

Rectangle
textRect,
boolean isSelected)

Paints text.

**Parameters:**
- g

- the graphics
- tabPlacement

- the tab placement
- font

- the font
- metrics

- the font metrics
- tabIndex

- the tab index
- title

- the title
- textRect

- the text rectangle
- isSelected

- selection status

---

#### protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)

Returns the tab label shift x.

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

Returns the tab label shift y.

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

#### protected void paintFocusIndicator​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)

Paints the focus indicator.

**Parameters:**
- g

- the graphics
- tabPlacement

- the tab placement
- rects

- rectangles
- tabIndex

- the tab index
- iconRect

- the icon rectangle
- textRect

- the text rectangle
- isSelected

- selection status

---

#### protected void paintTabBorder​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

this function draws the border around each tab
note that this function does now draw the background of the tab.
that is done elsewhere

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the index of the tab with respect to other tabs
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab
- isSelected

- a

boolean

which determines whether or not
the tab is selected

---

#### protected void paintTabBackground​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

Paints the tab background.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the index of the tab with respect to other tabs
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab
- isSelected

- a

boolean

which determines whether or not
the tab is selected

---

#### protected void paintContentBorder​(
Graphics
g,
int tabPlacement,
int selectedIndex)

Paints the content border.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- selectedIndex

- the tab index of the selected component

---

#### protected void paintContentBorderTopEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border top edge.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- selectedIndex

- the tab index of the selected component
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab

---

#### protected void paintContentBorderLeftEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border left edge.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- selectedIndex

- the tab index of the selected component
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab

---

#### protected void paintContentBorderBottomEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border bottom edge.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- selectedIndex

- the tab index of the selected component
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab

---

#### protected void paintContentBorderRightEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border right edge.

**Parameters:**
- g

- the graphics context in which to paint
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- selectedIndex

- the tab index of the selected component
- x

- the x coordinate of tab
- y

- the y coordinate of tab
- w

- the width of the tab
- h

- the height of the tab

---

#### public
Rectangle
getTabBounds​(
JTabbedPane
pane,
int i)

Returns the bounds of the specified tab index. The bounds are
with respect to the JTabbedPane's coordinate space.

**Specified by:**
- getTabBounds

in class

TabbedPaneUI

**Parameters:**
- pane

- the pane
- i

- the index

**Returns:**
- the rectangle for the tab bounds

---

#### public int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

**Specified by:**
- tabForCoordinate

in class

TabbedPaneUI

**Parameters:**
- pane

- the pane
- x

- the x coordinate
- y

- the y coordinate

**Returns:**
- the tab for the coordinate

---

#### protected
Rectangle
getTabBounds​(int tabIndex,

Rectangle
dest)

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component. This is required because the tab rects
are by default defined in the coordinate space of the component where
they are rendered, which could be the JTabbedPane
(for WRAP_TAB_LAYOUT) or a ScrollableTabPanel (SCROLL_TAB_LAYOUT).
This method should be used whenever the tab rectangle must be relative
to the JTabbedPane itself and the result should be placed in a
designated Rectangle object (rather than instantiating and returning
a new Rectangle each time). The tab index parameter must be a valid
tabbed pane tab index (0 to tab count - 1, inclusive). The destination
rectangle parameter must be a valid

Rectangle

instance.
The handling of invalid parameters is unspecified.

**Parameters:**
- tabIndex

- the index of the tab
- dest

- the rectangle where the result should be placed

**Returns:**
- the resulting rectangle

**Since:**
- 1.4

---

#### protected
Component
getVisibleComponent()

Returns the visible component.

**Returns:**
- the visible component

---

#### protected void setVisibleComponent​(
Component
component)

Sets the visible component.

**Parameters:**
- component

- the component

---

#### protected void assureRectsCreated​(int tabCount)

Assure the rectangles are created.

**Parameters:**
- tabCount

- the tab count

---

#### protected void expandTabRunsArray()

Expands the tab runs array.

---

#### protected int getRunForTab​(int tabCount,
int tabIndex)

Returns the run for a tab.

**Parameters:**
- tabCount

- the tab count
- tabIndex

- the tab index.

**Returns:**
- the run for a tab

---

#### protected int lastTabInRun​(int tabCount,
int run)

Returns the last tab in a run.

**Parameters:**
- tabCount

- the tab count
- run

- the run

**Returns:**
- the last tab in a run

---

#### protected int getTabRunOverlay​(int tabPlacement)

Returns the tab run overlay.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the tab run overlay

---

#### protected int getTabRunIndent​(int tabPlacement,
int run)

Returns the tab run indent.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- run

- the tab run

**Returns:**
- the tab run indent

---

#### protected boolean shouldPadTabRun​(int tabPlacement,
int run)

Returns whether or not the tab run should be padded.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- run

- the tab run

**Returns:**
- whether or not the tab run should be padded

---

#### protected boolean shouldRotateTabRuns​(int tabPlacement)

Returns whether or not the tab run should be rotated.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- whether or not the tab run should be rotated

---

#### protected
Icon
getIconForTab​(int tabIndex)

Returns the icon for a tab.

**Parameters:**
- tabIndex

- the index of the tab

**Returns:**
- the icon for a tab

---

#### protected
View
getTextViewForTab​(int tabIndex)

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab. This is provided to support html rendering inside tabs.

**Parameters:**
- tabIndex

- the index of the tab

**Returns:**
- the text view to render the tab's text or null if no
specialized rendering is required

**Since:**
- 1.4

---

#### protected int calculateTabHeight​(int tabPlacement,
int tabIndex,
int fontHeight)

Calculates the tab height.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the index of the tab with respect to other tabs
- fontHeight

- the font height

**Returns:**
- the tab height

---

#### protected int calculateMaxTabHeight​(int tabPlacement)

Calculates the maximum tab height.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the maximum tab height

---

#### protected int calculateTabWidth​(int tabPlacement,
int tabIndex,

FontMetrics
metrics)

Calculates the tab width.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the index of the tab with respect to other tabs
- metrics

- the font metrics

**Returns:**
- the tab width

---

#### protected int calculateMaxTabWidth​(int tabPlacement)

Calculates the maximum tab width.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the maximum tab width

---

#### protected int calculateTabAreaHeight​(int tabPlacement,
int horizRunCount,
int maxTabHeight)

Calculates the tab area height.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- horizRunCount

- horizontal run count
- maxTabHeight

- maximum tab height

**Returns:**
- the tab area height

---

#### protected int calculateTabAreaWidth​(int tabPlacement,
int vertRunCount,
int maxTabWidth)

Calculates the tab area width.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- vertRunCount

- vertical run count
- maxTabWidth

- maximum tab width

**Returns:**
- the tab area width

---

#### protected
Insets
getTabInsets​(int tabPlacement,
int tabIndex)

Returns the tab insets.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the tab index

**Returns:**
- the tab insets

---

#### protected
Insets
getSelectedTabPadInsets​(int tabPlacement)

Returns the selected tab pad insets.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the selected tab pad insets

---

#### protected
Insets
getTabAreaInsets​(int tabPlacement)

Returns the tab area insets.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the pad area insets

---

#### protected
Insets
getContentBorderInsets​(int tabPlacement)

Returns the content border insets.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab

**Returns:**
- the content border insets

---

#### protected
FontMetrics
getFontMetrics()

Returns the font metrics.

**Returns:**
- the font metrics

---

#### protected void navigateSelectedTab​(int direction)

Navigate the selected tab.

**Parameters:**
- direction

- the direction

---

#### protected void selectNextTabInRun​(int current)

Select the next tab in the run.

**Parameters:**
- current

- the current tab

---

#### protected void selectPreviousTabInRun​(int current)

Select the previous tab in the run.

**Parameters:**
- current

- the current tab

---

#### protected void selectNextTab​(int current)

Select the next tab.

**Parameters:**
- current

- the current tab

---

#### protected void selectPreviousTab​(int current)

Select the previous tab.

**Parameters:**
- current

- the current tab

---

#### protected void selectAdjacentRunTab​(int tabPlacement,
int tabIndex,
int offset)

Selects an adjacent run of tabs.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabIndex

- the index of the tab with respect to other tabs
- offset

- selection offset

---

#### protected int getFocusIndex()

Returns the index of the tab that has focus.

**Returns:**
- index of tab that has focus

**Since:**
- 1.5

---

#### protected int getTabRunOffset​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)

Returns the tab run offset.

**Parameters:**
- tabPlacement

- the placement (left, right, bottom, top) of the tab
- tabCount

- the tab count
- tabIndex

- the index of the tab with respect to other tabs
- forward

- forward or not

**Returns:**
- the tab run offset

---

#### protected int getPreviousTabIndex​(int base)

Returns the previous tab index.

**Parameters:**
- base

- the base

**Returns:**
- the previous tab index

---

#### protected int getNextTabIndex​(int base)

Returns the next tab index.

**Parameters:**
- base

- the base

**Returns:**
- the next tab index

---

#### protected int getNextTabIndexInRun​(int tabCount,
int base)

Returns the next tab index in the run.

**Parameters:**
- tabCount

- the tab count
- base

- the base

**Returns:**
- the next tab index in the run

---

#### protected int getPreviousTabIndexInRun​(int tabCount,
int base)

Returns the previous tab index in the run.

**Parameters:**
- tabCount

- the tab count
- base

- the base

**Returns:**
- the previous tab index in the run

---

#### protected int getPreviousTabRun​(int baseRun)

Returns the previous tab run.

**Parameters:**
- baseRun

- the base run

**Returns:**
- the previous tab run

---

#### protected int getNextTabRun​(int baseRun)

Returns the next tab run.

**Parameters:**
- baseRun

- the base run

**Returns:**
- the next tab run

---

#### protected static void rotateInsets​(
Insets
topInsets,

Insets
targetInsets,
int targetPlacement)

Rotates the insets.

**Parameters:**
- topInsets

- the top insets
- targetInsets

- the target insets
- targetPlacement

- the target placement

---

### Additional Sections

#### Class BasicTabbedPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI

javax.swing.plaf.TabbedPaneUI

- javax.swing.plaf.basic.BasicTabbedPaneUI

javax.swing.plaf.basic.BasicTabbedPaneUI

**All Implemented Interfaces:** SwingConstants

**Direct Known Subclasses:** MetalTabbedPaneUI

,

SynthTabbedPaneUI

```java
public class
BasicTabbedPaneUI

extends
TabbedPaneUI

implements
SwingConstants
```

A Basic L&F implementation of TabbedPaneUI.

public class

BasicTabbedPaneUI

extends

TabbedPaneUI

implements

SwingConstants

A Basic L&F implementation of TabbedPaneUI.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicTabbedPaneUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.MouseHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.PropertyChangeHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.TabbedPaneLayout

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.TabSelectionHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Rectangle

calcRect

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

protected

Insets

contentBorderInsets

Content border insets

protected

Color

darkShadow

Dark shadow color

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected

Color

focus

Focus color

protected

FocusListener

focusListener

Focus change listener

protected

Color

highlight

Highlight color

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected

Color

lightHighlight

Light highlight color

protected int

maxTabHeight

Maximum tab height

protected int

maxTabWidth

Maximum tab width

protected

MouseListener

mouseListener

Mouse change listener

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

Rectangle

[]

rects

Tab rects

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected int

runCount

Run count

protected int

selectedRun

Selected run

protected

Insets

selectedTabPadInsets

Selected tab insets

protected

Color

shadow

Shadow color

protected

Insets

tabAreaInsets

Tab area insets

protected

ChangeListener

tabChangeListener

Tab change listener

protected

Insets

tabInsets

Tab insets

protected

JTabbedPane

tabPane

The tab pane

protected int

tabRunOverlay

Tab run overlay

protected int[]

tabRuns

Tab runs

protected int

textIconGap

Text icon gap

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

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

BasicTabbedPaneUI

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

assureRectsCreated

​(int tabCount)

Assure the rectangles are created.

protected int

calculateMaxTabHeight

​(int tabPlacement)

Calculates the maximum tab height.

protected int

calculateMaxTabWidth

​(int tabPlacement)

Calculates the maximum tab width.

protected int

calculateTabAreaHeight

​(int tabPlacement,
int horizRunCount,
int maxTabHeight)

Calculates the tab area height.

protected int

calculateTabAreaWidth

​(int tabPlacement,
int vertRunCount,
int maxTabWidth)

Calculates the tab area width.

protected int

calculateTabHeight

​(int tabPlacement,
int tabIndex,
int fontHeight)

Calculates the tab height.

protected int

calculateTabWidth

​(int tabPlacement,
int tabIndex,

FontMetrics

metrics)

Calculates the tab width.

protected

ChangeListener

createChangeListener

()

Creates a change listener.

protected

FocusListener

createFocusListener

()

Creates a focus listener.

protected

LayoutManager

createLayoutManager

()

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

protected

MouseListener

createMouseListener

()

Creates a mouse listener.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a property change listener.

protected

JButton

createScrollButton

​(int direction)

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction.

static

ComponentUI

createUI

​(

JComponent

c)

Create a UI.

protected void

expandTabRunsArray

()

Expands the tab runs array.

protected int

getBaseline

​(int tab)

Returns the baseline for the specified tab.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

protected int

getBaselineOffset

()

Returns the amount the baseline is offset by.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Insets

getContentBorderInsets

​(int tabPlacement)

Returns the content border insets.

protected int

getFocusIndex

()

Returns the index of the tab that has focus.

protected

FontMetrics

getFontMetrics

()

Returns the font metrics.

protected

Icon

getIconForTab

​(int tabIndex)

Returns the icon for a tab.

protected int

getNextTabIndex

​(int base)

Returns the next tab index.

protected int

getNextTabIndexInRun

​(int tabCount,
int base)

Returns the next tab index in the run.

protected int

getNextTabRun

​(int baseRun)

Returns the next tab run.

protected int

getPreviousTabIndex

​(int base)

Returns the previous tab index.

protected int

getPreviousTabIndexInRun

​(int tabCount,
int base)

Returns the previous tab index in the run.

protected int

getPreviousTabRun

​(int baseRun)

Returns the previous tab run.

protected int

getRolloverTab

()

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

protected int

getRunForTab

​(int tabCount,
int tabIndex)

Returns the run for a tab.

protected

Insets

getSelectedTabPadInsets

​(int tabPlacement)

Returns the selected tab pad insets.

protected

Insets

getTabAreaInsets

​(int tabPlacement)

Returns the tab area insets.

protected

Rectangle

getTabBounds

​(int tabIndex,

Rectangle

dest)

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component.

Rectangle

getTabBounds

​(

JTabbedPane

pane,
int i)

Returns the bounds of the specified tab index.

protected

Insets

getTabInsets

​(int tabPlacement,
int tabIndex)

Returns the tab insets.

protected int

getTabLabelShiftX

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Returns the tab label shift x.

protected int

getTabLabelShiftY

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Returns the tab label shift y.

protected int

getTabRunIndent

​(int tabPlacement,
int run)

Returns the tab run indent.

protected int

getTabRunOffset

​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)

Returns the tab run offset.

protected int

getTabRunOverlay

​(int tabPlacement)

Returns the tab run overlay.

protected

View

getTextViewForTab

​(int tabIndex)

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab.

protected

Component

getVisibleComponent

()

Returns the visible component.

protected void

installComponents

()

Creates and installs any required subcomponents for the JTabbedPane.

protected void

installDefaults

()

Install the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Install the listeners.

protected int

lastTabInRun

​(int tabCount,
int run)

Returns the last tab in a run.

protected void

layoutLabel

​(int tabPlacement,

FontMetrics

metrics,
int tabIndex,

String

title,

Icon

icon,

Rectangle

tabRect,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Laysout a label.

protected void

navigateSelectedTab

​(int direction)

Navigate the selected tab.

protected void

paintContentBorder

​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the content border.

protected void

paintContentBorderBottomEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border bottom edge.

protected void

paintContentBorderLeftEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border left edge.

protected void

paintContentBorderRightEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border right edge.

protected void

paintContentBorderTopEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border top edge.

protected void

paintFocusIndicator

​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Paints the focus indicator.

protected void

paintIcon

​(

Graphics

g,
int tabPlacement,
int tabIndex,

Icon

icon,

Rectangle

iconRect,
boolean isSelected)

Paints an icon.

protected void

paintTab

​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect)

Paints a tab.

protected void

paintTabArea

​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the tabs in the tab area.

protected void

paintTabBackground

​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

Paints the tab background.

protected void

paintTabBorder

​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

this function draws the border around each tab
note that this function does now draw the background of the tab.

protected void

paintText

​(

Graphics

g,
int tabPlacement,

Font

font,

FontMetrics

metrics,
int tabIndex,

String

title,

Rectangle

textRect,
boolean isSelected)

Paints text.

protected static void

rotateInsets

​(

Insets

topInsets,

Insets

targetInsets,
int targetPlacement)

Rotates the insets.

protected void

selectAdjacentRunTab

​(int tabPlacement,
int tabIndex,
int offset)

Selects an adjacent run of tabs.

protected void

selectNextTab

​(int current)

Select the next tab.

protected void

selectNextTabInRun

​(int current)

Select the next tab in the run.

protected void

selectPreviousTab

​(int current)

Select the previous tab.

protected void

selectPreviousTabInRun

​(int current)

Select the previous tab in the run.

protected void

setRolloverTab

​(int index)

Sets the tab the mouse is currently over to

index

.

protected void

setVisibleComponent

​(

Component

component)

Sets the visible component.

protected boolean

shouldPadTabRun

​(int tabPlacement,
int run)

Returns whether or not the tab run should be padded.

protected boolean

shouldRotateTabRuns

​(int tabPlacement)

Returns whether or not the tab run should be rotated.

int

tabForCoordinate

​(

JTabbedPane

pane,
int x,
int y)

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

protected void

uninstallComponents

()

Removes any installed subcomponents from the JTabbedPane.

protected void

uninstallDefaults

()

Uninstall the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstall the listeners.

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

BasicTabbedPaneUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.MouseHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.PropertyChangeHandler

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.TabbedPaneLayout

This class should be treated as a "protected" inner class.

class

BasicTabbedPaneUI.TabSelectionHandler

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

calcRect

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

protected

Insets

contentBorderInsets

Content border insets

protected

Color

darkShadow

Dark shadow color

protected

KeyStroke

downKey

Deprecated.

As of Java 2 platform v1.3.

protected

Color

focus

Focus color

protected

FocusListener

focusListener

Focus change listener

protected

Color

highlight

Highlight color

protected

KeyStroke

leftKey

Deprecated.

As of Java 2 platform v1.3.

protected

Color

lightHighlight

Light highlight color

protected int

maxTabHeight

Maximum tab height

protected int

maxTabWidth

Maximum tab width

protected

MouseListener

mouseListener

Mouse change listener

protected

PropertyChangeListener

propertyChangeListener

Property change listener

protected

Rectangle

[]

rects

Tab rects

protected

KeyStroke

rightKey

Deprecated.

As of Java 2 platform v1.3.

protected int

runCount

Run count

protected int

selectedRun

Selected run

protected

Insets

selectedTabPadInsets

Selected tab insets

protected

Color

shadow

Shadow color

protected

Insets

tabAreaInsets

Tab area insets

protected

ChangeListener

tabChangeListener

Tab change listener

protected

Insets

tabInsets

Tab insets

protected

JTabbedPane

tabPane

The tab pane

protected int

tabRunOverlay

Tab run overlay

protected int[]

tabRuns

Tab runs

protected int

textIconGap

Text icon gap

protected

KeyStroke

upKey

Deprecated.

As of Java 2 platform v1.3.

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

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

Content border insets

Dark shadow color

Deprecated.

As of Java 2 platform v1.3.

Focus color

Focus change listener

Highlight color

Light highlight color

Maximum tab height

Maximum tab width

Mouse change listener

Property change listener

Tab rects

Run count

Selected run

Selected tab insets

Shadow color

Tab area insets

Tab change listener

Tab insets

The tab pane

Tab run overlay

Tab runs

Text icon gap

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

BasicTabbedPaneUI

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

assureRectsCreated

​(int tabCount)

Assure the rectangles are created.

protected int

calculateMaxTabHeight

​(int tabPlacement)

Calculates the maximum tab height.

protected int

calculateMaxTabWidth

​(int tabPlacement)

Calculates the maximum tab width.

protected int

calculateTabAreaHeight

​(int tabPlacement,
int horizRunCount,
int maxTabHeight)

Calculates the tab area height.

protected int

calculateTabAreaWidth

​(int tabPlacement,
int vertRunCount,
int maxTabWidth)

Calculates the tab area width.

protected int

calculateTabHeight

​(int tabPlacement,
int tabIndex,
int fontHeight)

Calculates the tab height.

protected int

calculateTabWidth

​(int tabPlacement,
int tabIndex,

FontMetrics

metrics)

Calculates the tab width.

protected

ChangeListener

createChangeListener

()

Creates a change listener.

protected

FocusListener

createFocusListener

()

Creates a focus listener.

protected

LayoutManager

createLayoutManager

()

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

protected

MouseListener

createMouseListener

()

Creates a mouse listener.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a property change listener.

protected

JButton

createScrollButton

​(int direction)

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction.

static

ComponentUI

createUI

​(

JComponent

c)

Create a UI.

protected void

expandTabRunsArray

()

Expands the tab runs array.

protected int

getBaseline

​(int tab)

Returns the baseline for the specified tab.

int

getBaseline

​(

JComponent

c,
int width,
int height)

Returns the baseline.

protected int

getBaselineOffset

()

Returns the amount the baseline is offset by.

Component.BaselineResizeBehavior

getBaselineResizeBehavior

​(

JComponent

c)

Returns an enum indicating how the baseline of the component
changes as the size changes.

protected

Insets

getContentBorderInsets

​(int tabPlacement)

Returns the content border insets.

protected int

getFocusIndex

()

Returns the index of the tab that has focus.

protected

FontMetrics

getFontMetrics

()

Returns the font metrics.

protected

Icon

getIconForTab

​(int tabIndex)

Returns the icon for a tab.

protected int

getNextTabIndex

​(int base)

Returns the next tab index.

protected int

getNextTabIndexInRun

​(int tabCount,
int base)

Returns the next tab index in the run.

protected int

getNextTabRun

​(int baseRun)

Returns the next tab run.

protected int

getPreviousTabIndex

​(int base)

Returns the previous tab index.

protected int

getPreviousTabIndexInRun

​(int tabCount,
int base)

Returns the previous tab index in the run.

protected int

getPreviousTabRun

​(int baseRun)

Returns the previous tab run.

protected int

getRolloverTab

()

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

protected int

getRunForTab

​(int tabCount,
int tabIndex)

Returns the run for a tab.

protected

Insets

getSelectedTabPadInsets

​(int tabPlacement)

Returns the selected tab pad insets.

protected

Insets

getTabAreaInsets

​(int tabPlacement)

Returns the tab area insets.

protected

Rectangle

getTabBounds

​(int tabIndex,

Rectangle

dest)

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component.

Rectangle

getTabBounds

​(

JTabbedPane

pane,
int i)

Returns the bounds of the specified tab index.

protected

Insets

getTabInsets

​(int tabPlacement,
int tabIndex)

Returns the tab insets.

protected int

getTabLabelShiftX

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Returns the tab label shift x.

protected int

getTabLabelShiftY

​(int tabPlacement,
int tabIndex,
boolean isSelected)

Returns the tab label shift y.

protected int

getTabRunIndent

​(int tabPlacement,
int run)

Returns the tab run indent.

protected int

getTabRunOffset

​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)

Returns the tab run offset.

protected int

getTabRunOverlay

​(int tabPlacement)

Returns the tab run overlay.

protected

View

getTextViewForTab

​(int tabIndex)

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab.

protected

Component

getVisibleComponent

()

Returns the visible component.

protected void

installComponents

()

Creates and installs any required subcomponents for the JTabbedPane.

protected void

installDefaults

()

Install the defaults.

protected void

installKeyboardActions

()

Installs the keyboard actions.

protected void

installListeners

()

Install the listeners.

protected int

lastTabInRun

​(int tabCount,
int run)

Returns the last tab in a run.

protected void

layoutLabel

​(int tabPlacement,

FontMetrics

metrics,
int tabIndex,

String

title,

Icon

icon,

Rectangle

tabRect,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Laysout a label.

protected void

navigateSelectedTab

​(int direction)

Navigate the selected tab.

protected void

paintContentBorder

​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the content border.

protected void

paintContentBorderBottomEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border bottom edge.

protected void

paintContentBorderLeftEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border left edge.

protected void

paintContentBorderRightEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border right edge.

protected void

paintContentBorderTopEdge

​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border top edge.

protected void

paintFocusIndicator

​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Paints the focus indicator.

protected void

paintIcon

​(

Graphics

g,
int tabPlacement,
int tabIndex,

Icon

icon,

Rectangle

iconRect,
boolean isSelected)

Paints an icon.

protected void

paintTab

​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect)

Paints a tab.

protected void

paintTabArea

​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the tabs in the tab area.

protected void

paintTabBackground

​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

Paints the tab background.

protected void

paintTabBorder

​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

this function draws the border around each tab
note that this function does now draw the background of the tab.

protected void

paintText

​(

Graphics

g,
int tabPlacement,

Font

font,

FontMetrics

metrics,
int tabIndex,

String

title,

Rectangle

textRect,
boolean isSelected)

Paints text.

protected static void

rotateInsets

​(

Insets

topInsets,

Insets

targetInsets,
int targetPlacement)

Rotates the insets.

protected void

selectAdjacentRunTab

​(int tabPlacement,
int tabIndex,
int offset)

Selects an adjacent run of tabs.

protected void

selectNextTab

​(int current)

Select the next tab.

protected void

selectNextTabInRun

​(int current)

Select the next tab in the run.

protected void

selectPreviousTab

​(int current)

Select the previous tab.

protected void

selectPreviousTabInRun

​(int current)

Select the previous tab in the run.

protected void

setRolloverTab

​(int index)

Sets the tab the mouse is currently over to

index

.

protected void

setVisibleComponent

​(

Component

component)

Sets the visible component.

protected boolean

shouldPadTabRun

​(int tabPlacement,
int run)

Returns whether or not the tab run should be padded.

protected boolean

shouldRotateTabRuns

​(int tabPlacement)

Returns whether or not the tab run should be rotated.

int

tabForCoordinate

​(

JTabbedPane

pane,
int x,
int y)

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

protected void

uninstallComponents

()

Removes any installed subcomponents from the JTabbedPane.

protected void

uninstallDefaults

()

Uninstall the defaults.

protected void

uninstallKeyboardActions

()

Uninstalls the keyboard actions.

protected void

uninstallListeners

()

Uninstall the listeners.

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

Assure the rectangles are created.

Calculates the maximum tab height.

Calculates the maximum tab width.

Calculates the tab area height.

Calculates the tab area width.

Calculates the tab height.

Calculates the tab width.

Creates a change listener.

Creates a focus listener.

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

Creates a mouse listener.

Creates a property change listener.

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction.

Create a UI.

Expands the tab runs array.

Returns the baseline for the specified tab.

Returns the baseline.

Returns the amount the baseline is offset by.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns the content border insets.

Returns the index of the tab that has focus.

Returns the font metrics.

Returns the icon for a tab.

Returns the next tab index.

Returns the next tab index in the run.

Returns the next tab run.

Returns the previous tab index.

Returns the previous tab index in the run.

Returns the previous tab run.

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

Returns the run for a tab.

Returns the selected tab pad insets.

Returns the tab area insets.

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component.

Returns the bounds of the specified tab index.

Returns the tab insets.

Returns the tab label shift x.

Returns the tab label shift y.

Returns the tab run indent.

Returns the tab run offset.

Returns the tab run overlay.

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab.

Returns the visible component.

Creates and installs any required subcomponents for the JTabbedPane.

Install the defaults.

Installs the keyboard actions.

Install the listeners.

Returns the last tab in a run.

Laysout a label.

Navigate the selected tab.

Paints the content border.

Paints the content border bottom edge.

Paints the content border left edge.

Paints the content border right edge.

Paints the content border top edge.

Paints the focus indicator.

Paints an icon.

Paints a tab.

Paints the tabs in the tab area.

Paints the tab background.

this function draws the border around each tab
note that this function does now draw the background of the tab.

Paints text.

Rotates the insets.

Selects an adjacent run of tabs.

Select the next tab.

Select the next tab in the run.

Select the previous tab.

Select the previous tab in the run.

Sets the tab the mouse is currently over to

index

.

Sets the visible component.

Returns whether or not the tab run should be padded.

Returns whether or not the tab run should be rotated.

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

Removes any installed subcomponents from the JTabbedPane.

Uninstall the defaults.

Uninstalls the keyboard actions.

Uninstall the listeners.

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

- tabPane

```java
protected
JTabbedPane
tabPane
```

The tab pane

- highlight

```java
protected
Color
highlight
```

Highlight color

- lightHighlight

```java
protected
Color
lightHighlight
```

Light highlight color

- shadow

```java
protected
Color
shadow
```

Shadow color

- darkShadow

```java
protected
Color
darkShadow
```

Dark shadow color

- focus

```java
protected
Color
focus
```

Focus color

- textIconGap

```java
protected int textIconGap
```

Text icon gap

- tabRunOverlay

```java
protected int tabRunOverlay
```

Tab run overlay

- tabInsets

```java
protected
Insets
tabInsets
```

Tab insets

- selectedTabPadInsets

```java
protected
Insets
selectedTabPadInsets
```

Selected tab insets

- tabAreaInsets

```java
protected
Insets
tabAreaInsets
```

Tab area insets

- contentBorderInsets

```java
protected
Insets
contentBorderInsets
```

Content border insets

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- tabRuns

```java
protected int[] tabRuns
```

Tab runs

- runCount

```java
protected int runCount
```

Run count

- selectedRun

```java
protected int selectedRun
```

Selected run

- rects

```java
protected
Rectangle
[] rects
```

Tab rects

- maxTabHeight

```java
protected int maxTabHeight
```

Maximum tab height

- maxTabWidth

```java
protected int maxTabWidth
```

Maximum tab width

- tabChangeListener

```java
protected
ChangeListener
tabChangeListener
```

Tab change listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- mouseListener

```java
protected
MouseListener
mouseListener
```

Mouse change listener

- focusListener

```java
protected
FocusListener
focusListener
```

Focus change listener

- calcRect

```java
protected transient
Rectangle
calcRect
```

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicTabbedPaneUI

```java
public BasicTabbedPaneUI()
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

Create a UI.

**Parameters:** c

- a component
**Returns:** a UI

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

**Returns:** a layout manager object
**See Also:** BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

- installComponents

```java
protected void installComponents()
```

Creates and installs any required subcomponents for the JTabbedPane.
Invoked by installUI.

**Since:** 1.4

- createScrollButton

```java
protected
JButton
createScrollButton​(int direction)
```

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction. The
returned JButton must be instance of UIResource.

**Parameters:** direction

- One of the SwingConstants constants:
SOUTH, NORTH, EAST or WEST
**Returns:** Widget for user to
**Throws:** IllegalArgumentException

- if direction is not one of
NORTH, SOUTH, EAST or WEST
**Since:** 1.5
**See Also:** JTabbedPane.setTabPlacement(int)

,

SwingConstants

- uninstallComponents

```java
protected void uninstallComponents()
```

Removes any installed subcomponents from the JTabbedPane.
Invoked by uninstallUI.

**Since:** 1.4

- installDefaults

```java
protected void installDefaults()
```

Install the defaults.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstall the defaults.

- installListeners

```java
protected void installListeners()
```

Install the listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

**Returns:** a mouse listener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a focus listener.

**Returns:** a focus listener

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Creates a change listener.

**Returns:** a change listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a property change listener.

**Returns:** a property change listener

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

- setRolloverTab

```java
protected void setRolloverTab​(int index)
```

Sets the tab the mouse is currently over to

index

.

index

will be -1 if the mouse is no longer over any
tab. No checking is done to ensure the passed in index identifies a
valid tab.

**Parameters:** index

- Index of the tab the mouse is over.
**Since:** 1.5

- getRolloverTab

```java
protected int getRolloverTab()
```

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

**Returns:** the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab
**Since:** 1.5

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

- getBaseline

```java
protected int getBaseline​(int tab)
```

Returns the baseline for the specified tab.

**Parameters:** tab

- index of tab to get baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IndexOutOfBoundsException

- if index is out of range
(index < 0 || index >= tab count)
**Since:** 1.6

- getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Returns:** amount to offset the baseline by
**Since:** 1.6

- paintTabArea

```java
protected void paintTabArea​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the tabs in the tab area.
Invoked by paint().
The graphics parameter must be a valid

Graphics

object. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
The selected index must be a valid tabbed pane tab index (0 to
tab count - 1, inclusive) or -1 if no tab is currently selected.
The handling of invalid parameters is unspecified.

**Parameters:** g

- the graphics object to use for rendering
**Parameters:** tabPlacement

- the placement for the tabs within the JTabbedPane
**Parameters:** selectedIndex

- the tab index of the selected component
**Since:** 1.4

- paintTab

```java
protected void paintTab​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect)
```

Paints a tab.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle

- layoutLabel

```java
protected void layoutLabel​(int tabPlacement,

FontMetrics
metrics,
int tabIndex,

String
title,

Icon
icon,

Rectangle
tabRect,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Laysout a label.

**Parameters:** tabPlacement

- the tab placement
**Parameters:** metrics

- the font metric
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** icon

- the icon
**Parameters:** tabRect

- the tab rectangle
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- paintIcon

```java
protected void paintIcon​(
Graphics
g,
int tabPlacement,
int tabIndex,

Icon
icon,

Rectangle
iconRect,
boolean isSelected)
```

Paints an icon.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** icon

- the icon
**Parameters:** iconRect

- the icon rectangle
**Parameters:** isSelected

- selection status

- paintText

```java
protected void paintText​(
Graphics
g,
int tabPlacement,

Font
font,

FontMetrics
metrics,
int tabIndex,

String
title,

Rectangle
textRect,
boolean isSelected)
```

Paints text.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** font

- the font
**Parameters:** metrics

- the font metrics
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Returns the tab label shift x.

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

Returns the tab label shift y.

**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift y

- paintFocusIndicator

```java
protected void paintFocusIndicator​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Paints the focus indicator.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- paintTabBorder

```java
protected void paintTabBorder​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

this function draws the border around each tab
note that this function does now draw the background of the tab.
that is done elsewhere

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

- paintTabBackground

```java
protected void paintTabBackground​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

Paints the tab background.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

- paintContentBorder

```java
protected void paintContentBorder​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the content border.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component

- paintContentBorderTopEdge

```java
protected void paintContentBorderTopEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border top edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderLeftEdge

```java
protected void paintContentBorderLeftEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border left edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderBottomEdge

```java
protected void paintContentBorderBottomEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border bottom edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderRightEdge

```java
protected void paintContentBorderRightEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border right edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- getTabBounds

```java
public
Rectangle
getTabBounds​(
JTabbedPane
pane,
int i)
```

Returns the bounds of the specified tab index. The bounds are
with respect to the JTabbedPane's coordinate space.

**Specified by:** getTabBounds

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** i

- the index
**Returns:** the rectangle for the tab bounds

- tabForCoordinate

```java
public int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

**Specified by:** tabForCoordinate

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

- getTabBounds

```java
protected
Rectangle
getTabBounds​(int tabIndex,

Rectangle
dest)
```

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component. This is required because the tab rects
are by default defined in the coordinate space of the component where
they are rendered, which could be the JTabbedPane
(for WRAP_TAB_LAYOUT) or a ScrollableTabPanel (SCROLL_TAB_LAYOUT).
This method should be used whenever the tab rectangle must be relative
to the JTabbedPane itself and the result should be placed in a
designated Rectangle object (rather than instantiating and returning
a new Rectangle each time). The tab index parameter must be a valid
tabbed pane tab index (0 to tab count - 1, inclusive). The destination
rectangle parameter must be a valid

Rectangle

instance.
The handling of invalid parameters is unspecified.

**Parameters:** tabIndex

- the index of the tab
**Parameters:** dest

- the rectangle where the result should be placed
**Returns:** the resulting rectangle
**Since:** 1.4

- getVisibleComponent

```java
protected
Component
getVisibleComponent()
```

Returns the visible component.

**Returns:** the visible component

- setVisibleComponent

```java
protected void setVisibleComponent​(
Component
component)
```

Sets the visible component.

**Parameters:** component

- the component

- assureRectsCreated

```java
protected void assureRectsCreated​(int tabCount)
```

Assure the rectangles are created.

**Parameters:** tabCount

- the tab count

- expandTabRunsArray

```java
protected void expandTabRunsArray()
```

Expands the tab runs array.

- getRunForTab

```java
protected int getRunForTab​(int tabCount,
int tabIndex)
```

Returns the run for a tab.

**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the tab index.
**Returns:** the run for a tab

- lastTabInRun

```java
protected int lastTabInRun​(int tabCount,
int run)
```

Returns the last tab in a run.

**Parameters:** tabCount

- the tab count
**Parameters:** run

- the run
**Returns:** the last tab in a run

- getTabRunOverlay

```java
protected int getTabRunOverlay​(int tabPlacement)
```

Returns the tab run overlay.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the tab run overlay

- getTabRunIndent

```java
protected int getTabRunIndent​(int tabPlacement,
int run)
```

Returns the tab run indent.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** the tab run indent

- shouldPadTabRun

```java
protected boolean shouldPadTabRun​(int tabPlacement,
int run)
```

Returns whether or not the tab run should be padded.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** whether or not the tab run should be padded

- shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement)
```

Returns whether or not the tab run should be rotated.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** whether or not the tab run should be rotated

- getIconForTab

```java
protected
Icon
getIconForTab​(int tabIndex)
```

Returns the icon for a tab.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the icon for a tab

- getTextViewForTab

```java
protected
View
getTextViewForTab​(int tabIndex)
```

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab. This is provided to support html rendering inside tabs.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the text view to render the tab's text or null if no
specialized rendering is required
**Since:** 1.4

- calculateTabHeight

```java
protected int calculateTabHeight​(int tabPlacement,
int tabIndex,
int fontHeight)
```

Calculates the tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** fontHeight

- the font height
**Returns:** the tab height

- calculateMaxTabHeight

```java
protected int calculateMaxTabHeight​(int tabPlacement)
```

Calculates the maximum tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab height

- calculateTabWidth

```java
protected int calculateTabWidth​(int tabPlacement,
int tabIndex,

FontMetrics
metrics)
```

Calculates the tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** metrics

- the font metrics
**Returns:** the tab width

- calculateMaxTabWidth

```java
protected int calculateMaxTabWidth​(int tabPlacement)
```

Calculates the maximum tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab width

- calculateTabAreaHeight

```java
protected int calculateTabAreaHeight​(int tabPlacement,
int horizRunCount,
int maxTabHeight)
```

Calculates the tab area height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** horizRunCount

- horizontal run count
**Parameters:** maxTabHeight

- maximum tab height
**Returns:** the tab area height

- calculateTabAreaWidth

```java
protected int calculateTabAreaWidth​(int tabPlacement,
int vertRunCount,
int maxTabWidth)
```

Calculates the tab area width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** vertRunCount

- vertical run count
**Parameters:** maxTabWidth

- maximum tab width
**Returns:** the tab area width

- getTabInsets

```java
protected
Insets
getTabInsets​(int tabPlacement,
int tabIndex)
```

Returns the tab insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the tab index
**Returns:** the tab insets

- getSelectedTabPadInsets

```java
protected
Insets
getSelectedTabPadInsets​(int tabPlacement)
```

Returns the selected tab pad insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the selected tab pad insets

- getTabAreaInsets

```java
protected
Insets
getTabAreaInsets​(int tabPlacement)
```

Returns the tab area insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the pad area insets

- getContentBorderInsets

```java
protected
Insets
getContentBorderInsets​(int tabPlacement)
```

Returns the content border insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the content border insets

- getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Returns the font metrics.

**Returns:** the font metrics

- navigateSelectedTab

```java
protected void navigateSelectedTab​(int direction)
```

Navigate the selected tab.

**Parameters:** direction

- the direction

- selectNextTabInRun

```java
protected void selectNextTabInRun​(int current)
```

Select the next tab in the run.

**Parameters:** current

- the current tab

- selectPreviousTabInRun

```java
protected void selectPreviousTabInRun​(int current)
```

Select the previous tab in the run.

**Parameters:** current

- the current tab

- selectNextTab

```java
protected void selectNextTab​(int current)
```

Select the next tab.

**Parameters:** current

- the current tab

- selectPreviousTab

```java
protected void selectPreviousTab​(int current)
```

Select the previous tab.

**Parameters:** current

- the current tab

- selectAdjacentRunTab

```java
protected void selectAdjacentRunTab​(int tabPlacement,
int tabIndex,
int offset)
```

Selects an adjacent run of tabs.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** offset

- selection offset

- getFocusIndex

```java
protected int getFocusIndex()
```

Returns the index of the tab that has focus.

**Returns:** index of tab that has focus
**Since:** 1.5

- getTabRunOffset

```java
protected int getTabRunOffset​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)
```

Returns the tab run offset.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** forward

- forward or not
**Returns:** the tab run offset

- getPreviousTabIndex

```java
protected int getPreviousTabIndex​(int base)
```

Returns the previous tab index.

**Parameters:** base

- the base
**Returns:** the previous tab index

- getNextTabIndex

```java
protected int getNextTabIndex​(int base)
```

Returns the next tab index.

**Parameters:** base

- the base
**Returns:** the next tab index

- getNextTabIndexInRun

```java
protected int getNextTabIndexInRun​(int tabCount,
int base)
```

Returns the next tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the next tab index in the run

- getPreviousTabIndexInRun

```java
protected int getPreviousTabIndexInRun​(int tabCount,
int base)
```

Returns the previous tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the previous tab index in the run

- getPreviousTabRun

```java
protected int getPreviousTabRun​(int baseRun)
```

Returns the previous tab run.

**Parameters:** baseRun

- the base run
**Returns:** the previous tab run

- getNextTabRun

```java
protected int getNextTabRun​(int baseRun)
```

Returns the next tab run.

**Parameters:** baseRun

- the base run
**Returns:** the next tab run

- rotateInsets

```java
protected static void rotateInsets​(
Insets
topInsets,

Insets
targetInsets,
int targetPlacement)
```

Rotates the insets.

**Parameters:** topInsets

- the top insets
**Parameters:** targetInsets

- the target insets
**Parameters:** targetPlacement

- the target placement

Field Detail

- tabPane

```java
protected
JTabbedPane
tabPane
```

The tab pane

- highlight

```java
protected
Color
highlight
```

Highlight color

- lightHighlight

```java
protected
Color
lightHighlight
```

Light highlight color

- shadow

```java
protected
Color
shadow
```

Shadow color

- darkShadow

```java
protected
Color
darkShadow
```

Dark shadow color

- focus

```java
protected
Color
focus
```

Focus color

- textIconGap

```java
protected int textIconGap
```

Text icon gap

- tabRunOverlay

```java
protected int tabRunOverlay
```

Tab run overlay

- tabInsets

```java
protected
Insets
tabInsets
```

Tab insets

- selectedTabPadInsets

```java
protected
Insets
selectedTabPadInsets
```

Selected tab insets

- tabAreaInsets

```java
protected
Insets
tabAreaInsets
```

Tab area insets

- contentBorderInsets

```java
protected
Insets
contentBorderInsets
```

Content border insets

- upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

- tabRuns

```java
protected int[] tabRuns
```

Tab runs

- runCount

```java
protected int runCount
```

Run count

- selectedRun

```java
protected int selectedRun
```

Selected run

- rects

```java
protected
Rectangle
[] rects
```

Tab rects

- maxTabHeight

```java
protected int maxTabHeight
```

Maximum tab height

- maxTabWidth

```java
protected int maxTabWidth
```

Maximum tab width

- tabChangeListener

```java
protected
ChangeListener
tabChangeListener
```

Tab change listener

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

Property change listener

- mouseListener

```java
protected
MouseListener
mouseListener
```

Mouse change listener

- focusListener

```java
protected
FocusListener
focusListener
```

Focus change listener

- calcRect

```java
protected transient
Rectangle
calcRect
```

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

---

#### Field Detail

tabPane

```java
protected
JTabbedPane
tabPane
```

The tab pane

---

#### tabPane

protected

JTabbedPane

tabPane

The tab pane

highlight

```java
protected
Color
highlight
```

Highlight color

---

#### highlight

protected

Color

highlight

Highlight color

lightHighlight

```java
protected
Color
lightHighlight
```

Light highlight color

---

#### lightHighlight

protected

Color

lightHighlight

Light highlight color

shadow

```java
protected
Color
shadow
```

Shadow color

---

#### shadow

protected

Color

shadow

Shadow color

darkShadow

```java
protected
Color
darkShadow
```

Dark shadow color

---

#### darkShadow

protected

Color

darkShadow

Dark shadow color

focus

```java
protected
Color
focus
```

Focus color

---

#### focus

protected

Color

focus

Focus color

textIconGap

```java
protected int textIconGap
```

Text icon gap

---

#### textIconGap

protected int textIconGap

Text icon gap

tabRunOverlay

```java
protected int tabRunOverlay
```

Tab run overlay

---

#### tabRunOverlay

protected int tabRunOverlay

Tab run overlay

tabInsets

```java
protected
Insets
tabInsets
```

Tab insets

---

#### tabInsets

protected

Insets

tabInsets

Tab insets

selectedTabPadInsets

```java
protected
Insets
selectedTabPadInsets
```

Selected tab insets

---

#### selectedTabPadInsets

protected

Insets

selectedTabPadInsets

Selected tab insets

tabAreaInsets

```java
protected
Insets
tabAreaInsets
```

Tab area insets

---

#### tabAreaInsets

protected

Insets

tabAreaInsets

Tab area insets

contentBorderInsets

```java
protected
Insets
contentBorderInsets
```

Content border insets

---

#### contentBorderInsets

protected

Insets

contentBorderInsets

Content border insets

upKey

```java
@Deprecated

protected
KeyStroke
upKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### upKey

@Deprecated

protected

KeyStroke

upKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

downKey

```java
@Deprecated

protected
KeyStroke
downKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### downKey

@Deprecated

protected

KeyStroke

downKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

leftKey

```java
@Deprecated

protected
KeyStroke
leftKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### leftKey

@Deprecated

protected

KeyStroke

leftKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

rightKey

```java
@Deprecated

protected
KeyStroke
rightKey
```

Deprecated.

As of Java 2 platform v1.3.

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

---

#### rightKey

@Deprecated

protected

KeyStroke

rightKey

As of Java 2 platform v1.3 this previously undocumented field is no
longer used.
Key bindings are now defined by the LookAndFeel, please refer to
the key bindings specification for further details.

tabRuns

```java
protected int[] tabRuns
```

Tab runs

---

#### tabRuns

protected int[] tabRuns

Tab runs

runCount

```java
protected int runCount
```

Run count

---

#### runCount

protected int runCount

Run count

selectedRun

```java
protected int selectedRun
```

Selected run

---

#### selectedRun

protected int selectedRun

Selected run

rects

```java
protected
Rectangle
[] rects
```

Tab rects

---

#### rects

protected

Rectangle

[] rects

Tab rects

maxTabHeight

```java
protected int maxTabHeight
```

Maximum tab height

---

#### maxTabHeight

protected int maxTabHeight

Maximum tab height

maxTabWidth

```java
protected int maxTabWidth
```

Maximum tab width

---

#### maxTabWidth

protected int maxTabWidth

Maximum tab width

tabChangeListener

```java
protected
ChangeListener
tabChangeListener
```

Tab change listener

---

#### tabChangeListener

protected

ChangeListener

tabChangeListener

Tab change listener

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

mouseListener

```java
protected
MouseListener
mouseListener
```

Mouse change listener

---

#### mouseListener

protected

MouseListener

mouseListener

Mouse change listener

focusListener

```java
protected
FocusListener
focusListener
```

Focus change listener

---

#### focusListener

protected

FocusListener

focusListener

Focus change listener

calcRect

```java
protected transient
Rectangle
calcRect
```

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

---

#### calcRect

protected transient

Rectangle

calcRect

A rectangle used for general layout calculations in order
to avoid constructing many new Rectangles on the fly.

Constructor Detail

- BasicTabbedPaneUI

```java
public BasicTabbedPaneUI()
```

---

#### Constructor Detail

BasicTabbedPaneUI

```java
public BasicTabbedPaneUI()
```

---

#### BasicTabbedPaneUI

public BasicTabbedPaneUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Create a UI.

**Parameters:** c

- a component
**Returns:** a UI

- createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

**Returns:** a layout manager object
**See Also:** BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

- installComponents

```java
protected void installComponents()
```

Creates and installs any required subcomponents for the JTabbedPane.
Invoked by installUI.

**Since:** 1.4

- createScrollButton

```java
protected
JButton
createScrollButton​(int direction)
```

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction. The
returned JButton must be instance of UIResource.

**Parameters:** direction

- One of the SwingConstants constants:
SOUTH, NORTH, EAST or WEST
**Returns:** Widget for user to
**Throws:** IllegalArgumentException

- if direction is not one of
NORTH, SOUTH, EAST or WEST
**Since:** 1.5
**See Also:** JTabbedPane.setTabPlacement(int)

,

SwingConstants

- uninstallComponents

```java
protected void uninstallComponents()
```

Removes any installed subcomponents from the JTabbedPane.
Invoked by uninstallUI.

**Since:** 1.4

- installDefaults

```java
protected void installDefaults()
```

Install the defaults.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstall the defaults.

- installListeners

```java
protected void installListeners()
```

Install the listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

**Returns:** a mouse listener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a focus listener.

**Returns:** a focus listener

- createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Creates a change listener.

**Returns:** a change listener

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a property change listener.

**Returns:** a property change listener

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

- setRolloverTab

```java
protected void setRolloverTab​(int index)
```

Sets the tab the mouse is currently over to

index

.

index

will be -1 if the mouse is no longer over any
tab. No checking is done to ensure the passed in index identifies a
valid tab.

**Parameters:** index

- Index of the tab the mouse is over.
**Since:** 1.5

- getRolloverTab

```java
protected int getRolloverTab()
```

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

**Returns:** the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab
**Since:** 1.5

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

- getBaseline

```java
protected int getBaseline​(int tab)
```

Returns the baseline for the specified tab.

**Parameters:** tab

- index of tab to get baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IndexOutOfBoundsException

- if index is out of range
(index < 0 || index >= tab count)
**Since:** 1.6

- getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Returns:** amount to offset the baseline by
**Since:** 1.6

- paintTabArea

```java
protected void paintTabArea​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the tabs in the tab area.
Invoked by paint().
The graphics parameter must be a valid

Graphics

object. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
The selected index must be a valid tabbed pane tab index (0 to
tab count - 1, inclusive) or -1 if no tab is currently selected.
The handling of invalid parameters is unspecified.

**Parameters:** g

- the graphics object to use for rendering
**Parameters:** tabPlacement

- the placement for the tabs within the JTabbedPane
**Parameters:** selectedIndex

- the tab index of the selected component
**Since:** 1.4

- paintTab

```java
protected void paintTab​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect)
```

Paints a tab.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle

- layoutLabel

```java
protected void layoutLabel​(int tabPlacement,

FontMetrics
metrics,
int tabIndex,

String
title,

Icon
icon,

Rectangle
tabRect,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Laysout a label.

**Parameters:** tabPlacement

- the tab placement
**Parameters:** metrics

- the font metric
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** icon

- the icon
**Parameters:** tabRect

- the tab rectangle
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- paintIcon

```java
protected void paintIcon​(
Graphics
g,
int tabPlacement,
int tabIndex,

Icon
icon,

Rectangle
iconRect,
boolean isSelected)
```

Paints an icon.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** icon

- the icon
**Parameters:** iconRect

- the icon rectangle
**Parameters:** isSelected

- selection status

- paintText

```java
protected void paintText​(
Graphics
g,
int tabPlacement,

Font
font,

FontMetrics
metrics,
int tabIndex,

String
title,

Rectangle
textRect,
boolean isSelected)
```

Paints text.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** font

- the font
**Parameters:** metrics

- the font metrics
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Returns the tab label shift x.

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

Returns the tab label shift y.

**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** isSelected

- selection status
**Returns:** the tab label shift y

- paintFocusIndicator

```java
protected void paintFocusIndicator​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Paints the focus indicator.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

- paintTabBorder

```java
protected void paintTabBorder​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

this function draws the border around each tab
note that this function does now draw the background of the tab.
that is done elsewhere

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

- paintTabBackground

```java
protected void paintTabBackground​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

Paints the tab background.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

- paintContentBorder

```java
protected void paintContentBorder​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the content border.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component

- paintContentBorderTopEdge

```java
protected void paintContentBorderTopEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border top edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderLeftEdge

```java
protected void paintContentBorderLeftEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border left edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderBottomEdge

```java
protected void paintContentBorderBottomEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border bottom edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- paintContentBorderRightEdge

```java
protected void paintContentBorderRightEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border right edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

- getTabBounds

```java
public
Rectangle
getTabBounds​(
JTabbedPane
pane,
int i)
```

Returns the bounds of the specified tab index. The bounds are
with respect to the JTabbedPane's coordinate space.

**Specified by:** getTabBounds

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** i

- the index
**Returns:** the rectangle for the tab bounds

- tabForCoordinate

```java
public int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

**Specified by:** tabForCoordinate

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

- getTabBounds

```java
protected
Rectangle
getTabBounds​(int tabIndex,

Rectangle
dest)
```

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component. This is required because the tab rects
are by default defined in the coordinate space of the component where
they are rendered, which could be the JTabbedPane
(for WRAP_TAB_LAYOUT) or a ScrollableTabPanel (SCROLL_TAB_LAYOUT).
This method should be used whenever the tab rectangle must be relative
to the JTabbedPane itself and the result should be placed in a
designated Rectangle object (rather than instantiating and returning
a new Rectangle each time). The tab index parameter must be a valid
tabbed pane tab index (0 to tab count - 1, inclusive). The destination
rectangle parameter must be a valid

Rectangle

instance.
The handling of invalid parameters is unspecified.

**Parameters:** tabIndex

- the index of the tab
**Parameters:** dest

- the rectangle where the result should be placed
**Returns:** the resulting rectangle
**Since:** 1.4

- getVisibleComponent

```java
protected
Component
getVisibleComponent()
```

Returns the visible component.

**Returns:** the visible component

- setVisibleComponent

```java
protected void setVisibleComponent​(
Component
component)
```

Sets the visible component.

**Parameters:** component

- the component

- assureRectsCreated

```java
protected void assureRectsCreated​(int tabCount)
```

Assure the rectangles are created.

**Parameters:** tabCount

- the tab count

- expandTabRunsArray

```java
protected void expandTabRunsArray()
```

Expands the tab runs array.

- getRunForTab

```java
protected int getRunForTab​(int tabCount,
int tabIndex)
```

Returns the run for a tab.

**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the tab index.
**Returns:** the run for a tab

- lastTabInRun

```java
protected int lastTabInRun​(int tabCount,
int run)
```

Returns the last tab in a run.

**Parameters:** tabCount

- the tab count
**Parameters:** run

- the run
**Returns:** the last tab in a run

- getTabRunOverlay

```java
protected int getTabRunOverlay​(int tabPlacement)
```

Returns the tab run overlay.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the tab run overlay

- getTabRunIndent

```java
protected int getTabRunIndent​(int tabPlacement,
int run)
```

Returns the tab run indent.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** the tab run indent

- shouldPadTabRun

```java
protected boolean shouldPadTabRun​(int tabPlacement,
int run)
```

Returns whether or not the tab run should be padded.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** whether or not the tab run should be padded

- shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement)
```

Returns whether or not the tab run should be rotated.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** whether or not the tab run should be rotated

- getIconForTab

```java
protected
Icon
getIconForTab​(int tabIndex)
```

Returns the icon for a tab.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the icon for a tab

- getTextViewForTab

```java
protected
View
getTextViewForTab​(int tabIndex)
```

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab. This is provided to support html rendering inside tabs.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the text view to render the tab's text or null if no
specialized rendering is required
**Since:** 1.4

- calculateTabHeight

```java
protected int calculateTabHeight​(int tabPlacement,
int tabIndex,
int fontHeight)
```

Calculates the tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** fontHeight

- the font height
**Returns:** the tab height

- calculateMaxTabHeight

```java
protected int calculateMaxTabHeight​(int tabPlacement)
```

Calculates the maximum tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab height

- calculateTabWidth

```java
protected int calculateTabWidth​(int tabPlacement,
int tabIndex,

FontMetrics
metrics)
```

Calculates the tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** metrics

- the font metrics
**Returns:** the tab width

- calculateMaxTabWidth

```java
protected int calculateMaxTabWidth​(int tabPlacement)
```

Calculates the maximum tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab width

- calculateTabAreaHeight

```java
protected int calculateTabAreaHeight​(int tabPlacement,
int horizRunCount,
int maxTabHeight)
```

Calculates the tab area height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** horizRunCount

- horizontal run count
**Parameters:** maxTabHeight

- maximum tab height
**Returns:** the tab area height

- calculateTabAreaWidth

```java
protected int calculateTabAreaWidth​(int tabPlacement,
int vertRunCount,
int maxTabWidth)
```

Calculates the tab area width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** vertRunCount

- vertical run count
**Parameters:** maxTabWidth

- maximum tab width
**Returns:** the tab area width

- getTabInsets

```java
protected
Insets
getTabInsets​(int tabPlacement,
int tabIndex)
```

Returns the tab insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the tab index
**Returns:** the tab insets

- getSelectedTabPadInsets

```java
protected
Insets
getSelectedTabPadInsets​(int tabPlacement)
```

Returns the selected tab pad insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the selected tab pad insets

- getTabAreaInsets

```java
protected
Insets
getTabAreaInsets​(int tabPlacement)
```

Returns the tab area insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the pad area insets

- getContentBorderInsets

```java
protected
Insets
getContentBorderInsets​(int tabPlacement)
```

Returns the content border insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the content border insets

- getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Returns the font metrics.

**Returns:** the font metrics

- navigateSelectedTab

```java
protected void navigateSelectedTab​(int direction)
```

Navigate the selected tab.

**Parameters:** direction

- the direction

- selectNextTabInRun

```java
protected void selectNextTabInRun​(int current)
```

Select the next tab in the run.

**Parameters:** current

- the current tab

- selectPreviousTabInRun

```java
protected void selectPreviousTabInRun​(int current)
```

Select the previous tab in the run.

**Parameters:** current

- the current tab

- selectNextTab

```java
protected void selectNextTab​(int current)
```

Select the next tab.

**Parameters:** current

- the current tab

- selectPreviousTab

```java
protected void selectPreviousTab​(int current)
```

Select the previous tab.

**Parameters:** current

- the current tab

- selectAdjacentRunTab

```java
protected void selectAdjacentRunTab​(int tabPlacement,
int tabIndex,
int offset)
```

Selects an adjacent run of tabs.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** offset

- selection offset

- getFocusIndex

```java
protected int getFocusIndex()
```

Returns the index of the tab that has focus.

**Returns:** index of tab that has focus
**Since:** 1.5

- getTabRunOffset

```java
protected int getTabRunOffset​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)
```

Returns the tab run offset.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** forward

- forward or not
**Returns:** the tab run offset

- getPreviousTabIndex

```java
protected int getPreviousTabIndex​(int base)
```

Returns the previous tab index.

**Parameters:** base

- the base
**Returns:** the previous tab index

- getNextTabIndex

```java
protected int getNextTabIndex​(int base)
```

Returns the next tab index.

**Parameters:** base

- the base
**Returns:** the next tab index

- getNextTabIndexInRun

```java
protected int getNextTabIndexInRun​(int tabCount,
int base)
```

Returns the next tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the next tab index in the run

- getPreviousTabIndexInRun

```java
protected int getPreviousTabIndexInRun​(int tabCount,
int base)
```

Returns the previous tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the previous tab index in the run

- getPreviousTabRun

```java
protected int getPreviousTabRun​(int baseRun)
```

Returns the previous tab run.

**Parameters:** baseRun

- the base run
**Returns:** the previous tab run

- getNextTabRun

```java
protected int getNextTabRun​(int baseRun)
```

Returns the next tab run.

**Parameters:** baseRun

- the base run
**Returns:** the next tab run

- rotateInsets

```java
protected static void rotateInsets​(
Insets
topInsets,

Insets
targetInsets,
int targetPlacement)
```

Rotates the insets.

**Parameters:** topInsets

- the top insets
**Parameters:** targetInsets

- the target insets
**Parameters:** targetPlacement

- the target placement

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

Create a UI.

**Parameters:** c

- a component
**Returns:** a UI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Create a UI.

createLayoutManager

```java
protected
LayoutManager
createLayoutManager()
```

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

**Returns:** a layout manager object
**See Also:** BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

---

#### createLayoutManager

protected

LayoutManager

createLayoutManager()

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

installComponents

```java
protected void installComponents()
```

Creates and installs any required subcomponents for the JTabbedPane.
Invoked by installUI.

**Since:** 1.4

---

#### installComponents

protected void installComponents()

Creates and installs any required subcomponents for the JTabbedPane.
Invoked by installUI.

createScrollButton

```java
protected
JButton
createScrollButton​(int direction)
```

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction. The
returned JButton must be instance of UIResource.

**Parameters:** direction

- One of the SwingConstants constants:
SOUTH, NORTH, EAST or WEST
**Returns:** Widget for user to
**Throws:** IllegalArgumentException

- if direction is not one of
NORTH, SOUTH, EAST or WEST
**Since:** 1.5
**See Also:** JTabbedPane.setTabPlacement(int)

,

SwingConstants

---

#### createScrollButton

protected

JButton

createScrollButton​(int direction)

Creates and returns a JButton that will provide the user
with a way to scroll the tabs in a particular direction. The
returned JButton must be instance of UIResource.

uninstallComponents

```java
protected void uninstallComponents()
```

Removes any installed subcomponents from the JTabbedPane.
Invoked by uninstallUI.

**Since:** 1.4

---

#### uninstallComponents

protected void uninstallComponents()

Removes any installed subcomponents from the JTabbedPane.
Invoked by uninstallUI.

installDefaults

```java
protected void installDefaults()
```

Install the defaults.

---

#### installDefaults

protected void installDefaults()

Install the defaults.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstall the defaults.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstall the defaults.

installListeners

```java
protected void installListeners()
```

Install the listeners.

---

#### installListeners

protected void installListeners()

Install the listeners.

uninstallListeners

```java
protected void uninstallListeners()
```

Uninstall the listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Uninstall the listeners.

createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

**Returns:** a mouse listener

---

#### createMouseListener

protected

MouseListener

createMouseListener()

Creates a mouse listener.

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a focus listener.

**Returns:** a focus listener

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Creates a focus listener.

createChangeListener

```java
protected
ChangeListener
createChangeListener()
```

Creates a change listener.

**Returns:** a change listener

---

#### createChangeListener

protected

ChangeListener

createChangeListener()

Creates a change listener.

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

setRolloverTab

```java
protected void setRolloverTab​(int index)
```

Sets the tab the mouse is currently over to

index

.

index

will be -1 if the mouse is no longer over any
tab. No checking is done to ensure the passed in index identifies a
valid tab.

**Parameters:** index

- Index of the tab the mouse is over.
**Since:** 1.5

---

#### setRolloverTab

protected void setRolloverTab​(int index)

Sets the tab the mouse is currently over to

index

.

index

will be -1 if the mouse is no longer over any
tab. No checking is done to ensure the passed in index identifies a
valid tab.

getRolloverTab

```java
protected int getRolloverTab()
```

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

**Returns:** the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab
**Since:** 1.5

---

#### getRolloverTab

protected int getRolloverTab()

Returns the tab the mouse is currently over, or

-1

if the mouse is no
longer over any tab.

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

getBaseline

```java
protected int getBaseline​(int tab)
```

Returns the baseline for the specified tab.

**Parameters:** tab

- index of tab to get baseline for
**Returns:** baseline or a value < 0 indicating there is no reasonable
baseline
**Throws:** IndexOutOfBoundsException

- if index is out of range
(index < 0 || index >= tab count)
**Since:** 1.6

---

#### getBaseline

protected int getBaseline​(int tab)

Returns the baseline for the specified tab.

getBaselineOffset

```java
protected int getBaselineOffset()
```

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

**Returns:** amount to offset the baseline by
**Since:** 1.6

---

#### getBaselineOffset

protected int getBaselineOffset()

Returns the amount the baseline is offset by. This is typically
the same as

getTabLabelShiftY

.

paintTabArea

```java
protected void paintTabArea​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the tabs in the tab area.
Invoked by paint().
The graphics parameter must be a valid

Graphics

object. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
The selected index must be a valid tabbed pane tab index (0 to
tab count - 1, inclusive) or -1 if no tab is currently selected.
The handling of invalid parameters is unspecified.

**Parameters:** g

- the graphics object to use for rendering
**Parameters:** tabPlacement

- the placement for the tabs within the JTabbedPane
**Parameters:** selectedIndex

- the tab index of the selected component
**Since:** 1.4

---

#### paintTabArea

protected void paintTabArea​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the tabs in the tab area.
Invoked by paint().
The graphics parameter must be a valid

Graphics

object. Tab placement may be either:

JTabbedPane.TOP

,

JTabbedPane.BOTTOM

,

JTabbedPane.LEFT

, or

JTabbedPane.RIGHT

.
The selected index must be a valid tabbed pane tab index (0 to
tab count - 1, inclusive) or -1 if no tab is currently selected.
The handling of invalid parameters is unspecified.

paintTab

```java
protected void paintTab​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect)
```

Paints a tab.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle

---

#### paintTab

protected void paintTab​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect)

Paints a tab.

layoutLabel

```java
protected void layoutLabel​(int tabPlacement,

FontMetrics
metrics,
int tabIndex,

String
title,

Icon
icon,

Rectangle
tabRect,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Laysout a label.

**Parameters:** tabPlacement

- the tab placement
**Parameters:** metrics

- the font metric
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** icon

- the icon
**Parameters:** tabRect

- the tab rectangle
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

---

#### layoutLabel

protected void layoutLabel​(int tabPlacement,

FontMetrics

metrics,
int tabIndex,

String

title,

Icon

icon,

Rectangle

tabRect,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Laysout a label.

paintIcon

```java
protected void paintIcon​(
Graphics
g,
int tabPlacement,
int tabIndex,

Icon
icon,

Rectangle
iconRect,
boolean isSelected)
```

Paints an icon.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** tabIndex

- the tab index
**Parameters:** icon

- the icon
**Parameters:** iconRect

- the icon rectangle
**Parameters:** isSelected

- selection status

---

#### paintIcon

protected void paintIcon​(

Graphics

g,
int tabPlacement,
int tabIndex,

Icon

icon,

Rectangle

iconRect,
boolean isSelected)

Paints an icon.

paintText

```java
protected void paintText​(
Graphics
g,
int tabPlacement,

Font
font,

FontMetrics
metrics,
int tabIndex,

String
title,

Rectangle
textRect,
boolean isSelected)
```

Paints text.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** font

- the font
**Parameters:** metrics

- the font metrics
**Parameters:** tabIndex

- the tab index
**Parameters:** title

- the title
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

---

#### paintText

protected void paintText​(

Graphics

g,
int tabPlacement,

Font

font,

FontMetrics

metrics,
int tabIndex,

String

title,

Rectangle

textRect,
boolean isSelected)

Paints text.

getTabLabelShiftX

```java
protected int getTabLabelShiftX​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Returns the tab label shift x.

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

Returns the tab label shift x.

getTabLabelShiftY

```java
protected int getTabLabelShiftY​(int tabPlacement,
int tabIndex,
boolean isSelected)
```

Returns the tab label shift y.

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

Returns the tab label shift y.

paintFocusIndicator

```java
protected void paintFocusIndicator​(
Graphics
g,
int tabPlacement,

Rectangle
[] rects,
int tabIndex,

Rectangle
iconRect,

Rectangle
textRect,
boolean isSelected)
```

Paints the focus indicator.

**Parameters:** g

- the graphics
**Parameters:** tabPlacement

- the tab placement
**Parameters:** rects

- rectangles
**Parameters:** tabIndex

- the tab index
**Parameters:** iconRect

- the icon rectangle
**Parameters:** textRect

- the text rectangle
**Parameters:** isSelected

- selection status

---

#### paintFocusIndicator

protected void paintFocusIndicator​(

Graphics

g,
int tabPlacement,

Rectangle

[] rects,
int tabIndex,

Rectangle

iconRect,

Rectangle

textRect,
boolean isSelected)

Paints the focus indicator.

paintTabBorder

```java
protected void paintTabBorder​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

this function draws the border around each tab
note that this function does now draw the background of the tab.
that is done elsewhere

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

---

#### paintTabBorder

protected void paintTabBorder​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

this function draws the border around each tab
note that this function does now draw the background of the tab.
that is done elsewhere

paintTabBackground

```java
protected void paintTabBackground​(
Graphics
g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)
```

Paints the tab background.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab
**Parameters:** isSelected

- a

boolean

which determines whether or not
the tab is selected

---

#### paintTabBackground

protected void paintTabBackground​(

Graphics

g,
int tabPlacement,
int tabIndex,
int x,
int y,
int w,
int h,
boolean isSelected)

Paints the tab background.

paintContentBorder

```java
protected void paintContentBorder​(
Graphics
g,
int tabPlacement,
int selectedIndex)
```

Paints the content border.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component

---

#### paintContentBorder

protected void paintContentBorder​(

Graphics

g,
int tabPlacement,
int selectedIndex)

Paints the content border.

paintContentBorderTopEdge

```java
protected void paintContentBorderTopEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border top edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

---

#### paintContentBorderTopEdge

protected void paintContentBorderTopEdge​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border top edge.

paintContentBorderLeftEdge

```java
protected void paintContentBorderLeftEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border left edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

---

#### paintContentBorderLeftEdge

protected void paintContentBorderLeftEdge​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border left edge.

paintContentBorderBottomEdge

```java
protected void paintContentBorderBottomEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border bottom edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

---

#### paintContentBorderBottomEdge

protected void paintContentBorderBottomEdge​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border bottom edge.

paintContentBorderRightEdge

```java
protected void paintContentBorderRightEdge​(
Graphics
g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)
```

Paints the content border right edge.

**Parameters:** g

- the graphics context in which to paint
**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** selectedIndex

- the tab index of the selected component
**Parameters:** x

- the x coordinate of tab
**Parameters:** y

- the y coordinate of tab
**Parameters:** w

- the width of the tab
**Parameters:** h

- the height of the tab

---

#### paintContentBorderRightEdge

protected void paintContentBorderRightEdge​(

Graphics

g,
int tabPlacement,
int selectedIndex,
int x,
int y,
int w,
int h)

Paints the content border right edge.

getTabBounds

```java
public
Rectangle
getTabBounds​(
JTabbedPane
pane,
int i)
```

Returns the bounds of the specified tab index. The bounds are
with respect to the JTabbedPane's coordinate space.

**Specified by:** getTabBounds

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** i

- the index
**Returns:** the rectangle for the tab bounds

---

#### getTabBounds

public

Rectangle

getTabBounds​(

JTabbedPane

pane,
int i)

Returns the bounds of the specified tab index. The bounds are
with respect to the JTabbedPane's coordinate space.

tabForCoordinate

```java
public int tabForCoordinate​(
JTabbedPane
pane,
int x,
int y)
```

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

**Specified by:** tabForCoordinate

in class

TabbedPaneUI
**Parameters:** pane

- the pane
**Parameters:** x

- the x coordinate
**Parameters:** y

- the y coordinate
**Returns:** the tab for the coordinate

---

#### tabForCoordinate

public int tabForCoordinate​(

JTabbedPane

pane,
int x,
int y)

Returns the tab index which intersects the specified point
in the JTabbedPane's coordinate space.

getTabBounds

```java
protected
Rectangle
getTabBounds​(int tabIndex,

Rectangle
dest)
```

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component. This is required because the tab rects
are by default defined in the coordinate space of the component where
they are rendered, which could be the JTabbedPane
(for WRAP_TAB_LAYOUT) or a ScrollableTabPanel (SCROLL_TAB_LAYOUT).
This method should be used whenever the tab rectangle must be relative
to the JTabbedPane itself and the result should be placed in a
designated Rectangle object (rather than instantiating and returning
a new Rectangle each time). The tab index parameter must be a valid
tabbed pane tab index (0 to tab count - 1, inclusive). The destination
rectangle parameter must be a valid

Rectangle

instance.
The handling of invalid parameters is unspecified.

**Parameters:** tabIndex

- the index of the tab
**Parameters:** dest

- the rectangle where the result should be placed
**Returns:** the resulting rectangle
**Since:** 1.4

---

#### getTabBounds

protected

Rectangle

getTabBounds​(int tabIndex,

Rectangle

dest)

Returns the bounds of the specified tab in the coordinate space
of the JTabbedPane component. This is required because the tab rects
are by default defined in the coordinate space of the component where
they are rendered, which could be the JTabbedPane
(for WRAP_TAB_LAYOUT) or a ScrollableTabPanel (SCROLL_TAB_LAYOUT).
This method should be used whenever the tab rectangle must be relative
to the JTabbedPane itself and the result should be placed in a
designated Rectangle object (rather than instantiating and returning
a new Rectangle each time). The tab index parameter must be a valid
tabbed pane tab index (0 to tab count - 1, inclusive). The destination
rectangle parameter must be a valid

Rectangle

instance.
The handling of invalid parameters is unspecified.

getVisibleComponent

```java
protected
Component
getVisibleComponent()
```

Returns the visible component.

**Returns:** the visible component

---

#### getVisibleComponent

protected

Component

getVisibleComponent()

Returns the visible component.

setVisibleComponent

```java
protected void setVisibleComponent​(
Component
component)
```

Sets the visible component.

**Parameters:** component

- the component

---

#### setVisibleComponent

protected void setVisibleComponent​(

Component

component)

Sets the visible component.

assureRectsCreated

```java
protected void assureRectsCreated​(int tabCount)
```

Assure the rectangles are created.

**Parameters:** tabCount

- the tab count

---

#### assureRectsCreated

protected void assureRectsCreated​(int tabCount)

Assure the rectangles are created.

expandTabRunsArray

```java
protected void expandTabRunsArray()
```

Expands the tab runs array.

---

#### expandTabRunsArray

protected void expandTabRunsArray()

Expands the tab runs array.

getRunForTab

```java
protected int getRunForTab​(int tabCount,
int tabIndex)
```

Returns the run for a tab.

**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the tab index.
**Returns:** the run for a tab

---

#### getRunForTab

protected int getRunForTab​(int tabCount,
int tabIndex)

Returns the run for a tab.

lastTabInRun

```java
protected int lastTabInRun​(int tabCount,
int run)
```

Returns the last tab in a run.

**Parameters:** tabCount

- the tab count
**Parameters:** run

- the run
**Returns:** the last tab in a run

---

#### lastTabInRun

protected int lastTabInRun​(int tabCount,
int run)

Returns the last tab in a run.

getTabRunOverlay

```java
protected int getTabRunOverlay​(int tabPlacement)
```

Returns the tab run overlay.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the tab run overlay

---

#### getTabRunOverlay

protected int getTabRunOverlay​(int tabPlacement)

Returns the tab run overlay.

getTabRunIndent

```java
protected int getTabRunIndent​(int tabPlacement,
int run)
```

Returns the tab run indent.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** the tab run indent

---

#### getTabRunIndent

protected int getTabRunIndent​(int tabPlacement,
int run)

Returns the tab run indent.

shouldPadTabRun

```java
protected boolean shouldPadTabRun​(int tabPlacement,
int run)
```

Returns whether or not the tab run should be padded.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** run

- the tab run
**Returns:** whether or not the tab run should be padded

---

#### shouldPadTabRun

protected boolean shouldPadTabRun​(int tabPlacement,
int run)

Returns whether or not the tab run should be padded.

shouldRotateTabRuns

```java
protected boolean shouldRotateTabRuns​(int tabPlacement)
```

Returns whether or not the tab run should be rotated.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** whether or not the tab run should be rotated

---

#### shouldRotateTabRuns

protected boolean shouldRotateTabRuns​(int tabPlacement)

Returns whether or not the tab run should be rotated.

getIconForTab

```java
protected
Icon
getIconForTab​(int tabIndex)
```

Returns the icon for a tab.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the icon for a tab

---

#### getIconForTab

protected

Icon

getIconForTab​(int tabIndex)

Returns the icon for a tab.

getTextViewForTab

```java
protected
View
getTextViewForTab​(int tabIndex)
```

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab. This is provided to support html rendering inside tabs.

**Parameters:** tabIndex

- the index of the tab
**Returns:** the text view to render the tab's text or null if no
specialized rendering is required
**Since:** 1.4

---

#### getTextViewForTab

protected

View

getTextViewForTab​(int tabIndex)

Returns the text View object required to render stylized text (HTML) for
the specified tab or null if no specialized text rendering is needed
for this tab. This is provided to support html rendering inside tabs.

calculateTabHeight

```java
protected int calculateTabHeight​(int tabPlacement,
int tabIndex,
int fontHeight)
```

Calculates the tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** fontHeight

- the font height
**Returns:** the tab height

---

#### calculateTabHeight

protected int calculateTabHeight​(int tabPlacement,
int tabIndex,
int fontHeight)

Calculates the tab height.

calculateMaxTabHeight

```java
protected int calculateMaxTabHeight​(int tabPlacement)
```

Calculates the maximum tab height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab height

---

#### calculateMaxTabHeight

protected int calculateMaxTabHeight​(int tabPlacement)

Calculates the maximum tab height.

calculateTabWidth

```java
protected int calculateTabWidth​(int tabPlacement,
int tabIndex,

FontMetrics
metrics)
```

Calculates the tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** metrics

- the font metrics
**Returns:** the tab width

---

#### calculateTabWidth

protected int calculateTabWidth​(int tabPlacement,
int tabIndex,

FontMetrics

metrics)

Calculates the tab width.

calculateMaxTabWidth

```java
protected int calculateMaxTabWidth​(int tabPlacement)
```

Calculates the maximum tab width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the maximum tab width

---

#### calculateMaxTabWidth

protected int calculateMaxTabWidth​(int tabPlacement)

Calculates the maximum tab width.

calculateTabAreaHeight

```java
protected int calculateTabAreaHeight​(int tabPlacement,
int horizRunCount,
int maxTabHeight)
```

Calculates the tab area height.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** horizRunCount

- horizontal run count
**Parameters:** maxTabHeight

- maximum tab height
**Returns:** the tab area height

---

#### calculateTabAreaHeight

protected int calculateTabAreaHeight​(int tabPlacement,
int horizRunCount,
int maxTabHeight)

Calculates the tab area height.

calculateTabAreaWidth

```java
protected int calculateTabAreaWidth​(int tabPlacement,
int vertRunCount,
int maxTabWidth)
```

Calculates the tab area width.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** vertRunCount

- vertical run count
**Parameters:** maxTabWidth

- maximum tab width
**Returns:** the tab area width

---

#### calculateTabAreaWidth

protected int calculateTabAreaWidth​(int tabPlacement,
int vertRunCount,
int maxTabWidth)

Calculates the tab area width.

getTabInsets

```java
protected
Insets
getTabInsets​(int tabPlacement,
int tabIndex)
```

Returns the tab insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the tab index
**Returns:** the tab insets

---

#### getTabInsets

protected

Insets

getTabInsets​(int tabPlacement,
int tabIndex)

Returns the tab insets.

getSelectedTabPadInsets

```java
protected
Insets
getSelectedTabPadInsets​(int tabPlacement)
```

Returns the selected tab pad insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the selected tab pad insets

---

#### getSelectedTabPadInsets

protected

Insets

getSelectedTabPadInsets​(int tabPlacement)

Returns the selected tab pad insets.

getTabAreaInsets

```java
protected
Insets
getTabAreaInsets​(int tabPlacement)
```

Returns the tab area insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the pad area insets

---

#### getTabAreaInsets

protected

Insets

getTabAreaInsets​(int tabPlacement)

Returns the tab area insets.

getContentBorderInsets

```java
protected
Insets
getContentBorderInsets​(int tabPlacement)
```

Returns the content border insets.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Returns:** the content border insets

---

#### getContentBorderInsets

protected

Insets

getContentBorderInsets​(int tabPlacement)

Returns the content border insets.

getFontMetrics

```java
protected
FontMetrics
getFontMetrics()
```

Returns the font metrics.

**Returns:** the font metrics

---

#### getFontMetrics

protected

FontMetrics

getFontMetrics()

Returns the font metrics.

navigateSelectedTab

```java
protected void navigateSelectedTab​(int direction)
```

Navigate the selected tab.

**Parameters:** direction

- the direction

---

#### navigateSelectedTab

protected void navigateSelectedTab​(int direction)

Navigate the selected tab.

selectNextTabInRun

```java
protected void selectNextTabInRun​(int current)
```

Select the next tab in the run.

**Parameters:** current

- the current tab

---

#### selectNextTabInRun

protected void selectNextTabInRun​(int current)

Select the next tab in the run.

selectPreviousTabInRun

```java
protected void selectPreviousTabInRun​(int current)
```

Select the previous tab in the run.

**Parameters:** current

- the current tab

---

#### selectPreviousTabInRun

protected void selectPreviousTabInRun​(int current)

Select the previous tab in the run.

selectNextTab

```java
protected void selectNextTab​(int current)
```

Select the next tab.

**Parameters:** current

- the current tab

---

#### selectNextTab

protected void selectNextTab​(int current)

Select the next tab.

selectPreviousTab

```java
protected void selectPreviousTab​(int current)
```

Select the previous tab.

**Parameters:** current

- the current tab

---

#### selectPreviousTab

protected void selectPreviousTab​(int current)

Select the previous tab.

selectAdjacentRunTab

```java
protected void selectAdjacentRunTab​(int tabPlacement,
int tabIndex,
int offset)
```

Selects an adjacent run of tabs.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** offset

- selection offset

---

#### selectAdjacentRunTab

protected void selectAdjacentRunTab​(int tabPlacement,
int tabIndex,
int offset)

Selects an adjacent run of tabs.

getFocusIndex

```java
protected int getFocusIndex()
```

Returns the index of the tab that has focus.

**Returns:** index of tab that has focus
**Since:** 1.5

---

#### getFocusIndex

protected int getFocusIndex()

Returns the index of the tab that has focus.

getTabRunOffset

```java
protected int getTabRunOffset​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)
```

Returns the tab run offset.

**Parameters:** tabPlacement

- the placement (left, right, bottom, top) of the tab
**Parameters:** tabCount

- the tab count
**Parameters:** tabIndex

- the index of the tab with respect to other tabs
**Parameters:** forward

- forward or not
**Returns:** the tab run offset

---

#### getTabRunOffset

protected int getTabRunOffset​(int tabPlacement,
int tabCount,
int tabIndex,
boolean forward)

Returns the tab run offset.

getPreviousTabIndex

```java
protected int getPreviousTabIndex​(int base)
```

Returns the previous tab index.

**Parameters:** base

- the base
**Returns:** the previous tab index

---

#### getPreviousTabIndex

protected int getPreviousTabIndex​(int base)

Returns the previous tab index.

getNextTabIndex

```java
protected int getNextTabIndex​(int base)
```

Returns the next tab index.

**Parameters:** base

- the base
**Returns:** the next tab index

---

#### getNextTabIndex

protected int getNextTabIndex​(int base)

Returns the next tab index.

getNextTabIndexInRun

```java
protected int getNextTabIndexInRun​(int tabCount,
int base)
```

Returns the next tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the next tab index in the run

---

#### getNextTabIndexInRun

protected int getNextTabIndexInRun​(int tabCount,
int base)

Returns the next tab index in the run.

getPreviousTabIndexInRun

```java
protected int getPreviousTabIndexInRun​(int tabCount,
int base)
```

Returns the previous tab index in the run.

**Parameters:** tabCount

- the tab count
**Parameters:** base

- the base
**Returns:** the previous tab index in the run

---

#### getPreviousTabIndexInRun

protected int getPreviousTabIndexInRun​(int tabCount,
int base)

Returns the previous tab index in the run.

getPreviousTabRun

```java
protected int getPreviousTabRun​(int baseRun)
```

Returns the previous tab run.

**Parameters:** baseRun

- the base run
**Returns:** the previous tab run

---

#### getPreviousTabRun

protected int getPreviousTabRun​(int baseRun)

Returns the previous tab run.

getNextTabRun

```java
protected int getNextTabRun​(int baseRun)
```

Returns the next tab run.

**Parameters:** baseRun

- the base run
**Returns:** the next tab run

---

#### getNextTabRun

protected int getNextTabRun​(int baseRun)

Returns the next tab run.

rotateInsets

```java
protected static void rotateInsets​(
Insets
topInsets,

Insets
targetInsets,
int targetPlacement)
```

Rotates the insets.

**Parameters:** topInsets

- the top insets
**Parameters:** targetInsets

- the target insets
**Parameters:** targetPlacement

- the target placement

---

#### rotateInsets

protected static void rotateInsets​(

Insets

topInsets,

Insets

targetInsets,
int targetPlacement)

Rotates the insets.

---

