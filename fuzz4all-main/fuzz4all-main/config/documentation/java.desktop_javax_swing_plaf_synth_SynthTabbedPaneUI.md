# Class SynthTabbedPaneUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthTabbedPaneUI.html`

### Class Description

```java
public class
SynthTabbedPaneUI

extends
BasicTabbedPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JTabbedPane

.

Looks up the

selectedTabPadInsets

property from the Style,
which represents additional insets for the selected tab.

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public SynthTabbedPaneUI()

*No description found.*

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

#### protected
MouseListener
createMouseListener()

Creates a mouse listener.

Overridden to keep track of whether the selected tab is also pressed.

**Overrides:**
- createMouseListener

in class

BasicTabbedPaneUI

**Returns:**
- a mouse listener

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

Overridden to create a TabbedPaneLayout subclass which takes into
account tabOverlap.

**Overrides:**
- createLayoutManager

in class

BasicTabbedPaneUI

**Returns:**
- a layout manager object

**See Also:**
- BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

---

### Additional Sections

#### Class SynthTabbedPaneUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.synth.SynthTabbedPaneUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TabbedPaneUI
- - javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.synth.SynthTabbedPaneUI

javax.swing.plaf.TabbedPaneUI

- javax.swing.plaf.basic.BasicTabbedPaneUI
- - javax.swing.plaf.synth.SynthTabbedPaneUI

javax.swing.plaf.basic.BasicTabbedPaneUI

- javax.swing.plaf.synth.SynthTabbedPaneUI

javax.swing.plaf.synth.SynthTabbedPaneUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

,

SwingConstants

```java
public class
SynthTabbedPaneUI

extends
BasicTabbedPaneUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JTabbedPane

.

Looks up the

selectedTabPadInsets

property from the Style,
which represents additional insets for the selected tab.

**Since:** 1.7

public class

SynthTabbedPaneUI

extends

BasicTabbedPaneUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JTabbedPane

.

Looks up the

selectedTabPadInsets

property from the Style,
which represents additional insets for the selected tab.

Looks up the

selectedTabPadInsets

property from the Style,
which represents additional insets for the selected tab.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabbedPaneLayout

,

BasicTabbedPaneUI.TabSelectionHandler

=========== FIELD SUMMARY ===========

- Field Summary

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

Constructor

Description

SynthTabbedPaneUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

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

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

getBaselineOffset

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

getTabLabelShiftX

,

getTabLabelShiftY

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

uninstallUI

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

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabbedPaneLayout

,

BasicTabbedPaneUI.TabSelectionHandler

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTabbedPaneUI

BasicTabbedPaneUI.FocusHandler

,

BasicTabbedPaneUI.MouseHandler

,

BasicTabbedPaneUI.PropertyChangeHandler

,

BasicTabbedPaneUI.TabbedPaneLayout

,

BasicTabbedPaneUI.TabSelectionHandler

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicTabbedPaneUI

Field Summary

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

Constructor

Description

SynthTabbedPaneUI

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

static

ComponentUI

createUI

​(

JComponent

c)

Creates a new UI object for the given component.

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

void

update

​(

Graphics

g,

JComponent

c)

Notifies this UI delegate to repaint the specified component.

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

getBaselineOffset

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

getTabLabelShiftX

,

getTabLabelShiftY

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

uninstallUI

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

Invoked by

installUI

to create
a layout manager object to manage
the

JTabbedPane

.

Creates a mouse listener.

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

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

getBaselineOffset

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

getTabLabelShiftX

,

getTabLabelShiftY

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

uninstallUI

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

- SynthTabbedPaneUI

```java
public SynthTabbedPaneUI()
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

Creates a new UI object for the given component.

**Parameters:** c

- component to create UI object for
**Returns:** the UI object

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

Overridden to keep track of whether the selected tab is also pressed.

**Overrides:** createMouseListener

in class

BasicTabbedPaneUI
**Returns:** a mouse listener

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

Overridden to create a TabbedPaneLayout subclass which takes into
account tabOverlap.

**Overrides:** createLayoutManager

in class

BasicTabbedPaneUI
**Returns:** a layout manager object
**See Also:** BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

Constructor Detail

- SynthTabbedPaneUI

```java
public SynthTabbedPaneUI()
```

---

#### Constructor Detail

SynthTabbedPaneUI

```java
public SynthTabbedPaneUI()
```

---

#### SynthTabbedPaneUI

public SynthTabbedPaneUI()

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

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

Overridden to keep track of whether the selected tab is also pressed.

**Overrides:** createMouseListener

in class

BasicTabbedPaneUI
**Returns:** a mouse listener

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

Overridden to create a TabbedPaneLayout subclass which takes into
account tabOverlap.

**Overrides:** createLayoutManager

in class

BasicTabbedPaneUI
**Returns:** a layout manager object
**See Also:** BasicTabbedPaneUI.TabbedPaneLayout

,

JTabbedPane.getTabLayoutPolicy()

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

createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a mouse listener.

Overridden to keep track of whether the selected tab is also pressed.

**Overrides:** createMouseListener

in class

BasicTabbedPaneUI
**Returns:** a mouse listener

---

#### createMouseListener

protected

MouseListener

createMouseListener()

Creates a mouse listener.

Overridden to keep track of whether the selected tab is also pressed.

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

Overridden to create a TabbedPaneLayout subclass which takes into
account tabOverlap.

**Overrides:** createLayoutManager

in class

BasicTabbedPaneUI
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

Overridden to create a TabbedPaneLayout subclass which takes into
account tabOverlap.

---

