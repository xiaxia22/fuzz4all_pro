# Class BasicTreeUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicTreeUI.html`

### Class Description

```java
public class
BasicTreeUI

extends
TreeUI
```

The basic L&F for a hierarchical data structure.

**Direct Known Subclasses:** MetalTreeUI

,

SynthTreeUI

---

### Field Details

#### protected transient
Icon
collapsedIcon

The collapsed icon.

---

#### protected transient
Icon
expandedIcon

The expanded icon.

---

#### protected int leftChildIndent

Distance between left margin and where vertical dashes will be
drawn.

---

#### protected int rightChildIndent

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

---

#### protected int totalChildIndent

Total distance that will be indented. The sum of leftChildIndent
and rightChildIndent.

---

#### protected
Dimension
preferredMinSize

Minimum preferred size.

---

#### protected int lastSelectedRow

Index of the row that was last selected.

---

#### protected
JTree
tree

Component that we're going to be drawing into.

---

#### protected transient
TreeCellRenderer
currentCellRenderer

Renderer that is being used to do the actual cell drawing.

---

#### protected boolean createdRenderer

Set to true if the renderer that is currently in the tree was
created by this instance.

---

#### protected transient
TreeCellEditor
cellEditor

Editor for the tree.

---

#### protected boolean createdCellEditor

Set to true if editor that is currently in the tree was
created by this instance.

---

#### protected boolean stopEditingInCompleteEditing

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

---

#### protected
CellRendererPane
rendererPane

Used to paint the TreeCellRenderer.

---

#### protected
Dimension
preferredSize

Size needed to completely display all the nodes.

---

#### protected boolean validCachedPreferredSize

Is the preferredSize valid?

---

#### protected
AbstractLayoutCache
treeState

Object responsible for handling sizing and expanded issues.

---

#### protected
Hashtable
<
TreePath
,​
Boolean
> drawingCache

Used for minimizing the drawing of vertical lines.

---

#### protected boolean largeModel

True if doing optimizations for a largeModel. Subclasses that
don't support this may wish to override createLayoutCache to not
return a FixedHeightLayoutCache instance.

---

#### protected
AbstractLayoutCache.NodeDimensions
nodeDimensions

Reponsible for telling the TreeState the size needed for a node.

---

#### protected
TreeModel
treeModel

Used to determine what to display.

---

#### protected
TreeSelectionModel
treeSelectionModel

Model maintaining the selection.

---

#### protected int depthOffset

How much the depth should be offset to properly calculate
x locations. This is based on whether or not the root is visible,
and if the root handles are visible.

---

#### protected
Component
editingComponent

When editing, this will be the Component that is doing the actual
editing.

---

#### protected
TreePath
editingPath

Path that is being edited.

---

#### protected int editingRow

Row that is being edited. Should only be referenced if
editingComponent is not null.

---

#### protected boolean editorHasDifferentSize

Set to true if the editor has a different size than the renderer.

---

### Constructor Details

#### public BasicTreeUI()

Constructs a new instance of

BasicTreeUI

.

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
x)

Constructs a new instance of

BasicTreeUI

.

**Parameters:**
- x

- a component

**Returns:**
- a new instance of

BasicTreeUI

---

#### protected
Color
getHashColor()

Returns the hash color.

**Returns:**
- the hash color

---

#### protected void setHashColor​(
Color
color)

Sets the hash color.

**Parameters:**
- color

- the hash color

---

#### public void setLeftChildIndent​(int newAmount)

Sets the left child indent.

**Parameters:**
- newAmount

- the left child indent

---

#### public int getLeftChildIndent()

Returns the left child indent.

**Returns:**
- the left child indent

---

#### public void setRightChildIndent​(int newAmount)

Sets the right child indent.

**Parameters:**
- newAmount

- the right child indent

---

#### public int getRightChildIndent()

Returns the right child indent.

**Returns:**
- the right child indent

---

#### public void setExpandedIcon​(
Icon
newG)

Sets the expanded icon.

**Parameters:**
- newG

- the expanded icon

---

#### public
Icon
getExpandedIcon()

Returns the expanded icon.

**Returns:**
- the expanded icon

---

#### public void setCollapsedIcon​(
Icon
newG)

Sets the collapsed icon.

**Parameters:**
- newG

- the collapsed icon

---

#### public
Icon
getCollapsedIcon()

Returns the collapsed icon.

**Returns:**
- the collapsed icon

---

#### protected void setLargeModel​(boolean largeModel)

Updates the componentListener, if necessary.

**Parameters:**
- largeModel

- the new value

---

#### protected boolean isLargeModel()

Returns

true

if large model is set.

**Returns:**
- true

if large model is set

---

#### protected void setRowHeight​(int rowHeight)

Sets the row height, this is forwarded to the treeState.

**Parameters:**
- rowHeight

- the row height

---

#### protected int getRowHeight()

Returns the row height.

**Returns:**
- the row height

---

#### protected void setCellRenderer​(
TreeCellRenderer
tcr)

Sets the

TreeCellRenderer

to

tcr

. This invokes

updateRenderer

.

**Parameters:**
- tcr

- the new value

---

#### protected
TreeCellRenderer
getCellRenderer()

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

**Returns:**
- an instance of

TreeCellRenderer

---

#### protected void setModel​(
TreeModel
model)

Sets the

TreeModel

.

**Parameters:**
- model

- the new value

---

#### protected
TreeModel
getModel()

Returns the tree model.

**Returns:**
- the tree model

---

#### protected void setRootVisible​(boolean newValue)

Sets the root to being visible.

**Parameters:**
- newValue

- the new value

---

#### protected boolean isRootVisible()

Returns

true

if the tree root is visible.

**Returns:**
- true

if the tree root is visible

---

#### protected void setShowsRootHandles​(boolean newValue)

Determines whether the node handles are to be displayed.

**Parameters:**
- newValue

- the new value

---

#### protected boolean getShowsRootHandles()

Returns

true

if the root handles are to be displayed.

**Returns:**
- true

if the root handles are to be displayed

---

#### protected void setCellEditor​(
TreeCellEditor
editor)

Sets the cell editor.

**Parameters:**
- editor

- the new cell editor

---

#### protected
TreeCellEditor
getCellEditor()

Returns an instance of

TreeCellEditor

.

**Returns:**
- an instance of

TreeCellEditor

---

#### protected void setEditable​(boolean newValue)

Configures the receiver to allow, or not allow, editing.

**Parameters:**
- newValue

- the new value

---

#### protected boolean isEditable()

Returns

true

if the tree is editable.

**Returns:**
- true

if the tree is editable

---

#### protected void setSelectionModel​(
TreeSelectionModel
newLSM)

Resets the selection model. The appropriate listener are installed
on the model.

**Parameters:**
- newLSM

- new selection model

---

#### protected
TreeSelectionModel
getSelectionModel()

Returns the tree selection model.

**Returns:**
- the tree selection model

---

#### public
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Specified by:**
- getPathBounds

in class

TreeUI

**Parameters:**
- tree

- the

JTree

for

path
- path

- the

TreePath

identifying the node

**Returns:**
- the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

---

#### public
TreePath
getPathForRow​(
JTree
tree,
int row)

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:**
- getPathForRow

in class

TreeUI

**Parameters:**
- tree

- a

JTree

object
- row

- an integer specifying a row

**Returns:**
- the

path

for

row

or

null

if

row

is not visible

---

#### public int getRowForPath​(
JTree
tree,

TreePath
path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:**
- getRowForPath

in class

TreeUI

**Parameters:**
- tree

- the

JTree

for

path
- path

- the

TreePath

object to look in

**Returns:**
- an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

---

#### public int getRowCount​(
JTree
tree)

Returns the number of rows that are being displayed.

**Specified by:**
- getRowCount

in class

TreeUI

**Parameters:**
- tree

- the

JTree

for which to count rows

**Returns:**
- an integer specifying the number of row being displayed

---

#### public
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:**
- getClosestPathForLocation

in class

TreeUI

**Parameters:**
- tree

- a

JTree

object
- x

- an integer giving the number of pixels horizontally from the
left edge of the display area
- y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin

**Returns:**
- the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

---

#### public boolean isEditing​(
JTree
tree)

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Specified by:**
- isEditing

in class

TreeUI

**Parameters:**
- tree

- a

JTree

object

**Returns:**
- true if

tree

is being edited

---

#### public boolean stopEditing​(
JTree
tree)

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Specified by:**
- stopEditing

in class

TreeUI

**Parameters:**
- tree

- a

JTree

object

**Returns:**
- true if the editor allows the editing session to stop

---

#### public void cancelEditing​(
JTree
tree)

Cancels the current editing session.

**Specified by:**
- cancelEditing

in class

TreeUI

**Parameters:**
- tree

- a

JTree

object

---

#### public void startEditingAtPath​(
JTree
tree,

TreePath
path)

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Specified by:**
- startEditingAtPath

in class

TreeUI

**Parameters:**
- tree

- the

JTree

being edited
- path

- the

TreePath

to be edited

---

#### public
TreePath
getEditingPath​(
JTree
tree)

Returns the path to the element that is being edited.

**Specified by:**
- getEditingPath

in class

TreeUI

**Parameters:**
- tree

- the

JTree

for which to return a path

**Returns:**
- a

TreePath

containing the path to

tree

---

#### protected void prepareForUIInstall()

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

---

#### protected void completeUIInstall()

Invoked from installUI after all the defaults/listeners have been
installed.

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void installKeyboardActions()

Registers keyboard actions.

---

#### protected void installComponents()

Intalls the subcomponents of the tree, which is the renderer pane.

---

#### protected
AbstractLayoutCache.NodeDimensions
createNodeDimensions()

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

**Returns:**
- an instance of

NodeDimensions

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a listener that is responsible that updates the UI based on
how the tree changes.

**Returns:**
- an instance of the

PropertyChangeListener

---

#### protected
MouseListener
createMouseListener()

Creates the listener responsible for updating the selection based on
mouse events.

**Returns:**
- an instance of the

MouseListener

---

#### protected
FocusListener
createFocusListener()

Creates a listener that is responsible for updating the display
when focus is lost/gained.

**Returns:**
- an instance of the

FocusListener

---

#### protected
KeyListener
createKeyListener()

Creates the listener responsible for getting key events from
the tree.

**Returns:**
- an instance of the

KeyListener

---

#### protected
PropertyChangeListener
createSelectionModelPropertyChangeListener()

Creates the listener responsible for getting property change
events from the selection model.

**Returns:**
- an instance of the

PropertyChangeListener

---

#### protected
TreeSelectionListener
createTreeSelectionListener()

Creates the listener that updates the display based on selection change
methods.

**Returns:**
- an instance of the

TreeSelectionListener

---

#### protected
CellEditorListener
createCellEditorListener()

Creates a listener to handle events from the current editor.

**Returns:**
- an instance of the

CellEditorListener

---

#### protected
ComponentListener
createComponentListener()

Creates and returns a new ComponentHandler. This is used for
the large model to mark the validCachedPreferredSize as invalid
when the component moves.

**Returns:**
- an instance of the

ComponentListener

---

#### protected
TreeExpansionListener
createTreeExpansionListener()

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

**Returns:**
- an instance of the

TreeExpansionListener

---

#### protected
AbstractLayoutCache
createLayoutCache()

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

**Returns:**
- the object responsible for managing what is expanded

---

#### protected
CellRendererPane
createCellRendererPane()

Returns the renderer pane that renderer components are placed in.

**Returns:**
- an instance of the

CellRendererPane

---

#### protected
TreeCellEditor
createDefaultCellEditor()

Creates a default cell editor.

**Returns:**
- a default cell editor

---

#### protected
TreeCellRenderer
createDefaultCellRenderer()

Returns the default cell renderer that is used to do the
stamping of each node.

**Returns:**
- an instance of

TreeCellRenderer

---

#### protected
TreeModelListener
createTreeModelListener()

Returns a listener that can update the tree when the model changes.

**Returns:**
- an instance of the

TreeModelListener

.

---

#### protected void prepareForUIUninstall()

Invoked before unstallation of UI.

---

#### protected void completeUIUninstall()

Uninstalls UI.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### protected void uninstallComponents()

Uninstalls the renderer pane.

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

#### protected boolean isDropLine​(
JTree.DropLocation
loc)

Tells if a

DropLocation

should be indicated by a line between
nodes. This is meant for

javax.swing.DropMode.INSERT

and

javax.swing.DropMode.ON_OR_INSERT

drop modes.

**Parameters:**
- loc

- a

DropLocation

**Returns:**
- true

if the drop location should be shown as a line

**Since:**
- 1.7

---

#### protected void paintDropLine​(
Graphics
g)

Paints the drop line.

**Parameters:**
- g

-

Graphics

object to draw on

**Since:**
- 1.7

---

#### protected
Rectangle
getDropLineRect​(
JTree.DropLocation
loc)

Returns a unbounding box for the drop line.

**Parameters:**
- loc

- a

DropLocation

**Returns:**
- bounding box for the drop line

**Since:**
- 1.7

---

#### protected void paintHorizontalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the horizontal part of the leg. The receiver should
NOT modify

clipBounds

, or

insets

.

NOTE:

parentRow

can be -1 if the root is not visible.

**Parameters:**
- g

- a graphics context
- clipBounds

- a clipped rectangle
- insets

- insets
- bounds

- a bounding rectangle
- path

- a tree path
- row

- a row
- isExpanded

-

true

if the path is expanded
- hasBeenExpanded

-

true

if the path has been expanded
- isLeaf

-

true

if the path is leaf

---

#### protected void paintVerticalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

TreePath
path)

Paints the vertical part of the leg. The receiver should
NOT modify

clipBounds

,

insets

.

**Parameters:**
- g

- a graphics context
- clipBounds

- a clipped rectangle
- insets

- insets
- path

- a tree path

---

#### protected void paintExpandControl​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the expand (toggle) part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:**
- g

- a graphics context
- clipBounds

- a clipped rectangle
- insets

- insets
- bounds

- a bounding rectangle
- path

- a tree path
- row

- a row
- isExpanded

-

true

if the path is expanded
- hasBeenExpanded

-

true

if the path has been expanded
- isLeaf

-

true

if the row is leaf

---

#### protected void paintRow​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the renderer part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:**
- g

- a graphics context
- clipBounds

- a clipped rectangle
- insets

- insets
- bounds

- a bounding rectangle
- path

- a tree path
- row

- a row
- isExpanded

-

true

if the path is expanded
- hasBeenExpanded

-

true

if the path has been expanded
- isLeaf

-

true

if the path is leaf

---

#### protected boolean shouldPaintExpandControl​(
TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

**Parameters:**
- path

- a tree path
- row

- a row
- isExpanded

-

true

if the path is expanded
- hasBeenExpanded

-

true

if the path has been expanded
- isLeaf

-

true

if the row is leaf

**Returns:**
- true

if the expand (toggle) control should be drawn
for the specified row

---

#### protected void paintVerticalLine​(
Graphics
g,

JComponent
c,
int x,
int top,
int bottom)

Paints a vertical line.

**Parameters:**
- g

- a graphics context
- c

- a component
- x

- an X coordinate
- top

- an Y1 coordinate
- bottom

- an Y2 coordinate

---

#### protected void paintHorizontalLine​(
Graphics
g,

JComponent
c,
int y,
int left,
int right)

Paints a horizontal line.

**Parameters:**
- g

- a graphics context
- c

- a component
- y

- an Y coordinate
- left

- an X1 coordinate
- right

- an X2 coordinate

---

#### protected int getVerticalLegBuffer()

The vertical element of legs between nodes starts at the bottom of the
parent node by default. This method makes the leg start below that.

**Returns:**
- the vertical leg buffer

---

#### protected int getHorizontalLegBuffer()

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default. This
method makes the leg end before that.

**Returns:**
- the horizontal leg buffer

---

#### protected void drawCentered​(
Component
c,

Graphics
graphics,

Icon
icon,
int x,
int y)

Draws the

icon

centered at (x,y).

**Parameters:**
- c

- a component
- graphics

- a graphics context
- icon

- an icon
- x

- an X coordinate
- y

- an Y coordinate

---

#### protected void drawDashedHorizontalLine​(
Graphics
g,
int y,
int x1,
int x2)

Draws a horizontal dashed line. It is assumed

x1

<=

x2

.
If

x1

is greater than

x2

, the method draws nothing.

**Parameters:**
- g

- an instance of

Graphics
- y

- an Y coordinate
- x1

- an X1 coordinate
- x2

- an X2 coordinate

---

#### protected void drawDashedVerticalLine​(
Graphics
g,
int x,
int y1,
int y2)

Draws a vertical dashed line. It is assumed

y1

<=

y2

.
If

y1

is greater than

y2

, the method draws nothing.

**Parameters:**
- g

- an instance of

Graphics
- x

- an X coordinate
- y1

- an Y1 coordinate
- y2

- an Y2 coordinate

---

#### protected int getRowX​(int row,
int depth)

Returns the location, along the x-axis, to render a particular row
at. The return value does not include any Insets specified on the JTree.
This does not check for the validity of the row or depth, it is assumed
to be correct and will not throw an Exception if the row or depth
doesn't match that of the tree.

**Parameters:**
- row

- Row to return x location for
- depth

- Depth of the row

**Returns:**
- amount to indent the given row.

**Since:**
- 1.5

---

#### protected void updateLayoutCacheExpandedNodes()

Makes all the nodes that are expanded in JTree expanded in LayoutCache.
This invokes updateExpandedDescendants with the root path.

---

#### protected void updateExpandedDescendants​(
TreePath
path)

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

**Parameters:**
- path

- a tree path

---

#### protected
TreePath
getLastChildPath​(
TreePath
parent)

Returns a path to the last child of

parent

.

**Parameters:**
- parent

- a tree path

**Returns:**
- a path to the last child of

parent

---

#### protected void updateDepthOffset()

Updates how much each depth should be offset by.

---

#### protected void updateCellEditor()

Updates the cellEditor based on the editability of the JTree that
we're contained in. If the tree is editable but doesn't have a
cellEditor, a basic one will be used.

---

#### protected void updateRenderer()

Messaged from the tree we're in when the renderer has changed.

---

#### protected void configureLayoutCache()

Resets the TreeState instance based on the tree we're providing the
look and feel for.

---

#### protected void updateSize()

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

---

#### protected void updateCachedPreferredSize()

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

---

#### protected void pathWasExpanded​(
TreePath
path)

Messaged from the

VisibleTreeNode

after it has been expanded.

**Parameters:**
- path

- a tree path

---

#### protected void pathWasCollapsed​(
TreePath
path)

Messaged from the

VisibleTreeNode

after it has collapsed.

**Parameters:**
- path

- a tree path

---

#### protected void ensureRowsAreVisible​(int beginRow,
int endRow)

Ensures that the rows identified by

beginRow

through

endRow

are visible.

**Parameters:**
- beginRow

- the begin row
- endRow

- the end row

---

#### public void setPreferredMinSize​(
Dimension
newSize)

Sets the preferred minimum size.

**Parameters:**
- newSize

- the new preferred size

---

#### public
Dimension
getPreferredMinSize()

Returns the minimum preferred size.

**Returns:**
- the minimum preferred size

---

#### public
Dimension
getPreferredSize​(
JComponent
c)

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- a component

**Returns:**
- the preferred size to represent the tree in the component

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### public
Dimension
getPreferredSize​(
JComponent
c,
boolean checkConsistency)

Returns the preferred size to represent the tree in

c

. If

checkConsistency

is

true

checkConsistency

is messaged first.

**Parameters:**
- c

- a component
- checkConsistency

- if

true

consistency is checked

**Returns:**
- the preferred size to represent the tree in the component

---

#### public
Dimension
getMinimumSize​(
JComponent
c)

Returns the minimum size for this component. Which will be
the min preferred size or 0, 0.

**Overrides:**
- getMinimumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

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

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

**Overrides:**
- getMaximumSize

in class

ComponentUI

**Parameters:**
- c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**Returns:**
- a

Dimension

object or

null

**See Also:**
- JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

---

#### protected void completeEditing()

Messages to stop the editing session. If the UI the receiver
is providing the look and feel for returns true from

getInvokesStopCellEditing

, stopCellEditing will
invoked on the current editor. Then completeEditing will
be messaged with false, true, false to cancel any lingering
editing.

---

#### protected void completeEditing​(boolean messageStop,
boolean messageCancel,
boolean messageTree)

Stops the editing session. If

messageStop

is

true

the editor
is messaged with

stopEditing

, if

messageCancel

is

true

the editor is messaged with

cancelEditing

.
If

messageTree

is

true

the

treeModel

is messaged
with

valueForPathChanged

.

**Parameters:**
- messageStop

- message to stop editing
- messageCancel

- message to cancel editing
- messageTree

- message to tree

---

#### protected boolean startEditing​(
TreePath
path,

MouseEvent
event)

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

This assumes that path is valid and visible.

**Parameters:**
- path

- a tree path
- event

- a mouse event

**Returns:**
- true

if the editing is successful

---

#### protected void checkForClickInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

**Parameters:**
- path

- a tree path
- mouseX

- an X coordinate
- mouseY

- an Y coordinate

---

#### protected boolean isLocationInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

**Parameters:**
- path

- a tree path
- mouseX

- an X coordinate
- mouseY

- an Y coordinate

**Returns:**
- true

if the mouse cursor fall in the area of row that
is used to expand/collapse the node and the node is not a leaf.

---

#### protected void handleExpandControlClick​(
TreePath
path,
int mouseX,
int mouseY)

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

**Parameters:**
- path

- a tree path
- mouseX

- an X coordinate
- mouseY

- an Y coordinate

---

#### protected void toggleExpandState​(
TreePath
path)

Expands path if it is not expanded, or collapses row if it is expanded.
If expanding a path and

JTree

scrolls on expand,

ensureRowsAreVisible

is invoked to scroll as many of the children
to visible as possible (tries to scroll to last visible descendant of path).

**Parameters:**
- path

- a tree path

---

#### protected boolean isToggleSelectionEvent​(
MouseEvent
event)

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

**Parameters:**
- event

- a mouse event

**Returns:**
- true

if a mouse event on the node should toggle the selection

---

#### protected boolean isMultiSelectEvent​(
MouseEvent
event)

Returning

true

signifies a mouse event on the node should select
from the anchor point.

**Parameters:**
- event

- a mouse event

**Returns:**
- true

if a mouse event on the node should select
from the anchor point

---

#### protected boolean isToggleEvent​(
MouseEvent
event)

Returning

true

indicates the row under the mouse should be toggled
based on the event. This is invoked after

checkForClickInExpandControl

,
implying the location is not in the expand (toggle) control.

**Parameters:**
- event

- a mouse event

**Returns:**
- true

if the row under the mouse should be toggled

---

#### protected void selectPathForEvent​(
TreePath
path,

MouseEvent
event)

Messaged to update the selection based on a

MouseEvent

over a
particular row. If the event is a toggle selection event, the
row is either selected, or deselected. If the event identifies
a multi selection event, the selection is updated from the
anchor point. Otherwise the row is selected, and if the event
specified a toggle event the row is expanded/collapsed.

**Parameters:**
- path

- the selected path
- event

- the mouse event

---

#### protected boolean isLeaf​(int row)

Returns

true

if the node at

row

is a leaf.

**Parameters:**
- row

- a row

**Returns:**
- true

if the node at

row

is a leaf

---

#### protected void updateLeadSelectionRow()

Updates the lead row of the selection.

**Since:**
- 1.7

---

#### protected int getLeadSelectionRow()

Returns the lead row of the selection.

**Returns:**
- selection lead row

**Since:**
- 1.7

---

### Additional Sections

#### Class BasicTreeUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TreeUI
- - javax.swing.plaf.basic.BasicTreeUI

javax.swing.plaf.TreeUI

- javax.swing.plaf.basic.BasicTreeUI

javax.swing.plaf.basic.BasicTreeUI

**Direct Known Subclasses:** MetalTreeUI

,

SynthTreeUI

```java
public class
BasicTreeUI

extends
TreeUI
```

The basic L&F for a hierarchical data structure.

public class

BasicTreeUI

extends

TreeUI

The basic L&F for a hierarchical data structure.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicTreeUI.CellEditorHandler

Listener responsible for getting cell editing events and updating
the tree accordingly.

class

BasicTreeUI.ComponentHandler

Updates the preferred size when scrolling (if necessary).

class

BasicTreeUI.FocusHandler

Repaints the lead selection row when focus is lost/gained.

class

BasicTreeUI.KeyHandler

This is used to get multiple key down events to appropriately generate
events.

class

BasicTreeUI.MouseHandler

TreeMouseListener is responsible for updating the selection
based on mouse events.

class

BasicTreeUI.MouseInputHandler

MouseInputHandler handles passing all mouse events,
including mouse motion events, until the mouse is released to
the destination it is constructed with.

class

BasicTreeUI.NodeDimensionsHandler

Class responsible for getting size of node, method is forwarded
to BasicTreeUI method.

class

BasicTreeUI.PropertyChangeHandler

PropertyChangeListener for the tree.

class

BasicTreeUI.SelectionModelPropertyChangeHandler

Listener on the TreeSelectionModel, resets the row selection if
any of the properties of the model change.

class

BasicTreeUI.TreeCancelEditingAction

ActionListener that invokes cancelEditing when action performed.

class

BasicTreeUI.TreeExpansionHandler

Updates the TreeState in response to nodes expanding/collapsing.

class

BasicTreeUI.TreeHomeAction

TreeHomeAction is used to handle end/home actions.

class

BasicTreeUI.TreeIncrementAction

TreeIncrementAction is used to handle up/down actions.

class

BasicTreeUI.TreeModelHandler

Forwards all TreeModel events to the TreeState.

class

BasicTreeUI.TreePageAction

TreePageAction handles page up and page down events.

class

BasicTreeUI.TreeSelectionHandler

Listens for changes in the selection model and updates the display
accordingly.

class

BasicTreeUI.TreeToggleAction

For the first selected row expandedness will be toggled.

class

BasicTreeUI.TreeTraverseAction

TreeTraverseAction

is the action used for left/right keys.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

TreeCellEditor

cellEditor

Editor for the tree.

protected

Icon

collapsedIcon

The collapsed icon.

protected boolean

createdCellEditor

Set to true if editor that is currently in the tree was
created by this instance.

protected boolean

createdRenderer

Set to true if the renderer that is currently in the tree was
created by this instance.

protected

TreeCellRenderer

currentCellRenderer

Renderer that is being used to do the actual cell drawing.

protected int

depthOffset

How much the depth should be offset to properly calculate
x locations.

protected

Hashtable

<

TreePath

,​

Boolean

>

drawingCache

Used for minimizing the drawing of vertical lines.

protected

Component

editingComponent

When editing, this will be the Component that is doing the actual
editing.

protected

TreePath

editingPath

Path that is being edited.

protected int

editingRow

Row that is being edited.

protected boolean

editorHasDifferentSize

Set to true if the editor has a different size than the renderer.

protected

Icon

expandedIcon

The expanded icon.

protected boolean

largeModel

True if doing optimizations for a largeModel.

protected int

lastSelectedRow

Index of the row that was last selected.

protected int

leftChildIndent

Distance between left margin and where vertical dashes will be
drawn.

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Reponsible for telling the TreeState the size needed for a node.

protected

Dimension

preferredMinSize

Minimum preferred size.

protected

Dimension

preferredSize

Size needed to completely display all the nodes.

protected

CellRendererPane

rendererPane

Used to paint the TreeCellRenderer.

protected int

rightChildIndent

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

protected boolean

stopEditingInCompleteEditing

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

protected int

totalChildIndent

Total distance that will be indented.

protected

JTree

tree

Component that we're going to be drawing into.

protected

TreeModel

treeModel

Used to determine what to display.

protected

TreeSelectionModel

treeSelectionModel

Model maintaining the selection.

protected

AbstractLayoutCache

treeState

Object responsible for handling sizing and expanded issues.

protected boolean

validCachedPreferredSize

Is the preferredSize valid?

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicTreeUI

()

Constructs a new instance of

BasicTreeUI

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

void

cancelEditing

​(

JTree

tree)

Cancels the current editing session.

protected void

checkForClickInExpandControl

​(

TreePath

path,
int mouseX,
int mouseY)

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

protected void

completeEditing

()

Messages to stop the editing session.

protected void

completeEditing

​(boolean messageStop,
boolean messageCancel,
boolean messageTree)

Stops the editing session.

protected void

completeUIInstall

()

Invoked from installUI after all the defaults/listeners have been
installed.

protected void

completeUIUninstall

()

Uninstalls UI.

protected void

configureLayoutCache

()

Resets the TreeState instance based on the tree we're providing the
look and feel for.

protected

CellEditorListener

createCellEditorListener

()

Creates a listener to handle events from the current editor.

protected

CellRendererPane

createCellRendererPane

()

Returns the renderer pane that renderer components are placed in.

protected

ComponentListener

createComponentListener

()

Creates and returns a new ComponentHandler.

protected

TreeCellEditor

createDefaultCellEditor

()

Creates a default cell editor.

protected

TreeCellRenderer

createDefaultCellRenderer

()

Returns the default cell renderer that is used to do the
stamping of each node.

protected

FocusListener

createFocusListener

()

Creates a listener that is responsible for updating the display
when focus is lost/gained.

protected

KeyListener

createKeyListener

()

Creates the listener responsible for getting key events from
the tree.

protected

AbstractLayoutCache

createLayoutCache

()

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

protected

MouseListener

createMouseListener

()

Creates the listener responsible for updating the selection based on
mouse events.

protected

AbstractLayoutCache.NodeDimensions

createNodeDimensions

()

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a listener that is responsible that updates the UI based on
how the tree changes.

protected

PropertyChangeListener

createSelectionModelPropertyChangeListener

()

Creates the listener responsible for getting property change
events from the selection model.

protected

TreeExpansionListener

createTreeExpansionListener

()

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

protected

TreeModelListener

createTreeModelListener

()

Returns a listener that can update the tree when the model changes.

protected

TreeSelectionListener

createTreeSelectionListener

()

Creates the listener that updates the display based on selection change
methods.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new instance of

BasicTreeUI

.

protected void

drawCentered

​(

Component

c,

Graphics

graphics,

Icon

icon,
int x,
int y)

Draws the

icon

centered at (x,y).

protected void

drawDashedHorizontalLine

​(

Graphics

g,
int y,
int x1,
int x2)

Draws a horizontal dashed line.

protected void

drawDashedVerticalLine

​(

Graphics

g,
int x,
int y1,
int y2)

Draws a vertical dashed line.

protected void

ensureRowsAreVisible

​(int beginRow,
int endRow)

Ensures that the rows identified by

beginRow

through

endRow

are visible.

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

TreeCellEditor

getCellEditor

()

Returns an instance of

TreeCellEditor

.

protected

TreeCellRenderer

getCellRenderer

()

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

TreePath

getClosestPathForLocation

​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y.

Icon

getCollapsedIcon

()

Returns the collapsed icon.

protected

Rectangle

getDropLineRect

​(

JTree.DropLocation

loc)

Returns a unbounding box for the drop line.

TreePath

getEditingPath

​(

JTree

tree)

Returns the path to the element that is being edited.

Icon

getExpandedIcon

()

Returns the expanded icon.

protected

Color

getHashColor

()

Returns the hash color.

protected int

getHorizontalLegBuffer

()

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default.

protected

TreePath

getLastChildPath

​(

TreePath

parent)

Returns a path to the last child of

parent

.

protected int

getLeadSelectionRow

()

Returns the lead row of the selection.

int

getLeftChildIndent

()

Returns the left child indent.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size for this component.

protected

TreeModel

getModel

()

Returns the tree model.

Rectangle

getPathBounds

​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

TreePath

getPathForRow

​(

JTree

tree,
int row)

Returns the path for passed in row.

Dimension

getPreferredMinSize

()

Returns the minimum preferred size.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

Dimension

getPreferredSize

​(

JComponent

c,
boolean checkConsistency)

Returns the preferred size to represent the tree in

c

.

int

getRightChildIndent

()

Returns the right child indent.

int

getRowCount

​(

JTree

tree)

Returns the number of rows that are being displayed.

int

getRowForPath

​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at.

protected int

getRowHeight

()

Returns the row height.

protected int

getRowX

​(int row,
int depth)

Returns the location, along the x-axis, to render a particular row
at.

protected

TreeSelectionModel

getSelectionModel

()

Returns the tree selection model.

protected boolean

getShowsRootHandles

()

Returns

true

if the root handles are to be displayed.

protected int

getVerticalLegBuffer

()

The vertical element of legs between nodes starts at the bottom of the
parent node by default.

protected void

handleExpandControlClick

​(

TreePath

path,
int mouseX,
int mouseY)

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

protected void

installComponents

()

Intalls the subcomponents of the tree, which is the renderer pane.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected boolean

isDropLine

​(

JTree.DropLocation

loc)

Tells if a

DropLocation

should be indicated by a line between
nodes.

protected boolean

isEditable

()

Returns

true

if the tree is editable.

boolean

isEditing

​(

JTree

tree)

Returns true if the tree is being edited.

protected boolean

isLargeModel

()

Returns

true

if large model is set.

protected boolean

isLeaf

​(int row)

Returns

true

if the node at

row

is a leaf.

protected boolean

isLocationInExpandControl

​(

TreePath

path,
int mouseX,
int mouseY)

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

protected boolean

isMultiSelectEvent

​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should select
from the anchor point.

protected boolean

isRootVisible

()

Returns

true

if the tree root is visible.

protected boolean

isToggleEvent

​(

MouseEvent

event)

Returning

true

indicates the row under the mouse should be toggled
based on the event.

protected boolean

isToggleSelectionEvent

​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

protected void

paintDropLine

​(

Graphics

g)

Paints the drop line.

protected void

paintExpandControl

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the expand (toggle) part of a row.

protected void

paintHorizontalLine

​(

Graphics

g,

JComponent

c,
int y,
int left,
int right)

Paints a horizontal line.

protected void

paintHorizontalPartOfLeg

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the horizontal part of the leg.

protected void

paintRow

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the renderer part of a row.

protected void

paintVerticalLine

​(

Graphics

g,

JComponent

c,
int x,
int top,
int bottom)

Paints a vertical line.

protected void

paintVerticalPartOfLeg

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

TreePath

path)

Paints the vertical part of the leg.

protected void

pathWasCollapsed

​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has collapsed.

protected void

pathWasExpanded

​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has been expanded.

protected void

prepareForUIInstall

()

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

protected void

prepareForUIUninstall

()

Invoked before unstallation of UI.

protected void

selectPathForEvent

​(

TreePath

path,

MouseEvent

event)

Messaged to update the selection based on a

MouseEvent

over a
particular row.

protected void

setCellEditor

​(

TreeCellEditor

editor)

Sets the cell editor.

protected void

setCellRenderer

​(

TreeCellRenderer

tcr)

Sets the

TreeCellRenderer

to

tcr

.

void

setCollapsedIcon

​(

Icon

newG)

Sets the collapsed icon.

protected void

setEditable

​(boolean newValue)

Configures the receiver to allow, or not allow, editing.

void

setExpandedIcon

​(

Icon

newG)

Sets the expanded icon.

protected void

setHashColor

​(

Color

color)

Sets the hash color.

protected void

setLargeModel

​(boolean largeModel)

Updates the componentListener, if necessary.

void

setLeftChildIndent

​(int newAmount)

Sets the left child indent.

protected void

setModel

​(

TreeModel

model)

Sets the

TreeModel

.

void

setPreferredMinSize

​(

Dimension

newSize)

Sets the preferred minimum size.

void

setRightChildIndent

​(int newAmount)

Sets the right child indent.

protected void

setRootVisible

​(boolean newValue)

Sets the root to being visible.

protected void

setRowHeight

​(int rowHeight)

Sets the row height, this is forwarded to the treeState.

protected void

setSelectionModel

​(

TreeSelectionModel

newLSM)

Resets the selection model.

protected void

setShowsRootHandles

​(boolean newValue)

Determines whether the node handles are to be displayed.

protected boolean

shouldPaintExpandControl

​(

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

protected boolean

startEditing

​(

TreePath

path,

MouseEvent

event)

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

void

startEditingAtPath

​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it.

boolean

stopEditing

​(

JTree

tree)

Stops the current editing session.

protected void

toggleExpandState

​(

TreePath

path)

Expands path if it is not expanded, or collapses row if it is expanded.

protected void

uninstallComponents

()

Uninstalls the renderer pane.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

protected void

updateCachedPreferredSize

()

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

protected void

updateCellEditor

()

Updates the cellEditor based on the editability of the JTree that
we're contained in.

protected void

updateDepthOffset

()

Updates how much each depth should be offset by.

protected void

updateExpandedDescendants

​(

TreePath

path)

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

protected void

updateLayoutCacheExpandedNodes

()

Makes all the nodes that are expanded in JTree expanded in LayoutCache.

protected void

updateLeadSelectionRow

()

Updates the lead row of the selection.

protected void

updateRenderer

()

Messaged from the tree we're in when the renderer has changed.

protected void

updateSize

()

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

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

Nested Classes

Modifier and Type

Class

Description

class

BasicTreeUI.CellEditorHandler

Listener responsible for getting cell editing events and updating
the tree accordingly.

class

BasicTreeUI.ComponentHandler

Updates the preferred size when scrolling (if necessary).

class

BasicTreeUI.FocusHandler

Repaints the lead selection row when focus is lost/gained.

class

BasicTreeUI.KeyHandler

This is used to get multiple key down events to appropriately generate
events.

class

BasicTreeUI.MouseHandler

TreeMouseListener is responsible for updating the selection
based on mouse events.

class

BasicTreeUI.MouseInputHandler

MouseInputHandler handles passing all mouse events,
including mouse motion events, until the mouse is released to
the destination it is constructed with.

class

BasicTreeUI.NodeDimensionsHandler

Class responsible for getting size of node, method is forwarded
to BasicTreeUI method.

class

BasicTreeUI.PropertyChangeHandler

PropertyChangeListener for the tree.

class

BasicTreeUI.SelectionModelPropertyChangeHandler

Listener on the TreeSelectionModel, resets the row selection if
any of the properties of the model change.

class

BasicTreeUI.TreeCancelEditingAction

ActionListener that invokes cancelEditing when action performed.

class

BasicTreeUI.TreeExpansionHandler

Updates the TreeState in response to nodes expanding/collapsing.

class

BasicTreeUI.TreeHomeAction

TreeHomeAction is used to handle end/home actions.

class

BasicTreeUI.TreeIncrementAction

TreeIncrementAction is used to handle up/down actions.

class

BasicTreeUI.TreeModelHandler

Forwards all TreeModel events to the TreeState.

class

BasicTreeUI.TreePageAction

TreePageAction handles page up and page down events.

class

BasicTreeUI.TreeSelectionHandler

Listens for changes in the selection model and updates the display
accordingly.

class

BasicTreeUI.TreeToggleAction

For the first selected row expandedness will be toggled.

class

BasicTreeUI.TreeTraverseAction

TreeTraverseAction

is the action used for left/right keys.

---

#### Nested Class Summary

Listener responsible for getting cell editing events and updating
the tree accordingly.

Updates the preferred size when scrolling (if necessary).

Repaints the lead selection row when focus is lost/gained.

This is used to get multiple key down events to appropriately generate
events.

TreeMouseListener is responsible for updating the selection
based on mouse events.

MouseInputHandler handles passing all mouse events,
including mouse motion events, until the mouse is released to
the destination it is constructed with.

Class responsible for getting size of node, method is forwarded
to BasicTreeUI method.

PropertyChangeListener for the tree.

Listener on the TreeSelectionModel, resets the row selection if
any of the properties of the model change.

ActionListener that invokes cancelEditing when action performed.

Updates the TreeState in response to nodes expanding/collapsing.

TreeHomeAction is used to handle end/home actions.

TreeIncrementAction is used to handle up/down actions.

Forwards all TreeModel events to the TreeState.

TreePageAction handles page up and page down events.

Listens for changes in the selection model and updates the display
accordingly.

For the first selected row expandedness will be toggled.

TreeTraverseAction

is the action used for left/right keys.

Field Summary

Fields

Modifier and Type

Field

Description

protected

TreeCellEditor

cellEditor

Editor for the tree.

protected

Icon

collapsedIcon

The collapsed icon.

protected boolean

createdCellEditor

Set to true if editor that is currently in the tree was
created by this instance.

protected boolean

createdRenderer

Set to true if the renderer that is currently in the tree was
created by this instance.

protected

TreeCellRenderer

currentCellRenderer

Renderer that is being used to do the actual cell drawing.

protected int

depthOffset

How much the depth should be offset to properly calculate
x locations.

protected

Hashtable

<

TreePath

,​

Boolean

>

drawingCache

Used for minimizing the drawing of vertical lines.

protected

Component

editingComponent

When editing, this will be the Component that is doing the actual
editing.

protected

TreePath

editingPath

Path that is being edited.

protected int

editingRow

Row that is being edited.

protected boolean

editorHasDifferentSize

Set to true if the editor has a different size than the renderer.

protected

Icon

expandedIcon

The expanded icon.

protected boolean

largeModel

True if doing optimizations for a largeModel.

protected int

lastSelectedRow

Index of the row that was last selected.

protected int

leftChildIndent

Distance between left margin and where vertical dashes will be
drawn.

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Reponsible for telling the TreeState the size needed for a node.

protected

Dimension

preferredMinSize

Minimum preferred size.

protected

Dimension

preferredSize

Size needed to completely display all the nodes.

protected

CellRendererPane

rendererPane

Used to paint the TreeCellRenderer.

protected int

rightChildIndent

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

protected boolean

stopEditingInCompleteEditing

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

protected int

totalChildIndent

Total distance that will be indented.

protected

JTree

tree

Component that we're going to be drawing into.

protected

TreeModel

treeModel

Used to determine what to display.

protected

TreeSelectionModel

treeSelectionModel

Model maintaining the selection.

protected

AbstractLayoutCache

treeState

Object responsible for handling sizing and expanded issues.

protected boolean

validCachedPreferredSize

Is the preferredSize valid?

---

#### Field Summary

Editor for the tree.

The collapsed icon.

Set to true if editor that is currently in the tree was
created by this instance.

Set to true if the renderer that is currently in the tree was
created by this instance.

Renderer that is being used to do the actual cell drawing.

How much the depth should be offset to properly calculate
x locations.

Used for minimizing the drawing of vertical lines.

When editing, this will be the Component that is doing the actual
editing.

Path that is being edited.

Row that is being edited.

Set to true if the editor has a different size than the renderer.

The expanded icon.

True if doing optimizations for a largeModel.

Index of the row that was last selected.

Distance between left margin and where vertical dashes will be
drawn.

Reponsible for telling the TreeState the size needed for a node.

Minimum preferred size.

Size needed to completely display all the nodes.

Used to paint the TreeCellRenderer.

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

Total distance that will be indented.

Component that we're going to be drawing into.

Used to determine what to display.

Model maintaining the selection.

Object responsible for handling sizing and expanded issues.

Is the preferredSize valid?

Constructor Summary

Constructors

Constructor

Description

BasicTreeUI

()

Constructs a new instance of

BasicTreeUI

.

---

#### Constructor Summary

Constructs a new instance of

BasicTreeUI

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

cancelEditing

​(

JTree

tree)

Cancels the current editing session.

protected void

checkForClickInExpandControl

​(

TreePath

path,
int mouseX,
int mouseY)

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

protected void

completeEditing

()

Messages to stop the editing session.

protected void

completeEditing

​(boolean messageStop,
boolean messageCancel,
boolean messageTree)

Stops the editing session.

protected void

completeUIInstall

()

Invoked from installUI after all the defaults/listeners have been
installed.

protected void

completeUIUninstall

()

Uninstalls UI.

protected void

configureLayoutCache

()

Resets the TreeState instance based on the tree we're providing the
look and feel for.

protected

CellEditorListener

createCellEditorListener

()

Creates a listener to handle events from the current editor.

protected

CellRendererPane

createCellRendererPane

()

Returns the renderer pane that renderer components are placed in.

protected

ComponentListener

createComponentListener

()

Creates and returns a new ComponentHandler.

protected

TreeCellEditor

createDefaultCellEditor

()

Creates a default cell editor.

protected

TreeCellRenderer

createDefaultCellRenderer

()

Returns the default cell renderer that is used to do the
stamping of each node.

protected

FocusListener

createFocusListener

()

Creates a listener that is responsible for updating the display
when focus is lost/gained.

protected

KeyListener

createKeyListener

()

Creates the listener responsible for getting key events from
the tree.

protected

AbstractLayoutCache

createLayoutCache

()

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

protected

MouseListener

createMouseListener

()

Creates the listener responsible for updating the selection based on
mouse events.

protected

AbstractLayoutCache.NodeDimensions

createNodeDimensions

()

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a listener that is responsible that updates the UI based on
how the tree changes.

protected

PropertyChangeListener

createSelectionModelPropertyChangeListener

()

Creates the listener responsible for getting property change
events from the selection model.

protected

TreeExpansionListener

createTreeExpansionListener

()

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

protected

TreeModelListener

createTreeModelListener

()

Returns a listener that can update the tree when the model changes.

protected

TreeSelectionListener

createTreeSelectionListener

()

Creates the listener that updates the display based on selection change
methods.

static

ComponentUI

createUI

​(

JComponent

x)

Constructs a new instance of

BasicTreeUI

.

protected void

drawCentered

​(

Component

c,

Graphics

graphics,

Icon

icon,
int x,
int y)

Draws the

icon

centered at (x,y).

protected void

drawDashedHorizontalLine

​(

Graphics

g,
int y,
int x1,
int x2)

Draws a horizontal dashed line.

protected void

drawDashedVerticalLine

​(

Graphics

g,
int x,
int y1,
int y2)

Draws a vertical dashed line.

protected void

ensureRowsAreVisible

​(int beginRow,
int endRow)

Ensures that the rows identified by

beginRow

through

endRow

are visible.

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

TreeCellEditor

getCellEditor

()

Returns an instance of

TreeCellEditor

.

protected

TreeCellRenderer

getCellRenderer

()

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

TreePath

getClosestPathForLocation

​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y.

Icon

getCollapsedIcon

()

Returns the collapsed icon.

protected

Rectangle

getDropLineRect

​(

JTree.DropLocation

loc)

Returns a unbounding box for the drop line.

TreePath

getEditingPath

​(

JTree

tree)

Returns the path to the element that is being edited.

Icon

getExpandedIcon

()

Returns the expanded icon.

protected

Color

getHashColor

()

Returns the hash color.

protected int

getHorizontalLegBuffer

()

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default.

protected

TreePath

getLastChildPath

​(

TreePath

parent)

Returns a path to the last child of

parent

.

protected int

getLeadSelectionRow

()

Returns the lead row of the selection.

int

getLeftChildIndent

()

Returns the left child indent.

Dimension

getMaximumSize

​(

JComponent

c)

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

Dimension

getMinimumSize

​(

JComponent

c)

Returns the minimum size for this component.

protected

TreeModel

getModel

()

Returns the tree model.

Rectangle

getPathBounds

​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

TreePath

getPathForRow

​(

JTree

tree,
int row)

Returns the path for passed in row.

Dimension

getPreferredMinSize

()

Returns the minimum preferred size.

Dimension

getPreferredSize

​(

JComponent

c)

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

Dimension

getPreferredSize

​(

JComponent

c,
boolean checkConsistency)

Returns the preferred size to represent the tree in

c

.

int

getRightChildIndent

()

Returns the right child indent.

int

getRowCount

​(

JTree

tree)

Returns the number of rows that are being displayed.

int

getRowForPath

​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at.

protected int

getRowHeight

()

Returns the row height.

protected int

getRowX

​(int row,
int depth)

Returns the location, along the x-axis, to render a particular row
at.

protected

TreeSelectionModel

getSelectionModel

()

Returns the tree selection model.

protected boolean

getShowsRootHandles

()

Returns

true

if the root handles are to be displayed.

protected int

getVerticalLegBuffer

()

The vertical element of legs between nodes starts at the bottom of the
parent node by default.

protected void

handleExpandControlClick

​(

TreePath

path,
int mouseX,
int mouseY)

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

protected void

installComponents

()

Intalls the subcomponents of the tree, which is the renderer pane.

protected void

installDefaults

()

Installs default properties.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListeners

()

Registers listeners.

protected boolean

isDropLine

​(

JTree.DropLocation

loc)

Tells if a

DropLocation

should be indicated by a line between
nodes.

protected boolean

isEditable

()

Returns

true

if the tree is editable.

boolean

isEditing

​(

JTree

tree)

Returns true if the tree is being edited.

protected boolean

isLargeModel

()

Returns

true

if large model is set.

protected boolean

isLeaf

​(int row)

Returns

true

if the node at

row

is a leaf.

protected boolean

isLocationInExpandControl

​(

TreePath

path,
int mouseX,
int mouseY)

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

protected boolean

isMultiSelectEvent

​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should select
from the anchor point.

protected boolean

isRootVisible

()

Returns

true

if the tree root is visible.

protected boolean

isToggleEvent

​(

MouseEvent

event)

Returning

true

indicates the row under the mouse should be toggled
based on the event.

protected boolean

isToggleSelectionEvent

​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

protected void

paintDropLine

​(

Graphics

g)

Paints the drop line.

protected void

paintExpandControl

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the expand (toggle) part of a row.

protected void

paintHorizontalLine

​(

Graphics

g,

JComponent

c,
int y,
int left,
int right)

Paints a horizontal line.

protected void

paintHorizontalPartOfLeg

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the horizontal part of the leg.

protected void

paintRow

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the renderer part of a row.

protected void

paintVerticalLine

​(

Graphics

g,

JComponent

c,
int x,
int top,
int bottom)

Paints a vertical line.

protected void

paintVerticalPartOfLeg

​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

TreePath

path)

Paints the vertical part of the leg.

protected void

pathWasCollapsed

​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has collapsed.

protected void

pathWasExpanded

​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has been expanded.

protected void

prepareForUIInstall

()

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

protected void

prepareForUIUninstall

()

Invoked before unstallation of UI.

protected void

selectPathForEvent

​(

TreePath

path,

MouseEvent

event)

Messaged to update the selection based on a

MouseEvent

over a
particular row.

protected void

setCellEditor

​(

TreeCellEditor

editor)

Sets the cell editor.

protected void

setCellRenderer

​(

TreeCellRenderer

tcr)

Sets the

TreeCellRenderer

to

tcr

.

void

setCollapsedIcon

​(

Icon

newG)

Sets the collapsed icon.

protected void

setEditable

​(boolean newValue)

Configures the receiver to allow, or not allow, editing.

void

setExpandedIcon

​(

Icon

newG)

Sets the expanded icon.

protected void

setHashColor

​(

Color

color)

Sets the hash color.

protected void

setLargeModel

​(boolean largeModel)

Updates the componentListener, if necessary.

void

setLeftChildIndent

​(int newAmount)

Sets the left child indent.

protected void

setModel

​(

TreeModel

model)

Sets the

TreeModel

.

void

setPreferredMinSize

​(

Dimension

newSize)

Sets the preferred minimum size.

void

setRightChildIndent

​(int newAmount)

Sets the right child indent.

protected void

setRootVisible

​(boolean newValue)

Sets the root to being visible.

protected void

setRowHeight

​(int rowHeight)

Sets the row height, this is forwarded to the treeState.

protected void

setSelectionModel

​(

TreeSelectionModel

newLSM)

Resets the selection model.

protected void

setShowsRootHandles

​(boolean newValue)

Determines whether the node handles are to be displayed.

protected boolean

shouldPaintExpandControl

​(

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

protected boolean

startEditing

​(

TreePath

path,

MouseEvent

event)

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

void

startEditingAtPath

​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it.

boolean

stopEditing

​(

JTree

tree)

Stops the current editing session.

protected void

toggleExpandState

​(

TreePath

path)

Expands path if it is not expanded, or collapses row if it is expanded.

protected void

uninstallComponents

()

Uninstalls the renderer pane.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

uninstallListeners

()

Unregisters listeners.

protected void

updateCachedPreferredSize

()

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

protected void

updateCellEditor

()

Updates the cellEditor based on the editability of the JTree that
we're contained in.

protected void

updateDepthOffset

()

Updates how much each depth should be offset by.

protected void

updateExpandedDescendants

​(

TreePath

path)

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

protected void

updateLayoutCacheExpandedNodes

()

Makes all the nodes that are expanded in JTree expanded in LayoutCache.

protected void

updateLeadSelectionRow

()

Updates the lead row of the selection.

protected void

updateRenderer

()

Messaged from the tree we're in when the renderer has changed.

protected void

updateSize

()

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

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

Cancels the current editing session.

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

Messages to stop the editing session.

Stops the editing session.

Invoked from installUI after all the defaults/listeners have been
installed.

Uninstalls UI.

Resets the TreeState instance based on the tree we're providing the
look and feel for.

Creates a listener to handle events from the current editor.

Returns the renderer pane that renderer components are placed in.

Creates and returns a new ComponentHandler.

Creates a default cell editor.

Returns the default cell renderer that is used to do the
stamping of each node.

Creates a listener that is responsible for updating the display
when focus is lost/gained.

Creates the listener responsible for getting key events from
the tree.

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

Creates the listener responsible for updating the selection based on
mouse events.

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

Creates a listener that is responsible that updates the UI based on
how the tree changes.

Creates the listener responsible for getting property change
events from the selection model.

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

Returns a listener that can update the tree when the model changes.

Creates the listener that updates the display based on selection change
methods.

Constructs a new instance of

BasicTreeUI

.

Draws the

icon

centered at (x,y).

Draws a horizontal dashed line.

Draws a vertical dashed line.

Ensures that the rows identified by

beginRow

through

endRow

are visible.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

Returns an instance of

TreeCellEditor

.

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

Returns the path to the node that is closest to x,y.

Returns the collapsed icon.

Returns a unbounding box for the drop line.

Returns the path to the element that is being edited.

Returns the expanded icon.

Returns the hash color.

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default.

Returns a path to the last child of

parent

.

Returns the lead row of the selection.

Returns the left child indent.

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

Returns the minimum size for this component.

Returns the tree model.

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

Returns the path for passed in row.

Returns the minimum preferred size.

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

Returns the preferred size to represent the tree in

c

.

Returns the right child indent.

Returns the number of rows that are being displayed.

Returns the row that the last item identified in path is visible
at.

Returns the row height.

Returns the location, along the x-axis, to render a particular row
at.

Returns the tree selection model.

Returns

true

if the root handles are to be displayed.

The vertical element of legs between nodes starts at the bottom of the
parent node by default.

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

Intalls the subcomponents of the tree, which is the renderer pane.

Installs default properties.

Registers keyboard actions.

Registers listeners.

Tells if a

DropLocation

should be indicated by a line between
nodes.

Returns

true

if the tree is editable.

Returns true if the tree is being edited.

Returns

true

if large model is set.

Returns

true

if the node at

row

is a leaf.

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

Returning

true

signifies a mouse event on the node should select
from the anchor point.

Returns

true

if the tree root is visible.

Returning

true

indicates the row under the mouse should be toggled
based on the event.

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

Paints the drop line.

Paints the expand (toggle) part of a row.

Paints a horizontal line.

Paints the horizontal part of the leg.

Paints the renderer part of a row.

Paints a vertical line.

Paints the vertical part of the leg.

Messaged from the

VisibleTreeNode

after it has collapsed.

Messaged from the

VisibleTreeNode

after it has been expanded.

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

Invoked before unstallation of UI.

Messaged to update the selection based on a

MouseEvent

over a
particular row.

Sets the cell editor.

Sets the

TreeCellRenderer

to

tcr

.

Sets the collapsed icon.

Configures the receiver to allow, or not allow, editing.

Sets the expanded icon.

Sets the hash color.

Updates the componentListener, if necessary.

Sets the left child indent.

Sets the

TreeModel

.

Sets the preferred minimum size.

Sets the right child indent.

Sets the root to being visible.

Sets the row height, this is forwarded to the treeState.

Resets the selection model.

Determines whether the node handles are to be displayed.

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

Selects the last item in path and tries to edit it.

Stops the current editing session.

Expands path if it is not expanded, or collapses row if it is expanded.

Uninstalls the renderer pane.

Uninstalls default properties.

Unregisters keyboard actions.

Unregisters listeners.

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

Updates the cellEditor based on the editability of the JTree that
we're contained in.

Updates how much each depth should be offset by.

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

Makes all the nodes that are expanded in JTree expanded in LayoutCache.

Updates the lead row of the selection.

Messaged from the tree we're in when the renderer has changed.

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

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

============ FIELD DETAIL ===========

- Field Detail

- collapsedIcon

```java
protected transient
Icon
collapsedIcon
```

The collapsed icon.

- expandedIcon

```java
protected transient
Icon
expandedIcon
```

The expanded icon.

- leftChildIndent

```java
protected int leftChildIndent
```

Distance between left margin and where vertical dashes will be
drawn.

- rightChildIndent

```java
protected int rightChildIndent
```

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

- totalChildIndent

```java
protected int totalChildIndent
```

Total distance that will be indented. The sum of leftChildIndent
and rightChildIndent.

- preferredMinSize

```java
protected
Dimension
preferredMinSize
```

Minimum preferred size.

- lastSelectedRow

```java
protected int lastSelectedRow
```

Index of the row that was last selected.

- tree

```java
protected
JTree
tree
```

Component that we're going to be drawing into.

- currentCellRenderer

```java
protected transient
TreeCellRenderer
currentCellRenderer
```

Renderer that is being used to do the actual cell drawing.

- createdRenderer

```java
protected boolean createdRenderer
```

Set to true if the renderer that is currently in the tree was
created by this instance.

- cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the tree.

- createdCellEditor

```java
protected boolean createdCellEditor
```

Set to true if editor that is currently in the tree was
created by this instance.

- stopEditingInCompleteEditing

```java
protected boolean stopEditingInCompleteEditing
```

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

Used to paint the TreeCellRenderer.

- preferredSize

```java
protected
Dimension
preferredSize
```

Size needed to completely display all the nodes.

- validCachedPreferredSize

```java
protected boolean validCachedPreferredSize
```

Is the preferredSize valid?

- treeState

```java
protected
AbstractLayoutCache
treeState
```

Object responsible for handling sizing and expanded issues.

- drawingCache

```java
protected
Hashtable
<
TreePath
,​
Boolean
> drawingCache
```

Used for minimizing the drawing of vertical lines.

- largeModel

```java
protected boolean largeModel
```

True if doing optimizations for a largeModel. Subclasses that
don't support this may wish to override createLayoutCache to not
return a FixedHeightLayoutCache instance.

- nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Reponsible for telling the TreeState the size needed for a node.

- treeModel

```java
protected
TreeModel
treeModel
```

Used to determine what to display.

- treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Model maintaining the selection.

- depthOffset

```java
protected int depthOffset
```

How much the depth should be offset to properly calculate
x locations. This is based on whether or not the root is visible,
and if the root handles are visible.

- editingComponent

```java
protected
Component
editingComponent
```

When editing, this will be the Component that is doing the actual
editing.

- editingPath

```java
protected
TreePath
editingPath
```

Path that is being edited.

- editingRow

```java
protected int editingRow
```

Row that is being edited. Should only be referenced if
editingComponent is not null.

- editorHasDifferentSize

```java
protected boolean editorHasDifferentSize
```

Set to true if the editor has a different size than the renderer.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicTreeUI

```java
public BasicTreeUI()
```

Constructs a new instance of

BasicTreeUI

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

Constructs a new instance of

BasicTreeUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicTreeUI

- getHashColor

```java
protected
Color
getHashColor()
```

Returns the hash color.

**Returns:** the hash color

- setHashColor

```java
protected void setHashColor​(
Color
color)
```

Sets the hash color.

**Parameters:** color

- the hash color

- setLeftChildIndent

```java
public void setLeftChildIndent​(int newAmount)
```

Sets the left child indent.

**Parameters:** newAmount

- the left child indent

- getLeftChildIndent

```java
public int getLeftChildIndent()
```

Returns the left child indent.

**Returns:** the left child indent

- setRightChildIndent

```java
public void setRightChildIndent​(int newAmount)
```

Sets the right child indent.

**Parameters:** newAmount

- the right child indent

- getRightChildIndent

```java
public int getRightChildIndent()
```

Returns the right child indent.

**Returns:** the right child indent

- setExpandedIcon

```java
public void setExpandedIcon​(
Icon
newG)
```

Sets the expanded icon.

**Parameters:** newG

- the expanded icon

- getExpandedIcon

```java
public
Icon
getExpandedIcon()
```

Returns the expanded icon.

**Returns:** the expanded icon

- setCollapsedIcon

```java
public void setCollapsedIcon​(
Icon
newG)
```

Sets the collapsed icon.

**Parameters:** newG

- the collapsed icon

- getCollapsedIcon

```java
public
Icon
getCollapsedIcon()
```

Returns the collapsed icon.

**Returns:** the collapsed icon

- setLargeModel

```java
protected void setLargeModel​(boolean largeModel)
```

Updates the componentListener, if necessary.

**Parameters:** largeModel

- the new value

- isLargeModel

```java
protected boolean isLargeModel()
```

Returns

true

if large model is set.

**Returns:** true

if large model is set

- setRowHeight

```java
protected void setRowHeight​(int rowHeight)
```

Sets the row height, this is forwarded to the treeState.

**Parameters:** rowHeight

- the row height

- getRowHeight

```java
protected int getRowHeight()
```

Returns the row height.

**Returns:** the row height

- setCellRenderer

```java
protected void setCellRenderer​(
TreeCellRenderer
tcr)
```

Sets the

TreeCellRenderer

to

tcr

. This invokes

updateRenderer

.

**Parameters:** tcr

- the new value

- getCellRenderer

```java
protected
TreeCellRenderer
getCellRenderer()
```

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

**Returns:** an instance of

TreeCellRenderer

- setModel

```java
protected void setModel​(
TreeModel
model)
```

Sets the

TreeModel

.

**Parameters:** model

- the new value

- getModel

```java
protected
TreeModel
getModel()
```

Returns the tree model.

**Returns:** the tree model

- setRootVisible

```java
protected void setRootVisible​(boolean newValue)
```

Sets the root to being visible.

**Parameters:** newValue

- the new value

- isRootVisible

```java
protected boolean isRootVisible()
```

Returns

true

if the tree root is visible.

**Returns:** true

if the tree root is visible

- setShowsRootHandles

```java
protected void setShowsRootHandles​(boolean newValue)
```

Determines whether the node handles are to be displayed.

**Parameters:** newValue

- the new value

- getShowsRootHandles

```java
protected boolean getShowsRootHandles()
```

Returns

true

if the root handles are to be displayed.

**Returns:** true

if the root handles are to be displayed

- setCellEditor

```java
protected void setCellEditor​(
TreeCellEditor
editor)
```

Sets the cell editor.

**Parameters:** editor

- the new cell editor

- getCellEditor

```java
protected
TreeCellEditor
getCellEditor()
```

Returns an instance of

TreeCellEditor

.

**Returns:** an instance of

TreeCellEditor

- setEditable

```java
protected void setEditable​(boolean newValue)
```

Configures the receiver to allow, or not allow, editing.

**Parameters:** newValue

- the new value

- isEditable

```java
protected boolean isEditable()
```

Returns

true

if the tree is editable.

**Returns:** true

if the tree is editable

- setSelectionModel

```java
protected void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Resets the selection model. The appropriate listener are installed
on the model.

**Parameters:** newLSM

- new selection model

- getSelectionModel

```java
protected
TreeSelectionModel
getSelectionModel()
```

Returns the tree selection model.

**Returns:** the tree selection model

- getPathBounds

```java
public
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Specified by:** getPathBounds

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

- getPathForRow

```java
public
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

- getRowForPath

```java
public int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

- getRowCount

```java
public int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Specified by:** getRowCount

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

- getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getClosestPathForLocation

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

- isEditing

```java
public boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Specified by:** isEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

- stopEditing

```java
public boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Specified by:** stopEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

- cancelEditing

```java
public void cancelEditing​(
JTree
tree)
```

Cancels the current editing session.

**Specified by:** cancelEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object

- startEditingAtPath

```java
public void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Specified by:** startEditingAtPath

in class

TreeUI
**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

- getEditingPath

```java
public
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Specified by:** getEditingPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

- prepareForUIInstall

```java
protected void prepareForUIInstall()
```

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

- completeUIInstall

```java
protected void completeUIInstall()
```

Invoked from installUI after all the defaults/listeners have been
installed.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- installComponents

```java
protected void installComponents()
```

Intalls the subcomponents of the tree, which is the renderer pane.

- createNodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
createNodeDimensions()
```

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

**Returns:** an instance of

NodeDimensions

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a listener that is responsible that updates the UI based on
how the tree changes.

**Returns:** an instance of the

PropertyChangeListener

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates the listener responsible for updating the selection based on
mouse events.

**Returns:** an instance of the

MouseListener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a listener that is responsible for updating the display
when focus is lost/gained.

**Returns:** an instance of the

FocusListener

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the listener responsible for getting key events from
the tree.

**Returns:** an instance of the

KeyListener

- createSelectionModelPropertyChangeListener

```java
protected
PropertyChangeListener
createSelectionModelPropertyChangeListener()
```

Creates the listener responsible for getting property change
events from the selection model.

**Returns:** an instance of the

PropertyChangeListener

- createTreeSelectionListener

```java
protected
TreeSelectionListener
createTreeSelectionListener()
```

Creates the listener that updates the display based on selection change
methods.

**Returns:** an instance of the

TreeSelectionListener

- createCellEditorListener

```java
protected
CellEditorListener
createCellEditorListener()
```

Creates a listener to handle events from the current editor.

**Returns:** an instance of the

CellEditorListener

- createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates and returns a new ComponentHandler. This is used for
the large model to mark the validCachedPreferredSize as invalid
when the component moves.

**Returns:** an instance of the

ComponentListener

- createTreeExpansionListener

```java
protected
TreeExpansionListener
createTreeExpansionListener()
```

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

**Returns:** an instance of the

TreeExpansionListener

- createLayoutCache

```java
protected
AbstractLayoutCache
createLayoutCache()
```

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

**Returns:** the object responsible for managing what is expanded

- createCellRendererPane

```java
protected
CellRendererPane
createCellRendererPane()
```

Returns the renderer pane that renderer components are placed in.

**Returns:** an instance of the

CellRendererPane

- createDefaultCellEditor

```java
protected
TreeCellEditor
createDefaultCellEditor()
```

Creates a default cell editor.

**Returns:** a default cell editor

- createDefaultCellRenderer

```java
protected
TreeCellRenderer
createDefaultCellRenderer()
```

Returns the default cell renderer that is used to do the
stamping of each node.

**Returns:** an instance of

TreeCellRenderer

- createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Returns a listener that can update the tree when the model changes.

**Returns:** an instance of the

TreeModelListener

.

- prepareForUIUninstall

```java
protected void prepareForUIUninstall()
```

Invoked before unstallation of UI.

- completeUIUninstall

```java
protected void completeUIUninstall()
```

Uninstalls UI.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the renderer pane.

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

- isDropLine

```java
protected boolean isDropLine​(
JTree.DropLocation
loc)
```

Tells if a

DropLocation

should be indicated by a line between
nodes. This is meant for

javax.swing.DropMode.INSERT

and

javax.swing.DropMode.ON_OR_INSERT

drop modes.

**Parameters:** loc

- a

DropLocation
**Returns:** true

if the drop location should be shown as a line
**Since:** 1.7

- paintDropLine

```java
protected void paintDropLine​(
Graphics
g)
```

Paints the drop line.

**Parameters:** g

-

Graphics

object to draw on
**Since:** 1.7

- getDropLineRect

```java
protected
Rectangle
getDropLineRect​(
JTree.DropLocation
loc)
```

Returns a unbounding box for the drop line.

**Parameters:** loc

- a

DropLocation
**Returns:** bounding box for the drop line
**Since:** 1.7

- paintHorizontalPartOfLeg

```java
protected void paintHorizontalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the horizontal part of the leg. The receiver should
NOT modify

clipBounds

, or

insets

.

NOTE:

parentRow

can be -1 if the root is not visible.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

- paintVerticalPartOfLeg

```java
protected void paintVerticalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

TreePath
path)
```

Paints the vertical part of the leg. The receiver should
NOT modify

clipBounds

,

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** path

- a tree path

- paintExpandControl

```java
protected void paintExpandControl​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the expand (toggle) part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf

- paintRow

```java
protected void paintRow​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the renderer part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

- shouldPaintExpandControl

```java
protected boolean shouldPaintExpandControl​(
TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf
**Returns:** true

if the expand (toggle) control should be drawn
for the specified row

- paintVerticalLine

```java
protected void paintVerticalLine​(
Graphics
g,

JComponent
c,
int x,
int top,
int bottom)
```

Paints a vertical line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** x

- an X coordinate
**Parameters:** top

- an Y1 coordinate
**Parameters:** bottom

- an Y2 coordinate

- paintHorizontalLine

```java
protected void paintHorizontalLine​(
Graphics
g,

JComponent
c,
int y,
int left,
int right)
```

Paints a horizontal line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** y

- an Y coordinate
**Parameters:** left

- an X1 coordinate
**Parameters:** right

- an X2 coordinate

- getVerticalLegBuffer

```java
protected int getVerticalLegBuffer()
```

The vertical element of legs between nodes starts at the bottom of the
parent node by default. This method makes the leg start below that.

**Returns:** the vertical leg buffer

- getHorizontalLegBuffer

```java
protected int getHorizontalLegBuffer()
```

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default. This
method makes the leg end before that.

**Returns:** the horizontal leg buffer

- drawCentered

```java
protected void drawCentered​(
Component
c,

Graphics
graphics,

Icon
icon,
int x,
int y)
```

Draws the

icon

centered at (x,y).

**Parameters:** c

- a component
**Parameters:** graphics

- a graphics context
**Parameters:** icon

- an icon
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- drawDashedHorizontalLine

```java
protected void drawDashedHorizontalLine​(
Graphics
g,
int y,
int x1,
int x2)
```

Draws a horizontal dashed line. It is assumed

x1

<=

x2

.
If

x1

is greater than

x2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** y

- an Y coordinate
**Parameters:** x1

- an X1 coordinate
**Parameters:** x2

- an X2 coordinate

- drawDashedVerticalLine

```java
protected void drawDashedVerticalLine​(
Graphics
g,
int x,
int y1,
int y2)
```

Draws a vertical dashed line. It is assumed

y1

<=

y2

.
If

y1

is greater than

y2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y1

- an Y1 coordinate
**Parameters:** y2

- an Y2 coordinate

- getRowX

```java
protected int getRowX​(int row,
int depth)
```

Returns the location, along the x-axis, to render a particular row
at. The return value does not include any Insets specified on the JTree.
This does not check for the validity of the row or depth, it is assumed
to be correct and will not throw an Exception if the row or depth
doesn't match that of the tree.

**Parameters:** row

- Row to return x location for
**Parameters:** depth

- Depth of the row
**Returns:** amount to indent the given row.
**Since:** 1.5

- updateLayoutCacheExpandedNodes

```java
protected void updateLayoutCacheExpandedNodes()
```

Makes all the nodes that are expanded in JTree expanded in LayoutCache.
This invokes updateExpandedDescendants with the root path.

- updateExpandedDescendants

```java
protected void updateExpandedDescendants​(
TreePath
path)
```

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

**Parameters:** path

- a tree path

- getLastChildPath

```java
protected
TreePath
getLastChildPath​(
TreePath
parent)
```

Returns a path to the last child of

parent

.

**Parameters:** parent

- a tree path
**Returns:** a path to the last child of

parent

- updateDepthOffset

```java
protected void updateDepthOffset()
```

Updates how much each depth should be offset by.

- updateCellEditor

```java
protected void updateCellEditor()
```

Updates the cellEditor based on the editability of the JTree that
we're contained in. If the tree is editable but doesn't have a
cellEditor, a basic one will be used.

- updateRenderer

```java
protected void updateRenderer()
```

Messaged from the tree we're in when the renderer has changed.

- configureLayoutCache

```java
protected void configureLayoutCache()
```

Resets the TreeState instance based on the tree we're providing the
look and feel for.

- updateSize

```java
protected void updateSize()
```

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

- updateCachedPreferredSize

```java
protected void updateCachedPreferredSize()
```

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

- pathWasExpanded

```java
protected void pathWasExpanded​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has been expanded.

**Parameters:** path

- a tree path

- pathWasCollapsed

```java
protected void pathWasCollapsed​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has collapsed.

**Parameters:** path

- a tree path

- ensureRowsAreVisible

```java
protected void ensureRowsAreVisible​(int beginRow,
int endRow)
```

Ensures that the rows identified by

beginRow

through

endRow

are visible.

**Parameters:** beginRow

- the begin row
**Parameters:** endRow

- the end row

- setPreferredMinSize

```java
public void setPreferredMinSize​(
Dimension
newSize)
```

Sets the preferred minimum size.

**Parameters:** newSize

- the new preferred size

- getPreferredMinSize

```java
public
Dimension
getPreferredMinSize()
```

Returns the minimum preferred size.

**Returns:** the minimum preferred size

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size to represent the tree in the component
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c,
boolean checkConsistency)
```

Returns the preferred size to represent the tree in

c

. If

checkConsistency

is

true

checkConsistency

is messaged first.

**Parameters:** c

- a component
**Parameters:** checkConsistency

- if

true

consistency is checked
**Returns:** the preferred size to represent the tree in the component

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size for this component. Which will be
the min preferred size or 0, 0.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
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

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- completeEditing

```java
protected void completeEditing()
```

Messages to stop the editing session. If the UI the receiver
is providing the look and feel for returns true from

getInvokesStopCellEditing

, stopCellEditing will
invoked on the current editor. Then completeEditing will
be messaged with false, true, false to cancel any lingering
editing.

- completeEditing

```java
protected void completeEditing​(boolean messageStop,
boolean messageCancel,
boolean messageTree)
```

Stops the editing session. If

messageStop

is

true

the editor
is messaged with

stopEditing

, if

messageCancel

is

true

the editor is messaged with

cancelEditing

.
If

messageTree

is

true

the

treeModel

is messaged
with

valueForPathChanged

.

**Parameters:** messageStop

- message to stop editing
**Parameters:** messageCancel

- message to cancel editing
**Parameters:** messageTree

- message to tree

- startEditing

```java
protected boolean startEditing​(
TreePath
path,

MouseEvent
event)
```

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

This assumes that path is valid and visible.

**Parameters:** path

- a tree path
**Parameters:** event

- a mouse event
**Returns:** true

if the editing is successful

- checkForClickInExpandControl

```java
protected void checkForClickInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

- isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate
**Returns:** true

if the mouse cursor fall in the area of row that
is used to expand/collapse the node and the node is not a leaf.

- handleExpandControlClick

```java
protected void handleExpandControlClick​(
TreePath
path,
int mouseX,
int mouseY)
```

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

- toggleExpandState

```java
protected void toggleExpandState​(
TreePath
path)
```

Expands path if it is not expanded, or collapses row if it is expanded.
If expanding a path and

JTree

scrolls on expand,

ensureRowsAreVisible

is invoked to scroll as many of the children
to visible as possible (tries to scroll to last visible descendant of path).

**Parameters:** path

- a tree path

- isToggleSelectionEvent

```java
protected boolean isToggleSelectionEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should toggle the selection

- isMultiSelectEvent

```java
protected boolean isMultiSelectEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should select
from the anchor point.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should select
from the anchor point

- isToggleEvent

```java
protected boolean isToggleEvent​(
MouseEvent
event)
```

Returning

true

indicates the row under the mouse should be toggled
based on the event. This is invoked after

checkForClickInExpandControl

,
implying the location is not in the expand (toggle) control.

**Parameters:** event

- a mouse event
**Returns:** true

if the row under the mouse should be toggled

- selectPathForEvent

```java
protected void selectPathForEvent​(
TreePath
path,

MouseEvent
event)
```

Messaged to update the selection based on a

MouseEvent

over a
particular row. If the event is a toggle selection event, the
row is either selected, or deselected. If the event identifies
a multi selection event, the selection is updated from the
anchor point. Otherwise the row is selected, and if the event
specified a toggle event the row is expanded/collapsed.

**Parameters:** path

- the selected path
**Parameters:** event

- the mouse event

- isLeaf

```java
protected boolean isLeaf​(int row)
```

Returns

true

if the node at

row

is a leaf.

**Parameters:** row

- a row
**Returns:** true

if the node at

row

is a leaf

- updateLeadSelectionRow

```java
protected void updateLeadSelectionRow()
```

Updates the lead row of the selection.

**Since:** 1.7

- getLeadSelectionRow

```java
protected int getLeadSelectionRow()
```

Returns the lead row of the selection.

**Returns:** selection lead row
**Since:** 1.7

Field Detail

- collapsedIcon

```java
protected transient
Icon
collapsedIcon
```

The collapsed icon.

- expandedIcon

```java
protected transient
Icon
expandedIcon
```

The expanded icon.

- leftChildIndent

```java
protected int leftChildIndent
```

Distance between left margin and where vertical dashes will be
drawn.

- rightChildIndent

```java
protected int rightChildIndent
```

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

- totalChildIndent

```java
protected int totalChildIndent
```

Total distance that will be indented. The sum of leftChildIndent
and rightChildIndent.

- preferredMinSize

```java
protected
Dimension
preferredMinSize
```

Minimum preferred size.

- lastSelectedRow

```java
protected int lastSelectedRow
```

Index of the row that was last selected.

- tree

```java
protected
JTree
tree
```

Component that we're going to be drawing into.

- currentCellRenderer

```java
protected transient
TreeCellRenderer
currentCellRenderer
```

Renderer that is being used to do the actual cell drawing.

- createdRenderer

```java
protected boolean createdRenderer
```

Set to true if the renderer that is currently in the tree was
created by this instance.

- cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the tree.

- createdCellEditor

```java
protected boolean createdCellEditor
```

Set to true if editor that is currently in the tree was
created by this instance.

- stopEditingInCompleteEditing

```java
protected boolean stopEditingInCompleteEditing
```

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

Used to paint the TreeCellRenderer.

- preferredSize

```java
protected
Dimension
preferredSize
```

Size needed to completely display all the nodes.

- validCachedPreferredSize

```java
protected boolean validCachedPreferredSize
```

Is the preferredSize valid?

- treeState

```java
protected
AbstractLayoutCache
treeState
```

Object responsible for handling sizing and expanded issues.

- drawingCache

```java
protected
Hashtable
<
TreePath
,​
Boolean
> drawingCache
```

Used for minimizing the drawing of vertical lines.

- largeModel

```java
protected boolean largeModel
```

True if doing optimizations for a largeModel. Subclasses that
don't support this may wish to override createLayoutCache to not
return a FixedHeightLayoutCache instance.

- nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Reponsible for telling the TreeState the size needed for a node.

- treeModel

```java
protected
TreeModel
treeModel
```

Used to determine what to display.

- treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Model maintaining the selection.

- depthOffset

```java
protected int depthOffset
```

How much the depth should be offset to properly calculate
x locations. This is based on whether or not the root is visible,
and if the root handles are visible.

- editingComponent

```java
protected
Component
editingComponent
```

When editing, this will be the Component that is doing the actual
editing.

- editingPath

```java
protected
TreePath
editingPath
```

Path that is being edited.

- editingRow

```java
protected int editingRow
```

Row that is being edited. Should only be referenced if
editingComponent is not null.

- editorHasDifferentSize

```java
protected boolean editorHasDifferentSize
```

Set to true if the editor has a different size than the renderer.

---

#### Field Detail

collapsedIcon

```java
protected transient
Icon
collapsedIcon
```

The collapsed icon.

---

#### collapsedIcon

protected transient

Icon

collapsedIcon

The collapsed icon.

expandedIcon

```java
protected transient
Icon
expandedIcon
```

The expanded icon.

---

#### expandedIcon

protected transient

Icon

expandedIcon

The expanded icon.

leftChildIndent

```java
protected int leftChildIndent
```

Distance between left margin and where vertical dashes will be
drawn.

---

#### leftChildIndent

protected int leftChildIndent

Distance between left margin and where vertical dashes will be
drawn.

rightChildIndent

```java
protected int rightChildIndent
```

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

---

#### rightChildIndent

protected int rightChildIndent

Distance to add to leftChildIndent to determine where cell
contents will be drawn.

totalChildIndent

```java
protected int totalChildIndent
```

Total distance that will be indented. The sum of leftChildIndent
and rightChildIndent.

---

#### totalChildIndent

protected int totalChildIndent

Total distance that will be indented. The sum of leftChildIndent
and rightChildIndent.

preferredMinSize

```java
protected
Dimension
preferredMinSize
```

Minimum preferred size.

---

#### preferredMinSize

protected

Dimension

preferredMinSize

Minimum preferred size.

lastSelectedRow

```java
protected int lastSelectedRow
```

Index of the row that was last selected.

---

#### lastSelectedRow

protected int lastSelectedRow

Index of the row that was last selected.

tree

```java
protected
JTree
tree
```

Component that we're going to be drawing into.

---

#### tree

protected

JTree

tree

Component that we're going to be drawing into.

currentCellRenderer

```java
protected transient
TreeCellRenderer
currentCellRenderer
```

Renderer that is being used to do the actual cell drawing.

---

#### currentCellRenderer

protected transient

TreeCellRenderer

currentCellRenderer

Renderer that is being used to do the actual cell drawing.

createdRenderer

```java
protected boolean createdRenderer
```

Set to true if the renderer that is currently in the tree was
created by this instance.

---

#### createdRenderer

protected boolean createdRenderer

Set to true if the renderer that is currently in the tree was
created by this instance.

cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the tree.

---

#### cellEditor

protected transient

TreeCellEditor

cellEditor

Editor for the tree.

createdCellEditor

```java
protected boolean createdCellEditor
```

Set to true if editor that is currently in the tree was
created by this instance.

---

#### createdCellEditor

protected boolean createdCellEditor

Set to true if editor that is currently in the tree was
created by this instance.

stopEditingInCompleteEditing

```java
protected boolean stopEditingInCompleteEditing
```

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

---

#### stopEditingInCompleteEditing

protected boolean stopEditingInCompleteEditing

Set to false when editing and shouldSelectCell() returns true meaning
the node should be selected before editing, used in completeEditing.

rendererPane

```java
protected
CellRendererPane
rendererPane
```

Used to paint the TreeCellRenderer.

---

#### rendererPane

protected

CellRendererPane

rendererPane

Used to paint the TreeCellRenderer.

preferredSize

```java
protected
Dimension
preferredSize
```

Size needed to completely display all the nodes.

---

#### preferredSize

protected

Dimension

preferredSize

Size needed to completely display all the nodes.

validCachedPreferredSize

```java
protected boolean validCachedPreferredSize
```

Is the preferredSize valid?

---

#### validCachedPreferredSize

protected boolean validCachedPreferredSize

Is the preferredSize valid?

treeState

```java
protected
AbstractLayoutCache
treeState
```

Object responsible for handling sizing and expanded issues.

---

#### treeState

protected

AbstractLayoutCache

treeState

Object responsible for handling sizing and expanded issues.

drawingCache

```java
protected
Hashtable
<
TreePath
,​
Boolean
> drawingCache
```

Used for minimizing the drawing of vertical lines.

---

#### drawingCache

protected

Hashtable

<

TreePath

,​

Boolean

> drawingCache

Used for minimizing the drawing of vertical lines.

largeModel

```java
protected boolean largeModel
```

True if doing optimizations for a largeModel. Subclasses that
don't support this may wish to override createLayoutCache to not
return a FixedHeightLayoutCache instance.

---

#### largeModel

protected boolean largeModel

True if doing optimizations for a largeModel. Subclasses that
don't support this may wish to override createLayoutCache to not
return a FixedHeightLayoutCache instance.

nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Reponsible for telling the TreeState the size needed for a node.

---

#### nodeDimensions

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Reponsible for telling the TreeState the size needed for a node.

treeModel

```java
protected
TreeModel
treeModel
```

Used to determine what to display.

---

#### treeModel

protected

TreeModel

treeModel

Used to determine what to display.

treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Model maintaining the selection.

---

#### treeSelectionModel

protected

TreeSelectionModel

treeSelectionModel

Model maintaining the selection.

depthOffset

```java
protected int depthOffset
```

How much the depth should be offset to properly calculate
x locations. This is based on whether or not the root is visible,
and if the root handles are visible.

---

#### depthOffset

protected int depthOffset

How much the depth should be offset to properly calculate
x locations. This is based on whether or not the root is visible,
and if the root handles are visible.

editingComponent

```java
protected
Component
editingComponent
```

When editing, this will be the Component that is doing the actual
editing.

---

#### editingComponent

protected

Component

editingComponent

When editing, this will be the Component that is doing the actual
editing.

editingPath

```java
protected
TreePath
editingPath
```

Path that is being edited.

---

#### editingPath

protected

TreePath

editingPath

Path that is being edited.

editingRow

```java
protected int editingRow
```

Row that is being edited. Should only be referenced if
editingComponent is not null.

---

#### editingRow

protected int editingRow

Row that is being edited. Should only be referenced if
editingComponent is not null.

editorHasDifferentSize

```java
protected boolean editorHasDifferentSize
```

Set to true if the editor has a different size than the renderer.

---

#### editorHasDifferentSize

protected boolean editorHasDifferentSize

Set to true if the editor has a different size than the renderer.

Constructor Detail

- BasicTreeUI

```java
public BasicTreeUI()
```

Constructs a new instance of

BasicTreeUI

.

---

#### Constructor Detail

BasicTreeUI

```java
public BasicTreeUI()
```

Constructs a new instance of

BasicTreeUI

.

---

#### BasicTreeUI

public BasicTreeUI()

Constructs a new instance of

BasicTreeUI

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

Constructs a new instance of

BasicTreeUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicTreeUI

- getHashColor

```java
protected
Color
getHashColor()
```

Returns the hash color.

**Returns:** the hash color

- setHashColor

```java
protected void setHashColor​(
Color
color)
```

Sets the hash color.

**Parameters:** color

- the hash color

- setLeftChildIndent

```java
public void setLeftChildIndent​(int newAmount)
```

Sets the left child indent.

**Parameters:** newAmount

- the left child indent

- getLeftChildIndent

```java
public int getLeftChildIndent()
```

Returns the left child indent.

**Returns:** the left child indent

- setRightChildIndent

```java
public void setRightChildIndent​(int newAmount)
```

Sets the right child indent.

**Parameters:** newAmount

- the right child indent

- getRightChildIndent

```java
public int getRightChildIndent()
```

Returns the right child indent.

**Returns:** the right child indent

- setExpandedIcon

```java
public void setExpandedIcon​(
Icon
newG)
```

Sets the expanded icon.

**Parameters:** newG

- the expanded icon

- getExpandedIcon

```java
public
Icon
getExpandedIcon()
```

Returns the expanded icon.

**Returns:** the expanded icon

- setCollapsedIcon

```java
public void setCollapsedIcon​(
Icon
newG)
```

Sets the collapsed icon.

**Parameters:** newG

- the collapsed icon

- getCollapsedIcon

```java
public
Icon
getCollapsedIcon()
```

Returns the collapsed icon.

**Returns:** the collapsed icon

- setLargeModel

```java
protected void setLargeModel​(boolean largeModel)
```

Updates the componentListener, if necessary.

**Parameters:** largeModel

- the new value

- isLargeModel

```java
protected boolean isLargeModel()
```

Returns

true

if large model is set.

**Returns:** true

if large model is set

- setRowHeight

```java
protected void setRowHeight​(int rowHeight)
```

Sets the row height, this is forwarded to the treeState.

**Parameters:** rowHeight

- the row height

- getRowHeight

```java
protected int getRowHeight()
```

Returns the row height.

**Returns:** the row height

- setCellRenderer

```java
protected void setCellRenderer​(
TreeCellRenderer
tcr)
```

Sets the

TreeCellRenderer

to

tcr

. This invokes

updateRenderer

.

**Parameters:** tcr

- the new value

- getCellRenderer

```java
protected
TreeCellRenderer
getCellRenderer()
```

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

**Returns:** an instance of

TreeCellRenderer

- setModel

```java
protected void setModel​(
TreeModel
model)
```

Sets the

TreeModel

.

**Parameters:** model

- the new value

- getModel

```java
protected
TreeModel
getModel()
```

Returns the tree model.

**Returns:** the tree model

- setRootVisible

```java
protected void setRootVisible​(boolean newValue)
```

Sets the root to being visible.

**Parameters:** newValue

- the new value

- isRootVisible

```java
protected boolean isRootVisible()
```

Returns

true

if the tree root is visible.

**Returns:** true

if the tree root is visible

- setShowsRootHandles

```java
protected void setShowsRootHandles​(boolean newValue)
```

Determines whether the node handles are to be displayed.

**Parameters:** newValue

- the new value

- getShowsRootHandles

```java
protected boolean getShowsRootHandles()
```

Returns

true

if the root handles are to be displayed.

**Returns:** true

if the root handles are to be displayed

- setCellEditor

```java
protected void setCellEditor​(
TreeCellEditor
editor)
```

Sets the cell editor.

**Parameters:** editor

- the new cell editor

- getCellEditor

```java
protected
TreeCellEditor
getCellEditor()
```

Returns an instance of

TreeCellEditor

.

**Returns:** an instance of

TreeCellEditor

- setEditable

```java
protected void setEditable​(boolean newValue)
```

Configures the receiver to allow, or not allow, editing.

**Parameters:** newValue

- the new value

- isEditable

```java
protected boolean isEditable()
```

Returns

true

if the tree is editable.

**Returns:** true

if the tree is editable

- setSelectionModel

```java
protected void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Resets the selection model. The appropriate listener are installed
on the model.

**Parameters:** newLSM

- new selection model

- getSelectionModel

```java
protected
TreeSelectionModel
getSelectionModel()
```

Returns the tree selection model.

**Returns:** the tree selection model

- getPathBounds

```java
public
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Specified by:** getPathBounds

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

- getPathForRow

```java
public
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

- getRowForPath

```java
public int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

- getRowCount

```java
public int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Specified by:** getRowCount

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

- getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getClosestPathForLocation

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

- isEditing

```java
public boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Specified by:** isEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

- stopEditing

```java
public boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Specified by:** stopEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

- cancelEditing

```java
public void cancelEditing​(
JTree
tree)
```

Cancels the current editing session.

**Specified by:** cancelEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object

- startEditingAtPath

```java
public void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Specified by:** startEditingAtPath

in class

TreeUI
**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

- getEditingPath

```java
public
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Specified by:** getEditingPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

- prepareForUIInstall

```java
protected void prepareForUIInstall()
```

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

- completeUIInstall

```java
protected void completeUIInstall()
```

Invoked from installUI after all the defaults/listeners have been
installed.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- installComponents

```java
protected void installComponents()
```

Intalls the subcomponents of the tree, which is the renderer pane.

- createNodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
createNodeDimensions()
```

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

**Returns:** an instance of

NodeDimensions

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a listener that is responsible that updates the UI based on
how the tree changes.

**Returns:** an instance of the

PropertyChangeListener

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates the listener responsible for updating the selection based on
mouse events.

**Returns:** an instance of the

MouseListener

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a listener that is responsible for updating the display
when focus is lost/gained.

**Returns:** an instance of the

FocusListener

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the listener responsible for getting key events from
the tree.

**Returns:** an instance of the

KeyListener

- createSelectionModelPropertyChangeListener

```java
protected
PropertyChangeListener
createSelectionModelPropertyChangeListener()
```

Creates the listener responsible for getting property change
events from the selection model.

**Returns:** an instance of the

PropertyChangeListener

- createTreeSelectionListener

```java
protected
TreeSelectionListener
createTreeSelectionListener()
```

Creates the listener that updates the display based on selection change
methods.

**Returns:** an instance of the

TreeSelectionListener

- createCellEditorListener

```java
protected
CellEditorListener
createCellEditorListener()
```

Creates a listener to handle events from the current editor.

**Returns:** an instance of the

CellEditorListener

- createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates and returns a new ComponentHandler. This is used for
the large model to mark the validCachedPreferredSize as invalid
when the component moves.

**Returns:** an instance of the

ComponentListener

- createTreeExpansionListener

```java
protected
TreeExpansionListener
createTreeExpansionListener()
```

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

**Returns:** an instance of the

TreeExpansionListener

- createLayoutCache

```java
protected
AbstractLayoutCache
createLayoutCache()
```

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

**Returns:** the object responsible for managing what is expanded

- createCellRendererPane

```java
protected
CellRendererPane
createCellRendererPane()
```

Returns the renderer pane that renderer components are placed in.

**Returns:** an instance of the

CellRendererPane

- createDefaultCellEditor

```java
protected
TreeCellEditor
createDefaultCellEditor()
```

Creates a default cell editor.

**Returns:** a default cell editor

- createDefaultCellRenderer

```java
protected
TreeCellRenderer
createDefaultCellRenderer()
```

Returns the default cell renderer that is used to do the
stamping of each node.

**Returns:** an instance of

TreeCellRenderer

- createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Returns a listener that can update the tree when the model changes.

**Returns:** an instance of the

TreeModelListener

.

- prepareForUIUninstall

```java
protected void prepareForUIUninstall()
```

Invoked before unstallation of UI.

- completeUIUninstall

```java
protected void completeUIUninstall()
```

Uninstalls UI.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the renderer pane.

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

- isDropLine

```java
protected boolean isDropLine​(
JTree.DropLocation
loc)
```

Tells if a

DropLocation

should be indicated by a line between
nodes. This is meant for

javax.swing.DropMode.INSERT

and

javax.swing.DropMode.ON_OR_INSERT

drop modes.

**Parameters:** loc

- a

DropLocation
**Returns:** true

if the drop location should be shown as a line
**Since:** 1.7

- paintDropLine

```java
protected void paintDropLine​(
Graphics
g)
```

Paints the drop line.

**Parameters:** g

-

Graphics

object to draw on
**Since:** 1.7

- getDropLineRect

```java
protected
Rectangle
getDropLineRect​(
JTree.DropLocation
loc)
```

Returns a unbounding box for the drop line.

**Parameters:** loc

- a

DropLocation
**Returns:** bounding box for the drop line
**Since:** 1.7

- paintHorizontalPartOfLeg

```java
protected void paintHorizontalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the horizontal part of the leg. The receiver should
NOT modify

clipBounds

, or

insets

.

NOTE:

parentRow

can be -1 if the root is not visible.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

- paintVerticalPartOfLeg

```java
protected void paintVerticalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

TreePath
path)
```

Paints the vertical part of the leg. The receiver should
NOT modify

clipBounds

,

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** path

- a tree path

- paintExpandControl

```java
protected void paintExpandControl​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the expand (toggle) part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf

- paintRow

```java
protected void paintRow​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the renderer part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

- shouldPaintExpandControl

```java
protected boolean shouldPaintExpandControl​(
TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf
**Returns:** true

if the expand (toggle) control should be drawn
for the specified row

- paintVerticalLine

```java
protected void paintVerticalLine​(
Graphics
g,

JComponent
c,
int x,
int top,
int bottom)
```

Paints a vertical line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** x

- an X coordinate
**Parameters:** top

- an Y1 coordinate
**Parameters:** bottom

- an Y2 coordinate

- paintHorizontalLine

```java
protected void paintHorizontalLine​(
Graphics
g,

JComponent
c,
int y,
int left,
int right)
```

Paints a horizontal line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** y

- an Y coordinate
**Parameters:** left

- an X1 coordinate
**Parameters:** right

- an X2 coordinate

- getVerticalLegBuffer

```java
protected int getVerticalLegBuffer()
```

The vertical element of legs between nodes starts at the bottom of the
parent node by default. This method makes the leg start below that.

**Returns:** the vertical leg buffer

- getHorizontalLegBuffer

```java
protected int getHorizontalLegBuffer()
```

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default. This
method makes the leg end before that.

**Returns:** the horizontal leg buffer

- drawCentered

```java
protected void drawCentered​(
Component
c,

Graphics
graphics,

Icon
icon,
int x,
int y)
```

Draws the

icon

centered at (x,y).

**Parameters:** c

- a component
**Parameters:** graphics

- a graphics context
**Parameters:** icon

- an icon
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

- drawDashedHorizontalLine

```java
protected void drawDashedHorizontalLine​(
Graphics
g,
int y,
int x1,
int x2)
```

Draws a horizontal dashed line. It is assumed

x1

<=

x2

.
If

x1

is greater than

x2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** y

- an Y coordinate
**Parameters:** x1

- an X1 coordinate
**Parameters:** x2

- an X2 coordinate

- drawDashedVerticalLine

```java
protected void drawDashedVerticalLine​(
Graphics
g,
int x,
int y1,
int y2)
```

Draws a vertical dashed line. It is assumed

y1

<=

y2

.
If

y1

is greater than

y2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y1

- an Y1 coordinate
**Parameters:** y2

- an Y2 coordinate

- getRowX

```java
protected int getRowX​(int row,
int depth)
```

Returns the location, along the x-axis, to render a particular row
at. The return value does not include any Insets specified on the JTree.
This does not check for the validity of the row or depth, it is assumed
to be correct and will not throw an Exception if the row or depth
doesn't match that of the tree.

**Parameters:** row

- Row to return x location for
**Parameters:** depth

- Depth of the row
**Returns:** amount to indent the given row.
**Since:** 1.5

- updateLayoutCacheExpandedNodes

```java
protected void updateLayoutCacheExpandedNodes()
```

Makes all the nodes that are expanded in JTree expanded in LayoutCache.
This invokes updateExpandedDescendants with the root path.

- updateExpandedDescendants

```java
protected void updateExpandedDescendants​(
TreePath
path)
```

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

**Parameters:** path

- a tree path

- getLastChildPath

```java
protected
TreePath
getLastChildPath​(
TreePath
parent)
```

Returns a path to the last child of

parent

.

**Parameters:** parent

- a tree path
**Returns:** a path to the last child of

parent

- updateDepthOffset

```java
protected void updateDepthOffset()
```

Updates how much each depth should be offset by.

- updateCellEditor

```java
protected void updateCellEditor()
```

Updates the cellEditor based on the editability of the JTree that
we're contained in. If the tree is editable but doesn't have a
cellEditor, a basic one will be used.

- updateRenderer

```java
protected void updateRenderer()
```

Messaged from the tree we're in when the renderer has changed.

- configureLayoutCache

```java
protected void configureLayoutCache()
```

Resets the TreeState instance based on the tree we're providing the
look and feel for.

- updateSize

```java
protected void updateSize()
```

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

- updateCachedPreferredSize

```java
protected void updateCachedPreferredSize()
```

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

- pathWasExpanded

```java
protected void pathWasExpanded​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has been expanded.

**Parameters:** path

- a tree path

- pathWasCollapsed

```java
protected void pathWasCollapsed​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has collapsed.

**Parameters:** path

- a tree path

- ensureRowsAreVisible

```java
protected void ensureRowsAreVisible​(int beginRow,
int endRow)
```

Ensures that the rows identified by

beginRow

through

endRow

are visible.

**Parameters:** beginRow

- the begin row
**Parameters:** endRow

- the end row

- setPreferredMinSize

```java
public void setPreferredMinSize​(
Dimension
newSize)
```

Sets the preferred minimum size.

**Parameters:** newSize

- the new preferred size

- getPreferredMinSize

```java
public
Dimension
getPreferredMinSize()
```

Returns the minimum preferred size.

**Returns:** the minimum preferred size

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size to represent the tree in the component
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c,
boolean checkConsistency)
```

Returns the preferred size to represent the tree in

c

. If

checkConsistency

is

true

checkConsistency

is messaged first.

**Parameters:** c

- a component
**Parameters:** checkConsistency

- if

true

consistency is checked
**Returns:** the preferred size to represent the tree in the component

- getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size for this component. Which will be
the min preferred size or 0, 0.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
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

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
**See Also:** JComponent.getMaximumSize()

,

LayoutManager2.maximumLayoutSize(java.awt.Container)

- completeEditing

```java
protected void completeEditing()
```

Messages to stop the editing session. If the UI the receiver
is providing the look and feel for returns true from

getInvokesStopCellEditing

, stopCellEditing will
invoked on the current editor. Then completeEditing will
be messaged with false, true, false to cancel any lingering
editing.

- completeEditing

```java
protected void completeEditing​(boolean messageStop,
boolean messageCancel,
boolean messageTree)
```

Stops the editing session. If

messageStop

is

true

the editor
is messaged with

stopEditing

, if

messageCancel

is

true

the editor is messaged with

cancelEditing

.
If

messageTree

is

true

the

treeModel

is messaged
with

valueForPathChanged

.

**Parameters:** messageStop

- message to stop editing
**Parameters:** messageCancel

- message to cancel editing
**Parameters:** messageTree

- message to tree

- startEditing

```java
protected boolean startEditing​(
TreePath
path,

MouseEvent
event)
```

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

This assumes that path is valid and visible.

**Parameters:** path

- a tree path
**Parameters:** event

- a mouse event
**Returns:** true

if the editing is successful

- checkForClickInExpandControl

```java
protected void checkForClickInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

- isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate
**Returns:** true

if the mouse cursor fall in the area of row that
is used to expand/collapse the node and the node is not a leaf.

- handleExpandControlClick

```java
protected void handleExpandControlClick​(
TreePath
path,
int mouseX,
int mouseY)
```

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

- toggleExpandState

```java
protected void toggleExpandState​(
TreePath
path)
```

Expands path if it is not expanded, or collapses row if it is expanded.
If expanding a path and

JTree

scrolls on expand,

ensureRowsAreVisible

is invoked to scroll as many of the children
to visible as possible (tries to scroll to last visible descendant of path).

**Parameters:** path

- a tree path

- isToggleSelectionEvent

```java
protected boolean isToggleSelectionEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should toggle the selection

- isMultiSelectEvent

```java
protected boolean isMultiSelectEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should select
from the anchor point.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should select
from the anchor point

- isToggleEvent

```java
protected boolean isToggleEvent​(
MouseEvent
event)
```

Returning

true

indicates the row under the mouse should be toggled
based on the event. This is invoked after

checkForClickInExpandControl

,
implying the location is not in the expand (toggle) control.

**Parameters:** event

- a mouse event
**Returns:** true

if the row under the mouse should be toggled

- selectPathForEvent

```java
protected void selectPathForEvent​(
TreePath
path,

MouseEvent
event)
```

Messaged to update the selection based on a

MouseEvent

over a
particular row. If the event is a toggle selection event, the
row is either selected, or deselected. If the event identifies
a multi selection event, the selection is updated from the
anchor point. Otherwise the row is selected, and if the event
specified a toggle event the row is expanded/collapsed.

**Parameters:** path

- the selected path
**Parameters:** event

- the mouse event

- isLeaf

```java
protected boolean isLeaf​(int row)
```

Returns

true

if the node at

row

is a leaf.

**Parameters:** row

- a row
**Returns:** true

if the node at

row

is a leaf

- updateLeadSelectionRow

```java
protected void updateLeadSelectionRow()
```

Updates the lead row of the selection.

**Since:** 1.7

- getLeadSelectionRow

```java
protected int getLeadSelectionRow()
```

Returns the lead row of the selection.

**Returns:** selection lead row
**Since:** 1.7

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

Constructs a new instance of

BasicTreeUI

.

**Parameters:** x

- a component
**Returns:** a new instance of

BasicTreeUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

x)

Constructs a new instance of

BasicTreeUI

.

getHashColor

```java
protected
Color
getHashColor()
```

Returns the hash color.

**Returns:** the hash color

---

#### getHashColor

protected

Color

getHashColor()

Returns the hash color.

setHashColor

```java
protected void setHashColor​(
Color
color)
```

Sets the hash color.

**Parameters:** color

- the hash color

---

#### setHashColor

protected void setHashColor​(

Color

color)

Sets the hash color.

setLeftChildIndent

```java
public void setLeftChildIndent​(int newAmount)
```

Sets the left child indent.

**Parameters:** newAmount

- the left child indent

---

#### setLeftChildIndent

public void setLeftChildIndent​(int newAmount)

Sets the left child indent.

getLeftChildIndent

```java
public int getLeftChildIndent()
```

Returns the left child indent.

**Returns:** the left child indent

---

#### getLeftChildIndent

public int getLeftChildIndent()

Returns the left child indent.

setRightChildIndent

```java
public void setRightChildIndent​(int newAmount)
```

Sets the right child indent.

**Parameters:** newAmount

- the right child indent

---

#### setRightChildIndent

public void setRightChildIndent​(int newAmount)

Sets the right child indent.

getRightChildIndent

```java
public int getRightChildIndent()
```

Returns the right child indent.

**Returns:** the right child indent

---

#### getRightChildIndent

public int getRightChildIndent()

Returns the right child indent.

setExpandedIcon

```java
public void setExpandedIcon​(
Icon
newG)
```

Sets the expanded icon.

**Parameters:** newG

- the expanded icon

---

#### setExpandedIcon

public void setExpandedIcon​(

Icon

newG)

Sets the expanded icon.

getExpandedIcon

```java
public
Icon
getExpandedIcon()
```

Returns the expanded icon.

**Returns:** the expanded icon

---

#### getExpandedIcon

public

Icon

getExpandedIcon()

Returns the expanded icon.

setCollapsedIcon

```java
public void setCollapsedIcon​(
Icon
newG)
```

Sets the collapsed icon.

**Parameters:** newG

- the collapsed icon

---

#### setCollapsedIcon

public void setCollapsedIcon​(

Icon

newG)

Sets the collapsed icon.

getCollapsedIcon

```java
public
Icon
getCollapsedIcon()
```

Returns the collapsed icon.

**Returns:** the collapsed icon

---

#### getCollapsedIcon

public

Icon

getCollapsedIcon()

Returns the collapsed icon.

setLargeModel

```java
protected void setLargeModel​(boolean largeModel)
```

Updates the componentListener, if necessary.

**Parameters:** largeModel

- the new value

---

#### setLargeModel

protected void setLargeModel​(boolean largeModel)

Updates the componentListener, if necessary.

isLargeModel

```java
protected boolean isLargeModel()
```

Returns

true

if large model is set.

**Returns:** true

if large model is set

---

#### isLargeModel

protected boolean isLargeModel()

Returns

true

if large model is set.

setRowHeight

```java
protected void setRowHeight​(int rowHeight)
```

Sets the row height, this is forwarded to the treeState.

**Parameters:** rowHeight

- the row height

---

#### setRowHeight

protected void setRowHeight​(int rowHeight)

Sets the row height, this is forwarded to the treeState.

getRowHeight

```java
protected int getRowHeight()
```

Returns the row height.

**Returns:** the row height

---

#### getRowHeight

protected int getRowHeight()

Returns the row height.

setCellRenderer

```java
protected void setCellRenderer​(
TreeCellRenderer
tcr)
```

Sets the

TreeCellRenderer

to

tcr

. This invokes

updateRenderer

.

**Parameters:** tcr

- the new value

---

#### setCellRenderer

protected void setCellRenderer​(

TreeCellRenderer

tcr)

Sets the

TreeCellRenderer

to

tcr

. This invokes

updateRenderer

.

getCellRenderer

```java
protected
TreeCellRenderer
getCellRenderer()
```

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

**Returns:** an instance of

TreeCellRenderer

---

#### getCellRenderer

protected

TreeCellRenderer

getCellRenderer()

Return

currentCellRenderer

, which will either be the trees
renderer, or

defaultCellRenderer

, which ever wasn't null.

setModel

```java
protected void setModel​(
TreeModel
model)
```

Sets the

TreeModel

.

**Parameters:** model

- the new value

---

#### setModel

protected void setModel​(

TreeModel

model)

Sets the

TreeModel

.

getModel

```java
protected
TreeModel
getModel()
```

Returns the tree model.

**Returns:** the tree model

---

#### getModel

protected

TreeModel

getModel()

Returns the tree model.

setRootVisible

```java
protected void setRootVisible​(boolean newValue)
```

Sets the root to being visible.

**Parameters:** newValue

- the new value

---

#### setRootVisible

protected void setRootVisible​(boolean newValue)

Sets the root to being visible.

isRootVisible

```java
protected boolean isRootVisible()
```

Returns

true

if the tree root is visible.

**Returns:** true

if the tree root is visible

---

#### isRootVisible

protected boolean isRootVisible()

Returns

true

if the tree root is visible.

setShowsRootHandles

```java
protected void setShowsRootHandles​(boolean newValue)
```

Determines whether the node handles are to be displayed.

**Parameters:** newValue

- the new value

---

#### setShowsRootHandles

protected void setShowsRootHandles​(boolean newValue)

Determines whether the node handles are to be displayed.

getShowsRootHandles

```java
protected boolean getShowsRootHandles()
```

Returns

true

if the root handles are to be displayed.

**Returns:** true

if the root handles are to be displayed

---

#### getShowsRootHandles

protected boolean getShowsRootHandles()

Returns

true

if the root handles are to be displayed.

setCellEditor

```java
protected void setCellEditor​(
TreeCellEditor
editor)
```

Sets the cell editor.

**Parameters:** editor

- the new cell editor

---

#### setCellEditor

protected void setCellEditor​(

TreeCellEditor

editor)

Sets the cell editor.

getCellEditor

```java
protected
TreeCellEditor
getCellEditor()
```

Returns an instance of

TreeCellEditor

.

**Returns:** an instance of

TreeCellEditor

---

#### getCellEditor

protected

TreeCellEditor

getCellEditor()

Returns an instance of

TreeCellEditor

.

setEditable

```java
protected void setEditable​(boolean newValue)
```

Configures the receiver to allow, or not allow, editing.

**Parameters:** newValue

- the new value

---

#### setEditable

protected void setEditable​(boolean newValue)

Configures the receiver to allow, or not allow, editing.

isEditable

```java
protected boolean isEditable()
```

Returns

true

if the tree is editable.

**Returns:** true

if the tree is editable

---

#### isEditable

protected boolean isEditable()

Returns

true

if the tree is editable.

setSelectionModel

```java
protected void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Resets the selection model. The appropriate listener are installed
on the model.

**Parameters:** newLSM

- new selection model

---

#### setSelectionModel

protected void setSelectionModel​(

TreeSelectionModel

newLSM)

Resets the selection model. The appropriate listener are installed
on the model.

getSelectionModel

```java
protected
TreeSelectionModel
getSelectionModel()
```

Returns the tree selection model.

**Returns:** the tree selection model

---

#### getSelectionModel

protected

TreeSelectionModel

getSelectionModel()

Returns the tree selection model.

getPathBounds

```java
public
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Specified by:** getPathBounds

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

---

#### getPathBounds

public

Rectangle

getPathBounds​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

getPathForRow

```java
public
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

---

#### getPathForRow

public

TreePath

getPathForRow​(

JTree

tree,
int row)

Returns the path for passed in row. If row is not visible
null is returned.

getRowForPath

```java
public int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

---

#### getRowForPath

public int getRowForPath​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

getRowCount

```java
public int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Specified by:** getRowCount

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

---

#### getRowCount

public int getRowCount​(

JTree

tree)

Returns the number of rows that are being displayed.

getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getClosestPathForLocation

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

---

#### getClosestPathForLocation

public

TreePath

getClosestPathForLocation​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

isEditing

```java
public boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Specified by:** isEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

---

#### isEditing

public boolean isEditing​(

JTree

tree)

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

stopEditing

```java
public boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Specified by:** stopEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

---

#### stopEditing

public boolean stopEditing​(

JTree

tree)

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

cancelEditing

```java
public void cancelEditing​(
JTree
tree)
```

Cancels the current editing session.

**Specified by:** cancelEditing

in class

TreeUI
**Parameters:** tree

- a

JTree

object

---

#### cancelEditing

public void cancelEditing​(

JTree

tree)

Cancels the current editing session.

startEditingAtPath

```java
public void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Specified by:** startEditingAtPath

in class

TreeUI
**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

---

#### startEditingAtPath

public void startEditingAtPath​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

getEditingPath

```java
public
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Specified by:** getEditingPath

in class

TreeUI
**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

---

#### getEditingPath

public

TreePath

getEditingPath​(

JTree

tree)

Returns the path to the element that is being edited.

prepareForUIInstall

```java
protected void prepareForUIInstall()
```

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

---

#### prepareForUIInstall

protected void prepareForUIInstall()

Invoked after the

tree

instance variable has been
set, but before any defaults/listeners have been installed.

completeUIInstall

```java
protected void completeUIInstall()
```

Invoked from installUI after all the defaults/listeners have been
installed.

---

#### completeUIInstall

protected void completeUIInstall()

Invoked from installUI after all the defaults/listeners have been
installed.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard actions.

installComponents

```java
protected void installComponents()
```

Intalls the subcomponents of the tree, which is the renderer pane.

---

#### installComponents

protected void installComponents()

Intalls the subcomponents of the tree, which is the renderer pane.

createNodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
createNodeDimensions()
```

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

**Returns:** an instance of

NodeDimensions

---

#### createNodeDimensions

protected

AbstractLayoutCache.NodeDimensions

createNodeDimensions()

Creates an instance of

NodeDimensions

that is able to determine
the size of a given node in the tree.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a listener that is responsible that updates the UI based on
how the tree changes.

**Returns:** an instance of the

PropertyChangeListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a listener that is responsible that updates the UI based on
how the tree changes.

createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates the listener responsible for updating the selection based on
mouse events.

**Returns:** an instance of the

MouseListener

---

#### createMouseListener

protected

MouseListener

createMouseListener()

Creates the listener responsible for updating the selection based on
mouse events.

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Creates a listener that is responsible for updating the display
when focus is lost/gained.

**Returns:** an instance of the

FocusListener

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Creates a listener that is responsible for updating the display
when focus is lost/gained.

createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the listener responsible for getting key events from
the tree.

**Returns:** an instance of the

KeyListener

---

#### createKeyListener

protected

KeyListener

createKeyListener()

Creates the listener responsible for getting key events from
the tree.

createSelectionModelPropertyChangeListener

```java
protected
PropertyChangeListener
createSelectionModelPropertyChangeListener()
```

Creates the listener responsible for getting property change
events from the selection model.

**Returns:** an instance of the

PropertyChangeListener

---

#### createSelectionModelPropertyChangeListener

protected

PropertyChangeListener

createSelectionModelPropertyChangeListener()

Creates the listener responsible for getting property change
events from the selection model.

createTreeSelectionListener

```java
protected
TreeSelectionListener
createTreeSelectionListener()
```

Creates the listener that updates the display based on selection change
methods.

**Returns:** an instance of the

TreeSelectionListener

---

#### createTreeSelectionListener

protected

TreeSelectionListener

createTreeSelectionListener()

Creates the listener that updates the display based on selection change
methods.

createCellEditorListener

```java
protected
CellEditorListener
createCellEditorListener()
```

Creates a listener to handle events from the current editor.

**Returns:** an instance of the

CellEditorListener

---

#### createCellEditorListener

protected

CellEditorListener

createCellEditorListener()

Creates a listener to handle events from the current editor.

createComponentListener

```java
protected
ComponentListener
createComponentListener()
```

Creates and returns a new ComponentHandler. This is used for
the large model to mark the validCachedPreferredSize as invalid
when the component moves.

**Returns:** an instance of the

ComponentListener

---

#### createComponentListener

protected

ComponentListener

createComponentListener()

Creates and returns a new ComponentHandler. This is used for
the large model to mark the validCachedPreferredSize as invalid
when the component moves.

createTreeExpansionListener

```java
protected
TreeExpansionListener
createTreeExpansionListener()
```

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

**Returns:** an instance of the

TreeExpansionListener

---

#### createTreeExpansionListener

protected

TreeExpansionListener

createTreeExpansionListener()

Creates and returns the object responsible for updating the treestate
when nodes expanded state changes.

createLayoutCache

```java
protected
AbstractLayoutCache
createLayoutCache()
```

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

**Returns:** the object responsible for managing what is expanded

---

#### createLayoutCache

protected

AbstractLayoutCache

createLayoutCache()

Creates the object responsible for managing what is expanded, as
well as the size of nodes.

createCellRendererPane

```java
protected
CellRendererPane
createCellRendererPane()
```

Returns the renderer pane that renderer components are placed in.

**Returns:** an instance of the

CellRendererPane

---

#### createCellRendererPane

protected

CellRendererPane

createCellRendererPane()

Returns the renderer pane that renderer components are placed in.

createDefaultCellEditor

```java
protected
TreeCellEditor
createDefaultCellEditor()
```

Creates a default cell editor.

**Returns:** a default cell editor

---

#### createDefaultCellEditor

protected

TreeCellEditor

createDefaultCellEditor()

Creates a default cell editor.

createDefaultCellRenderer

```java
protected
TreeCellRenderer
createDefaultCellRenderer()
```

Returns the default cell renderer that is used to do the
stamping of each node.

**Returns:** an instance of

TreeCellRenderer

---

#### createDefaultCellRenderer

protected

TreeCellRenderer

createDefaultCellRenderer()

Returns the default cell renderer that is used to do the
stamping of each node.

createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Returns a listener that can update the tree when the model changes.

**Returns:** an instance of the

TreeModelListener

.

---

#### createTreeModelListener

protected

TreeModelListener

createTreeModelListener()

Returns a listener that can update the tree when the model changes.

prepareForUIUninstall

```java
protected void prepareForUIUninstall()
```

Invoked before unstallation of UI.

---

#### prepareForUIUninstall

protected void prepareForUIUninstall()

Invoked before unstallation of UI.

completeUIUninstall

```java
protected void completeUIUninstall()
```

Uninstalls UI.

---

#### completeUIUninstall

protected void completeUIUninstall()

Uninstalls UI.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

uninstallComponents

```java
protected void uninstallComponents()
```

Uninstalls the renderer pane.

---

#### uninstallComponents

protected void uninstallComponents()

Uninstalls the renderer pane.

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

isDropLine

```java
protected boolean isDropLine​(
JTree.DropLocation
loc)
```

Tells if a

DropLocation

should be indicated by a line between
nodes. This is meant for

javax.swing.DropMode.INSERT

and

javax.swing.DropMode.ON_OR_INSERT

drop modes.

**Parameters:** loc

- a

DropLocation
**Returns:** true

if the drop location should be shown as a line
**Since:** 1.7

---

#### isDropLine

protected boolean isDropLine​(

JTree.DropLocation

loc)

Tells if a

DropLocation

should be indicated by a line between
nodes. This is meant for

javax.swing.DropMode.INSERT

and

javax.swing.DropMode.ON_OR_INSERT

drop modes.

paintDropLine

```java
protected void paintDropLine​(
Graphics
g)
```

Paints the drop line.

**Parameters:** g

-

Graphics

object to draw on
**Since:** 1.7

---

#### paintDropLine

protected void paintDropLine​(

Graphics

g)

Paints the drop line.

getDropLineRect

```java
protected
Rectangle
getDropLineRect​(
JTree.DropLocation
loc)
```

Returns a unbounding box for the drop line.

**Parameters:** loc

- a

DropLocation
**Returns:** bounding box for the drop line
**Since:** 1.7

---

#### getDropLineRect

protected

Rectangle

getDropLineRect​(

JTree.DropLocation

loc)

Returns a unbounding box for the drop line.

paintHorizontalPartOfLeg

```java
protected void paintHorizontalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the horizontal part of the leg. The receiver should
NOT modify

clipBounds

, or

insets

.

NOTE:

parentRow

can be -1 if the root is not visible.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

---

#### paintHorizontalPartOfLeg

protected void paintHorizontalPartOfLeg​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the horizontal part of the leg. The receiver should
NOT modify

clipBounds

, or

insets

.

NOTE:

parentRow

can be -1 if the root is not visible.

NOTE:

parentRow

can be -1 if the root is not visible.

paintVerticalPartOfLeg

```java
protected void paintVerticalPartOfLeg​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

TreePath
path)
```

Paints the vertical part of the leg. The receiver should
NOT modify

clipBounds

,

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** path

- a tree path

---

#### paintVerticalPartOfLeg

protected void paintVerticalPartOfLeg​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

TreePath

path)

Paints the vertical part of the leg. The receiver should
NOT modify

clipBounds

,

insets

.

paintExpandControl

```java
protected void paintExpandControl​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the expand (toggle) part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf

---

#### paintExpandControl

protected void paintExpandControl​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the expand (toggle) part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

paintRow

```java
protected void paintRow​(
Graphics
g,

Rectangle
clipBounds,

Insets
insets,

Rectangle
bounds,

TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Paints the renderer part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

**Parameters:** g

- a graphics context
**Parameters:** clipBounds

- a clipped rectangle
**Parameters:** insets

- insets
**Parameters:** bounds

- a bounding rectangle
**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the path is leaf

---

#### paintRow

protected void paintRow​(

Graphics

g,

Rectangle

clipBounds,

Insets

insets,

Rectangle

bounds,

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Paints the renderer part of a row. The receiver should
NOT modify

clipBounds

, or

insets

.

shouldPaintExpandControl

```java
protected boolean shouldPaintExpandControl​(
TreePath
path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)
```

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

**Parameters:** path

- a tree path
**Parameters:** row

- a row
**Parameters:** isExpanded

-

true

if the path is expanded
**Parameters:** hasBeenExpanded

-

true

if the path has been expanded
**Parameters:** isLeaf

-

true

if the row is leaf
**Returns:** true

if the expand (toggle) control should be drawn
for the specified row

---

#### shouldPaintExpandControl

protected boolean shouldPaintExpandControl​(

TreePath

path,
int row,
boolean isExpanded,
boolean hasBeenExpanded,
boolean isLeaf)

Returns

true

if the expand (toggle) control should be drawn for
the specified row.

paintVerticalLine

```java
protected void paintVerticalLine​(
Graphics
g,

JComponent
c,
int x,
int top,
int bottom)
```

Paints a vertical line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** x

- an X coordinate
**Parameters:** top

- an Y1 coordinate
**Parameters:** bottom

- an Y2 coordinate

---

#### paintVerticalLine

protected void paintVerticalLine​(

Graphics

g,

JComponent

c,
int x,
int top,
int bottom)

Paints a vertical line.

paintHorizontalLine

```java
protected void paintHorizontalLine​(
Graphics
g,

JComponent
c,
int y,
int left,
int right)
```

Paints a horizontal line.

**Parameters:** g

- a graphics context
**Parameters:** c

- a component
**Parameters:** y

- an Y coordinate
**Parameters:** left

- an X1 coordinate
**Parameters:** right

- an X2 coordinate

---

#### paintHorizontalLine

protected void paintHorizontalLine​(

Graphics

g,

JComponent

c,
int y,
int left,
int right)

Paints a horizontal line.

getVerticalLegBuffer

```java
protected int getVerticalLegBuffer()
```

The vertical element of legs between nodes starts at the bottom of the
parent node by default. This method makes the leg start below that.

**Returns:** the vertical leg buffer

---

#### getVerticalLegBuffer

protected int getVerticalLegBuffer()

The vertical element of legs between nodes starts at the bottom of the
parent node by default. This method makes the leg start below that.

getHorizontalLegBuffer

```java
protected int getHorizontalLegBuffer()
```

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default. This
method makes the leg end before that.

**Returns:** the horizontal leg buffer

---

#### getHorizontalLegBuffer

protected int getHorizontalLegBuffer()

The horizontal element of legs between nodes starts at the
right of the left-hand side of the child node by default. This
method makes the leg end before that.

drawCentered

```java
protected void drawCentered​(
Component
c,

Graphics
graphics,

Icon
icon,
int x,
int y)
```

Draws the

icon

centered at (x,y).

**Parameters:** c

- a component
**Parameters:** graphics

- a graphics context
**Parameters:** icon

- an icon
**Parameters:** x

- an X coordinate
**Parameters:** y

- an Y coordinate

---

#### drawCentered

protected void drawCentered​(

Component

c,

Graphics

graphics,

Icon

icon,
int x,
int y)

Draws the

icon

centered at (x,y).

drawDashedHorizontalLine

```java
protected void drawDashedHorizontalLine​(
Graphics
g,
int y,
int x1,
int x2)
```

Draws a horizontal dashed line. It is assumed

x1

<=

x2

.
If

x1

is greater than

x2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** y

- an Y coordinate
**Parameters:** x1

- an X1 coordinate
**Parameters:** x2

- an X2 coordinate

---

#### drawDashedHorizontalLine

protected void drawDashedHorizontalLine​(

Graphics

g,
int y,
int x1,
int x2)

Draws a horizontal dashed line. It is assumed

x1

<=

x2

.
If

x1

is greater than

x2

, the method draws nothing.

drawDashedVerticalLine

```java
protected void drawDashedVerticalLine​(
Graphics
g,
int x,
int y1,
int y2)
```

Draws a vertical dashed line. It is assumed

y1

<=

y2

.
If

y1

is greater than

y2

, the method draws nothing.

**Parameters:** g

- an instance of

Graphics
**Parameters:** x

- an X coordinate
**Parameters:** y1

- an Y1 coordinate
**Parameters:** y2

- an Y2 coordinate

---

#### drawDashedVerticalLine

protected void drawDashedVerticalLine​(

Graphics

g,
int x,
int y1,
int y2)

Draws a vertical dashed line. It is assumed

y1

<=

y2

.
If

y1

is greater than

y2

, the method draws nothing.

getRowX

```java
protected int getRowX​(int row,
int depth)
```

Returns the location, along the x-axis, to render a particular row
at. The return value does not include any Insets specified on the JTree.
This does not check for the validity of the row or depth, it is assumed
to be correct and will not throw an Exception if the row or depth
doesn't match that of the tree.

**Parameters:** row

- Row to return x location for
**Parameters:** depth

- Depth of the row
**Returns:** amount to indent the given row.
**Since:** 1.5

---

#### getRowX

protected int getRowX​(int row,
int depth)

Returns the location, along the x-axis, to render a particular row
at. The return value does not include any Insets specified on the JTree.
This does not check for the validity of the row or depth, it is assumed
to be correct and will not throw an Exception if the row or depth
doesn't match that of the tree.

updateLayoutCacheExpandedNodes

```java
protected void updateLayoutCacheExpandedNodes()
```

Makes all the nodes that are expanded in JTree expanded in LayoutCache.
This invokes updateExpandedDescendants with the root path.

---

#### updateLayoutCacheExpandedNodes

protected void updateLayoutCacheExpandedNodes()

Makes all the nodes that are expanded in JTree expanded in LayoutCache.
This invokes updateExpandedDescendants with the root path.

updateExpandedDescendants

```java
protected void updateExpandedDescendants​(
TreePath
path)
```

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

**Parameters:** path

- a tree path

---

#### updateExpandedDescendants

protected void updateExpandedDescendants​(

TreePath

path)

Updates the expanded state of all the descendants of

path

by getting the expanded descendants from the tree and forwarding
to the tree state.

getLastChildPath

```java
protected
TreePath
getLastChildPath​(
TreePath
parent)
```

Returns a path to the last child of

parent

.

**Parameters:** parent

- a tree path
**Returns:** a path to the last child of

parent

---

#### getLastChildPath

protected

TreePath

getLastChildPath​(

TreePath

parent)

Returns a path to the last child of

parent

.

updateDepthOffset

```java
protected void updateDepthOffset()
```

Updates how much each depth should be offset by.

---

#### updateDepthOffset

protected void updateDepthOffset()

Updates how much each depth should be offset by.

updateCellEditor

```java
protected void updateCellEditor()
```

Updates the cellEditor based on the editability of the JTree that
we're contained in. If the tree is editable but doesn't have a
cellEditor, a basic one will be used.

---

#### updateCellEditor

protected void updateCellEditor()

Updates the cellEditor based on the editability of the JTree that
we're contained in. If the tree is editable but doesn't have a
cellEditor, a basic one will be used.

updateRenderer

```java
protected void updateRenderer()
```

Messaged from the tree we're in when the renderer has changed.

---

#### updateRenderer

protected void updateRenderer()

Messaged from the tree we're in when the renderer has changed.

configureLayoutCache

```java
protected void configureLayoutCache()
```

Resets the TreeState instance based on the tree we're providing the
look and feel for.

---

#### configureLayoutCache

protected void configureLayoutCache()

Resets the TreeState instance based on the tree we're providing the
look and feel for.

updateSize

```java
protected void updateSize()
```

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

---

#### updateSize

protected void updateSize()

Marks the cached size as being invalid, and messages the
tree with

treeDidChange

.

updateCachedPreferredSize

```java
protected void updateCachedPreferredSize()
```

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

---

#### updateCachedPreferredSize

protected void updateCachedPreferredSize()

Updates the

preferredSize

instance variable,
which is returned from

getPreferredSize()

.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

For left to right orientations, the size is determined from the
current AbstractLayoutCache. For RTL orientations, the preferred size
becomes the width minus the minimum x position.

pathWasExpanded

```java
protected void pathWasExpanded​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has been expanded.

**Parameters:** path

- a tree path

---

#### pathWasExpanded

protected void pathWasExpanded​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has been expanded.

pathWasCollapsed

```java
protected void pathWasCollapsed​(
TreePath
path)
```

Messaged from the

VisibleTreeNode

after it has collapsed.

**Parameters:** path

- a tree path

---

#### pathWasCollapsed

protected void pathWasCollapsed​(

TreePath

path)

Messaged from the

VisibleTreeNode

after it has collapsed.

ensureRowsAreVisible

```java
protected void ensureRowsAreVisible​(int beginRow,
int endRow)
```

Ensures that the rows identified by

beginRow

through

endRow

are visible.

**Parameters:** beginRow

- the begin row
**Parameters:** endRow

- the end row

---

#### ensureRowsAreVisible

protected void ensureRowsAreVisible​(int beginRow,
int endRow)

Ensures that the rows identified by

beginRow

through

endRow

are visible.

setPreferredMinSize

```java
public void setPreferredMinSize​(
Dimension
newSize)
```

Sets the preferred minimum size.

**Parameters:** newSize

- the new preferred size

---

#### setPreferredMinSize

public void setPreferredMinSize​(

Dimension

newSize)

Sets the preferred minimum size.

getPreferredMinSize

```java
public
Dimension
getPreferredMinSize()
```

Returns the minimum preferred size.

**Returns:** the minimum preferred size

---

#### getPreferredMinSize

public

Dimension

getPreferredMinSize()

Returns the minimum preferred size.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- a component
**Returns:** the preferred size to represent the tree in the component
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

Returns the preferred size to properly display the tree,
this is a cover method for

getPreferredSize(c, true)

.

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c,
boolean checkConsistency)
```

Returns the preferred size to represent the tree in

c

. If

checkConsistency

is

true

checkConsistency

is messaged first.

**Parameters:** c

- a component
**Parameters:** checkConsistency

- if

true

consistency is checked
**Returns:** the preferred size to represent the tree in the component

---

#### getPreferredSize

public

Dimension

getPreferredSize​(

JComponent

c,
boolean checkConsistency)

Returns the preferred size to represent the tree in

c

. If

checkConsistency

is

true

checkConsistency

is messaged first.

getMinimumSize

```java
public
Dimension
getMinimumSize​(
JComponent
c)
```

Returns the minimum size for this component. Which will be
the min preferred size or 0, 0.

**Overrides:** getMinimumSize

in class

ComponentUI
**Parameters:** c

- the component whose minimum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
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

Returns the minimum size for this component. Which will be
the min preferred size or 0, 0.

getMaximumSize

```java
public
Dimension
getMaximumSize​(
JComponent
c)
```

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

**Overrides:** getMaximumSize

in class

ComponentUI
**Parameters:** c

- the component whose maximum size is being queried;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**Returns:** a

Dimension

object or

null
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

Returns the maximum size for this component, which will be the
preferred size if the instance is currently in a JTree, or 0, 0.

completeEditing

```java
protected void completeEditing()
```

Messages to stop the editing session. If the UI the receiver
is providing the look and feel for returns true from

getInvokesStopCellEditing

, stopCellEditing will
invoked on the current editor. Then completeEditing will
be messaged with false, true, false to cancel any lingering
editing.

---

#### completeEditing

protected void completeEditing()

Messages to stop the editing session. If the UI the receiver
is providing the look and feel for returns true from

getInvokesStopCellEditing

, stopCellEditing will
invoked on the current editor. Then completeEditing will
be messaged with false, true, false to cancel any lingering
editing.

completeEditing

```java
protected void completeEditing​(boolean messageStop,
boolean messageCancel,
boolean messageTree)
```

Stops the editing session. If

messageStop

is

true

the editor
is messaged with

stopEditing

, if

messageCancel

is

true

the editor is messaged with

cancelEditing

.
If

messageTree

is

true

the

treeModel

is messaged
with

valueForPathChanged

.

**Parameters:** messageStop

- message to stop editing
**Parameters:** messageCancel

- message to cancel editing
**Parameters:** messageTree

- message to tree

---

#### completeEditing

protected void completeEditing​(boolean messageStop,
boolean messageCancel,
boolean messageTree)

Stops the editing session. If

messageStop

is

true

the editor
is messaged with

stopEditing

, if

messageCancel

is

true

the editor is messaged with

cancelEditing

.
If

messageTree

is

true

the

treeModel

is messaged
with

valueForPathChanged

.

startEditing

```java
protected boolean startEditing​(
TreePath
path,

MouseEvent
event)
```

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

This assumes that path is valid and visible.

**Parameters:** path

- a tree path
**Parameters:** event

- a mouse event
**Returns:** true

if the editing is successful

---

#### startEditing

protected boolean startEditing​(

TreePath

path,

MouseEvent

event)

Will start editing for node if there is a

cellEditor

and

shouldSelectCell

returns

true

.

This assumes that path is valid and visible.

This assumes that path is valid and visible.

checkForClickInExpandControl

```java
protected void checkForClickInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

---

#### checkForClickInExpandControl

protected void checkForClickInExpandControl​(

TreePath

path,
int mouseX,
int mouseY)

If the

mouseX

and

mouseY

are in the
expand/collapse region of the

row

, this will toggle
the row.

isLocationInExpandControl

```java
protected boolean isLocationInExpandControl​(
TreePath
path,
int mouseX,
int mouseY)
```

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate
**Returns:** true

if the mouse cursor fall in the area of row that
is used to expand/collapse the node and the node is not a leaf.

---

#### isLocationInExpandControl

protected boolean isLocationInExpandControl​(

TreePath

path,
int mouseX,
int mouseY)

Returns

true

if

mouseX

and

mouseY

fall
in the area of row that is used to expand/collapse the node and
the node at

row

does not represent a leaf.

handleExpandControlClick

```java
protected void handleExpandControlClick​(
TreePath
path,
int mouseX,
int mouseY)
```

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

**Parameters:** path

- a tree path
**Parameters:** mouseX

- an X coordinate
**Parameters:** mouseY

- an Y coordinate

---

#### handleExpandControlClick

protected void handleExpandControlClick​(

TreePath

path,
int mouseX,
int mouseY)

Messaged when the user clicks the particular row, this invokes

toggleExpandState

.

toggleExpandState

```java
protected void toggleExpandState​(
TreePath
path)
```

Expands path if it is not expanded, or collapses row if it is expanded.
If expanding a path and

JTree

scrolls on expand,

ensureRowsAreVisible

is invoked to scroll as many of the children
to visible as possible (tries to scroll to last visible descendant of path).

**Parameters:** path

- a tree path

---

#### toggleExpandState

protected void toggleExpandState​(

TreePath

path)

Expands path if it is not expanded, or collapses row if it is expanded.
If expanding a path and

JTree

scrolls on expand,

ensureRowsAreVisible

is invoked to scroll as many of the children
to visible as possible (tries to scroll to last visible descendant of path).

isToggleSelectionEvent

```java
protected boolean isToggleSelectionEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should toggle the selection

---

#### isToggleSelectionEvent

protected boolean isToggleSelectionEvent​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should toggle
the selection of only the row under mouse.

isMultiSelectEvent

```java
protected boolean isMultiSelectEvent​(
MouseEvent
event)
```

Returning

true

signifies a mouse event on the node should select
from the anchor point.

**Parameters:** event

- a mouse event
**Returns:** true

if a mouse event on the node should select
from the anchor point

---

#### isMultiSelectEvent

protected boolean isMultiSelectEvent​(

MouseEvent

event)

Returning

true

signifies a mouse event on the node should select
from the anchor point.

isToggleEvent

```java
protected boolean isToggleEvent​(
MouseEvent
event)
```

Returning

true

indicates the row under the mouse should be toggled
based on the event. This is invoked after

checkForClickInExpandControl

,
implying the location is not in the expand (toggle) control.

**Parameters:** event

- a mouse event
**Returns:** true

if the row under the mouse should be toggled

---

#### isToggleEvent

protected boolean isToggleEvent​(

MouseEvent

event)

Returning

true

indicates the row under the mouse should be toggled
based on the event. This is invoked after

checkForClickInExpandControl

,
implying the location is not in the expand (toggle) control.

selectPathForEvent

```java
protected void selectPathForEvent​(
TreePath
path,

MouseEvent
event)
```

Messaged to update the selection based on a

MouseEvent

over a
particular row. If the event is a toggle selection event, the
row is either selected, or deselected. If the event identifies
a multi selection event, the selection is updated from the
anchor point. Otherwise the row is selected, and if the event
specified a toggle event the row is expanded/collapsed.

**Parameters:** path

- the selected path
**Parameters:** event

- the mouse event

---

#### selectPathForEvent

protected void selectPathForEvent​(

TreePath

path,

MouseEvent

event)

Messaged to update the selection based on a

MouseEvent

over a
particular row. If the event is a toggle selection event, the
row is either selected, or deselected. If the event identifies
a multi selection event, the selection is updated from the
anchor point. Otherwise the row is selected, and if the event
specified a toggle event the row is expanded/collapsed.

isLeaf

```java
protected boolean isLeaf​(int row)
```

Returns

true

if the node at

row

is a leaf.

**Parameters:** row

- a row
**Returns:** true

if the node at

row

is a leaf

---

#### isLeaf

protected boolean isLeaf​(int row)

Returns

true

if the node at

row

is a leaf.

updateLeadSelectionRow

```java
protected void updateLeadSelectionRow()
```

Updates the lead row of the selection.

**Since:** 1.7

---

#### updateLeadSelectionRow

protected void updateLeadSelectionRow()

Updates the lead row of the selection.

getLeadSelectionRow

```java
protected int getLeadSelectionRow()
```

Returns the lead row of the selection.

**Returns:** selection lead row
**Since:** 1.7

---

#### getLeadSelectionRow

protected int getLeadSelectionRow()

Returns the lead row of the selection.

---

