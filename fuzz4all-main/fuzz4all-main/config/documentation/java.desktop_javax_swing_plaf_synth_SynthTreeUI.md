# Class SynthTreeUI

**Source:** `java.desktop\javax\swing\plaf\synth\SynthTreeUI.html`

### Class Description

```java
public class
SynthTreeUI

extends
BasicTreeUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JTree

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

#### public SynthTreeUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Creates a new UI object for the given component.

**Parameters:**
- x

- component to create UI object for

**Returns:**
- the UI object

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

### Additional Sections

#### Class SynthTreeUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.synth.SynthTreeUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.synth.SynthTreeUI

javax.swing.plaf.TreeUI

- javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.synth.SynthTreeUI

javax.swing.plaf.basic.BasicTreeUI

- javax.swing.plaf.synth.SynthTreeUI

javax.swing.plaf.synth.SynthTreeUI

**All Implemented Interfaces:** PropertyChangeListener

,

EventListener

,

SynthConstants

,

SynthUI

```java
public class
SynthTreeUI

extends
BasicTreeUI

implements
PropertyChangeListener
,
SynthUI
```

Provides the Synth L&F UI delegate for

JTree

.

**Since:** 1.7

public class

SynthTreeUI

extends

BasicTreeUI

implements

PropertyChangeListener

,

SynthUI

Provides the Synth L&F UI delegate for

JTree

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTreeUI

BasicTreeUI.CellEditorHandler

,

BasicTreeUI.ComponentHandler

,

BasicTreeUI.FocusHandler

,

BasicTreeUI.KeyHandler

,

BasicTreeUI.MouseHandler

,

BasicTreeUI.MouseInputHandler

,

BasicTreeUI.NodeDimensionsHandler

,

BasicTreeUI.PropertyChangeHandler

,

BasicTreeUI.SelectionModelPropertyChangeHandler

,

BasicTreeUI.TreeCancelEditingAction

,

BasicTreeUI.TreeExpansionHandler

,

BasicTreeUI.TreeHomeAction

,

BasicTreeUI.TreeIncrementAction

,

BasicTreeUI.TreeModelHandler

,

BasicTreeUI.TreePageAction

,

BasicTreeUI.TreeSelectionHandler

,

BasicTreeUI.TreeToggleAction

,

BasicTreeUI.TreeTraverseAction

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicTreeUI

cellEditor

,

collapsedIcon

,

createdCellEditor

,

createdRenderer

,

currentCellRenderer

,

depthOffset

,

drawingCache

,

editingComponent

,

editingPath

,

editingRow

,

editorHasDifferentSize

,

expandedIcon

,

largeModel

,

lastSelectedRow

,

leftChildIndent

,

nodeDimensions

,

preferredMinSize

,

preferredSize

,

rendererPane

,

rightChildIndent

,

stopEditingInCompleteEditing

,

totalChildIndent

,

tree

,

treeModel

,

treeSelectionModel

,

treeState

,

validCachedPreferredSize

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

SynthTreeUI

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

BasicTreeUI

cancelEditing

,

checkForClickInExpandControl

,

completeEditing

,

completeEditing

,

completeUIInstall

,

completeUIUninstall

,

configureLayoutCache

,

createCellEditorListener

,

createCellRendererPane

,

createComponentListener

,

createDefaultCellEditor

,

createDefaultCellRenderer

,

createFocusListener

,

createKeyListener

,

createLayoutCache

,

createMouseListener

,

createNodeDimensions

,

createPropertyChangeListener

,

createSelectionModelPropertyChangeListener

,

createTreeExpansionListener

,

createTreeModelListener

,

createTreeSelectionListener

,

drawCentered

,

drawDashedHorizontalLine

,

drawDashedVerticalLine

,

ensureRowsAreVisible

,

getBaseline

,

getBaselineResizeBehavior

,

getCellEditor

,

getCellRenderer

,

getClosestPathForLocation

,

getCollapsedIcon

,

getDropLineRect

,

getEditingPath

,

getExpandedIcon

,

getHashColor

,

getHorizontalLegBuffer

,

getLastChildPath

,

getLeadSelectionRow

,

getLeftChildIndent

,

getMaximumSize

,

getMinimumSize

,

getModel

,

getPathBounds

,

getPathForRow

,

getPreferredMinSize

,

getPreferredSize

,

getPreferredSize

,

getRightChildIndent

,

getRowCount

,

getRowForPath

,

getRowHeight

,

getRowX

,

getSelectionModel

,

getShowsRootHandles

,

getVerticalLegBuffer

,

handleExpandControlClick

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isDropLine

,

isEditable

,

isEditing

,

isLargeModel

,

isLeaf

,

isLocationInExpandControl

,

isMultiSelectEvent

,

isRootVisible

,

isToggleEvent

,

isToggleSelectionEvent

,

paintDropLine

,

paintExpandControl

,

paintHorizontalLine

,

paintHorizontalPartOfLeg

,

paintRow

,

paintVerticalLine

,

paintVerticalPartOfLeg

,

pathWasCollapsed

,

pathWasExpanded

,

prepareForUIInstall

,

prepareForUIUninstall

,

selectPathForEvent

,

setCellEditor

,

setCellRenderer

,

setCollapsedIcon

,

setEditable

,

setExpandedIcon

,

setHashColor

,

setLargeModel

,

setLeftChildIndent

,

setModel

,

setPreferredMinSize

,

setRightChildIndent

,

setRootVisible

,

setRowHeight

,

setSelectionModel

,

setShowsRootHandles

,

shouldPaintExpandControl

,

startEditing

,

startEditingAtPath

,

stopEditing

,

toggleExpandState

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateCachedPreferredSize

,

updateCellEditor

,

updateDepthOffset

,

updateExpandedDescendants

,

updateLayoutCacheExpandedNodes

,

updateLeadSelectionRow

,

updateRenderer

,

updateSize

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

BasicTreeUI

BasicTreeUI.CellEditorHandler

,

BasicTreeUI.ComponentHandler

,

BasicTreeUI.FocusHandler

,

BasicTreeUI.KeyHandler

,

BasicTreeUI.MouseHandler

,

BasicTreeUI.MouseInputHandler

,

BasicTreeUI.NodeDimensionsHandler

,

BasicTreeUI.PropertyChangeHandler

,

BasicTreeUI.SelectionModelPropertyChangeHandler

,

BasicTreeUI.TreeCancelEditingAction

,

BasicTreeUI.TreeExpansionHandler

,

BasicTreeUI.TreeHomeAction

,

BasicTreeUI.TreeIncrementAction

,

BasicTreeUI.TreeModelHandler

,

BasicTreeUI.TreePageAction

,

BasicTreeUI.TreeSelectionHandler

,

BasicTreeUI.TreeToggleAction

,

BasicTreeUI.TreeTraverseAction

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicTreeUI

BasicTreeUI.CellEditorHandler

,

BasicTreeUI.ComponentHandler

,

BasicTreeUI.FocusHandler

,

BasicTreeUI.KeyHandler

,

BasicTreeUI.MouseHandler

,

BasicTreeUI.MouseInputHandler

,

BasicTreeUI.NodeDimensionsHandler

,

BasicTreeUI.PropertyChangeHandler

,

BasicTreeUI.SelectionModelPropertyChangeHandler

,

BasicTreeUI.TreeCancelEditingAction

,

BasicTreeUI.TreeExpansionHandler

,

BasicTreeUI.TreeHomeAction

,

BasicTreeUI.TreeIncrementAction

,

BasicTreeUI.TreeModelHandler

,

BasicTreeUI.TreePageAction

,

BasicTreeUI.TreeSelectionHandler

,

BasicTreeUI.TreeToggleAction

,

BasicTreeUI.TreeTraverseAction

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicTreeUI

Field Summary

- Fields declared in class javax.swing.plaf.basic.

BasicTreeUI

cellEditor

,

collapsedIcon

,

createdCellEditor

,

createdRenderer

,

currentCellRenderer

,

depthOffset

,

drawingCache

,

editingComponent

,

editingPath

,

editingRow

,

editorHasDifferentSize

,

expandedIcon

,

largeModel

,

lastSelectedRow

,

leftChildIndent

,

nodeDimensions

,

preferredMinSize

,

preferredSize

,

rendererPane

,

rightChildIndent

,

stopEditingInCompleteEditing

,

totalChildIndent

,

tree

,

treeModel

,

treeSelectionModel

,

treeState

,

validCachedPreferredSize

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

BasicTreeUI

cellEditor

,

collapsedIcon

,

createdCellEditor

,

createdRenderer

,

currentCellRenderer

,

depthOffset

,

drawingCache

,

editingComponent

,

editingPath

,

editingRow

,

editorHasDifferentSize

,

expandedIcon

,

largeModel

,

lastSelectedRow

,

leftChildIndent

,

nodeDimensions

,

preferredMinSize

,

preferredSize

,

rendererPane

,

rightChildIndent

,

stopEditingInCompleteEditing

,

totalChildIndent

,

tree

,

treeModel

,

treeSelectionModel

,

treeState

,

validCachedPreferredSize

---

#### Fields declared in class javax.swing.plaf.basic. BasicTreeUI

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

SynthTreeUI

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

BasicTreeUI

cancelEditing

,

checkForClickInExpandControl

,

completeEditing

,

completeEditing

,

completeUIInstall

,

completeUIUninstall

,

configureLayoutCache

,

createCellEditorListener

,

createCellRendererPane

,

createComponentListener

,

createDefaultCellEditor

,

createDefaultCellRenderer

,

createFocusListener

,

createKeyListener

,

createLayoutCache

,

createMouseListener

,

createNodeDimensions

,

createPropertyChangeListener

,

createSelectionModelPropertyChangeListener

,

createTreeExpansionListener

,

createTreeModelListener

,

createTreeSelectionListener

,

drawCentered

,

drawDashedHorizontalLine

,

drawDashedVerticalLine

,

ensureRowsAreVisible

,

getBaseline

,

getBaselineResizeBehavior

,

getCellEditor

,

getCellRenderer

,

getClosestPathForLocation

,

getCollapsedIcon

,

getDropLineRect

,

getEditingPath

,

getExpandedIcon

,

getHashColor

,

getHorizontalLegBuffer

,

getLastChildPath

,

getLeadSelectionRow

,

getLeftChildIndent

,

getMaximumSize

,

getMinimumSize

,

getModel

,

getPathBounds

,

getPathForRow

,

getPreferredMinSize

,

getPreferredSize

,

getPreferredSize

,

getRightChildIndent

,

getRowCount

,

getRowForPath

,

getRowHeight

,

getRowX

,

getSelectionModel

,

getShowsRootHandles

,

getVerticalLegBuffer

,

handleExpandControlClick

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isDropLine

,

isEditable

,

isEditing

,

isLargeModel

,

isLeaf

,

isLocationInExpandControl

,

isMultiSelectEvent

,

isRootVisible

,

isToggleEvent

,

isToggleSelectionEvent

,

paintDropLine

,

paintExpandControl

,

paintHorizontalLine

,

paintHorizontalPartOfLeg

,

paintRow

,

paintVerticalLine

,

paintVerticalPartOfLeg

,

pathWasCollapsed

,

pathWasExpanded

,

prepareForUIInstall

,

prepareForUIUninstall

,

selectPathForEvent

,

setCellEditor

,

setCellRenderer

,

setCollapsedIcon

,

setEditable

,

setExpandedIcon

,

setHashColor

,

setLargeModel

,

setLeftChildIndent

,

setModel

,

setPreferredMinSize

,

setRightChildIndent

,

setRootVisible

,

setRowHeight

,

setSelectionModel

,

setShowsRootHandles

,

shouldPaintExpandControl

,

startEditing

,

startEditingAtPath

,

stopEditing

,

toggleExpandState

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateCachedPreferredSize

,

updateCellEditor

,

updateDepthOffset

,

updateExpandedDescendants

,

updateLayoutCacheExpandedNodes

,

updateLeadSelectionRow

,

updateRenderer

,

updateSize

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

Creates a new UI object for the given component.

Paints the specified component according to the Look and Feel.

Paints the specified component.

Notifies this UI delegate to repaint the specified component.

Methods declared in class javax.swing.plaf.basic.

BasicTreeUI

cancelEditing

,

checkForClickInExpandControl

,

completeEditing

,

completeEditing

,

completeUIInstall

,

completeUIUninstall

,

configureLayoutCache

,

createCellEditorListener

,

createCellRendererPane

,

createComponentListener

,

createDefaultCellEditor

,

createDefaultCellRenderer

,

createFocusListener

,

createKeyListener

,

createLayoutCache

,

createMouseListener

,

createNodeDimensions

,

createPropertyChangeListener

,

createSelectionModelPropertyChangeListener

,

createTreeExpansionListener

,

createTreeModelListener

,

createTreeSelectionListener

,

drawCentered

,

drawDashedHorizontalLine

,

drawDashedVerticalLine

,

ensureRowsAreVisible

,

getBaseline

,

getBaselineResizeBehavior

,

getCellEditor

,

getCellRenderer

,

getClosestPathForLocation

,

getCollapsedIcon

,

getDropLineRect

,

getEditingPath

,

getExpandedIcon

,

getHashColor

,

getHorizontalLegBuffer

,

getLastChildPath

,

getLeadSelectionRow

,

getLeftChildIndent

,

getMaximumSize

,

getMinimumSize

,

getModel

,

getPathBounds

,

getPathForRow

,

getPreferredMinSize

,

getPreferredSize

,

getPreferredSize

,

getRightChildIndent

,

getRowCount

,

getRowForPath

,

getRowHeight

,

getRowX

,

getSelectionModel

,

getShowsRootHandles

,

getVerticalLegBuffer

,

handleExpandControlClick

,

installComponents

,

installDefaults

,

installKeyboardActions

,

installListeners

,

isDropLine

,

isEditable

,

isEditing

,

isLargeModel

,

isLeaf

,

isLocationInExpandControl

,

isMultiSelectEvent

,

isRootVisible

,

isToggleEvent

,

isToggleSelectionEvent

,

paintDropLine

,

paintExpandControl

,

paintHorizontalLine

,

paintHorizontalPartOfLeg

,

paintRow

,

paintVerticalLine

,

paintVerticalPartOfLeg

,

pathWasCollapsed

,

pathWasExpanded

,

prepareForUIInstall

,

prepareForUIUninstall

,

selectPathForEvent

,

setCellEditor

,

setCellRenderer

,

setCollapsedIcon

,

setEditable

,

setExpandedIcon

,

setHashColor

,

setLargeModel

,

setLeftChildIndent

,

setModel

,

setPreferredMinSize

,

setRightChildIndent

,

setRootVisible

,

setRowHeight

,

setSelectionModel

,

setShowsRootHandles

,

shouldPaintExpandControl

,

startEditing

,

startEditingAtPath

,

stopEditing

,

toggleExpandState

,

uninstallComponents

,

uninstallDefaults

,

uninstallKeyboardActions

,

uninstallListeners

,

updateCachedPreferredSize

,

updateCellEditor

,

updateDepthOffset

,

updateExpandedDescendants

,

updateLayoutCacheExpandedNodes

,

updateLeadSelectionRow

,

updateRenderer

,

updateSize

---

#### Methods declared in class javax.swing.plaf.basic. BasicTreeUI

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

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

- SynthTreeUI

```java
public SynthTreeUI()
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

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

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

Constructor Detail

- SynthTreeUI

```java
public SynthTreeUI()
```

---

#### Constructor Detail

SynthTreeUI

```java
public SynthTreeUI()
```

---

#### SynthTreeUI

public SynthTreeUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

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

Creates a new UI object for the given component.

**Parameters:** x

- component to create UI object for
**Returns:** the UI object

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Creates a new UI object for the given component.

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

---

