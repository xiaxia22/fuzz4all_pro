# Class MetalTreeUI

**Source:** `java.desktop\javax\swing\plaf\metal\MetalTreeUI.html`

### Class Description

```java
public class
MetalTreeUI

extends
BasicTreeUI
```

The metal look and feel implementation of

TreeUI

.

MetalTreeUI

allows for configuring how to
visually render the spacing and delineation between nodes. The following
hints are supported:

Descriptions of supported hints: Angled, Horizontal, and None

Hint

Description

Angled

A line is drawn connecting the child to the parent. For handling of
the root node refer to

JTree.setRootVisible(boolean)

and

JTree.setShowsRootHandles(boolean)

.

Horizontal

A horizontal line is drawn dividing the children of the root node.

None

Do not draw any visual indication between nodes.

As it is typically impractical to obtain the

TreeUI

from
the

JTree

and cast to an instance of

MetalTreeUI

you enable this property via the client property

JTree.lineStyle

. For example, to switch to

Horizontal

style you would do:

tree.putClientProperty("JTree.lineStyle", "Horizontal");

The default is

Angled

.

---

### Field Details

*No entries found.*

### Constructor Details

#### public MetalTreeUI()

Constructs the

MetalTreeUI

.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs the

MetalTreeUI

.

**Parameters:**
- x

- a component

**Returns:**
- the instance of the

MetalTreeUI

---

#### protected void decodeLineStyle​(
Object
lineStyleFlag)

Converts between the string passed into the client property
and the internal representation (currently and int)

**Parameters:**
- lineStyleFlag

- a flag

---

#### protected boolean isLocationInExpandControl​(int row,
int rowLevel,
int mouseX,
int mouseY)

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

**Parameters:**
- row

- a row
- rowLevel

- a row level
- mouseX

- X coordinate
- mouseY

- Y coordinate

**Returns:**
- true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

---

#### protected void paintHorizontalSeparators​(
Graphics
g,

JComponent
c)

Paints the horizontal separators.

**Parameters:**
- g

- an instance of

Graphics
- c

- a component

---

### Additional Sections

#### Class MetalTreeUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.metal.MetalTreeUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.metal.MetalTreeUI

javax.swing.plaf.TreeUI

- javax.swing.plaf.basic.BasicTreeUI
- - javax.swing.plaf.metal.MetalTreeUI

javax.swing.plaf.basic.BasicTreeUI

- javax.swing.plaf.metal.MetalTreeUI

javax.swing.plaf.metal.MetalTreeUI

```java
public class
MetalTreeUI

extends
BasicTreeUI
```

The metal look and feel implementation of

TreeUI

.

MetalTreeUI

allows for configuring how to
visually render the spacing and delineation between nodes. The following
hints are supported:

Descriptions of supported hints: Angled, Horizontal, and None

Hint

Description

Angled

A line is drawn connecting the child to the parent. For handling of
the root node refer to

JTree.setRootVisible(boolean)

and

JTree.setShowsRootHandles(boolean)

.

Horizontal

A horizontal line is drawn dividing the children of the root node.

None

Do not draw any visual indication between nodes.

As it is typically impractical to obtain the

TreeUI

from
the

JTree

and cast to an instance of

MetalTreeUI

you enable this property via the client property

JTree.lineStyle

. For example, to switch to

Horizontal

style you would do:

tree.putClientProperty("JTree.lineStyle", "Horizontal");

The default is

Angled

.

public class

MetalTreeUI

extends

BasicTreeUI

The metal look and feel implementation of

TreeUI

.

MetalTreeUI

allows for configuring how to
visually render the spacing and delineation between nodes. The following
hints are supported:

Descriptions of supported hints: Angled, Horizontal, and None

Hint

Description

Angled

A line is drawn connecting the child to the parent. For handling of
the root node refer to

JTree.setRootVisible(boolean)

and

JTree.setShowsRootHandles(boolean)

.

Horizontal

A horizontal line is drawn dividing the children of the root node.

None

Do not draw any visual indication between nodes.

As it is typically impractical to obtain the

TreeUI

from
the

JTree

and cast to an instance of

MetalTreeUI

you enable this property via the client property

JTree.lineStyle

. For example, to switch to

Horizontal

style you would do:

tree.putClientProperty("JTree.lineStyle", "Horizontal");

The default is

Angled

.

MetalTreeUI

allows for configuring how to
visually render the spacing and delineation between nodes. The following
hints are supported:

Descriptions of supported hints: Angled, Horizontal, and None

Hint

Description

Angled

A line is drawn connecting the child to the parent. For handling of
the root node refer to

JTree.setRootVisible(boolean)

and

JTree.setShowsRootHandles(boolean)

.

Horizontal

A horizontal line is drawn dividing the children of the root node.

None

Do not draw any visual indication between nodes.

As it is typically impractical to obtain the

TreeUI

from
the

JTree

and cast to an instance of

MetalTreeUI

you enable this property via the client property

JTree.lineStyle

. For example, to switch to

Horizontal

style you would do:

tree.putClientProperty("JTree.lineStyle", "Horizontal");

The default is

Angled

.

As it is typically impractical to obtain the

TreeUI

from
the

JTree

and cast to an instance of

MetalTreeUI

you enable this property via the client property

JTree.lineStyle

. For example, to switch to

Horizontal

style you would do:

tree.putClientProperty("JTree.lineStyle", "Horizontal");

The default is

Angled

.

The default is

Angled

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalTreeUI

()

Constructs the

MetalTreeUI

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

x)

Constructs the

MetalTreeUI

.

protected void

decodeLineStyle

​(

Object

lineStyleFlag)

Converts between the string passed into the client property
and the internal representation (currently and int)

protected boolean

isLocationInExpandControl

​(int row,
int rowLevel,
int mouseX,
int mouseY)

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

protected void

paintHorizontalSeparators

​(

Graphics

g,

JComponent

c)

Paints the horizontal separators.

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

Constructor Summary

Constructors

Constructor

Description

MetalTreeUI

()

Constructs the

MetalTreeUI

.

---

#### Constructor Summary

Constructs the

MetalTreeUI

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

x)

Constructs the

MetalTreeUI

.

protected void

decodeLineStyle

​(

Object

lineStyleFlag)

Converts between the string passed into the client property
and the internal representation (currently and int)

protected boolean

isLocationInExpandControl

​(int row,
int rowLevel,
int mouseX,
int mouseY)

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

protected void

paintHorizontalSeparators

​(

Graphics

g,

JComponent

c)

Paints the horizontal separators.

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

Constructs the

MetalTreeUI

.

Converts between the string passed into the client property
and the internal representation (currently and int)

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

Paints the horizontal separators.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalTreeUI

```java
public MetalTreeUI()
```

Constructs the

MetalTreeUI

.

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

Constructs the

MetalTreeUI

.

**Parameters:** x

- a component
**Returns:** the instance of the

MetalTreeUI

- decodeLineStyle

```java
protected void decodeLineStyle​(
Object
lineStyleFlag)
```

Converts between the string passed into the client property
and the internal representation (currently and int)

**Parameters:** lineStyleFlag

- a flag

- isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(int row,
int rowLevel,
int mouseX,
int mouseY)
```

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

**Parameters:** row

- a row
**Parameters:** rowLevel

- a row level
**Parameters:** mouseX

- X coordinate
**Parameters:** mouseY

- Y coordinate
**Returns:** true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

- paintHorizontalSeparators

```java
protected void paintHorizontalSeparators​(
Graphics
g,

JComponent
c)
```

Paints the horizontal separators.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component

Constructor Detail

- MetalTreeUI

```java
public MetalTreeUI()
```

Constructs the

MetalTreeUI

.

---

#### Constructor Detail

MetalTreeUI

```java
public MetalTreeUI()
```

Constructs the

MetalTreeUI

.

---

#### MetalTreeUI

public MetalTreeUI()

Constructs the

MetalTreeUI

.

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
x)
```

Constructs the

MetalTreeUI

.

**Parameters:** x

- a component
**Returns:** the instance of the

MetalTreeUI

- decodeLineStyle

```java
protected void decodeLineStyle​(
Object
lineStyleFlag)
```

Converts between the string passed into the client property
and the internal representation (currently and int)

**Parameters:** lineStyleFlag

- a flag

- isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(int row,
int rowLevel,
int mouseX,
int mouseY)
```

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

**Parameters:** row

- a row
**Parameters:** rowLevel

- a row level
**Parameters:** mouseX

- X coordinate
**Parameters:** mouseY

- Y coordinate
**Returns:** true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

- paintHorizontalSeparators

```java
protected void paintHorizontalSeparators​(
Graphics
g,

JComponent
c)
```

Paints the horizontal separators.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component

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

Constructs the

MetalTreeUI

.

**Parameters:** x

- a component
**Returns:** the instance of the

MetalTreeUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs the

MetalTreeUI

.

decodeLineStyle

```java
protected void decodeLineStyle​(
Object
lineStyleFlag)
```

Converts between the string passed into the client property
and the internal representation (currently and int)

**Parameters:** lineStyleFlag

- a flag

---

#### decodeLineStyle

protected void decodeLineStyle​(

Object

lineStyleFlag)

Converts between the string passed into the client property
and the internal representation (currently and int)

isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(int row,
int rowLevel,
int mouseX,
int mouseY)
```

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

**Parameters:** row

- a row
**Parameters:** rowLevel

- a row level
**Parameters:** mouseX

- X coordinate
**Parameters:** mouseY

- Y coordinate
**Returns:** true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

---

#### isLocationInExpandControl

protected boolean isLocationInExpandControl​(int row,
int rowLevel,
int mouseX,
int mouseY)

Returns

true

if a point with X coordinate

mouseX

and Y coordinate

mouseY

is in expanded control.

paintHorizontalSeparators

```java
protected void paintHorizontalSeparators​(
Graphics
g,

JComponent
c)
```

Paints the horizontal separators.

**Parameters:** g

- an instance of

Graphics
**Parameters:** c

- a component

---

#### paintHorizontalSeparators

protected void paintHorizontalSeparators​(

Graphics

g,

JComponent

c)

Paints the horizontal separators.

---

