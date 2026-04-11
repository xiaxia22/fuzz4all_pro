# Class JTree

**Source:** `java.desktop\javax\swing\JTree.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that displays a set of hierarchical data as an outline.")
public class
JTree

extends
JComponent

implements
Scrollable
,
Accessible
```

A control that displays a set of hierarchical data as an outline.
You can find task-oriented documentation and examples of using trees in

How to Use Trees

,
a section in

The Java Tutorial.

A specific node in a tree can be identified either by a

TreePath

(an object
that encapsulates a node and all of its ancestors), or by its
display row, where each row in the display area displays one node.
An

expanded

node is a non-leaf node (as identified by

TreeModel.isLeaf(node)

returning false) that will displays
its children when all its ancestors are

expanded

.
A

collapsed

node is one which hides them. A

hidden

node is one which is
under a collapsed ancestor. All of a

viewable

nodes parents
are expanded, but may or may not be displayed. A

displayed

node
is both viewable and in the display area, where it can be seen.

The following

JTree

methods use "visible" to mean "displayed":

- isRootVisible()

setRootVisible()

scrollPathToVisible()

scrollRowToVisible()

getVisibleRowCount()

setVisibleRowCount()

The next group of

JTree

methods use "visible" to mean
"viewable" (under an expanded parent):

- isVisible()

makeVisible()

If you are interested in knowing when the selection changes implement
the

TreeSelectionListener

interface and add the instance
using the method

addTreeSelectionListener

.

valueChanged

will be invoked when the
selection changes, that is if the user clicks twice on the same
node

valueChanged

will only be invoked once.

If you are interested in detecting either double-click events or when
a user clicks on a node, regardless of whether or not it was selected,
we recommend you do the following:

```java
final JTree tree = ...;

MouseListener ml = new MouseAdapter() {
public void
mousePressed
(MouseEvent e) {
int selRow = tree.getRowForLocation(e.getX(), e.getY());
TreePath selPath = tree.getPathForLocation(e.getX(), e.getY());
if(selRow != -1) {
if(e.getClickCount() == 1) {
mySingleClick(selRow, selPath);
}
else if(e.getClickCount() == 2) {
myDoubleClick(selRow, selPath);
}
}
}
};
tree.addMouseListener(ml);
```

NOTE: This example obtains both the path and row, but you only need to
get the one you're interested in.

To use

JTree

to display compound nodes
(for example, nodes containing both
a graphic icon and text), subclass

TreeCellRenderer

and use

setCellRenderer(javax.swing.tree.TreeCellRenderer)

to tell the tree to use it. To edit such nodes,
subclass

TreeCellEditor

and use

setCellEditor(javax.swing.tree.TreeCellEditor)

.

Like all

JComponent

classes, you can use

InputMap

and

ActionMap

to associate an

Action

object with a

KeyStroke

and execute the action under specified conditions.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

---

### Field Details

#### protected transient
TreeModel
treeModel

The model that defines the tree displayed by this object.

---

#### protected transient
TreeSelectionModel
selectionModel

Models the set of selected nodes in this tree.

---

#### protected boolean rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

---

#### protected transient
TreeCellRenderer
cellRenderer

The cell used to draw nodes. If

null

, the UI uses a default

cellRenderer

.

---

#### protected int rowHeight

Height to use for each display row. If this is <= 0 the renderer
determines the height for each row.

---

#### protected boolean showsRootHandles

True if handles are displayed at the topmost level of the tree.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

**See Also:**
- rootVisible

---

#### protected transient
JTree.TreeSelectionRedirector
selectionRedirector

Creates a new event and passed it off the

selectionListeners

.

---

#### protected transient
TreeCellEditor
cellEditor

Editor for the entries. Default is

null

(tree is not editable).

---

#### protected boolean editable

Is the tree editable? Default is false.

---

#### protected boolean largeModel

Is this tree a large model? This is a code-optimization setting.
A large model can be used when the cell height is the same for all
nodes. The UI will then cache very little information and instead
continually message the model. Without a large model the UI caches
most of the information, resulting in fewer method calls to the model.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

---

#### protected int visibleRowCount

Number of rows to make visible at one time. This value is used for
the

Scrollable

interface. It determines the preferred
size of the display area.

---

#### protected boolean invokesStopCellEditing

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved. If false,

cancelCellEditing

is invoked, and changes
are discarded. Default is false.

---

#### protected boolean scrollsOnExpand

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

---

#### protected int toggleClickCount

Number of mouse clicks before a node is expanded.

---

#### protected transient
TreeModelListener
treeModelListener

Updates the

expandedState

.

---

#### public static final
String
CELL_RENDERER_PROPERTY

Bound property name for

cellRenderer

.

**See Also:**
- Constant Field Values

---

#### public static final
String
TREE_MODEL_PROPERTY

Bound property name for

treeModel

.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROOT_VISIBLE_PROPERTY

Bound property name for

rootVisible

.

**See Also:**
- Constant Field Values

---

#### public static final
String
SHOWS_ROOT_HANDLES_PROPERTY

Bound property name for

showsRootHandles

.

**See Also:**
- Constant Field Values

---

#### public static final
String
ROW_HEIGHT_PROPERTY

Bound property name for

rowHeight

.

**See Also:**
- Constant Field Values

---

#### public static final
String
CELL_EDITOR_PROPERTY

Bound property name for

cellEditor

.

**See Also:**
- Constant Field Values

---

#### public static final
String
EDITABLE_PROPERTY

Bound property name for

editable

.

**See Also:**
- Constant Field Values

---

#### public static final
String
LARGE_MODEL_PROPERTY

Bound property name for

largeModel

.

**See Also:**
- Constant Field Values

---

#### public static final
String
SELECTION_MODEL_PROPERTY

Bound property name for selectionModel.

**See Also:**
- Constant Field Values

---

#### public static final
String
VISIBLE_ROW_COUNT_PROPERTY

Bound property name for

visibleRowCount

.

**See Also:**
- Constant Field Values

---

#### public static final
String
INVOKES_STOP_CELL_EDITING_PROPERTY

Bound property name for

messagesStopCellEditing

.

**See Also:**
- Constant Field Values

---

#### public static final
String
SCROLLS_ON_EXPAND_PROPERTY

Bound property name for

scrollsOnExpand

.

**See Also:**
- Constant Field Values

---

#### public static final
String
TOGGLE_CLICK_COUNT_PROPERTY

Bound property name for

toggleClickCount

.

**See Also:**
- Constant Field Values

---

#### public static final
String
LEAD_SELECTION_PATH_PROPERTY

Bound property name for

leadSelectionPath

.

**See Also:**
- Constant Field Values

**Since:**
- 1.3

---

#### public static final
String
ANCHOR_SELECTION_PATH_PROPERTY

Bound property name for anchor selection path.

**See Also:**
- Constant Field Values

**Since:**
- 1.3

---

#### public static final
String
EXPANDS_SELECTED_PATHS_PROPERTY

Bound property name for expands selected paths property

**See Also:**
- Constant Field Values

**Since:**
- 1.3

---

### Constructor Details

#### public JTree()

Returns a

JTree

with a sample model.
The default model used by the tree defines a leaf node as any node
without children.

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### public JTree​(
Object
[] value)

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.
By default, the tree defines a leaf node as any node without
children.

**Parameters:**
- value

- an array of

Object

s

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### public JTree​(
Vector
<?> value)

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed. By default, the
tree defines a leaf node as any node without children.

**Parameters:**
- value

- a

Vector

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### public JTree​(
Hashtable
<?,​?> value)

Returns a

JTree

created from a

Hashtable

which does not display with root.
Each value-half of the key/value pairs in the

HashTable

becomes a child of the new root node. By default, the tree defines
a leaf node as any node without children.

**Parameters:**
- value

- a

Hashtable

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### public JTree​(
TreeNode
root)

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.
By default, the tree defines a leaf node as any node without children.

**Parameters:**
- root

- a

TreeNode

object

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### public JTree​(
TreeNode
root,
boolean asksAllowsChildren)

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

**Parameters:**
- root

- a

TreeNode

object
- asksAllowsChildren

- if false, any node without children is a
leaf node; if true, only nodes that do not allow
children are leaf nodes

**See Also:**
- DefaultTreeModel.asksAllowsChildren

---

#### @ConstructorProperties
("model")
public JTree​(
TreeModel
newModel)

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

**Parameters:**
- newModel

- the

TreeModel

to use as the data model

---

### Method Details

#### protected static
TreeModel
getDefaultTreeModel()

Creates and returns a sample

TreeModel

.
Used primarily for beanbuilders to show something interesting.

**Returns:**
- the default

TreeModel

---

#### protected static
TreeModel
createTreeModel​(
Object
value)

Returns a

TreeModel

wrapping the specified object.
If the object is:

- an array of

Object

s,

a

Hashtable

, or

a

Vector

then a new root node is created with each of the incoming
objects as children. Otherwise, a new root is created with
a value of

"root"

.

**Parameters:**
- value

- the

Object

used as the foundation for
the

TreeModel

**Returns:**
- a

TreeModel

wrapping the specified object

---

#### public
TreeUI
getUI()

Returns the L&F object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

TreeUI

object that renders this component

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
TreeUI
ui)

Sets the L&F object that renders this component.

This is a bound property.

**Parameters:**
- ui

- the

TreeUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:**
- updateUI

in class

JComponent

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false)
public
String
getUIClassID()

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "TreeUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public
TreeCellRenderer
getCellRenderer()

Returns the current

TreeCellRenderer

that is rendering each cell.

**Returns:**
- the

TreeCellRenderer

that is rendering each cell

---

#### @BeanProperty
(
description
="The TreeCellRenderer that will be used to draw each cell.")
public void setCellRenderer​(
TreeCellRenderer
x)

Sets the

TreeCellRenderer

that will be used to
draw each cell.

This is a bound property.

**Parameters:**
- x

- the

TreeCellRenderer

that is to render each cell

---

#### @BeanProperty
(
description
="Whether the tree is editable.")
public void setEditable​(boolean flag)

Determines whether the tree is editable. Fires a property
change event if the new setting is different from the existing
setting.

This is a bound property.

**Parameters:**
- flag

- a boolean value, true if the tree is editable

---

#### public boolean isEditable()

Returns true if the tree is editable.

**Returns:**
- true if the tree is editable

---

#### @BeanProperty
(
description
="The cell editor. A null value implies the tree cannot be edited.")
public void setCellEditor​(
TreeCellEditor
cellEditor)

Sets the cell editor. A

null

value implies that the
tree cannot be edited. If this represents a change in the

cellEditor

, the

propertyChange

method is invoked on all listeners.

This is a bound property.

**Parameters:**
- cellEditor

- the

TreeCellEditor

to use

---

#### public
TreeCellEditor
getCellEditor()

Returns the editor used to edit entries in the tree.

**Returns:**
- the

TreeCellEditor

in use,
or

null

if the tree cannot be edited

---

#### public
TreeModel
getModel()

Returns the

TreeModel

that is providing the data.

**Returns:**
- the

TreeModel

that is providing the data

---

#### @BeanProperty
(
description
="The TreeModel that will provide the data.")
public void setModel​(
TreeModel
newModel)

Sets the

TreeModel

that will provide the data.

This is a bound property.

**Parameters:**
- newModel

- the

TreeModel

that is to provide the data

---

#### public boolean isRootVisible()

Returns true if the root node of the tree is displayed.

**Returns:**
- true if the root node of the tree is displayed

**See Also:**
- rootVisible

---

#### @BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

This is a bound property.

**Parameters:**
- rootVisible

- true if the root node of the tree is to be displayed

**See Also:**
- rootVisible

---

#### @BeanProperty
(
description
="Whether the node handles are to be displayed.")
public void setShowsRootHandles​(boolean newValue)

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.
The default value of this property depends on the constructor
used to create the

JTree

.
Some look and feels might not support handles;
they will ignore this property.

This is a bound property.

**Parameters:**
- newValue

-

true

if root handles should be displayed;
otherwise,

false

**See Also:**
- showsRootHandles

,

getShowsRootHandles()

---

#### public boolean getShowsRootHandles()

Returns the value of the

showsRootHandles

property.

**Returns:**
- the value of the

showsRootHandles

property

**See Also:**
- showsRootHandles

---

#### @BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)

Sets the height of each cell, in pixels. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

This is a bound property.

**Parameters:**
- rowHeight

- the height of each cell, in pixels

---

#### public int getRowHeight()

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:**
- the height of each row

---

#### @BeanProperty
(
bound
=false)
public boolean isFixedRowHeight()

Returns true if the height of each display row is a fixed size.

**Returns:**
- true if the height of each row is a fixed size

---

#### @BeanProperty
(
description
="Whether the UI should use a large model.")
public void setLargeModel​(boolean newValue)

Specifies whether the UI should use a large model.
(Not all UIs will implement this.) Fires a property change
for the LARGE_MODEL_PROPERTY.

This is a bound property.

**Parameters:**
- newValue

- true to suggest a large model to the UI

**See Also:**
- largeModel

---

#### public boolean isLargeModel()

Returns true if the tree is configured for a large model.

**Returns:**
- true if a large model is suggested

**See Also:**
- largeModel

---

#### @BeanProperty
(
description
="Determines what happens when editing is interrupted, selecting another node in the tree, a change in the tree\'s data, or some other means.")
public void setInvokesStopCellEditing​(boolean newValue)

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means. Setting this property to

true

causes the
changes to be automatically saved when editing is interrupted.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

**Parameters:**
- newValue

- true means that

stopCellEditing

is invoked
when editing is interrupted, and data is saved; false means that

cancelCellEditing

is invoked, and changes are lost

---

#### public boolean getInvokesStopCellEditing()

Returns the indicator that tells what happens when editing is
interrupted.

**Returns:**
- the indicator that tells what happens when editing is
interrupted

**See Also:**
- setInvokesStopCellEditing(boolean)

---

#### @BeanProperty
(
description
="Indicates if a node descendant should be scrolled when expanded.")
public void setScrollsOnExpand​(boolean newValue)

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.
If this property is

true

(the default),
when a node expands
the tree can use scrolling to make
the maximum possible number of the node's descendants visible.
In some look and feels, trees might not need to scroll when expanded;
those look and feels will ignore this property.

This is a bound property.

**Parameters:**
- newValue

-

false

to disable scrolling on expansion;

true

to enable it

**See Also:**
- getScrollsOnExpand()

---

#### public boolean getScrollsOnExpand()

Returns the value of the

scrollsOnExpand

property.

**Returns:**
- the value of the

scrollsOnExpand

property

---

#### @BeanProperty
(
description
="Number of clicks before a node will expand/collapse.")
public void setToggleClickCount​(int clickCount)

Sets the number of mouse clicks before a node will expand or close.
The default is two.

This is a bound property.

**Parameters:**
- clickCount

- the number of mouse clicks to get a node expanded or closed

**Since:**
- 1.3

---

#### public int getToggleClickCount()

Returns the number of mouse clicks needed to expand or close a node.

**Returns:**
- number of mouse clicks before node is expanded

**Since:**
- 1.3

---

#### @BeanProperty
(
description
="Indicates whether changes to the selection should make the parent of the path visible.")
public void setExpandsSelectedPaths​(boolean newValue)

Configures the

expandsSelectedPaths

property. If
true, any time the selection is changed, either via the

TreeSelectionModel

, or the cover methods provided by

JTree

, the

TreePath

s parents will be
expanded to make them visible (visible meaning the parent path is
expanded, not necessarily in the visible rectangle of the

JTree

). If false, when the selection
changes the nodes parent is not made visible (all its parents expanded).
This is useful if you wish to have your selection model maintain paths
that are not always visible (all parents expanded).

This is a bound property.

**Parameters:**
- newValue

- the new value for

expandsSelectedPaths

**Since:**
- 1.3

---

#### public boolean getExpandsSelectedPaths()

Returns the

expandsSelectedPaths

property.

**Returns:**
- true if selection changes result in the parent path being
expanded

**See Also:**
- setExpandsSelectedPaths(boolean)

**Since:**
- 1.3

---

#### @BeanProperty
(
bound
=false,

description
="determines whether automatic drag handling is enabled")
public void setDragEnabled​(boolean b)

Turns on or off automatic drag handling. In order to enable automatic
drag handling, this property should be set to

true

, and the
tree's

TransferHandler

needs to be

non-null

.
The default value of the

dragEnabled

property is

false

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

**Parameters:**
- b

- whether or not to enable automatic drag handling

**Throws:**
- HeadlessException

- if

b

is

true

and

GraphicsEnvironment.isHeadless()

returns

true

**See Also:**
- GraphicsEnvironment.isHeadless()

,

getDragEnabled()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

**Since:**
- 1.4

---

#### public boolean getDragEnabled()

Returns whether or not automatic drag handling is enabled.

**Returns:**
- the value of the

dragEnabled

property

**See Also:**
- setDragEnabled(boolean)

**Since:**
- 1.4

---

#### public final void setDropMode​(
DropMode
dropMode)

Sets the drop mode for this component. For backward compatibility,
the default for this property is

DropMode.USE_SELECTION

.
Usage of one of the other modes is recommended, however, for an
improved user experience.

DropMode.ON

, for instance,
offers similar behavior of showing items as selected, but does so without
affecting the actual selection in the tree.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

**Parameters:**
- dropMode

- the drop mode to use

**Throws:**
- IllegalArgumentException

- if the drop mode is unsupported
or

null

**See Also:**
- getDropMode()

,

getDropLocation()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

**Since:**
- 1.6

---

#### public final
DropMode
getDropMode()

Returns the drop mode for this component.

**Returns:**
- the drop mode for this component

**See Also:**
- setDropMode(javax.swing.DropMode)

**Since:**
- 1.6

---

#### @BeanProperty
(
bound
=false)
public final
JTree.DropLocation
getDropLocation()

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

**Returns:**
- the drop location

**See Also:**
- setDropMode(javax.swing.DropMode)

,

TransferHandler.canImport(TransferHandler.TransferSupport)

**Since:**
- 1.6

---

#### public boolean isPathEditable​(
TreePath
path)

Returns

isEditable

. This is invoked from the UI before
editing begins to insure that the given path can be edited. This
is provided as an entry point for subclassers to add filtered
editing without having to resort to creating a new editor.

**Parameters:**
- path

- a

TreePath

identifying a node

**Returns:**
- true if every parent node and the node itself is editable

**See Also:**
- isEditable()

---

#### public
String
getToolTipText​(
MouseEvent
event)

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

**Overrides:**
- getToolTipText

in class

JComponent

**Parameters:**
- event

- the

MouseEvent

that initiated the

ToolTip

display

**Returns:**
- a string containing the tooltip or

null

if

event

is null

---

#### public
String
convertValueToText​(
Object
value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Called by the renderers to convert the specified value to
text. This implementation returns

value.toString

, ignoring
all other arguments. To control the conversion, subclass this
method and use any of the arguments you need.

**Parameters:**
- value

- the

Object

to convert to text
- selected

- true if the node is selected
- expanded

- true if the node is expanded
- leaf

- true if the node is a leaf node
- row

- an integer specifying the node's display row, where 0 is
the first row in the display
- hasFocus

- true if the node has the focus

**Returns:**
- the

String

representation of the node's value

---

#### @BeanProperty
(
bound
=false)
public int getRowCount()

Returns the number of viewable nodes. A node is viewable if all of its
parents are expanded. The root is only included in this count if

isRootVisible()

is

true

. This returns

0

if
the UI has not been set.

**Returns:**
- the number of viewable nodes

---

#### public void setSelectionPath​(
TreePath
path)

Selects the node identified by the specified path. If any
component of the path is hidden (under a collapsed node), and

getExpandsSelectedPaths

is true it is
exposed (made viewable).

**Parameters:**
- path

- the

TreePath

specifying the node to select

---

#### public void setSelectionPaths​(
TreePath
[] paths)

Selects the nodes identified by the specified array of paths.
If any component in any of the paths is hidden (under a collapsed
node), and

getExpandsSelectedPaths

is true
it is exposed (made viewable).

**Parameters:**
- paths

- an array of

TreePath

objects that specifies
the nodes to select

---

#### @BeanProperty
(
description
="Lead selection path")
public void setLeadSelectionPath​(
TreePath
newPath)

Sets the path identifies as the lead. The lead may not be selected.
The lead is not maintained by

JTree

,
rather the UI will update it.

This is a bound property.

**Parameters:**
- newPath

- the new lead path

**Since:**
- 1.3

---

#### @BeanProperty
(
description
="Anchor selection path")
public void setAnchorSelectionPath​(
TreePath
newPath)

Sets the path identified as the anchor.
The anchor is not maintained by

JTree

, rather the UI will
update it.

This is a bound property.

**Parameters:**
- newPath

- the new anchor path

**Since:**
- 1.3

---

#### public void setSelectionRow​(int row)

Selects the node at the specified row in the display.

**Parameters:**
- row

- the row to select, where 0 is the first row in
the display

---

#### public void setSelectionRows​(int[] rows)

Selects the nodes corresponding to each of the specified rows
in the display. If a particular element of

rows

is
< 0 or >=

getRowCount

, it will be ignored.
If none of the elements
in

rows

are valid rows, the selection will
be cleared. That is it will be as if

clearSelection

was invoked.

**Parameters:**
- rows

- an array of ints specifying the rows to select,
where 0 indicates the first row in the display

---

#### public void addSelectionPath​(
TreePath
path)

Adds the node identified by the specified

TreePath

to the current selection. If any component of the path isn't
viewable, and

getExpandsSelectedPaths

is true it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:**
- path

- the

TreePath

to add

---

#### public void addSelectionPaths​(
TreePath
[] paths)

Adds each path in the array of paths to the current selection. If
any component of any of the paths isn't viewable and

getExpandsSelectedPaths

is true, it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:**
- paths

- an array of

TreePath

objects that specifies
the nodes to add

---

#### public void addSelectionRow​(int row)

Adds the path at the specified row to the current selection.

**Parameters:**
- row

- an integer specifying the row of the node to add,
where 0 is the first row in the display

---

#### public void addSelectionRows​(int[] rows)

Adds the paths at each of the specified rows to the current selection.

**Parameters:**
- rows

- an array of ints specifying the rows to add,
where 0 indicates the first row in the display

---

#### @BeanProperty
(
bound
=false)
public
Object
getLastSelectedPathComponent()

Returns the last path component of the selected path. This is
a convenience method for

getSelectionModel().getSelectionPath().getLastPathComponent()

.
This is typically only useful if the selection has one path.

**Returns:**
- the last path component of the selected path, or

null

if nothing is selected

**See Also:**
- TreePath.getLastPathComponent()

---

#### public
TreePath
getLeadSelectionPath()

Returns the path identified as the lead.

**Returns:**
- path identified as the lead

---

#### public
TreePath
getAnchorSelectionPath()

Returns the path identified as the anchor.

**Returns:**
- path identified as the anchor

**Since:**
- 1.3

---

#### public
TreePath
getSelectionPath()

Returns the path to the first selected node.

**Returns:**
- the

TreePath

for the first selected node,
or

null

if nothing is currently selected

---

#### public
TreePath
[] getSelectionPaths()

Returns the paths of all selected values.

**Returns:**
- an array of

TreePath

objects indicating the selected
nodes, or

null

if nothing is currently selected

---

#### public int[] getSelectionRows()

Returns all of the currently selected rows. This method is simply
forwarded to the

TreeSelectionModel

.
If nothing is selected

null

or an empty array will
be returned, based on the

TreeSelectionModel

implementation.

**Returns:**
- an array of integers that identifies all currently selected rows
where 0 is the first row in the display

---

#### @BeanProperty
(
bound
=false)
public int getSelectionCount()

Returns the number of nodes selected.

**Returns:**
- the number of nodes selected

---

#### @BeanProperty
(
bound
=false)
public int getMinSelectionRow()

Returns the smallest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:**
- the smallest selected row

---

#### @BeanProperty
(
bound
=false)
public int getMaxSelectionRow()

Returns the largest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:**
- the largest selected row

---

#### @BeanProperty
(
bound
=false)
public int getLeadSelectionRow()

Returns the row index corresponding to the lead path.

**Returns:**
- an integer giving the row index of the lead path,
where 0 is the first row in the display; or -1
if

leadPath

is

null

---

#### public boolean isPathSelected​(
TreePath
path)

Returns true if the item identified by the path is currently selected.

**Parameters:**
- path

- a

TreePath

identifying a node

**Returns:**
- true if the node is selected

---

#### public boolean isRowSelected​(int row)

Returns true if the node identified by row is selected.

**Parameters:**
- row

- an integer specifying a display row, where 0 is the first
row in the display

**Returns:**
- true if the node is selected

---

#### public
Enumeration
<
TreePath
> getExpandedDescendants​(
TreePath
parent)

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded. If

parent

is not currently
expanded, this will return

null

.
If you expand/collapse nodes while
iterating over the returned

Enumeration

this may not return all
the expanded paths, or may return paths that are no longer expanded.

**Parameters:**
- parent

- the path which is to be examined

**Returns:**
- an

Enumeration

of the descendents of

parent

, or

null

if

parent

is not currently expanded

---

#### public boolean hasBeenExpanded​(
TreePath
path)

Returns true if the node identified by the path has ever been
expanded.

**Parameters:**
- path

- a

TreePath

identifying a node

**Returns:**
- true if the

path

has ever been expanded

---

#### public boolean isExpanded​(
TreePath
path)

Returns true if the node identified by the path is currently expanded,

**Parameters:**
- path

- the

TreePath

specifying the node to check

**Returns:**
- false if any of the nodes in the node's path are collapsed,
true if all nodes in the path are expanded

---

#### public boolean isExpanded​(int row)

Returns true if the node at the specified display row is currently
expanded.

**Parameters:**
- row

- the row to check, where 0 is the first row in the
display

**Returns:**
- true if the node is currently expanded, otherwise false

---

#### public boolean isCollapsed​(
TreePath
path)

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

**Parameters:**
- path

- the

TreePath

to check

**Returns:**
- true if any of the nodes in the node's path are collapsed,
false if all nodes in the path are expanded

---

#### public boolean isCollapsed​(int row)

Returns true if the node at the specified display row is collapsed.

**Parameters:**
- row

- the row to check, where 0 is the first row in the
display

**Returns:**
- true if the node is currently collapsed, otherwise false

---

#### public void makeVisible​(
TreePath
path)

Ensures that the node identified by path is currently viewable.

**Parameters:**
- path

- the

TreePath

to make visible

---

#### public boolean isVisible​(
TreePath
path)

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.
Otherwise, this method returns false.

**Parameters:**
- path

-

TreePath

identifying a node

**Returns:**
- true if the node is viewable, otherwise false

---

#### public
Rectangle
getPathBounds​(
TreePath
path)

Returns the

Rectangle

that the specified node will be drawn
into. Returns

null

if any component in the path is hidden
(under a collapsed parent).

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

**Parameters:**
- path

- the

TreePath

identifying the node

**Returns:**
- the

Rectangle

the node is drawn in,
or

null

---

#### public
Rectangle
getRowBounds​(int row)

Returns the

Rectangle

that the node at the specified row is
drawn in.

**Parameters:**
- row

- the row to be drawn, where 0 is the first row in the
display

**Returns:**
- the

Rectangle

the node is drawn in

---

#### public void scrollPathToVisible​(
TreePath
path)

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:**
- path

- the

TreePath

identifying the node to
bring into view

---

#### public void scrollRowToVisible​(int row)

Scrolls the item identified by row until it is displayed. The minimum
of amount of scrolling necessary to bring the row into view
is performed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:**
- row

- an integer specifying the row to scroll, where 0 is the
first row in the display

---

#### @BeanProperty
(
bound
=false)
public
TreePath
getPathForRow​(int row)

Returns the path for the specified row. If

row

is
not visible, or a

TreeUI

has not been set,

null

is returned.

**Parameters:**
- row

- an integer specifying a row

**Returns:**
- the

TreePath

to the specified node,

null

if

row < 0

or

row >= getRowCount()

---

#### public int getRowForPath​(
TreePath
path)

Returns the row that displays the node identified by the specified
path.

**Parameters:**
- path

- the

TreePath

identifying a node

**Returns:**
- an integer specifying the display row, where 0 is the first
row in the display, or -1 if any of the elements in path
are hidden under a collapsed parent.

---

#### public void expandPath​(
TreePath
path)

Ensures that the node identified by the specified path is
expanded and viewable. If the last item in the path is a
leaf, this will have no effect.

**Parameters:**
- path

- the

TreePath

identifying a node

---

#### public void expandRow​(int row)

Ensures that the node in the specified row is expanded and
viewable.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:**
- row

- an integer specifying a display row, where 0 is the
first row in the display

---

#### public void collapsePath​(
TreePath
path)

Ensures that the node identified by the specified path is
collapsed and viewable.

**Parameters:**
- path

- the

TreePath

identifying a node

---

#### public void collapseRow​(int row)

Ensures that the node in the specified row is collapsed.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:**
- row

- an integer specifying a display row, where 0 is the
first row in the display

---

#### public
TreePath
getPathForLocation​(int x,
int y)

Returns the path for the node at the specified location.

**Parameters:**
- x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
- y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin

**Returns:**
- the

TreePath

for the node at that location

---

#### public int getRowForLocation​(int x,
int y)

Returns the row for the specified location.

**Parameters:**
- x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
- y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin

**Returns:**
- the row corresponding to the location, or -1 if the
location is not within the bounds of a displayed cell

**See Also:**
- getClosestRowForLocation(int, int)

---

#### public
TreePath
getClosestPathForLocation​(int x,
int y)

Returns the path to the node that is closest to x,y. If
no nodes are currently viewable, or there is no model, returns

null

, otherwise it always returns a valid path. To test if
the node is exactly at x, y, get the node's bounds and
test x, y against that.

**Parameters:**
- x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
- y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin

**Returns:**
- the

TreePath

for the node closest to that location,

null

if nothing is viewable or there is no model

**See Also:**
- getPathForLocation(int, int)

,

getPathBounds(javax.swing.tree.TreePath)

---

#### public int getClosestRowForLocation​(int x,
int y)

Returns the row to the node that is closest to x,y. If no nodes
are viewable or there is no model, returns -1. Otherwise,
it always returns a valid row. To test if the returned object is
exactly at x, y, get the bounds for the node at the returned
row and test x, y against that.

**Parameters:**
- x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
- y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin

**Returns:**
- the row closest to the location, -1 if nothing is
viewable or there is no model

**See Also:**
- getRowForLocation(int, int)

,

getRowBounds(int)

---

#### @BeanProperty
(
bound
=false)
public boolean isEditing()

Returns true if the tree is being edited. The item that is being
edited can be obtained using

getSelectionPath

.

**Returns:**
- true if the user is currently editing a node

**See Also:**
- getSelectionPath()

---

#### public boolean stopEditing()

Ends the current editing session.
(The

DefaultTreeCellEditor

object saves any edits that are currently in progress on a cell.
Other implementations may operate differently.)
Has no effect if the tree isn't being edited.

Note:

To make edit-saves automatic whenever the user changes
their position in the tree, use

setInvokesStopCellEditing(boolean)

.

**Returns:**
- true if editing was in progress and is now stopped,
false if editing was not in progress

---

#### public void cancelEditing()

Cancels the current editing session. Has no effect if the
tree isn't being edited.

---

#### public void startEditingAtPath​(
TreePath
path)

Selects the node identified by the specified path and initiates
editing. The edit-attempt fails if the

CellEditor

does not allow
editing for the specified item.

**Parameters:**
- path

- the

TreePath

identifying a node

---

#### @BeanProperty
(
bound
=false)
public
TreePath
getEditingPath()

Returns the path to the element that is currently being edited.

**Returns:**
- the

TreePath

for the node being edited

---

#### @BeanProperty
(
description
="The tree\'s selection model.")
public void setSelectionModel​(
TreeSelectionModel
selectionModel)

Sets the tree's selection model. When a

null

value is
specified an empty

selectionModel

is used, which does not allow selections.

This is a bound property.

**Parameters:**
- selectionModel

- the

TreeSelectionModel

to use,
or

null

to disable selections

**See Also:**
- TreeSelectionModel

---

#### public
TreeSelectionModel
getSelectionModel()

Returns the model for selections. This should always return a
non-

null

value. If you don't want to allow anything
to be selected
set the selection model to

null

, which forces an empty
selection model to be used.

**Returns:**
- the model for selections

**See Also:**
- setSelectionModel(javax.swing.tree.TreeSelectionModel)

---

#### protected
TreePath
[] getPathBetweenRows​(int index0,
int index1)

Returns the paths (inclusive) between the specified rows. If
the specified indices are within the viewable set of rows, or
bound the viewable set of rows, then the indices are
constrained by the viewable set of rows. If the specified
indices are not within the viewable set of rows, or do not
bound the viewable set of rows, then an empty array is
returned. For example, if the row count is

10

, and this
method is invoked with

-1, 20

, then the specified
indices are constrained to the viewable set of rows, and this is
treated as if invoked with

0, 9

. On the other hand, if
this were invoked with

-10, -1

, then the specified
indices do not bound the viewable set of rows, and an empty
array is returned.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

**Parameters:**
- index0

- the first index in the range
- index1

- the last index in the range

**Returns:**
- the paths (inclusive) between the specified row indices

---

#### public void setSelectionInterval​(int index0,
int index1)

Selects the rows in the specified interval (inclusive). If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified rows are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is cleared. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified indices bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified indices do not
bound the viewable set of rows, and the selection is cleared.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

**Parameters:**
- index0

- the first index in the range to select
- index1

- the last index in the range to select

---

#### public void addSelectionInterval​(int index0,
int index1)

Adds the specified rows (inclusive) to the selection. If the
specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are
constrained by the viewable set of rows. If the indices are not
within the viewable set of rows, or do not bound the viewable
set of rows, then the selection is unchanged. For example, if
the row count is

10

, and this method is invoked with

-1, 20

, then the specified indices bounds the viewable
range, and this is treated as if invoked with

0, 9

. On
the other hand, if this were invoked with

-10, -1

, then
the specified indices do not bound the viewable set of rows,
and the selection is unchanged.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

**Parameters:**
- index0

- the first index in the range to add to the selection
- index1

- the last index in the range to add to the selection

---

#### public void removeSelectionInterval​(int index0,
int index1)

Removes the specified rows (inclusive) from the selection. If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is unchanged. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified range bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified range does not
bound the viewable set of rows, and the selection is unchanged.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

**Parameters:**
- index0

- the first row to remove from the selection
- index1

- the last row to remove from the selection

---

#### public void removeSelectionPath​(
TreePath
path)

Removes the node identified by the specified path from the current
selection.

**Parameters:**
- path

- the

TreePath

identifying a node

---

#### public void removeSelectionPaths​(
TreePath
[] paths)

Removes the nodes identified by the specified paths from the
current selection.

**Parameters:**
- paths

- an array of

TreePath

objects that
specifies the nodes to remove

---

#### public void removeSelectionRow​(int row)

Removes the row at the index

row

from the current
selection.

**Parameters:**
- row

- the row to remove

---

#### public void removeSelectionRows​(int[] rows)

Removes the rows that are selected at each of the specified
rows.

**Parameters:**
- rows

- an array of ints specifying display rows, where 0 is
the first row in the display

---

#### public void clearSelection()

Clears the selection.

---

#### @BeanProperty
(
bound
=false)
public boolean isSelectionEmpty()

Returns true if the selection is currently empty.

**Returns:**
- true if the selection is currently empty

---

#### public void addTreeExpansionListener​(
TreeExpansionListener
tel)

Adds a listener for

TreeExpansion

events.

**Parameters:**
- tel

- a TreeExpansionListener that will be notified when
a tree node is expanded or collapsed (a "negative
expansion")

---

#### public void removeTreeExpansionListener​(
TreeExpansionListener
tel)

Removes a listener for

TreeExpansion

events.

**Parameters:**
- tel

- the

TreeExpansionListener

to remove

---

#### @BeanProperty
(
bound
=false)
public
TreeExpansionListener
[] getTreeExpansionListeners()

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

**Returns:**
- all of the

TreeExpansionListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void addTreeWillExpandListener​(
TreeWillExpandListener
tel)

Adds a listener for

TreeWillExpand

events.

**Parameters:**
- tel

- a

TreeWillExpandListener

that will be notified
when a tree node will be expanded or collapsed (a "negative
expansion")

---

#### public void removeTreeWillExpandListener​(
TreeWillExpandListener
tel)

Removes a listener for

TreeWillExpand

events.

**Parameters:**
- tel

- the

TreeWillExpandListener

to remove

---

#### @BeanProperty
(
bound
=false)
public
TreeWillExpandListener
[] getTreeWillExpandListeners()

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

**Returns:**
- all of the

TreeWillExpandListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void fireTreeExpanded​(
TreePath
path)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:**
- path

- the

TreePath

indicating the node that was
expanded

**See Also:**
- EventListenerList

---

#### public void fireTreeCollapsed​(
TreePath
path)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:**
- path

- the

TreePath

indicating the node that was
collapsed

**See Also:**
- EventListenerList

---

#### public void fireTreeWillExpand​(
TreePath
path)
throws
ExpandVetoException

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:**
- path

- the

TreePath

indicating the node that was
expanded

**Throws:**
- ExpandVetoException

- if the expansion is prevented from occurring

**See Also:**
- EventListenerList

---

#### public void fireTreeWillCollapse​(
TreePath
path)
throws
ExpandVetoException

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:**
- path

- the

TreePath

indicating the node that was
expanded

**Throws:**
- ExpandVetoException

- if the collapse is prevented from occurring

**See Also:**
- EventListenerList

---

#### public void addTreeSelectionListener​(
TreeSelectionListener
tsl)

Adds a listener for

TreeSelection

events.

**Parameters:**
- tsl

- the

TreeSelectionListener

that will be notified
when a node is selected or deselected (a "negative
selection")

---

#### public void removeTreeSelectionListener​(
TreeSelectionListener
tsl)

Removes a

TreeSelection

listener.

**Parameters:**
- tsl

- the

TreeSelectionListener

to remove

---

#### @BeanProperty
(
bound
=false)
public
TreeSelectionListener
[] getTreeSelectionListeners()

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

**Returns:**
- all of the

TreeSelectionListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### protected void fireValueChanged​(
TreeSelectionEvent
e)

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:**
- e

- the

TreeSelectionEvent

to be fired;
generated by the

TreeSelectionModel

when a node is selected or deselected

**See Also:**
- EventListenerList

---

#### public void treeDidChange()

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree). You should never have to
invoke this, the UI will invoke this as it needs to.

---

#### @BeanProperty
(
description
="The number of rows that are to be displayed.")
public void setVisibleRowCount​(int newCount)

Sets the number of rows that are to be displayed.
This will only work if the tree is contained in a

JScrollPane

,
and will adjust the preferred size and size of that scrollpane.

This is a bound property.

**Parameters:**
- newCount

- the number of rows to display

---

#### public int getVisibleRowCount()

Returns the number of rows that are displayed in the display area.

**Returns:**
- the number of rows displayed

---

#### public
TreePath
getNextMatch​(
String
prefix,
int startingRow,

Position.Bias
bias)

Returns the TreePath to the next tree element that
begins with a prefix. To handle the conversion of a

TreePath

into a String,

convertValueToText

is used.

**Parameters:**
- prefix

- the string to test for a match
- startingRow

- the row for starting the search
- bias

- the search direction, either
Position.Bias.Forward or Position.Bias.Backward.

**Returns:**
- the TreePath of the next tree element that
starts with the prefix; otherwise null

**Throws:**
- IllegalArgumentException

- if prefix is null
or startingRow is out of bounds

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false)
public
Dimension
getPreferredScrollableViewportSize()

Returns the preferred display size of a

JTree

. The height is
determined from

getVisibleRowCount

and the width
is the current preferred width.

**Specified by:**
- getPreferredScrollableViewportSize

in interface

Scrollable

**Returns:**
- a

Dimension

object containing the preferred size

**See Also:**
- JComponent.getPreferredSize()

---

#### public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)

Returns the amount to increment when scrolling. The amount is
the height of the first displayed row that isn't completely in view
or, if it is totally displayed, the height of the next row in the
scrolling direction.

**Specified by:**
- getScrollableUnitIncrement

in interface

Scrollable

**Parameters:**
- visibleRect

- the view area visible within the viewport
- orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
- direction

- less than zero to scroll up/left,
greater than zero for down/right

**Returns:**
- the "unit" increment for scrolling in the specified direction

**See Also:**
- JScrollBar.setUnitIncrement(int)

---

#### public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

**Specified by:**
- getScrollableBlockIncrement

in interface

Scrollable

**Parameters:**
- visibleRect

- the view area visible within the viewport
- orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
- direction

- less than zero to scroll up/left,
greater than zero for down/right.

**Returns:**
- the "block" increment for scrolling in the specified direction

**See Also:**
- JScrollBar.setBlockIncrement(int)

---

#### @BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:**
- getScrollableTracksViewportWidth

in interface

Scrollable

**Returns:**
- whether the tree should track the width of the viewport

**See Also:**
- Scrollable.getScrollableTracksViewportWidth()

---

#### @BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:**
- getScrollableTracksViewportHeight

in interface

Scrollable

**Returns:**
- whether the tree should track the height of the viewport

**See Also:**
- Scrollable.getScrollableTracksViewportHeight()

---

#### protected void setExpandedState​(
TreePath
path,
boolean state)

Sets the expanded state of this

JTree

.
If

state

is
true, all parents of

path

and path are marked as
expanded. If

state

is false, all parents of

path

are marked EXPANDED, but

path

itself
is marked collapsed.

This will fail if a

TreeWillExpandListener

vetos it.

**Parameters:**
- path

- a

TreePath

identifying a node
- state

- if

true

, all parents of @{code path} and path are marked as expanded.
Otherwise, all parents of

path

are marked EXPANDED,
but

path

itself is marked collapsed.

---

#### protected
Enumeration
<
TreePath
> getDescendantToggledPaths​(
TreePath
parent)

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

**Parameters:**
- parent

- a path

**Returns:**
- the

Enumeration

of

TreePaths

---

#### protected void removeDescendantToggledPaths​(
Enumeration
<
TreePath
> toRemove)

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

**Parameters:**
- toRemove

- an enumeration of the paths to remove; a value of

null

is ignored

**Throws:**
- ClassCastException

- if

toRemove

contains an
element that is not a

TreePath

;

null

values are ignored

---

#### protected void clearToggledPaths()

Clears the cache of toggled tree paths. This does NOT send out
any

TreeExpansionListener

events.

---

#### protected
TreeModelListener
createTreeModelListener()

Creates and returns an instance of

TreeModelHandler

.
The returned
object is responsible for updating the expanded state when the

TreeModel

changes.

For more information on what expanded state means, see the

JTree description

above.

**Returns:**
- the instance of

TreeModelHandler

---

#### protected boolean removeDescendantSelectedPaths​(
TreePath
path,
boolean includePath)

Removes any paths in the selection that are descendants of

path

. If

includePath

is true and

path

is selected, it will be removed from the selection.

**Parameters:**
- path

- a path
- includePath

- is

true

and

path

is selected,
it will be removed from the selection.

**Returns:**
- true if a descendant was selected

**Since:**
- 1.3

---

#### protected
String
paramString()

Returns a string representation of this

JTree

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

JTree

.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JTree.
For JTrees, the AccessibleContext takes the form of an
AccessibleJTree.
A new AccessibleJTree instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJTree that serves as the
AccessibleContext of this JTree

---

### Additional Sections

#### Class JTree

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JTree

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JTree

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JTree

javax.swing.JComponent

- javax.swing.JTree

javax.swing.JTree

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

Scrollable

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component that displays a set of hierarchical data as an outline.")
public class
JTree

extends
JComponent

implements
Scrollable
,
Accessible
```

A control that displays a set of hierarchical data as an outline.
You can find task-oriented documentation and examples of using trees in

How to Use Trees

,
a section in

The Java Tutorial.

A specific node in a tree can be identified either by a

TreePath

(an object
that encapsulates a node and all of its ancestors), or by its
display row, where each row in the display area displays one node.
An

expanded

node is a non-leaf node (as identified by

TreeModel.isLeaf(node)

returning false) that will displays
its children when all its ancestors are

expanded

.
A

collapsed

node is one which hides them. A

hidden

node is one which is
under a collapsed ancestor. All of a

viewable

nodes parents
are expanded, but may or may not be displayed. A

displayed

node
is both viewable and in the display area, where it can be seen.

The following

JTree

methods use "visible" to mean "displayed":

- isRootVisible()

setRootVisible()

scrollPathToVisible()

scrollRowToVisible()

getVisibleRowCount()

setVisibleRowCount()

The next group of

JTree

methods use "visible" to mean
"viewable" (under an expanded parent):

- isVisible()

makeVisible()

If you are interested in knowing when the selection changes implement
the

TreeSelectionListener

interface and add the instance
using the method

addTreeSelectionListener

.

valueChanged

will be invoked when the
selection changes, that is if the user clicks twice on the same
node

valueChanged

will only be invoked once.

If you are interested in detecting either double-click events or when
a user clicks on a node, regardless of whether or not it was selected,
we recommend you do the following:

```java
final JTree tree = ...;

MouseListener ml = new MouseAdapter() {
public void
mousePressed
(MouseEvent e) {
int selRow = tree.getRowForLocation(e.getX(), e.getY());
TreePath selPath = tree.getPathForLocation(e.getX(), e.getY());
if(selRow != -1) {
if(e.getClickCount() == 1) {
mySingleClick(selRow, selPath);
}
else if(e.getClickCount() == 2) {
myDoubleClick(selRow, selPath);
}
}
}
};
tree.addMouseListener(ml);
```

NOTE: This example obtains both the path and row, but you only need to
get the one you're interested in.

To use

JTree

to display compound nodes
(for example, nodes containing both
a graphic icon and text), subclass

TreeCellRenderer

and use

setCellRenderer(javax.swing.tree.TreeCellRenderer)

to tell the tree to use it. To edit such nodes,
subclass

TreeCellEditor

and use

setCellEditor(javax.swing.tree.TreeCellEditor)

.

Like all

JComponent

classes, you can use

InputMap

and

ActionMap

to associate an

Action

object with a

KeyStroke

and execute the action under specified conditions.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

**Since:** 1.2
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component that displays a set of hierarchical data as an outline.")
public class

JTree

extends

JComponent

implements

Scrollable

,

Accessible

A control that displays a set of hierarchical data as an outline.
You can find task-oriented documentation and examples of using trees in

How to Use Trees

,
a section in

The Java Tutorial.

A specific node in a tree can be identified either by a

TreePath

(an object
that encapsulates a node and all of its ancestors), or by its
display row, where each row in the display area displays one node.
An

expanded

node is a non-leaf node (as identified by

TreeModel.isLeaf(node)

returning false) that will displays
its children when all its ancestors are

expanded

.
A

collapsed

node is one which hides them. A

hidden

node is one which is
under a collapsed ancestor. All of a

viewable

nodes parents
are expanded, but may or may not be displayed. A

displayed

node
is both viewable and in the display area, where it can be seen.

The following

JTree

methods use "visible" to mean "displayed":

- isRootVisible()

setRootVisible()

scrollPathToVisible()

scrollRowToVisible()

getVisibleRowCount()

setVisibleRowCount()

The next group of

JTree

methods use "visible" to mean
"viewable" (under an expanded parent):

- isVisible()

makeVisible()

If you are interested in knowing when the selection changes implement
the

TreeSelectionListener

interface and add the instance
using the method

addTreeSelectionListener

.

valueChanged

will be invoked when the
selection changes, that is if the user clicks twice on the same
node

valueChanged

will only be invoked once.

If you are interested in detecting either double-click events or when
a user clicks on a node, regardless of whether or not it was selected,
we recommend you do the following:

```java
final JTree tree = ...;

MouseListener ml = new MouseAdapter() {
public void
mousePressed
(MouseEvent e) {
int selRow = tree.getRowForLocation(e.getX(), e.getY());
TreePath selPath = tree.getPathForLocation(e.getX(), e.getY());
if(selRow != -1) {
if(e.getClickCount() == 1) {
mySingleClick(selRow, selPath);
}
else if(e.getClickCount() == 2) {
myDoubleClick(selRow, selPath);
}
}
}
};
tree.addMouseListener(ml);
```

NOTE: This example obtains both the path and row, but you only need to
get the one you're interested in.

To use

JTree

to display compound nodes
(for example, nodes containing both
a graphic icon and text), subclass

TreeCellRenderer

and use

setCellRenderer(javax.swing.tree.TreeCellRenderer)

to tell the tree to use it. To edit such nodes,
subclass

TreeCellEditor

and use

setCellEditor(javax.swing.tree.TreeCellEditor)

.

Like all

JComponent

classes, you can use

InputMap

and

ActionMap

to associate an

Action

object with a

KeyStroke

and execute the action under specified conditions.

Warning:

Swing is not thread safe. For more
information see

Swing's Threading
Policy

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

A specific node in a tree can be identified either by a

TreePath

(an object
that encapsulates a node and all of its ancestors), or by its
display row, where each row in the display area displays one node.
An

expanded

node is a non-leaf node (as identified by

TreeModel.isLeaf(node)

returning false) that will displays
its children when all its ancestors are

expanded

.
A

collapsed

node is one which hides them. A

hidden

node is one which is
under a collapsed ancestor. All of a

viewable

nodes parents
are expanded, but may or may not be displayed. A

displayed

node
is both viewable and in the display area, where it can be seen.

isRootVisible()

setRootVisible()

scrollPathToVisible()

scrollRowToVisible()

getVisibleRowCount()

setVisibleRowCount()

isVisible()

makeVisible()

If you are interested in detecting either double-click events or when
a user clicks on a node, regardless of whether or not it was selected,
we recommend you do the following:

final JTree tree = ...;

MouseListener ml = new MouseAdapter() {
public void

mousePressed

(MouseEvent e) {
int selRow = tree.getRowForLocation(e.getX(), e.getY());
TreePath selPath = tree.getPathForLocation(e.getX(), e.getY());
if(selRow != -1) {
if(e.getClickCount() == 1) {
mySingleClick(selRow, selPath);
}
else if(e.getClickCount() == 2) {
myDoubleClick(selRow, selPath);
}
}
}
};
tree.addMouseListener(ml);

To use

JTree

to display compound nodes
(for example, nodes containing both
a graphic icon and text), subclass

TreeCellRenderer

and use

setCellRenderer(javax.swing.tree.TreeCellRenderer)

to tell the tree to use it. To edit such nodes,
subclass

TreeCellEditor

and use

setCellEditor(javax.swing.tree.TreeCellEditor)

.

Like all

JComponent

classes, you can use

InputMap

and

ActionMap

to associate an

Action

object with a

KeyStroke

and execute the action under specified conditions.

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

JTree.AccessibleJTree

This class implements accessibility support for the

JTree

class.

static class

JTree.DropLocation

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

.

static class

JTree.DynamicUtilTreeNode

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary.

protected static class

JTree.EmptySelectionModel

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

protected class

JTree.TreeModelHandler

Listens to the model and updates the

expandedState

accordingly when nodes are removed, or changed.

protected class

JTree.TreeSelectionRedirector

Handles creating a new

TreeSelectionEvent

with the

JTree

as the
source and passing it off to all the listeners.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

ANCHOR_SELECTION_PATH_PROPERTY

Bound property name for anchor selection path.

static

String

CELL_EDITOR_PROPERTY

Bound property name for

cellEditor

.

static

String

CELL_RENDERER_PROPERTY

Bound property name for

cellRenderer

.

protected

TreeCellEditor

cellEditor

Editor for the entries.

protected

TreeCellRenderer

cellRenderer

The cell used to draw nodes.

protected boolean

editable

Is the tree editable?

static

String

EDITABLE_PROPERTY

Bound property name for

editable

.

static

String

EXPANDS_SELECTED_PATHS_PROPERTY

Bound property name for expands selected paths property

static

String

INVOKES_STOP_CELL_EDITING_PROPERTY

Bound property name for

messagesStopCellEditing

.

protected boolean

invokesStopCellEditing

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved.

static

String

LARGE_MODEL_PROPERTY

Bound property name for

largeModel

.

protected boolean

largeModel

Is this tree a large model?

static

String

LEAD_SELECTION_PATH_PROPERTY

Bound property name for

leadSelectionPath

.

static

String

ROOT_VISIBLE_PROPERTY

Bound property name for

rootVisible

.

protected boolean

rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

static

String

ROW_HEIGHT_PROPERTY

Bound property name for

rowHeight

.

protected int

rowHeight

Height to use for each display row.

static

String

SCROLLS_ON_EXPAND_PROPERTY

Bound property name for

scrollsOnExpand

.

protected boolean

scrollsOnExpand

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

static

String

SELECTION_MODEL_PROPERTY

Bound property name for selectionModel.

protected

TreeSelectionModel

selectionModel

Models the set of selected nodes in this tree.

protected

JTree.TreeSelectionRedirector

selectionRedirector

Creates a new event and passed it off the

selectionListeners

.

static

String

SHOWS_ROOT_HANDLES_PROPERTY

Bound property name for

showsRootHandles

.

protected boolean

showsRootHandles

True if handles are displayed at the topmost level of the tree.

static

String

TOGGLE_CLICK_COUNT_PROPERTY

Bound property name for

toggleClickCount

.

protected int

toggleClickCount

Number of mouse clicks before a node is expanded.

static

String

TREE_MODEL_PROPERTY

Bound property name for

treeModel

.

protected

TreeModel

treeModel

The model that defines the tree displayed by this object.

protected

TreeModelListener

treeModelListener

Updates the

expandedState

.

static

String

VISIBLE_ROW_COUNT_PROPERTY

Bound property name for

visibleRowCount

.

protected int

visibleRowCount

Number of rows to make visible at one time.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JTree

()

Returns a

JTree

with a sample model.

JTree

​(

Object

[] value)

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.

JTree

​(

Hashtable

<?,​?> value)

Returns a

JTree

created from a

Hashtable

which does not display with root.

JTree

​(

Vector

<?> value)

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed.

JTree

​(

TreeModel

newModel)

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

JTree

​(

TreeNode

root)

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.

JTree

​(

TreeNode

root,
boolean asksAllowsChildren)

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

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

addSelectionInterval

​(int index0,
int index1)

Adds the specified rows (inclusive) to the selection.

void

addSelectionPath

​(

TreePath

path)

Adds the node identified by the specified

TreePath

to the current selection.

void

addSelectionPaths

​(

TreePath

[] paths)

Adds each path in the array of paths to the current selection.

void

addSelectionRow

​(int row)

Adds the path at the specified row to the current selection.

void

addSelectionRows

​(int[] rows)

Adds the paths at each of the specified rows to the current selection.

void

addTreeExpansionListener

​(

TreeExpansionListener

tel)

Adds a listener for

TreeExpansion

events.

void

addTreeSelectionListener

​(

TreeSelectionListener

tsl)

Adds a listener for

TreeSelection

events.

void

addTreeWillExpandListener

​(

TreeWillExpandListener

tel)

Adds a listener for

TreeWillExpand

events.

void

cancelEditing

()

Cancels the current editing session.

void

clearSelection

()

Clears the selection.

protected void

clearToggledPaths

()

Clears the cache of toggled tree paths.

void

collapsePath

​(

TreePath

path)

Ensures that the node identified by the specified path is
collapsed and viewable.

void

collapseRow

​(int row)

Ensures that the node in the specified row is collapsed.

String

convertValueToText

​(

Object

value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Called by the renderers to convert the specified value to
text.

protected static

TreeModel

createTreeModel

​(

Object

value)

Returns a

TreeModel

wrapping the specified object.

protected

TreeModelListener

createTreeModelListener

()

Creates and returns an instance of

TreeModelHandler

.

void

expandPath

​(

TreePath

path)

Ensures that the node identified by the specified path is
expanded and viewable.

void

expandRow

​(int row)

Ensures that the node in the specified row is expanded and
viewable.

void

fireTreeCollapsed

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeExpanded

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeWillCollapse

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeWillExpand

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireValueChanged

​(

TreeSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTree.

TreePath

getAnchorSelectionPath

()

Returns the path identified as the anchor.

TreeCellEditor

getCellEditor

()

Returns the editor used to edit entries in the tree.

TreeCellRenderer

getCellRenderer

()

Returns the current

TreeCellRenderer

that is rendering each cell.

TreePath

getClosestPathForLocation

​(int x,
int y)

Returns the path to the node that is closest to x,y.

int

getClosestRowForLocation

​(int x,
int y)

Returns the row to the node that is closest to x,y.

protected static

TreeModel

getDefaultTreeModel

()

Creates and returns a sample

TreeModel

.

protected

Enumeration

<

TreePath

>

getDescendantToggledPaths

​(

TreePath

parent)

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

boolean

getDragEnabled

()

Returns whether or not automatic drag handling is enabled.

JTree.DropLocation

getDropLocation

()

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

DropMode

getDropMode

()

Returns the drop mode for this component.

TreePath

getEditingPath

()

Returns the path to the element that is currently being edited.

Enumeration

<

TreePath

>

getExpandedDescendants

​(

TreePath

parent)

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded.

boolean

getExpandsSelectedPaths

()

Returns the

expandsSelectedPaths

property.

boolean

getInvokesStopCellEditing

()

Returns the indicator that tells what happens when editing is
interrupted.

Object

getLastSelectedPathComponent

()

Returns the last path component of the selected path.

TreePath

getLeadSelectionPath

()

Returns the path identified as the lead.

int

getLeadSelectionRow

()

Returns the row index corresponding to the lead path.

int

getMaxSelectionRow

()

Returns the largest selected row.

int

getMinSelectionRow

()

Returns the smallest selected row.

TreeModel

getModel

()

Returns the

TreeModel

that is providing the data.

TreePath

getNextMatch

​(

String

prefix,
int startingRow,

Position.Bias

bias)

Returns the TreePath to the next tree element that
begins with a prefix.

protected

TreePath

[]

getPathBetweenRows

​(int index0,
int index1)

Returns the paths (inclusive) between the specified rows.

Rectangle

getPathBounds

​(

TreePath

path)

Returns the

Rectangle

that the specified node will be drawn
into.

TreePath

getPathForLocation

​(int x,
int y)

Returns the path for the node at the specified location.

TreePath

getPathForRow

​(int row)

Returns the path for the specified row.

Dimension

getPreferredScrollableViewportSize

()

Returns the preferred display size of a

JTree

.

Rectangle

getRowBounds

​(int row)

Returns the

Rectangle

that the node at the specified row is
drawn in.

int

getRowCount

()

Returns the number of viewable nodes.

int

getRowForLocation

​(int x,
int y)

Returns the row for the specified location.

int

getRowForPath

​(

TreePath

path)

Returns the row that displays the node identified by the specified
path.

int

getRowHeight

()

Returns the height of each row.

int

getScrollableBlockIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

boolean

getScrollableTracksViewportHeight

()

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height.

boolean

getScrollableTracksViewportWidth

()

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width.

int

getScrollableUnitIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount to increment when scrolling.

boolean

getScrollsOnExpand

()

Returns the value of the

scrollsOnExpand

property.

int

getSelectionCount

()

Returns the number of nodes selected.

TreeSelectionModel

getSelectionModel

()

Returns the model for selections.

TreePath

getSelectionPath

()

Returns the path to the first selected node.

TreePath

[]

getSelectionPaths

()

Returns the paths of all selected values.

int[]

getSelectionRows

()

Returns all of the currently selected rows.

boolean

getShowsRootHandles

()

Returns the value of the

showsRootHandles

property.

int

getToggleClickCount

()

Returns the number of mouse clicks needed to expand or close a node.

String

getToolTipText

​(

MouseEvent

event)

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

TreeExpansionListener

[]

getTreeExpansionListeners

()

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

TreeSelectionListener

[]

getTreeSelectionListeners

()

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

TreeWillExpandListener

[]

getTreeWillExpandListeners

()

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

TreeUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

int

getVisibleRowCount

()

Returns the number of rows that are displayed in the display area.

boolean

hasBeenExpanded

​(

TreePath

path)

Returns true if the node identified by the path has ever been
expanded.

boolean

isCollapsed

​(int row)

Returns true if the node at the specified display row is collapsed.

boolean

isCollapsed

​(

TreePath

path)

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

boolean

isEditable

()

Returns true if the tree is editable.

boolean

isEditing

()

Returns true if the tree is being edited.

boolean

isExpanded

​(int row)

Returns true if the node at the specified display row is currently
expanded.

boolean

isExpanded

​(

TreePath

path)

Returns true if the node identified by the path is currently expanded,

boolean

isFixedRowHeight

()

Returns true if the height of each display row is a fixed size.

boolean

isLargeModel

()

Returns true if the tree is configured for a large model.

boolean

isPathEditable

​(

TreePath

path)

Returns

isEditable

.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the item identified by the path is currently selected.

boolean

isRootVisible

()

Returns true if the root node of the tree is displayed.

boolean

isRowSelected

​(int row)

Returns true if the node identified by row is selected.

boolean

isSelectionEmpty

()

Returns true if the selection is currently empty.

boolean

isVisible

​(

TreePath

path)

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.

void

makeVisible

​(

TreePath

path)

Ensures that the node identified by path is currently viewable.

protected

String

paramString

()

Returns a string representation of this

JTree

.

protected boolean

removeDescendantSelectedPaths

​(

TreePath

path,
boolean includePath)

Removes any paths in the selection that are descendants of

path

.

protected void

removeDescendantToggledPaths

​(

Enumeration

<

TreePath

> toRemove)

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

void

removeSelectionInterval

​(int index0,
int index1)

Removes the specified rows (inclusive) from the selection.

void

removeSelectionPath

​(

TreePath

path)

Removes the node identified by the specified path from the current
selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

Removes the nodes identified by the specified paths from the
current selection.

void

removeSelectionRow

​(int row)

Removes the row at the index

row

from the current
selection.

void

removeSelectionRows

​(int[] rows)

Removes the rows that are selected at each of the specified
rows.

void

removeTreeExpansionListener

​(

TreeExpansionListener

tel)

Removes a listener for

TreeExpansion

events.

void

removeTreeSelectionListener

​(

TreeSelectionListener

tsl)

Removes a

TreeSelection

listener.

void

removeTreeWillExpandListener

​(

TreeWillExpandListener

tel)

Removes a listener for

TreeWillExpand

events.

void

scrollPathToVisible

​(

TreePath

path)

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed.

void

scrollRowToVisible

​(int row)

Scrolls the item identified by row until it is displayed.

void

setAnchorSelectionPath

​(

TreePath

newPath)

Sets the path identified as the anchor.

void

setCellEditor

​(

TreeCellEditor

cellEditor)

Sets the cell editor.

void

setCellRenderer

​(

TreeCellRenderer

x)

Sets the

TreeCellRenderer

that will be used to
draw each cell.

void

setDragEnabled

​(boolean b)

Turns on or off automatic drag handling.

void

setDropMode

​(

DropMode

dropMode)

Sets the drop mode for this component.

void

setEditable

​(boolean flag)

Determines whether the tree is editable.

protected void

setExpandedState

​(

TreePath

path,
boolean state)

Sets the expanded state of this

JTree

.

void

setExpandsSelectedPaths

​(boolean newValue)

Configures the

expandsSelectedPaths

property.

void

setInvokesStopCellEditing

​(boolean newValue)

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means.

void

setLargeModel

​(boolean newValue)

Specifies whether the UI should use a large model.

void

setLeadSelectionPath

​(

TreePath

newPath)

Sets the path identifies as the lead.

void

setModel

​(

TreeModel

newModel)

Sets the

TreeModel

that will provide the data.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell, in pixels.

void

setScrollsOnExpand

​(boolean newValue)

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.

void

setSelectionInterval

​(int index0,
int index1)

Selects the rows in the specified interval (inclusive).

void

setSelectionModel

​(

TreeSelectionModel

selectionModel)

Sets the tree's selection model.

void

setSelectionPath

​(

TreePath

path)

Selects the node identified by the specified path.

void

setSelectionPaths

​(

TreePath

[] paths)

Selects the nodes identified by the specified array of paths.

void

setSelectionRow

​(int row)

Selects the node at the specified row in the display.

void

setSelectionRows

​(int[] rows)

Selects the nodes corresponding to each of the specified rows
in the display.

void

setShowsRootHandles

​(boolean newValue)

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.

void

setToggleClickCount

​(int clickCount)

Sets the number of mouse clicks before a node will expand or close.

void

setUI

​(

TreeUI

ui)

Sets the L&F object that renders this component.

void

setVisibleRowCount

​(int newCount)

Sets the number of rows that are to be displayed.

void

startEditingAtPath

​(

TreePath

path)

Selects the node identified by the specified path and initiates
editing.

boolean

stopEditing

()

Ends the current editing session.

void

treeDidChange

()

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree).

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

JTree.AccessibleJTree

This class implements accessibility support for the

JTree

class.

static class

JTree.DropLocation

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

.

static class

JTree.DynamicUtilTreeNode

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary.

protected static class

JTree.EmptySelectionModel

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

protected class

JTree.TreeModelHandler

Listens to the model and updates the

expandedState

accordingly when nodes are removed, or changed.

protected class

JTree.TreeSelectionRedirector

Handles creating a new

TreeSelectionEvent

with the

JTree

as the
source and passing it off to all the listeners.

- Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

- Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

- Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested Class Summary

This class implements accessibility support for the

JTree

class.

A subclass of

TransferHandler.DropLocation

representing
a drop location for a

JTree

.

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary.

EmptySelectionModel

is a

TreeSelectionModel

that does not allow anything to be selected.

Listens to the model and updates the

expandedState

accordingly when nodes are removed, or changed.

Handles creating a new

TreeSelectionEvent

with the

JTree

as the
source and passing it off to all the listeners.

Nested classes/interfaces declared in class javax.swing.

JComponent

JComponent.AccessibleJComponent

---

#### Nested classes/interfaces declared in class javax.swing. JComponent

Nested classes/interfaces declared in class java.awt.

Container

Container.AccessibleAWTContainer

---

#### Nested classes/interfaces declared in class java.awt. Container

Nested classes/interfaces declared in class java.awt.

Component

Component.AccessibleAWTComponent

,

Component.BaselineResizeBehavior

,

Component.BltBufferStrategy

,

Component.FlipBufferStrategy

---

#### Nested classes/interfaces declared in class java.awt. Component

Field Summary

Fields

Modifier and Type

Field

Description

static

String

ANCHOR_SELECTION_PATH_PROPERTY

Bound property name for anchor selection path.

static

String

CELL_EDITOR_PROPERTY

Bound property name for

cellEditor

.

static

String

CELL_RENDERER_PROPERTY

Bound property name for

cellRenderer

.

protected

TreeCellEditor

cellEditor

Editor for the entries.

protected

TreeCellRenderer

cellRenderer

The cell used to draw nodes.

protected boolean

editable

Is the tree editable?

static

String

EDITABLE_PROPERTY

Bound property name for

editable

.

static

String

EXPANDS_SELECTED_PATHS_PROPERTY

Bound property name for expands selected paths property

static

String

INVOKES_STOP_CELL_EDITING_PROPERTY

Bound property name for

messagesStopCellEditing

.

protected boolean

invokesStopCellEditing

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved.

static

String

LARGE_MODEL_PROPERTY

Bound property name for

largeModel

.

protected boolean

largeModel

Is this tree a large model?

static

String

LEAD_SELECTION_PATH_PROPERTY

Bound property name for

leadSelectionPath

.

static

String

ROOT_VISIBLE_PROPERTY

Bound property name for

rootVisible

.

protected boolean

rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

static

String

ROW_HEIGHT_PROPERTY

Bound property name for

rowHeight

.

protected int

rowHeight

Height to use for each display row.

static

String

SCROLLS_ON_EXPAND_PROPERTY

Bound property name for

scrollsOnExpand

.

protected boolean

scrollsOnExpand

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

static

String

SELECTION_MODEL_PROPERTY

Bound property name for selectionModel.

protected

TreeSelectionModel

selectionModel

Models the set of selected nodes in this tree.

protected

JTree.TreeSelectionRedirector

selectionRedirector

Creates a new event and passed it off the

selectionListeners

.

static

String

SHOWS_ROOT_HANDLES_PROPERTY

Bound property name for

showsRootHandles

.

protected boolean

showsRootHandles

True if handles are displayed at the topmost level of the tree.

static

String

TOGGLE_CLICK_COUNT_PROPERTY

Bound property name for

toggleClickCount

.

protected int

toggleClickCount

Number of mouse clicks before a node is expanded.

static

String

TREE_MODEL_PROPERTY

Bound property name for

treeModel

.

protected

TreeModel

treeModel

The model that defines the tree displayed by this object.

protected

TreeModelListener

treeModelListener

Updates the

expandedState

.

static

String

VISIBLE_ROW_COUNT_PROPERTY

Bound property name for

visibleRowCount

.

protected int

visibleRowCount

Number of rows to make visible at one time.

- Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

- Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

- Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Field Summary

Bound property name for anchor selection path.

Bound property name for

cellEditor

.

Bound property name for

cellRenderer

.

Editor for the entries.

The cell used to draw nodes.

Is the tree editable?

Bound property name for

editable

.

Bound property name for expands selected paths property

Bound property name for

messagesStopCellEditing

.

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved.

Bound property name for

largeModel

.

Is this tree a large model?

Bound property name for

leadSelectionPath

.

Bound property name for

rootVisible

.

True if the root node is displayed, false if its children are
the highest visible nodes.

Bound property name for

rowHeight

.

Height to use for each display row.

Bound property name for

scrollsOnExpand

.

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

Bound property name for selectionModel.

Models the set of selected nodes in this tree.

Creates a new event and passed it off the

selectionListeners

.

Bound property name for

showsRootHandles

.

True if handles are displayed at the topmost level of the tree.

Bound property name for

toggleClickCount

.

Number of mouse clicks before a node is expanded.

Bound property name for

treeModel

.

The model that defines the tree displayed by this object.

Updates the

expandedState

.

Bound property name for

visibleRowCount

.

Number of rows to make visible at one time.

Fields declared in class javax.swing.

JComponent

listenerList

,

TOOL_TIP_TEXT_KEY

,

ui

,

UNDEFINED_CONDITION

,

WHEN_ANCESTOR_OF_FOCUSED_COMPONENT

,

WHEN_FOCUSED

,

WHEN_IN_FOCUSED_WINDOW

---

#### Fields declared in class javax.swing. JComponent

Fields declared in class java.awt.

Component

accessibleContext

,

BOTTOM_ALIGNMENT

,

CENTER_ALIGNMENT

,

LEFT_ALIGNMENT

,

RIGHT_ALIGNMENT

,

TOP_ALIGNMENT

---

#### Fields declared in class java.awt. Component

Fields declared in interface java.awt.image.

ImageObserver

ABORT

,

ALLBITS

,

ERROR

,

FRAMEBITS

,

HEIGHT

,

PROPERTIES

,

SOMEBITS

,

WIDTH

---

#### Fields declared in interface java.awt.image. ImageObserver

Constructor Summary

Constructors

Constructor

Description

JTree

()

Returns a

JTree

with a sample model.

JTree

​(

Object

[] value)

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.

JTree

​(

Hashtable

<?,​?> value)

Returns a

JTree

created from a

Hashtable

which does not display with root.

JTree

​(

Vector

<?> value)

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed.

JTree

​(

TreeModel

newModel)

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

JTree

​(

TreeNode

root)

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.

JTree

​(

TreeNode

root,
boolean asksAllowsChildren)

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

---

#### Constructor Summary

Returns a

JTree

with a sample model.

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.

Returns a

JTree

created from a

Hashtable

which does not display with root.

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed.

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addSelectionInterval

​(int index0,
int index1)

Adds the specified rows (inclusive) to the selection.

void

addSelectionPath

​(

TreePath

path)

Adds the node identified by the specified

TreePath

to the current selection.

void

addSelectionPaths

​(

TreePath

[] paths)

Adds each path in the array of paths to the current selection.

void

addSelectionRow

​(int row)

Adds the path at the specified row to the current selection.

void

addSelectionRows

​(int[] rows)

Adds the paths at each of the specified rows to the current selection.

void

addTreeExpansionListener

​(

TreeExpansionListener

tel)

Adds a listener for

TreeExpansion

events.

void

addTreeSelectionListener

​(

TreeSelectionListener

tsl)

Adds a listener for

TreeSelection

events.

void

addTreeWillExpandListener

​(

TreeWillExpandListener

tel)

Adds a listener for

TreeWillExpand

events.

void

cancelEditing

()

Cancels the current editing session.

void

clearSelection

()

Clears the selection.

protected void

clearToggledPaths

()

Clears the cache of toggled tree paths.

void

collapsePath

​(

TreePath

path)

Ensures that the node identified by the specified path is
collapsed and viewable.

void

collapseRow

​(int row)

Ensures that the node in the specified row is collapsed.

String

convertValueToText

​(

Object

value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Called by the renderers to convert the specified value to
text.

protected static

TreeModel

createTreeModel

​(

Object

value)

Returns a

TreeModel

wrapping the specified object.

protected

TreeModelListener

createTreeModelListener

()

Creates and returns an instance of

TreeModelHandler

.

void

expandPath

​(

TreePath

path)

Ensures that the node identified by the specified path is
expanded and viewable.

void

expandRow

​(int row)

Ensures that the node in the specified row is expanded and
viewable.

void

fireTreeCollapsed

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeExpanded

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeWillCollapse

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

void

fireTreeWillExpand

​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireValueChanged

​(

TreeSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTree.

TreePath

getAnchorSelectionPath

()

Returns the path identified as the anchor.

TreeCellEditor

getCellEditor

()

Returns the editor used to edit entries in the tree.

TreeCellRenderer

getCellRenderer

()

Returns the current

TreeCellRenderer

that is rendering each cell.

TreePath

getClosestPathForLocation

​(int x,
int y)

Returns the path to the node that is closest to x,y.

int

getClosestRowForLocation

​(int x,
int y)

Returns the row to the node that is closest to x,y.

protected static

TreeModel

getDefaultTreeModel

()

Creates and returns a sample

TreeModel

.

protected

Enumeration

<

TreePath

>

getDescendantToggledPaths

​(

TreePath

parent)

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

boolean

getDragEnabled

()

Returns whether or not automatic drag handling is enabled.

JTree.DropLocation

getDropLocation

()

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

DropMode

getDropMode

()

Returns the drop mode for this component.

TreePath

getEditingPath

()

Returns the path to the element that is currently being edited.

Enumeration

<

TreePath

>

getExpandedDescendants

​(

TreePath

parent)

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded.

boolean

getExpandsSelectedPaths

()

Returns the

expandsSelectedPaths

property.

boolean

getInvokesStopCellEditing

()

Returns the indicator that tells what happens when editing is
interrupted.

Object

getLastSelectedPathComponent

()

Returns the last path component of the selected path.

TreePath

getLeadSelectionPath

()

Returns the path identified as the lead.

int

getLeadSelectionRow

()

Returns the row index corresponding to the lead path.

int

getMaxSelectionRow

()

Returns the largest selected row.

int

getMinSelectionRow

()

Returns the smallest selected row.

TreeModel

getModel

()

Returns the

TreeModel

that is providing the data.

TreePath

getNextMatch

​(

String

prefix,
int startingRow,

Position.Bias

bias)

Returns the TreePath to the next tree element that
begins with a prefix.

protected

TreePath

[]

getPathBetweenRows

​(int index0,
int index1)

Returns the paths (inclusive) between the specified rows.

Rectangle

getPathBounds

​(

TreePath

path)

Returns the

Rectangle

that the specified node will be drawn
into.

TreePath

getPathForLocation

​(int x,
int y)

Returns the path for the node at the specified location.

TreePath

getPathForRow

​(int row)

Returns the path for the specified row.

Dimension

getPreferredScrollableViewportSize

()

Returns the preferred display size of a

JTree

.

Rectangle

getRowBounds

​(int row)

Returns the

Rectangle

that the node at the specified row is
drawn in.

int

getRowCount

()

Returns the number of viewable nodes.

int

getRowForLocation

​(int x,
int y)

Returns the row for the specified location.

int

getRowForPath

​(

TreePath

path)

Returns the row that displays the node identified by the specified
path.

int

getRowHeight

()

Returns the height of each row.

int

getScrollableBlockIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

boolean

getScrollableTracksViewportHeight

()

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height.

boolean

getScrollableTracksViewportWidth

()

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width.

int

getScrollableUnitIncrement

​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount to increment when scrolling.

boolean

getScrollsOnExpand

()

Returns the value of the

scrollsOnExpand

property.

int

getSelectionCount

()

Returns the number of nodes selected.

TreeSelectionModel

getSelectionModel

()

Returns the model for selections.

TreePath

getSelectionPath

()

Returns the path to the first selected node.

TreePath

[]

getSelectionPaths

()

Returns the paths of all selected values.

int[]

getSelectionRows

()

Returns all of the currently selected rows.

boolean

getShowsRootHandles

()

Returns the value of the

showsRootHandles

property.

int

getToggleClickCount

()

Returns the number of mouse clicks needed to expand or close a node.

String

getToolTipText

​(

MouseEvent

event)

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

TreeExpansionListener

[]

getTreeExpansionListeners

()

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

TreeSelectionListener

[]

getTreeSelectionListeners

()

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

TreeWillExpandListener

[]

getTreeWillExpandListeners

()

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

TreeUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

int

getVisibleRowCount

()

Returns the number of rows that are displayed in the display area.

boolean

hasBeenExpanded

​(

TreePath

path)

Returns true if the node identified by the path has ever been
expanded.

boolean

isCollapsed

​(int row)

Returns true if the node at the specified display row is collapsed.

boolean

isCollapsed

​(

TreePath

path)

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

boolean

isEditable

()

Returns true if the tree is editable.

boolean

isEditing

()

Returns true if the tree is being edited.

boolean

isExpanded

​(int row)

Returns true if the node at the specified display row is currently
expanded.

boolean

isExpanded

​(

TreePath

path)

Returns true if the node identified by the path is currently expanded,

boolean

isFixedRowHeight

()

Returns true if the height of each display row is a fixed size.

boolean

isLargeModel

()

Returns true if the tree is configured for a large model.

boolean

isPathEditable

​(

TreePath

path)

Returns

isEditable

.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the item identified by the path is currently selected.

boolean

isRootVisible

()

Returns true if the root node of the tree is displayed.

boolean

isRowSelected

​(int row)

Returns true if the node identified by row is selected.

boolean

isSelectionEmpty

()

Returns true if the selection is currently empty.

boolean

isVisible

​(

TreePath

path)

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.

void

makeVisible

​(

TreePath

path)

Ensures that the node identified by path is currently viewable.

protected

String

paramString

()

Returns a string representation of this

JTree

.

protected boolean

removeDescendantSelectedPaths

​(

TreePath

path,
boolean includePath)

Removes any paths in the selection that are descendants of

path

.

protected void

removeDescendantToggledPaths

​(

Enumeration

<

TreePath

> toRemove)

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

void

removeSelectionInterval

​(int index0,
int index1)

Removes the specified rows (inclusive) from the selection.

void

removeSelectionPath

​(

TreePath

path)

Removes the node identified by the specified path from the current
selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

Removes the nodes identified by the specified paths from the
current selection.

void

removeSelectionRow

​(int row)

Removes the row at the index

row

from the current
selection.

void

removeSelectionRows

​(int[] rows)

Removes the rows that are selected at each of the specified
rows.

void

removeTreeExpansionListener

​(

TreeExpansionListener

tel)

Removes a listener for

TreeExpansion

events.

void

removeTreeSelectionListener

​(

TreeSelectionListener

tsl)

Removes a

TreeSelection

listener.

void

removeTreeWillExpandListener

​(

TreeWillExpandListener

tel)

Removes a listener for

TreeWillExpand

events.

void

scrollPathToVisible

​(

TreePath

path)

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed.

void

scrollRowToVisible

​(int row)

Scrolls the item identified by row until it is displayed.

void

setAnchorSelectionPath

​(

TreePath

newPath)

Sets the path identified as the anchor.

void

setCellEditor

​(

TreeCellEditor

cellEditor)

Sets the cell editor.

void

setCellRenderer

​(

TreeCellRenderer

x)

Sets the

TreeCellRenderer

that will be used to
draw each cell.

void

setDragEnabled

​(boolean b)

Turns on or off automatic drag handling.

void

setDropMode

​(

DropMode

dropMode)

Sets the drop mode for this component.

void

setEditable

​(boolean flag)

Determines whether the tree is editable.

protected void

setExpandedState

​(

TreePath

path,
boolean state)

Sets the expanded state of this

JTree

.

void

setExpandsSelectedPaths

​(boolean newValue)

Configures the

expandsSelectedPaths

property.

void

setInvokesStopCellEditing

​(boolean newValue)

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means.

void

setLargeModel

​(boolean newValue)

Specifies whether the UI should use a large model.

void

setLeadSelectionPath

​(

TreePath

newPath)

Sets the path identifies as the lead.

void

setModel

​(

TreeModel

newModel)

Sets the

TreeModel

that will provide the data.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell, in pixels.

void

setScrollsOnExpand

​(boolean newValue)

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.

void

setSelectionInterval

​(int index0,
int index1)

Selects the rows in the specified interval (inclusive).

void

setSelectionModel

​(

TreeSelectionModel

selectionModel)

Sets the tree's selection model.

void

setSelectionPath

​(

TreePath

path)

Selects the node identified by the specified path.

void

setSelectionPaths

​(

TreePath

[] paths)

Selects the nodes identified by the specified array of paths.

void

setSelectionRow

​(int row)

Selects the node at the specified row in the display.

void

setSelectionRows

​(int[] rows)

Selects the nodes corresponding to each of the specified rows
in the display.

void

setShowsRootHandles

​(boolean newValue)

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.

void

setToggleClickCount

​(int clickCount)

Sets the number of mouse clicks before a node will expand or close.

void

setUI

​(

TreeUI

ui)

Sets the L&F object that renders this component.

void

setVisibleRowCount

​(int newCount)

Sets the number of rows that are to be displayed.

void

startEditingAtPath

​(

TreePath

path)

Selects the node identified by the specified path and initiates
editing.

boolean

stopEditing

()

Ends the current editing session.

void

treeDidChange

()

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree).

void

updateUI

()

Notification from the

UIManager

that the L&F has changed.

- Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

- Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

- Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

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

wait

,

wait

,

wait

---

#### Method Summary

Adds the specified rows (inclusive) to the selection.

Adds the node identified by the specified

TreePath

to the current selection.

Adds each path in the array of paths to the current selection.

Adds the path at the specified row to the current selection.

Adds the paths at each of the specified rows to the current selection.

Adds a listener for

TreeExpansion

events.

Adds a listener for

TreeSelection

events.

Adds a listener for

TreeWillExpand

events.

Cancels the current editing session.

Clears the selection.

Clears the cache of toggled tree paths.

Ensures that the node identified by the specified path is
collapsed and viewable.

Ensures that the node in the specified row is collapsed.

Called by the renderers to convert the specified value to
text.

Returns a

TreeModel

wrapping the specified object.

Creates and returns an instance of

TreeModelHandler

.

Ensures that the node identified by the specified path is
expanded and viewable.

Ensures that the node in the specified row is expanded and
viewable.

Notifies all listeners that have registered interest for
notification on this event type.

Gets the AccessibleContext associated with this JTree.

Returns the path identified as the anchor.

Returns the editor used to edit entries in the tree.

Returns the current

TreeCellRenderer

that is rendering each cell.

Returns the path to the node that is closest to x,y.

Returns the row to the node that is closest to x,y.

Creates and returns a sample

TreeModel

.

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

Returns whether or not automatic drag handling is enabled.

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

Returns the drop mode for this component.

Returns the path to the element that is currently being edited.

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded.

Returns the

expandsSelectedPaths

property.

Returns the indicator that tells what happens when editing is
interrupted.

Returns the last path component of the selected path.

Returns the path identified as the lead.

Returns the row index corresponding to the lead path.

Returns the largest selected row.

Returns the smallest selected row.

Returns the

TreeModel

that is providing the data.

Returns the TreePath to the next tree element that
begins with a prefix.

Returns the paths (inclusive) between the specified rows.

Returns the

Rectangle

that the specified node will be drawn
into.

Returns the path for the node at the specified location.

Returns the path for the specified row.

Returns the preferred display size of a

JTree

.

Returns the

Rectangle

that the node at the specified row is
drawn in.

Returns the number of viewable nodes.

Returns the row for the specified location.

Returns the row that displays the node identified by the specified
path.

Returns the height of each row.

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height.

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width.

Returns the amount to increment when scrolling.

Returns the value of the

scrollsOnExpand

property.

Returns the number of nodes selected.

Returns the model for selections.

Returns the path to the first selected node.

Returns the paths of all selected values.

Returns all of the currently selected rows.

Returns the value of the

showsRootHandles

property.

Returns the number of mouse clicks needed to expand or close a node.

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

Returns the L&F object that renders this component.

Returns the name of the L&F class that renders this component.

Returns the number of rows that are displayed in the display area.

Returns true if the node identified by the path has ever been
expanded.

Returns true if the node at the specified display row is collapsed.

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

Returns true if the tree is editable.

Returns true if the tree is being edited.

Returns true if the node at the specified display row is currently
expanded.

Returns true if the node identified by the path is currently expanded,

Returns true if the height of each display row is a fixed size.

Returns true if the tree is configured for a large model.

Returns

isEditable

.

Returns true if the item identified by the path is currently selected.

Returns true if the root node of the tree is displayed.

Returns true if the node identified by row is selected.

Returns true if the selection is currently empty.

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.

Ensures that the node identified by path is currently viewable.

Returns a string representation of this

JTree

.

Removes any paths in the selection that are descendants of

path

.

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

Removes the specified rows (inclusive) from the selection.

Removes the node identified by the specified path from the current
selection.

Removes the nodes identified by the specified paths from the
current selection.

Removes the row at the index

row

from the current
selection.

Removes the rows that are selected at each of the specified
rows.

Removes a listener for

TreeExpansion

events.

Removes a

TreeSelection

listener.

Removes a listener for

TreeWillExpand

events.

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed.

Scrolls the item identified by row until it is displayed.

Sets the path identified as the anchor.

Sets the cell editor.

Sets the

TreeCellRenderer

that will be used to
draw each cell.

Turns on or off automatic drag handling.

Sets the drop mode for this component.

Determines whether the tree is editable.

Sets the expanded state of this

JTree

.

Configures the

expandsSelectedPaths

property.

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means.

Specifies whether the UI should use a large model.

Sets the path identifies as the lead.

Sets the

TreeModel

that will provide the data.

Determines whether or not the root node from
the

TreeModel

is visible.

Sets the height of each cell, in pixels.

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.

Selects the rows in the specified interval (inclusive).

Sets the tree's selection model.

Selects the node identified by the specified path.

Selects the nodes identified by the specified array of paths.

Selects the node at the specified row in the display.

Selects the nodes corresponding to each of the specified rows
in the display.

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.

Sets the number of mouse clicks before a node will expand or close.

Sets the L&F object that renders this component.

Sets the number of rows that are to be displayed.

Selects the node identified by the specified path and initiates
editing.

Ends the current editing session.

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree).

Notification from the

UIManager

that the L&F has changed.

Methods declared in class javax.swing.

JComponent

addAncestorListener

,

addNotify

,

addVetoableChangeListener

,

computeVisibleRect

,

contains

,

createToolTip

,

disable

,

enable

,

firePropertyChange

,

firePropertyChange

,

fireVetoableChange

,

getActionForKeyStroke

,

getActionMap

,

getAlignmentX

,

getAlignmentY

,

getAncestorListeners

,

getAutoscrolls

,

getBaseline

,

getBaselineResizeBehavior

,

getBorder

,

getBounds

,

getClientProperty

,

getComponentGraphics

,

getComponentPopupMenu

,

getConditionForKeyStroke

,

getDebugGraphicsOptions

,

getDefaultLocale

,

getFontMetrics

,

getGraphics

,

getHeight

,

getInheritsPopupMenu

,

getInputMap

,

getInputMap

,

getInputVerifier

,

getInsets

,

getInsets

,

getListeners

,

getLocation

,

getMaximumSize

,

getMinimumSize

,

getNextFocusableComponent

,

getPopupLocation

,

getPreferredSize

,

getRegisteredKeyStrokes

,

getRootPane

,

getSize

,

getToolTipLocation

,

getToolTipText

,

getTopLevelAncestor

,

getTransferHandler

,

getVerifyInputWhenFocusTarget

,

getVetoableChangeListeners

,

getVisibleRect

,

getWidth

,

getX

,

getY

,

grabFocus

,

isDoubleBuffered

,

isLightweightComponent

,

isManagingFocus

,

isOpaque

,

isOptimizedDrawingEnabled

,

isPaintingForPrint

,

isPaintingOrigin

,

isPaintingTile

,

isRequestFocusEnabled

,

isValidateRoot

,

paint

,

paintBorder

,

paintChildren

,

paintComponent

,

paintImmediately

,

paintImmediately

,

print

,

printAll

,

printBorder

,

printChildren

,

printComponent

,

processComponentKeyEvent

,

processKeyBinding

,

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

,

putClientProperty

,

registerKeyboardAction

,

registerKeyboardAction

,

removeAncestorListener

,

removeNotify

,

removeVetoableChangeListener

,

repaint

,

repaint

,

requestDefaultFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

resetKeyboardActions

,

reshape

,

revalidate

,

scrollRectToVisible

,

setActionMap

,

setAlignmentX

,

setAlignmentY

,

setAutoscrolls

,

setBackground

,

setBorder

,

setComponentPopupMenu

,

setDebugGraphicsOptions

,

setDefaultLocale

,

setDoubleBuffered

,

setEnabled

,

setFocusTraversalKeys

,

setFont

,

setForeground

,

setInheritsPopupMenu

,

setInputMap

,

setInputVerifier

,

setMaximumSize

,

setMinimumSize

,

setNextFocusableComponent

,

setOpaque

,

setPreferredSize

,

setRequestFocusEnabled

,

setToolTipText

,

setTransferHandler

,

setUI

,

setVerifyInputWhenFocusTarget

,

setVisible

,

unregisterKeyboardAction

,

update

---

#### Methods declared in class javax.swing. JComponent

Methods declared in class java.awt.

Container

add

,

add

,

add

,

add

,

add

,

addContainerListener

,

addImpl

,

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

,

countComponents

,

deliverEvent

,

doLayout

,

findComponentAt

,

findComponentAt

,

getComponent

,

getComponentAt

,

getComponentAt

,

getComponentCount

,

getComponents

,

getComponentZOrder

,

getContainerListeners

,

getFocusTraversalKeys

,

getFocusTraversalPolicy

,

getLayout

,

getMousePosition

,

insets

,

invalidate

,

isAncestorOf

,

isFocusCycleRoot

,

isFocusCycleRoot

,

isFocusTraversalPolicyProvider

,

isFocusTraversalPolicySet

,

layout

,

list

,

list

,

locate

,

minimumSize

,

paintComponents

,

preferredSize

,

printComponents

,

processContainerEvent

,

processEvent

,

remove

,

remove

,

removeAll

,

removeContainerListener

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setLayout

,

transferFocusDownCycle

,

validate

,

validateTree

---

#### Methods declared in class java.awt. Container

Methods declared in class java.awt.

Component

action

,

add

,

addComponentListener

,

addFocusListener

,

addHierarchyBoundsListener

,

addHierarchyListener

,

addInputMethodListener

,

addKeyListener

,

addMouseListener

,

addMouseMotionListener

,

addMouseWheelListener

,

bounds

,

checkImage

,

checkImage

,

coalesceEvents

,

contains

,

createImage

,

createImage

,

createVolatileImage

,

createVolatileImage

,

disableEvents

,

dispatchEvent

,

enable

,

enableEvents

,

enableInputMethods

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

firePropertyChange

,

getBackground

,

getBounds

,

getColorModel

,

getComponentListeners

,

getComponentOrientation

,

getCursor

,

getDropTarget

,

getFocusCycleRootAncestor

,

getFocusListeners

,

getFocusTraversalKeysEnabled

,

getFont

,

getForeground

,

getGraphicsConfiguration

,

getHierarchyBoundsListeners

,

getHierarchyListeners

,

getIgnoreRepaint

,

getInputContext

,

getInputMethodListeners

,

getInputMethodRequests

,

getKeyListeners

,

getLocale

,

getLocation

,

getLocationOnScreen

,

getMouseListeners

,

getMouseMotionListeners

,

getMousePosition

,

getMouseWheelListeners

,

getName

,

getParent

,

getPropertyChangeListeners

,

getPropertyChangeListeners

,

getSize

,

getToolkit

,

getTreeLock

,

gotFocus

,

handleEvent

,

hasFocus

,

hide

,

imageUpdate

,

inside

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isEnabled

,

isFocusable

,

isFocusOwner

,

isFocusTraversable

,

isFontSet

,

isForegroundSet

,

isLightweight

,

isMaximumSizeSet

,

isMinimumSizeSet

,

isPreferredSizeSet

,

isShowing

,

isValid

,

isVisible

,

keyDown

,

keyUp

,

list

,

list

,

list

,

location

,

lostFocus

,

mouseDown

,

mouseDrag

,

mouseEnter

,

mouseExit

,

mouseMove

,

mouseUp

,

move

,

nextFocus

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

processComponentEvent

,

processFocusEvent

,

processHierarchyBoundsEvent

,

processHierarchyEvent

,

processInputMethodEvent

,

processMouseWheelEvent

,

remove

,

removeComponentListener

,

removeFocusListener

,

removeHierarchyBoundsListener

,

removeHierarchyListener

,

removeInputMethodListener

,

removeKeyListener

,

removeMouseListener

,

removeMouseMotionListener

,

removeMouseWheelListener

,

removePropertyChangeListener

,

removePropertyChangeListener

,

repaint

,

repaint

,

repaint

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

resize

,

resize

,

setBounds

,

setBounds

,

setComponentOrientation

,

setCursor

,

setDropTarget

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMixingCutoutShape

,

setName

,

setSize

,

setSize

,

show

,

show

,

size

,

toString

,

transferFocus

,

transferFocusBackward

,

transferFocusUpCycle

---

#### Methods declared in class java.awt. Component

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- treeModel

```java
protected transient
TreeModel
treeModel
```

The model that defines the tree displayed by this object.

- selectionModel

```java
protected transient
TreeSelectionModel
selectionModel
```

Models the set of selected nodes in this tree.

- rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

- cellRenderer

```java
protected transient
TreeCellRenderer
cellRenderer
```

The cell used to draw nodes. If

null

, the UI uses a default

cellRenderer

.

- rowHeight

```java
protected int rowHeight
```

Height to use for each display row. If this is <= 0 the renderer
determines the height for each row.

- showsRootHandles

```java
protected boolean showsRootHandles
```

True if handles are displayed at the topmost level of the tree.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

**See Also:** rootVisible

- selectionRedirector

```java
protected transient
JTree.TreeSelectionRedirector
selectionRedirector
```

Creates a new event and passed it off the

selectionListeners

.

- cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the entries. Default is

null

(tree is not editable).

- editable

```java
protected boolean editable
```

Is the tree editable? Default is false.

- largeModel

```java
protected boolean largeModel
```

Is this tree a large model? This is a code-optimization setting.
A large model can be used when the cell height is the same for all
nodes. The UI will then cache very little information and instead
continually message the model. Without a large model the UI caches
most of the information, resulting in fewer method calls to the model.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

- visibleRowCount

```java
protected int visibleRowCount
```

Number of rows to make visible at one time. This value is used for
the

Scrollable

interface. It determines the preferred
size of the display area.

- invokesStopCellEditing

```java
protected boolean invokesStopCellEditing
```

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved. If false,

cancelCellEditing

is invoked, and changes
are discarded. Default is false.

- scrollsOnExpand

```java
protected boolean scrollsOnExpand
```

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

- toggleClickCount

```java
protected int toggleClickCount
```

Number of mouse clicks before a node is expanded.

- treeModelListener

```java
protected transient
TreeModelListener
treeModelListener
```

Updates the

expandedState

.

- CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Bound property name for

cellRenderer

.

**See Also:** Constant Field Values

- TREE_MODEL_PROPERTY

```java
public static final
String
TREE_MODEL_PROPERTY
```

Bound property name for

treeModel

.

**See Also:** Constant Field Values

- ROOT_VISIBLE_PROPERTY

```java
public static final
String
ROOT_VISIBLE_PROPERTY
```

Bound property name for

rootVisible

.

**See Also:** Constant Field Values

- SHOWS_ROOT_HANDLES_PROPERTY

```java
public static final
String
SHOWS_ROOT_HANDLES_PROPERTY
```

Bound property name for

showsRootHandles

.

**See Also:** Constant Field Values

- ROW_HEIGHT_PROPERTY

```java
public static final
String
ROW_HEIGHT_PROPERTY
```

Bound property name for

rowHeight

.

**See Also:** Constant Field Values

- CELL_EDITOR_PROPERTY

```java
public static final
String
CELL_EDITOR_PROPERTY
```

Bound property name for

cellEditor

.

**See Also:** Constant Field Values

- EDITABLE_PROPERTY

```java
public static final
String
EDITABLE_PROPERTY
```

Bound property name for

editable

.

**See Also:** Constant Field Values

- LARGE_MODEL_PROPERTY

```java
public static final
String
LARGE_MODEL_PROPERTY
```

Bound property name for

largeModel

.

**See Also:** Constant Field Values

- SELECTION_MODEL_PROPERTY

```java
public static final
String
SELECTION_MODEL_PROPERTY
```

Bound property name for selectionModel.

**See Also:** Constant Field Values

- VISIBLE_ROW_COUNT_PROPERTY

```java
public static final
String
VISIBLE_ROW_COUNT_PROPERTY
```

Bound property name for

visibleRowCount

.

**See Also:** Constant Field Values

- INVOKES_STOP_CELL_EDITING_PROPERTY

```java
public static final
String
INVOKES_STOP_CELL_EDITING_PROPERTY
```

Bound property name for

messagesStopCellEditing

.

**See Also:** Constant Field Values

- SCROLLS_ON_EXPAND_PROPERTY

```java
public static final
String
SCROLLS_ON_EXPAND_PROPERTY
```

Bound property name for

scrollsOnExpand

.

**See Also:** Constant Field Values

- TOGGLE_CLICK_COUNT_PROPERTY

```java
public static final
String
TOGGLE_CLICK_COUNT_PROPERTY
```

Bound property name for

toggleClickCount

.

**See Also:** Constant Field Values

- LEAD_SELECTION_PATH_PROPERTY

```java
public static final
String
LEAD_SELECTION_PATH_PROPERTY
```

Bound property name for

leadSelectionPath

.

**Since:** 1.3
**See Also:** Constant Field Values

- ANCHOR_SELECTION_PATH_PROPERTY

```java
public static final
String
ANCHOR_SELECTION_PATH_PROPERTY
```

Bound property name for anchor selection path.

**Since:** 1.3
**See Also:** Constant Field Values

- EXPANDS_SELECTED_PATHS_PROPERTY

```java
public static final
String
EXPANDS_SELECTED_PATHS_PROPERTY
```

Bound property name for expands selected paths property

**Since:** 1.3
**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JTree

```java
public JTree()
```

Returns a

JTree

with a sample model.
The default model used by the tree defines a leaf node as any node
without children.

**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Object
[] value)
```

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.
By default, the tree defines a leaf node as any node without
children.

**Parameters:** value

- an array of

Object

s
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Vector
<?> value)
```

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed. By default, the
tree defines a leaf node as any node without children.

**Parameters:** value

- a

Vector
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Hashtable
<?,​?> value)
```

Returns a

JTree

created from a

Hashtable

which does not display with root.
Each value-half of the key/value pairs in the

HashTable

becomes a child of the new root node. By default, the tree defines
a leaf node as any node without children.

**Parameters:** value

- a

Hashtable
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
TreeNode
root)
```

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.
By default, the tree defines a leaf node as any node without children.

**Parameters:** root

- a

TreeNode

object
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
TreeNode
root,
boolean asksAllowsChildren)
```

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

**Parameters:** root

- a

TreeNode

object
**Parameters:** asksAllowsChildren

- if false, any node without children is a
leaf node; if true, only nodes that do not allow
children are leaf nodes
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
@ConstructorProperties
("model")
public JTree​(
TreeModel
newModel)
```

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

**Parameters:** newModel

- the

TreeModel

to use as the data model

============ METHOD DETAIL ==========

- Method Detail

- getDefaultTreeModel

```java
protected static
TreeModel
getDefaultTreeModel()
```

Creates and returns a sample

TreeModel

.
Used primarily for beanbuilders to show something interesting.

**Returns:** the default

TreeModel

- createTreeModel

```java
protected static
TreeModel
createTreeModel​(
Object
value)
```

Returns a

TreeModel

wrapping the specified object.
If the object is:

- an array of

Object

s,

a

Hashtable

, or

a

Vector

then a new root node is created with each of the incoming
objects as children. Otherwise, a new root is created with
a value of

"root"

.

**Parameters:** value

- the

Object

used as the foundation for
the

TreeModel
**Returns:** a

TreeModel

wrapping the specified object

- getUI

```java
public
TreeUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TreeUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
TreeUI
ui)
```

Sets the L&F object that renders this component.

This is a bound property.

**Parameters:** ui

- the

TreeUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TreeUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getCellRenderer

```java
public
TreeCellRenderer
getCellRenderer()
```

Returns the current

TreeCellRenderer

that is rendering each cell.

**Returns:** the

TreeCellRenderer

that is rendering each cell

- setCellRenderer

```java
@BeanProperty
(
description
="The TreeCellRenderer that will be used to draw each cell.")
public void setCellRenderer​(
TreeCellRenderer
x)
```

Sets the

TreeCellRenderer

that will be used to
draw each cell.

This is a bound property.

**Parameters:** x

- the

TreeCellRenderer

that is to render each cell

- setEditable

```java
@BeanProperty
(
description
="Whether the tree is editable.")
public void setEditable​(boolean flag)
```

Determines whether the tree is editable. Fires a property
change event if the new setting is different from the existing
setting.

This is a bound property.

**Parameters:** flag

- a boolean value, true if the tree is editable

- isEditable

```java
public boolean isEditable()
```

Returns true if the tree is editable.

**Returns:** true if the tree is editable

- setCellEditor

```java
@BeanProperty
(
description
="The cell editor. A null value implies the tree cannot be edited.")
public void setCellEditor​(
TreeCellEditor
cellEditor)
```

Sets the cell editor. A

null

value implies that the
tree cannot be edited. If this represents a change in the

cellEditor

, the

propertyChange

method is invoked on all listeners.

This is a bound property.

**Parameters:** cellEditor

- the

TreeCellEditor

to use

- getCellEditor

```java
public
TreeCellEditor
getCellEditor()
```

Returns the editor used to edit entries in the tree.

**Returns:** the

TreeCellEditor

in use,
or

null

if the tree cannot be edited

- getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

- setModel

```java
@BeanProperty
(
description
="The TreeModel that will provide the data.")
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

This is a bound property.

**Parameters:** newModel

- the

TreeModel

that is to provide the data

- isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

- setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

This is a bound property.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

- setShowsRootHandles

```java
@BeanProperty
(
description
="Whether the node handles are to be displayed.")
public void setShowsRootHandles​(boolean newValue)
```

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.
The default value of this property depends on the constructor
used to create the

JTree

.
Some look and feels might not support handles;
they will ignore this property.

This is a bound property.

**Parameters:** newValue

-

true

if root handles should be displayed;
otherwise,

false
**See Also:** showsRootHandles

,

getShowsRootHandles()

- getShowsRootHandles

```java
public boolean getShowsRootHandles()
```

Returns the value of the

showsRootHandles

property.

**Returns:** the value of the

showsRootHandles

property
**See Also:** showsRootHandles

- setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell, in pixels. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

This is a bound property.

**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

- isFixedRowHeight

```java
@BeanProperty
(
bound
=false)
public boolean isFixedRowHeight()
```

Returns true if the height of each display row is a fixed size.

**Returns:** true if the height of each row is a fixed size

- setLargeModel

```java
@BeanProperty
(
description
="Whether the UI should use a large model.")
public void setLargeModel​(boolean newValue)
```

Specifies whether the UI should use a large model.
(Not all UIs will implement this.) Fires a property change
for the LARGE_MODEL_PROPERTY.

This is a bound property.

**Parameters:** newValue

- true to suggest a large model to the UI
**See Also:** largeModel

- isLargeModel

```java
public boolean isLargeModel()
```

Returns true if the tree is configured for a large model.

**Returns:** true if a large model is suggested
**See Also:** largeModel

- setInvokesStopCellEditing

```java
@BeanProperty
(
description
="Determines what happens when editing is interrupted, selecting another node in the tree, a change in the tree\'s data, or some other means.")
public void setInvokesStopCellEditing​(boolean newValue)
```

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means. Setting this property to

true

causes the
changes to be automatically saved when editing is interrupted.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

**Parameters:** newValue

- true means that

stopCellEditing

is invoked
when editing is interrupted, and data is saved; false means that

cancelCellEditing

is invoked, and changes are lost

- getInvokesStopCellEditing

```java
public boolean getInvokesStopCellEditing()
```

Returns the indicator that tells what happens when editing is
interrupted.

**Returns:** the indicator that tells what happens when editing is
interrupted
**See Also:** setInvokesStopCellEditing(boolean)

- setScrollsOnExpand

```java
@BeanProperty
(
description
="Indicates if a node descendant should be scrolled when expanded.")
public void setScrollsOnExpand​(boolean newValue)
```

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.
If this property is

true

(the default),
when a node expands
the tree can use scrolling to make
the maximum possible number of the node's descendants visible.
In some look and feels, trees might not need to scroll when expanded;
those look and feels will ignore this property.

This is a bound property.

**Parameters:** newValue

-

false

to disable scrolling on expansion;

true

to enable it
**See Also:** getScrollsOnExpand()

- getScrollsOnExpand

```java
public boolean getScrollsOnExpand()
```

Returns the value of the

scrollsOnExpand

property.

**Returns:** the value of the

scrollsOnExpand

property

- setToggleClickCount

```java
@BeanProperty
(
description
="Number of clicks before a node will expand/collapse.")
public void setToggleClickCount​(int clickCount)
```

Sets the number of mouse clicks before a node will expand or close.
The default is two.

This is a bound property.

**Parameters:** clickCount

- the number of mouse clicks to get a node expanded or closed
**Since:** 1.3

- getToggleClickCount

```java
public int getToggleClickCount()
```

Returns the number of mouse clicks needed to expand or close a node.

**Returns:** number of mouse clicks before node is expanded
**Since:** 1.3

- setExpandsSelectedPaths

```java
@BeanProperty
(
description
="Indicates whether changes to the selection should make the parent of the path visible.")
public void setExpandsSelectedPaths​(boolean newValue)
```

Configures the

expandsSelectedPaths

property. If
true, any time the selection is changed, either via the

TreeSelectionModel

, or the cover methods provided by

JTree

, the

TreePath

s parents will be
expanded to make them visible (visible meaning the parent path is
expanded, not necessarily in the visible rectangle of the

JTree

). If false, when the selection
changes the nodes parent is not made visible (all its parents expanded).
This is useful if you wish to have your selection model maintain paths
that are not always visible (all parents expanded).

This is a bound property.

**Parameters:** newValue

- the new value for

expandsSelectedPaths
**Since:** 1.3

- getExpandsSelectedPaths

```java
public boolean getExpandsSelectedPaths()
```

Returns the

expandsSelectedPaths

property.

**Returns:** true if selection changes result in the parent path being
expanded
**Since:** 1.3
**See Also:** setExpandsSelectedPaths(boolean)

- setDragEnabled

```java
@BeanProperty
(
bound
=false,

description
="determines whether automatic drag handling is enabled")
public void setDragEnabled​(boolean b)
```

Turns on or off automatic drag handling. In order to enable automatic
drag handling, this property should be set to

true

, and the
tree's

TransferHandler

needs to be

non-null

.
The default value of the

dragEnabled

property is

false

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

**Parameters:** b

- whether or not to enable automatic drag handling
**Throws:** HeadlessException

- if

b

is

true

and

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

,

getDragEnabled()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

- getDragEnabled

```java
public boolean getDragEnabled()
```

Returns whether or not automatic drag handling is enabled.

**Returns:** the value of the

dragEnabled

property
**Since:** 1.4
**See Also:** setDragEnabled(boolean)

- setDropMode

```java
public final void setDropMode​(
DropMode
dropMode)
```

Sets the drop mode for this component. For backward compatibility,
the default for this property is

DropMode.USE_SELECTION

.
Usage of one of the other modes is recommended, however, for an
improved user experience.

DropMode.ON

, for instance,
offers similar behavior of showing items as selected, but does so without
affecting the actual selection in the tree.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

**Parameters:** dropMode

- the drop mode to use
**Throws:** IllegalArgumentException

- if the drop mode is unsupported
or

null
**Since:** 1.6
**See Also:** getDropMode()

,

getDropLocation()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

- getDropMode

```java
public final
DropMode
getDropMode()
```

Returns the drop mode for this component.

**Returns:** the drop mode for this component
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

- getDropLocation

```java
@BeanProperty
(
bound
=false)
public final
JTree.DropLocation
getDropLocation()
```

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

**Returns:** the drop location
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

,

TransferHandler.canImport(TransferHandler.TransferSupport)

- isPathEditable

```java
public boolean isPathEditable​(
TreePath
path)
```

Returns

isEditable

. This is invoked from the UI before
editing begins to insure that the given path can be edited. This
is provided as an entry point for subclassers to add filtered
editing without having to resort to creating a new editor.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if every parent node and the node itself is editable
**See Also:** isEditable()

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that initiated the

ToolTip

display
**Returns:** a string containing the tooltip or

null

if

event

is null

- convertValueToText

```java
public
String
convertValueToText​(
Object
value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Called by the renderers to convert the specified value to
text. This implementation returns

value.toString

, ignoring
all other arguments. To control the conversion, subclass this
method and use any of the arguments you need.

**Parameters:** value

- the

Object

to convert to text
**Parameters:** selected

- true if the node is selected
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- an integer specifying the node's display row, where 0 is
the first row in the display
**Parameters:** hasFocus

- true if the node has the focus
**Returns:** the

String

representation of the node's value

- getRowCount

```java
@BeanProperty
(
bound
=false)
public int getRowCount()
```

Returns the number of viewable nodes. A node is viewable if all of its
parents are expanded. The root is only included in this count if

isRootVisible()

is

true

. This returns

0

if
the UI has not been set.

**Returns:** the number of viewable nodes

- setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Selects the node identified by the specified path. If any
component of the path is hidden (under a collapsed node), and

getExpandsSelectedPaths

is true it is
exposed (made viewable).

**Parameters:** path

- the

TreePath

specifying the node to select

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

Selects the nodes identified by the specified array of paths.
If any component in any of the paths is hidden (under a collapsed
node), and

getExpandsSelectedPaths

is true
it is exposed (made viewable).

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to select

- setLeadSelectionPath

```java
@BeanProperty
(
description
="Lead selection path")
public void setLeadSelectionPath​(
TreePath
newPath)
```

Sets the path identifies as the lead. The lead may not be selected.
The lead is not maintained by

JTree

,
rather the UI will update it.

This is a bound property.

**Parameters:** newPath

- the new lead path
**Since:** 1.3

- setAnchorSelectionPath

```java
@BeanProperty
(
description
="Anchor selection path")
public void setAnchorSelectionPath​(
TreePath
newPath)
```

Sets the path identified as the anchor.
The anchor is not maintained by

JTree

, rather the UI will
update it.

This is a bound property.

**Parameters:** newPath

- the new anchor path
**Since:** 1.3

- setSelectionRow

```java
public void setSelectionRow​(int row)
```

Selects the node at the specified row in the display.

**Parameters:** row

- the row to select, where 0 is the first row in
the display

- setSelectionRows

```java
public void setSelectionRows​(int[] rows)
```

Selects the nodes corresponding to each of the specified rows
in the display. If a particular element of

rows

is
< 0 or >=

getRowCount

, it will be ignored.
If none of the elements
in

rows

are valid rows, the selection will
be cleared. That is it will be as if

clearSelection

was invoked.

**Parameters:** rows

- an array of ints specifying the rows to select,
where 0 indicates the first row in the display

- addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds the node identified by the specified

TreePath

to the current selection. If any component of the path isn't
viewable, and

getExpandsSelectedPaths

is true it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** path

- the

TreePath

to add

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds each path in the array of paths to the current selection. If
any component of any of the paths isn't viewable and

getExpandsSelectedPaths

is true, it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to add

- addSelectionRow

```java
public void addSelectionRow​(int row)
```

Adds the path at the specified row to the current selection.

**Parameters:** row

- an integer specifying the row of the node to add,
where 0 is the first row in the display

- addSelectionRows

```java
public void addSelectionRows​(int[] rows)
```

Adds the paths at each of the specified rows to the current selection.

**Parameters:** rows

- an array of ints specifying the rows to add,
where 0 indicates the first row in the display

- getLastSelectedPathComponent

```java
@BeanProperty
(
bound
=false)
public
Object
getLastSelectedPathComponent()
```

Returns the last path component of the selected path. This is
a convenience method for

getSelectionModel().getSelectionPath().getLastPathComponent()

.
This is typically only useful if the selection has one path.

**Returns:** the last path component of the selected path, or

null

if nothing is selected
**See Also:** TreePath.getLastPathComponent()

- getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the path identified as the lead.

**Returns:** path identified as the lead

- getAnchorSelectionPath

```java
public
TreePath
getAnchorSelectionPath()
```

Returns the path identified as the anchor.

**Returns:** path identified as the anchor
**Since:** 1.3

- getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the path to the first selected node.

**Returns:** the

TreePath

for the first selected node,
or

null

if nothing is currently selected

- getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the paths of all selected values.

**Returns:** an array of

TreePath

objects indicating the selected
nodes, or

null

if nothing is currently selected

- getSelectionRows

```java
public int[] getSelectionRows()
```

Returns all of the currently selected rows. This method is simply
forwarded to the

TreeSelectionModel

.
If nothing is selected

null

or an empty array will
be returned, based on the

TreeSelectionModel

implementation.

**Returns:** an array of integers that identifies all currently selected rows
where 0 is the first row in the display

- getSelectionCount

```java
@BeanProperty
(
bound
=false)
public int getSelectionCount()
```

Returns the number of nodes selected.

**Returns:** the number of nodes selected

- getMinSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMinSelectionRow()
```

Returns the smallest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the smallest selected row

- getMaxSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMaxSelectionRow()
```

Returns the largest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the largest selected row

- getLeadSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getLeadSelectionRow()
```

Returns the row index corresponding to the lead path.

**Returns:** an integer giving the row index of the lead path,
where 0 is the first row in the display; or -1
if

leadPath

is

null

- isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the item identified by the path is currently selected.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the node is selected

- isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the node identified by row is selected.

**Parameters:** row

- an integer specifying a display row, where 0 is the first
row in the display
**Returns:** true if the node is selected

- getExpandedDescendants

```java
public
Enumeration
<
TreePath
> getExpandedDescendants​(
TreePath
parent)
```

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded. If

parent

is not currently
expanded, this will return

null

.
If you expand/collapse nodes while
iterating over the returned

Enumeration

this may not return all
the expanded paths, or may return paths that are no longer expanded.

**Parameters:** parent

- the path which is to be examined
**Returns:** an

Enumeration

of the descendents of

parent

, or

null

if

parent

is not currently expanded

- hasBeenExpanded

```java
public boolean hasBeenExpanded​(
TreePath
path)
```

Returns true if the node identified by the path has ever been
expanded.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the

path

has ever been expanded

- isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the node identified by the path is currently expanded,

**Parameters:** path

- the

TreePath

specifying the node to check
**Returns:** false if any of the nodes in the node's path are collapsed,
true if all nodes in the path are expanded

- isExpanded

```java
public boolean isExpanded​(int row)
```

Returns true if the node at the specified display row is currently
expanded.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently expanded, otherwise false

- isCollapsed

```java
public boolean isCollapsed​(
TreePath
path)
```

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

**Parameters:** path

- the

TreePath

to check
**Returns:** true if any of the nodes in the node's path are collapsed,
false if all nodes in the path are expanded

- isCollapsed

```java
public boolean isCollapsed​(int row)
```

Returns true if the node at the specified display row is collapsed.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently collapsed, otherwise false

- makeVisible

```java
public void makeVisible​(
TreePath
path)
```

Ensures that the node identified by path is currently viewable.

**Parameters:** path

- the

TreePath

to make visible

- isVisible

```java
public boolean isVisible​(
TreePath
path)
```

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.
Otherwise, this method returns false.

**Parameters:** path

-

TreePath

identifying a node
**Returns:** true if the node is viewable, otherwise false

- getPathBounds

```java
public
Rectangle
getPathBounds​(
TreePath
path)
```

Returns the

Rectangle

that the specified node will be drawn
into. Returns

null

if any component in the path is hidden
(under a collapsed parent).

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

the node is drawn in,
or

null

- getRowBounds

```java
public
Rectangle
getRowBounds​(int row)
```

Returns the

Rectangle

that the node at the specified row is
drawn in.

**Parameters:** row

- the row to be drawn, where 0 is the first row in the
display
**Returns:** the

Rectangle

the node is drawn in

- scrollPathToVisible

```java
public void scrollPathToVisible​(
TreePath
path)
```

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** path

- the

TreePath

identifying the node to
bring into view

- scrollRowToVisible

```java
public void scrollRowToVisible​(int row)
```

Scrolls the item identified by row until it is displayed. The minimum
of amount of scrolling necessary to bring the row into view
is performed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** row

- an integer specifying the row to scroll, where 0 is the
first row in the display

- getPathForRow

```java
@BeanProperty
(
bound
=false)
public
TreePath
getPathForRow​(int row)
```

Returns the path for the specified row. If

row

is
not visible, or a

TreeUI

has not been set,

null

is returned.

**Parameters:** row

- an integer specifying a row
**Returns:** the

TreePath

to the specified node,

null

if

row < 0

or

row >= getRowCount()

- getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that displays the node identified by the specified
path.

**Parameters:** path

- the

TreePath

identifying a node
**Returns:** an integer specifying the display row, where 0 is the first
row in the display, or -1 if any of the elements in path
are hidden under a collapsed parent.

- expandPath

```java
public void expandPath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
expanded and viewable. If the last item in the path is a
leaf, this will have no effect.

**Parameters:** path

- the

TreePath

identifying a node

- expandRow

```java
public void expandRow​(int row)
```

Ensures that the node in the specified row is expanded and
viewable.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

- collapsePath

```java
public void collapsePath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
collapsed and viewable.

**Parameters:** path

- the

TreePath

identifying a node

- collapseRow

```java
public void collapseRow​(int row)
```

Ensures that the node in the specified row is collapsed.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

- getPathForLocation

```java
public
TreePath
getPathForLocation​(int x,
int y)
```

Returns the path for the node at the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node at that location

- getRowForLocation

```java
public int getRowForLocation​(int x,
int y)
```

Returns the row for the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row corresponding to the location, or -1 if the
location is not within the bounds of a displayed cell
**See Also:** getClosestRowForLocation(int, int)

- getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
no nodes are currently viewable, or there is no model, returns

null

, otherwise it always returns a valid path. To test if
the node is exactly at x, y, get the node's bounds and
test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node closest to that location,

null

if nothing is viewable or there is no model
**See Also:** getPathForLocation(int, int)

,

getPathBounds(javax.swing.tree.TreePath)

- getClosestRowForLocation

```java
public int getClosestRowForLocation​(int x,
int y)
```

Returns the row to the node that is closest to x,y. If no nodes
are viewable or there is no model, returns -1. Otherwise,
it always returns a valid row. To test if the returned object is
exactly at x, y, get the bounds for the node at the returned
row and test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row closest to the location, -1 if nothing is
viewable or there is no model
**See Also:** getRowForLocation(int, int)

,

getRowBounds(int)

- isEditing

```java
@BeanProperty
(
bound
=false)
public boolean isEditing()
```

Returns true if the tree is being edited. The item that is being
edited can be obtained using

getSelectionPath

.

**Returns:** true if the user is currently editing a node
**See Also:** getSelectionPath()

- stopEditing

```java
public boolean stopEditing()
```

Ends the current editing session.
(The

DefaultTreeCellEditor

object saves any edits that are currently in progress on a cell.
Other implementations may operate differently.)
Has no effect if the tree isn't being edited.

Note:

To make edit-saves automatic whenever the user changes
their position in the tree, use

setInvokesStopCellEditing(boolean)

.

**Returns:** true if editing was in progress and is now stopped,
false if editing was not in progress

- cancelEditing

```java
public void cancelEditing()
```

Cancels the current editing session. Has no effect if the
tree isn't being edited.

- startEditingAtPath

```java
public void startEditingAtPath​(
TreePath
path)
```

Selects the node identified by the specified path and initiates
editing. The edit-attempt fails if the

CellEditor

does not allow
editing for the specified item.

**Parameters:** path

- the

TreePath

identifying a node

- getEditingPath

```java
@BeanProperty
(
bound
=false)
public
TreePath
getEditingPath()
```

Returns the path to the element that is currently being edited.

**Returns:** the

TreePath

for the node being edited

- setSelectionModel

```java
@BeanProperty
(
description
="The tree\'s selection model.")
public void setSelectionModel​(
TreeSelectionModel
selectionModel)
```

Sets the tree's selection model. When a

null

value is
specified an empty

selectionModel

is used, which does not allow selections.

This is a bound property.

**Parameters:** selectionModel

- the

TreeSelectionModel

to use,
or

null

to disable selections
**See Also:** TreeSelectionModel

- getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model for selections. This should always return a
non-

null

value. If you don't want to allow anything
to be selected
set the selection model to

null

, which forces an empty
selection model to be used.

**Returns:** the model for selections
**See Also:** setSelectionModel(javax.swing.tree.TreeSelectionModel)

- getPathBetweenRows

```java
protected
TreePath
[] getPathBetweenRows​(int index0,
int index1)
```

Returns the paths (inclusive) between the specified rows. If
the specified indices are within the viewable set of rows, or
bound the viewable set of rows, then the indices are
constrained by the viewable set of rows. If the specified
indices are not within the viewable set of rows, or do not
bound the viewable set of rows, then an empty array is
returned. For example, if the row count is

10

, and this
method is invoked with

-1, 20

, then the specified
indices are constrained to the viewable set of rows, and this is
treated as if invoked with

0, 9

. On the other hand, if
this were invoked with

-10, -1

, then the specified
indices do not bound the viewable set of rows, and an empty
array is returned.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

**Parameters:** index0

- the first index in the range
**Parameters:** index1

- the last index in the range
**Returns:** the paths (inclusive) between the specified row indices

- setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Selects the rows in the specified interval (inclusive). If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified rows are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is cleared. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified indices bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified indices do not
bound the viewable set of rows, and the selection is cleared.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to select
**Parameters:** index1

- the last index in the range to select

- addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Adds the specified rows (inclusive) to the selection. If the
specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are
constrained by the viewable set of rows. If the indices are not
within the viewable set of rows, or do not bound the viewable
set of rows, then the selection is unchanged. For example, if
the row count is

10

, and this method is invoked with

-1, 20

, then the specified indices bounds the viewable
range, and this is treated as if invoked with

0, 9

. On
the other hand, if this were invoked with

-10, -1

, then
the specified indices do not bound the viewable set of rows,
and the selection is unchanged.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to add to the selection
**Parameters:** index1

- the last index in the range to add to the selection

- removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Removes the specified rows (inclusive) from the selection. If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is unchanged. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified range bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified range does not
bound the viewable set of rows, and the selection is unchanged.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

**Parameters:** index0

- the first row to remove from the selection
**Parameters:** index1

- the last row to remove from the selection

- removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes the node identified by the specified path from the current
selection.

**Parameters:** path

- the

TreePath

identifying a node

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes the nodes identified by the specified paths from the
current selection.

**Parameters:** paths

- an array of

TreePath

objects that
specifies the nodes to remove

- removeSelectionRow

```java
public void removeSelectionRow​(int row)
```

Removes the row at the index

row

from the current
selection.

**Parameters:** row

- the row to remove

- removeSelectionRows

```java
public void removeSelectionRows​(int[] rows)
```

Removes the rows that are selected at each of the specified
rows.

**Parameters:** rows

- an array of ints specifying display rows, where 0 is
the first row in the display

- clearSelection

```java
public void clearSelection()
```

Clears the selection.

- isSelectionEmpty

```java
@BeanProperty
(
bound
=false)
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** true if the selection is currently empty

- addTreeExpansionListener

```java
public void addTreeExpansionListener​(
TreeExpansionListener
tel)
```

Adds a listener for

TreeExpansion

events.

**Parameters:** tel

- a TreeExpansionListener that will be notified when
a tree node is expanded or collapsed (a "negative
expansion")

- removeTreeExpansionListener

```java
public void removeTreeExpansionListener​(
TreeExpansionListener
tel)
```

Removes a listener for

TreeExpansion

events.

**Parameters:** tel

- the

TreeExpansionListener

to remove

- getTreeExpansionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeExpansionListener
[] getTreeExpansionListeners()
```

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

**Returns:** all of the

TreeExpansionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addTreeWillExpandListener

```java
public void addTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Adds a listener for

TreeWillExpand

events.

**Parameters:** tel

- a

TreeWillExpandListener

that will be notified
when a tree node will be expanded or collapsed (a "negative
expansion")

- removeTreeWillExpandListener

```java
public void removeTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Removes a listener for

TreeWillExpand

events.

**Parameters:** tel

- the

TreeWillExpandListener

to remove

- getTreeWillExpandListeners

```java
@BeanProperty
(
bound
=false)
public
TreeWillExpandListener
[] getTreeWillExpandListeners()
```

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

**Returns:** all of the

TreeWillExpandListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireTreeExpanded

```java
public void fireTreeExpanded​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**See Also:** EventListenerList

- fireTreeCollapsed

```java
public void fireTreeCollapsed​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
collapsed
**See Also:** EventListenerList

- fireTreeWillExpand

```java
public void fireTreeWillExpand​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the expansion is prevented from occurring
**See Also:** EventListenerList

- fireTreeWillCollapse

```java
public void fireTreeWillCollapse​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the collapse is prevented from occurring
**See Also:** EventListenerList

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Adds a listener for

TreeSelection

events.

**Parameters:** tsl

- the

TreeSelectionListener

that will be notified
when a node is selected or deselected (a "negative
selection")

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Removes a

TreeSelection

listener.

**Parameters:** tsl

- the

TreeSelectionListener

to remove

- getTreeSelectionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

**Returns:** all of the

TreeSelectionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

TreeSelectionEvent

to be fired;
generated by the

TreeSelectionModel

when a node is selected or deselected
**See Also:** EventListenerList

- treeDidChange

```java
public void treeDidChange()
```

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree). You should never have to
invoke this, the UI will invoke this as it needs to.

- setVisibleRowCount

```java
@BeanProperty
(
description
="The number of rows that are to be displayed.")
public void setVisibleRowCount​(int newCount)
```

Sets the number of rows that are to be displayed.
This will only work if the tree is contained in a

JScrollPane

,
and will adjust the preferred size and size of that scrollpane.

This is a bound property.

**Parameters:** newCount

- the number of rows to display

- getVisibleRowCount

```java
public int getVisibleRowCount()
```

Returns the number of rows that are displayed in the display area.

**Returns:** the number of rows displayed

- getNextMatch

```java
public
TreePath
getNextMatch​(
String
prefix,
int startingRow,

Position.Bias
bias)
```

Returns the TreePath to the next tree element that
begins with a prefix. To handle the conversion of a

TreePath

into a String,

convertValueToText

is used.

**Parameters:** prefix

- the string to test for a match
**Parameters:** startingRow

- the row for starting the search
**Parameters:** bias

- the search direction, either
Position.Bias.Forward or Position.Bias.Backward.
**Returns:** the TreePath of the next tree element that
starts with the prefix; otherwise null
**Throws:** IllegalArgumentException

- if prefix is null
or startingRow is out of bounds
**Since:** 1.4

- getPreferredScrollableViewportSize

```java
@BeanProperty
(
bound
=false)
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred display size of a

JTree

. The height is
determined from

getVisibleRowCount

and the width
is the current preferred width.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** a

Dimension

object containing the preferred size
**See Also:** JComponent.getPreferredSize()

- getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount to increment when scrolling. The amount is
the height of the first displayed row that isn't completely in view
or, if it is totally displayed, the height of the next row in the
scrolling direction.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right
**Returns:** the "unit" increment for scrolling in the specified direction
**See Also:** JScrollBar.setUnitIncrement(int)

- getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** JScrollBar.setBlockIncrement(int)

- getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the tree should track the width of the viewport
**See Also:** Scrollable.getScrollableTracksViewportWidth()

- getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the tree should track the height of the viewport
**See Also:** Scrollable.getScrollableTracksViewportHeight()

- setExpandedState

```java
protected void setExpandedState​(
TreePath
path,
boolean state)
```

Sets the expanded state of this

JTree

.
If

state

is
true, all parents of

path

and path are marked as
expanded. If

state

is false, all parents of

path

are marked EXPANDED, but

path

itself
is marked collapsed.

This will fail if a

TreeWillExpandListener

vetos it.

**Parameters:** path

- a

TreePath

identifying a node
**Parameters:** state

- if

true

, all parents of @{code path} and path are marked as expanded.
Otherwise, all parents of

path

are marked EXPANDED,
but

path

itself is marked collapsed.

- getDescendantToggledPaths

```java
protected
Enumeration
<
TreePath
> getDescendantToggledPaths​(
TreePath
parent)
```

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

**Parameters:** parent

- a path
**Returns:** the

Enumeration

of

TreePaths

- removeDescendantToggledPaths

```java
protected void removeDescendantToggledPaths​(
Enumeration
<
TreePath
> toRemove)
```

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

**Parameters:** toRemove

- an enumeration of the paths to remove; a value of

null

is ignored
**Throws:** ClassCastException

- if

toRemove

contains an
element that is not a

TreePath

;

null

values are ignored

- clearToggledPaths

```java
protected void clearToggledPaths()
```

Clears the cache of toggled tree paths. This does NOT send out
any

TreeExpansionListener

events.

- createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Creates and returns an instance of

TreeModelHandler

.
The returned
object is responsible for updating the expanded state when the

TreeModel

changes.

For more information on what expanded state means, see the

JTree description

above.

**Returns:** the instance of

TreeModelHandler

- removeDescendantSelectedPaths

```java
protected boolean removeDescendantSelectedPaths​(
TreePath
path,
boolean includePath)
```

Removes any paths in the selection that are descendants of

path

. If

includePath

is true and

path

is selected, it will be removed from the selection.

**Parameters:** path

- a path
**Parameters:** includePath

- is

true

and

path

is selected,
it will be removed from the selection.
**Returns:** true if a descendant was selected
**Since:** 1.3

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTree

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTree

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTree.
For JTrees, the AccessibleContext takes the form of an
AccessibleJTree.
A new AccessibleJTree instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTree that serves as the
AccessibleContext of this JTree

Field Detail

- treeModel

```java
protected transient
TreeModel
treeModel
```

The model that defines the tree displayed by this object.

- selectionModel

```java
protected transient
TreeSelectionModel
selectionModel
```

Models the set of selected nodes in this tree.

- rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

- cellRenderer

```java
protected transient
TreeCellRenderer
cellRenderer
```

The cell used to draw nodes. If

null

, the UI uses a default

cellRenderer

.

- rowHeight

```java
protected int rowHeight
```

Height to use for each display row. If this is <= 0 the renderer
determines the height for each row.

- showsRootHandles

```java
protected boolean showsRootHandles
```

True if handles are displayed at the topmost level of the tree.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

**See Also:** rootVisible

- selectionRedirector

```java
protected transient
JTree.TreeSelectionRedirector
selectionRedirector
```

Creates a new event and passed it off the

selectionListeners

.

- cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the entries. Default is

null

(tree is not editable).

- editable

```java
protected boolean editable
```

Is the tree editable? Default is false.

- largeModel

```java
protected boolean largeModel
```

Is this tree a large model? This is a code-optimization setting.
A large model can be used when the cell height is the same for all
nodes. The UI will then cache very little information and instead
continually message the model. Without a large model the UI caches
most of the information, resulting in fewer method calls to the model.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

- visibleRowCount

```java
protected int visibleRowCount
```

Number of rows to make visible at one time. This value is used for
the

Scrollable

interface. It determines the preferred
size of the display area.

- invokesStopCellEditing

```java
protected boolean invokesStopCellEditing
```

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved. If false,

cancelCellEditing

is invoked, and changes
are discarded. Default is false.

- scrollsOnExpand

```java
protected boolean scrollsOnExpand
```

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

- toggleClickCount

```java
protected int toggleClickCount
```

Number of mouse clicks before a node is expanded.

- treeModelListener

```java
protected transient
TreeModelListener
treeModelListener
```

Updates the

expandedState

.

- CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Bound property name for

cellRenderer

.

**See Also:** Constant Field Values

- TREE_MODEL_PROPERTY

```java
public static final
String
TREE_MODEL_PROPERTY
```

Bound property name for

treeModel

.

**See Also:** Constant Field Values

- ROOT_VISIBLE_PROPERTY

```java
public static final
String
ROOT_VISIBLE_PROPERTY
```

Bound property name for

rootVisible

.

**See Also:** Constant Field Values

- SHOWS_ROOT_HANDLES_PROPERTY

```java
public static final
String
SHOWS_ROOT_HANDLES_PROPERTY
```

Bound property name for

showsRootHandles

.

**See Also:** Constant Field Values

- ROW_HEIGHT_PROPERTY

```java
public static final
String
ROW_HEIGHT_PROPERTY
```

Bound property name for

rowHeight

.

**See Also:** Constant Field Values

- CELL_EDITOR_PROPERTY

```java
public static final
String
CELL_EDITOR_PROPERTY
```

Bound property name for

cellEditor

.

**See Also:** Constant Field Values

- EDITABLE_PROPERTY

```java
public static final
String
EDITABLE_PROPERTY
```

Bound property name for

editable

.

**See Also:** Constant Field Values

- LARGE_MODEL_PROPERTY

```java
public static final
String
LARGE_MODEL_PROPERTY
```

Bound property name for

largeModel

.

**See Also:** Constant Field Values

- SELECTION_MODEL_PROPERTY

```java
public static final
String
SELECTION_MODEL_PROPERTY
```

Bound property name for selectionModel.

**See Also:** Constant Field Values

- VISIBLE_ROW_COUNT_PROPERTY

```java
public static final
String
VISIBLE_ROW_COUNT_PROPERTY
```

Bound property name for

visibleRowCount

.

**See Also:** Constant Field Values

- INVOKES_STOP_CELL_EDITING_PROPERTY

```java
public static final
String
INVOKES_STOP_CELL_EDITING_PROPERTY
```

Bound property name for

messagesStopCellEditing

.

**See Also:** Constant Field Values

- SCROLLS_ON_EXPAND_PROPERTY

```java
public static final
String
SCROLLS_ON_EXPAND_PROPERTY
```

Bound property name for

scrollsOnExpand

.

**See Also:** Constant Field Values

- TOGGLE_CLICK_COUNT_PROPERTY

```java
public static final
String
TOGGLE_CLICK_COUNT_PROPERTY
```

Bound property name for

toggleClickCount

.

**See Also:** Constant Field Values

- LEAD_SELECTION_PATH_PROPERTY

```java
public static final
String
LEAD_SELECTION_PATH_PROPERTY
```

Bound property name for

leadSelectionPath

.

**Since:** 1.3
**See Also:** Constant Field Values

- ANCHOR_SELECTION_PATH_PROPERTY

```java
public static final
String
ANCHOR_SELECTION_PATH_PROPERTY
```

Bound property name for anchor selection path.

**Since:** 1.3
**See Also:** Constant Field Values

- EXPANDS_SELECTED_PATHS_PROPERTY

```java
public static final
String
EXPANDS_SELECTED_PATHS_PROPERTY
```

Bound property name for expands selected paths property

**Since:** 1.3
**See Also:** Constant Field Values

---

#### Field Detail

treeModel

```java
protected transient
TreeModel
treeModel
```

The model that defines the tree displayed by this object.

---

#### treeModel

protected transient

TreeModel

treeModel

The model that defines the tree displayed by this object.

selectionModel

```java
protected transient
TreeSelectionModel
selectionModel
```

Models the set of selected nodes in this tree.

---

#### selectionModel

protected transient

TreeSelectionModel

selectionModel

Models the set of selected nodes in this tree.

rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

---

#### rootVisible

protected boolean rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

cellRenderer

```java
protected transient
TreeCellRenderer
cellRenderer
```

The cell used to draw nodes. If

null

, the UI uses a default

cellRenderer

.

---

#### cellRenderer

protected transient

TreeCellRenderer

cellRenderer

The cell used to draw nodes. If

null

, the UI uses a default

cellRenderer

.

rowHeight

```java
protected int rowHeight
```

Height to use for each display row. If this is <= 0 the renderer
determines the height for each row.

---

#### rowHeight

protected int rowHeight

Height to use for each display row. If this is <= 0 the renderer
determines the height for each row.

showsRootHandles

```java
protected boolean showsRootHandles
```

True if handles are displayed at the topmost level of the tree.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

**See Also:** rootVisible

---

#### showsRootHandles

protected boolean showsRootHandles

True if handles are displayed at the topmost level of the tree.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

A handle is a small icon that displays adjacent to the node which
allows the user to click once to expand or collapse the node. A
common interface shows a plus sign (+) for a node which can be
expanded and a minus sign (-) for a node which can be collapsed.
Handles are always shown for nodes below the topmost level.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

If the

rootVisible

setting specifies that the root
node is to be displayed, then that is the only node at the topmost
level. If the root node is not displayed, then all of its
children are at the topmost level of the tree. Handles are
always displayed for nodes other than the topmost.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

If the root node isn't visible, it is generally a good to make
this value true. Otherwise, the tree looks exactly like a list,
and users may not know that the "list entries" are actually
tree nodes.

selectionRedirector

```java
protected transient
JTree.TreeSelectionRedirector
selectionRedirector
```

Creates a new event and passed it off the

selectionListeners

.

---

#### selectionRedirector

protected transient

JTree.TreeSelectionRedirector

selectionRedirector

Creates a new event and passed it off the

selectionListeners

.

cellEditor

```java
protected transient
TreeCellEditor
cellEditor
```

Editor for the entries. Default is

null

(tree is not editable).

---

#### cellEditor

protected transient

TreeCellEditor

cellEditor

Editor for the entries. Default is

null

(tree is not editable).

editable

```java
protected boolean editable
```

Is the tree editable? Default is false.

---

#### editable

protected boolean editable

Is the tree editable? Default is false.

largeModel

```java
protected boolean largeModel
```

Is this tree a large model? This is a code-optimization setting.
A large model can be used when the cell height is the same for all
nodes. The UI will then cache very little information and instead
continually message the model. Without a large model the UI caches
most of the information, resulting in fewer method calls to the model.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

---

#### largeModel

protected boolean largeModel

Is this tree a large model? This is a code-optimization setting.
A large model can be used when the cell height is the same for all
nodes. The UI will then cache very little information and instead
continually message the model. Without a large model the UI caches
most of the information, resulting in fewer method calls to the model.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

This value is only a suggestion to the UI. Not all UIs will
take advantage of it. Default value is false.

visibleRowCount

```java
protected int visibleRowCount
```

Number of rows to make visible at one time. This value is used for
the

Scrollable

interface. It determines the preferred
size of the display area.

---

#### visibleRowCount

protected int visibleRowCount

Number of rows to make visible at one time. This value is used for
the

Scrollable

interface. It determines the preferred
size of the display area.

invokesStopCellEditing

```java
protected boolean invokesStopCellEditing
```

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved. If false,

cancelCellEditing

is invoked, and changes
are discarded. Default is false.

---

#### invokesStopCellEditing

protected boolean invokesStopCellEditing

If true, when editing is to be stopped by way of selection changing,
data in tree changing or other means

stopCellEditing

is invoked, and changes are saved. If false,

cancelCellEditing

is invoked, and changes
are discarded. Default is false.

scrollsOnExpand

```java
protected boolean scrollsOnExpand
```

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

---

#### scrollsOnExpand

protected boolean scrollsOnExpand

If true, when a node is expanded, as many of the descendants are
scrolled to be visible.

toggleClickCount

```java
protected int toggleClickCount
```

Number of mouse clicks before a node is expanded.

---

#### toggleClickCount

protected int toggleClickCount

Number of mouse clicks before a node is expanded.

treeModelListener

```java
protected transient
TreeModelListener
treeModelListener
```

Updates the

expandedState

.

---

#### treeModelListener

protected transient

TreeModelListener

treeModelListener

Updates the

expandedState

.

CELL_RENDERER_PROPERTY

```java
public static final
String
CELL_RENDERER_PROPERTY
```

Bound property name for

cellRenderer

.

**See Also:** Constant Field Values

---

#### CELL_RENDERER_PROPERTY

public static final

String

CELL_RENDERER_PROPERTY

Bound property name for

cellRenderer

.

TREE_MODEL_PROPERTY

```java
public static final
String
TREE_MODEL_PROPERTY
```

Bound property name for

treeModel

.

**See Also:** Constant Field Values

---

#### TREE_MODEL_PROPERTY

public static final

String

TREE_MODEL_PROPERTY

Bound property name for

treeModel

.

ROOT_VISIBLE_PROPERTY

```java
public static final
String
ROOT_VISIBLE_PROPERTY
```

Bound property name for

rootVisible

.

**See Also:** Constant Field Values

---

#### ROOT_VISIBLE_PROPERTY

public static final

String

ROOT_VISIBLE_PROPERTY

Bound property name for

rootVisible

.

SHOWS_ROOT_HANDLES_PROPERTY

```java
public static final
String
SHOWS_ROOT_HANDLES_PROPERTY
```

Bound property name for

showsRootHandles

.

**See Also:** Constant Field Values

---

#### SHOWS_ROOT_HANDLES_PROPERTY

public static final

String

SHOWS_ROOT_HANDLES_PROPERTY

Bound property name for

showsRootHandles

.

ROW_HEIGHT_PROPERTY

```java
public static final
String
ROW_HEIGHT_PROPERTY
```

Bound property name for

rowHeight

.

**See Also:** Constant Field Values

---

#### ROW_HEIGHT_PROPERTY

public static final

String

ROW_HEIGHT_PROPERTY

Bound property name for

rowHeight

.

CELL_EDITOR_PROPERTY

```java
public static final
String
CELL_EDITOR_PROPERTY
```

Bound property name for

cellEditor

.

**See Also:** Constant Field Values

---

#### CELL_EDITOR_PROPERTY

public static final

String

CELL_EDITOR_PROPERTY

Bound property name for

cellEditor

.

EDITABLE_PROPERTY

```java
public static final
String
EDITABLE_PROPERTY
```

Bound property name for

editable

.

**See Also:** Constant Field Values

---

#### EDITABLE_PROPERTY

public static final

String

EDITABLE_PROPERTY

Bound property name for

editable

.

LARGE_MODEL_PROPERTY

```java
public static final
String
LARGE_MODEL_PROPERTY
```

Bound property name for

largeModel

.

**See Also:** Constant Field Values

---

#### LARGE_MODEL_PROPERTY

public static final

String

LARGE_MODEL_PROPERTY

Bound property name for

largeModel

.

SELECTION_MODEL_PROPERTY

```java
public static final
String
SELECTION_MODEL_PROPERTY
```

Bound property name for selectionModel.

**See Also:** Constant Field Values

---

#### SELECTION_MODEL_PROPERTY

public static final

String

SELECTION_MODEL_PROPERTY

Bound property name for selectionModel.

VISIBLE_ROW_COUNT_PROPERTY

```java
public static final
String
VISIBLE_ROW_COUNT_PROPERTY
```

Bound property name for

visibleRowCount

.

**See Also:** Constant Field Values

---

#### VISIBLE_ROW_COUNT_PROPERTY

public static final

String

VISIBLE_ROW_COUNT_PROPERTY

Bound property name for

visibleRowCount

.

INVOKES_STOP_CELL_EDITING_PROPERTY

```java
public static final
String
INVOKES_STOP_CELL_EDITING_PROPERTY
```

Bound property name for

messagesStopCellEditing

.

**See Also:** Constant Field Values

---

#### INVOKES_STOP_CELL_EDITING_PROPERTY

public static final

String

INVOKES_STOP_CELL_EDITING_PROPERTY

Bound property name for

messagesStopCellEditing

.

SCROLLS_ON_EXPAND_PROPERTY

```java
public static final
String
SCROLLS_ON_EXPAND_PROPERTY
```

Bound property name for

scrollsOnExpand

.

**See Also:** Constant Field Values

---

#### SCROLLS_ON_EXPAND_PROPERTY

public static final

String

SCROLLS_ON_EXPAND_PROPERTY

Bound property name for

scrollsOnExpand

.

TOGGLE_CLICK_COUNT_PROPERTY

```java
public static final
String
TOGGLE_CLICK_COUNT_PROPERTY
```

Bound property name for

toggleClickCount

.

**See Also:** Constant Field Values

---

#### TOGGLE_CLICK_COUNT_PROPERTY

public static final

String

TOGGLE_CLICK_COUNT_PROPERTY

Bound property name for

toggleClickCount

.

LEAD_SELECTION_PATH_PROPERTY

```java
public static final
String
LEAD_SELECTION_PATH_PROPERTY
```

Bound property name for

leadSelectionPath

.

**Since:** 1.3
**See Also:** Constant Field Values

---

#### LEAD_SELECTION_PATH_PROPERTY

public static final

String

LEAD_SELECTION_PATH_PROPERTY

Bound property name for

leadSelectionPath

.

ANCHOR_SELECTION_PATH_PROPERTY

```java
public static final
String
ANCHOR_SELECTION_PATH_PROPERTY
```

Bound property name for anchor selection path.

**Since:** 1.3
**See Also:** Constant Field Values

---

#### ANCHOR_SELECTION_PATH_PROPERTY

public static final

String

ANCHOR_SELECTION_PATH_PROPERTY

Bound property name for anchor selection path.

EXPANDS_SELECTED_PATHS_PROPERTY

```java
public static final
String
EXPANDS_SELECTED_PATHS_PROPERTY
```

Bound property name for expands selected paths property

**Since:** 1.3
**See Also:** Constant Field Values

---

#### EXPANDS_SELECTED_PATHS_PROPERTY

public static final

String

EXPANDS_SELECTED_PATHS_PROPERTY

Bound property name for expands selected paths property

Constructor Detail

- JTree

```java
public JTree()
```

Returns a

JTree

with a sample model.
The default model used by the tree defines a leaf node as any node
without children.

**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Object
[] value)
```

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.
By default, the tree defines a leaf node as any node without
children.

**Parameters:** value

- an array of

Object

s
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Vector
<?> value)
```

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed. By default, the
tree defines a leaf node as any node without children.

**Parameters:** value

- a

Vector
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
Hashtable
<?,​?> value)
```

Returns a

JTree

created from a

Hashtable

which does not display with root.
Each value-half of the key/value pairs in the

HashTable

becomes a child of the new root node. By default, the tree defines
a leaf node as any node without children.

**Parameters:** value

- a

Hashtable
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
TreeNode
root)
```

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.
By default, the tree defines a leaf node as any node without children.

**Parameters:** root

- a

TreeNode

object
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
public JTree​(
TreeNode
root,
boolean asksAllowsChildren)
```

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

**Parameters:** root

- a

TreeNode

object
**Parameters:** asksAllowsChildren

- if false, any node without children is a
leaf node; if true, only nodes that do not allow
children are leaf nodes
**See Also:** DefaultTreeModel.asksAllowsChildren

- JTree

```java
@ConstructorProperties
("model")
public JTree​(
TreeModel
newModel)
```

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

**Parameters:** newModel

- the

TreeModel

to use as the data model

---

#### Constructor Detail

JTree

```java
public JTree()
```

Returns a

JTree

with a sample model.
The default model used by the tree defines a leaf node as any node
without children.

**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree()

Returns a

JTree

with a sample model.
The default model used by the tree defines a leaf node as any node
without children.

JTree

```java
public JTree​(
Object
[] value)
```

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.
By default, the tree defines a leaf node as any node without
children.

**Parameters:** value

- an array of

Object

s
**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree​(

Object

[] value)

Returns a

JTree

with each element of the
specified array as the
child of a new root node which is not displayed.
By default, the tree defines a leaf node as any node without
children.

JTree

```java
public JTree​(
Vector
<?> value)
```

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed. By default, the
tree defines a leaf node as any node without children.

**Parameters:** value

- a

Vector
**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree​(

Vector

<?> value)

Returns a

JTree

with each element of the specified

Vector

as the
child of a new root node which is not displayed. By default, the
tree defines a leaf node as any node without children.

JTree

```java
public JTree​(
Hashtable
<?,​?> value)
```

Returns a

JTree

created from a

Hashtable

which does not display with root.
Each value-half of the key/value pairs in the

HashTable

becomes a child of the new root node. By default, the tree defines
a leaf node as any node without children.

**Parameters:** value

- a

Hashtable
**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree​(

Hashtable

<?,​?> value)

Returns a

JTree

created from a

Hashtable

which does not display with root.
Each value-half of the key/value pairs in the

HashTable

becomes a child of the new root node. By default, the tree defines
a leaf node as any node without children.

JTree

```java
public JTree​(
TreeNode
root)
```

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.
By default, the tree defines a leaf node as any node without children.

**Parameters:** root

- a

TreeNode

object
**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree​(

TreeNode

root)

Returns a

JTree

with the specified

TreeNode

as its root,
which displays the root node.
By default, the tree defines a leaf node as any node without children.

JTree

```java
public JTree​(
TreeNode
root,
boolean asksAllowsChildren)
```

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

**Parameters:** root

- a

TreeNode

object
**Parameters:** asksAllowsChildren

- if false, any node without children is a
leaf node; if true, only nodes that do not allow
children are leaf nodes
**See Also:** DefaultTreeModel.asksAllowsChildren

---

#### JTree

public JTree​(

TreeNode

root,
boolean asksAllowsChildren)

Returns a

JTree

with the specified

TreeNode

as its root, which
displays the root node and which decides whether a node is a
leaf node in the specified manner.

JTree

```java
@ConstructorProperties
("model")
public JTree​(
TreeModel
newModel)
```

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

**Parameters:** newModel

- the

TreeModel

to use as the data model

---

#### JTree

@ConstructorProperties

("model")
public JTree​(

TreeModel

newModel)

Returns an instance of

JTree

which displays the root node
-- the tree is created using the specified data model.

Method Detail

- getDefaultTreeModel

```java
protected static
TreeModel
getDefaultTreeModel()
```

Creates and returns a sample

TreeModel

.
Used primarily for beanbuilders to show something interesting.

**Returns:** the default

TreeModel

- createTreeModel

```java
protected static
TreeModel
createTreeModel​(
Object
value)
```

Returns a

TreeModel

wrapping the specified object.
If the object is:

- an array of

Object

s,

a

Hashtable

, or

a

Vector

then a new root node is created with each of the incoming
objects as children. Otherwise, a new root is created with
a value of

"root"

.

**Parameters:** value

- the

Object

used as the foundation for
the

TreeModel
**Returns:** a

TreeModel

wrapping the specified object

- getUI

```java
public
TreeUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TreeUI

object that renders this component

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
TreeUI
ui)
```

Sets the L&F object that renders this component.

This is a bound property.

**Parameters:** ui

- the

TreeUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TreeUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getCellRenderer

```java
public
TreeCellRenderer
getCellRenderer()
```

Returns the current

TreeCellRenderer

that is rendering each cell.

**Returns:** the

TreeCellRenderer

that is rendering each cell

- setCellRenderer

```java
@BeanProperty
(
description
="The TreeCellRenderer that will be used to draw each cell.")
public void setCellRenderer​(
TreeCellRenderer
x)
```

Sets the

TreeCellRenderer

that will be used to
draw each cell.

This is a bound property.

**Parameters:** x

- the

TreeCellRenderer

that is to render each cell

- setEditable

```java
@BeanProperty
(
description
="Whether the tree is editable.")
public void setEditable​(boolean flag)
```

Determines whether the tree is editable. Fires a property
change event if the new setting is different from the existing
setting.

This is a bound property.

**Parameters:** flag

- a boolean value, true if the tree is editable

- isEditable

```java
public boolean isEditable()
```

Returns true if the tree is editable.

**Returns:** true if the tree is editable

- setCellEditor

```java
@BeanProperty
(
description
="The cell editor. A null value implies the tree cannot be edited.")
public void setCellEditor​(
TreeCellEditor
cellEditor)
```

Sets the cell editor. A

null

value implies that the
tree cannot be edited. If this represents a change in the

cellEditor

, the

propertyChange

method is invoked on all listeners.

This is a bound property.

**Parameters:** cellEditor

- the

TreeCellEditor

to use

- getCellEditor

```java
public
TreeCellEditor
getCellEditor()
```

Returns the editor used to edit entries in the tree.

**Returns:** the

TreeCellEditor

in use,
or

null

if the tree cannot be edited

- getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

- setModel

```java
@BeanProperty
(
description
="The TreeModel that will provide the data.")
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

This is a bound property.

**Parameters:** newModel

- the

TreeModel

that is to provide the data

- isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

- setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

This is a bound property.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

- setShowsRootHandles

```java
@BeanProperty
(
description
="Whether the node handles are to be displayed.")
public void setShowsRootHandles​(boolean newValue)
```

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.
The default value of this property depends on the constructor
used to create the

JTree

.
Some look and feels might not support handles;
they will ignore this property.

This is a bound property.

**Parameters:** newValue

-

true

if root handles should be displayed;
otherwise,

false
**See Also:** showsRootHandles

,

getShowsRootHandles()

- getShowsRootHandles

```java
public boolean getShowsRootHandles()
```

Returns the value of the

showsRootHandles

property.

**Returns:** the value of the

showsRootHandles

property
**See Also:** showsRootHandles

- setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell, in pixels. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

This is a bound property.

**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

- isFixedRowHeight

```java
@BeanProperty
(
bound
=false)
public boolean isFixedRowHeight()
```

Returns true if the height of each display row is a fixed size.

**Returns:** true if the height of each row is a fixed size

- setLargeModel

```java
@BeanProperty
(
description
="Whether the UI should use a large model.")
public void setLargeModel​(boolean newValue)
```

Specifies whether the UI should use a large model.
(Not all UIs will implement this.) Fires a property change
for the LARGE_MODEL_PROPERTY.

This is a bound property.

**Parameters:** newValue

- true to suggest a large model to the UI
**See Also:** largeModel

- isLargeModel

```java
public boolean isLargeModel()
```

Returns true if the tree is configured for a large model.

**Returns:** true if a large model is suggested
**See Also:** largeModel

- setInvokesStopCellEditing

```java
@BeanProperty
(
description
="Determines what happens when editing is interrupted, selecting another node in the tree, a change in the tree\'s data, or some other means.")
public void setInvokesStopCellEditing​(boolean newValue)
```

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means. Setting this property to

true

causes the
changes to be automatically saved when editing is interrupted.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

**Parameters:** newValue

- true means that

stopCellEditing

is invoked
when editing is interrupted, and data is saved; false means that

cancelCellEditing

is invoked, and changes are lost

- getInvokesStopCellEditing

```java
public boolean getInvokesStopCellEditing()
```

Returns the indicator that tells what happens when editing is
interrupted.

**Returns:** the indicator that tells what happens when editing is
interrupted
**See Also:** setInvokesStopCellEditing(boolean)

- setScrollsOnExpand

```java
@BeanProperty
(
description
="Indicates if a node descendant should be scrolled when expanded.")
public void setScrollsOnExpand​(boolean newValue)
```

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.
If this property is

true

(the default),
when a node expands
the tree can use scrolling to make
the maximum possible number of the node's descendants visible.
In some look and feels, trees might not need to scroll when expanded;
those look and feels will ignore this property.

This is a bound property.

**Parameters:** newValue

-

false

to disable scrolling on expansion;

true

to enable it
**See Also:** getScrollsOnExpand()

- getScrollsOnExpand

```java
public boolean getScrollsOnExpand()
```

Returns the value of the

scrollsOnExpand

property.

**Returns:** the value of the

scrollsOnExpand

property

- setToggleClickCount

```java
@BeanProperty
(
description
="Number of clicks before a node will expand/collapse.")
public void setToggleClickCount​(int clickCount)
```

Sets the number of mouse clicks before a node will expand or close.
The default is two.

This is a bound property.

**Parameters:** clickCount

- the number of mouse clicks to get a node expanded or closed
**Since:** 1.3

- getToggleClickCount

```java
public int getToggleClickCount()
```

Returns the number of mouse clicks needed to expand or close a node.

**Returns:** number of mouse clicks before node is expanded
**Since:** 1.3

- setExpandsSelectedPaths

```java
@BeanProperty
(
description
="Indicates whether changes to the selection should make the parent of the path visible.")
public void setExpandsSelectedPaths​(boolean newValue)
```

Configures the

expandsSelectedPaths

property. If
true, any time the selection is changed, either via the

TreeSelectionModel

, or the cover methods provided by

JTree

, the

TreePath

s parents will be
expanded to make them visible (visible meaning the parent path is
expanded, not necessarily in the visible rectangle of the

JTree

). If false, when the selection
changes the nodes parent is not made visible (all its parents expanded).
This is useful if you wish to have your selection model maintain paths
that are not always visible (all parents expanded).

This is a bound property.

**Parameters:** newValue

- the new value for

expandsSelectedPaths
**Since:** 1.3

- getExpandsSelectedPaths

```java
public boolean getExpandsSelectedPaths()
```

Returns the

expandsSelectedPaths

property.

**Returns:** true if selection changes result in the parent path being
expanded
**Since:** 1.3
**See Also:** setExpandsSelectedPaths(boolean)

- setDragEnabled

```java
@BeanProperty
(
bound
=false,

description
="determines whether automatic drag handling is enabled")
public void setDragEnabled​(boolean b)
```

Turns on or off automatic drag handling. In order to enable automatic
drag handling, this property should be set to

true

, and the
tree's

TransferHandler

needs to be

non-null

.
The default value of the

dragEnabled

property is

false

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

**Parameters:** b

- whether or not to enable automatic drag handling
**Throws:** HeadlessException

- if

b

is

true

and

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

,

getDragEnabled()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

- getDragEnabled

```java
public boolean getDragEnabled()
```

Returns whether or not automatic drag handling is enabled.

**Returns:** the value of the

dragEnabled

property
**Since:** 1.4
**See Also:** setDragEnabled(boolean)

- setDropMode

```java
public final void setDropMode​(
DropMode
dropMode)
```

Sets the drop mode for this component. For backward compatibility,
the default for this property is

DropMode.USE_SELECTION

.
Usage of one of the other modes is recommended, however, for an
improved user experience.

DropMode.ON

, for instance,
offers similar behavior of showing items as selected, but does so without
affecting the actual selection in the tree.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

**Parameters:** dropMode

- the drop mode to use
**Throws:** IllegalArgumentException

- if the drop mode is unsupported
or

null
**Since:** 1.6
**See Also:** getDropMode()

,

getDropLocation()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

- getDropMode

```java
public final
DropMode
getDropMode()
```

Returns the drop mode for this component.

**Returns:** the drop mode for this component
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

- getDropLocation

```java
@BeanProperty
(
bound
=false)
public final
JTree.DropLocation
getDropLocation()
```

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

**Returns:** the drop location
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

,

TransferHandler.canImport(TransferHandler.TransferSupport)

- isPathEditable

```java
public boolean isPathEditable​(
TreePath
path)
```

Returns

isEditable

. This is invoked from the UI before
editing begins to insure that the given path can be edited. This
is provided as an entry point for subclassers to add filtered
editing without having to resort to creating a new editor.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if every parent node and the node itself is editable
**See Also:** isEditable()

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that initiated the

ToolTip

display
**Returns:** a string containing the tooltip or

null

if

event

is null

- convertValueToText

```java
public
String
convertValueToText​(
Object
value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Called by the renderers to convert the specified value to
text. This implementation returns

value.toString

, ignoring
all other arguments. To control the conversion, subclass this
method and use any of the arguments you need.

**Parameters:** value

- the

Object

to convert to text
**Parameters:** selected

- true if the node is selected
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- an integer specifying the node's display row, where 0 is
the first row in the display
**Parameters:** hasFocus

- true if the node has the focus
**Returns:** the

String

representation of the node's value

- getRowCount

```java
@BeanProperty
(
bound
=false)
public int getRowCount()
```

Returns the number of viewable nodes. A node is viewable if all of its
parents are expanded. The root is only included in this count if

isRootVisible()

is

true

. This returns

0

if
the UI has not been set.

**Returns:** the number of viewable nodes

- setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Selects the node identified by the specified path. If any
component of the path is hidden (under a collapsed node), and

getExpandsSelectedPaths

is true it is
exposed (made viewable).

**Parameters:** path

- the

TreePath

specifying the node to select

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

Selects the nodes identified by the specified array of paths.
If any component in any of the paths is hidden (under a collapsed
node), and

getExpandsSelectedPaths

is true
it is exposed (made viewable).

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to select

- setLeadSelectionPath

```java
@BeanProperty
(
description
="Lead selection path")
public void setLeadSelectionPath​(
TreePath
newPath)
```

Sets the path identifies as the lead. The lead may not be selected.
The lead is not maintained by

JTree

,
rather the UI will update it.

This is a bound property.

**Parameters:** newPath

- the new lead path
**Since:** 1.3

- setAnchorSelectionPath

```java
@BeanProperty
(
description
="Anchor selection path")
public void setAnchorSelectionPath​(
TreePath
newPath)
```

Sets the path identified as the anchor.
The anchor is not maintained by

JTree

, rather the UI will
update it.

This is a bound property.

**Parameters:** newPath

- the new anchor path
**Since:** 1.3

- setSelectionRow

```java
public void setSelectionRow​(int row)
```

Selects the node at the specified row in the display.

**Parameters:** row

- the row to select, where 0 is the first row in
the display

- setSelectionRows

```java
public void setSelectionRows​(int[] rows)
```

Selects the nodes corresponding to each of the specified rows
in the display. If a particular element of

rows

is
< 0 or >=

getRowCount

, it will be ignored.
If none of the elements
in

rows

are valid rows, the selection will
be cleared. That is it will be as if

clearSelection

was invoked.

**Parameters:** rows

- an array of ints specifying the rows to select,
where 0 indicates the first row in the display

- addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds the node identified by the specified

TreePath

to the current selection. If any component of the path isn't
viewable, and

getExpandsSelectedPaths

is true it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** path

- the

TreePath

to add

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds each path in the array of paths to the current selection. If
any component of any of the paths isn't viewable and

getExpandsSelectedPaths

is true, it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to add

- addSelectionRow

```java
public void addSelectionRow​(int row)
```

Adds the path at the specified row to the current selection.

**Parameters:** row

- an integer specifying the row of the node to add,
where 0 is the first row in the display

- addSelectionRows

```java
public void addSelectionRows​(int[] rows)
```

Adds the paths at each of the specified rows to the current selection.

**Parameters:** rows

- an array of ints specifying the rows to add,
where 0 indicates the first row in the display

- getLastSelectedPathComponent

```java
@BeanProperty
(
bound
=false)
public
Object
getLastSelectedPathComponent()
```

Returns the last path component of the selected path. This is
a convenience method for

getSelectionModel().getSelectionPath().getLastPathComponent()

.
This is typically only useful if the selection has one path.

**Returns:** the last path component of the selected path, or

null

if nothing is selected
**See Also:** TreePath.getLastPathComponent()

- getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the path identified as the lead.

**Returns:** path identified as the lead

- getAnchorSelectionPath

```java
public
TreePath
getAnchorSelectionPath()
```

Returns the path identified as the anchor.

**Returns:** path identified as the anchor
**Since:** 1.3

- getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the path to the first selected node.

**Returns:** the

TreePath

for the first selected node,
or

null

if nothing is currently selected

- getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the paths of all selected values.

**Returns:** an array of

TreePath

objects indicating the selected
nodes, or

null

if nothing is currently selected

- getSelectionRows

```java
public int[] getSelectionRows()
```

Returns all of the currently selected rows. This method is simply
forwarded to the

TreeSelectionModel

.
If nothing is selected

null

or an empty array will
be returned, based on the

TreeSelectionModel

implementation.

**Returns:** an array of integers that identifies all currently selected rows
where 0 is the first row in the display

- getSelectionCount

```java
@BeanProperty
(
bound
=false)
public int getSelectionCount()
```

Returns the number of nodes selected.

**Returns:** the number of nodes selected

- getMinSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMinSelectionRow()
```

Returns the smallest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the smallest selected row

- getMaxSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMaxSelectionRow()
```

Returns the largest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the largest selected row

- getLeadSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getLeadSelectionRow()
```

Returns the row index corresponding to the lead path.

**Returns:** an integer giving the row index of the lead path,
where 0 is the first row in the display; or -1
if

leadPath

is

null

- isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the item identified by the path is currently selected.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the node is selected

- isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the node identified by row is selected.

**Parameters:** row

- an integer specifying a display row, where 0 is the first
row in the display
**Returns:** true if the node is selected

- getExpandedDescendants

```java
public
Enumeration
<
TreePath
> getExpandedDescendants​(
TreePath
parent)
```

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded. If

parent

is not currently
expanded, this will return

null

.
If you expand/collapse nodes while
iterating over the returned

Enumeration

this may not return all
the expanded paths, or may return paths that are no longer expanded.

**Parameters:** parent

- the path which is to be examined
**Returns:** an

Enumeration

of the descendents of

parent

, or

null

if

parent

is not currently expanded

- hasBeenExpanded

```java
public boolean hasBeenExpanded​(
TreePath
path)
```

Returns true if the node identified by the path has ever been
expanded.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the

path

has ever been expanded

- isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the node identified by the path is currently expanded,

**Parameters:** path

- the

TreePath

specifying the node to check
**Returns:** false if any of the nodes in the node's path are collapsed,
true if all nodes in the path are expanded

- isExpanded

```java
public boolean isExpanded​(int row)
```

Returns true if the node at the specified display row is currently
expanded.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently expanded, otherwise false

- isCollapsed

```java
public boolean isCollapsed​(
TreePath
path)
```

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

**Parameters:** path

- the

TreePath

to check
**Returns:** true if any of the nodes in the node's path are collapsed,
false if all nodes in the path are expanded

- isCollapsed

```java
public boolean isCollapsed​(int row)
```

Returns true if the node at the specified display row is collapsed.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently collapsed, otherwise false

- makeVisible

```java
public void makeVisible​(
TreePath
path)
```

Ensures that the node identified by path is currently viewable.

**Parameters:** path

- the

TreePath

to make visible

- isVisible

```java
public boolean isVisible​(
TreePath
path)
```

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.
Otherwise, this method returns false.

**Parameters:** path

-

TreePath

identifying a node
**Returns:** true if the node is viewable, otherwise false

- getPathBounds

```java
public
Rectangle
getPathBounds​(
TreePath
path)
```

Returns the

Rectangle

that the specified node will be drawn
into. Returns

null

if any component in the path is hidden
(under a collapsed parent).

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

the node is drawn in,
or

null

- getRowBounds

```java
public
Rectangle
getRowBounds​(int row)
```

Returns the

Rectangle

that the node at the specified row is
drawn in.

**Parameters:** row

- the row to be drawn, where 0 is the first row in the
display
**Returns:** the

Rectangle

the node is drawn in

- scrollPathToVisible

```java
public void scrollPathToVisible​(
TreePath
path)
```

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** path

- the

TreePath

identifying the node to
bring into view

- scrollRowToVisible

```java
public void scrollRowToVisible​(int row)
```

Scrolls the item identified by row until it is displayed. The minimum
of amount of scrolling necessary to bring the row into view
is performed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** row

- an integer specifying the row to scroll, where 0 is the
first row in the display

- getPathForRow

```java
@BeanProperty
(
bound
=false)
public
TreePath
getPathForRow​(int row)
```

Returns the path for the specified row. If

row

is
not visible, or a

TreeUI

has not been set,

null

is returned.

**Parameters:** row

- an integer specifying a row
**Returns:** the

TreePath

to the specified node,

null

if

row < 0

or

row >= getRowCount()

- getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that displays the node identified by the specified
path.

**Parameters:** path

- the

TreePath

identifying a node
**Returns:** an integer specifying the display row, where 0 is the first
row in the display, or -1 if any of the elements in path
are hidden under a collapsed parent.

- expandPath

```java
public void expandPath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
expanded and viewable. If the last item in the path is a
leaf, this will have no effect.

**Parameters:** path

- the

TreePath

identifying a node

- expandRow

```java
public void expandRow​(int row)
```

Ensures that the node in the specified row is expanded and
viewable.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

- collapsePath

```java
public void collapsePath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
collapsed and viewable.

**Parameters:** path

- the

TreePath

identifying a node

- collapseRow

```java
public void collapseRow​(int row)
```

Ensures that the node in the specified row is collapsed.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

- getPathForLocation

```java
public
TreePath
getPathForLocation​(int x,
int y)
```

Returns the path for the node at the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node at that location

- getRowForLocation

```java
public int getRowForLocation​(int x,
int y)
```

Returns the row for the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row corresponding to the location, or -1 if the
location is not within the bounds of a displayed cell
**See Also:** getClosestRowForLocation(int, int)

- getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
no nodes are currently viewable, or there is no model, returns

null

, otherwise it always returns a valid path. To test if
the node is exactly at x, y, get the node's bounds and
test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node closest to that location,

null

if nothing is viewable or there is no model
**See Also:** getPathForLocation(int, int)

,

getPathBounds(javax.swing.tree.TreePath)

- getClosestRowForLocation

```java
public int getClosestRowForLocation​(int x,
int y)
```

Returns the row to the node that is closest to x,y. If no nodes
are viewable or there is no model, returns -1. Otherwise,
it always returns a valid row. To test if the returned object is
exactly at x, y, get the bounds for the node at the returned
row and test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row closest to the location, -1 if nothing is
viewable or there is no model
**See Also:** getRowForLocation(int, int)

,

getRowBounds(int)

- isEditing

```java
@BeanProperty
(
bound
=false)
public boolean isEditing()
```

Returns true if the tree is being edited. The item that is being
edited can be obtained using

getSelectionPath

.

**Returns:** true if the user is currently editing a node
**See Also:** getSelectionPath()

- stopEditing

```java
public boolean stopEditing()
```

Ends the current editing session.
(The

DefaultTreeCellEditor

object saves any edits that are currently in progress on a cell.
Other implementations may operate differently.)
Has no effect if the tree isn't being edited.

Note:

To make edit-saves automatic whenever the user changes
their position in the tree, use

setInvokesStopCellEditing(boolean)

.

**Returns:** true if editing was in progress and is now stopped,
false if editing was not in progress

- cancelEditing

```java
public void cancelEditing()
```

Cancels the current editing session. Has no effect if the
tree isn't being edited.

- startEditingAtPath

```java
public void startEditingAtPath​(
TreePath
path)
```

Selects the node identified by the specified path and initiates
editing. The edit-attempt fails if the

CellEditor

does not allow
editing for the specified item.

**Parameters:** path

- the

TreePath

identifying a node

- getEditingPath

```java
@BeanProperty
(
bound
=false)
public
TreePath
getEditingPath()
```

Returns the path to the element that is currently being edited.

**Returns:** the

TreePath

for the node being edited

- setSelectionModel

```java
@BeanProperty
(
description
="The tree\'s selection model.")
public void setSelectionModel​(
TreeSelectionModel
selectionModel)
```

Sets the tree's selection model. When a

null

value is
specified an empty

selectionModel

is used, which does not allow selections.

This is a bound property.

**Parameters:** selectionModel

- the

TreeSelectionModel

to use,
or

null

to disable selections
**See Also:** TreeSelectionModel

- getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model for selections. This should always return a
non-

null

value. If you don't want to allow anything
to be selected
set the selection model to

null

, which forces an empty
selection model to be used.

**Returns:** the model for selections
**See Also:** setSelectionModel(javax.swing.tree.TreeSelectionModel)

- getPathBetweenRows

```java
protected
TreePath
[] getPathBetweenRows​(int index0,
int index1)
```

Returns the paths (inclusive) between the specified rows. If
the specified indices are within the viewable set of rows, or
bound the viewable set of rows, then the indices are
constrained by the viewable set of rows. If the specified
indices are not within the viewable set of rows, or do not
bound the viewable set of rows, then an empty array is
returned. For example, if the row count is

10

, and this
method is invoked with

-1, 20

, then the specified
indices are constrained to the viewable set of rows, and this is
treated as if invoked with

0, 9

. On the other hand, if
this were invoked with

-10, -1

, then the specified
indices do not bound the viewable set of rows, and an empty
array is returned.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

**Parameters:** index0

- the first index in the range
**Parameters:** index1

- the last index in the range
**Returns:** the paths (inclusive) between the specified row indices

- setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Selects the rows in the specified interval (inclusive). If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified rows are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is cleared. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified indices bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified indices do not
bound the viewable set of rows, and the selection is cleared.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to select
**Parameters:** index1

- the last index in the range to select

- addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Adds the specified rows (inclusive) to the selection. If the
specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are
constrained by the viewable set of rows. If the indices are not
within the viewable set of rows, or do not bound the viewable
set of rows, then the selection is unchanged. For example, if
the row count is

10

, and this method is invoked with

-1, 20

, then the specified indices bounds the viewable
range, and this is treated as if invoked with

0, 9

. On
the other hand, if this were invoked with

-10, -1

, then
the specified indices do not bound the viewable set of rows,
and the selection is unchanged.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to add to the selection
**Parameters:** index1

- the last index in the range to add to the selection

- removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Removes the specified rows (inclusive) from the selection. If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is unchanged. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified range bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified range does not
bound the viewable set of rows, and the selection is unchanged.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

**Parameters:** index0

- the first row to remove from the selection
**Parameters:** index1

- the last row to remove from the selection

- removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes the node identified by the specified path from the current
selection.

**Parameters:** path

- the

TreePath

identifying a node

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes the nodes identified by the specified paths from the
current selection.

**Parameters:** paths

- an array of

TreePath

objects that
specifies the nodes to remove

- removeSelectionRow

```java
public void removeSelectionRow​(int row)
```

Removes the row at the index

row

from the current
selection.

**Parameters:** row

- the row to remove

- removeSelectionRows

```java
public void removeSelectionRows​(int[] rows)
```

Removes the rows that are selected at each of the specified
rows.

**Parameters:** rows

- an array of ints specifying display rows, where 0 is
the first row in the display

- clearSelection

```java
public void clearSelection()
```

Clears the selection.

- isSelectionEmpty

```java
@BeanProperty
(
bound
=false)
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** true if the selection is currently empty

- addTreeExpansionListener

```java
public void addTreeExpansionListener​(
TreeExpansionListener
tel)
```

Adds a listener for

TreeExpansion

events.

**Parameters:** tel

- a TreeExpansionListener that will be notified when
a tree node is expanded or collapsed (a "negative
expansion")

- removeTreeExpansionListener

```java
public void removeTreeExpansionListener​(
TreeExpansionListener
tel)
```

Removes a listener for

TreeExpansion

events.

**Parameters:** tel

- the

TreeExpansionListener

to remove

- getTreeExpansionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeExpansionListener
[] getTreeExpansionListeners()
```

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

**Returns:** all of the

TreeExpansionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addTreeWillExpandListener

```java
public void addTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Adds a listener for

TreeWillExpand

events.

**Parameters:** tel

- a

TreeWillExpandListener

that will be notified
when a tree node will be expanded or collapsed (a "negative
expansion")

- removeTreeWillExpandListener

```java
public void removeTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Removes a listener for

TreeWillExpand

events.

**Parameters:** tel

- the

TreeWillExpandListener

to remove

- getTreeWillExpandListeners

```java
@BeanProperty
(
bound
=false)
public
TreeWillExpandListener
[] getTreeWillExpandListeners()
```

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

**Returns:** all of the

TreeWillExpandListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireTreeExpanded

```java
public void fireTreeExpanded​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**See Also:** EventListenerList

- fireTreeCollapsed

```java
public void fireTreeCollapsed​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
collapsed
**See Also:** EventListenerList

- fireTreeWillExpand

```java
public void fireTreeWillExpand​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the expansion is prevented from occurring
**See Also:** EventListenerList

- fireTreeWillCollapse

```java
public void fireTreeWillCollapse​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the collapse is prevented from occurring
**See Also:** EventListenerList

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Adds a listener for

TreeSelection

events.

**Parameters:** tsl

- the

TreeSelectionListener

that will be notified
when a node is selected or deselected (a "negative
selection")

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Removes a

TreeSelection

listener.

**Parameters:** tsl

- the

TreeSelectionListener

to remove

- getTreeSelectionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

**Returns:** all of the

TreeSelectionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

TreeSelectionEvent

to be fired;
generated by the

TreeSelectionModel

when a node is selected or deselected
**See Also:** EventListenerList

- treeDidChange

```java
public void treeDidChange()
```

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree). You should never have to
invoke this, the UI will invoke this as it needs to.

- setVisibleRowCount

```java
@BeanProperty
(
description
="The number of rows that are to be displayed.")
public void setVisibleRowCount​(int newCount)
```

Sets the number of rows that are to be displayed.
This will only work if the tree is contained in a

JScrollPane

,
and will adjust the preferred size and size of that scrollpane.

This is a bound property.

**Parameters:** newCount

- the number of rows to display

- getVisibleRowCount

```java
public int getVisibleRowCount()
```

Returns the number of rows that are displayed in the display area.

**Returns:** the number of rows displayed

- getNextMatch

```java
public
TreePath
getNextMatch​(
String
prefix,
int startingRow,

Position.Bias
bias)
```

Returns the TreePath to the next tree element that
begins with a prefix. To handle the conversion of a

TreePath

into a String,

convertValueToText

is used.

**Parameters:** prefix

- the string to test for a match
**Parameters:** startingRow

- the row for starting the search
**Parameters:** bias

- the search direction, either
Position.Bias.Forward or Position.Bias.Backward.
**Returns:** the TreePath of the next tree element that
starts with the prefix; otherwise null
**Throws:** IllegalArgumentException

- if prefix is null
or startingRow is out of bounds
**Since:** 1.4

- getPreferredScrollableViewportSize

```java
@BeanProperty
(
bound
=false)
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred display size of a

JTree

. The height is
determined from

getVisibleRowCount

and the width
is the current preferred width.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** a

Dimension

object containing the preferred size
**See Also:** JComponent.getPreferredSize()

- getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount to increment when scrolling. The amount is
the height of the first displayed row that isn't completely in view
or, if it is totally displayed, the height of the next row in the
scrolling direction.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right
**Returns:** the "unit" increment for scrolling in the specified direction
**See Also:** JScrollBar.setUnitIncrement(int)

- getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** JScrollBar.setBlockIncrement(int)

- getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the tree should track the width of the viewport
**See Also:** Scrollable.getScrollableTracksViewportWidth()

- getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the tree should track the height of the viewport
**See Also:** Scrollable.getScrollableTracksViewportHeight()

- setExpandedState

```java
protected void setExpandedState​(
TreePath
path,
boolean state)
```

Sets the expanded state of this

JTree

.
If

state

is
true, all parents of

path

and path are marked as
expanded. If

state

is false, all parents of

path

are marked EXPANDED, but

path

itself
is marked collapsed.

This will fail if a

TreeWillExpandListener

vetos it.

**Parameters:** path

- a

TreePath

identifying a node
**Parameters:** state

- if

true

, all parents of @{code path} and path are marked as expanded.
Otherwise, all parents of

path

are marked EXPANDED,
but

path

itself is marked collapsed.

- getDescendantToggledPaths

```java
protected
Enumeration
<
TreePath
> getDescendantToggledPaths​(
TreePath
parent)
```

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

**Parameters:** parent

- a path
**Returns:** the

Enumeration

of

TreePaths

- removeDescendantToggledPaths

```java
protected void removeDescendantToggledPaths​(
Enumeration
<
TreePath
> toRemove)
```

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

**Parameters:** toRemove

- an enumeration of the paths to remove; a value of

null

is ignored
**Throws:** ClassCastException

- if

toRemove

contains an
element that is not a

TreePath

;

null

values are ignored

- clearToggledPaths

```java
protected void clearToggledPaths()
```

Clears the cache of toggled tree paths. This does NOT send out
any

TreeExpansionListener

events.

- createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Creates and returns an instance of

TreeModelHandler

.
The returned
object is responsible for updating the expanded state when the

TreeModel

changes.

For more information on what expanded state means, see the

JTree description

above.

**Returns:** the instance of

TreeModelHandler

- removeDescendantSelectedPaths

```java
protected boolean removeDescendantSelectedPaths​(
TreePath
path,
boolean includePath)
```

Removes any paths in the selection that are descendants of

path

. If

includePath

is true and

path

is selected, it will be removed from the selection.

**Parameters:** path

- a path
**Parameters:** includePath

- is

true

and

path

is selected,
it will be removed from the selection.
**Returns:** true if a descendant was selected
**Since:** 1.3

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTree

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTree

.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTree.
For JTrees, the AccessibleContext takes the form of an
AccessibleJTree.
A new AccessibleJTree instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTree that serves as the
AccessibleContext of this JTree

---

#### Method Detail

getDefaultTreeModel

```java
protected static
TreeModel
getDefaultTreeModel()
```

Creates and returns a sample

TreeModel

.
Used primarily for beanbuilders to show something interesting.

**Returns:** the default

TreeModel

---

#### getDefaultTreeModel

protected static

TreeModel

getDefaultTreeModel()

Creates and returns a sample

TreeModel

.
Used primarily for beanbuilders to show something interesting.

createTreeModel

```java
protected static
TreeModel
createTreeModel​(
Object
value)
```

Returns a

TreeModel

wrapping the specified object.
If the object is:

- an array of

Object

s,

a

Hashtable

, or

a

Vector

then a new root node is created with each of the incoming
objects as children. Otherwise, a new root is created with
a value of

"root"

.

**Parameters:** value

- the

Object

used as the foundation for
the

TreeModel
**Returns:** a

TreeModel

wrapping the specified object

---

#### createTreeModel

protected static

TreeModel

createTreeModel​(

Object

value)

Returns a

TreeModel

wrapping the specified object.
If the object is:

- an array of

Object

s,

a

Hashtable

, or

a

Vector

then a new root node is created with each of the incoming
objects as children. Otherwise, a new root is created with
a value of

"root"

.

an array of

Object

s,

a

Hashtable

, or

a

Vector

getUI

```java
public
TreeUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TreeUI

object that renders this component

---

#### getUI

public

TreeUI

getUI()

Returns the L&F object that renders this component.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
TreeUI
ui)
```

Sets the L&F object that renders this component.

This is a bound property.

**Parameters:** ui

- the

TreeUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

TreeUI

ui)

Sets the L&F object that renders this component.

This is a bound property.

This is a bound property.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Notification from the

UIManager

that the L&F has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getUIClassID

```java
@BeanProperty
(
bound
=false)
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TreeUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false)
public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

getCellRenderer

```java
public
TreeCellRenderer
getCellRenderer()
```

Returns the current

TreeCellRenderer

that is rendering each cell.

**Returns:** the

TreeCellRenderer

that is rendering each cell

---

#### getCellRenderer

public

TreeCellRenderer

getCellRenderer()

Returns the current

TreeCellRenderer

that is rendering each cell.

setCellRenderer

```java
@BeanProperty
(
description
="The TreeCellRenderer that will be used to draw each cell.")
public void setCellRenderer​(
TreeCellRenderer
x)
```

Sets the

TreeCellRenderer

that will be used to
draw each cell.

This is a bound property.

**Parameters:** x

- the

TreeCellRenderer

that is to render each cell

---

#### setCellRenderer

@BeanProperty

(

description

="The TreeCellRenderer that will be used to draw each cell.")
public void setCellRenderer​(

TreeCellRenderer

x)

Sets the

TreeCellRenderer

that will be used to
draw each cell.

This is a bound property.

This is a bound property.

setEditable

```java
@BeanProperty
(
description
="Whether the tree is editable.")
public void setEditable​(boolean flag)
```

Determines whether the tree is editable. Fires a property
change event if the new setting is different from the existing
setting.

This is a bound property.

**Parameters:** flag

- a boolean value, true if the tree is editable

---

#### setEditable

@BeanProperty

(

description

="Whether the tree is editable.")
public void setEditable​(boolean flag)

Determines whether the tree is editable. Fires a property
change event if the new setting is different from the existing
setting.

This is a bound property.

This is a bound property.

isEditable

```java
public boolean isEditable()
```

Returns true if the tree is editable.

**Returns:** true if the tree is editable

---

#### isEditable

public boolean isEditable()

Returns true if the tree is editable.

setCellEditor

```java
@BeanProperty
(
description
="The cell editor. A null value implies the tree cannot be edited.")
public void setCellEditor​(
TreeCellEditor
cellEditor)
```

Sets the cell editor. A

null

value implies that the
tree cannot be edited. If this represents a change in the

cellEditor

, the

propertyChange

method is invoked on all listeners.

This is a bound property.

**Parameters:** cellEditor

- the

TreeCellEditor

to use

---

#### setCellEditor

@BeanProperty

(

description

="The cell editor. A null value implies the tree cannot be edited.")
public void setCellEditor​(

TreeCellEditor

cellEditor)

Sets the cell editor. A

null

value implies that the
tree cannot be edited. If this represents a change in the

cellEditor

, the

propertyChange

method is invoked on all listeners.

This is a bound property.

This is a bound property.

getCellEditor

```java
public
TreeCellEditor
getCellEditor()
```

Returns the editor used to edit entries in the tree.

**Returns:** the

TreeCellEditor

in use,
or

null

if the tree cannot be edited

---

#### getCellEditor

public

TreeCellEditor

getCellEditor()

Returns the editor used to edit entries in the tree.

getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

---

#### getModel

public

TreeModel

getModel()

Returns the

TreeModel

that is providing the data.

setModel

```java
@BeanProperty
(
description
="The TreeModel that will provide the data.")
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

This is a bound property.

**Parameters:** newModel

- the

TreeModel

that is to provide the data

---

#### setModel

@BeanProperty

(

description

="The TreeModel that will provide the data.")
public void setModel​(

TreeModel

newModel)

Sets the

TreeModel

that will provide the data.

This is a bound property.

This is a bound property.

isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

---

#### isRootVisible

public boolean isRootVisible()

Returns true if the root node of the tree is displayed.

setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

This is a bound property.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

---

#### setRootVisible

@BeanProperty

(

description

="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

This is a bound property.

This is a bound property.

setShowsRootHandles

```java
@BeanProperty
(
description
="Whether the node handles are to be displayed.")
public void setShowsRootHandles​(boolean newValue)
```

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.
The default value of this property depends on the constructor
used to create the

JTree

.
Some look and feels might not support handles;
they will ignore this property.

This is a bound property.

**Parameters:** newValue

-

true

if root handles should be displayed;
otherwise,

false
**See Also:** showsRootHandles

,

getShowsRootHandles()

---

#### setShowsRootHandles

@BeanProperty

(

description

="Whether the node handles are to be displayed.")
public void setShowsRootHandles​(boolean newValue)

Sets the value of the

showsRootHandles

property,
which specifies whether the node handles should be displayed.
The default value of this property depends on the constructor
used to create the

JTree

.
Some look and feels might not support handles;
they will ignore this property.

This is a bound property.

This is a bound property.

getShowsRootHandles

```java
public boolean getShowsRootHandles()
```

Returns the value of the

showsRootHandles

property.

**Returns:** the value of the

showsRootHandles

property
**See Also:** showsRootHandles

---

#### getShowsRootHandles

public boolean getShowsRootHandles()

Returns the value of the

showsRootHandles

property.

setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell, in pixels. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

This is a bound property.

**Parameters:** rowHeight

- the height of each cell, in pixels

---

#### setRowHeight

@BeanProperty

(

description

="The height of each cell.")
public void setRowHeight​(int rowHeight)

Sets the height of each cell, in pixels. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

This is a bound property.

This is a bound property.

getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

---

#### getRowHeight

public int getRowHeight()

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

isFixedRowHeight

```java
@BeanProperty
(
bound
=false)
public boolean isFixedRowHeight()
```

Returns true if the height of each display row is a fixed size.

**Returns:** true if the height of each row is a fixed size

---

#### isFixedRowHeight

@BeanProperty

(

bound

=false)
public boolean isFixedRowHeight()

Returns true if the height of each display row is a fixed size.

setLargeModel

```java
@BeanProperty
(
description
="Whether the UI should use a large model.")
public void setLargeModel​(boolean newValue)
```

Specifies whether the UI should use a large model.
(Not all UIs will implement this.) Fires a property change
for the LARGE_MODEL_PROPERTY.

This is a bound property.

**Parameters:** newValue

- true to suggest a large model to the UI
**See Also:** largeModel

---

#### setLargeModel

@BeanProperty

(

description

="Whether the UI should use a large model.")
public void setLargeModel​(boolean newValue)

Specifies whether the UI should use a large model.
(Not all UIs will implement this.) Fires a property change
for the LARGE_MODEL_PROPERTY.

This is a bound property.

This is a bound property.

isLargeModel

```java
public boolean isLargeModel()
```

Returns true if the tree is configured for a large model.

**Returns:** true if a large model is suggested
**See Also:** largeModel

---

#### isLargeModel

public boolean isLargeModel()

Returns true if the tree is configured for a large model.

setInvokesStopCellEditing

```java
@BeanProperty
(
description
="Determines what happens when editing is interrupted, selecting another node in the tree, a change in the tree\'s data, or some other means.")
public void setInvokesStopCellEditing​(boolean newValue)
```

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means. Setting this property to

true

causes the
changes to be automatically saved when editing is interrupted.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

**Parameters:** newValue

- true means that

stopCellEditing

is invoked
when editing is interrupted, and data is saved; false means that

cancelCellEditing

is invoked, and changes are lost

---

#### setInvokesStopCellEditing

@BeanProperty

(

description

="Determines what happens when editing is interrupted, selecting another node in the tree, a change in the tree\'s data, or some other means.")
public void setInvokesStopCellEditing​(boolean newValue)

Determines what happens when editing is interrupted by selecting
another node in the tree, a change in the tree's data, or by some
other means. Setting this property to

true

causes the
changes to be automatically saved when editing is interrupted.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

Fires a property change for the INVOKES_STOP_CELL_EDITING_PROPERTY.

getInvokesStopCellEditing

```java
public boolean getInvokesStopCellEditing()
```

Returns the indicator that tells what happens when editing is
interrupted.

**Returns:** the indicator that tells what happens when editing is
interrupted
**See Also:** setInvokesStopCellEditing(boolean)

---

#### getInvokesStopCellEditing

public boolean getInvokesStopCellEditing()

Returns the indicator that tells what happens when editing is
interrupted.

setScrollsOnExpand

```java
@BeanProperty
(
description
="Indicates if a node descendant should be scrolled when expanded.")
public void setScrollsOnExpand​(boolean newValue)
```

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.
If this property is

true

(the default),
when a node expands
the tree can use scrolling to make
the maximum possible number of the node's descendants visible.
In some look and feels, trees might not need to scroll when expanded;
those look and feels will ignore this property.

This is a bound property.

**Parameters:** newValue

-

false

to disable scrolling on expansion;

true

to enable it
**See Also:** getScrollsOnExpand()

---

#### setScrollsOnExpand

@BeanProperty

(

description

="Indicates if a node descendant should be scrolled when expanded.")
public void setScrollsOnExpand​(boolean newValue)

Sets the

scrollsOnExpand

property,
which determines whether the
tree might scroll to show previously hidden children.
If this property is

true

(the default),
when a node expands
the tree can use scrolling to make
the maximum possible number of the node's descendants visible.
In some look and feels, trees might not need to scroll when expanded;
those look and feels will ignore this property.

This is a bound property.

This is a bound property.

getScrollsOnExpand

```java
public boolean getScrollsOnExpand()
```

Returns the value of the

scrollsOnExpand

property.

**Returns:** the value of the

scrollsOnExpand

property

---

#### getScrollsOnExpand

public boolean getScrollsOnExpand()

Returns the value of the

scrollsOnExpand

property.

setToggleClickCount

```java
@BeanProperty
(
description
="Number of clicks before a node will expand/collapse.")
public void setToggleClickCount​(int clickCount)
```

Sets the number of mouse clicks before a node will expand or close.
The default is two.

This is a bound property.

**Parameters:** clickCount

- the number of mouse clicks to get a node expanded or closed
**Since:** 1.3

---

#### setToggleClickCount

@BeanProperty

(

description

="Number of clicks before a node will expand/collapse.")
public void setToggleClickCount​(int clickCount)

Sets the number of mouse clicks before a node will expand or close.
The default is two.

This is a bound property.

This is a bound property.

getToggleClickCount

```java
public int getToggleClickCount()
```

Returns the number of mouse clicks needed to expand or close a node.

**Returns:** number of mouse clicks before node is expanded
**Since:** 1.3

---

#### getToggleClickCount

public int getToggleClickCount()

Returns the number of mouse clicks needed to expand or close a node.

setExpandsSelectedPaths

```java
@BeanProperty
(
description
="Indicates whether changes to the selection should make the parent of the path visible.")
public void setExpandsSelectedPaths​(boolean newValue)
```

Configures the

expandsSelectedPaths

property. If
true, any time the selection is changed, either via the

TreeSelectionModel

, or the cover methods provided by

JTree

, the

TreePath

s parents will be
expanded to make them visible (visible meaning the parent path is
expanded, not necessarily in the visible rectangle of the

JTree

). If false, when the selection
changes the nodes parent is not made visible (all its parents expanded).
This is useful if you wish to have your selection model maintain paths
that are not always visible (all parents expanded).

This is a bound property.

**Parameters:** newValue

- the new value for

expandsSelectedPaths
**Since:** 1.3

---

#### setExpandsSelectedPaths

@BeanProperty

(

description

="Indicates whether changes to the selection should make the parent of the path visible.")
public void setExpandsSelectedPaths​(boolean newValue)

Configures the

expandsSelectedPaths

property. If
true, any time the selection is changed, either via the

TreeSelectionModel

, or the cover methods provided by

JTree

, the

TreePath

s parents will be
expanded to make them visible (visible meaning the parent path is
expanded, not necessarily in the visible rectangle of the

JTree

). If false, when the selection
changes the nodes parent is not made visible (all its parents expanded).
This is useful if you wish to have your selection model maintain paths
that are not always visible (all parents expanded).

This is a bound property.

This is a bound property.

getExpandsSelectedPaths

```java
public boolean getExpandsSelectedPaths()
```

Returns the

expandsSelectedPaths

property.

**Returns:** true if selection changes result in the parent path being
expanded
**Since:** 1.3
**See Also:** setExpandsSelectedPaths(boolean)

---

#### getExpandsSelectedPaths

public boolean getExpandsSelectedPaths()

Returns the

expandsSelectedPaths

property.

setDragEnabled

```java
@BeanProperty
(
bound
=false,

description
="determines whether automatic drag handling is enabled")
public void setDragEnabled​(boolean b)
```

Turns on or off automatic drag handling. In order to enable automatic
drag handling, this property should be set to

true

, and the
tree's

TransferHandler

needs to be

non-null

.
The default value of the

dragEnabled

property is

false

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

**Parameters:** b

- whether or not to enable automatic drag handling
**Throws:** HeadlessException

- if

b

is

true

and

GraphicsEnvironment.isHeadless()

returns

true
**Since:** 1.4
**See Also:** GraphicsEnvironment.isHeadless()

,

getDragEnabled()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

---

#### setDragEnabled

@BeanProperty

(

bound

=false,

description

="determines whether automatic drag handling is enabled")
public void setDragEnabled​(boolean b)

Turns on or off automatic drag handling. In order to enable automatic
drag handling, this property should be set to

true

, and the
tree's

TransferHandler

needs to be

non-null

.
The default value of the

dragEnabled

property is

false

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

The job of honoring this property, and recognizing a user drag gesture,
lies with the look and feel implementation, and in particular, the tree's

TreeUI

. When automatic drag handling is enabled, most look and
feels (including those that subclass

BasicLookAndFeel

) begin a
drag and drop operation whenever the user presses the mouse button over
an item and then moves the mouse a few pixels. Setting this property to

true

can therefore have a subtle effect on how selections behave.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

If a look and feel is used that ignores this property, you can still
begin a drag and drop operation by calling

exportAsDrag

on the
tree's

TransferHandler

.

getDragEnabled

```java
public boolean getDragEnabled()
```

Returns whether or not automatic drag handling is enabled.

**Returns:** the value of the

dragEnabled

property
**Since:** 1.4
**See Also:** setDragEnabled(boolean)

---

#### getDragEnabled

public boolean getDragEnabled()

Returns whether or not automatic drag handling is enabled.

setDropMode

```java
public final void setDropMode​(
DropMode
dropMode)
```

Sets the drop mode for this component. For backward compatibility,
the default for this property is

DropMode.USE_SELECTION

.
Usage of one of the other modes is recommended, however, for an
improved user experience.

DropMode.ON

, for instance,
offers similar behavior of showing items as selected, but does so without
affecting the actual selection in the tree.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

**Parameters:** dropMode

- the drop mode to use
**Throws:** IllegalArgumentException

- if the drop mode is unsupported
or

null
**Since:** 1.6
**See Also:** getDropMode()

,

getDropLocation()

,

JComponent.setTransferHandler(javax.swing.TransferHandler)

,

TransferHandler

---

#### setDropMode

public final void setDropMode​(

DropMode

dropMode)

Sets the drop mode for this component. For backward compatibility,
the default for this property is

DropMode.USE_SELECTION

.
Usage of one of the other modes is recommended, however, for an
improved user experience.

DropMode.ON

, for instance,
offers similar behavior of showing items as selected, but does so without
affecting the actual selection in the tree.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

JTree

supports the following drop modes:

- DropMode.USE_SELECTION
- DropMode.ON
- DropMode.INSERT
- DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

DropMode.USE_SELECTION

DropMode.ON

DropMode.INSERT

DropMode.ON_OR_INSERT

The drop mode is only meaningful if this component has a

TransferHandler

that accepts drops.

getDropMode

```java
public final
DropMode
getDropMode()
```

Returns the drop mode for this component.

**Returns:** the drop mode for this component
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

---

#### getDropMode

public final

DropMode

getDropMode()

Returns the drop mode for this component.

getDropLocation

```java
@BeanProperty
(
bound
=false)
public final
JTree.DropLocation
getDropLocation()
```

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

**Returns:** the drop location
**Since:** 1.6
**See Also:** setDropMode(javax.swing.DropMode)

,

TransferHandler.canImport(TransferHandler.TransferSupport)

---

#### getDropLocation

@BeanProperty

(

bound

=false)
public final

JTree.DropLocation

getDropLocation()

Returns the location that this component should visually indicate
as the drop location during a DnD operation over the component,
or

null

if no location is to currently be shown.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

This method is not meant for querying the drop location
from a

TransferHandler

, as the drop location is only
set after the

TransferHandler

's

canImport

has returned and has allowed for the location to be shown.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

When this property changes, a property change event with
name "dropLocation" is fired by the component.

isPathEditable

```java
public boolean isPathEditable​(
TreePath
path)
```

Returns

isEditable

. This is invoked from the UI before
editing begins to insure that the given path can be edited. This
is provided as an entry point for subclassers to add filtered
editing without having to resort to creating a new editor.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if every parent node and the node itself is editable
**See Also:** isEditable()

---

#### isPathEditable

public boolean isPathEditable​(

TreePath

path)

Returns

isEditable

. This is invoked from the UI before
editing begins to insure that the given path can be edited. This
is provided as an entry point for subclassers to add filtered
editing without having to resort to creating a new editor.

getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the

MouseEvent

that initiated the

ToolTip

display
**Returns:** a string containing the tooltip or

null

if

event

is null

---

#### getToolTipText

public

String

getToolTipText​(

MouseEvent

event)

Overrides

JComponent

's

getToolTipText

method in order to allow
renderer's tips to be used if it has text set.

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

NOTE: For

JTree

to properly display tooltips of its
renderers,

JTree

must be a registered component with the

ToolTipManager

. This can be done by invoking

ToolTipManager.sharedInstance().registerComponent(tree)

.
This is not done automatically!

convertValueToText

```java
public
String
convertValueToText​(
Object
value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)
```

Called by the renderers to convert the specified value to
text. This implementation returns

value.toString

, ignoring
all other arguments. To control the conversion, subclass this
method and use any of the arguments you need.

**Parameters:** value

- the

Object

to convert to text
**Parameters:** selected

- true if the node is selected
**Parameters:** expanded

- true if the node is expanded
**Parameters:** leaf

- true if the node is a leaf node
**Parameters:** row

- an integer specifying the node's display row, where 0 is
the first row in the display
**Parameters:** hasFocus

- true if the node has the focus
**Returns:** the

String

representation of the node's value

---

#### convertValueToText

public

String

convertValueToText​(

Object

value,
boolean selected,
boolean expanded,
boolean leaf,
int row,
boolean hasFocus)

Called by the renderers to convert the specified value to
text. This implementation returns

value.toString

, ignoring
all other arguments. To control the conversion, subclass this
method and use any of the arguments you need.

getRowCount

```java
@BeanProperty
(
bound
=false)
public int getRowCount()
```

Returns the number of viewable nodes. A node is viewable if all of its
parents are expanded. The root is only included in this count if

isRootVisible()

is

true

. This returns

0

if
the UI has not been set.

**Returns:** the number of viewable nodes

---

#### getRowCount

@BeanProperty

(

bound

=false)
public int getRowCount()

Returns the number of viewable nodes. A node is viewable if all of its
parents are expanded. The root is only included in this count if

isRootVisible()

is

true

. This returns

0

if
the UI has not been set.

setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Selects the node identified by the specified path. If any
component of the path is hidden (under a collapsed node), and

getExpandsSelectedPaths

is true it is
exposed (made viewable).

**Parameters:** path

- the

TreePath

specifying the node to select

---

#### setSelectionPath

public void setSelectionPath​(

TreePath

path)

Selects the node identified by the specified path. If any
component of the path is hidden (under a collapsed node), and

getExpandsSelectedPaths

is true it is
exposed (made viewable).

setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] paths)
```

Selects the nodes identified by the specified array of paths.
If any component in any of the paths is hidden (under a collapsed
node), and

getExpandsSelectedPaths

is true
it is exposed (made viewable).

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to select

---

#### setSelectionPaths

public void setSelectionPaths​(

TreePath

[] paths)

Selects the nodes identified by the specified array of paths.
If any component in any of the paths is hidden (under a collapsed
node), and

getExpandsSelectedPaths

is true
it is exposed (made viewable).

setLeadSelectionPath

```java
@BeanProperty
(
description
="Lead selection path")
public void setLeadSelectionPath​(
TreePath
newPath)
```

Sets the path identifies as the lead. The lead may not be selected.
The lead is not maintained by

JTree

,
rather the UI will update it.

This is a bound property.

**Parameters:** newPath

- the new lead path
**Since:** 1.3

---

#### setLeadSelectionPath

@BeanProperty

(

description

="Lead selection path")
public void setLeadSelectionPath​(

TreePath

newPath)

Sets the path identifies as the lead. The lead may not be selected.
The lead is not maintained by

JTree

,
rather the UI will update it.

This is a bound property.

This is a bound property.

setAnchorSelectionPath

```java
@BeanProperty
(
description
="Anchor selection path")
public void setAnchorSelectionPath​(
TreePath
newPath)
```

Sets the path identified as the anchor.
The anchor is not maintained by

JTree

, rather the UI will
update it.

This is a bound property.

**Parameters:** newPath

- the new anchor path
**Since:** 1.3

---

#### setAnchorSelectionPath

@BeanProperty

(

description

="Anchor selection path")
public void setAnchorSelectionPath​(

TreePath

newPath)

Sets the path identified as the anchor.
The anchor is not maintained by

JTree

, rather the UI will
update it.

This is a bound property.

This is a bound property.

setSelectionRow

```java
public void setSelectionRow​(int row)
```

Selects the node at the specified row in the display.

**Parameters:** row

- the row to select, where 0 is the first row in
the display

---

#### setSelectionRow

public void setSelectionRow​(int row)

Selects the node at the specified row in the display.

setSelectionRows

```java
public void setSelectionRows​(int[] rows)
```

Selects the nodes corresponding to each of the specified rows
in the display. If a particular element of

rows

is
< 0 or >=

getRowCount

, it will be ignored.
If none of the elements
in

rows

are valid rows, the selection will
be cleared. That is it will be as if

clearSelection

was invoked.

**Parameters:** rows

- an array of ints specifying the rows to select,
where 0 indicates the first row in the display

---

#### setSelectionRows

public void setSelectionRows​(int[] rows)

Selects the nodes corresponding to each of the specified rows
in the display. If a particular element of

rows

is
< 0 or >=

getRowCount

, it will be ignored.
If none of the elements
in

rows

are valid rows, the selection will
be cleared. That is it will be as if

clearSelection

was invoked.

addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds the node identified by the specified

TreePath

to the current selection. If any component of the path isn't
viewable, and

getExpandsSelectedPaths

is true it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** path

- the

TreePath

to add

---

#### addSelectionPath

public void addSelectionPath​(

TreePath

path)

Adds the node identified by the specified

TreePath

to the current selection. If any component of the path isn't
viewable, and

getExpandsSelectedPaths

is true it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds each path in the array of paths to the current selection. If
any component of any of the paths isn't viewable and

getExpandsSelectedPaths

is true, it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

**Parameters:** paths

- an array of

TreePath

objects that specifies
the nodes to add

---

#### addSelectionPaths

public void addSelectionPaths​(

TreePath

[] paths)

Adds each path in the array of paths to the current selection. If
any component of any of the paths isn't viewable and

getExpandsSelectedPaths

is true, it is
made viewable.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

Note that

JTree

does not allow duplicate nodes to
exist as children under the same parent -- each sibling must be
a unique object.

addSelectionRow

```java
public void addSelectionRow​(int row)
```

Adds the path at the specified row to the current selection.

**Parameters:** row

- an integer specifying the row of the node to add,
where 0 is the first row in the display

---

#### addSelectionRow

public void addSelectionRow​(int row)

Adds the path at the specified row to the current selection.

addSelectionRows

```java
public void addSelectionRows​(int[] rows)
```

Adds the paths at each of the specified rows to the current selection.

**Parameters:** rows

- an array of ints specifying the rows to add,
where 0 indicates the first row in the display

---

#### addSelectionRows

public void addSelectionRows​(int[] rows)

Adds the paths at each of the specified rows to the current selection.

getLastSelectedPathComponent

```java
@BeanProperty
(
bound
=false)
public
Object
getLastSelectedPathComponent()
```

Returns the last path component of the selected path. This is
a convenience method for

getSelectionModel().getSelectionPath().getLastPathComponent()

.
This is typically only useful if the selection has one path.

**Returns:** the last path component of the selected path, or

null

if nothing is selected
**See Also:** TreePath.getLastPathComponent()

---

#### getLastSelectedPathComponent

@BeanProperty

(

bound

=false)
public

Object

getLastSelectedPathComponent()

Returns the last path component of the selected path. This is
a convenience method for

getSelectionModel().getSelectionPath().getLastPathComponent()

.
This is typically only useful if the selection has one path.

getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the path identified as the lead.

**Returns:** path identified as the lead

---

#### getLeadSelectionPath

public

TreePath

getLeadSelectionPath()

Returns the path identified as the lead.

getAnchorSelectionPath

```java
public
TreePath
getAnchorSelectionPath()
```

Returns the path identified as the anchor.

**Returns:** path identified as the anchor
**Since:** 1.3

---

#### getAnchorSelectionPath

public

TreePath

getAnchorSelectionPath()

Returns the path identified as the anchor.

getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the path to the first selected node.

**Returns:** the

TreePath

for the first selected node,
or

null

if nothing is currently selected

---

#### getSelectionPath

public

TreePath

getSelectionPath()

Returns the path to the first selected node.

getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the paths of all selected values.

**Returns:** an array of

TreePath

objects indicating the selected
nodes, or

null

if nothing is currently selected

---

#### getSelectionPaths

public

TreePath

[] getSelectionPaths()

Returns the paths of all selected values.

getSelectionRows

```java
public int[] getSelectionRows()
```

Returns all of the currently selected rows. This method is simply
forwarded to the

TreeSelectionModel

.
If nothing is selected

null

or an empty array will
be returned, based on the

TreeSelectionModel

implementation.

**Returns:** an array of integers that identifies all currently selected rows
where 0 is the first row in the display

---

#### getSelectionRows

public int[] getSelectionRows()

Returns all of the currently selected rows. This method is simply
forwarded to the

TreeSelectionModel

.
If nothing is selected

null

or an empty array will
be returned, based on the

TreeSelectionModel

implementation.

getSelectionCount

```java
@BeanProperty
(
bound
=false)
public int getSelectionCount()
```

Returns the number of nodes selected.

**Returns:** the number of nodes selected

---

#### getSelectionCount

@BeanProperty

(

bound

=false)
public int getSelectionCount()

Returns the number of nodes selected.

getMinSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMinSelectionRow()
```

Returns the smallest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the smallest selected row

---

#### getMinSelectionRow

@BeanProperty

(

bound

=false)
public int getMinSelectionRow()

Returns the smallest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

getMaxSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getMaxSelectionRow()
```

Returns the largest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

**Returns:** the largest selected row

---

#### getMaxSelectionRow

@BeanProperty

(

bound

=false)
public int getMaxSelectionRow()

Returns the largest selected row. If the selection is empty, or
none of the selected paths are viewable,

-1

is returned.

getLeadSelectionRow

```java
@BeanProperty
(
bound
=false)
public int getLeadSelectionRow()
```

Returns the row index corresponding to the lead path.

**Returns:** an integer giving the row index of the lead path,
where 0 is the first row in the display; or -1
if

leadPath

is

null

---

#### getLeadSelectionRow

@BeanProperty

(

bound

=false)
public int getLeadSelectionRow()

Returns the row index corresponding to the lead path.

isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the item identified by the path is currently selected.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the node is selected

---

#### isPathSelected

public boolean isPathSelected​(

TreePath

path)

Returns true if the item identified by the path is currently selected.

isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the node identified by row is selected.

**Parameters:** row

- an integer specifying a display row, where 0 is the first
row in the display
**Returns:** true if the node is selected

---

#### isRowSelected

public boolean isRowSelected​(int row)

Returns true if the node identified by row is selected.

getExpandedDescendants

```java
public
Enumeration
<
TreePath
> getExpandedDescendants​(
TreePath
parent)
```

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded. If

parent

is not currently
expanded, this will return

null

.
If you expand/collapse nodes while
iterating over the returned

Enumeration

this may not return all
the expanded paths, or may return paths that are no longer expanded.

**Parameters:** parent

- the path which is to be examined
**Returns:** an

Enumeration

of the descendents of

parent

, or

null

if

parent

is not currently expanded

---

#### getExpandedDescendants

public

Enumeration

<

TreePath

> getExpandedDescendants​(

TreePath

parent)

Returns an

Enumeration

of the descendants of the
path

parent

that
are currently expanded. If

parent

is not currently
expanded, this will return

null

.
If you expand/collapse nodes while
iterating over the returned

Enumeration

this may not return all
the expanded paths, or may return paths that are no longer expanded.

hasBeenExpanded

```java
public boolean hasBeenExpanded​(
TreePath
path)
```

Returns true if the node identified by the path has ever been
expanded.

**Parameters:** path

- a

TreePath

identifying a node
**Returns:** true if the

path

has ever been expanded

---

#### hasBeenExpanded

public boolean hasBeenExpanded​(

TreePath

path)

Returns true if the node identified by the path has ever been
expanded.

isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the node identified by the path is currently expanded,

**Parameters:** path

- the

TreePath

specifying the node to check
**Returns:** false if any of the nodes in the node's path are collapsed,
true if all nodes in the path are expanded

---

#### isExpanded

public boolean isExpanded​(

TreePath

path)

Returns true if the node identified by the path is currently expanded,

isExpanded

```java
public boolean isExpanded​(int row)
```

Returns true if the node at the specified display row is currently
expanded.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently expanded, otherwise false

---

#### isExpanded

public boolean isExpanded​(int row)

Returns true if the node at the specified display row is currently
expanded.

isCollapsed

```java
public boolean isCollapsed​(
TreePath
path)
```

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

**Parameters:** path

- the

TreePath

to check
**Returns:** true if any of the nodes in the node's path are collapsed,
false if all nodes in the path are expanded

---

#### isCollapsed

public boolean isCollapsed​(

TreePath

path)

Returns true if the value identified by path is currently collapsed,
this will return false if any of the values in path are currently
not being displayed.

isCollapsed

```java
public boolean isCollapsed​(int row)
```

Returns true if the node at the specified display row is collapsed.

**Parameters:** row

- the row to check, where 0 is the first row in the
display
**Returns:** true if the node is currently collapsed, otherwise false

---

#### isCollapsed

public boolean isCollapsed​(int row)

Returns true if the node at the specified display row is collapsed.

makeVisible

```java
public void makeVisible​(
TreePath
path)
```

Ensures that the node identified by path is currently viewable.

**Parameters:** path

- the

TreePath

to make visible

---

#### makeVisible

public void makeVisible​(

TreePath

path)

Ensures that the node identified by path is currently viewable.

isVisible

```java
public boolean isVisible​(
TreePath
path)
```

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.
Otherwise, this method returns false.

**Parameters:** path

-

TreePath

identifying a node
**Returns:** true if the node is viewable, otherwise false

---

#### isVisible

public boolean isVisible​(

TreePath

path)

Returns true if the value identified by path is currently viewable,
which means it is either the root or all of its parents are expanded.
Otherwise, this method returns false.

getPathBounds

```java
public
Rectangle
getPathBounds​(
TreePath
path)
```

Returns the

Rectangle

that the specified node will be drawn
into. Returns

null

if any component in the path is hidden
(under a collapsed parent).

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

the node is drawn in,
or

null

---

#### getPathBounds

public

Rectangle

getPathBounds​(

TreePath

path)

Returns the

Rectangle

that the specified node will be drawn
into. Returns

null

if any component in the path is hidden
(under a collapsed parent).

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

Note:

This method returns a valid rectangle, even if the specified
node is not currently displayed.

getRowBounds

```java
public
Rectangle
getRowBounds​(int row)
```

Returns the

Rectangle

that the node at the specified row is
drawn in.

**Parameters:** row

- the row to be drawn, where 0 is the first row in the
display
**Returns:** the

Rectangle

the node is drawn in

---

#### getRowBounds

public

Rectangle

getRowBounds​(int row)

Returns the

Rectangle

that the node at the specified row is
drawn in.

scrollPathToVisible

```java
public void scrollPathToVisible​(
TreePath
path)
```

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** path

- the

TreePath

identifying the node to
bring into view

---

#### scrollPathToVisible

public void scrollPathToVisible​(

TreePath

path)

Makes sure all the path components in path are expanded (except
for the last path component) and scrolls so that the
node identified by the path is displayed. Only works when this

JTree

is contained in a

JScrollPane

.

scrollRowToVisible

```java
public void scrollRowToVisible​(int row)
```

Scrolls the item identified by row until it is displayed. The minimum
of amount of scrolling necessary to bring the row into view
is performed. Only works when this

JTree

is contained in a

JScrollPane

.

**Parameters:** row

- an integer specifying the row to scroll, where 0 is the
first row in the display

---

#### scrollRowToVisible

public void scrollRowToVisible​(int row)

Scrolls the item identified by row until it is displayed. The minimum
of amount of scrolling necessary to bring the row into view
is performed. Only works when this

JTree

is contained in a

JScrollPane

.

getPathForRow

```java
@BeanProperty
(
bound
=false)
public
TreePath
getPathForRow​(int row)
```

Returns the path for the specified row. If

row

is
not visible, or a

TreeUI

has not been set,

null

is returned.

**Parameters:** row

- an integer specifying a row
**Returns:** the

TreePath

to the specified node,

null

if

row < 0

or

row >= getRowCount()

---

#### getPathForRow

@BeanProperty

(

bound

=false)
public

TreePath

getPathForRow​(int row)

Returns the path for the specified row. If

row

is
not visible, or a

TreeUI

has not been set,

null

is returned.

getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that displays the node identified by the specified
path.

**Parameters:** path

- the

TreePath

identifying a node
**Returns:** an integer specifying the display row, where 0 is the first
row in the display, or -1 if any of the elements in path
are hidden under a collapsed parent.

---

#### getRowForPath

public int getRowForPath​(

TreePath

path)

Returns the row that displays the node identified by the specified
path.

expandPath

```java
public void expandPath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
expanded and viewable. If the last item in the path is a
leaf, this will have no effect.

**Parameters:** path

- the

TreePath

identifying a node

---

#### expandPath

public void expandPath​(

TreePath

path)

Ensures that the node identified by the specified path is
expanded and viewable. If the last item in the path is a
leaf, this will have no effect.

expandRow

```java
public void expandRow​(int row)
```

Ensures that the node in the specified row is expanded and
viewable.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

---

#### expandRow

public void expandRow​(int row)

Ensures that the node in the specified row is expanded and
viewable.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

collapsePath

```java
public void collapsePath​(
TreePath
path)
```

Ensures that the node identified by the specified path is
collapsed and viewable.

**Parameters:** path

- the

TreePath

identifying a node

---

#### collapsePath

public void collapsePath​(

TreePath

path)

Ensures that the node identified by the specified path is
collapsed and viewable.

collapseRow

```java
public void collapseRow​(int row)
```

Ensures that the node in the specified row is collapsed.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

**Parameters:** row

- an integer specifying a display row, where 0 is the
first row in the display

---

#### collapseRow

public void collapseRow​(int row)

Ensures that the node in the specified row is collapsed.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

If

row

is < 0 or >=

getRowCount

this
will have no effect.

getPathForLocation

```java
public
TreePath
getPathForLocation​(int x,
int y)
```

Returns the path for the node at the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node at that location

---

#### getPathForLocation

public

TreePath

getPathForLocation​(int x,
int y)

Returns the path for the node at the specified location.

getRowForLocation

```java
public int getRowForLocation​(int x,
int y)
```

Returns the row for the specified location.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row corresponding to the location, or -1 if the
location is not within the bounds of a displayed cell
**See Also:** getClosestRowForLocation(int, int)

---

#### getRowForLocation

public int getRowForLocation​(int x,
int y)

Returns the row for the specified location.

getClosestPathForLocation

```java
public
TreePath
getClosestPathForLocation​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
no nodes are currently viewable, or there is no model, returns

null

, otherwise it always returns a valid path. To test if
the node is exactly at x, y, get the node's bounds and
test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the

TreePath

for the node closest to that location,

null

if nothing is viewable or there is no model
**See Also:** getPathForLocation(int, int)

,

getPathBounds(javax.swing.tree.TreePath)

---

#### getClosestPathForLocation

public

TreePath

getClosestPathForLocation​(int x,
int y)

Returns the path to the node that is closest to x,y. If
no nodes are currently viewable, or there is no model, returns

null

, otherwise it always returns a valid path. To test if
the node is exactly at x, y, get the node's bounds and
test x, y against that.

getClosestRowForLocation

```java
public int getClosestRowForLocation​(int x,
int y)
```

Returns the row to the node that is closest to x,y. If no nodes
are viewable or there is no model, returns -1. Otherwise,
it always returns a valid row. To test if the returned object is
exactly at x, y, get the bounds for the node at the returned
row and test x, y against that.

**Parameters:** x

- an integer giving the number of pixels horizontally from
the left edge of the display area, minus any left margin
**Parameters:** y

- an integer giving the number of pixels vertically from
the top of the display area, minus any top margin
**Returns:** the row closest to the location, -1 if nothing is
viewable or there is no model
**See Also:** getRowForLocation(int, int)

,

getRowBounds(int)

---

#### getClosestRowForLocation

public int getClosestRowForLocation​(int x,
int y)

Returns the row to the node that is closest to x,y. If no nodes
are viewable or there is no model, returns -1. Otherwise,
it always returns a valid row. To test if the returned object is
exactly at x, y, get the bounds for the node at the returned
row and test x, y against that.

isEditing

```java
@BeanProperty
(
bound
=false)
public boolean isEditing()
```

Returns true if the tree is being edited. The item that is being
edited can be obtained using

getSelectionPath

.

**Returns:** true if the user is currently editing a node
**See Also:** getSelectionPath()

---

#### isEditing

@BeanProperty

(

bound

=false)
public boolean isEditing()

Returns true if the tree is being edited. The item that is being
edited can be obtained using

getSelectionPath

.

stopEditing

```java
public boolean stopEditing()
```

Ends the current editing session.
(The

DefaultTreeCellEditor

object saves any edits that are currently in progress on a cell.
Other implementations may operate differently.)
Has no effect if the tree isn't being edited.

Note:

To make edit-saves automatic whenever the user changes
their position in the tree, use

setInvokesStopCellEditing(boolean)

.

**Returns:** true if editing was in progress and is now stopped,
false if editing was not in progress

---

#### stopEditing

public boolean stopEditing()

Ends the current editing session.
(The

DefaultTreeCellEditor

object saves any edits that are currently in progress on a cell.
Other implementations may operate differently.)
Has no effect if the tree isn't being edited.

Note:

To make edit-saves automatic whenever the user changes
their position in the tree, use

setInvokesStopCellEditing(boolean)

.

cancelEditing

```java
public void cancelEditing()
```

Cancels the current editing session. Has no effect if the
tree isn't being edited.

---

#### cancelEditing

public void cancelEditing()

Cancels the current editing session. Has no effect if the
tree isn't being edited.

startEditingAtPath

```java
public void startEditingAtPath​(
TreePath
path)
```

Selects the node identified by the specified path and initiates
editing. The edit-attempt fails if the

CellEditor

does not allow
editing for the specified item.

**Parameters:** path

- the

TreePath

identifying a node

---

#### startEditingAtPath

public void startEditingAtPath​(

TreePath

path)

Selects the node identified by the specified path and initiates
editing. The edit-attempt fails if the

CellEditor

does not allow
editing for the specified item.

getEditingPath

```java
@BeanProperty
(
bound
=false)
public
TreePath
getEditingPath()
```

Returns the path to the element that is currently being edited.

**Returns:** the

TreePath

for the node being edited

---

#### getEditingPath

@BeanProperty

(

bound

=false)
public

TreePath

getEditingPath()

Returns the path to the element that is currently being edited.

setSelectionModel

```java
@BeanProperty
(
description
="The tree\'s selection model.")
public void setSelectionModel​(
TreeSelectionModel
selectionModel)
```

Sets the tree's selection model. When a

null

value is
specified an empty

selectionModel

is used, which does not allow selections.

This is a bound property.

**Parameters:** selectionModel

- the

TreeSelectionModel

to use,
or

null

to disable selections
**See Also:** TreeSelectionModel

---

#### setSelectionModel

@BeanProperty

(

description

="The tree\'s selection model.")
public void setSelectionModel​(

TreeSelectionModel

selectionModel)

Sets the tree's selection model. When a

null

value is
specified an empty

selectionModel

is used, which does not allow selections.

This is a bound property.

This is a bound property.

getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model for selections. This should always return a
non-

null

value. If you don't want to allow anything
to be selected
set the selection model to

null

, which forces an empty
selection model to be used.

**Returns:** the model for selections
**See Also:** setSelectionModel(javax.swing.tree.TreeSelectionModel)

---

#### getSelectionModel

public

TreeSelectionModel

getSelectionModel()

Returns the model for selections. This should always return a
non-

null

value. If you don't want to allow anything
to be selected
set the selection model to

null

, which forces an empty
selection model to be used.

getPathBetweenRows

```java
protected
TreePath
[] getPathBetweenRows​(int index0,
int index1)
```

Returns the paths (inclusive) between the specified rows. If
the specified indices are within the viewable set of rows, or
bound the viewable set of rows, then the indices are
constrained by the viewable set of rows. If the specified
indices are not within the viewable set of rows, or do not
bound the viewable set of rows, then an empty array is
returned. For example, if the row count is

10

, and this
method is invoked with

-1, 20

, then the specified
indices are constrained to the viewable set of rows, and this is
treated as if invoked with

0, 9

. On the other hand, if
this were invoked with

-10, -1

, then the specified
indices do not bound the viewable set of rows, and an empty
array is returned.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

**Parameters:** index0

- the first index in the range
**Parameters:** index1

- the last index in the range
**Returns:** the paths (inclusive) between the specified row indices

---

#### getPathBetweenRows

protected

TreePath

[] getPathBetweenRows​(int index0,
int index1)

Returns the paths (inclusive) between the specified rows. If
the specified indices are within the viewable set of rows, or
bound the viewable set of rows, then the indices are
constrained by the viewable set of rows. If the specified
indices are not within the viewable set of rows, or do not
bound the viewable set of rows, then an empty array is
returned. For example, if the row count is

10

, and this
method is invoked with

-1, 20

, then the specified
indices are constrained to the viewable set of rows, and this is
treated as if invoked with

0, 9

. On the other hand, if
this were invoked with

-10, -1

, then the specified
indices do not bound the viewable set of rows, and an empty
array is returned.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

The parameters are not order dependent. That is,

getPathBetweenRows(x, y)

is equivalent to

getPathBetweenRows(y, x)

.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

An empty array is returned if the row count is

0

, or
the specified indices do not bound the viewable set of rows.

setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Selects the rows in the specified interval (inclusive). If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified rows are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is cleared. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified indices bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified indices do not
bound the viewable set of rows, and the selection is cleared.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to select
**Parameters:** index1

- the last index in the range to select

---

#### setSelectionInterval

public void setSelectionInterval​(int index0,
int index1)

Selects the rows in the specified interval (inclusive). If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified rows are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is cleared. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified indices bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified indices do not
bound the viewable set of rows, and the selection is cleared.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

The parameters are not order dependent. That is,

setSelectionInterval(x, y)

is equivalent to

setSelectionInterval(y, x)

.

addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Adds the specified rows (inclusive) to the selection. If the
specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are
constrained by the viewable set of rows. If the indices are not
within the viewable set of rows, or do not bound the viewable
set of rows, then the selection is unchanged. For example, if
the row count is

10

, and this method is invoked with

-1, 20

, then the specified indices bounds the viewable
range, and this is treated as if invoked with

0, 9

. On
the other hand, if this were invoked with

-10, -1

, then
the specified indices do not bound the viewable set of rows,
and the selection is unchanged.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

**Parameters:** index0

- the first index in the range to add to the selection
**Parameters:** index1

- the last index in the range to add to the selection

---

#### addSelectionInterval

public void addSelectionInterval​(int index0,
int index1)

Adds the specified rows (inclusive) to the selection. If the
specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are
constrained by the viewable set of rows. If the indices are not
within the viewable set of rows, or do not bound the viewable
set of rows, then the selection is unchanged. For example, if
the row count is

10

, and this method is invoked with

-1, 20

, then the specified indices bounds the viewable
range, and this is treated as if invoked with

0, 9

. On
the other hand, if this were invoked with

-10, -1

, then
the specified indices do not bound the viewable set of rows,
and the selection is unchanged.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

The parameters are not order dependent. That is,

addSelectionInterval(x, y)

is equivalent to

addSelectionInterval(y, x)

.

removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Removes the specified rows (inclusive) from the selection. If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is unchanged. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified range bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified range does not
bound the viewable set of rows, and the selection is unchanged.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

**Parameters:** index0

- the first row to remove from the selection
**Parameters:** index1

- the last row to remove from the selection

---

#### removeSelectionInterval

public void removeSelectionInterval​(int index0,
int index1)

Removes the specified rows (inclusive) from the selection. If
the specified indices are within the viewable set of rows, or bound
the viewable set of rows, then the specified indices are constrained by
the viewable set of rows. If the specified indices are not within the
viewable set of rows, or do not bound the viewable set of rows, then
the selection is unchanged. For example, if the row count is

10

, and this method is invoked with

-1, 20

, then the
specified range bounds the viewable range, and this is treated as
if invoked with

0, 9

. On the other hand, if this were
invoked with

-10, -1

, then the specified range does not
bound the viewable set of rows, and the selection is unchanged.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

The parameters are not order dependent. That is,

removeSelectionInterval(x, y)

is equivalent to

removeSelectionInterval(y, x)

.

removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes the node identified by the specified path from the current
selection.

**Parameters:** path

- the

TreePath

identifying a node

---

#### removeSelectionPath

public void removeSelectionPath​(

TreePath

path)

Removes the node identified by the specified path from the current
selection.

removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes the nodes identified by the specified paths from the
current selection.

**Parameters:** paths

- an array of

TreePath

objects that
specifies the nodes to remove

---

#### removeSelectionPaths

public void removeSelectionPaths​(

TreePath

[] paths)

Removes the nodes identified by the specified paths from the
current selection.

removeSelectionRow

```java
public void removeSelectionRow​(int row)
```

Removes the row at the index

row

from the current
selection.

**Parameters:** row

- the row to remove

---

#### removeSelectionRow

public void removeSelectionRow​(int row)

Removes the row at the index

row

from the current
selection.

removeSelectionRows

```java
public void removeSelectionRows​(int[] rows)
```

Removes the rows that are selected at each of the specified
rows.

**Parameters:** rows

- an array of ints specifying display rows, where 0 is
the first row in the display

---

#### removeSelectionRows

public void removeSelectionRows​(int[] rows)

Removes the rows that are selected at each of the specified
rows.

clearSelection

```java
public void clearSelection()
```

Clears the selection.

---

#### clearSelection

public void clearSelection()

Clears the selection.

isSelectionEmpty

```java
@BeanProperty
(
bound
=false)
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** true if the selection is currently empty

---

#### isSelectionEmpty

@BeanProperty

(

bound

=false)
public boolean isSelectionEmpty()

Returns true if the selection is currently empty.

addTreeExpansionListener

```java
public void addTreeExpansionListener​(
TreeExpansionListener
tel)
```

Adds a listener for

TreeExpansion

events.

**Parameters:** tel

- a TreeExpansionListener that will be notified when
a tree node is expanded or collapsed (a "negative
expansion")

---

#### addTreeExpansionListener

public void addTreeExpansionListener​(

TreeExpansionListener

tel)

Adds a listener for

TreeExpansion

events.

removeTreeExpansionListener

```java
public void removeTreeExpansionListener​(
TreeExpansionListener
tel)
```

Removes a listener for

TreeExpansion

events.

**Parameters:** tel

- the

TreeExpansionListener

to remove

---

#### removeTreeExpansionListener

public void removeTreeExpansionListener​(

TreeExpansionListener

tel)

Removes a listener for

TreeExpansion

events.

getTreeExpansionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeExpansionListener
[] getTreeExpansionListeners()
```

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

**Returns:** all of the

TreeExpansionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getTreeExpansionListeners

@BeanProperty

(

bound

=false)
public

TreeExpansionListener

[] getTreeExpansionListeners()

Returns an array of all the

TreeExpansionListener

s added
to this JTree with addTreeExpansionListener().

addTreeWillExpandListener

```java
public void addTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Adds a listener for

TreeWillExpand

events.

**Parameters:** tel

- a

TreeWillExpandListener

that will be notified
when a tree node will be expanded or collapsed (a "negative
expansion")

---

#### addTreeWillExpandListener

public void addTreeWillExpandListener​(

TreeWillExpandListener

tel)

Adds a listener for

TreeWillExpand

events.

removeTreeWillExpandListener

```java
public void removeTreeWillExpandListener​(
TreeWillExpandListener
tel)
```

Removes a listener for

TreeWillExpand

events.

**Parameters:** tel

- the

TreeWillExpandListener

to remove

---

#### removeTreeWillExpandListener

public void removeTreeWillExpandListener​(

TreeWillExpandListener

tel)

Removes a listener for

TreeWillExpand

events.

getTreeWillExpandListeners

```java
@BeanProperty
(
bound
=false)
public
TreeWillExpandListener
[] getTreeWillExpandListeners()
```

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

**Returns:** all of the

TreeWillExpandListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getTreeWillExpandListeners

@BeanProperty

(

bound

=false)
public

TreeWillExpandListener

[] getTreeWillExpandListeners()

Returns an array of all the

TreeWillExpandListener

s added
to this JTree with addTreeWillExpandListener().

fireTreeExpanded

```java
public void fireTreeExpanded​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**See Also:** EventListenerList

---

#### fireTreeExpanded

public void fireTreeExpanded​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

fireTreeCollapsed

```java
public void fireTreeCollapsed​(
TreePath
path)
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
collapsed
**See Also:** EventListenerList

---

#### fireTreeCollapsed

public void fireTreeCollapsed​(

TreePath

path)

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

fireTreeWillExpand

```java
public void fireTreeWillExpand​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the expansion is prevented from occurring
**See Also:** EventListenerList

---

#### fireTreeWillExpand

public void fireTreeWillExpand​(

TreePath

path)
throws

ExpandVetoException

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

fireTreeWillCollapse

```java
public void fireTreeWillCollapse​(
TreePath
path)
throws
ExpandVetoException
```

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

**Parameters:** path

- the

TreePath

indicating the node that was
expanded
**Throws:** ExpandVetoException

- if the collapse is prevented from occurring
**See Also:** EventListenerList

---

#### fireTreeWillCollapse

public void fireTreeWillCollapse​(

TreePath

path)
throws

ExpandVetoException

Notifies all listeners that have registered interest for
notification on this event type. The event instance
is lazily created using the

path

parameter.

addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Adds a listener for

TreeSelection

events.

**Parameters:** tsl

- the

TreeSelectionListener

that will be notified
when a node is selected or deselected (a "negative
selection")

---

#### addTreeSelectionListener

public void addTreeSelectionListener​(

TreeSelectionListener

tsl)

Adds a listener for

TreeSelection

events.

removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
tsl)
```

Removes a

TreeSelection

listener.

**Parameters:** tsl

- the

TreeSelectionListener

to remove

---

#### removeTreeSelectionListener

public void removeTreeSelectionListener​(

TreeSelectionListener

tsl)

Removes a

TreeSelection

listener.

getTreeSelectionListeners

```java
@BeanProperty
(
bound
=false)
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

**Returns:** all of the

TreeSelectionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getTreeSelectionListeners

@BeanProperty

(

bound

=false)
public

TreeSelectionListener

[] getTreeSelectionListeners()

Returns an array of all the

TreeSelectionListener

s added
to this JTree with addTreeSelectionListener().

fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the

TreeSelectionEvent

to be fired;
generated by the

TreeSelectionModel

when a node is selected or deselected
**See Also:** EventListenerList

---

#### fireValueChanged

protected void fireValueChanged​(

TreeSelectionEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

treeDidChange

```java
public void treeDidChange()
```

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree). You should never have to
invoke this, the UI will invoke this as it needs to.

---

#### treeDidChange

public void treeDidChange()

Sent when the tree has changed enough that we need to resize
the bounds, but not enough that we need to remove the
expanded node set (e.g nodes were expanded or collapsed, or
nodes were inserted into the tree). You should never have to
invoke this, the UI will invoke this as it needs to.

setVisibleRowCount

```java
@BeanProperty
(
description
="The number of rows that are to be displayed.")
public void setVisibleRowCount​(int newCount)
```

Sets the number of rows that are to be displayed.
This will only work if the tree is contained in a

JScrollPane

,
and will adjust the preferred size and size of that scrollpane.

This is a bound property.

**Parameters:** newCount

- the number of rows to display

---

#### setVisibleRowCount

@BeanProperty

(

description

="The number of rows that are to be displayed.")
public void setVisibleRowCount​(int newCount)

Sets the number of rows that are to be displayed.
This will only work if the tree is contained in a

JScrollPane

,
and will adjust the preferred size and size of that scrollpane.

This is a bound property.

This is a bound property.

getVisibleRowCount

```java
public int getVisibleRowCount()
```

Returns the number of rows that are displayed in the display area.

**Returns:** the number of rows displayed

---

#### getVisibleRowCount

public int getVisibleRowCount()

Returns the number of rows that are displayed in the display area.

getNextMatch

```java
public
TreePath
getNextMatch​(
String
prefix,
int startingRow,

Position.Bias
bias)
```

Returns the TreePath to the next tree element that
begins with a prefix. To handle the conversion of a

TreePath

into a String,

convertValueToText

is used.

**Parameters:** prefix

- the string to test for a match
**Parameters:** startingRow

- the row for starting the search
**Parameters:** bias

- the search direction, either
Position.Bias.Forward or Position.Bias.Backward.
**Returns:** the TreePath of the next tree element that
starts with the prefix; otherwise null
**Throws:** IllegalArgumentException

- if prefix is null
or startingRow is out of bounds
**Since:** 1.4

---

#### getNextMatch

public

TreePath

getNextMatch​(

String

prefix,
int startingRow,

Position.Bias

bias)

Returns the TreePath to the next tree element that
begins with a prefix. To handle the conversion of a

TreePath

into a String,

convertValueToText

is used.

getPreferredScrollableViewportSize

```java
@BeanProperty
(
bound
=false)
public
Dimension
getPreferredScrollableViewportSize()
```

Returns the preferred display size of a

JTree

. The height is
determined from

getVisibleRowCount

and the width
is the current preferred width.

**Specified by:** getPreferredScrollableViewportSize

in interface

Scrollable
**Returns:** a

Dimension

object containing the preferred size
**See Also:** JComponent.getPreferredSize()

---

#### getPreferredScrollableViewportSize

@BeanProperty

(

bound

=false)
public

Dimension

getPreferredScrollableViewportSize()

Returns the preferred display size of a

JTree

. The height is
determined from

getVisibleRowCount

and the width
is the current preferred width.

getScrollableUnitIncrement

```java
public int getScrollableUnitIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount to increment when scrolling. The amount is
the height of the first displayed row that isn't completely in view
or, if it is totally displayed, the height of the next row in the
scrolling direction.

**Specified by:** getScrollableUnitIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right
**Returns:** the "unit" increment for scrolling in the specified direction
**See Also:** JScrollBar.setUnitIncrement(int)

---

#### getScrollableUnitIncrement

public int getScrollableUnitIncrement​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount to increment when scrolling. The amount is
the height of the first displayed row that isn't completely in view
or, if it is totally displayed, the height of the next row in the
scrolling direction.

getScrollableBlockIncrement

```java
public int getScrollableBlockIncrement​(
Rectangle
visibleRect,
int orientation,
int direction)
```

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

**Specified by:** getScrollableBlockIncrement

in interface

Scrollable
**Parameters:** visibleRect

- the view area visible within the viewport
**Parameters:** orientation

- either

SwingConstants.VERTICAL

or

SwingConstants.HORIZONTAL
**Parameters:** direction

- less than zero to scroll up/left,
greater than zero for down/right.
**Returns:** the "block" increment for scrolling in the specified direction
**See Also:** JScrollBar.setBlockIncrement(int)

---

#### getScrollableBlockIncrement

public int getScrollableBlockIncrement​(

Rectangle

visibleRect,
int orientation,
int direction)

Returns the amount for a block increment, which is the height or
width of

visibleRect

, based on

orientation

.

getScrollableTracksViewportWidth

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportWidth()
```

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportWidth

in interface

Scrollable
**Returns:** whether the tree should track the width of the viewport
**See Also:** Scrollable.getScrollableTracksViewportWidth()

---

#### getScrollableTracksViewportWidth

@BeanProperty

(

bound

=false)
public boolean getScrollableTracksViewportWidth()

Returns false to indicate that the width of the viewport does not
determine the width of the table, unless the preferred width of
the tree is smaller than the viewports width. In other words:
ensure that the tree is never smaller than its viewport.

getScrollableTracksViewportHeight

```java
@BeanProperty
(
bound
=false)
public boolean getScrollableTracksViewportHeight()
```

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height. In other words:
ensure that the tree is never smaller than its viewport.

**Specified by:** getScrollableTracksViewportHeight

in interface

Scrollable
**Returns:** whether the tree should track the height of the viewport
**See Also:** Scrollable.getScrollableTracksViewportHeight()

---

#### getScrollableTracksViewportHeight

@BeanProperty

(

bound

=false)
public boolean getScrollableTracksViewportHeight()

Returns false to indicate that the height of the viewport does not
determine the height of the table, unless the preferred height
of the tree is smaller than the viewports height. In other words:
ensure that the tree is never smaller than its viewport.

setExpandedState

```java
protected void setExpandedState​(
TreePath
path,
boolean state)
```

Sets the expanded state of this

JTree

.
If

state

is
true, all parents of

path

and path are marked as
expanded. If

state

is false, all parents of

path

are marked EXPANDED, but

path

itself
is marked collapsed.

This will fail if a

TreeWillExpandListener

vetos it.

**Parameters:** path

- a

TreePath

identifying a node
**Parameters:** state

- if

true

, all parents of @{code path} and path are marked as expanded.
Otherwise, all parents of

path

are marked EXPANDED,
but

path

itself is marked collapsed.

---

#### setExpandedState

protected void setExpandedState​(

TreePath

path,
boolean state)

Sets the expanded state of this

JTree

.
If

state

is
true, all parents of

path

and path are marked as
expanded. If

state

is false, all parents of

path

are marked EXPANDED, but

path

itself
is marked collapsed.

This will fail if a

TreeWillExpandListener

vetos it.

This will fail if a

TreeWillExpandListener

vetos it.

getDescendantToggledPaths

```java
protected
Enumeration
<
TreePath
> getDescendantToggledPaths​(
TreePath
parent)
```

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

**Parameters:** parent

- a path
**Returns:** the

Enumeration

of

TreePaths

---

#### getDescendantToggledPaths

protected

Enumeration

<

TreePath

> getDescendantToggledPaths​(

TreePath

parent)

Returns an

Enumeration

of

TreePaths

that have been expanded that
are descendants of

parent

.

removeDescendantToggledPaths

```java
protected void removeDescendantToggledPaths​(
Enumeration
<
TreePath
> toRemove)
```

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

**Parameters:** toRemove

- an enumeration of the paths to remove; a value of

null

is ignored
**Throws:** ClassCastException

- if

toRemove

contains an
element that is not a

TreePath

;

null

values are ignored

---

#### removeDescendantToggledPaths

protected void removeDescendantToggledPaths​(

Enumeration

<

TreePath

> toRemove)

Removes any descendants of the

TreePaths

in

toRemove

that have been expanded.

clearToggledPaths

```java
protected void clearToggledPaths()
```

Clears the cache of toggled tree paths. This does NOT send out
any

TreeExpansionListener

events.

---

#### clearToggledPaths

protected void clearToggledPaths()

Clears the cache of toggled tree paths. This does NOT send out
any

TreeExpansionListener

events.

createTreeModelListener

```java
protected
TreeModelListener
createTreeModelListener()
```

Creates and returns an instance of

TreeModelHandler

.
The returned
object is responsible for updating the expanded state when the

TreeModel

changes.

For more information on what expanded state means, see the

JTree description

above.

**Returns:** the instance of

TreeModelHandler

---

#### createTreeModelListener

protected

TreeModelListener

createTreeModelListener()

Creates and returns an instance of

TreeModelHandler

.
The returned
object is responsible for updating the expanded state when the

TreeModel

changes.

For more information on what expanded state means, see the

JTree description

above.

For more information on what expanded state means, see the

JTree description

above.

removeDescendantSelectedPaths

```java
protected boolean removeDescendantSelectedPaths​(
TreePath
path,
boolean includePath)
```

Removes any paths in the selection that are descendants of

path

. If

includePath

is true and

path

is selected, it will be removed from the selection.

**Parameters:** path

- a path
**Parameters:** includePath

- is

true

and

path

is selected,
it will be removed from the selection.
**Returns:** true if a descendant was selected
**Since:** 1.3

---

#### removeDescendantSelectedPaths

protected boolean removeDescendantSelectedPaths​(

TreePath

path,
boolean includePath)

Removes any paths in the selection that are descendants of

path

. If

includePath

is true and

path

is selected, it will be removed from the selection.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTree

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTree

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JTree

.
This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

getAccessibleContext

```java
@BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTree.
For JTrees, the AccessibleContext takes the form of an
AccessibleJTree.
A new AccessibleJTree instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTree that serves as the
AccessibleContext of this JTree

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JTree.
For JTrees, the AccessibleContext takes the form of an
AccessibleJTree.
A new AccessibleJTree instance is created if necessary.

---

